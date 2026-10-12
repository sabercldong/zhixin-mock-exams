from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
SOURCE = FIGURES / "蔡题089_图稿源文件.pdf"


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=ROOT)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="cai089-figures-") as temporary:
        pages = Path(temporary) / "page-%02d.pdf"
        run(["pdfseparate", str(SOURCE), str(pages)])
        split_pages = sorted(Path(temporary).glob("page-*.pdf"))
        if len(split_pages) != 16:
            raise RuntimeError(f"图稿源文件应为 16 页，实际为 {len(split_pages)} 页")
        for index, page in enumerate(split_pages):
            question = index % 2 == 0
            number = index // 2 + 1
            stem = f"{'question' if question else 'solution'}-{number:02d}"
            pdf_target = FIGURES / f"{stem}.pdf"
            pdf_target.write_bytes(page.read_bytes())
            run([
                "pdftoppm", "-f", "1", "-l", "1", "-singlefile", "-png", "-r", "180",
                str(pdf_target), str(FIGURES / stem),
            ])


if __name__ == "__main__":
    main()
