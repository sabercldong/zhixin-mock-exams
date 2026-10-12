"""High-resolution Q6 paper/hand crops; originals remain unchanged."""
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]

def main():
    target = ROOT / 'preview/originals'
    items = [
        ('试卷.pdf', 2, (.12, .055, .94, .34), 'q06-paper-detail.png'),
        ('答案.pdf', 7, (.025, .075, .51, .90), 'q06-hand-left-detail.png'),
        ('答案.pdf', 7, (.50, .075, .97, .86), 'q06-hand-right-detail.png'),
    ]
    for filename, page, clip, name in items:
        with fitz.open(ROOT.parent / filename) as doc:
            p = doc[page]
            w, h = p.rect.width, p.rect.height
            region = fitz.Rect(clip[0]*w, clip[1]*h, clip[2]*w, clip[3]*h)
            p.get_pixmap(matrix=fitz.Matrix(4, 4), clip=region, alpha=False).save(target/name)

if __name__ == '__main__':
    main()
