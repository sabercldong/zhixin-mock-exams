"""Retain the observed fringe photograph as data, without synthetic replacement."""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]

if __name__ == "__main__":
    doc = fitz.open(ROOT.parent / "试卷.pdf")
    page = doc[2]
    clip = fitz.Rect(page.rect.width * .23, page.rect.height * .700,
                     page.rect.width * .80, page.rect.height * .86)
    target = fitz.open()
    cropped = target.new_page(width=clip.width, height=clip.height)
    cropped.show_pdf_page(cropped.rect, doc, 2, clip=clip)
    target.save(ROOT / "figures" / "measurement-07.pdf")
    cropped.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=False).save(
        ROOT / "figures" / "measurement-07.png")
