from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
TEACHER = MD / "蔡题083_教师备课.md"
STUDENT = MD / "蔡题083_学生详解.md"
PAPER = MD / "蔡题083_试卷.md"

TEACHER_ONLY_RE = re.compile(
    r"\n?<!--\s*(?:TEACHER_ONLY_START|teacher-only-start)\s*-->.*?"
    r"<!--\s*(?:TEACHER_ONLY_END|teacher-only-end)\s*-->\n?",
    re.DOTALL,
)


def main() -> None:
    text = TEACHER.read_text(encoding="utf-8")
    front, body = text.split("\n---\n", 1)
    front = front + "\n---\n"
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", body))
    chunks: list[str] = []
    paper_chunks: list[str] = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        block = body[match.start():end].strip()
        cut = block.find("\n## 六、关键洞察")
        if cut < 0:
            raise RuntimeError(f"第 {match.group(1)} 题缺少第六模块")
        chunks.append(TEACHER_ONLY_RE.sub("\n", block[:cut]).strip())
        question_end = block.find("\n## 一、题型定位")
        if question_end < 0:
            raise RuntimeError(f"第 {match.group(1)} 题缺少第一模块")
        paper_chunks.append(block[:question_end].strip())
    STUDENT.write_text(front + "\n\n\\newpage\n\n".join(chunks) + "\n", encoding="utf-8")
    PAPER.write_text(front + "\n\n\\newpage\n\n".join(paper_chunks) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
