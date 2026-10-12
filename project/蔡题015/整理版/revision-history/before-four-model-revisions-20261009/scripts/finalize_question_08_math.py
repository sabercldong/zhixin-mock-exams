"""Finalize Q8 numerical report against complete source, without claiming visual read."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    pre=json.loads((ROOT/"build/question-08-preverification.json").read_text())
    for n,h in pre["bound_sha256"].items():assert sha(ROOT/n)==h,(n,h)
    geo=json.loads((ROOT/"build/question-08-figure-geometry.json").read_text())
    qa=json.loads((ROOT/"build/source-quality-q08.json").read_text())
    assert geo["passed"] and qa["passed"]
    for n,h in geo["bound_sha256"].items():assert sha(ROOT/n)==h,n
    pre["saved_utc"]=datetime.now(timezone.utc).isoformat()
    names=list(pre["bound_sha256"])+["drafts/question-08.md","drafts/question-08-核验备忘.md",
       "figures/题08_图稿源文件.tex","build/question-08-preverification.json",
       "build/question-08-figure-geometry.json","build/source-quality-q08.json",
       "scripts/finalize_question_08_math.py","latex/template.tex"]
    for name in ["space-08","field-08","simultaneity-08","dipole-08","angles-08","maximum-08"]:
        names.extend([f"figures/{name}.pdf",f"figures/{name}.png"])
    pre["bound_sha256"]={n:sha(ROOT/n) for n in names}
    pre["bound_files"]={n:{"path":str(ROOT/n),"sha256":sha(ROOT/n)} for n in names}
    pre.update(verified_math=True,model_condition_resolved=True,remaining_model_issues=[],
               symbolic_count=pre["symbolic_checks"],numeric_count=pre["numeric_checks"],
               max_normalized_error=pre["max_normalized_numeric_error"],figures=geo["figures"])
    pre.update(document_complete=True,figures_complete=True,actual_pdf_reviewed=False,
               question_accepted=False,set_accepted=False)
    pre["acceptance_note"]="Full ideal-model source and calculation complete; actual PDF/figure review is separate."
    (ROOT/"build/question-08-verification.json").write_text(json.dumps(pre,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(symbolic=pre["symbolic_checks"],numeric=pre["numeric_checks"],
                        geometry=geo["count"],document_complete=True,actual_pdf_reviewed=False)))
if __name__=="__main__":main()
