"""Render every output page, contact sheets, and selected full-size pages."""
from pathlib import Path
import json
import re
import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/"preview"
FONT=ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf",16)

if __name__=="__main__":
    DEST.mkdir(exist_ok=True)
    report={}
    for kind,suffix in (("paper","试卷版"),("student","学生详解版"),("teacher","教师备课版")):
        doc=fitz.open(ROOT/"output"/f"第036套_{suffix}.pdf")
        pages=[]
        for i,p in enumerate(doc):
            pm=p.get_pixmap(matrix=fitz.Matrix(.55,.55),alpha=False)
            img=Image.frombytes("RGB",(pm.width,pm.height),pm.samples)
            img.save(DEST/f"{kind}-{i+1:03}.png")
            text=p.get_text()
            body=[b for b in p.get_text("blocks") if b[1]>55 and b[3]<p.rect.height-35]
            pages.append({"page":i+1,"chars":len(re.sub(r"\s+","",text)),
                          "bottom":max([b[3] for b in body],default=0),
                          "questions":re.findall(r"第\s*[1-8]\s*题",text)})
        for start in range(0,len(doc),12):
            sheet=Image.new("RGB",(1050,1600),"#eeeeee")
            draw=ImageDraw.Draw(sheet)
            for j in range(start,min(start+12,len(doc))):
                img=Image.open(DEST/f"{kind}-{j+1:03}.png")
                img.thumbnail((335,368))
                x=(j-start)%3*350+(350-img.width)//2
                y=(j-start)//3*400+26
                sheet.paste(img,(x,y))
                draw.text((x,y-22),f"{kind} {j+1}",fill="black",font=FONT)
            sheet.save(DEST/f"{kind}-overview-{start//12+1:02}.jpg",quality=90)
        report[kind]=pages
    (DEST/"page-audit.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:{"pages":len(v),"sparse":[p for p in v[1:] if p["chars"]<120]}
                      for k,v in report.items()},ensure_ascii=False,indent=2))
