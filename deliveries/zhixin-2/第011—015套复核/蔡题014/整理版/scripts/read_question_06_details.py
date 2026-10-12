"""Additional Q6 original crops, without replacing earlier manifests."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    rows=[]
    specs=[('试卷.pdf',1,(.12,.78,.94,.92),'q06-paper'),
           ('答案.pdf',6,(.035,.16,.505,.605),'q06-answer-left')]
    folder=ROOT/'preview/originals/details'
    for source,page,bounds,name in specs:
        with fitz.open(ROOT.parent/source) as doc:
            p=doc[page];w,h=p.rect.width,p.rect.height
            rect=fitz.Rect(bounds[0]*w,bounds[1]*h,bounds[2]*w,bounds[3]*h)
            path=folder/(name+'.png')
            p.get_pixmap(matrix=fitz.Matrix(5,5),clip=rect,alpha=False).save(path)
        rows.append(dict(source=source,pdf_page=page+1,bounds=bounds,
                         path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         actual_displayed_and_read=False))
    (folder/'q06-detail-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(rows,ensure_ascii=False))
if __name__=='__main__':main()
