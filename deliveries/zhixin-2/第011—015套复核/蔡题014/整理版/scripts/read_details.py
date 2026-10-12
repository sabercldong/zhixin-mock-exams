"""Render source-detail crops only; originals stay unchanged."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    items=[]
    specs=[
      ('试卷.pdf',0,(0.08,0.20,0.95,0.40),'q01-paper'),
      ('答案.pdf',0,(0.03,0.20,0.98,0.86),'q01-answer'),
      ('试卷.pdf',0,(0.08,0.38,0.95,0.60),'q02-paper'),
      ('试卷.pdf',1,(0.08,0.31,0.95,0.49),'q04-paper'),
      ('答案.pdf',4,(0.51,0.27,0.98,0.83),'q04-answer'),
      ('试卷.pdf',2,(0.08,0.05,0.94,0.16),'q07-paper'),
      ('答案.pdf',6,(0.51,0.12,0.98,0.50),'q07-answer')]
    out=ROOT/'preview/originals/details';out.mkdir(exist_ok=True)
    for source,page,bounds,name in specs:
        pdf=ROOT.parent/source
        with fitz.open(pdf) as doc:
            p=doc[page];w,h=p.rect.width,p.rect.height
            clip=fitz.Rect(bounds[0]*w,bounds[1]*h,bounds[2]*w,bounds[3]*h)
            target=out/(name+'.png')
            p.get_pixmap(matrix=fitz.Matrix(4,4),clip=clip,alpha=False).save(target)
        items.append(dict(source=source,pdf_page=page+1,bounds_fraction=bounds,path=str(target.relative_to(ROOT)),sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
    (out/'detail-manifest.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(items,ensure_ascii=False))
if __name__=='__main__':main()
