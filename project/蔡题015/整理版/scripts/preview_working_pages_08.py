"""分题预览实际页面；生成图片不等于已审读，审读记录单独保存。"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
FONT=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',16)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    manifest={}
    for q in args.questions or ['08']:
        for version in ['student','teacher']:
            name=f'working-q{q}-{version}'
            folder=ROOT/'preview'/name
            path=folder/(name+'.pdf')
            with fitz.open(path) as doc:
                pages=[]
                for i,p in enumerate(doc):
                    p.get_pixmap(matrix=fitz.Matrix(1.7,1.7),alpha=False).save(folder/f'page-{i+1:03}.png')
                    pages.append(dict(page=i+1,nonspace=len(re.sub(r'\s','',p.get_text())),images=len(p.get_images())))
                for start in range(0,len(doc),12):
                    sheet=Image.new('RGB',(1050,1600),'#eeeeee');draw=ImageDraw.Draw(sheet)
                    for j in range(start,min(start+12,len(doc))):
                        im=Image.open(folder/f'page-{j+1:03}.png');im.thumbnail((335,368))
                        x=(j-start)%3*350+(350-im.width)//2;y=(j-start)//3*400+26
                        sheet.paste(im,(x,y));draw.text((x,y-22),f'{version} {j+1}',fill='black',font=FONT)
                    sheet.save(folder/f'overview-{start//12+1:02}.jpg',quality=92)
            manifest[name]=dict(pdf_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pages=pages,actual_reviewed=False)
    dest=ROOT/'preview'/'working-page-manifest-q08.json'
    dest.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(manifest,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
