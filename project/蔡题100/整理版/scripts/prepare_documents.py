from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "markdown"
TEACHER_PATH = MD_DIR / "蔡题100_教师备课.md"
STUDENT_PATH = MD_DIR / "蔡题100_学生详解.md"
PAPER_PATH = MD_DIR / "蔡题100_试卷.md"


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            return text[end + 5 :].lstrip()
    return text


def front_matter() -> str:
    return (
        "---\n"
        'title: "第100套"\n'
        'shorttitle: "第100套"\n'
        'author: "物理竞赛教学资料"\n'
        "toc: false\n"
        "---\n\n"
    )


def split_problems(body: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"(?m)^# 第 (\d+) 题\n")
    matches = list(pattern.finditer(body))
    result: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        result.append((match.group(1), body[start:end].strip()))
    if len(result) != 8:
        raise RuntimeError(f"expected 8 problems, found {len(result)}")
    return result


def section_between(text: str, start_heading: str, end_heading: str | None) -> str:
    start = text.find(start_heading)
    if start < 0:
        raise RuntimeError(f"missing heading: {start_heading}")
    start += len(start_heading)
    end = len(text) if end_heading is None else text.find(end_heading, start)
    if end < 0:
        raise RuntimeError(f"missing heading: {end_heading}")
    return text[start:end].strip()


def add_page_breaks(chunks: list[str]) -> str:
    return "\n\n\\newpage\n\n".join(chunks).rstrip() + "\n"


def student_solution(text: str) -> str:
    """Remove teacher-only derivation audits while preserving the full solution."""
    text = re.sub(
        r"(?s)<!-- teacher-only-start -->.*?<!-- teacher-only-end -->\s*",
        "",
        text,
    )
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def normalize_teacher_block(block: str) -> str:
    block = re.sub(
        r"(?s)<!-- question-start -->.*?<!-- question-end -->\s*", "", block
    )
    block = re.sub(r"(?m)^\s*\\newpage\s*$", "", block)
    return re.sub(r"\n{3,}", "\n\n", block).strip()


def main() -> None:
    paper_body = strip_front_matter(PAPER_PATH.read_text(encoding="utf-8"))
    paper_body = re.sub(r"(?m)^\s*\\newpage\s*$", "", paper_body)
    question_map = dict(split_problems(paper_body))

    teacher_body = strip_front_matter(TEACHER_PATH.read_text(encoding="utf-8"))
    teacher_body = re.sub(r"(?m)^\s*\\newpage\s*$", "", teacher_body)
    problems = split_problems(teacher_body)

    paper_chunks: list[str] = []
    student_chunks: list[str] = []
    teacher_chunks: list[str] = []

    for number, raw_block in problems:
        block = normalize_teacher_block(raw_block)
        type_position = section_between(block, "## 一、题型定位", "## 二、知识点")
        knowledge = section_between(block, "## 二、知识点", "## 三、物理图像")
        physical_image = section_between(block, "## 三、物理图像", "## 四、解题入口")
        entry = section_between(block, "## 四、解题入口", "## 五、解析")
        solution = section_between(block, "## 五、解析", "## 六、关键洞察")
        insights = section_between(block, "## 六、关键洞察", "## 七、易错点")
        errors = section_between(block, "## 七、易错点", "## 八、课堂讲解建议")
        teaching = section_between(block, "## 八、课堂讲解建议", "## 九、变式训练")
        variants = section_between(block, "## 九、变式训练", None)

        question = question_map[number]
        question_block = (
            "<!-- question-start -->\n"
            f"{question}\n\n"
            "<!-- question-end -->"
        )

        paper_chunks.append(f"# 第 {number} 题\n\n{question}")
        teacher_chunks.append(
            f"# 第 {number} 题\n\n"
            f"{question_block}\n\n"
            "## 一、题型定位\n\n"
            f"{type_position}\n\n"
            "## 二、知识点\n\n"
            f"{knowledge}\n\n"
            "## 三、物理图像\n\n"
            f"{physical_image}\n\n"
            "## 四、解题入口\n\n"
            f"{entry}\n\n"
            "## 五、解析\n\n"
            f"{solution}\n\n"
            "## 六、关键洞察\n\n"
            f"{insights}\n\n"
            "## 七、易错点\n\n"
            f"{errors}\n\n"
            "## 八、课堂讲解建议\n\n"
            f"{teaching}\n\n"
            "## 九、变式训练\n\n"
            f"{variants}"
        )
        student_chunks.append(
            f"# 第 {number} 题\n\n"
            f"{question_block}\n\n"
            "## 一、题型定位\n\n"
            f"{type_position}\n\n"
            "## 二、知识点\n\n"
            f"{knowledge}\n\n"
            "## 三、物理图像\n\n"
            f"{physical_image}\n\n"
            "## 四、解题入口\n\n"
            f"{entry}\n\n"
            "## 五、解析\n\n"
            f"{student_solution(solution)}"
        )

    TEACHER_PATH.write_text(front_matter() + add_page_breaks(teacher_chunks), encoding="utf-8")
    STUDENT_PATH.write_text(front_matter() + add_page_breaks(student_chunks), encoding="utf-8")
    PAPER_PATH.write_text(front_matter() + add_page_breaks(paper_chunks), encoding="utf-8")


if __name__ == "__main__":
    main()
