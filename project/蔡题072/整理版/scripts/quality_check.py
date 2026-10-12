from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
BUILD = ROOT / "build"

NAMES = ["蔡题072_试卷", "蔡题072_学生详解", "蔡题072_教师备课"]
FORBIDDEN = [
    "手写答案", "手写解答", "数字化重构", "完成本题",
    "继续下一题", "原卷图", "参考文件", "高一新生知识台阶",
    "教练引导话术",
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
        assert not re.search(r"(?m)^#{3,}\s", text), name
        for phrase in FORBIDDEN:
            assert phrase not in text, (name, phrase)
        for target in re.findall(r"!\[[^]]*]\(([^)]+\.png)\)", text):
            image = (MD / target).resolve()
            assert image.exists(), image
            assert image.with_suffix(".pdf").exists(), image.with_suffix(".pdf")

    teacher = texts["蔡题072_教师备课"]
    for heading in REQUIRED_SECTIONS:
        count = len(re.findall(rf"(?m)^## {re.escape(heading)}$", teacher))
        assert count == 8, (heading, count)

    paper = texts["蔡题072_试卷"]
    assert not re.search(r"(?m)^## ", paper)


def check_pdfs() -> None:
    for name in NAMES:
        pdf = BUILD / f"{name}.pdf"
        assert pdf.exists() and pdf.stat().st_size > 10_000, pdf
        command("qpdf", "--check", str(pdf))
        with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
            command("pdftotext", str(pdf), tmp.name)
            text = Path(tmp.name).read_text(encoding="utf-8")
        assert "\ufffd" not in text, pdf
        first = re.sub(r"\s+", "", text[:500])
        assert "第072套" in first, (pdf, text[:500])


def main() -> None:
    check_markdown()
    check_pdfs()
    print("PASS markdown structure, forbidden phrases, figure paths")
    print("PASS qpdf integrity and extractable PDF text")


if __name__ == "__main__":
    main()
