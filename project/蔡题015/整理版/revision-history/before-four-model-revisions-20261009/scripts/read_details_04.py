"""Render Q4-only source details; originals and earlier manifests unchanged."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    dest=ROOT/"preview/originals"
    requests=[
        ("试卷.pdf",1,(.120,.055,.950,.310),"q04-paper-text"),
        ("试卷.pdf",1,(.405,.310,.710,.457),"q04-paper-diagram"),
        ("答案.pdf",3,(.025,.045,.505,.905),"q04-answer-left"),
        ("答案.pdf",3,(.510,.055,.970,.380),"q04-answer-right"),
    ]
    report={"actual_reviewed":False,"sources":{},"crops":{}}
    for name,idx,box,label in requests:
        source=ROOT.parent/name
        report["sources"][name]=sha(source)
        with fitz.open(source) as doc:
            page=doc[idx];w,h=page.rect.width,page.rect.height
            clip=fitz.Rect(box[0]*w,box[1]*h,box[2]*w,box[3]*h)
            path=dest/(label+".png")
            page.get_pixmap(matrix=fitz.Matrix(5,5),clip=clip,alpha=False).save(path)
            report["crops"][label]={"source":name,"page":idx+1,"relative_clip":box,"sha256":sha(path)}
    (dest/"question-04-detail-manifest.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False))
if __name__=="__main__": main()
