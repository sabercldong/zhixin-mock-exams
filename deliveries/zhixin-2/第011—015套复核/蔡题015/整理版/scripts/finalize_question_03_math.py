"""Bind current q03 conditional mathematical evidence; never infer visual/model approval."""
from pathlib import Path
import hashlib, json
import verify_question_03 as physics

ROOT=Path(__file__).resolve().parents[1]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    physics.main()
    pre=json.loads((ROOT/"build/question-03-preverification.json").read_text())
    geo=json.loads((ROOT/"build/question-03-figure-geometry.json").read_text())
    quality=json.loads((ROOT/"build/source-quality-q03.json").read_text())
    model=json.loads((ROOT/"build/question-03-模型审查.json").read_text())
    assert pre["verified_math"] and geo["passed"] and quality["passed"]
    assert model["model_condition_resolved"] and model["human_answer"]=="统一"
    paths={
        "manuscript":ROOT/"drafts/question-03.md",
        "figure_source":ROOT/"figures/题03_图稿源文件.tex",
        "geometry":ROOT/"build/question-03-figure-geometry.json",
        "quality":ROOT/"build/source-quality-q03.json",
        "math_script":ROOT/"scripts/verify_question_03.py",
        "finalizer":Path(__file__),
        "geometry_script":ROOT/"scripts/check_figures_03.py",
        "figure_renderer":ROOT/"scripts/render_figures_03.py",
        "model_review":ROOT/"build/question-03-模型审查.json",
        "human_authorization":ROOT/"build/model-revisions-015-2026-10-09.json",
        "original_paper":ROOT.parent/"试卷.pdf",
        "original_answers":ROOT.parent/"答案.pdf",
        "source_detail_manifest":ROOT/"preview/originals/question-03-detail-manifest.json",
    }
    for name in geo["figures"]:
        for ext in ["pdf","png"]:paths[name+"_"+ext]=ROOT/f"figures/{name}.{ext}"
    report=dict(pre)
    report.update(
        scope="q03 authorized horizontal model, complete source/mathematics; visual reading separate",
        document_complete=True,conditional_source_complete=True,
        model_condition_resolved=True,question_accepted=False,set_accepted=False,
        figures_rendered=True,figures=geo["figures"],
        remaining_model_issues=[],
        bound_files={k:{"path":str(p),"sha256":sha(p)} for k,p in paths.items()},
    )
    (ROOT/"build/question-03-verification.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({
        "verified_math":True,"conditional_source_complete":True,
        "model_condition_resolved":True,"question_accepted":False,
        "symbolic":pre["symbolic_count"],"numeric":pre["numeric_count"],
        "figures":len(geo["figures"]),
    },ensure_ascii=False))

if __name__=="__main__":main()
