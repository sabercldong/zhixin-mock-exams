"""Compare final page body pixels with current, actually reviewed working PDFs.
This produces candidates only, never visual acceptance or human review claims.
"""
from pathlib import Path
import hashlib,json
from PIL import Image
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def body_digest(path):
    with Image.open(path) as im:
        box=(0,90,im.width,im.height-95)
        crop=im.convert('RGB').crop(box)
        return hashlib.sha256(crop.tobytes()).hexdigest(),list(box),list(im.size)
def main():
    index={}
    for q in range(1,9):
        record=ROOT/f'preview/visual-reviewed-q{q:02}.json'
        if not record.exists():continue
        data=json.loads(record.read_text())
        assert data['actual_visual_reviewed'] and data.get('question_accepted',True)
        assert sha(ROOT/f'drafts/question-{q:02}.md')==data['source_sha256']
        for version,item in data['pdfs'].items():
            folder=ROOT/f'preview/working-q{q:02}-{version}'
            pdf=folder/(folder.name+'.pdf')
            assert sha(pdf)==item['pdf_sha256']
            for page in item['high_resolution_pages_reviewed']:
                name=f'page-{page:03}.png';path=folder/name
                assert sha(path)==item['page_png_sha256'][name]
                digest,box,size=body_digest(path)
                index.setdefault(digest,[]).append(dict(question=q,version=version,page=page,
                    working_png=str(path),working_png_sha256=sha(path),
                    actual_review_record_sha256=sha(record),body_crop=box,png_size=size))
    result=dict(actual_final_visual_review=False,scope='candidate exact body-pixel matches; current final overviews and unmatched pages still need actual review',versions={})
    labels=dict(paper='试卷',student='学生详解',teacher='教师备课')
    for version,label in labels.items():
        pdf=ROOT/f'output/pdf/蔡题015_{label}.pdf'
        folder=ROOT/f'preview/full-{version}';matches=[];unmatched=[]
        with fitz.open(pdf) as doc:
            count=len(doc)
            for n in range(1,count+1):
                path=folder/f'page-{n:03}.png';digest,box,size=body_digest(path)
                if digest in index:
                    matches.append(dict(page=n,body_pixel_sha256=digest,body_crop=box,
                        png_size=size,png_sha256=sha(path),matches=index[digest]))
                else:unmatched.append(n)
        result['versions'][version]=dict(pdf_sha256=sha(pdf),total_pages=count,
            exact_reviewed_working_body_matches=matches,new_body_pages_requiring_actual_review=unmatched)
    path=ROOT/'build/final-working-body-comparison.json'
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({v:dict(pages=d['total_pages'],matched=len(d['exact_reviewed_working_body_matches']),
        unmatched=d['new_body_pages_requiring_actual_review']) for v,d in result['versions'].items()}))
if __name__=='__main__':main()
