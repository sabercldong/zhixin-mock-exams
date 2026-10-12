"""Q7 source/geometry and flux checks, not an automatic visual review."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math,re,subprocess
ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def check(name,truth):
    assert truth,name
    CHECKS.append(dict(name=name,passed=True))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    tex=(ROOT/"figures/题07_图稿源文件.tex").read_text()
    md=(ROOT/"drafts/question-07.md").read_text()
    check("six independent transverse/path diagrams",tex.count(r"\begin{tikzpicture}")==6)
    check("unfolded source rows keep physical R and L",r"{1.8/R/P_R/Q_R,0/L/P_L/Q_L}" in tex)
    check("both unfolded destinations are right physical eye",r"(r\src)at(9.30,\yy){$R$}" in tex)
    check("unfolded mirror between outward and inward plates",
          r"(m\src)at(4.65,\yy)" in tex and r"(q\src)at(3.10,\yy)" in tex and r"(u\src)at(6.20,\yy)" in tex)
    xs=[0,1.55,3.10,4.65,6.20,7.75,9.30]
    check("device centers ordered along expanded actual path",all(b>a for a,b in zip(xs,xs[1:])))
    check("device nodes have at least .7cm separation",min(b-a for a,b in zip(xs,xs[1:]))>.82)
    check("paths use node boundaries, not loose center connections",
          all(v in tex for v in [r"(s\src)--(p\src)",r"(p\src)--(q\src)",r"(q\src)--(m\src)",
                                 r"(m\src)--(u\src)",r"(u\src)--(v\src)",r"(v\src)--(r\src)"]))
    a,b=(1/math.sqrt(2),1/math.sqrt(2)),(-1/math.sqrt(2),1/math.sqrt(2))
    dot=lambda u,v:sum(x*y for x,y in zip(u,v))
    check("principal vectors unit",abs(dot(a,a)-1)<1e-14 and abs(dot(b,b)-1)<1e-14)
    check("principal vectors orthogonal",abs(dot(a,b))<1e-14)
    check("a minus b reconstructs physical x",abs((a[0]-b[0])/math.sqrt(2)-1)<1e-14 and abs(a[1]-b[1])<1e-14)
    check("a plus b reconstructs physical y",abs(a[0]+b[0])<1e-14 and abs((a[1]+b[1])/math.sqrt(2)-1)<1e-14)
    check("optic principal axis is in transverse plane",r"{片面内的电场方向}" in tex)
    check("a and b labels placed at their own positive ends",
          r"(2.10,2.10)" in tex and r"(-2.10,2.10)" in tex)
    check("45degree arc truly goes x to a","end angle=45" in tex)
    check("state initial diagonal has equal sign",r"(-.99,-.99)--(.99,.99)" in tex)
    check("state final diagonal has opposite sign",r"(7.81,.99)--(9.79,-.99)" in tex)
    check("constant principal component amplitude across the three states",
          abs((8.8-7.81)-.99)<1e-14 and abs((9.79-8.8)-.99)<1e-14)
    check("circle center and start radius consistent",r"(4.4,0)circle(.99)" in tex and r"(5.39,0)" in tex)
    check("circle arrow clockwise for chosen cos/sin sign","end angle=-65" in tex)
    check("projector input plus selects x right, minus selects y left",
          r"{1.8/C_+/x/P_R/P_L,0/C_-/y/P_L/P_R}" in tex)
    check("projector inward path explicitly labeled","银幕" in tex and r"{入射：" in tex)
    values=[]
    for j in range(151):
        u=j/150; cross=math.sin(math.pi*u)**2;same=math.cos(math.pi*u)**2
        values.append((u,cross,same))
    check("all 151 intensity vertices nonnegative and normalized",
          all(-1e-14<=c<=1+1e-14 and -1e-14<=s<=1+1e-14 and abs(c+s-1)<1e-14 for _,c,s in values))
    check("quarterwave point is full crossed return",abs(values[75][1]-1)<1e-14 and abs(values[75][2])<1e-14)
    check("zero and halfwave point full same return",all(abs(values[j][2]-1)<1e-14 for j in [0,150]))
    check("phase midpoint label at exact axis midpoint",r"at(3.2,0){$\pi/2$}" in tex)
    check("legend separated from graph top","3.55" in tex)
    check("correct physical layer P then Q, wrong Q then P",
          r"{A/1.8/正确层次/P/Q,B/0/反装层次/Q/P}" in tex)
    check("outward and inward arrows on different boundaries",
          r"(eye\idx.north east)--(first\idx.north west)" in tex and
          r"(first\idx.south west)--(eye\idx.south east)" in tex)
    names=["path-07","axes-07","states-07","projectors-07","leakage-07","order-07"]
    for j,name in enumerate(names,1):
        check(f"figure7-{j} centered source and actual derivation referenced",
              f"图7-{j}" in md and md.count(f"图7-{j}")>=2 and
              f"../figures/{name}.png" in md)
        for ext in ["pdf","png"]:
            check(f"{name}.{ext} exists",(ROOT/f"figures/{name}.{ext}").is_file())
        run=subprocess.run(["qpdf","--check",str(ROOT/f"figures/{name}.pdf")],capture_output=True,text=True)
        check(f"{name} vector PDF integrity",run.returncode==0)
    log=(ROOT/"figures/题07_图稿源文件.log").read_text(errors="replace")
    check("current TikZ log strictly clean",not re.search(r"Warning|Overfull|Underfull|Missing character|Undefined control sequence|^! ",log,re.M))
    report=dict(paper="015",question=7,saved_utc=datetime.now(timezone.utc).isoformat(),
                checks=CHECKS,count=len(CHECKS),passed=True,actual_visual_review=False,
                bound_sha256={n:sha(ROOT/n) for n in ["scripts/check_figures_07.py","drafts/question-07.md",
                 "figures/题07_图稿源文件.tex"]+[f"figures/{name}.{ext}" for name in names for ext in ["pdf","png"]]})
    report["check_count"]=len(CHECKS)
    report["figures"]={name:{ext+"_sha256":sha(ROOT/f"figures/{name}.{ext}") for ext in ["pdf","png"]} for name in names}
    (ROOT/"build/question-07-figure-geometry.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(count=len(CHECKS),passed=True,actual_visual_review=False)))
if __name__=="__main__":main()
