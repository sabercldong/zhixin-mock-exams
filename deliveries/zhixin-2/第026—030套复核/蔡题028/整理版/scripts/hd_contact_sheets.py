"""高清检查页的四页并排总览；原高清单页全部保留。"""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'preview/formal/hd'
record=json.loads((DEST/'rendered-pages.json').read_text())
targets=[(kind,p) for kind,item in record.items() for p in item['pages']]
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',24)
for start in range(0,len(targets),4):
    canvas=Image.new('RGB',(2040,2880),'#e9e9e9');draw=ImageDraw.Draw(canvas)
    for i,(kind,p) in enumerate(targets[start:start+4]):
        im=Image.open(DEST/f'{kind}-{p:03}.png').convert('RGB');im.thumbnail((995,1390))
        x=i%2*1020+(1020-im.width)//2;y=i//2*1440+42
        canvas.paste(im,(x,y));draw.text((x,y-32),f'{kind} PDF page {p}',fill='black',font=font)
    canvas.save(DEST/f'contact-{start//4+1:02}.jpg',quality=96)
print(len(targets),'高清页；', (len(targets)+3)//4,'检查图')
