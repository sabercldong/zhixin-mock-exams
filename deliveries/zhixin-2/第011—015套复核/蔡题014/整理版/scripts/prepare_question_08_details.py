"""Render original Q8 regions for explicit reading, without altering either PDF."""
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]
for filename,page_index,box,name in [
    ('试卷.pdf',2,(.08,.25,.92,.38),'q08-paper.png'),
    ('答案.pdf',7,(.01,.08,.50,.32),'q08-answer.png')]:
    with fitz.open(ROOT.parent/filename) as doc:
        page=doc[page_index];w,h=page.rect.width,page.rect.height
        clip=fitz.Rect(box[0]*w,box[1]*h,box[2]*w,box[3]*h)
        page.get_pixmap(matrix=fitz.Matrix(5,5),clip=clip,alpha=False).save(ROOT/'preview/originals/details'/name)
        print(name,clip)
