"""014 Q1: exact differentiation, frame transport, independent finite differences.

The co-rotating observer was authorized by the user on 2026-10-10.
Successful checks do not constitute document or visual acceptance.
"""
from pathlib import Path
import hashlib
import json
import math
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
t = s.symbols('t', real=True)
r, l, w = s.symbols('r l w', positive=True, real=True)
theta = w*t
c, sn = s.cos(theta), s.sin(theta)
rho = r*(1+c)/2
Q = s.Matrix([[c, -sn], [sn, c]])
J = s.Matrix([[0, -1], [1, 0]])
H = s.Matrix([l, 0])
T = s.Matrix([rho*c, rho*sn])
R = s.simplify(Q.T*(H-T))
A = l-r/2
expected_R = s.Matrix([A*c-r/2, -l*sn])
expected_v = s.Matrix([-r*w*(sn+s.sin(2*theta))/2,
                       r*w*(c+s.cos(2*theta))/2])
expected_a = s.Matrix([-r*w**2*(c+2*s.cos(2*theta))/2,
                       -r*w**2*(sn+2*s.sin(2*theta))/2])
checks = []

def identity(name, residual):
    values = list(residual) if isinstance(residual, s.MatrixBase) else [residual]
    simplified = [s.trigsimp(s.expand_trig(s.simplify(value))) for value in values]
    assert all(value == 0 for value in simplified), (name, simplified)
    checks.append(dict(name=name, passed=True))

identity('rotating coordinates derived from rotation matrix', R-expected_R)
identity('ground velocity from original position', T.diff(t)-expected_v)
identity('ground acceleration from original position', T.diff(t, 2)-expected_a)
identity('ellipse equation', (R[0]+r/2)**2/A**2+R[1]**2/l**2-1)
identity('rotating velocity from transport theorem',
         R.diff(t)-(Q.T*(-T.diff(t))-w*J*R))
identity('rotating acceleration from transport theorem',
         R.diff(t, 2)-(Q.T*(-T.diff(t, 2))-2*w*J*R.diff(t)+w**2*R))
identity('polar ground velocity', Q.T*T.diff(t)-s.Matrix([rho.diff(t), w*rho]))
identity('polar ground acceleration',
         Q.T*T.diff(t, 2)-s.Matrix([rho.diff(t, 2)-w**2*rho, 2*w*rho.diff(t)]))
identity('ground speed squared', T.diff(t).dot(T.diff(t))-r**2*w**2*(1+c)/2)
identity('ground acceleration squared', T.diff(t, 2).dot(T.diff(t, 2))-r**2*w**4*(5+4*c)/4)
identity('observer velocity', R.diff(t)-s.Matrix([-w*A*sn, -w*l*c]))
identity('observer acceleration', R.diff(t, 2)-s.Matrix([-w**2*A*c, w**2*l*sn]))
T_fixed = s.Matrix([r*c, r*sn])
R_fixed = s.simplify(Q.T*(H-T_fixed))
identity('fixed rider ground speed', T_fixed.diff(t).dot(T_fixed.diff(t))-w**2*r**2)
identity('fixed rider observer speed', R_fixed.diff(t).dot(R_fixed.diff(t))-w**2*l**2)
identity('fixed rider ground acceleration', T_fixed.diff(t, 2).dot(T_fixed.diff(t, 2))-w**4*r**2)
identity('fixed rider observer acceleration', R_fixed.diff(t, 2).dot(R_fixed.diff(t, 2))-w**4*l**2)
identity('tangent condition', s.det(s.Matrix.hstack(T_fixed-H, T_fixed.diff(t)))-w*r*(r-l*c))
identity('initial ground velocity', T.diff(t).subs(t, 0)-s.Matrix([0, r*w]))
identity('initial ground acceleration', T.diff(t, 2).subs(t, 0)-s.Matrix([-3*r*w**2/2, 0]))
identity('cusp ground velocity', T.diff(t).subs(t, s.pi/w))
identity('cusp ground acceleration', T.diff(t, 2).subs(t, s.pi/w)-s.Matrix([-r*w**2/2, 0]))
a, b = s.symbols('a b', positive=True, real=True)
rhog = a+b*c
Tg = s.Matrix([rhog*c, rhog*sn])
Rg = s.simplify(Q.T*(H-Tg))
identity('variant 1 translating observer is negative ground separation', H-T+s.Matrix([T[0]-l,T[1]]))
identity('variant 2 general rotating position', Rg-s.Matrix([(l-b)*c-a,-l*sn]))
identity('variant 2 general ground velocity', Tg.diff(t)-s.Matrix([-w*sn*(a+2*b*c),w*(a*c+b*s.cos(2*theta))]))
identity('variant 2 general ground acceleration', Tg.diff(t,2)-s.Matrix([-w**2*(a*c+2*b*s.cos(2*theta)),-w**2*(a*sn+2*b*s.sin(2*theta))]))
identity('variant 3 speed extrema representation', R.diff(t).dot(R.diff(t))-w**2*(A**2+(l**2-A**2)*c**2))
identity('variant 3 acceleration extrema representation', R.diff(t,2).dot(R.diff(t,2))-w**4*(A**2+(l**2-A**2)*sn**2))
identity('variant 4 pi/4 velocity exact value', T.diff(t)[0].subs({r:2,w:1,t:s.pi/4})+1+s.sqrt(2)/2)
identity('actual velocity facing x component', T.diff(t)[0]+r*w*s.cos(theta/2)*s.sin(3*theta/2))
identity('actual velocity facing y component', T.diff(t)[1]-r*w*s.cos(theta/2)*s.cos(3*theta/2))

def position(time, rr, ll, ww, observer=False):
    angle = ww*time
    cs, si = math.cos(angle), math.sin(angle)
    radius = rr*(1+cs)/2
    tx, ty = radius*cs, radius*si
    if not observer:
        return (tx-ll, ty)
    # Rotate the actual separation H-T numerically; not the derived ellipse.
    dx, dy = ll-tx, -ty
    return (cs*dx+si*dy, -si*dx+cs*dy)

numeric = []
for rr, ll, ww in [(1.0, 2.0, .7), (1.3, 1.31, 1.5), (.2, 100.0, .03)]:
    for angle in [.0, .15, .4, .83, 1.4, 2.1, 2.85, math.pi, 3.7, 5.3, 6.1]:
        time = angle/ww
        step = 2e-4/ww
        for observer in [False, True]:
            samples = {k:position(time+k*step, rr, ll, ww, observer) for k in [-2,-1,0,1,2]}
            vel = [(-samples[2][i]+8*samples[1][i]-8*samples[-1][i]+samples[-2][i])/(12*step) for i in range(2)]
            acc = [(-samples[2][i]+16*samples[1][i]-30*samples[0][i]+16*samples[-1][i]-samples[-2][i])/(12*step**2) for i in range(2)]
            cs, si = math.cos(angle), math.sin(angle)
            if observer:
                aa = ll-rr/2
                vref = (-ww*aa*si, -ww*ll*cs)
                aref = (-ww**2*aa*cs, ww**2*ll*si)
            else:
                vref = (-rr*ww*(si+math.sin(2*angle))/2, rr*ww*(cs+math.cos(2*angle))/2)
                aref = (-rr*ww**2*(cs+2*math.cos(2*angle))/2, -rr*ww**2*(si+2*math.sin(2*angle))/2)
            for label, result, reference, tol in [('velocity',vel,vref,3e-8), ('acceleration',acc,aref,2e-6)]:
                error = max(abs(result[i]-reference[i])/(1+abs(reference[i])) for i in range(2))
                assert error < tol, (rr,ll,ww,angle,observer,label,error)
                numeric.append(dict(parameters=[rr,ll,ww],theta=angle,observer=observer,quantity=label,max_scaled_error=error,passed=True))

report = dict(paper='014',question='01',model='authorized co-rotating observer',
              model_authorized=True,authorization='用户2026-10-10明确回复：四项均按建议修订并注明',symbolic_checks=checks,numeric_checks=numeric,
              symbolic_count=len(checks),numeric_count=len(numeric),math_passed=True,
              accepted=False,source_sha256={key:hashlib.sha256((ROOT.parent/key).read_bytes()).hexdigest() for key in ['试卷.pdf','答案.pdf']},
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              draft_sha256=hashlib.sha256((ROOT/'drafts/question-01.md').read_bytes()).hexdigest(),
              figure_source_sha256=hashlib.sha256((ROOT/'figures/题01_图稿源文件.tex').read_bytes()).hexdigest())
out=ROOT/'verification';out.mkdir(exist_ok=True)
(out/'question-01-math.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['symbolic_count','numeric_count','math_passed','accepted']},ensure_ascii=False))
