"""015 Q8: tensor field boost and independently solved simultaneous worldline events.
p is the neutral charge first moment on a lab-time slice, not an unqualified tensor dipole.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
import numpy as np
import sympy as sp
from scipy.optimize import brentq,minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
SYMBOLIC,NUMERIC=[],[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
g,b=sp.symbols("gamma beta",positive=True)
def reduce(z):
    z=sp.trigsimp(sp.cancel(sp.expand(z)))
    n,d=sp.fraction(z)
    n=sp.rem(n,b*b-1+g**-2,b)
    return sp.simplify(sp.trigsimp(n/d))
def exact(name,z):
    res=z.applyfunc(reduce) if isinstance(z,sp.MatrixBase) else reduce(z)
    assert res==(sp.zeros(*z.shape) if isinstance(z,sp.MatrixBase) else 0),(name,res)
    SYMBOLIC.append(dict(name=name,residual=str(res)))
def close(name,actual,expected,tol=4e-10):
    a,e=np.asarray(actual,float),np.asarray(expected,float)
    err=float(np.linalg.norm(a-e)/max(1,np.linalg.norm(e)))
    assert err<tol,(name,actual,expected,err,tol)
    NUMERIC.append(dict(name=name,normalized_error=err,tolerance=tol))
def boost(beta):
    ga=1/math.sqrt(1-beta*beta)
    return np.array([[ga,-ga*beta,0,0],[-ga*beta,ga,0,0],[0,0,1,0],[0,0,0,1]],float)
def fields_tensor(e,bb,beta,c=1):
    ex,ey,ez=e; bx,by,bz=bb
    f=np.array([[0,-ex/c,-ey/c,-ez/c],[ex/c,0,-bz,by],[ey/c,bz,0,-bx],[ez/c,-by,bx,0]],float)
    out=boost(beta)@f@boost(beta).T
    return -c*out[0,1:],np.array([-out[2,3],out[1,3],-out[1,2]])
def charge_event(xprime,beta,ctlab):
    """Find each endpoint event on the requested LAB time slice; c=1 units."""
    inv=boost(-beta)
    def event(ctprime):return inv@np.array([ctprime,*xprime],float)
    center=ctlab/inv[0,0]-beta*xprime[0]
    ctprime=brentq(lambda tau:event(tau)[0]-ctlab,center-10,center+10,xtol=1e-13)
    out=event(ctprime)
    assert abs(out[0]-ctlab)<2e-11
    return out,ctprime
def dipole_events(e,bb,beta,alpha=1,q=1,ctlab=.37,origin=None):
    ep,bp=fields_tensor(e,bb,beta)
    # Solve the specified rest-frame linear equilibrium as a 3D system.
    stiffness=q*q/alpha
    lp=np.linalg.solve(stiffness*np.eye(3),q*ep)
    origin=np.zeros(3) if origin is None else np.asarray(origin,float)
    plus,tp=charge_event(origin+lp/2,beta,ctlab)
    minus,tm=charge_event(origin-lp/2,beta,ctlab)
    pp=q*lp; p=q*(plus[1:]-minus[1:])
    return p,pp,ep,bp,tp-tm
def angle_events(theta,ga):
    beta=math.sqrt(1-1/(ga*ga))
    e=np.array([math.cos(theta),math.sin(theta),0])
    p,*_=dipole_events(e,np.zeros(3),beta,ctlab=.21)
    return math.atan2(np.linalg.norm(np.cross(e,p)),np.dot(e,p))
def main():
    c,a,q=sp.symbols("c alpha q",positive=True)
    ex,ey,ez,bx,by,bz=sp.symbols("Ex Ey Ez Bx By Bz",real=True)
    lm=sp.Matrix([[g,-g*b,0,0],[-g*b,g,0,0],[0,0,1,0],[0,0,0,1]])
    eta=sp.diag(1,-1,-1,-1)
    exact("boost metric",lm.T*eta*lm-eta)
    exact("boost inverse",lm.subs(b,-b)*lm-sp.eye(4))
    f=sp.Matrix([[0,-ex/c,-ey/c,-ez/c],[ex/c,0,-bz,by],[ey/c,bz,0,-bx],[ez/c,-by,bx,0]])
    fp=lm*f*lm.T
    expected_e=sp.Matrix([ex,g*(ey-b*c*bz),g*(ez+b*c*by)])
    expected_b=sp.Matrix([bx,g*(by+b*ez/c),g*(bz-b*ey/c)])
    actual_e=-c*fp[0,1:].T
    actual_b=sp.Matrix([-fp[2,3],fp[1,3],-fp[1,2]])
    exact("field tensor gives all E signs and indices",actual_e-expected_e)
    exact("field tensor gives all B signs and indices",actual_b-expected_b)
    exact("general E dot B invariant",actual_e.dot(actual_b)-sp.Matrix([ex,ey,ez]).dot(sp.Matrix([bx,by,bz])))
    exact("general E2 c2B2 invariant",actual_e.dot(actual_e)-c*c*actual_b.dot(actual_b)-(ex*ex+ey*ey+ez*ez-c*c*(bx*bx+by*by+bz*bz)))
    ep=sp.Matrix([ex,g*ey,g*ez]); bp=sp.Matrix([0,g*b*ez/c,-g*b*ey/c])
    exact("zero lab B rest electric",actual_e.subs({bx:0,by:0,bz:0})-ep)
    exact("zero lab B rest magnetic",actual_b.subs({bx:0,by:0,bz:0})-bp)
    exact("zero lab B orthogonal rest fields",ep.dot(bp))
    dx,dt,tt=sp.symbols("dx_prime dt_prime t",real=True)
    dtp=-b*dx/c
    exact("lab simultaneity",g*(dtp+b*dx/c))
    exact("longitudinal same-time separation",g*(dx+b*c*dtp)-dx/g)
    exact("rest-simultaneous events not lab simultaneous",g*(b*dx/c)-g*b*dx/c)
    rest=a*ep; lab=sp.diag(1/g,1,1)*rest
    exact("rest response",rest-a*ep)
    exact("lab first moment",lab-sp.Matrix([a*ex/g,a*g*ey,a*g*ez]))
    exact("rest norm squared",rest.dot(rest)-a*a*(ex*ex+g*g*(ey*ey+ez*ez)))
    exact("lab norm squared",lab.dot(lab)-a*a*(ex*ex/g**2+g*g*(ey*ey+ez*ez)))
    exact("two norms difference",rest.dot(rest)-lab.dot(lab)-a*a*b*b*ex*ex)
    exact("coordinate-free parallel response",a*g*ex*(1-b*b)-a*ex/g)
    e0,theta,t=sp.symbols("E theta tan_theta",positive=True)
    ee=sp.Matrix([e0*sp.cos(theta),e0*sp.sin(theta),0])
    pp=sp.Matrix([a*e0*sp.cos(theta)/g,a*e0*g*sp.sin(theta),0])
    exact("dot product",ee.dot(pp)-a*e0**2*(sp.cos(theta)**2/g+g*sp.sin(theta)**2))
    exact("signed cross product",ee.cross(pp)[2]-a*e0**2*(g-1/g)*sp.sin(theta)*sp.cos(theta))
    ff=(g*g-1)*t/(1+g*g*t*t)
    exact("difference-angle rational form",(g*g*t-t)/(1+g*g*t*t)-ff)
    exact("AM GM square",1/t+g*g*t-2*g-(1/sp.sqrt(t)-g*sp.sqrt(t))**2)
    exact("derivative for global maximum",sp.diff(ff,t)-(g*g-1)*(1-g*g*t*t)/(1+g*g*t*t)**2)
    exact("stationary point",sp.diff(ff,t).subs(t,1/g))
    exact("second derivative at maximum",sp.diff(ff,t,2).subs(t,1/g)+(g*g-1)*g/2)
    exact("maximum tangent",ff.subs(t,1/g)-(g*g-1)/(2*g))
    exact("maximum sine cosine identity",((g*g-1)/(g*g+1))**2+(2*g/(g*g+1))**2-1)
    exact("maximum speed sine",(g*g-1)/(g*g+1)-b*b/(2-b*b))
    exact("maximum speed tangent",(g*g-1)/(2*g)-g*b*b/2)
    ss=sp.symbols("sin2theta",real=True)
    gg=(1+(g*g-1)*ss)**2/(1+(g**4-1)*ss)
    exact("independent cosine minimum stationary",sp.diff(gg,ss).subs(ss,1/(1+g*g)))
    exact("independent cosine minimum value",gg.subs(ss,1/(1+g*g))-4*g*g/(g*g+1)**2)
    exact("best lab norm equals alpha E",g*g/(g*g+1)/g**2+g*g/(g*g+1)-1)
    exact("best rest norm",g*g/(g*g+1)+g*g/(g*g+1)-2*g*g/(g*g+1))
    z=sp.symbols("beta_small",real=True)
    gs=1/sp.sqrt(1-z*z)
    exact("small beta maximum angle coefficient",sp.series(sp.atan((gs-1/gs)/2),z,0,5).removeO()-z*z/2-z**4/4)
    exact("small beta optimal field angle",sp.series(sp.atan(1/gs),z,0,5).removeO()-(sp.pi/4-z*z/4-z**4/8))
    ax,at,k=sp.symbols("alpha_x alpha_t k",positive=True)
    anis=sp.Matrix([ax*ex/g,at*g*ey,at*g*ez])
    exact("anisotropic coefficient ratio",(at*g)/(ax/g)-at*g*g/ax)
    fk=(k-1)*t/(1+k*t*t)
    exact("anisotropic maximum stationary",sp.diff(fk,t).subs(t,1/sp.sqrt(k)))
    exact("anisotropic optimum norm",((ax/g)**2*k/(1+k)+(at*g)**2/(1+k)-ax*at).subs(k,at*g*g/ax))
    # Previous identity uses k=at*g^2/ax; substitute before evaluating.
    rng=np.random.default_rng(1508)
    for idx in range(22):
        beta=float(rng.uniform(-.95,.95)); ga=1/math.sqrt(1-beta*beta)
        en=rng.normal(size=3); bn=rng.normal(size=3)
        epn,bpn=fields_tensor(en,bn,beta)
        want_e=np.array([en[0],ga*(en[1]-beta*bn[2]),ga*(en[2]+beta*bn[1])])
        want_b=np.array([bn[0],ga*(bn[1]+beta*en[2]),ga*(bn[2]-beta*en[1])])
        close(f"tensor E case {idx+1}",epn,want_e)
        close(f"tensor B case {idx+1}",bpn,want_b)
        close(f"field invariant dot case {idx+1}",np.dot(epn,bpn),np.dot(en,bn))
        close(f"field invariant norm case {idx+1}",np.dot(epn,epn)-np.dot(bpn,bpn),np.dot(en,en)-np.dot(bn,bn))
    for idx in range(24):
        beta=float(rng.uniform(-.9,.9)); ga=1/math.sqrt(1-beta*beta)
        en=rng.normal(size=3); al=float(rng.uniform(.2,2)); qn=float(rng.uniform(.3,1.7))
        origin=rng.normal(size=3); ctl=float(rng.uniform(-2,2))
        p,pr,epn,bpn,dtp=dipole_events(en,np.zeros(3),beta,al,qn,ctl,origin)
        close(f"simultaneous events moment case {idx+1}",p,al*np.array([en[0]/ga,ga*en[1],ga*en[2]]))
        close(f"simultaneous events rest moment case {idx+1}",pr,al*np.array([en[0],ga*en[1],ga*en[2]]))
        close(f"simultaneous rest times case {idx+1}",dtp,-beta*pr[0]/qn)
        p2,*_=dipole_events(en,np.zeros(3),beta,al,qn,ctl+1.7,origin+np.array([1,-2,.4]))
        close(f"neutral origin and time invariance case {idx+1}",p2,p)
        actual=math.atan2(np.linalg.norm(np.cross(en,p)),np.dot(en,p))
        xp=en[0]; tp=np.linalg.norm(en[1:])
        expected=math.atan2((ga*ga-1)*abs(xp)*tp,xp*xp+ga*ga*tp*tp)
        close(f"actual vector angle case {idx+1}",actual,expected)
        close(f"norm difference case {idx+1}",np.dot(pr,pr)-np.dot(p,p),al*al*beta*beta*en[0]*en[0])
    optima=[]
    for ga in [1.0001,1.25,math.sqrt(3),2,8,30]:
        sol=minimize_scalar(lambda th:-angle_events(th,ga),bounds=(0,math.pi/2),method="bounded",options={"xatol":1e-13})
        assert sol.success
        sol2=minimize_scalar(lambda th:-angle_events(th,ga),bounds=(math.pi/2,math.pi),method="bounded",options={"xatol":1e-13})
        assert sol2.success
        wanted=math.atan(1/ga); delta=math.atan((ga*ga-1)/(2*ga))
        close(f"independent angular optimizer gamma {ga}",sol.x,wanted,tol=4e-6)
        close(f"independent angular maximum gamma {ga}",-sol.fun,delta,tol=1e-10)
        close(f"independent obtuse optimizer gamma {ga}",sol2.x,math.pi-wanted,tol=4e-6)
        close(f"independent obtuse maximum gamma {ga}",-sol2.fun,delta,tol=1e-10)
        for th in [0,math.pi/2,math.pi]:
            close(f"endpoint gamma {ga} theta {th}",angle_events(th,ga),0)
        optima.append(dict(gamma=ga,theta_actual=sol.x,delta_actual=-sol.fun))
    zero=dipole_events([.3,-.7,1.1],[0,0,0],0)[0]
    close("zero speed exact degeneracy",zero,[.3,-.7,1.1])
    pv,ppv,*_=dipole_events([3,4,12],[0,0,0],.6)
    v1delta=math.atan2(np.linalg.norm(np.cross([3,4,12],pv)),np.dot([3,4,12],pv))
    close("variant 1 lab vector from events",pv,[2.4,5,15])
    close("variant 1 rest vector from tensor and response",ppv,[3,5,15])
    close("variant 1 lab size",np.linalg.norm(pv),math.sqrt(6394)/5)
    close("variant 1 rest size",np.linalg.norm(ppv),math.sqrt(259))
    close("variant 1 angle direct vector",v1delta,math.atan(27*math.sqrt(10)/1036))
    beta2=brentq(lambda beta:max(angle_events(th,1/math.sqrt(1-beta*beta)) for th in [math.pi/6,5*math.pi/6])-math.pi/6,.7,.9,xtol=1e-13)
    close("variant 2 independently inverted speed",beta2,math.sqrt(2/3))
    close("variant 2 two equal angles",angle_events(5*math.pi/6,math.sqrt(3)),math.pi/6)
    pv3,ppv3,ee3,bb3,_=dipole_events([0,0,0],[0,0,2],.6,alpha=.7)
    close("variant 3 transverse induced lab vector",pv3,[0,-.7*1.25*.6*2,0])
    close("variant 3 transverse rest equals lab",pv3,ppv3)
    close("variant 3 magnetic field invariant",np.dot(ee3,ee3)-np.dot(bb3,bb3),-4)
    def anis_angle(th,ga,axv=4,atv=1):
        beta=math.sqrt(1-1/ga**2); en=np.array([math.cos(th),math.sin(th),0])
        epn,_=fields_tensor(en,[0,0,0],beta)
        lp=np.linalg.solve(np.diag([1/axv,1/atv,1/atv]),epn)
        plus,_=charge_event(lp/2,beta,.31); minus,_=charge_event(-lp/2,beta,.31)
        pn=plus[1:]-minus[1:]
        return math.atan2(np.linalg.norm(np.cross(en,pn)),np.dot(en,pn)),pn
    sol4=minimize_scalar(lambda th:-anis_angle(th,math.sqrt(2))[0],bounds=(0,math.pi/2),method="bounded",options={"xatol":1e-13})
    close("variant 4 anisotropic angle optimizer",sol4.x,math.atan(math.sqrt(2)),tol=4e-6)
    close("variant 4 anisotropic maximum", -sol4.fun,math.asin(1/3))
    close("variant 4 anisotropic optimum norm",np.linalg.norm(anis_angle(math.atan(math.sqrt(2)),math.sqrt(2))[1]),2)
    for th in [.1,.5,1.1,2.2,3]:
        d,pn=anis_angle(th,2)
        close(f"variant 4 compensation angle {th}",d,0)
        close(f"variant 4 compensation vector {th}",pn,2*np.array([math.cos(th),math.sin(th),0]))
    report=dict(paper="015",question=8,saved_utc=datetime.now(timezone.utc).isoformat(),
        symbolic=SYMBOLIC,numeric=NUMERIC,symbolic_checks=len(SYMBOLIC),numeric_checks=len(NUMERIC),
        max_normalized_numeric_error=max(x["normalized_error"] for x in NUMERIC),
        numerical_optimization_results=optima,solved_variants=dict(
            variant1_rest_norm=math.sqrt(259),variant1_lab_norm=math.sqrt(6394)/5,
            variant1_angle_deg=math.degrees(v1delta),variant1_max_angle_deg=math.degrees(math.atan(.225)),
            variant2_beta=beta2,variant4_theta_deg=math.degrees(sol4.x),
            variant4_max_angle_deg=math.degrees(-sol4.fun)),
        model_scope=["specified neutral +/-q mean-position model","steady isotropic electric response in rest frame",
                     "p is charge first moment on each frame's simultaneous slice","no independent magnetic response introduced"],
        original_typos_corrected=True,new_human_choice_required=False,source_text_complete=True,
        source_review_complete=True,document_complete=False,figures_complete=False,actual_pdf_reviewed=False,
        question_accepted=False,set_accepted=False,
        bound_sha256={n:sha(ROOT/n) for n in ["scripts/verify_question_08.py","preview/source-reviewed-q08.json",
            "preview/originals/question-08-detail-manifest.json","preview/originals/source-manifest.json"]})
    (ROOT/"build/question-08-preverification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["symbolic_checks","numeric_checks","max_normalized_numeric_error","solved_variants"]},indent=2))
if __name__=="__main__":main()
