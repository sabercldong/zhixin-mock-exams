from __future__ import annotations

import re
from pathlib import Path


def main() -> None:
    path = Path(__file__).resolve().parents[1] / "markdown" / "蔡题090_教师备课.md"
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    if len(matches) != 8:
        raise RuntimeError(f"expected 8 question blocks, got {len(matches)}")
    front = text[:matches[0].start()].rstrip()
    blocks: dict[int, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start():end].strip()
        block = re.sub(r"\n\\newpage\s*$", "", block).strip()
        blocks[int(match.group(1))] = block
    ordered = front + "\n\n" + "\n\n\\newpage\n\n".join(blocks[n] for n in range(1, 9)) + "\n"
    path.write_text(ordered, encoding="utf-8")


if __name__ == "__main__":
    main()
