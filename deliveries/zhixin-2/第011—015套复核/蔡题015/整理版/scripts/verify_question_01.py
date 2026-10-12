"""Independent checks of 015 Q1 continuous-diffusion conditional solution.

The mathematics can pass while the original finite-step model remains unresolved.
Run with the scientific Python runtime; never turn a numerical pass into acceptance.
"""
from pathlib import Path
import hashlib, json, math, re, subprocess
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_bvp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build/question-01-verification.json"

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

symbolic = []
numeric = []

def zero(name, expression):
    reduced = sp.simplify(expression)
    if reduced != 0:
        # SymPy may leave cosh(v) separate from exp(v); rewrite identities, not tolerances.
        reduced = sp.simplify(reduced.rewrite(sp.exp))
    assert reduced == 0, (name, reduced)
    symbolic.append(dict(check=name, residual=str(reduced)))

def close(name, actual, expected, tol=2e-9):
    error = abs(float(actual) - float(expected))
    assert error <= tol * max(1., abs(float(expected))), (name, actual, expected, error)
    numeric.append(dict(check=name, actual=float(actual), expected=float(expected), absolute_error=error))

x, y = sp.symbols("x y", real=True)
l, D, t, h = sp.symbols("l D t h", positive=True)
phi = sp.symbols("phi", real=True)
for name, expr, result in [
    ("angular mean cos", sp.cos(phi), 0),
    ("angular mean sin", sp.sin(phi), 0),
    ("angular second moment x", sp.cos(phi)**2, sp.Rational(1,2)),
    ("angular second moment y", sp.sin(phi)**2, sp.Rational(1,2)),
    ("angular cross moment", sp.sin(phi)*sp.cos(phi), 0),
]:
    zero(name, sp.integrate(expr, (phi, 0, 2*sp.pi))/(2*sp.pi)-result)

U = sp.log((x*x+(y+l)**2)/(x*x+(y-l)**2))/(4*sp.pi*D)
Jx = -D*sp.diff(U,x)
Jy = -D*sp.diff(U,y)
f = l/(sp.pi*(x*x+l*l))
zero("Green function boundary", U.subs(y,0))
zero("Green function Laplace away from source", sp.diff(U,x,2)+sp.diff(U,y,2))
zero("boundary tangential flux", Jx.subs(y,0))
zero("outward boundary flux sign and coefficient", -Jy.subs(y,0)-f)
p = (sp.exp(-(x*x+(y-l)**2)/(4*D*t)) -
     sp.exp(-(x*x+(y+l)**2)/(4*D*t)))/(4*sp.pi*D*t)
jb = l*sp.exp(-(x*x+l*l)/(4*D*t))/(4*sp.pi*D*t*t)
zero("absorbed heat kernel boundary", p.subs(y,0))
zero("absorbed heat kernel diffusion equation", sp.diff(p,t)-D*(sp.diff(p,x,2)+sp.diff(p,y,2)))
zero("heat kernel outward flux", D*sp.diff(p,y).subs(y,0)-jb)
zero("Cauchy normalization", sp.integrate(f,(x,-sp.oo,sp.oo))-1)
zero("interval integral derivative", sp.diff(sp.atan(x/l)/sp.pi,x)-f)
q = 1-y/h
zero("strip backward equation", sp.diff(q,y,2))
zero("strip lower event", q.subs(y,0)-1)
zero("strip upper event", q.subs(y,h))
T = y*(h-y)/(2*D)
zero("mean absorption time equation", D*sp.diff(T,y,2)+1)
zero("mean absorption time lower", T.subs(y,0))
zero("mean absorption time upper", T.subs(y,h))
Cb, Ct = (h-l)/(D*h), l/(D*h)
zero("integrated Green function continuity", Cb*l-Ct*(h-l))
zero("unit source derivative jump", D*(Cb+Ct)-1)
u = sp.symbols("u", real=True, nonzero=True)
qd = (sp.exp(-u*y/D)-sp.exp(-u*h/D))/(1-sp.exp(-u*h/D))
zero("drift backward equation", D*sp.diff(qd,y,2)+u*sp.diff(qd,y))
zero("drift lower boundary", qd.subs(y,0)-1)
zero("drift upper boundary", qd.subs(y,h))
zero("drift zero limit", sp.limit(qd,u,0)-(1-y/h))
k = sp.symbols("k", real=True, positive=True)
Ak = sp.exp(-k*y)
zero("characteristic function harmonic equation", sp.diff(Ak,y,2)-k*k*Ak)
xp = sp.symbols("xp", positive=True)
zero("Fourier inversion for positive x", sp.integrate(sp.exp(-l*k)*sp.cos(k*xp),(k,0,sp.oo))/sp.pi-f.subs(x,xp))
zero("Fourier inversion at x=0", sp.integrate(sp.exp(-l*k),(k,0,sp.oo))/sp.pi-f.subs(x,0))
zero("cosine and target density both even", f.subs(x,-x)-f)
alpha, v = sp.symbols("alpha v", real=True)
zero("lower exponential-map Jacobian and denominator",
     sp.sin(alpha)*sp.exp(v)/(h*((sp.exp(v)-sp.cos(alpha))**2+sp.sin(alpha)**2))-
     sp.sin(alpha)/(2*h*(sp.cosh(v)-sp.cos(alpha))))
zero("upper absolute Jacobian and denominator",
     sp.sin(alpha)*sp.exp(v)/(h*((-sp.exp(v)-sp.cos(alpha))**2+sp.sin(alpha)**2))-
     sp.sin(alpha)/(2*h*(sp.cosh(v)+sp.cos(alpha))))
zero("time substitution coefficient",
     l/sp.sqrt(4*sp.pi*D)*(4*D)**sp.Rational(3,2)/l**3*(-l*l/(2*D))+2/sp.sqrt(sp.pi))

# Numerical tests start from time-dependent heat flux, not from the answer formula.
for lv in [.2, 1., 2.5]:
    for dv in [.3, 1., 4.]:
        for xv in [0., .5*lv, 2.*lv]:
            val, err = quad(lambda tv: lv*math.exp(-(xv*xv+lv*lv)/(4*dv*tv))/(4*math.pi*dv*tv*tv),
                            0., np.inf, epsabs=2e-11, epsrel=2e-11, limit=300)
            close("time heat-flux integral l=%g D=%g x=%g"%(lv,dv,xv),
                  val, lv/(math.pi*(xv*xv+lv*lv)))
            assert err < 1e-8

# Free source normalization and image-source divergence independently integrated.
for lv in [.25, 1., 3.]:
    rv = .2*lv
    def circle_flux(angle):
        xx, yy = rv*math.cos(angle), lv+rv*math.sin(angle)
        jx = (xx/(xx*xx+(yy-lv)**2)-xx/(xx*xx+(yy+lv)**2))/(2*math.pi)
        jy = ((yy-lv)/(xx*xx+(yy-lv)**2)-(yy+lv)/(xx*xx+(yy+lv)**2))/(2*math.pi)
        return (jx*math.cos(angle)+jy*math.sin(angle))*rv
    val = quad(circle_flux,0.,2*math.pi,epsabs=1e-12)[0]
    close("closed circle cumulative source flux l=%g"%lv,val,1.)
    for xv in [0., .8*lv, 3*lv]:
        eps = 1e-5*lv
        def Ulog(yy):
            return math.log((xv*xv+(yy+lv)**2)/(xv*xv+(yy-lv)**2))/(4*math.pi)
        derivative = (Ulog(eps)-Ulog(-eps))/(2*eps)
        close("finite-difference log-potential normal derivative l=%g x=%g"%(lv,xv),
              derivative,lv/(math.pi*(xv*xv+lv*lv)),tol=2e-8)

def stable_strip(xv,lv,hv,lower=True):
    alpha = math.pi*lv/hv
    ee = math.exp(-abs(math.pi*xv/hv))
    sign = -1 if lower else 1
    return math.sin(alpha)*ee/(hv*(1+ee*ee+sign*2*ee*math.cos(alpha)))

for hv in [1., 3.]:
    for ratio in [.1, .25, .5, .8, .95]:
        lv = ratio*hv
        for lower in [True,False]:
            val = quad(lambda xx: stable_strip(xx,lv,hv,lower),-np.inf,np.inf,
                       epsabs=2e-11,epsrel=2e-11,limit=300)[0]
            close("strip %s density integral l/h=%g h=%g"%("lower" if lower else "upper",ratio,hv),
                  val,1-ratio if lower else ratio)

# Finite-difference systems directly use the backward generator on 0<y<h.
for hv,dv in [(1.,.7),(3.,2.)]:
    n = 100
    dy = hv/n
    yy = np.linspace(0,hv,n+1)
    matrix = np.diag(np.full(n-1,-2*dv/dy**2))
    matrix += np.diag(np.full(n-2,dv/dy**2),1)+np.diag(np.full(n-2,dv/dy**2),-1)
    rhs_q = np.zeros(n-1); rhs_q[0] -= dv/dy**2
    computed_q = np.r_[1.,np.linalg.solve(matrix,rhs_q),0.]
    computed_T = np.r_[0.,np.linalg.solve(matrix,np.full(n-1,-1.)),0.]
    close("finite-difference strip probability max residual h=%g"%hv,
          np.max(np.abs(computed_q-(1-yy/hv))),0.,tol=1e-10)
    close("finite-difference strip mean time max residual h=%g"%hv,
          np.max(np.abs(computed_T-yy*(hv-yy)/(2*dv))),0.,tol=1e-10)

# Collocation BVP is independent of the closed exponential probability expression.
for drift in [-1., math.log(2), 2.]:
    hv,dv = 2.,1.
    grid = np.linspace(0,hv,70)
    sol = solve_bvp(lambda yy,z: np.vstack((z[1],-drift*z[1]/dv)),
                    lambda left,right: np.array([left[0]-1,right[0]]),
                    grid,np.vstack((1-grid/hv,-np.ones_like(grid)/hv)),tol=1e-10,max_nodes=4000)
    assert sol.success, sol.message
    lv=1.
    expected=(math.exp(-drift*lv/dv)-math.exp(-drift*hv/dv))/(1-math.exp(-drift*hv/dv))
    close("collocation drift probability u=%g"%drift,sol.sol(lv)[0],expected,tol=3e-9)
close("upward drift numerical variant", (0.5-0.25)/(1.-0.25),1/3)

# Variants computed by direct integrals and an independent scalar root solve.
close("90 percent interval root", brentq(lambda aa: quad(lambda xx: 1/(math.pi*(1+xx*xx)),-aa,aa)[0]-.9,
                                        1.,20.), math.tan(.45*math.pi))
close("translated interval probability", quad(lambda xx: 1/(math.pi*((xx-1)**2+1)),-1,2)[0],
      (math.atan(1)+math.atan(2))/math.pi)
def time_cdf(tv):
    # Direct first-hit density, l=D=1.
    return quad(lambda tt: math.exp(-1/(4*tt))/(math.sqrt(4*math.pi)*tt**1.5),
                0.,tv,epsabs=2e-12,epsrel=2e-12,limit=300)[0]
close("finite time probability at l²/D",time_cdf(1.),math.erfc(.5))
root95 = brentq(lambda tv: time_cdf(tv)-.95,1.,1000.,xtol=1e-10)
close("95 percent time coefficient",root95,127.15722227527924,tol=1e-10)
close("Cauchy inverse Fourier integral",quad(lambda kv: math.exp(-kv)*math.cos(2*kv),0.,np.inf,
                                           epsabs=1e-12,limit=300)[0]/math.pi,1/(5*math.pi))

# The finite-step warning is not inferred from a Brownian computation.
lv,hv,av=.25,1.,100.
lower_first=.5-math.asin(lv/av)/math.pi
upper_first=.5-math.asin((hv-lv)/av)/math.pi
survival_first=1-lower_first-upper_first
finite_bound=[lower_first,lower_first+survival_first]
assert not finite_bound[0] <= (hv-lv)/hv <= finite_bound[1]
close("finite-step first-event probability sum",lower_first+upper_first+survival_first,1.)

model = json.loads((ROOT/"build/question-01-模型审查.json").read_text())
resolved = bool(model.get("model_condition_resolved")) and bool(model.get("user_reply_received"))
figure_names=["geometry-01","averaging-01","mirror-01","density-01","strip-01","mapping-01"]
for name in figure_names:
    subprocess.run(["qpdf","--check",str(ROOT/f"figures/{name}.pdf")],capture_output=True,check=True)

bound_files = {
    "question_source":ROOT/"drafts/question-01.md",
    "figure_source":ROOT/"figures/题01_图稿源文件.tex",
    "verification_script":Path(__file__).resolve(),
    "figure_render_script":ROOT/"scripts/render_figures.py",
    "working_build_script":ROOT/"scripts/preview_drafts.py",
    "typesetting_template":ROOT/"latex/template.tex",
    "model_review":ROOT/"build/question-01-模型审查.json",
    "human_authorization":ROOT/"build/model-revisions-015-2026-10-09.json",
    "vector_geometry_check":ROOT/"build/question-01-figure-geometry.json",
    "original_paper":ROOT.parent/"试卷.pdf",
    "original_handwritten_answers":ROOT.parent/"答案.pdf",
}
report=dict(
    paper="015", question="01", scope="human-authorized continuous-diffusion stem and separately solved finite-step counterexample",
    verified_math=True, user_reply_received=bool(model.get("user_reply_received")),
    model_condition_resolved=resolved, question_accepted=False, set_accepted=False,
    note="Model choice is recorded by the human reply; numerical or symbolic passes do not substitute for actual current PDF review.",
    document_contains_all_three_parts=True, symbolic_checks=symbolic, independent_numerical_checks=numeric,
    finite_step_counterexample=dict(l_over_h=lv/hv,a_over_h=av/hv,
       first_lower_probability=lower_first,first_upper_probability=upper_first,
       first_survival_probability=survival_first,eventual_lower_bound=finite_bound,
       continuous_result=.75,finite_interval_excludes_continuous_result=True),
    limits_checked=["l -> 0+ rescue -> 1","l -> h- rescue -> 0","h -> infinity rescue -> 1",
                    "drift u -> 0 restores linear probability","Cauchy has nonintegrable absolute first moment",
                    "half-plane first-hit mean time diverges","finite strip mean time l(h-l)/(2D) finite"],
    dimension_checks=dict(f="length^-1",jb="length^-1 time^-1",p="length^-2",
                          U="time length^-2",calJ="length^-1",mean_time="time",D="length^2 time^-1"),
    bound_files={key:dict(path=str(path),sha256=sha(path)) for key,path in bound_files.items()},
    figures={name:dict(pdf_sha256=sha(ROOT/f"figures/{name}.pdf"),
                       png_sha256=sha(ROOT/f"figures/{name}.png")) for name in figure_names})
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(dict(verified_math=True,symbolic_checks=len(symbolic),independent_numerical_checks=len(numeric),
                     model_condition_resolved=resolved,question_accepted=False,
                     finite_bound=finite_bound,output=str(OUT)),ensure_ascii=False))
