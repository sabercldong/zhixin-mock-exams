from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "figures"
SOURCE = FIGURE_DIR / "蔡题100_图稿源文件.tex"
MULTIPAGE = FIGURE_DIR / "蔡题100_图稿源文件.pdf"

NAMES = [
    "question-01",
    "solution-01",
    "solution-02",
    "question-03",
    "solution-03",
    "question-04",
    "solution-04",
    "question-05",
    "solution-05",
    "solution-06",
    "question-07",
    "solution-07",
    "question-08",
    "solution-08",
]


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=FIGURE_DIR, check=True)


def main() -> None:
    run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", SOURCE.name])
    for index, name in enumerate(NAMES, start=1):
        pdf = FIGURE_DIR / f"{name}.pdf"
        png_prefix = FIGURE_DIR / name
        run(["pdfseparate", "-f", str(index), "-l", str(index), str(MULTIPAGE), str(pdf)])
        run(["pdftoppm", "-f", "1", "-l", "1", "-png", "-r", "180", "-singlefile", str(pdf), str(png_prefix)])


if __name__ == "__main__":
    main()
