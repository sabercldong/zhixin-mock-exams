from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
BUILD = ROOT / "build"
OUTPUT = ROOT / "output" / "pdf"

NAMES = ["蔡题073_试卷", "蔡题073_学生详解", "蔡题073_教师备课"]
FORBIDDEN = [
    "手写答案", "手写解答", "数字化重构", "完成本题",
    "继续下一题", "原卷图", "参考文件", "高一新生知识台阶",
    "教练引导话术", "更正版特别指出", "普通答案",
]
REQUIRED_SECTIONS = [
    "一、题型定位", "二、知识点", "三、物理图像", "四、解题入口",
    "五、解析", "六、关键洞察", "七、易错点", "八、课堂讲解建议",
    "九、变式训练",
]


def command(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True,
                            text=True, capture_output=True)
    return result.stdout + result.stderr


def check_markdown() -> None:
    texts: dict[str, str] = {}
    for name in NAMES:
        path = MD / f"{name}.md"
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        questions = re.findall(r"(?m)^# 第 ([1-8]) 题$", text)
        assert questions == list("12345678"), (name, questions)
        assert "\ufffd" not in text
        assert "\x0c" not in text
        assert not re.search(r"(?m)^#{3,}\s", text), name
        for phrase in FORBIDDEN:
            assert phrase not in text, (name, phrase)
        for target in re.findall(r"!\[[^]]*]\(([^)]+\.png)\)", text):
            image = (MD / target).resolve()
            assert image.exists(), image
            assert image.with_suffix(".pdf").exists(), image.with_suffix(".pdf")

    teacher = texts["蔡题073_教师备课"]
    for heading in REQUIRED_SECTIONS:
        count = len(re.findall(rf"(?m)^## {re.escape(heading)}$", teacher))
        assert count == 8, (heading, count)

    student = texts["蔡题073_学生详解"]
    for heading in REQUIRED_SECTIONS[:5]:
        count = len(re.findall(rf"(?m)^## {re.escape(heading)}$", student))
        assert count == 8, (heading, count)
    for heading in REQUIRED_SECTIONS[5:]:
        assert heading not in student, heading

    paper = texts["蔡题073_试卷"]
    assert not re.search(r"(?m)^## ", paper)


def check_pdfs() -> None:
    page_minimums = {
        "蔡题073_试卷": 8,
        "蔡题073_学生详解": 40,
        "蔡题073_教师备课": 65,
    }
    for name in NAMES:
        pdf = OUTPUT / f"{name}.pdf"
        assert pdf.exists() and pdf.stat().st_size > 10_000, pdf
        command("qpdf", "--check", str(pdf))
        info = command("pdfinfo", str(pdf))
        pages_match = re.search(r"(?m)^Pages:\s+(\d+)$", info)
        assert pages_match, info
        pages = int(pages_match.group(1))
        assert pages >= page_minimums[name], (name, pages)
        with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
            command("pdftotext", str(pdf), tmp.name)
            text = Path(tmp.name).read_text(encoding="utf-8")
        assert "\ufffd" not in text, pdf
        first = re.sub(r"\s+", "", text[:500])
        assert "第073套" in first, (pdf, text[:500])


def check_logs() -> None:
    bad = re.compile(
        r"(?m)^!|Overfull|Missing character|Undefined control|"
        r"Emergency stop|Fatal error"
    )
    for log in BUILD.glob("*.log"):
        text = log.read_text(encoding="utf-8", errors="replace")
        assert not bad.search(text), log


def main() -> None:
    check_markdown()
    check_pdfs()
    check_logs()
    print("PASS markdown structure, headings, forbidden phrases, figure paths")
    print("PASS page-depth thresholds, qpdf integrity, extractable PDF text")
    print("PASS TeX logs contain no targeted errors or overfull boxes")


if __name__ == "__main__":
    main()
