from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
BUILD = ROOT / "build"
OUTPUT = ROOT / "output"
FIGURE_SOURCE = ROOT / "figures" / "蔡题067_图稿源文件.tex"

NAMES = ["蔡题067_试卷", "蔡题067_学生详解", "蔡题067_教师备课"]
FORBIDDEN = [
    "手写答案", "手写解答", "数字化重构", "完成本题", "继续下一题",
    "原卷图", "参考文件", "高一新生知识台阶", "教练引导话术",
]
REQUIRED_SECTIONS = [
    "一、题型定位", "二、知识点", "三、物理图像", "四、解题入口",
    "五、解析", "六、关键洞察", "七、易错点", "八、课堂讲解建议",
    "九、变式训练",
]


def command(*args: str) -> str:
    result = subprocess.run(
        args, cwd=ROOT, check=True, text=True, capture_output=True
    )
    return result.stdout + result.stderr


def question_block(text: str, number: int) -> str:
    start = text.split(f"# 第 {number} 题", 1)[1]
    if number < 8:
        return start.split(f"# 第 {number + 1} 题", 1)[0]
    return start


def check_markdown() -> None:
    texts: dict[str, str] = {}
    for name in NAMES:
        path = MD / f"{name}.md"
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        questions = re.findall(r"(?m)^# 第 ([1-8]) 题$", text)
        assert questions == list("12345678"), (name, questions)
        assert "\ufffd" not in text and "\x0c" not in text
        assert not re.search(r"(?m)^#{3,}\s", text), name
        for phrase in FORBIDDEN:
            assert phrase not in text, (name, phrase)
        for target in re.findall(r"!\[[^]]*]\(([^)]+\.png)\)", text):
            image = (MD / target).resolve()
            assert image.exists(), image
            assert image.with_suffix(".pdf").exists(), image.with_suffix(".pdf")

        q7 = question_block(text, 7)
        assert r"P(z)=P_0(1-bz)^\lambda" in q7, name
        assert r"\gamma" not in q7, name

    teacher = texts["蔡题067_教师备课"]
    for heading in REQUIRED_SECTIONS:
        assert len(re.findall(rf"(?m)^## {re.escape(heading)}$", teacher)) == 8, heading

    student = texts["蔡题067_学生详解"]
    for heading in REQUIRED_SECTIONS[:5]:
        assert len(re.findall(rf"(?m)^## {re.escape(heading)}$", student)) == 8, heading
    for heading in REQUIRED_SECTIONS[5:]:
        assert heading not in student, heading

    assert not re.search(r"(?m)^## ", texts["蔡题067_试卷"])


def check_figure_source() -> None:
    source = FIGURE_SOURCE.read_text(encoding="utf-8")
    q2 = source.split("% q2", 1)[1].split("% s2", 1)[0]
    s2 = source.split("% s2", 1)[1].split("% q3", 1)[0]
    q7 = source.split("% q7", 1)[1].split("% s7", 1)[0]
    s7 = source.split("% s7", 1)[1].split("% q8", 1)[0]
    assert "镜像" not in q2 and "+q_1" not in q2 and "-q_2" not in q2
    assert "镜像电荷构型" in s2
    for leaked in ("P(z)A", "\\rho gA", "Mg", "\\rho_{\\rm out}"):
        assert leaked not in q7, leaked
    for required in ("P(z)A", "\\rho gA", "Mg", "\\rho_{\\rm out}"):
        assert required in s7, required
    assert r"\lambda-1" in s7 and r"1-\lambda" in s7


def check_pdfs() -> None:
    page_minimums = {
        "蔡题067_试卷": 8,
        "蔡题067_学生详解": 40,
        "蔡题067_教师备课": 65,
    }
    for name in NAMES:
        pdf = OUTPUT / f"{name}.pdf"
        assert pdf.exists() and pdf.stat().st_size > 10_000, pdf
        command("qpdf", "--check", str(pdf))
        info = command("pdfinfo", str(pdf))
        match = re.search(r"(?m)^Pages:\s+(\d+)$", info)
        assert match, info
        pages = int(match.group(1))
        assert pages >= page_minimums[name], (name, pages)
        with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
            command("pdftotext", str(pdf), tmp.name)
            text = Path(tmp.name).read_text(encoding="utf-8")
        assert "\ufffd" not in text, pdf
        assert "第067套" in re.sub(r"\s+", "", text[:500]), pdf


def check_logs() -> None:
    bad = re.compile(
        r"(?m)^!|Overfull|Missing character|Undefined control|"
        r"Emergency stop|Fatal error"
    )
    for log in BUILD.glob("*.log"):
        assert not bad.search(log.read_text(encoding="utf-8", errors="replace")), log


def main() -> None:
    check_markdown()
    check_figure_source()
    check_pdfs()
    check_logs()
    print("PASS markdown structure, headings, forbidden phrases, and figure paths")
    print("PASS Q2 question/solution separation and Q7 symbol consistency")
    print("PASS page thresholds, qpdf integrity, extractable text, and TeX logs")


if __name__ == "__main__":
    main()
