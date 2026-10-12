"""第021套原件只读提取与预览；不修改原始PDF。"""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    source=ROOT.parent/'试卷.pdf'
    dest=ROOT/'preview/originals';dest.mkdir(parents=True,exist_ok=True)
    with fitz.open(source) as doc:
        record={'试卷.pdf':dict(pages=len(doc),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),questions=list(range(1,9)))}
        for i,page in enumerate(doc,1):
            half=page.rect.width/2
            for side,bounds in [('left',fitz.Rect(0,0,half,page.rect.height)),('right',fitz.Rect(half,0,page.rect.width,page.rect.height))]:
                page.get_pixmap(matrix=fitz.Matrix(2.3,2.3),clip=bounds,alpha=False).save(dest/f'paper-{i:02}-{side}.png')
    (dest/'source-manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record,ensure_ascii=False))
if __name__=='__main__':main()
