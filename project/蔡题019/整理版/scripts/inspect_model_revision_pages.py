"""Compare actual rendered page bodies with the retained reviewed version.

This produces candidates only. It never claims that new images were viewed.
"""
from pathlib import Path
import hashlib, json
from PIL import Image
import fitz

ROOT=Path(__file__).resolve().parents[1]
BACKUP=ROOT/'revisions/2026-10-09_五项模型修订前'

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def body_hash(path):
    with Image.open(path) as image:
        # Headers and page counters are checked in current overviews.
        # Reuse is permitted only for byte-identical body pixels.
        crop=image.crop((0,90,image.width,image.height-95))
        return hashlib.sha256(crop.tobytes()).hexdigest()

def main():
    results={}
    for kind in ['paper','student','teacher']:
        old_folder=BACKUP/f'preview/full-{kind}'
        old_pages={}
        for path in old_folder.glob('page-*.png'):
            old_pages.setdefault(body_hash(path),[]).append(int(path.stem.split('-')[1]))
        folder=ROOT/f'preview/full-{kind}'
        pdf=next((ROOT/'output/pdf').glob('*'+{'paper':'试卷','student':'学生详解','teacher':'教师备课'}[kind]+'.pdf'))
        with fitz.open(pdf) as document: count=len(document)
        pages=[]
        for number in range(1,count+1):
            path=folder/f'page-{number:03}.png'
            key=body_hash(path)
            pages.append(dict(page=number,png_sha256=sha(path),body_pixels_sha256=key,
                identical_previously_reviewed_body_pages=old_pages.get(key,[]),
                needs_direct_high_resolution_review=key not in old_pages))
        overview_count=(count+11)//12
        results[kind]=dict(pdf_sha256=sha(pdf),total_pages=count,pages=pages,
            new_body_pages=[row['page'] for row in pages if row['needs_direct_high_resolution_review']],
            current_overviews={str(index):sha(folder/f'overview-{index:02}.jpg')
                               for index in range(1,overview_count+1)})
    dest=ROOT/'build/model-revision-page-comparison.json'
    dest.write_text(json.dumps(dict(actual_reviewed=False,
        previous_review_sha256=sha(BACKUP/'preview/visual-reviewed-full.json'),
        compared_crop=[0,90,'width','height-95'],documents=results),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:dict(total_pages=v['total_pages'],new_body_pages=v['new_body_pages'])
                     for k,v in results.items()},ensure_ascii=False))

if __name__=='__main__': main()
