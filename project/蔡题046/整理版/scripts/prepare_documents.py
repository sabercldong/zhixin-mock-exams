from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
TEACHER = MD / "蔡题046_教师备课.md"
STUDENT = MD / "蔡题046_学生详解.md"
PAPER = MD / "蔡题046_试卷.md"

TEACHER_ONLY_RE = re.compile(
    r"\n?<!--\s*(?:TEACHER_ONLY_START|teacher-only-start)\s*-->.*?"
    r"<!--\s*(?:TEACHER_ONLY_END|teacher-only-end)\s*-->\n?",
    re.DOTALL,
)


def main() -> None:
    text = TEACHER.read_text(encoding="utf-8")
    front, body = text.split("\n---\n", 1)
    front += "\n---\n"
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", body))
    if len(matches) != 8:
        raise RuntimeError(f"应有 8 道题，实际找到 {len(matches)} 道")
    numbered_blocks: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[match.start():end].strip()
        block = re.sub(r"(?:\n\\newpage\s*)+$", "", block).strip()
        numbered_blocks.append((int(match.group(1)), block))
    numbered_blocks.sort(key=lambda item: item[0])
    body = "\n\n\\newpage\n\n".join(block for _, block in numbered_blocks) + "\n"
    text = front + body
    TEACHER.write_text(text, encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", body))
    student_chunks: list[str] = []
    paper_chunks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[match.start():end].strip()
        cut = block.find("\n## 六、关键洞察")
        if cut < 0:
            raise RuntimeError(f"第 {match.group(1)} 题缺少第六模块")
        student_main = TEACHER_ONLY_RE.sub("\n", block[:cut]).strip()
        supplement_end = block.find("\n## 八、课堂讲解建议", cut)
        if supplement_end < 0:
            raise RuntimeError(f"第 {match.group(1)} 题缺少第八模块")
        supplement = block[cut:supplement_end]
        supplement = supplement.replace("\n## 六、关键洞察\n", "\n\n**解析后的关键检查。**\n")
        supplement = supplement.replace("\n## 七、易错点\n", "\n\n**解析中的易错辨析。**\n")
        supplement = re.sub(
            r"(?m)^<!--\s*(?:TEACHER_ONLY_START|TEACHER_ONLY_END|"
            r"teacher-only-start|teacher-only-end)\s*-->\s*$",
            "",
            supplement,
        ).strip()
        if supplement:
            student_main = (student_main + "\n\n" + supplement).strip()
        variation_start = block.find("\n## 九、变式训练", supplement_end)
        if variation_start < 0:
            raise RuntimeError(f"第 {match.group(1)} 题缺少第九模块")
        review = block[supplement_end:variation_start]
        review = review.replace("\n## 八、课堂讲解建议\n", "\n")
        review = review.replace("先让学生", "可先").replace("让学生", "可以")
        review = review.replace("板书时", "书写时").replace("板书", "书写")
        review = review.replace("课堂上", "理解时").replace("教师", "读者")
        review = re.sub(r"(?m)^<!--.*?-->\s*$", "", review).strip()
        if review:
            student_main = (student_main + "\n\n**解题顺序与直观复盘。**\n\n" + review).strip()
        variation = block[variation_start:]
        variation = variation.replace("\n## 九、变式训练\n", "\n", 1)
        variation = variation.replace("<!-- TEACHER_ONLY_END -->", "").strip()
        if variation:
            student_main = (student_main + "\n\n**进一步思考与自测。**\n\n" + variation).strip()
        end_marker = "<!-- TEACHER_ONLY_END -->"
        last_end = block.rfind(end_marker)
        shared_tail = ""
        if last_end > cut:
            shared_tail = block[last_end + len(end_marker):].strip()
            shared_tail = re.sub(r"(?:\n\\newpage\s*)+$", "", shared_tail).strip()
        student_main = student_main.replace("<!-- TEACHER_ONLY_START -->", "").strip()
        student_chunks.append(
            (student_main + ("\n\n" + shared_tail if shared_tail else "")).strip()
        )
        question_end = block.find("\n## 一、题型定位")
        if question_end < 0:
            raise RuntimeError(f"第 {match.group(1)} 题缺少第一模块")
        paper_chunks.append(TEACHER_ONLY_RE.sub("\n", block[:question_end]).strip())
    STUDENT.write_text(front + "\n\n\\newpage\n\n".join(student_chunks) + "\n", encoding="utf-8")
    PAPER.write_text(front + "\n\n\\newpage\n\n".join(paper_chunks) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import sys

    project_root = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(project_root))
    from tools.document_pipeline import prepare_set

    prepare_set("046")
