"""015 Q7 independent phase propagation, real fields and incoherent light checks.
Fixed lab x/y; exp(+i omega t); delta=2pi(n_a-n_b)d/lambda_0.
Return through a reciprocal wave plate adds the same eigenmode phases.
Near-normal ideal mirror is rI. The scope is explicit, not a real-broadband claim.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[1]
SYMBOLIC, NUMERIC=[],[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(name, expr):
    if isinstance(expr, sp.MatrixBase):
        res=expr.applyfunc(lambda z:sp.simplify(sp.expand_complex(sp.expand_trig(z))))
        assert res==sp.zeros(*expr.shape),(name,res)
    else:
        res=sp.simplify(sp.trigsimp(sp.expand_complex(expr),method="fu")); assert res==0,(name,res)
    SYMBOLIC.append(dict(name=name,residual=str(res)))
def close(name,actual,expected,tol=3e-10):
    error=float(np.linalg.norm(np.asarray(actual)-np.asarray(expected))/max(1,np.linalg.norm(np.asarray(expected))))
    assert error<=tol,(name,actual,expected,error)
    NUMERIC.append(dict(name=name,normalized_error=error))
def rotate(a):
    return np.array([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]],complex)
def propagation(e,chi,delta):
    f=rotate(chi); common=.73
    generator=f@np.diag([common,common+delta])@f.T
    sol=solve_ivp(lambda z,v:1j*generator@v,(0,1),np.asarray(e,complex),method="DOP853",rtol=2e-12,atol=2e-13)
    assert sol.success
    return sol.y[:,-1]*np.exp(-1j*common)
def main():
    chi,delta,alpha,t=sp.symbols("chi delta alpha t",real=True)
    c,s=sp.cos(chi),sp.sin(chi); f=sp.Matrix([[c,-s],[s,c]])
    q=f*sp.diag(1,sp.exp(sp.I*delta))*f.T
    pr,pl=sp.diag(1,0),sp.diag(0,1); eye=sp.eye(2)
    x,y=sp.Matrix([1,0]),sp.Matrix([0,1])
    cp,cm=sp.Matrix([1,sp.I])/sp.sqrt(2),sp.Matrix([1,-sp.I])/sp.sqrt(2)
    exact("principal axes orthonormal",f.T*f-eye)
    exact("right polarizer idempotent",pr*pr-pr)
    exact("left polarizer idempotent",pl*pl-pl)
    exact("orthogonal polarizers block",pr*pl)
    exact("polarizer resolution of identity",pr+pl-eye)
    exact("plate conserves intensity",q.conjugate().T*q-eye)
    exact("same fixed-frame reciprocal return matrix",q.T-q)
    exact("two traversals double eigenphase",q*q-f*sp.diag(1,sp.exp(2*sp.I*delta))*f.T)
    q45=q.subs({chi:sp.pi/4,delta:sp.pi/2})
    exact("quarter-wave 45 degree matrix",q45-sp.Matrix([[1+sp.I,1-sp.I],[1-sp.I,1+sp.I]])/2)
    exact("double pass swaps linear axes",q45*q45-sp.Matrix([[0,1],[1,0]]))
    exact("old right source",pr*eye*pr-pr)
    exact("old left source",pr*eye*pl)
    exact("new right source blocked",pr*q45*q45*pr)
    exact("new left source reaches right detector",pr*q45*q45*pl-sp.Matrix([[0,1],[0,0]]))
    exact("incoming right circular",q45*cp-sp.exp(sp.I*sp.pi/4)*x)
    exact("incoming left circular",q45*cm-sp.exp(-sp.I*sp.pi/4)*y)
    exact("outgoing right other fixed circular vector",q45*x-sp.exp(sp.I*sp.pi/4)*cm)
    exact("outgoing left other fixed circular vector",q45*y-sp.exp(-sp.I*sp.pi/4)*cp)
    exact("circular states orthogonal",(cp.conjugate().T*cm)[0])
    exact("mirror common phase preserves polarization",(-eye).conjugate().T*(-eye)-eye)
    before=sp.Matrix([sp.cos(t),sp.cos(t)])/sp.sqrt(2)
    final=sp.Matrix([sp.cos(t+sp.pi),sp.cos(t+2*sp.pi)])/sp.sqrt(2)
    exact("hand phase route perpendicular",(before.T*final)[0])
    exact("circular constant field length",(sp.cos(t)**2+sp.cos(t+sp.pi/2)**2)/2-sp.Rational(1,2))
    cross=(q*q)[1,0]; g=sp.sin(2*chi)**2*sp.sin(delta)**2
    exact("general cross intensity",sp.expand_complex(cross*sp.conjugate(cross))-g)
    same=(q*q)[0,0]
    exact("general same intensity",sp.expand_complex(same*sp.conjugate(same))-(1-g))
    exact("unit return flux",1-g+g-1)
    exact("phase leakage at 45 degrees",(1-g).subs(chi,sp.pi/4)-sp.cos(delta)**2)
    exact("angle leakage for quarter-wave",(1-g).subs(delta,sp.pi/2)-sp.cos(2*chi)**2)
    e1,e2=sp.symbols("e1 e2",real=True)
    leakage=(1-g).subs({chi:sp.pi/4+e1,delta:sp.pi/2+e2})
    exact("angle Taylor coefficient",sp.diff(leakage,e1,2).subs({e1:0,e2:0})/2-4)
    exact("phase Taylor coefficient",sp.diff(leakage,e2,2).subs({e1:0,e2:0})/2-1)
    exact("mixed Taylor coefficient",sp.diff(leakage,e1,e2).subs({e1:0,e2:0}))
    fa=sp.Matrix([[sp.cos(alpha),-sp.sin(alpha)],[sp.sin(alpha),sp.cos(alpha)]])
    exact("local circular phase under head rotation",fa.T*cp-sp.exp(sp.I*alpha)*cp)
    exact("tilted linear right channel",(x.T*fa.T*x)[0]**2-sp.cos(alpha)**2)
    exact("tilted linear leakage",(y.T*fa.T*x)[0]**2-sp.sin(alpha)**2)
    exact("swapped layers same source",q45*pr*pr*q45-q45*pr*q45)
    exact("swapped layers opposite source",q45*pr*pl*q45)
    j0=eye/2
    exact("natural light first polarizer half",sp.trace(pr*j0*pr)-sp.Rational(1,2))
    wrong=q45*pr*pr*q45
    exact("swapped natural source power",sp.trace(wrong*j0*wrong.conjugate().T)-sp.Rational(1,2))
    exact("outside polarizer both circular half",(pr*cp).norm()**2-sp.Rational(1,2))
    exact("inside plate cannot restore blocked signal",(q45*pr*cm).norm()**2-sp.Rational(1,2))
    exact("outside left polarizer plus phase",pl*cp-sp.I*y/sp.sqrt(2))
    exact("outside left polarizer minus phase",pl*cm+sp.I*y/sp.sqrt(2))
    exact("inside plate left plus power",(q45*pl*cp).norm()**2-sp.Rational(1,2))
    exact("inside plate left minus power",(q45*pl*cm).norm()**2-sp.Rational(1,2))
    exact("wrong layer equal input contrast",(sp.Rational(1,2)-sp.Rational(1,2))/(sp.Rational(1,2)+sp.Rational(1,2)))
    na,nb,d,lam=sp.symbols("na nb d lambda_0",positive=True)
    exact("signed physical phase",-2*sp.pi*nb*d/lam+2*sp.pi*na*d/lam-2*sp.pi*(na-nb)*d/lam)
    dn=sp.symbols("dn",positive=True)
    exact("lowest quarter-wave thickness",2*sp.pi*dn*(lam/(4*dn))/lam-sp.pi/2)
    rng=np.random.default_rng(1507)
    for k in range(18):
        a=float(rng.uniform(-math.pi,math.pi)); de=float(rng.uniform(-3*math.pi,3*math.pi))
        fn=rotate(a); qn=fn@np.diag([1,np.exp(1j*de)])@fn.T
        for label,v in [("right",np.array([1.,0.])),("left",np.array([0.,1.]))]:
            outward=propagation(v,a,de); returned=propagation(-outward,a,de)
            close(f"ODE {k+1} {label} complex return",returned,-qn@qn@v)
            cross_power=math.sin(2*a)**2*math.sin(de)**2
            wanted=1-cross_power if label=="right" else cross_power
            close(f"ODE {k+1} {label} detected return",abs(returned[0])**2,wanted)
            close(f"ODE {k+1} {label} conserved flux",np.vdot(returned,returned).real,1)
    times=np.linspace(0,2*math.pi,4096,endpoint=False)
    for k,de in enumerate([math.pi/2,-math.pi/2,3*math.pi/2,.3,1.2,2.4]):
        principal=np.vstack([np.cos(times+math.pi),np.cos(times+math.pi+2*de)])/math.sqrt(2)
        plus=(principal[0]+principal[1])/math.sqrt(2); minus=(principal[0]-principal[1])/math.sqrt(2)
        close(f"real fields {k+1} same mean",2*np.mean(plus**2),math.cos(de)**2)
        close(f"real fields {k+1} cross mean",2*np.mean(minus**2),math.sin(de)**2)
    qn=np.array(q45,complex); prn,pln=np.diag([1,0]),np.diag([0,1])
    initial=np.vstack([np.cos(times),np.sin(times)]).astype(complex)
    paths={"old right":prn@prn,"old left":prn@pln,"new right":prn@qn@qn@prn,
           "new left":prn@qn@qn@pln,"wrong order right":qn@prn@prn@qn,
           "wrong order left":qn@prn@pln@qn}
    for label,operator in paths.items():
        value=float(np.mean(np.sum(abs(operator@initial)**2,axis=0)))
        close(f"natural ensemble {label}",value,.5 if label in ["old right","new left","wrong order right"] else 0)
    cpn,cmn=np.array([1,1j])/math.sqrt(2),np.array([1,-1j])/math.sqrt(2)
    for label,incoming in [("plus",cpn),("minus",cmn)]:
        for analyzer,p in [("right",prn),("left",pln)]:
            actual=propagation(p@incoming,math.pi/4,math.pi/2)
            close(f"wrong layers {label} {analyzer} actual phase flow",np.vdot(actual,actual).real,.5)
    for degrees in [-75,-30,0,15,45,80]:
        a=math.radians(degrees)
        for label,incoming,wanted in [("right",cpn,1),("left",cmn,0)]:
            local=rotate(a).T@incoming; after=propagation(local,math.pi/4,math.pi/2)
            close(f"head {degrees} circular {label}",abs(after[0])**2,wanted)
        local=rotate(a).T@np.array([1.,0.])
        close(f"head {degrees} linear leakage",abs(local[1])**2,math.sin(a)**2)
    lam0,dnv=550e-9,.0090; thickness=lam0/(4*dnv); phase650=2*math.pi*dnv*thickness/650e-9
    re650=propagation(propagation([1,0],math.pi/4,phase650),math.pi/4,phase650)
    close("variant physical thickness",4*dnv*thickness,lam0)
    close("variant 650nm same leakage ODE",abs(re650[0])**2,math.cos(phase650)**2)
    a40=math.radians(40); re40=propagation(propagation([1,0],a40,math.pi/2),a40,math.pi/2)
    close("variant 40 degree leakage ODE",abs(re40[0])**2,math.cos(2*a40)**2)
    for ec,ed in [(1e-4,2e-4),(2e-4,-1e-4),(-1e-4,0)]:
        value=1-math.sin(2*(math.pi/4+ec))**2*math.sin(math.pi/2+ed)**2
        approx=4*ec**2+ed**2; assert abs(value-approx)<2e-14
        close(f"small error expansion {ec}/{ed}",value,approx)
    variants=dict(lowest_order_thickness_m=thickness,lowest_order_thickness_um=thickness*1e6,
                  phase650_rad=phase650,same650_fraction=math.cos(phase650)**2,cross650_fraction=math.sin(phase650)**2,
                  angle40_same_fraction=math.cos(2*a40)**2,angle40_cross_fraction=math.sin(2*a40)**2,
                  old_head_30degree_leak_fraction=math.sin(math.pi/6)**2)
    report=dict(paper="015",question=7,saved_utc=datetime.now(timezone.utc).isoformat(),
                original_results=dict(old_glasses="opened physical right eye",new_glasses="closed physical left eye"),
                ideal_scope=["ideal orthogonal polarizers","lossless reciprocal quarter-wave plates","normal plate incidence",
                             "near-normal nondepolarizing mirror rI","fixed lab axes; exp(+i omega t); delta=+pi/2",
                             "opposite propagation: screen incoming vs face outgoing"],
                assumed_human_model_change=False,new_human_choice_required=False,
                symbolic=SYMBOLIC,numeric=NUMERIC,symbolic_checks=len(SYMBOLIC),numeric_checks=len(NUMERIC),
                max_normalized_numeric_error=max(v["normalized_error"] for v in NUMERIC),solved_variants=variants,
                bound_sha256={n:sha(ROOT/n) for n in ["scripts/verify_question_07.py","preview/source-reviewed-q07.json",
                 "preview/originals/question-07-detail-manifest.json","preview/originals/source-manifest.json"]},
                source_review_complete=True,document_complete=False,figures_complete=False,
                actual_pdf_reviewed=False,question_accepted=False,set_accepted=False)
    (ROOT/"build/question-07-preverification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["symbolic_checks","numeric_checks","max_normalized_numeric_error","solved_variants"]},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
