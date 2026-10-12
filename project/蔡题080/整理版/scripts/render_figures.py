from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
SOURCE = FIGURES / "蔡题080_图稿源文件.tex"
MULTIPAGE = FIGURES / "蔡题080_图稿源文件.pdf"
NAMES = [item for n in range(1, 9) for item in (f"question-{n:02d}", f"solution-{n:02d}")]


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=FIGURES, check=True)


def main() -> None:
    run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", SOURCE.name])
    for page, name in enumerate(NAMES, 1):
        pdf = FIGURES / f"{name}.pdf"
        run(["pdfseparate", "-f", str(page), "-l", str(page), str(MULTIPAGE), str(pdf)])
        run(["pdftoppm", "-f", "1", "-l", "1", "-png", "-r", "180", "-singlefile", str(pdf), str(FIGURES / name)])


if __name__ == "__main__":
    main()
