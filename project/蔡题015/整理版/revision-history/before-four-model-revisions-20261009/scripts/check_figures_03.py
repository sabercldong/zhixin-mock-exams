"""q03 geometry and artifact checks; no automatic visual/PDF acceptance."""
from pathlib import Path
import hashlib, json, math, re, subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
NAMES=["question-03","material-03","domain-03","particle-03","supports-03","pressure-03"]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    source=ROOT/"figures/题03_图稿源文件.tex"
    tex=source.read_text()
    checks=[]
    def check(name,condition,details):
        if not condition:raise AssertionError((name,details))
        checks.append({"name":name,"passed":True,"details":details})
    check("six actual tikzpictures",tex.count(r"\begin{tikzpicture}")==6,{})
    check("question sand endpoints touch paper",
          "(-4,0).. controls" in tex and "..(0,0)--cycle;" in tex and
          "(-4.15,0)--(3.75,0)" in tex,{})
    l,s1,s2=4.,1.7,2.3
    check("question centroid distances",abs(s1+s2-l)<1e-12,
          {"left":-4,"right":0,"centroid":-2.3,"s1":s1,"s2":s2})
    check("original oblique force retained pending user",
          "(3.75,.055)--(5,1.02)" in tex,
          {"model_condition_resolved":False,"oblique_direction":[1.25,.965]})
    check("conditional translation and material location",
          "(-2.5,0)rectangle(1.5,1.04)" in tex and
          "(.43,0)rectangle(.57,1.03)" in tex and abs(1.5-1.-.5)<1e-12,
          {"l":4,"y":1.5,"x":1,"lab_position_y_minus_x":.5})
    check("conditional force is horizontal","(3.3,0)--(4.6,0)" in tex,{})
    check("Fubini upper triangular domain",
          "(0,0)--(0,4)--(4,4)--cycle;" in tex and
          "(1.15,1.15)--(1.15,4)" in tex and "(0,2.5)--(2.5,2.5)" in tex,
          {"conditions":"0<=x<=y<=l","vertical_section":"x<=y<=l"})
    check("particle two path lengths",
          "(-2,1.04)--(0,1.04)" in tex and "(0,1.04)--(2,1.04)" in tex,
          {"x":2,"l_minus_x":2,"l":4})
    check("two support contacts and reaction action points",
          "(-3,.04)..controls" in tex and "..(1,.04)" in tex and
          "(-3,.04)--(-3,.799)" in tex and "(1,.04)--(1,.601)" in tex,
          {"left_contact":[-3,.04],"right_contact":[1,.04],"paper_height":.04})
    gravity=.65-(-.67); nl=.799-.04; nr=.601-.04
    check("force arrow magnitudes obey equilibrium and torque",
          abs(nl+nr-gravity)<1e-12 and
          abs(nr*l-gravity*s1)<1e-12 and
          abs(nl/gravity-s2/l)<1e-12,
          {"gravity_arrow_length":gravity,"left_reaction_length":nl,
           "right_reaction_length":nr,"force_residual":nl+nr-gravity,
           "torque_residual":nr*l-gravity*s1})
    a,b=.45,.2
    pressures=[1+a*(2*u-1)+b*(6*u*u-6*u+1) for u in [i/400 for i in range(401)]]
    check("pressure is positive and its centroid matches other figures",
          min(pressures)>0 and abs(.5+a/6-s2/l)<1e-12 and
          ".45*(2*\\x/4-1)+.2*(6*(\\x/4)^2-6*\\x/4+1)" in tex,
          {"sampled_min_normalized_pressure":min(pressures),"centroid_fraction":.5+a/6})
    figures={}
    for name in NAMES:
        pdf=ROOT/f"figures/{name}.pdf";png=pdf.with_suffix(".png")
        subprocess.run(["qpdf","--check",str(pdf)],capture_output=True,check=True)
        with fitz.open(pdf) as doc:
            check(name+" single vector page",len(doc)==1 and len(doc[0].get_drawings())>0,{})
        figures[name]={"pdf_sha256":sha(pdf),"png_sha256":sha(png)}
    collection=source.with_suffix(".pdf")
    subprocess.run(["qpdf","--check",str(collection)],capture_output=True,check=True)
    log=source.with_suffix(".log")
    issues=[line for line in log.read_text().splitlines()
            if any(q in line for q in ["Overfull","Underfull","Missing character",
                                      "Warning","Undefined control sequence","! "])]
    check("current collection log has no listed layout/compiler warnings",not issues,{"issues":issues})
    report={"question":"03","checks":checks,"check_count":len(checks),
            "source_sha256":sha(source),"collection_sha256":sha(collection),
            "renderer_sha256":sha(ROOT/"scripts/render_figures_03.py"),
            "program_sha256":sha(Path(__file__)),"figures":figures,
            "passed":True,"actual_visual_review_inferred":False,
            "model_condition_resolved":False,"question_accepted":False,"set_accepted":False}
    (ROOT/"build/question-03-figure-geometry.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"check_count":len(checks),"passed":True,
                      "question_accepted":False},ensure_ascii=False))

if __name__=="__main__":main()

