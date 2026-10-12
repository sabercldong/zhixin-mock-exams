from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[1]
def crop(name, page_number, rect, label):
    page = fitz.open(ROOT.parent / name)[page_number-1]
    page.get_pixmap(matrix=fitz.Matrix(3.0, 3.0), clip=fitz.Rect(*rect), alpha=False).save(ROOT / 'preview/originals' / f'{label}.png')

if __name__ == '__main__':
    doc = fitz.open(ROOT.parent / '答案.pdf')
    w,h = doc[2].rect.width,doc[2].rect.height
    crop('答案.pdf',3,(0,0,w*.52,h*.43),'answer-q06-detail')
    doc = fitz.open(ROOT.parent / '试卷.pdf')
    w,h = doc[2].rect.width,doc[2].rect.height
    crop('试卷.pdf',3,(0,h*.64,w,h*.96),'paper-q06-graph-detail')
    w,h=doc[3].rect.width,doc[3].rect.height
    crop('试卷.pdf',4,(0,0,w,h*.33),'paper-q07-detail')
