"""只读原卷和手写答案；生成逐页预览与完整性清单，不修改来源。"""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    dest=ROOT/'preview/originals';dest.mkdir(parents=True,exist_ok=True)
    record={}
    for name,prefix in [('试卷.pdf','paper'),('答案.pdf','answer')]:
        source=ROOT.parent/name
        with fitz.open(source) as doc:
            record[name]={'pages':len(doc),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
            for i,page in enumerate(doc,1):page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(dest/f'{prefix}-{i:02}.png')
    (dest/'source-manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
