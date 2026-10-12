"""整套当前PDF逐页预览，审读状态不得由生成图片自动设为通过。"""
from pathlib import Path
import hashlib,json,re
import fitz
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
FONT=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',16)
def main():
    manifest={}
    for label,version in [('paper','试卷'),('student','学生详解'),('teacher','教师备课')]:
        pdf=ROOT/'output/pdf'/f'蔡题015_{version}.pdf';folder=ROOT/'preview'/f'full-{label}';folder.mkdir(exist_ok=True)
        pages=[]
        with fitz.open(pdf) as doc:
            for i,page in enumerate(doc):
                page.get_pixmap(matrix=fitz.Matrix(1.7,1.7),alpha=False).save(folder/f'page-{i+1:03}.png')
                pages.append(dict(page=i+1,nonspace=len(re.sub(r'\s','',page.get_text()))))
            for start in range(0,len(doc),12):
                sheet=Image.new('RGB',(1050,1600),'#eeeeee');draw=ImageDraw.Draw(sheet)
                for j in range(start,min(start+12,len(doc))):
                    im=Image.open(folder/f'page-{j+1:03}.png');im.thumbnail((335,368))
                    x=(j-start)%3*350+(350-im.width)//2;y=(j-start)//3*400+26
                    sheet.paste(im,(x,y));draw.text((x,y-22),f'{label} {j+1}',fill='black',font=FONT)
                sheet.save(folder/f'overview-{start//12+1:02}.jpg',quality=92)
        manifest[label]=dict(path=str(pdf),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pages=pages,actual_reviewed=False)
        print(label,len(pages),flush=True)
    (ROOT/'preview/full-page-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
