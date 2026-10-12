"""第2题：磁偶极子矢量叠加、数值磁通积分及笛卡尔运动方程。"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]

def field(r):
    # 归一化 h=m=q=1，μ0*m0=2π，C=1。
    return (2-r*r)/(1+r*r)**2.5

def dipole_vector(pos, center):
    displacement=np.array(pos,dtype=float)-np.array(center,dtype=float)
    distance=np.linalg.norm(displacement)
    moment=np.array([0.,0.,1.])
    return .5*(3*np.dot(moment,displacement)*displacement/distance**5-moment/distance**3)

def main():
    r=sp.symbols('r',nonnegative=True)
    primitive=r*r/(1+r*r)**sp.Rational(3,2)
    assert sp.simplify(sp.diff(primitive,r)-r*(2-r*r)/(1+r*r)**sp.Rational(5,2))==0
    W=r*r/(1+r*r)**3
    rb=1/math.sqrt(2);vc=2/(3*math.sqrt(3))
    assert sp.simplify(sp.diff(W,r,2).subs(r,sp.sqrt(2)/2)+sp.Rational(64,81))==0
    field_checks=[]
    for radius in [0,.1,.5,rb,1.,math.sqrt(2),2.,5.,12.]:
        vector=dipole_vector([radius,0,0],[0,0,1])+dipole_vector([radius,0,0],[0,0,-1])
        assert np.allclose(vector,[0.,0.,field(radius)],rtol=1e-12,atol=1e-12)
        integral=quad(lambda s:field(s)*s,0,radius,epsabs=1e-12,epsrel=1e-12)[0]
        closed=radius*radius/(1+radius*radius)**1.5
        assert abs(integral-closed)<1e-11
        field_checks.append(dict(r=radius,Bz=float(vector[2]),flux_div_2pi_integral=integral,flux_div_2pi_closed=closed))
    def derivative(t,state):
        x,y,vx,vy=state;B=field(math.hypot(x,y))
        return [vx,vy,vy*B,-vx*B]
    ode_checks=[]
    for ratio in [.8,1.,1.2]:
        initial_speed=ratio*vc
        def turning(t,state):
            x,y,vx,vy=state;radius=math.hypot(x,y)
            return initial_speed if radius<1e-12 else (x*vx+y*vy)/radius
        turning.terminal=True;turning.direction=-1
        horizon=14. if ratio==1 else 60.
        solution=solve_ivp(derivative,[0,horizon],[0.,0.,initial_speed,0.],rtol=3e-12,atol=1e-13,max_step=.02,events=turning if ratio<1 else None,dense_output=True)
        assert solution.success
        x,y,vx,vy=solution.y;radius=np.hypot(x,y)
        energy_error=float(np.max(np.abs((vx*vx+vy*vy)/initial_speed**2-1)))
        canonical_error=float(np.max(np.abs(x*vy-y*vx+radius*radius/(1+radius*radius)**1.5)))
        radial=(x[1:]*vx[1:]+y[1:]*vy[1:])/radius[1:]
        radial_squared_error=float(np.max(np.abs(radial**2-(initial_speed**2-radius[1:]**2/(1+radius[1:]**2)**3))))
        assert energy_error<1e-8 and canonical_error<1e-9 and radial_squared_error<1e-10
        result=dict(speed_ratio=ratio,time_end=float(solution.t[-1]),radius_end=float(radius[-1]),energy_error=energy_error,canonical_error=canonical_error,radial_squared_error=radial_squared_error)
        if ratio<1:
            root=brentq(lambda u:27/4*u*u/(1+u*u)**3-ratio**2,0,rb,xtol=1e-13)
            assert len(solution.t_events[0])==1 and abs(radius[-1]-root)<1e-9
            result['analytic_turning_radius']=root
        elif ratio==1:
            times=np.array([8.,10.,12.,14.]);state=solution.sol(times);distances=rb-np.hypot(state[0],state[1])
            assert np.all(distances>0) and np.all(np.diff(distances)<0)
            slopes=-np.diff(np.log(distances))/np.diff(times)
            kappa=4*math.sqrt(2)/9
            assert abs(slopes[-1]-kappa)<.002
            result.update(critical_distances=distances.tolist(),log_decay_rates=slopes.tolist(),analytic_kappa=kappa)
        else:
            assert radius[-1]>15 and np.all(radial>0)
            result['escaped_beyond_radius_15']=True
        ode_checks.append(result)
    sources={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['drafts/question-02.md','figures/题02_图稿源文件.tex']}
    report=dict(question=2,pass_all=True,normalization='h=m=q=C=1, μ0*m0=2π',barrier_radius=rb,critical_speed=vc,field_and_flux_checks=field_checks,cartesian_ode_checks=ode_checks,source_sha256=sources)
    dest=ROOT/'build'/'verification-q02.json';dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
