"""Render Q8 original details; generation is not actual reading."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    dest=ROOT/"preview/originals"
    requests=[
        ("试卷.pdf",2,(.105,.325,.952,.580),"q08-paper-model-fields"),
        ("试卷.pdf",2,(.105,.565,.952,.676),"q08-paper-questions"),
        ("答案.pdf",5,(.503,.078,.976,.386),"q08-answer-rest"),
        ("答案.pdf",5,(.505,.381,.974,.604),"q08-answer-contraction"),
        ("答案.pdf",5,(.503,.595,.974,.815),"q08-answer-angle"),
    ]
    report={"actual_reviewed":False,"sources":{},"crops":{}}
    for name,index,box,label in requests:
        source=ROOT.parent/name;report["sources"][name]=sha(source)
        with fitz.open(source) as doc:
            p=doc[index];w,h=p.rect.width,p.rect.height
            clip=fitz.Rect(box[0]*w,box[1]*h,box[2]*w,box[3]*h)
            path=dest/(label+".png")
            p.get_pixmap(matrix=fitz.Matrix(5,5),clip=clip,alpha=False).save(path)
            report["crops"][label]={"source":name,"page":index+1,"relative_clip":box,"sha256":sha(path)}
    (dest/"question-08-detail-manifest.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False))
if __name__=="__main__":main()
