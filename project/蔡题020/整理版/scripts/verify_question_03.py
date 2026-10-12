"""等边三星：平衡点独立二维求根、场的傅里叶积分与线性受迫轨道。"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, root

ROOT=Path(__file__).resolve().parents[1]
ANGLES=np.arange(3)*2*math.pi/3
STARS=np.column_stack((np.cos(ANGLES),np.sin(ANGLES)))
W0SQ=1/math.sqrt(3)
W0=math.sqrt(W0SQ)

def gravity(pos):
    displacement=np.asarray(pos)[None,:]-STARS
    distances=np.linalg.norm(displacement,axis=1)
    return -np.sum(displacement/distances[:,None]**3,axis=0)

def equilibrium(pos):
    return gravity(pos)+W0SQ*np.asarray(pos)

def main():
    approval=json.loads((ROOT/'build/question-03-条件确认.json').read_text())
    assert approval['approved'] and approval['document_revision_implemented']
    stem=(ROOT/'drafts/question-03.md').read_text().split('<!-- question-end -->')[0]
    assert '不计自由偏心分量' in stem and '修订说明' in stem
    fa=lambda s:1/(s-1)**2+(2*s+1)/(s*s+s+1)**1.5-s/math.sqrt(3)
    fb=lambda s:1/(s+1)**2+(2*s-1)/(s*s-s+1)**1.5-s/math.sqrt(3)
    radii=[brentq(fa,1.0001,5,xtol=1e-13),brentq(fb,.0001,.5,xtol=1e-13),brentq(fb,1,5,xtol=1e-13)]
    known=[np.zeros(2)]
    for radius,offset in zip(radii,[0,math.pi,math.pi]):
        for theta in ANGLES+offset:
            known.append(radius*np.array([math.cos(theta),math.sin(theta)]))
    assert all(np.linalg.norm(equilibrium(point))<1e-10 for point in known)
    found=[]
    for x in np.linspace(-3,3,25):
        for y in np.linspace(-3,3,25):
            if np.min(np.linalg.norm(np.array([x,y])[None,:]-STARS,axis=1))<.03:
                continue
            result=root(equilibrium,[x,y],tol=1e-11)
            if result.success and np.linalg.norm(equilibrium(result.x))<1e-8:
                if not any(np.linalg.norm(result.x-other)<1e-6 for other in found):
                    found.append(result.x)
    assert len(found)==10 and all(any(np.linalg.norm(p-k)<1e-6 for k in known) for p in found)
    s=sp.symbols('s',positive=True)
    inverse_bound=sp.factor(4-(2-s)*(1+s)**2)
    assert sp.simplify(inverse_bound-(s-1)**2*(s+2))==0
    x=sp.symbols('x',real=True)
    P3=(5*x**3-3*x)/2
    angular_sum=sp.expand(P3.subs(x,sp.cos(s))+P3.subs(x,sp.cos(s+2*sp.pi/3))+P3.subs(x,sp.cos(s-2*sp.pi/3)))
    assert sp.trigsimp(sp.expand_trig(angular_sum-sp.Rational(15,8)*sp.cos(3*s)))==0
    farfield=[]
    for radius in [10.,20.,40.]:
        def components(theta):
            er=np.array([math.cos(theta),math.sin(theta)])
            et=np.array([-math.sin(theta),math.cos(theta)])
            g=gravity(radius*er)
            return float(np.dot(g,er)),float(np.dot(g,et))
        mean_fr=quad(lambda theta:components(theta)[0],0,2*math.pi,epsabs=1e-13,epsrel=1e-11)[0]/(2*math.pi)
        omega=math.sqrt(-mean_fr/radius)
        forcing_fr=-quad(lambda theta:components(theta)[0]*math.cos(3*theta),0,2*math.pi,epsabs=1e-13,epsrel=1e-10)[0]/math.pi
        # Δ=φ-ω0t；切向场为负sin(3Δ)，沿时间则为正sin(νt)。
        forcing_ft=-quad(lambda theta:components(theta)[1]*math.sin(3*theta),0,2*math.pi,epsabs=1e-13,epsrel=1e-10)[0]/math.pi
        leading_fr=7.5/radius**5;leading_ft=5.625/radius**5
        assert abs(forcing_fr/leading_fr-1)<2/radius**2
        assert abs(forcing_ft/leading_ft-1)<2/radius**2
        def mean_fr_derivative(theta):
            cosines=np.cos(theta-ANGLES)
            distance=np.sqrt(radius**2+1-2*radius*cosines)
            return float(np.sum(3*(radius-cosines)**2/distance**5-1/distance**3))
        derivative=quad(mean_fr_derivative,0,2*math.pi,epsabs=1e-13,epsrel=1e-11)[0]/(2*math.pi)
        kappa2=3*omega**2-derivative
        nu=3*(W0-omega)
        amplitude=(forcing_fr+2*omega*forcing_ft/nu)/(nu**2-kappa2)
        leading_amplitude=5*math.sqrt(3)/(6*radius**5)
        # 在独立线性微分方程中积分，而不是仅代回幅值公式。
        def system(t,state):
            displacement,velocity=state
            return [velocity,-kappa2*displacement-(forcing_fr+2*omega*forcing_ft/nu)*math.cos(nu*t)]
        period=2*math.pi/nu
        sol=solve_ivp(system,[0,5*period],[amplitude,0.],rtol=1e-11,atol=1e-17,max_step=period/100,dense_output=True)
        times=np.linspace(0,5*period,2001)
        predicted=amplitude*np.cos(nu*times)
        error=float(np.max(np.abs(sol.sol(times)[0]-predicted))/amplitude)
        assert error<1e-6
        farfield.append(dict(R_over_a=radius,radial_force_fourier=forcing_fr,radial_force_leading=leading_fr,tangential_force_fourier=forcing_ft,tangential_force_leading=leading_ft,omega=omega,nu=nu,epicycle_frequency_squared=kappa2,amplitude_from_force_integrals=amplitude,leading_amplitude=leading_amplitude,amplitude_ratio=amplitude/leading_amplitude,independent_linear_ode_relative_error=error))
    assert all(a['amplitude_ratio']>b['amplitude_ratio']>1 for a,b in zip(farfield,farfield[1:]))
    # 不同初值下的完整二维线性系统，独立核对教师变式的自由项及切向位移。
    omega=.03;nu=3*(W0-omega);force=2.e-5;tangent=.75*force
    drive=force+2*omega*tangent/nu
    amplitude=drive/(nu**2-omega**2)
    def coupled(t,state):
        xx,vx,yy,vy=state
        return [vx,2*omega*vy+3*omega**2*xx-force*math.cos(nu*t),vy,
                -2*omega*vx+tangent*math.sin(nu*t)]
    duration=2*math.pi/omega
    initial=[0.,0.,0.,-tangent/nu]
    numerical=solve_ivp(coupled,[0,duration],initial,rtol=1e-11,atol=1e-16,
                        max_step=2*math.pi/nu/60,dense_output=True)
    tt=np.linspace(0,duration,4001)
    expected_x=amplitude*(np.cos(nu*tt)-np.cos(omega*tt))
    expected_y=-(2*omega*amplitude/nu+tangent/nu**2)*np.sin(nu*tt)+2*amplitude*np.sin(omega*tt)
    initial_value_errors=dict(x=float(np.max(np.abs(numerical.sol(tt)[0]-expected_x))/amplitude),
                              y=float(np.max(np.abs(numerical.sol(tt)[2]-expected_y))/amplitude))
    assert max(initial_value_errors.values())<1e-6
    delta=sp.symbols('delta',real=True)
    ratio=(1-delta/2)/((1-delta)*(1-2*delta+sp.Rational(8,9)*delta**2))
    assert sp.simplify(sp.diff(ratio,delta).subs(delta,0)-sp.Rational(5,2))==0
    # 相似系统用实际矢量场与转速同时缩放，而非仅重述幅值比例。
    def scaled_gravity(pos):
        displacement=np.asarray(pos)[None,:]-2*STARS
        distances=np.linalg.norm(displacement,axis=1)
        return -4*np.sum(displacement/distances[:,None]**3,axis=0)
    scaling_residuals=[float(np.linalg.norm(scaled_gravity(2*point)+W0SQ/2*(2*point))) for point in known]
    assert max(scaling_residuals)<1e-10
    near_star=[]
    for orbital_radius in [.1,.05,.01]:
        angles=np.linspace(0,2*math.pi,20001)
        distances=np.sqrt(1+orbital_radius**2+2*orbital_radius*np.cos(angles))
        range_value=float(np.max(distances)-np.min(distances))
        assert abs(range_value-2*orbital_radius)<1e-12
        near_star.append(dict(r_over_a=orbital_radius,geometric_radial_range=range_value,leading_range=2*orbital_radius))
    source_names=['scripts/verify_question_03.py','build/question-03-条件确认.json']
    source_names += [n for n in ['drafts/question-03.md','figures/题03_图稿源文件.tex'] if (ROOT/n).exists()]
    sources={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in source_names}
    report=dict(question=3,pass_all=True,model_condition_resolved=True,approved_model='forced radial response only; no free eccentricity in question 3',normalization='G=m=a=1, l=sqrt(3)',positive_radii_over_a=radii,positive_radii_over_l=[u/math.sqrt(3) for u in radii],cartesian_equilibria=[p.tolist() for p in found],equilibrium_count=len(found),farfield_force_and_ode_checks=farfield,leading_peak_to_peak_coefficient_in_a_units=5/math.sqrt(3),leading_peak_to_peak_coefficient_in_l_units=5/(27*math.sqrt(3)),near_star_geometric_checks=near_star,variant_coupled_initial_value_relative_errors=initial_value_errors,scaled_equilibrium_max_residual=max(scaling_residuals),source_sha256=sources)
    dest=ROOT/'build'/'verification-q03.json';dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
