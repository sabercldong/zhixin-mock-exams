"""Bind full Q5 conditional manuscript/math/figures; never grants human approval."""
from pathlib import Path
import hashlib,json
import verify_question_05 as physics
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    physics.main()
    pre=json.loads((ROOT/"build/question-05-preverification.json").read_text())
    geo=json.loads((ROOT/"build/question-05-figure-geometry.json").read_text())
    qa=json.loads((ROOT/"build/source-quality-q05.json").read_text())
    model_path=ROOT/"build/question-05-模型审查.json"
    model=json.loads(model_path.read_text())
    assert pre["verified_math"] and geo["passed"] and qa["passed"]
    assert model["reply_received"] and model["human_reply"]=="统一"
    assert model["authorized_changes"] and model["model_condition_resolved"]
    assert geo["source_sha256"]==sha(ROOT/"figures/题05_图稿源文件.tex")
    assert qa["questions"][0]["sha256"]==sha(ROOT/"drafts/question-05.md")
    for name,item in geo["figures"].items():
        for ext in ["pdf","png"]:
            assert item[ext+"_sha256"]==sha(ROOT/f"figures/{name}.{ext}")
    model["preverification_sha256"]=sha(ROOT/"build/question-05-preverification.json")
    model["revised_manuscript_sha256"]=sha(ROOT/"drafts/question-05.md")
    model["revised_figures_source_sha256"]=sha(ROOT/"figures/题05_图稿源文件.tex")
    model["conditional_source_complete"]=True
    model["formal_acceptance"]=False
    model_path.write_text(json.dumps(model,ensure_ascii=False,indent=2)+"\n")
    paths={"manuscript":ROOT/"drafts/question-05.md","figure_source":ROOT/"figures/题05_图稿源文件.tex",
           "geometry":ROOT/"build/question-05-figure-geometry.json","quality":ROOT/"build/source-quality-q05.json",
           "model_record":model_path,"math_script":ROOT/"scripts/verify_question_05.py","finalizer":Path(__file__),
           "geometry_script":ROOT/"scripts/check_figures_05.py","figure_renderer":ROOT/"scripts/render_figures_05.py",
           "human_authorization":ROOT/"build/model-revisions-015-2026-10-09.json",
        "original_paper":ROOT.parent/"试卷.pdf","original_answers":ROOT.parent/"答案.pdf",
           "source_detail_manifest":ROOT/"preview/originals/question-05-detail-manifest.json",
           "actual_source_reading":ROOT/"preview/source-reviewed-q05.json"}
    for name in geo["figures"]:
        for ext in ["pdf","png"]:paths[name+"_"+ext]=ROOT/f"figures/{name}.{ext}"
    report=dict(pre)
    report.update(stage="full conditional manuscript mathematics and vector geometry; PDF and visual evidence separate",
                  document_complete=True,model_condition_resolved=True,
                  model_scope="Human-authorized taut inextensible massless string, negligible-mass rings, in-plane branch. Out-plane normal mode separately solved as changed-condition extension; finite-ring/elastic models not claimed solved.", remaining_model_issues=[],
                  question_accepted=False,set_accepted=False,figures_rendered=True,
                  figures=geo["figures"],bound_files={key:{"path":str(path),"sha256":sha(path)} for key,path in paths.items()})
    (ROOT/"build/question-05-verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"verified_math":True,"document_complete":True,"model_condition_resolved":True,
                     "question_accepted":False,"figures":len(geo["figures"])}))
if __name__=="__main__":main()
