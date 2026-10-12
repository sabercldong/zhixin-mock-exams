"""每题单图总览；保留全部既有预览。"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from render_figures import NAMES
import argparse
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'preview/figures'
FONT=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',20)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('questions',nargs='*')
    args=parser.parse_args()
    DEST.mkdir(parents=True,exist_ok=True)
    count=0
    for q in args.questions or NAMES:
        names=NAMES[q]
        rows=(len(names)+1)//2
        canvas=Image.new('RGB',(1400,rows*430),'#eeeeee');draw=ImageDraw.Draw(canvas)
        for i,name in enumerate(names):
            im=Image.open(ROOT/'figures'/f'{name}.png').convert('RGB');im.thumbnail((670,385))
            x=i%2*700+(700-im.width)//2;y=i//2*430+30+(385-im.height)//2
            canvas.paste(im,(x,y));draw.text((i%2*700+15,i//2*430+6),name,fill='black',font=FONT)
        canvas.save(DEST/f'q{q}-figures.jpg',quality=94)
        count+=len(names)
    print(f'{count}幅图的分题总览已生成')
if __name__=='__main__':main()
