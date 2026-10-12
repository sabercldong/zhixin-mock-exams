"""Independent q03 model and route prechecks. No document/PDF acceptance."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math
import numpy as np
from scipy.integrate import quad
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
symbolic, numeric = [], []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def exact(name, expression):
    residual = sp.simplify(expression)
    if residual != 0:
        raise AssertionError((name, residual))
    symbolic.append({"name": name, "residual": str(residual)})

def close(name, value, expected, tol=3e-10):
    error = abs(value-expected)/max(1.0, abs(expected))
    if error > tol:
        raise AssertionError((name, value, expected, error))
    numeric.append({"name": name, "value": float(value),
                    "expected": float(expected), "normalized_error": float(error)})

def main():
    x, y, l, m, g = sp.symbols("x y l m g", positive=True)
    a, b, c = sp.symbols("a b c", real=True)
    mu1, mu2 = sp.symbols("mu_1 mu_2", nonnegative=True)
    u = x/l
    density = m/l*(1+a*(2*u-1)+b*(6*u**2-6*u+1))
    mass = sp.integrate(density, (x, 0, l))
    moment = sp.integrate(x*density, (x, 0, l))
    s2 = moment/m
    s1 = l-s2
    right_mass = sp.integrate(density, (x, 0, y))
    nested_mass = sp.integrate(right_mass, (y, 0, l))
    exchanged_mass = sp.integrate((l-x)*density, (x, 0, l))
    exact("mass normalization", mass-m)
    exact("centroid from integral", s2-l*(sp.Rational(1,2)+a/6))
    exact("two centroid distances", s1+s2-l)
    exact("Fubini on actual polynomial density", nested_mass-exchanged_mass)
    exact("integrated right mass is m*s1", nested_mass-m*s1)
    work = sp.integrate(g*(mu1*(m-right_mass)+mu2*right_mass), (y, 0, l))
    target = m*g*(mu1*s2+mu2*s1)
    exact("full work and mass moments", work-target)
    exact("equal friction limit", target.subs(mu2, mu1)-mu1*m*g*l)
    exact("density shape b does not affect centroid/work", sp.diff(work,b))
    exact("left-end reaction and vertical balance",
          m*g*s2/l+m*g*s1/l-m*g)
    exact("two reactions and moment about left end",
          m*g*s1/l*l-m*g*s1)
    exact("two-end friction work", l*(mu1*m*g*s2/l+mu2*m*g*s1/l)-target)

    # Continuous positive pressure family with constant mass/first moment
    # but redistribution depending on displacement. It demonstrates that
    # equilibrium alone is not a proof of a unique pressure history.
    z = sp.symbols("z", real=True)
    p2 = 6*u**2-6*u+1
    pressure = m*g/l*(1+c*sp.sin(2*sp.pi*y/l)*p2)
    exact("varying pressure has constant resultant",
          sp.integrate(pressure, (x,0,l))-m*g)
    exact("varying pressure has constant first moment",
          sp.integrate(x*pressure, (x,0,l))-m*g*l/2)
    right_pressure = sp.integrate(pressure, (x,0,y))
    varied_work = sp.integrate(mu1*(m*g-right_pressure)+mu2*right_pressure, (y,0,l))
    counter = m*g*l*((mu1+mu2)/2+(mu2-mu1)*3*c/(2*sp.pi**3))
    exact("redistributing continuous pressure actual double integral", varied_work-counter)
    exact("fixed-profile work recovered at c=0",
          varied_work.subs(c,0)-m*g*l*(mu1+mu2)/2)
    exact("nonzero redistribution correction",
          sp.diff(varied_work,c)-m*g*l*(mu2-mu1)*3/(2*sp.pi**3))

    # Three-point family, also satisfying static equations at every displacement.
    t = sp.Rational(1,4)+c*sp.sin(2*sp.pi*y/l)
    reactions = (m*g*t, m*g*(1-2*t), m*g*t)
    exact("three supports total load", sum(reactions)-m*g)
    exact("three supports first moment",
          reactions[1]*l/2+reactions[2]*l-m*g*l/2)
    three_area = sp.integrate(reactions[0],(y,0,l/2))+sp.integrate(
        reactions[0]+reactions[1],(y,l/2,l))
    exact("three supports displacement integral", three_area-m*g*l*(sp.Rational(1,2)+2*c/sp.pi))

    # These force equations only check the claimed horizontal, flat,
    # quasistatic submodel; not a complete flexible-paper oblique-pull model.
    alpha = sp.symbols("alpha", real=True)
    mu = sp.symbols("mu", positive=True)
    fh = mu*m*g/(1+mu*sp.tan(alpha))
    force = fh/sp.cos(alpha)
    normal = m*g-force*sp.sin(alpha)
    exact("inclined force vertical balance", normal+force*sp.sin(alpha)-m*g)
    exact("inclined force horizontal balance", fh-mu*normal)
    exact("inclined force horizontal-pull limit",
          fh.subs(alpha,0)-mu*m*g)

    # All four solved variants use independently integrated inputs.
    triangular = 2*m*x/l**2
    exact("variant 1 triangular mass", sp.integrate(triangular,(x,0,l))-m)
    exact("variant 1 triangular centroid", sp.integrate(x*triangular,(x,0,l))/m-2*l/3)
    triangular_force = g*(mu1*m+(mu2-mu1)*sp.integrate(triangular,(x,0,y)))
    exact("variant 1 actual force integral", sp.integrate(triangular_force,(y,0,l))-m*g*l*(2*mu1+mu2)/3)
    d = sp.symbols("d", nonnegative=True)
    partial = sp.integrate(g*(mu1*m+(mu2-mu1)*m*y/l),(y,0,d))
    exact("variant 2 partial displacement uniform", partial-m*g*(mu1*d+(mu2-mu1)*d**2/(2*l)))
    partial_correction = (mu2-mu1)*m*g*b/l*sp.integrate((d-x)*p2,(x,0,d))
    exact("variant 2 equal-centroid different-profile correction",
          partial_correction-(mu2-mu1)*m*g*b*d**2*(l-d)**2/(2*l**3))
    exact("variant 2 half displacement correction", partial_correction.subs(d,l/2)-(mu2-mu1)*m*g*b*l/32)
    mu3 = sp.symbols("mu_3", nonnegative=True)
    three_region_work = sp.integrate(g*density*(mu1*x+mu2*l+mu3*(l-x)),(x,0,l))
    exact("variant 3 three region path integration",three_region_work-m*g*(mu1*s2+mu2*l+mu3*s1))
    k=2*sp.pi
    a1=sp.integrate(z*sp.sin(k*z),(z,0,1))
    a2=sp.integrate(z**2*sp.sin(k*z),(z,0,1))
    a3=sp.integrate(z**3*sp.sin(k*z),(z,0,1))
    exact("variant 4 first integration by parts",a1+1/k)
    exact("variant 4 second integration by parts",a2+1/k)
    exact("variant 4 third integration by parts",a3+1/k-6/k**3)
    exact("variant 4 combined sine integral",2*a3-3*a2+a1-3/(2*sp.pi**3))

    # Direct numerical motion integration, not substitution into final W.
    for case,(av,bv,mv,lv,mu1v,mu2v) in enumerate([
        (-.7,.12,2.3,1.4,.20,.65),
        (.6,.25,1.7,.80,.55,.10),
        (0,.45,3.1,2.0,.30,.30),
        (.2,-.22,.9,1.6,0,.72),
        (-.3,.10,4.2,.60,.82,0),
        (.5,0,2.1,1.1,.04,.93),
    ],1):
        gv=9.81
        fn=lambda xv: mv/lv*(1+av*(2*xv/lv-1)+bv*(6*(xv/lv)**2-6*xv/lv+1))
        massv=quad(fn,0,lv,epsabs=1e-12)[0]
        s2v=quad(lambda xv:xv*fn(xv),0,lv,epsabs=1e-12)[0]/massv
        def pulling_force(yv):
            mr=quad(fn,0,yv,epsabs=1e-11)[0]
            return gv*(mu1v*(massv-mr)+mu2v*mr)
        direct=quad(pulling_force,0,lv,epsabs=1e-10)[0]
        close(f"density {case} mass",massv,mv)
        close(f"density {case} centroid",s2v,lv*(.5+av/6))
        close(f"density {case} motion-force work",direct,mv*gv*(mu1v*s2v+mu2v*(lv-s2v)))
        material_work=quad(lambda xv:gv*fn(xv)*(mu1v*xv+mu2v*(lv-xv)),0,lv)[0]
        close(f"density {case} motion vs independent material-path work",direct,material_work)
        values=np.array([fn(xx) for xx in np.linspace(0,lv,301)])
        if min(values)<0: raise AssertionError("density nonphysical")

    # Arbitrary positive point loads: direct region changes over every segment.
    rng=np.random.default_rng(1503)
    for case in range(12):
        lv=float(rng.uniform(.4,2))
        pos=np.sort(rng.uniform(0,lv,17))
        weights=rng.uniform(.01,1,17); weights/=weights.sum()
        mv=float(rng.uniform(.4,5)); weights*=mv*9.81
        mu1v,mu2v=rng.uniform(0,1,2)
        bounds=np.r_[0,pos,lv]
        motion=0.
        for left,right in zip(bounds[:-1],bounds[1:]):
            yv=(left+right)/2
            moved=weights[pos<yv].sum()
            motion+=(right-left)*(mu1v*(weights.sum()-moved)+mu2v*moved)
        centroid=np.dot(pos,weights)/weights.sum()
        expected=weights.sum()*(mu1v*centroid+mu2v*(lv-centroid))
        close(f"point pressure {case+1} piecewise motion work",motion,expected)

    # Smooth pressure counterfamilies: force, moment, positivity and nested
    # quadrature are independently evaluated at real displacement values.
    for case,cv in enumerate([-.5,-.2,0,.2,.5],1):
        mv,lv,gv,mu1v,mu2v=2.6,1.3,9.81,.17,.74
        def n(xv,yv):
            uv=xv/lv
            return mv*gv/lv*(1+cv*math.sin(2*math.pi*yv/lv)*(6*uv*uv-6*uv+1))
        for j,yv in enumerate(np.linspace(0,lv,7)):
            close(f"continuous {case} total reaction {j}",
                  quad(lambda xv:n(xv,yv),0,lv)[0],mv*gv)
            close(f"continuous {case} first moment {j}",
                  quad(lambda xv:xv*n(xv,yv),0,lv)[0],mv*gv*lv/2)
            if min(n(xx,yv) for xx in np.linspace(0,lv,201))<=0:
                raise AssertionError("pressure should remain positive")
        def f(yv):
            nr=quad(lambda xv:n(xv,yv),0,yv)[0]
            return mu1v*(mv*gv-nr)+mu2v*nr
        actual=quad(f,0,lv,epsabs=1e-10)[0]
        expected=mv*gv*lv*((mu1v+mu2v)/2+(mu2v-mu1v)*3*cv/(2*math.pi**3))
        close(f"continuous {case} actual work integral",actual,expected)
    for cv in [-.25,-.1,0,.1,.25]:
        def tnum(yv): return .25+cv*math.sin(2*math.pi*yv)
        actual=quad(tnum,0,.5)[0]+quad(lambda yy:1-tnum(yy),.5,1)[0]
        close(f"three points c={cv} right-load integral",actual,.5+2*cv/math.pi)

    close("variant 1 numerical full force curve",
          quad(lambda yy:20*(.2+.3*(yy/.6)**2),0,.6)[0],3.6)
    for frac in [.1,.25,.5,.75,1.]:
        lv,mv,gv,mu1v,mu2v=1.7,2.3,9.81,.12,.79
        dv=frac*lv
        direct=quad(lambda yy:gv*(mu1v*mv+(mu2v-mu1v)*quad(lambda xx:mv/lv,0,yy)[0]),0,dv)[0]
        close(f"variant 2 partial motion {frac}",direct,mv*gv*(mu1v*dv+(mu2v-mu1v)*dv*dv/(2*lv)))
        bval=.45
        def f_profile(yy):
            right=quad(lambda xx:mv/lv*(1+bval*(6*(xx/lv)**2-6*xx/lv+1)),0,yy)[0]
            return gv*(mu1v*mv+(mu2v-mu1v)*right)
        changed=quad(f_profile,0,dv)[0]
        difference=(mu2v-mu1v)*mv*gv*bval*dv**2*(lv-dv)**2/(2*lv**3)
        close(f"variant 2 actual equal-centroid difference {frac}",changed-direct,difference)
    for case in range(9):
        lv=float(rng.uniform(.4,2))
        pos=np.sort(rng.uniform(0,lv,19))
        weights=rng.uniform(.01,1,19); weights/=weights.sum()
        weights*=float(rng.uniform(.4,5))*9.81
        mus=rng.uniform(0,1,3)
        bounds=np.sort(np.r_[0,pos,pos+lv,2*lv])
        actual=0.
        for left,right in zip(bounds[:-1],bounds[1:]):
            yy=(left+right)/2
            locations=yy-pos
            coeff=np.where(locations<0,mus[0],np.where(locations<lv,mus[1],mus[2]))
            actual+=(right-left)*np.dot(weights,coeff)
        centroid=np.dot(pos,weights)/weights.sum()
        target3=weights.sum()*(mus[0]*centroid+mus[1]*lv+mus[2]*(lv-centroid))
        close(f"variant 3 actual three-region motion {case+1}",actual,target3)
    close("variant 3 stated numerical example",20*(.1*.3+.4*.5+.25*.2),5.6)
    counter_direct=quad(lambda zz:20*(.2+.4*(zz+.5*math.sin(2*math.pi*zz)*(2*zz**3-3*zz**2+zz))),0,1)[0]
    close("variant 4 stated numerical pressure-motion integral",counter_direct,8+6/math.pi**3)

    report={
        "question":"03","stage":"source/model preverification only",
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "symbolic_checks":symbolic,"numeric_checks":numeric,
        "symbolic_count":len(symbolic),"numeric_count":len(numeric),
        "verified_math":True,
        "max_normalized_error":max(v["normalized_error"] for v in numeric),
        "correct_hand_route":"fixed normal load profile: W=mg*(mu1*s2+mu2*s1)",
        "counterexample_scope":"positive continuous reaction histories satisfy force and moment balance; equilibrium alone does not determine pressure history; no claim of a specified elastic support realizing every history",
        "inclined_scope":"vertical-force balance disproves unqualified N=mg under inclined pull; full flexible-paper path/work requires more conditions",
        "question_complete":False,"model_condition_resolved":False,
        "question_accepted":False,"set_accepted":False,
        "program_sha256":sha(Path(__file__)),
        "manuscript_sha256":sha(ROOT/"drafts/question-03.md"),
        "source_details":json.loads((ROOT/"preview/originals/question-03-detail-manifest.json").read_text()),
    }
    dest=ROOT/"build/question-03-preverification.json"
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["symbolic_count","numeric_count","max_normalized_error","question_complete","model_condition_resolved"]},ensure_ascii=False))

if __name__=="__main__":
    main()
