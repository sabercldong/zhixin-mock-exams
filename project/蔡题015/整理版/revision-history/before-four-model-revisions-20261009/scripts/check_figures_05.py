"""Q5 true-coordinate and force/3D projection checks; does not certify visual reading."""
from pathlib import Path
import hashlib,json,math,re,subprocess
import numpy as np
import fitz
from verify_question_05 import numerical_branch
ROOT=Path(__file__).resolve().parents[1]
NAMES=["question-05","normals-05","curvature-05","auxiliary-05","perturbation-05","space-05"]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=ROOT/"figures/题05_图稿源文件.tex";tex=source.read_text();checks=[]
    def check(name,test,details=None):
        assert test,(name,details)
        checks.append({"name":name,"passed":True,"details":details})
    macros={k:float(v) for k,v in re.findall(r"\\def\\([A-Za-z]+)\{([-0-9.]+)\}",tex)}
    a=3.;b=math.sqrt(6);rho=16/(3*math.sqrt(3));d=2*math.sqrt(3)
    A=np.array([-math.sqrt(3),2.,0.]);B=np.array([math.sqrt(3),2.,0.]);P=np.array([0.,-1.,0.])
    nA=(P-A)/d;nB=(P-B)/d
    O1=A+rho*nA;O2=B+rho*nB
    check("six separate physical/auxiliary pictures",tex.count(r"\begin{tikzpicture}")==6)
    check("actual bead is inside original steel",P[0]**2/a**2+P[1]**2/b**2<1 and P[1]>-b,
          {"bead":P.tolist(),"steel_bottom":-b})
    for tag,V,n in [("left",A,nA),("right",B,nB)]:
        t=np.array([-a*V[1]/b,b*V[0]/a,0.])
        check(tag+" ring normal and string collinear",abs((P-V)@t)<1e-12)
    drawn_ring_F=np.array([.65,-1.12583,0.]);drawn_ring_N=np.array([-.65,1.12583,0.])
    check("drawn ring forces originate at ring and oppose along its normal",
          np.linalg.norm(drawn_ring_F+drawn_ring_N)<1e-12
          and np.linalg.norm(np.cross(drawn_ring_F,nA))<1e-5
          and r"(0,0)--(.65,-1.12583)" in tex and r"(0,0)--(-.65,1.12583)" in tex)
    check("drawn bead force arrows balance and attach to bead",
          np.linalg.norm(np.array([-.625,1.08253])+np.array([.625,1.08253])+np.array([0.,-2.16506]))<1e-12
          and r"(0,0)--(-.625,1.08253)" in tex and r"(0,0)--(.625,1.08253)" in tex
          and r"(0,0)--(0,-2.16506)" in tex)
    check("bead equal tensions support gravity",np.linalg.norm(-(nA+nB)/math.sqrt(3)-np.array([0.,1.,0.]))<1e-12)
    check("center between each ring and bead",0<rho<d and np.allclose(O1,[-1/(3*math.sqrt(3)),-2/3,0.]))
    check("both osculating centers belong to the proper corresponding ring",np.allclose(O2,[1/(3*math.sqrt(3)),-2/3,0.]))
    check("local arcs not huge full circles",r"domain=111:130" in tex and r"domain=50:69" in tex)
    check("auxiliary semiaxes/center agree with actual lower bead",abs(macros["ae"]-(d-rho))<1e-14 and
          abs(macros["ce"]-1/(3*math.sqrt(3)))<1e-14 and abs(macros["be"]-1/3)<1e-14)
    check("auxiliary markers not enlarged into disks",r"circle(.23pt)" in tex and r"circle(.34pt)" in tex)
    q,qx,state=numerical_branch(a,b,macros["pertX"])
    Ap=np.array([macros["pertXA"],macros["pertYA"],0.]);Bp=np.array([macros["pertXB"],macros["pertYB"],0.])
    Pp=np.array([macros["pertX"],macros["pertY"],0.])
    check("perturbed points are roots of original normal and length equations",np.allclose(Ap,state[3],atol=1e-13) and np.allclose(Bp,state[4],atol=1e-13) and abs(Pp[1]-q[2])<1e-13,
          {"A":Ap.tolist(),"B":Bp.tolist(),"P":Pp.tolist(),"normal_length_residuals":state[0].tolist()})
    check("both rings move left with left down and right up",Ap[0]<A[0] and Bp[0]<B[0] and Ap[1]<A[1] and Bp[1]>B[1])
    lA=np.linalg.norm(Pp-Ap);lB=np.linalg.norm(Pp-Bp)
    check("one real segment longer and one shorter at fixed total length",lA>d and lB<d and abs(lA+lB-2*d)<1e-12,{"lengths":[lA,lB]})
    check("bead zoom preserves x and y uniform scale",r"50*\pertX" in tex and r"50*(\pertY+1)" in tex and "plot({50*" not in tex)
    As=np.array([macros["spaceXA"],macros["spaceYA"],0.]);Bs=np.array([macros["spaceXB"],macros["spaceYB"],0.])
    Ps=np.array([0.,macros["spaceY"],macros["spaceW"]])
    for tag,V in [("A",As),("B",Bs)]:
        tangent=np.array([-a*V[1]/b,b*V[0]/a,0.])
        check("3D "+tag+" belongs to actual steel",abs(V[0]**2/a**2+V[1]**2/b**2-1)<1e-12)
        check("3D "+tag+" string perpendicular to steel tangent",abs((Ps-V)@tangent)<1e-12)
    check("3D snapshot preserves total length",abs(np.linalg.norm(Ps-As)+np.linalg.norm(Ps-Bs)-2*d)<1e-12)
    ca=math.cos(math.radians(50));sa=math.sin(math.radians(50));cp=math.cos(math.radians(30));sp=math.sin(math.radians(30))
    projector=np.array([[ca,0,sa],[sp*sa,cp,-sp*ca]])
    check("orthographic projection has orthonormal image rows",np.allclose(projector@projector.T,np.eye(2),atol=1e-14))
    screenP=projector@Ps;wireX=screenP[0]/ca;wireY=-b*math.sqrt(1-wireX**2/a**2)
    lower=projector@np.array([wireX,wireY,0.])
    check("space bead does not visually coincide with lower steel boundary",screenP[1]-lower[1]>.4,
          {"projected_bead":screenP.tolist(),"steel_same_screen_x":lower.tolist(),"vertical_clearance":screenP[1]-lower[1]})
    check("explicit 3D basis and plane projection connector",
          r"x={(.64278761cm,.38302222cm)}" in tex and r"z={(.76604444cm,-.32139380cm)}" in tex
          and r"(Ppr)--(Ps)" in tex and r"(As)--(Ps)--(Bs)" in tex)
    check("projection label offset from string",r"(Ppr)--(-.70,-1.18,0)" in tex)
    figures={}
    for name in NAMES:
        pdf=ROOT/f"figures/{name}.pdf";png=pdf.with_suffix(".png")
        subprocess.run(["qpdf","--check",str(pdf)],capture_output=True,check=True)
        with fitz.open(pdf) as doc:check(name+" vector single page",len(doc)==1 and len(doc[0].get_drawings())>0)
        figures[name]={"pdf_sha256":sha(pdf),"png_sha256":sha(png)}
    collection=source.with_suffix(".pdf")
    subprocess.run(["qpdf","--check",str(collection)],capture_output=True,check=True)
    warnings=re.findall(r"(?m)^.*(?:Warning|Underfull|Overfull|Missing character|^!).*$",source.with_suffix(".log").read_text())
    check("current figure log clean",not warnings,{"warnings":warnings})
    report={"question":"05","checks":checks,"check_count":len(checks),"passed":True,
            "source_sha256":sha(source),"collection_sha256":sha(collection),"program_sha256":sha(Path(__file__)),
            "renderer_sha256":sha(ROOT/"scripts/render_figures_05.py"),"figures":figures,
            "actual_visual_review_inferred":False,"model_condition_resolved":False,"question_accepted":False,"set_accepted":False}
    (ROOT/"build/question-05-figure-geometry.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"check_count":len(checks),"passed":True,"question_accepted":False}))
if __name__=="__main__":main()
