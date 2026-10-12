#!/usr/bin/env python3
"""在解答正文中明确建立解答图与前后公式的对应关系。"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETS = ("040", "045", "046", "047", "048", "050", "051", "053", "054")
REFERENCE_RE = re.compile(r"如图|图中|解答图|由图|见图|图示")
SOLUTION_IMAGE_RE = re.compile(
    r"(?m)^!\[[^]]*\]\(\.\./figures/solution-(\d{2})\.png\)(?:\{[^\n]*\})?\s*$"
)
LINK_SENTENCE = (
    "下图给出与上述推导相对应的解答示意；图中标出的量、方向和"
    "作用点均沿用正文约定，可与前后各式逐项核对。"
)


def integrate(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    if [int(match.group(1)) for match in matches] != list(range(1, 9)):
        raise RuntimeError(f"{path.name} 题号异常")

    front = text[: matches[0].start()]
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end].rstrip()
        question = int(match.group(1))
        image_match = SOLUTION_IMAGE_RE.search(block)
        if not image_match:
            raise RuntimeError(f"{path.name} 第 {question} 题缺少解答图")
        expected = f"{question:02d}"
        if image_match.group(1) != expected:
            raise RuntimeError(f"{path.name} 第 {question} 题解答图编号异常")

        marker = f"<!-- SOLUTION_FIGURE_LINK_{question:02d} -->"
        sixth = block.find("\n## 六、关键洞察")
        if sixth < 0 or image_match.start() > sixth:
            raise RuntimeError(f"{path.name} 第 {question} 题解答图未位于解析模块")
        nearby_context = block[max(0, image_match.start() - 360) : image_match.start()]
        if marker not in block and not REFERENCE_RE.search(nearby_context):
            insertion = f"{marker}\n\n{LINK_SENTENCE}\n\n"
            block = block[: image_match.start()] + insertion + block[image_match.start() :]
        blocks.append(block)

    path.write_text(front + "\n\n".join(blocks) + "\n", encoding="utf-8")


def main() -> None:
    for set_number in SETS:
        path = (
            ROOT
            / f"蔡题{set_number}"
            / "整理版"
            / "markdown"
            / f"蔡题{set_number}_教师备课.md"
        )
        integrate(path)


if __name__ == "__main__":
    main()
