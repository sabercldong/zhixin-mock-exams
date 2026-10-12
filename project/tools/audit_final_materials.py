from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETS = [f"{number:03d}" for number in range(83, 103)]
REQUIRED_TEACHER = [
    "题型定位",
    "知识点",
    "物理图像",
    "解题入口",
    "解析",
    "关键洞察",
    "易错点",
    "课堂讲解建议",
    "变式训练",
]
REQUIRED_STUDENT = REQUIRED_TEACHER[:5]
BANNED = ["完成本题", "继续下一题", "数字化重构", "原卷图", "参考文件链接"]


def run(command: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        command,
        cwd=cwd or ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode:
        raise AssertionError(f"command failed: {' '.join(command)}\n{result.stdout}")
    return result.stdout


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            return text[end + 5 :]
    return text


def split_questions(text: str) -> list[str]:
    body = strip_front_matter(text)
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题\s*$", body))
    if [int(match.group(1)) for match in matches] != list(range(1, 9)):
        raise AssertionError("question headings are not exactly 1 through 8")
    blocks = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        blocks.append(body[match.start() : end])
    return blocks


def math_blocks(text: str) -> list[str]:
    return re.findall(r"\$\$(.*?)\$\$", text, flags=re.DOTALL)


def unsupported_chinese_in_math(text: str) -> list[str]:
    failures = []
    for block in math_blocks(text):
        cleaned = re.sub(r"\\text\{[^{}]*\}", "", block)
        cleaned = re.sub(r"\\(?:mathrm|operatorname)\{[^{}]*\}", "", cleaned)
        if re.search(r"[\u3400-\u9fff]", cleaned):
            failures.append(" ".join(cleaned.split())[:120])
    return failures


def audit_markdown(path: Path, sections: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    blocks = split_questions(text)
    for number, block in enumerate(blocks, start=1):
        for index, section in enumerate(sections, start=1):
            heading = f"## {index_to_chinese(index)}、{section}"
            if block.count(heading) != 1:
                raise AssertionError(f"{path.name} Q{number}: missing or duplicate {heading}")
    for banned in BANNED:
        if banned in text:
            raise AssertionError(f"{path.name}: banned phrase {banned}")
    if "\\enlargethispage" in text:
        raise AssertionError(f"{path.name}: contains raw page enlargement command")
    compact_depth = 0
    for marker in re.findall(r"PAGE_COMPACT_(START|END)", text):
        compact_depth += 1 if marker == "START" else -1
        if compact_depth not in (0, 1):
            raise AssertionError(f"{path.name}: compact-page markers are nested or reversed")
    if compact_depth:
        raise AssertionError(f"{path.name}: unclosed compact-page marker")
    prose = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    prose = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", "", prose, flags=re.DOTALL)
    if re.search(r"(?<!!)\[[^\]]+\]\([^)]+\)", prose):
        raise AssertionError(f"{path.name}: contains a non-image Markdown link")
    failures = unsupported_chinese_in_math(text)
    if failures:
        raise AssertionError(f"{path.name}: Chinese outside \\text in display math: {failures}")
    for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
        image_path = (path.parent / target).resolve()
        if not image_path.exists() or image_path.stat().st_size == 0:
            raise AssertionError(f"{path.name}: missing image {target}")


def index_to_chinese(index: int) -> str:
    return "一二三四五六七八九"[index - 1]


def audit_pdf(path: Path) -> int:
    if not path.exists() or path.stat().st_size < 10_000:
        raise AssertionError(f"missing or suspiciously small PDF: {path}")
    info = run(["pdfinfo", str(path)])
    match = re.search(r"(?m)^Pages:\s+(\d+)", info)
    if match is None:
        raise AssertionError(f"cannot read page count: {path}")
    text = run(["pdftotext", "-layout", str(path), "-"])
    if "�" in text or "\ufffd" in text:
        raise AssertionError(f"replacement character in {path.name}")
    for banned in BANNED:
        if banned in text:
            raise AssertionError(f"{path.name}: banned phrase {banned}")
    return int(match.group(1))


def main() -> None:
    total_pages = 0
    for set_number in SETS:
        base = ROOT / f"蔡题{set_number}" / "整理版"
        markdown = base / "markdown"
        output = base / "output" / "pdf"
        teacher = markdown / f"蔡题{set_number}_教师备课.md"
        student = markdown / f"蔡题{set_number}_学生详解.md"
        paper = markdown / f"蔡题{set_number}_试卷.md"
        audit_markdown(teacher, REQUIRED_TEACHER)
        audit_markdown(student, REQUIRED_STUDENT)
        audit_markdown(paper, [])
        page_counts = []
        for suffix in ("试卷", "学生详解", "教师备课"):
            page_counts.append(audit_pdf(output / f"蔡题{set_number}_{suffix}.pdf"))
        total_pages += sum(page_counts)
        figure_files = sorted((base / "figures").glob("question-*.pdf"))
        solution_files = sorted((base / "figures").glob("solution-*.pdf"))
        if not figure_files or not solution_files:
            raise AssertionError(f"蔡题{set_number}: question or solution figures are missing")
        verifier = base / "scripts" / "verify_answers.py"
        verification = "no numerical verifier"
        if verifier.exists():
            verification = run(["python3", str(verifier)], cwd=base).strip().splitlines()[-1]
        print(
            f"蔡题{set_number}: pages={page_counts}, "
            f"figures={len(figure_files)}+{len(solution_files)}, "
            f"verification={verification}"
        )
    print(f"collection audit passed: {len(SETS)} sets, {total_pages} PDF pages")


if __name__ == "__main__":
    main()
