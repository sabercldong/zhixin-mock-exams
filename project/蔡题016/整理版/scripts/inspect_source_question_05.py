"""Render Q5 source crops; preserve both source PDFs unchanged."""
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    folder=ROOT/'preview/originals'
    for file,page,clip,name in [
        ('试卷.pdf',1,(.06,.60,.96,.95),'q05-paper-detail.png'),
        ('答案.pdf',6,(.03,.20,.51,.93),'q05-hand-left-detail.png'),
        ('答案.pdf',6,(.50,.06,.97,.94),'q05-hand-right-detail.png')]:
        with fitz.open(ROOT.parent/file) as doc:
            p=doc[page];w,h=p.rect.width,p.rect.height
            rect=fitz.Rect(clip[0]*w,clip[1]*h,clip[2]*w,clip[3]*h)
            p.get_pixmap(matrix=fitz.Matrix(4,4),clip=rect,alpha=False).save(folder/name)
if __name__=='__main__':main()
