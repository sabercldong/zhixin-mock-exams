"""Render q02 source-detail crops, preserving the original documents."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
 dest=ROOT/"preview/originals";dest.mkdir(parents=True,exist_ok=True)
 requests=[("试卷.pdf",0,(.125,.393,.942,.612),"q02-paper-detail"),
           ("答案.pdf",1,(.025,.065,.497,.88),"q02-answer-left-detail"),
           ("答案.pdf",1,(.51,.065,.985,.716),"q02-answer-right-detail")]
 report={}
 for name,number,box,label in requests:
  with fitz.open(ROOT.parent/name) as doc:
   page=doc[number];w,h=page.rect.width,page.rect.height
   clip=fitz.Rect(box[0]*w,box[1]*h,box[2]*w,box[3]*h)
   path=dest/(label+".png")
   page.get_pixmap(matrix=fitz.Matrix(4,4),clip=clip,alpha=False).save(path)
   report[label]={"source":name,"page":number+1,"relative_clip":box,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()}
 (dest/"question-02-detail-manifest.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps(report,ensure_ascii=False))
if __name__=="__main__":main()

