"""完整两点力矩矩阵与独立停止事件积分；停止后不延续滑动方程。"""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[1]
g=l=m=1.0
w=math.sqrt(2*g/(7*l));vc=math.sqrt(33*g*l/14)
def forces(x):
    muf=1-(x-l/2)/(4*l);mur=1-(x+l/2)/(4*l)
    A=np.array([[1,1,0],[1,-1,-1],[-muf,-mur,1.]])
    return np.linalg.solve(A,[m*g,0,0])
def stop(t,y): return y[1]
stop.terminal=True;stop.direction=1
rows=[]
for ratio in [.01,.1,.35,.7,.99,1.,1.03]:
    v=ratio*vc
    def rhs(t,y): return [y[1],forces(y[0])[2]/m]
    sol=solve_ivp(rhs,[0,10],[2*l,-v],events=stop,method="DOP853",rtol=2e-12,atol=1e-13,max_step=.008,dense_output=True)
    ts=float(sol.t_events[0][0]);xs=float(sol.y_events[0][0,0])
    exact_t=math.atan(v/(2*l*w))/w
    exact_x=4*l-math.sqrt(4*l*l+v*v/(w*w))
    assert abs(ts-exact_t)<2e-10 and abs(xs-exact_x)<2e-10
    if ratio<=1:
        X=sol.sol(np.linspace(0,ts,301))[0]
        assert min(forces(x)[1] for x in X)>-1e-10 and min(X)>=l/2-1e-10
    else: assert xs<l/2 and forces(xs)[1]<0
    rows.append(dict(speed_ratio=ratio,stop_time=ts,stop_x=xs,front_normal=float(forces(xs)[0]),rear_normal=float(forces(xs)[1]),physically_admissible=ratio<=1))
# Constant-mu contact: force and torque balance, independent stopping distance.
vc1=math.sqrt(7*g*l/4)
assert abs(2*l-vc1*vc1/(g)-l/4)<1e-14
# General linear mu(h)=a-b*h/l, using full local-contact equations.
for a,b in [(.8,.15),(1,.25),(.6,.08)]:
 for x in [1.,1.5,2.]:
  mf=a-b*(x-.5);mr=a-b*(x+.5)
  A=np.array([[1,1,0],[1,-1,-1],[-mf,-mr,1.]])
  nf,nr,f=np.linalg.solve(A,[1,0,0])
  assert abs(f-(a-b*x)/(1-b/2))<1e-12
report=dict(passed=True,method='contact force matrix + DOP853 adaptive independent ODE/stop event',cases=rows,constant_mu_speed_limit=vc1,variable_mu_speed_limit=vc,variable_mu_critical_time=math.atan(vc/(2*w))/w,original_hashes={p.name:__import__('hashlib').sha256(p.read_bytes()).hexdigest() for p in [ROOT.parent/'试卷.pdf',ROOT.parent/'答案.pdf']})
(ROOT/'preview/verify-question-01.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
