"""Compare working revision images; candidates, never automatic review."""
from pathlib import Path
from PIL import Image
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
BACKUP=ROOT/'revisions/2026-10-09_五项模型修订前'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    out={}
    old_review=json.loads((BACKUP/'preview/visual-reviewed-q05.json').read_text())
    for kind in ['student','teacher']:
        folder=ROOT/f'preview/working-q05-{kind}'
        oldsha={digest:name for name,digest in old_review['pdfs'][kind]['page_png_sha256'].items()}
        pdf=folder/(folder.name+'.pdf')
        with fitz.open(pdf) as doc:count=len(doc)
        pages=[]
        for n in range(1,count+1):
            path=folder/f'page-{n:03}.png';digest=sha(path)
            pages.append(dict(page=n,png_sha256=digest,identical_old_page=oldsha.get(digest)))
        out[kind]=dict(pdf_sha256=sha(pdf),total_pages=count,pages=pages,
          changed_pages=[x['page'] for x in pages if not x['identical_old_page']],
          overviews={p.name:sha(p) for p in sorted(folder.glob('overview-*.jpg'))})
    (ROOT/'build/working-q05-revision-comparison.json').write_text(json.dumps(dict(actual_reviewed=False,documents=out),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v['changed_pages'] for k,v in out.items()}))
if __name__=='__main__':main()
