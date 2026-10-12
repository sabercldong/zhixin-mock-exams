from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
BUILD = ROOT / "build"

FILES = {
    "paper": MD / "蔡题062_试卷.md",
    "student": MD / "蔡题062_学生详解.md",
    "teacher": MD / "蔡题062_教师备课.md",
}
PDFS = {
    "paper": BUILD / "蔡题062_试卷.pdf",
    "student": BUILD / "蔡题062_学生详解.pdf",
    "teacher": BUILD / "蔡题062_教师备课.pdf",
}
FORBIDDEN = ("数字化重构", "完成本题", "继续下一题", "原卷图", "参考文件", "手写答案")
TEACHER_HEADINGS = (
    "一、题型定位",
    "二、知识点",
    "三、物理图像",
    "四、解题入口",
    "五、解析",
    "六、关键洞察",
    "七、易错点",
    "八、课堂讲解建议",
    "九、变式训练",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def page_count(pdf: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    match = re.search(r"(?m)^Pages:\s+(\d+)$", out)
    if not match:
        fail(f"无法读取页数：{pdf}")
    return int(match.group(1))


def main() -> None:
    texts = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}

    for name, text in texts.items():
        questions = re.findall(r"(?m)^# 第 (\d+) 题$", text)
        if questions != [str(i) for i in range(1, 9)]:
            fail(f"{name} 题号异常：{questions}")
        for word in FORBIDDEN:
            if word in text:
                fail(f"{name} 含禁用语：{word}")
        if re.search(r"https?://|\[[^]]+\]\([^)]*\.pdf(?:[#?][^)]*)?\)", text):
            fail(f"{name} 含外部或 PDF 参考链接")

        for image_path in re.findall(r"!\[[^]]*\]\(([^)]+)\)", text):
            clean = image_path.split("{")[0].strip()
            target = (MD / clean).resolve()
            if not target.exists():
                fail(f"{name} 图片缺失：{target}")

    teacher_h2 = re.findall(r"(?m)^## (.+)$", texts["teacher"])
    expected = list(TEACHER_HEADINGS) * 8
    if teacher_h2 != expected:
        fail("教师版九模块标题或顺序异常")

    student_h2 = re.findall(r"(?m)^## (.+)$", texts["student"])
    if student_h2 != list(TEACHER_HEADINGS[:5]) * 8:
        fail("学生版五模块标题或顺序异常")
    if re.search(r"(?m)^## ", texts["paper"]):
        fail("试卷版不应包含解析模块")

    for name, pdf in PDFS.items():
        if not pdf.exists():
            fail(f"PDF 缺失：{pdf}")
        subprocess.run(["qpdf", "--check", str(pdf)], check=True, capture_output=True, text=True)
        text = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True)
        if len(text.strip()) < 500:
            fail(f"PDF 可提取文本异常：{pdf}")
        log = pdf.with_suffix(".log")
        if not log.exists():
            fail(f"编译日志缺失：{log}")
        log_text = log.read_text(encoding="utf-8", errors="replace")
        bad_log = re.search(
            r"Overfull|Missing character|LaTeX Error|Undefined control sequence|"
            r"Emergency stop|Fatal error",
            log_text,
        )
        if bad_log:
            fail(f"{log.name} 含未清理的编译警告：{bad_log.group(0)}")

    pages = {name: page_count(pdf) for name, pdf in PDFS.items()}
    if not 65 <= pages["teacher"] <= 80:
        fail(f"教师版页数不在 65--80：{pages['teacher']}")
    print("内容结构、图片路径、禁用语、PDF 结构与页数检查通过")
    print("页数：", pages)


if __name__ == "__main__":
    main()
