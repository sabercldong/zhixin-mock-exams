from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
OUTPUT = ROOT / "output"
FIGURE_SOURCE = ROOT / "figures" / "蔡题065_图稿源文件.tex"
NAMES = ["蔡题065_试卷", "蔡题065_学生详解", "蔡题065_教师备课"]
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


def prompt_block(block: str) -> str:
    return block.split("## 一、题型定位", 1)[0]


def check_markdown() -> None:
    texts: dict[str, str] = {}
    for name in NAMES:
        path = MD / f"{name}.md"
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        assert re.findall(r"(?m)^# 第 ([1-8]) 题$", text) == list("12345678"), name
        assert "�" not in text and "" not in text
        assert not re.search(r"(?m)^#{3,}\s", text), name
        for phrase in FORBIDDEN:
            assert phrase not in text, (name, phrase)
        for target in re.findall(r"!\[[^]]*]\(([^)]+\.png)\)", text):
            image = (MD / target).resolve()
            assert image.exists(), image
            assert image.with_suffix(".pdf").exists(), image.with_suffix(".pdf")

        q4 = question_block(text, 4)
        for token in ("7.682", "5.876", "4.047", "1.466", "1.471", "1.482"):
            assert token in prompt_block(q4), (name, token)
        q6 = question_block(text, 6)
        assert r"\Delta t=19\,\mu\mathrm s" in prompt_block(q6), name
        assert all(choice in prompt_block(q6) for choice in
                   ("50\,\mathrm{Hz}", "1\,\mathrm{kHz}", "100\,\mathrm{kHz}"))
        q7 = question_block(text, 7)
        assert "【思考题，不计分】" in prompt_block(q7), name
        q8 = question_block(text, 8)
        for token in ("50\,\mathrm{mm}", "30\,\mathrm{cm}", "R\propto r^{-4}", "25\%"):
            assert token in prompt_block(q8), (name, token)

    assert r"190\,\mu\mathrm s" not in texts["蔡题065_试卷"]
    for name in ("蔡题065_学生详解", "蔡题065_教师备课"):
        assert "数据矛盾" in texts[name]
        assert r"0.636\,\mathrm{mH}" in texts[name]
        assert r"13.4\,\mathrm{mH}" in texts[name]

    teacher = texts["蔡题065_教师备课"]
    for heading in REQUIRED_SECTIONS:
        assert len(re.findall(rf"(?m)^## {re.escape(heading)}$", teacher)) == 8, heading
    student = texts["蔡题065_学生详解"]
    for heading in REQUIRED_SECTIONS[:5]:
        assert len(re.findall(rf"(?m)^## {re.escape(heading)}$", student)) == 8, heading
    for heading in REQUIRED_SECTIONS[5:]:
        assert heading not in student, heading
    assert not re.search(r"(?m)^## ", texts["蔡题065_试卷"])


def source_block(source: str, start: str, end: str) -> str:
    return source.split(start, 1)[1].split(end, 1)[0]


def check_figures() -> None:
    source = FIGURE_SOURCE.read_text(encoding="utf-8")
    q1 = source_block(source, "% question-01", "% solution-01")
    s1 = source_block(source, "% solution-01", "% question-02")
    q3 = source_block(source, "% question-03", "% solution-03")
    q4 = source_block(source, "% question-04", "% solution-04")
    q6 = source_block(source, "% question-06", "% solution-06")
    q8 = source_block(source, "% question-08", "% solution-08")
    assert r"\bm L=" not in q1
    assert "domain=1.12:7.4" in s1
    assert r"{\omega R}" not in q3
    assert r"qE_0\cos" not in q4 and r"E_p=bx" not in q4
    assert "待测黑盒" in q6 and "13.4" not in q6 and "13.47" not in q6
    assert q6.count("{A}") >= 1 and q6.count("{D}") >= 1
    assert "液柱测压装置" in q8 and "搭桥血管" in q8
    assert "16R_0" not in q8 and "R_b" not in q8
    for number in range(1, 9):
        for prefix in ("question", "solution"):
            stem = ROOT / "figures" / f"{prefix}-{number:02d}"
            assert stem.with_suffix(".png").exists(), stem
            assert stem.with_suffix(".pdf").exists(), stem


def check_pdfs() -> None:
    minimums = {
        "蔡题065_试卷": 8,
        "蔡题065_学生详解": 40,
        "蔡题065_教师备课": 65,
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
        assert "�" not in text, pdf
        assert "第065套" in re.sub(r"\s+", "", text[:500]), pdf


def check_logs() -> None:
    bad = re.compile(
        r"(?m)^!|Overfull|Missing character|Undefined control|"
        r"Emergency stop|Fatal error"
    )
    for name in NAMES:
        log = OUTPUT / f"{name}.log"
        assert log.exists(), log
        assert not bad.search(log.read_text(encoding="utf-8", errors="replace")), log


def main() -> None:
    check_markdown()
    check_figures()
    check_pdfs()
    check_logs()
    print("PASS markdown structure, nine teacher headings, forbidden phrases, and full prompts")
    print("PASS question/solution figure semantics and all 16 PNG/PDF assets")
    print("PASS page thresholds, qpdf integrity, extractable text, and clean TeX logs")


if __name__ == "__main__":
    main()
