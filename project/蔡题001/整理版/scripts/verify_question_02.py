from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
L=m=J=1.;a=2/3
vG=J/m;omega=2*J/(m*L)
def velocity(s):return vG+omega*(s-L/2)
def moment_integral(x):
    ang=quad(lambda s:m/L*(x-s)*velocity(s),0,x,epsabs=1e-13)[0]
    return ang-(J*(x-a) if x>=a else 0)
def analytic(x):return J*x**3/(3*L*L)-(J*(x-a) if x>=a else 0)
rows=[]
for x in np.linspace(0,1,61):
 val=moment_integral(x);assert abs(val-analytic(x))<1e-12
 rows.append([float(x),float(val)])
assert abs(moment_integral(a)-8/81)<1e-13
left=minimize_scalar(lambda x:-moment_integral(x),bounds=(0,a),method='bounded',options={'xatol':1e-13})
right=minimize_scalar(lambda x:-moment_integral(x),bounds=(a,1),method='bounded',options={'xatol':1e-13})
assert abs(left.x-a)<1e-6 and abs(right.x-a)<1e-6
assert abs(quad(lambda s:m/L*velocity(s),0,L)[0]-J)<1e-13
assert abs(quad(lambda s:m/L*(s-L/2)*velocity(s),0,L)[0]-J/6)<1e-13
assert abs(velocity(0))<1e-13
# General strike alpha=s_hit/L; check top velocity and impulse energy from integrals.
for alpha in [.2,.5,2/3,1.]:
 w=12*(alpha-.5);v=lambda s:1+w*(s-.5)
 assert abs(quad(lambda s:v(s),0,1)[0]-1)<1e-12
 assert abs(quad(lambda s:(s-.5)*v(s),0,1)[0]-(alpha-.5))<1e-12
 assert abs(quad(lambda s:.5*v(s)**2,0,1)[0]-(.5+6*(alpha-.5)**2))<1e-12
report=dict(passed=True,method='section angular-momentum quadrature + bounded maximum + global impulse integrals',centre_speed=1,angular_speed=2,max_couple=8/81,max_section_from_top=a,J_threshold_factor=81/8,sections=rows)
(ROOT/'preview/verify-question-02.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='sections'},ensure_ascii=False))
