"""将全部分题工作稿逐页渲染，并生成带页码的总览。"""
from pathlib import Path
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]/"preview"
for folder in sorted(ROOT.glob("working-q*-*")):
    pdf=folder/(folder.name+".pdf")
    if not pdf.exists():continue
    doc=fitz.open(pdf)
    thumbs=[]
    for i,page in enumerate(doc):
        pix=page.get_pixmap(matrix=fitz.Matrix(.62,.62),alpha=False)
        target=folder/f"page-{i+1:02}.png"
        pix.save(target)
        im=Image.open(target).convert("RGB")
        im.thumbnail((298,422))
        cell=Image.new("RGB",(318,452),"#dddddd")
        cell.paste(im,((318-im.width)//2,25))
        ImageDraw.Draw(cell).text((12,7),f"{folder.name} p{i+1}",fill="black")
        thumbs.append(cell)
    for start in range(0,len(thumbs),16):
        batch=thumbs[start:start+16]
        cols=4;rows=(len(batch)+cols-1)//cols
        canvas=Image.new("RGB",(cols*318,rows*452),"#bbbbbb")
        for j,im in enumerate(batch):canvas.paste(im,((j%cols)*318,(j//cols)*452))
        canvas.save(folder/f"contact-{start//16+1}.jpg",quality=90)
    print(folder.name,len(doc))

