from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "markdown"
BUILD = ROOT / "build"
TEMPLATE = ROOT / "latex" / "template.tex"
DOCUMENTS = ["蔡题037_试卷", "蔡题037_学生详解", "蔡题037_教师备课"]


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    for name in DOCUMENTS:
        tex = BUILD / f"{name}.tex"
        run([
            "pandoc", str(MD / f"{name}.md"), "--from=markdown+raw_tex", "--to=latex",
            "--standalone", f"--template={TEMPLATE}",
            f"--lua-filter={ROOT.parents[1] / 'tools' / 'page_tuning.lua'}",
            "--top-level-division=section", "--output", str(tex),
        ])
        text = tex.read_text(encoding="utf-8")
        # Pandoc may keep equation tags beside aligned math, where amsmath
        # rejects them. Preserve a reader-visible number as ordinary math
        # text because the prose frequently refers back to “式（n）”.
        text = re.sub(
            r"\\tag\{(\d+)\}",
            lambda match: rf"\qquad\text{{({match.group(1)})}}",
            text,
        )
        text = re.sub(
            r"\.\./figures/([A-Za-z0-9_-]+)\.png",
            lambda match: str((ROOT / "figures" / f"{match.group(1)}.pdf").resolve()),
            text,
        )
        text = text.replace(r"\begin{figure}", r"\begin{figure}[H]")
        text = text.replace(r"\caption{图", r"\caption*{图")
        tex.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
