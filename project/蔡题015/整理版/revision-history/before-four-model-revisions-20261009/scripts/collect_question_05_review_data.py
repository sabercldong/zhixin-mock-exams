"""Collect current Q5 evidence read-only; NEVER assert actual visual reading or acceptance."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    qa=json.loads((ROOT/"build/source-quality-q05.json").read_text())
    physics=json.loads((ROOT/"build/question-05-verification.json").read_text())
    geo=json.loads((ROOT/"build/question-05-figure-geometry.json").read_text())
    model=json.loads((ROOT/"build/question-05-模型审查.json").read_text())
    assert qa["passed"] and physics["verified_math"] and physics["document_complete"] and geo["passed"]
    assert not physics["model_condition_resolved"] and not model["reply_received"]
    for item in physics["bound_files"].values():assert sha(Path(item["path"]))==item["sha256"]
    source=(ROOT/"drafts/question-05.md").read_text()
    student=source.split("## 六、关键洞察")[0].rstrip()+"\n"
    pdfs={};identical=[];logs={};qpdf=[]
    paths=["drafts/question-05.md","figures/题05_图稿源文件.tex","figures/题05_图稿源文件.pdf",
           "build/question-05-verification.json","build/question-05-preverification.json",
           "build/question-05-figure-geometry.json","build/question-05-模型审查.json",
           "build/source-quality-q05.json","preview/source-reviewed-q05.json",
           "preview/originals/question-05-detail-manifest.json","preview/originals/source-manifest.json",
           "preview/working-draft-check-q05.json","preview/working-page-manifest-q05.json",
           "scripts/read_details_05.py","scripts/verify_question_05.py","scripts/check_figures_05.py",
           "scripts/finalize_question_05_math.py","scripts/render_figures_05.py","scripts/render_figures.py",
           "scripts/preview_drafts_05.py","scripts/preview_working_pages_05.py",
           "scripts/collect_question_05_review_data.py","scripts/check_saved_reviews.py","latex/template.tex"]
    qpdf_paths=[ROOT/"figures/题05_图稿源文件.pdf"]+[ROOT/f"figures/{n}.pdf" for n in geo["figures"]]
    for version,body in [("student",student),("teacher",source)]:
        folder=ROOT/f"preview/working-q05-{version}";base=folder/f"working-q05-{version}"
        actual=base.with_suffix(".md").read_text().split("---\n",2)[2]
        assert actual==body
        qpdf_paths.append(base.with_suffix(".pdf"))
        with fitz.open(base.with_suffix(".pdf")) as doc:
            n=len(doc);density=[len(re.sub(r"\s","",p.get_text())) for p in doc][1:]
            assert all(v>100 for v in density)
            text="\n".join(p.get_text() for p in doc)
            assert not any(b in text for b in ["数字化重构","完成本题","继续下一题","原卷图","\ufffd","https://"])
            pngs={f"page-{i:03d}.png":sha(folder/f"page-{i:03d}.png") for i in range(1,n+1)}
            overviews={f"overview-{i:02d}.jpg":sha(folder/f"overview-{i:02d}.jpg") for i in range(1,(n+11)//12+1)}
            pdfs[version]={"pdf_sha256":sha(base.with_suffix(".pdf")),"total_pages":n,"body_pages":n-1,
                           "body_nonspace":sum(density),"per_page_nonspace":density,
                           "page_png_sha256":pngs,"overview_sha256":overviews}
        for ext in ["md","tex","pdf","log"]:paths.append(str(base.with_suffix("."+ext).relative_to(ROOT)))
        log=base.with_suffix(".log")
        warnings=re.findall(r"(?m)^.*(?:Warning|Underfull|Overfull|Missing character|^!).*$",log.read_text())
        assert not warnings,warnings
        logs[str(log.relative_to(ROOT))]={"sha256":sha(log),"warnings":[]}
    for i in range(1,min(pdfs["student"]["total_pages"],pdfs["teacher"]["total_pages"])+1):
        key=f"page-{i:03d}.png"
        if pdfs["student"]["page_png_sha256"][key]==pdfs["teacher"]["page_png_sha256"][key]:
            identical.append({"student_page":i,"teacher_page":i,"png_sha256":pdfs["student"]["page_png_sha256"][key]})
    qpdf_paths=list(dict.fromkeys(qpdf_paths))
    for p in qpdf_paths:
        run=subprocess.run(["qpdf","--check",str(p)],capture_output=True,text=True,check=True)
        qpdf.append({"path":str(p.relative_to(ROOT)),"sha256":sha(p),"passed":True})
    figurelog=ROOT/"figures/题05_图稿源文件.log"
    warnings=re.findall(r"(?m)^.*(?:Warning|Underfull|Overfull|Missing character|^!).*$",figurelog.read_text())
    assert not warnings,warnings
    logs[str(figurelog.relative_to(ROOT))]={"sha256":sha(figurelog),"warnings":[]}
    paths.append(str(figurelog.relative_to(ROOT)))
    template=sha(ROOT/"latex/template.tex")
    assert template=="434e4734708ef9c12c4be4629709e370fa5fe9a67a4cc88709ee13ffa571673b"
    original_images=model["source_images_actually_read"]
    for rel,digest in original_images.items():assert sha(ROOT/rel)==digest
    for name,item in geo["figures"].items():
        for ext in ["pdf","png"]:assert sha(ROOT/f"figures/{name}.{ext}")==item[ext+"_sha256"]
    unique={h for info in pdfs.values() for h in info["page_png_sha256"].values()}
    unique_body={h for info in pdfs.values() for name,h in info["page_png_sha256"].items() if name!="page-001.png"}
    output={"source_sha256":sha(ROOT/"drafts/question-05.md"),"source_quality_sha256":sha(ROOT/"build/source-quality-q05.json"),
            "verification_sha256":sha(ROOT/"build/question-05-verification.json"),
            "geometry_sha256":sha(ROOT/"build/question-05-figure-geometry.json"),"template_sha256":template,
            "pdfs":pdfs,"figures_review_data":geo["figures"],"identical_page_reuse":identical,
            "original_images":original_images,"qpdf_checks":qpdf,"logs":logs,
            "bound_sha256":{rel:sha(ROOT/rel) for rel in paths},
            "student":qa["questions"][0]["student"],"teacher":qa["questions"][0]["teacher"],
            "symbolic_count":physics["symbolic_count"],"numeric_count":physics["numeric_count"],
            "max_normalized_error":physics["max_normalized_error"],"geometry_checks":geo["check_count"],
            "unique_pages":len(unique),"unique_body_pages":len(unique_body),
            "remaining_model_issues":physics["remaining_model_issues"],"actual_visual_review_inferred":False}
    print(json.dumps(output,ensure_ascii=False))
if __name__=="__main__":main()

