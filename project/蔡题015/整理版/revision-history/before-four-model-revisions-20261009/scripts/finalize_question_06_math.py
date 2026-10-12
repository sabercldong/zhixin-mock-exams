"""Bind Q6 full conditional mathematics and figures; never grant model approval."""
from pathlib import Path
import hashlib,json
import verify_question_06 as physics
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    physics.main()
    pre_path=ROOT/"build/question-06-preverification.json"
    pre=json.loads(pre_path.read_text())
    geo=json.loads((ROOT/"build/question-06-figure-geometry.json").read_text())
    qa=json.loads((ROOT/"build/source-quality-q06.json").read_text())
    model_path=ROOT/"build/question-06-模型审查.json"
    model=json.loads(model_path.read_text())
    assert pre["verified_math"] and geo["passed"] and qa["passed"]
    assert model["status"]=="pending_human_choice" and model["human_choice_reply"] is None
    assert not model["authorized_changes"] and not model["model_condition_resolved"]
    draft=ROOT/"drafts/question-06.md"
    assert pre["source_sha256"]==geo["manuscript_sha256"]==qa["questions"][0]["sha256"]==sha(draft)
    assert geo["source_sha256"]==sha(ROOT/"figures/题06_图稿源文件.tex")
    for name,item in geo["figures"].items():
        for ext in ["pdf","png"]:
            assert item[ext+"_sha256"]==sha(ROOT/f"figures/{name}.{ext}")
    model["preverification_sha256"]=sha(pre_path)
    model["conditional_manuscript_sha256"]=sha(draft)
    model["conditional_figures_source_sha256"]=sha(ROOT/"figures/题06_图稿源文件.tex")
    model["conditional_source_complete"]=True
    model["formal_acceptance"]=False
    model_path.write_text(json.dumps(model,ensure_ascii=False,indent=2)+"\n")
    paths={"manuscript":draft,"figure_source":ROOT/"figures/题06_图稿源文件.tex",
           "geometry":ROOT/"build/question-06-figure-geometry.json",
           "quality":ROOT/"build/source-quality-q06.json",
           "model_record":model_path,"math_script":ROOT/"scripts/verify_question_06.py",
           "finalizer":Path(__file__),"geometry_script":ROOT/"scripts/check_figures_06.py",
           "figure_renderer":ROOT/"scripts/render_figures_06.py",
           "original_paper":ROOT.parent/"试卷.pdf","original_answers":ROOT.parent/"答案.pdf",
           "source_detail_manifest":ROOT/"preview/originals/question-06-detail-manifest.json",
           "actual_source_reading":ROOT/"preview/source-reviewed-q06.json"}
    for name in geo["figures"]:
        for ext in ["pdf","png"]:paths[name+"_"+ext]=ROOT/f"figures/{name}.{ext}"
    report=dict(pre)
    report.update(
        stage="full conditional manuscript mathematics and vector geometry; PDF and visual evidence separate",
        document_complete=True,model_condition_resolved=False,
        model_scope="Literal feed-phase stem preserved. Actual inlet enthalpy deficits, insulated/no-shaft-work/frozen-gas conditions are explicit conditional assumptions. No real same-temperature liquids, approval of lambda redefinition, or attainable global maximum claimed.",
        question_accepted=False,set_accepted=False,figures_rendered=True,
        remaining_model_issues=[item["description"] for item in model["issues"]],
        figures=geo["figures"],
        bound_files={key:{"path":str(path),"sha256":sha(path)} for key,path in paths.items()})
    (ROOT/"build/question-06-verification.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"verified_math":True,"document_complete":True,
                     "model_condition_resolved":False,"question_accepted":False,
                     "figures":len(geo["figures"])}))
if __name__=="__main__":main()
