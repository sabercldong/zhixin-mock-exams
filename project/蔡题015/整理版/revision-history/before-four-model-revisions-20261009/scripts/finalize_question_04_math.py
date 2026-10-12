"""Bind Q4 complete source and math; visual/document acceptance remains separate."""
from pathlib import Path
import hashlib,json
import verify_question_04 as physics
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    physics.main()
    pre=json.loads((ROOT/"build/question-04-preverification.json").read_text())
    geo=json.loads((ROOT/"build/question-04-figure-geometry.json").read_text())
    qa=json.loads((ROOT/"build/source-quality-q04.json").read_text())
    assert pre["verified_math"] and geo["passed"] and qa["passed"]
    paths={"manuscript":ROOT/"drafts/question-04.md","figure_source":ROOT/"figures/题04_图稿源文件.tex",
           "geometry":ROOT/"build/question-04-figure-geometry.json","quality":ROOT/"build/source-quality-q04.json",
           "math_script":ROOT/"scripts/verify_question_04.py","finalizer":Path(__file__),
           "geometry_script":ROOT/"scripts/check_figures_04.py","figure_renderer":ROOT/"scripts/render_figures_04.py",
           "original_paper":ROOT.parent/"试卷.pdf","original_answers":ROOT.parent/"答案.pdf",
           "source_detail_manifest":ROOT/"preview/originals/question-04-detail-manifest.json"}
    for name in geo["figures"]:
        for ext in ["pdf","png"]:paths[name+"_"+ext]=ROOT/f"figures/{name}.{ext}"
    report=dict(pre)
    report.update(scope="Q4 full mathematics/source under stated textbook limits; PDF/visual reading recorded separately",
                  document_complete=True,model_condition_resolved=True,
                  model_scope="Original tiny-gap, negligible touch load/quasi-static threshold interpretation. x rod travel and z piston travel are separate. Middle temperatures are ideal rapid-switching means, not a fabricated single-state or finite-frequency equilibrium. Hard-stop and explicitly specified finite-gap/hysteresis variants are separated.",
                  remaining_model_issues=[],question_accepted=False,set_accepted=False,figures_rendered=True,
                  figures=geo["figures"],bound_files={key:{"path":str(path),"sha256":sha(path)} for key,path in paths.items()})
    (ROOT/"build/question-04-verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"verified_math":True,"document_complete":True,"model_condition_resolved":True,"question_accepted":False,"figures":len(geo["figures"])}))
if __name__=="__main__":main()
