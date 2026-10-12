from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "markdown"
TEACHER_PATH = MD_DIR / "蔡题101_教师备课.md"
STUDENT_PATH = MD_DIR / "蔡题101_学生详解.md"
PAPER_PATH = MD_DIR / "蔡题101_试卷.md"
VERIFICATION_PATH = MD_DIR / "蔡题101_核验记录.md"


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            return text[end + 5 :].lstrip()
    return text


def front_matter() -> str:
    return (
        "---\n"
        'title: "第101套"\n'
        'shorttitle: "第101套"\n'
        'author: "物理竞赛教学资料"\n'
        "toc: false\n"
        "---\n\n"
    )


def split_problems(body: str) -> list[tuple[str, str]]:
    pattern = re.compile(
        r"(?m)^# (?:蔡题 101｜)?第 (\d+) 题(?:（竞赛教学设计）)?\n"
    )
    matches = list(pattern.finditer(body))
    result: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        result.append((match.group(1), body[start:end].strip()))
    if len(result) != 8:
        raise RuntimeError(f"expected 8 problems, found {len(result)}")
    return result


def section_between(text: str, start_heading: str, end_heading: str | None) -> str:
    start = text.find(start_heading)
    if start < 0:
        raise RuntimeError(f"missing heading: {start_heading}")
    start += len(start_heading)
    if end_heading is None:
        end = len(text)
    else:
        end = text.find(end_heading, start)
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


def normalize_problem_block(block: str) -> str:
    """Keep only the nine user-specified visible module headings.

    Subquestion numbers remain as bold inline labels, while teaching and
    variation subdivisions become ordinary paragraphs.
    """
    block = block.replace("### 题目", "")
    block = block.replace("### 定位说明", "")
    block = re.sub(r"(?m)^<!-- question-(?:start|end) -->\n*", "", block)
    block = re.sub(
        r"(?m)^### （(\d+)）｜[^\n]+$",
        lambda match: f"**（{match.group(1)}）**",
        block,
    )
    block = re.sub(r"(?m)^### [^\n]+\n+", "", block)
    return re.sub(r"\n{3,}", "\n\n", block).strip()


def main() -> None:
    paper_body = strip_front_matter(PAPER_PATH.read_text(encoding="utf-8"))
    paper_body = re.sub(r"(?m)^\s*\\newpage\s*$", "", paper_body)
    question_map = dict(split_problems(paper_body))

    teacher_body = strip_front_matter(TEACHER_PATH.read_text(encoding="utf-8"))
    # Remove all previously generated page-break lines before rebuilding.  A
    # line-anchored pattern is deliberate: repeated runs may otherwise leave
    # every second ``\\newpage`` in a consecutive pair.
    teacher_body = re.sub(r"(?m)^\s*\\newpage\s*$", "", teacher_body)
    appendix_marker = "# 蔡题 101｜答案核验记录"
    if appendix_marker in teacher_body:
        teacher_body = teacher_body.split(appendix_marker, 1)[0].rstrip()
    first_problem = re.search(
        r"(?m)^# (?:蔡题 101｜)?第 1 题(?:（竞赛教学设计）)?$",
        teacher_body,
    )
    if first_problem is None:
        raise RuntimeError("missing first problem heading")
    problems = split_problems(teacher_body)

    paper_chunks: list[str] = []
    student_chunks: list[str] = []
    teacher_chunks: list[str] = []

    for number, block in problems:
        block = normalize_problem_block(block)
        type_position = section_between(
            block, "## 一、题型定位", "## 二、知识点"
        )
        question_text = question_map[number]
        # Older generated files placed the complete question inside the first
        # module.  Remove that duplicated prefix once, then rebuild with the
        # question before the "题型定位" heading.
        if type_position.startswith(question_text):
            type_position = type_position[len(question_text) :].strip()
        knowledge = section_between(
            block, "## 二、知识点", "## 三、物理图像"
        )
        physical_image = section_between(
            block, "## 三、物理图像", "## 四、解题入口"
        )
        entry = section_between(
            block, "## 四、解题入口", "## 五、解析"
        )
        solution_text = section_between(
            block, "## 五、解析", "## 六、关键洞察"
        )
        insights = section_between(
            block, "## 六、关键洞察", "## 七、易错点"
        )
        errors = section_between(
            block, "## 七、易错点", "## 八、课堂讲解建议"
        )
        teaching = section_between(
            block, "## 八、课堂讲解建议", "## 九、变式训练"
        )
        variants = section_between(block, "## 九、变式训练", None)

        question_block = (
            "<!-- question-start -->\n"
            f"{question_text}\n\n"
            "<!-- question-end -->"
        )

        paper_chunks.append(f"# 第 {number} 题\n\n{question_text}")
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
            f"{solution_text}\n\n"
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
            f"{student_solution(solution_text)}"
        )

    teacher_output = (
        front_matter()
        + add_page_breaks(teacher_chunks)
    )
    student_output = (
        front_matter()
        + add_page_breaks(student_chunks)
    )
    paper_output = (
        front_matter()
        + add_page_breaks(paper_chunks)
    )

    TEACHER_PATH.write_text(teacher_output, encoding="utf-8")
    STUDENT_PATH.write_text(student_output, encoding="utf-8")
    PAPER_PATH.write_text(paper_output, encoding="utf-8")


if __name__ == "__main__":
    main()
