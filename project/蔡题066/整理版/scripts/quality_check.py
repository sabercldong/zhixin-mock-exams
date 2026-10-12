from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
BUILD = ROOT / "build"
OUTPUT = ROOT / "output"
FIGURE_SOURCE = ROOT / "figures" / "蔡题066_图稿源文件.tex"
NAMES = ["蔡题066_试卷", "蔡题066_学生详解", "蔡题066_教师备课"]
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
    block = text.split(f"# 第 {number} 题", 1)[1]
    return block.split(f"# 第 {number + 1} 题", 1)[0] if number < 8 else block


def check_markdown() -> None:
    texts: dict[str, str] = {}
    for name in NAMES:
        path = MD / f"{name}.md"
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        assert re.findall(r"(?m)^# 第 ([1-8]) 题$", text) == list("12345678"), name
        assert "\ufffd" not in text and "\x0c" not in text
        assert not re.search(r"(?m)^#{3,}\s", text), name
        for phrase in FORBIDDEN:
            assert phrase not in text, (name, phrase)
        for target in re.findall(r"!\[[^]]*]\(([^)]+\.png)\)", text):
            image = (MD / target).resolve()
            assert image.exists(), image
            assert image.with_suffix(".pdf").exists(), image.with_suffix(".pdf")

        q2 = question_block(text, 2)
        assert r"\frac1n\sim\frac43\pi a^3" in q2, name
        prompt = q2.split("## 一、题型定位", 1)[0]
        assert r"f=\frac43\pi n a^3\ll1" not in prompt, name
        assert "已知体积分数" not in prompt, name
        q5 = question_block(text, 5)
        assert "思考题（不计分）" in q5 and r"\mathrm{CH_3D}" in q5, name

    teacher = texts["蔡题066_教师备课"]
    for heading in REQUIRED_SECTIONS:
        assert len(re.findall(rf"(?m)^## {re.escape(heading)}$", teacher)) == 8, heading
    assert "**（六）同位素思考题**" in teacher

    student = texts["蔡题066_学生详解"]
    for heading in REQUIRED_SECTIONS[:5]:
        assert len(re.findall(rf"(?m)^## {re.escape(heading)}$", student)) == 8, heading
    for heading in REQUIRED_SECTIONS[5:]:
        assert heading not in student, heading
    assert "**（六）同位素思考题**" in student
    assert not re.search(r"(?m)^## ", texts["蔡题066_试卷"])


def source_block(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def check_figure_source() -> None:
    source = FIGURE_SOURCE.read_text(encoding="utf-8")
    q1 = source_block(source, "% question-01", "% solution-01")
    s1 = source_block(source, "% solution-01", "% question-02")
    q2 = source_block(source, "% question-02", "% solution-02")
    s3 = source_block(source, "% solution-03", "% question-04")
    s4 = source_block(source, "% solution-04", "% question-05")
    q8 = source_block(source, "% question-08", "% solution-08")
    assert r"(1.3,4)--(1.3,-1.6)" in q1
    assert r"(.42,.8)--(.42,2.2)" in s1
    assert r"\bm p_0" not in q2 and r"f\ll1" not in q2
    assert r"n^{-1}\sim \dfrac43\pi a^3" in q2
    assert "fill=white" in s3 and "fill=white" in s4
    assert q8.count("{$m$}") >= 2 and "{$l/2$}" in q8
    assert q8.count("{$\\omega$}") >= 2
    for number in range(1, 9):
        for prefix in ("question", "solution"):
            stem = ROOT / "figures" / f"{prefix}-{number:02d}"
            assert stem.with_suffix(".png").exists(), stem
            assert stem.with_suffix(".pdf").exists(), stem


def check_pdfs() -> None:
    minimums = {
        "蔡题066_试卷": 8,
        "蔡题066_学生详解": 40,
        "蔡题066_教师备课": 65,
    }
    for name in NAMES:
        pdf = OUTPUT / f"{name}.pdf"
        assert pdf.exists() and pdf.stat().st_size > 10_000, pdf
        command("qpdf", "--check", str(pdf))
        info = command("pdfinfo", str(pdf))
        match = re.search(r"(?m)^Pages:\s+(\d+)$", info)
        assert match and int(match.group(1)) >= minimums[name], (name, info)
        with tempfile.NamedTemporaryFile(suffix=".txt") as tmp:
            command("pdftotext", str(pdf), tmp.name)
            text = Path(tmp.name).read_text(encoding="utf-8")
        assert "\ufffd" not in text, pdf
        assert "第066套" in re.sub(r"\s+", "", text[:500]), pdf


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
    print("PASS Q2 original condition, Q5 unscored prompt, and revised figure semantics")
    print("PASS page thresholds, qpdf integrity, extractable text, and TeX logs")


if __name__ == "__main__":
    main()
