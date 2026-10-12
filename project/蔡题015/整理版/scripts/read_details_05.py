"""Render Q5 source details without changing prior source/review records."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    dest=ROOT/"preview/originals"
    requests=[
        ("试卷.pdf",1,(.135,.459,.950,.558),"q05-paper-text"),
        ("试卷.pdf",1,(.420,.574,.680,.743),"q05-paper-diagram"),
        ("答案.pdf",4,(.030,.185,.505,.655),"q05-answer-route"),
        ("答案.pdf",4,(.030,.405,.500,.660),"q05-answer-calculation"),
    ]
    report={"actual_reviewed":False,"sources":{},"crops":{}}
    for name,idx,box,label in requests:
        source=ROOT.parent/name;report["sources"][name]=sha(source)
        with fitz.open(source) as doc:
            page=doc[idx];w,h=page.rect.width,page.rect.height
            clip=fitz.Rect(box[0]*w,box[1]*h,box[2]*w,box[3]*h)
            path=dest/(label+".png")
            page.get_pixmap(matrix=fitz.Matrix(5,5),clip=clip,alpha=False).save(path)
            report["crops"][label]={"source":name,"page":idx+1,"relative_clip":box,"sha256":sha(path)}
    (dest/"question-05-detail-manifest.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False))
if __name__=="__main__":main()
