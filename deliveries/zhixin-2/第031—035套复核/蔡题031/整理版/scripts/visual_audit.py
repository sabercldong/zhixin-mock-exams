"""逐页渲染正式成品，保存总览和需高清核验的页码。"""
from pathlib import Path
import json
import re
import fitz
from PIL import Image,ImageDraw,ImageFont

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'preview/formal'
FONT=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',16)


def main():
    DEST.mkdir(exist_ok=True)
    report={}
    for kind,label in (('paper','试卷'),('student','学生详解'),('teacher','教师备课')):
        doc=fitz.open(ROOT/'output'/f'第031套_{label}版.pdf')
        pages=[]
        for i,p in enumerate(doc):
            pix=p.get_pixmap(matrix=fitz.Matrix(.65,.65),alpha=False)
            pix.save(DEST/f'{kind}-{i+1:03}.png')
            text=p.get_text()
            pages.append(dict(page=i+1,nonspace=len(re.sub(r'\s+','',text)),
                              figures='图 ' in text or '图' in text,
                              question_start=bool(re.search(r'^\s*第\s*[1-8]\s*题',text))))
        for start in range(0,len(doc),12):
            sheet=Image.new('RGB',(1050,1600),'#eeeeee');draw=ImageDraw.Draw(sheet)
            for j in range(start,min(start+12,len(doc))):
                im=Image.open(DEST/f'{kind}-{j+1:03}.png');im.thumbnail((335,368))
                x=(j-start)%3*350+(350-im.width)//2;y=(j-start)//3*400+26
                sheet.paste(im,(x,y));draw.text((x,y-22),f'{kind} {j+1}',fill='black',font=FONT)
            sheet.save(DEST/f'{kind}-overview-{start//12+1:02}.jpg',quality=90)
        report[kind]=pages
    (DEST/'page-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print({k:len(v) for k,v in report.items()})


if __name__=='__main__':main()
