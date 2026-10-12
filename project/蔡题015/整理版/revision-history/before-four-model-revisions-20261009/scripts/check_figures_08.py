"""Q8 actual coordinates, vector angles, spacetime events and files; not visual review."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,re,subprocess
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def check(n,x):
    assert x,n
    CHECKS.append(dict(name=n,passed=True))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    tex=(ROOT/"figures/题08_图稿源文件.tex").read_text()
    md=(ROOT/"drafts/question-08.md").read_text()
    check("six necessary space and solution diagrams",tex.count(r"\begin{tikzpicture}")==6)
    normal=np.array([4,6,4])/math.sqrt(68)
    horizontal=np.array([3,-2,0])/math.sqrt(13)
    vertical=np.cross(horizontal,normal)
    projection=np.stack([horizontal,vertical])
    check("true camera unit normal",abs(np.linalg.norm(normal)-1)<1e-14)
    check("orthonormal screen basis",np.linalg.norm(projection@projection.T-np.eye(2))<1e-14)
    check("screen transverse to camera",np.linalg.norm(projection@normal)<1e-14)
    rounded=np.array([[.8320503,-.5547002,0],[-.2690691,-.4036037,.8744746]])
    check("TikZ basis matches actual orthographic coordinates",np.max(abs(rounded-projection))<8e-8)
    e=np.array([2,1.2,1.6]); para=np.array([2,0,0]); perp=np.array([0,1.2,1.6])
    check("space field exactly sum of parallel and transverse",np.linalg.norm(e-para-perp)==0)
    check("space field retains both nonzero y z coordinates",np.count_nonzero(perp)==2)
    check("projection parallelogram closes",np.linalg.norm(projection@e-projection@para-projection@perp)<1e-14)
    check("transverse vector truly perpendicular to velocity",np.dot(para,perp)==0)
    check("actual yz plane shading not a flat x y construction",r"(0,2.5,2.6)" in tex and r"z={(0cm,.8744746cm)}" in tex)
    check("field diagram gamma two explicit",r"{\gamma=2}" in tex or r"$\gamma=2$" in tex)
    theta=math.atan(.5); vartheta=math.atan(1)
    check("first field tilt comes from gamma not gamma squared",abs(vartheta-math.atan(2*math.tan(theta)))<1e-14)
    beta=.6; ga=1/math.sqrt(1-beta*beta)
    a,b,apr,bpr=np.array([1.2,2]),np.array([2.8,2]),np.array([.75,1.25]),np.array([3.25,2.75])
    transform=lambda event:ga*np.array([event[0]-beta*event[1],event[1]-beta*event[0]])
    check("lab simultaneous A B really same ct",a[1]==b[1])
    check("same lab time longitudinal contraction",abs((b-a)[0]-2/ga)<1e-14)
    check("A B lie on their own actual worldlines",abs(a[0]-beta*a[1])<1e-14 and abs(b[0]-beta*b[1]-1.6)<1e-14)
    check("primed simultaneous pair same proper time",abs(transform(apr)[1]-transform(bpr)[1])<1e-14)
    check("primed simultaneous proper separation two",abs((transform(bpr)-transform(apr))[0]-2)<1e-14)
    check("primed simultaneous pair lab times differ",abs(bpr[1]-apr[1]-1.5)<1e-14)
    check("lab simultaneous pair proper times differ by minus beta length",abs((transform(b)-transform(a))[1]+beta*2)<1e-14)
    check("event annotations placed away from continuing worldlines",
          r"below right] at (Apr)" in tex and r"above left] at (Bpr)" in tex)
    check("spacetime horizontal extent leaves a text gap",r"x=1.3cm,y=.92cm" in tex)
    check("dipole transverse stays same while parallel contracts",r"{0/{S'}/2,5.8/{S}/1}" in tex)
    check("dipole vector goes negative to positive charge",r"(0,0)--(\endx,2)" in tex and r"at (0,0) {$-q$}" in tex and r"at (\endx,2) {$+q$}" in tex)
    check("primed x label used only in primed panels",tex.count(r"$x'$\else $x$")>=1 and tex.count(r"$x$\else $x'$")>=1)
    ef=np.array([2.683282,1.341641]);pf=np.array([1.341641,2.683282])
    check("angle diagram vectors actual gamma two optimum",np.max(abs(pf-np.diag([.5,2])@ef))<2e-6)
    th=math.atan2(ef[1],ef[0]);ps=math.atan2(pf[1],pf[0]);de=ps-th
    check("angle diagram theta psi complementary",abs(th+ps-math.pi/2)<1e-14)
    check("angle diagram delta correct",abs(de-math.atan(.75))<2e-7)
    vals=[]
    for j in range(361):
        theta=math.radians(j/2)
        e=np.array([math.cos(theta),math.sin(theta)])
        p=np.diag([.5,2])@e
        value=math.degrees(math.atan2(abs(e[0]*p[1]-e[1]*p[0]),np.dot(e,p)))
        vals.append(value)
    check("all curve vertices bounded nonnegative",all(-1e-12<=v<=math.degrees(math.atan(.75))+1e-12 for v in vals))
    check("curve full obtuse mirror symmetric",max(abs(vals[j]-vals[360-j]) for j in range(361))<5e-13)
    check("curve three zero angle directions",max(vals[j] for j in [0,180,360])<1e-12)
    check("curve near exact maxima",abs(max(vals)-math.degrees(math.atan(.75)))<.001)
    check("curve uses degree trigonometric PGF coordinates","samples=361" in tex and "atan(3*abs(sin(" in tex)
    check("right optimum annotation does not collide with 180 tick",r"(153.434949,-7)" in tex and r"at (\xx,-1)" in tex)
    names=["space-08","field-08","simultaneity-08","dipole-08","angles-08","maximum-08"]
    for j,name in enumerate(names,1):
        check(f"figure8-{j} referred in actual derivation",md.count(f"图8-{j}")>=2 and f"../figures/{name}.png" in md)
        for ext in ["pdf","png"]:check(name+"."+ext+" exists",(ROOT/f"figures/{name}.{ext}").is_file())
        run=subprocess.run(["qpdf","--check",str(ROOT/f"figures/{name}.pdf")],capture_output=True)
        check(name+" vector integrity",run.returncode==0)
    log=(ROOT/"figures/题08_图稿源文件.log").read_text(errors="replace")
    check("current TikZ log strictly clean",not re.search(r"Warning|Overfull|Underfull|Missing character|Undefined control sequence|^! ",log,re.M))
    report=dict(paper="015",question=8,saved_utc=datetime.now(timezone.utc).isoformat(),checks=CHECKS,
        count=len(CHECKS),check_count=len(CHECKS),passed=True,actual_visual_review=False,
        bound_sha256={n:sha(ROOT/n) for n in ["scripts/check_figures_08.py","drafts/question-08.md","figures/题08_图稿源文件.tex"]
                      +[f"figures/{name}.{ext}" for name in names for ext in ["pdf","png"]]},
        figures={name:{ext+"_sha256":sha(ROOT/f"figures/{name}.{ext}") for ext in ["pdf","png"]} for name in names})
    (ROOT/"build/question-08-figure-geometry.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(count=len(CHECKS),passed=True,actual_visual_review=False)))
if __name__=="__main__":main()
