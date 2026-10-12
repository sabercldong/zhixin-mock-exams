"""Read original PDFs without mutation; generate page previews and source hashes."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    dest=ROOT/'preview/originals';dest.mkdir(parents=True,exist_ok=True)
    record={}
    for name,prefix in [('\u8bd5\u5377.pdf','paper'),('\u7b54\u6848.pdf','answer')]:
        source=ROOT.parent/name
        with fitz.open(source) as doc:
            record[name]={'pages':len(doc),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
            for i,page in enumerate(doc,1):
                page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(dest/f'{prefix}-{i:02}.png')
    (dest/'source-manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
