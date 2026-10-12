"""Q4 graph/topology/geometry checks; rendering never certifies actual visual review."""
from pathlib import Path
import re,json,hashlib,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
NAMES=["question-04","circuit-04","geometry-04","forces-04","power-04","regulation-04"]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=ROOT/"figures/题04_图稿源文件.tex";tex=source.read_text();checks=[]
    def check(name,test,details=None):
        assert test,(name,details)
        checks.append({"name":name,"passed":True,"details":details or {}})
    check("six vector pictures",tex.count(r"\begin{tikzpicture}")==6)
    check("common top/bottom nodes of heater and shunt",
          "(0,3)--(4.4,3)" in tex and "(0,0)--(4.4,0)" in tex and
          "(2,3)--(2,2.18)" in tex and "(2,1.15)--(2,0)" in tex and
          "(4.4,1.15)--(4.4,0)" in tex)
    check("manual K on source branch; K_t on shunt",
          "(0,2.35)--(0,2.68)" in tex and "(4.4,2.32)--(4.14,2.64)" in tex
          and "(4.4,2.32)--(4.4,2.73)" in tex)
    check("heater explicitly inside box and both panels share R0",
          "(.65,.53)--(.90,.53)" in tex and tex.count(r"{$R_0$}")>=2)
    check("spring endpoints join moving plate and control rod",
          "(1.5,3.31)--(1.5,3.43)" in tex and "(1.5,4.45)--(1.5,4.57)" in tex)
    l0=4.73-3.15;x=4.73-4.30;z=3.52-3.15
    check("independent x/z spring shortening",
          abs((l0-x-z)-(4.30-3.52))<1e-12 and
          "(.46,3.52)--(.46,4.30)" in tex,
          {"drawing_l0":l0,"rod_down":x,"plate_up":z,"spring_length":l0-x-z})
    check("rigid rod length constant",
          abs((3.04-1.76)-(3.41-2.13))<1e-12,
          {"initial_rod":3.04-1.76,"moved_rod":3.41-2.13})
    check("piston and plate move same distance",
          abs((2.02-1.65)-z)<1e-12,
          {"piston_up":2.02-1.65,"plate_up":z})
    check("fixed trigger is reference line not a falsely detached electrical contact",
          "(-.75,3.15)--(7.2,3.15)" in tex and
          "(.40,3.15)--(.84,3.15)" not in tex)
    check("force resultant collinear and opposite",
          "(0,.02)--(0,1.55)" in tex and "(0,-.02)--(0,-1.55)" in tex and
          r"$(p-p_0)S_0$" in tex and r"$k(x+z)$" in tex)
    for name,T,P,cx,cy in [("low",325,25,3.25,3),("target",330,30,3.9,3.6),("high",336,36,4.68,4.32)]:
        check("power graph "+name,abs(cx-.13*(T-300))<1e-12 and abs(cy-.12*P)<1e-12,
              {"temperature":T,"power":P,"drawing_point":[cx,cy]})
    check("actual power graph lines",
          "(0,3.00)--(5.2,3.00)" in tex and "(0,4.32)--(5.2,4.32)" in tex
          and "(0,0)--(5.2,4.80)" in tex)
    points=[(0,325),(1,325),(1.44,336),(2.102941176,336)]
    coords=[(0,.75),(3.4,.75),(4.896,2.4),(7.15,2.4)]
    check("regulation graph mechanical slope and saturation",
          all(abs(cx-3.4*xx)<2e-9 and abs(cy-.15*(tt-320))<1e-12
              for (xx,tt),(cx,cy) in zip(points,coords))
          and "(0,.75)--(3.4,.75)--(4.896,2.4)--(7.15,2.4)" in tex
          and r"\node[left]at(0,0){$320$}" in tex,
          {"physical_points":points,"graph_points":coords})
    check("330 K graph target inside controllable segment",
          abs(4.08-3.4*1.2)<1e-12 and abs(1.5-.15*(330-320))<1e-12
          and "(4.08,1.5)" in tex)
    figures={}
    for name in NAMES:
        pdf=ROOT/f"figures/{name}.pdf";png=pdf.with_suffix(".png")
        subprocess.run(["qpdf","--check",str(pdf)],capture_output=True,check=True)
        with fitz.open(pdf) as doc:
            check(name+" actual vector single-page",len(doc)==1 and len(doc[0].get_drawings())>0)
        figures[name]={"pdf_sha256":sha(pdf),"png_sha256":sha(png)}
    collection=source.with_suffix(".pdf")
    subprocess.run(["qpdf","--check",str(collection)],capture_output=True,check=True)
    warnings=re.findall(r"(?m)^.*(?:Warning|Underfull|Overfull|Missing character|^!).*$",source.with_suffix(".log").read_text())
    check("current figure compilation log clean",not warnings,{"warnings":warnings})
    report={"question":"04","checks":checks,"check_count":len(checks),"source_sha256":sha(source),
            "collection_sha256":sha(collection),"program_sha256":sha(Path(__file__)),
            "renderer_sha256":sha(ROOT/"scripts/render_figures_04.py"),"figures":figures,
            "passed":True,"actual_visual_review_inferred":False,"question_accepted":False,"set_accepted":False}
    (ROOT/"build/question-04-figure-geometry.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"check_count":len(checks),"passed":True,"question_accepted":False}))
if __name__=="__main__": main()
