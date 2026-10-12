"""工作稿图形清单及重点页渲染，不替代正式逐页复审。"""
from pathlib import Path
import fitz
from PIL import Image, ImageDraw, ImageFont
from render_figures import NAMES

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'preview/working-review'

def main():
    DEST.mkdir(exist_ok=True)
    font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',20)
    files=[ROOT/'figures'/f'{name}.png' for names in NAMES.values() for name in names]
    for start in range(0,len(files),6):
        sheet=Image.new('RGB',(1600,1650),'#eeeeee');draw=ImageDraw.Draw(sheet)
        for j,path in enumerate(files[start:start+6]):
            im=Image.open(path).convert('RGB');im.thumbnail((755,495))
            x=j%2*800+(800-im.width)//2;y=j//2*550+35
            sheet.paste(im,(x,y));draw.text((j%2*800+20,j//2*550+8),path.stem,fill='black',font=font)
        sheet.save(DEST/f'figures-{start//6+1:02}.jpg',quality=94)
    targets=[('02','student',6),('04','teacher',13),('05','teacher',12),('06','teacher',13),('07','teacher',12),('07','teacher',11)]
    for q,kind,num in targets:
        doc=fitz.open(ROOT/f'preview/working-q{q}-{kind}/working-q{q}-{kind}.pdf')
        doc[num-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False).save(DEST/f'q{q}-{kind}-{num:02}.png')

if __name__=='__main__':main()
