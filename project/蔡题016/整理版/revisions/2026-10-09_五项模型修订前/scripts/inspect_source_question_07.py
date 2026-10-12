"""Render Q7 source crops; no changes to original PDFs."""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]

def main():
    items = [
        ('试卷.pdf', 2, (.12, .385, .95, .508), 'q07-paper-detail.png'),
        ('答案.pdf', 8, (.035, .090, .495, .395), 'q07-hand-detail.png'),
    ]
    for filename, index, clip, name in items:
        with fitz.open(ROOT.parent / filename) as doc:
            page = doc[index]
            w, h = page.rect.width, page.rect.height
            rect = fitz.Rect(clip[0]*w, clip[1]*h, clip[2]*w, clip[3]*h)
            page.get_pixmap(matrix=fitz.Matrix(5, 5), clip=rect, alpha=False).save(ROOT/'preview/originals'/name)

if __name__ == '__main__':
    main()
