from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "蔡题074" / "整理版"


def copy_with_number(source: Path, target: Path, number: str) -> None:
    text = source.read_text(encoding="utf-8").replace("蔡题074", f"蔡题{number}")
    target.write_text(text, encoding="utf-8")


def main() -> None:
    for value in range(64, 74):
        number = f"{value:03d}"
        base = ROOT / f"蔡题{number}" / "整理版"
        for relative in ("build", "figures", "latex", "markdown", "output/pdf", "scripts"):
            (base / relative).mkdir(parents=True, exist_ok=True)

        shutil.copy2(REFERENCE / "latex" / "template.tex", base / "latex" / "template.tex")
        for script in ("prepare_documents.py", "build_documents.py", "render_figures.py"):
            copy_with_number(REFERENCE / "scripts" / script, base / "scripts" / script, number)


if __name__ == "__main__":
    main()
