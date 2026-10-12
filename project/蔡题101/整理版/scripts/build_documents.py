from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MD_DIR = ROOT / "markdown"
LATEX_DIR = ROOT / "latex"
BUILD_DIR = ROOT / "build"
OUTPUT_DIR = ROOT / "output" / "pdf"
TEMPLATE = LATEX_DIR / "template.tex"

DOCUMENTS = [
    "蔡题101_试卷",
    "蔡题101_学生详解",
    "蔡题101_教师备课",
]


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for name in DOCUMENTS:
        markdown = MD_DIR / f"{name}.md"
        tex = BUILD_DIR / f"{name}.tex"
        run(
            [
                "pandoc",
                str(markdown),
                "--from=markdown+raw_tex",
                "--to=latex",
                "--standalone",
                f"--template={TEMPLATE}",
                f"--lua-filter={ROOT.parents[1] / 'tools' / 'page_tuning.lua'}",
                "--top-level-division=section",
                "--output",
                str(tex),
            ]
        )

        text = tex.read_text(encoding="utf-8")
        text = re.sub(
            r"\.\./figures/([A-Za-z0-9_-]+)\.(?:png|pdf)",
            lambda match: str((ROOT / "figures" / f"{match.group(1)}.pdf").resolve()),
            text,
        )
        # Pandoc turns an image with alt text into a real figure environment.
        # Keep every figure at its explanatory position; the environment itself
        # supplies \centering, so question and solution drawings share the same
        # alignment in all three PDFs.
        text = text.replace(r"\begin{figure}", r"\begin{figure}[H]")
        # Captions already carry the pedagogical number (for example 图 2-1).
        # Suppress LaTeX's automatic figure counter to avoid a duplicate prefix.
        text = text.replace(r"\caption{图", r"\caption*{图")
        tex.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
