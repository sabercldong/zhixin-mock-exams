"""Q8 source paper and handwritten details, originals unchanged."""
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    items=[
        ('试卷.pdf',2,(.13,.505,.95,.713),'q08-paper-detail.png'),
        ('答案.pdf',8,(.035,.414,.496,.665),'q08-hand-detail.png'),
    ]
    for filename,index,crop,name in items:
        with fitz.open(ROOT.parent/filename) as doc:
            p=doc[index];w,h=p.rect.width,p.rect.height
            rect=fitz.Rect(crop[0]*w,crop[1]*h,crop[2]*w,crop[3]*h)
            p.get_pixmap(matrix=fitz.Matrix(5,5),clip=rect,alpha=False).save(ROOT/'preview/originals'/name)
if __name__=='__main__':main()
