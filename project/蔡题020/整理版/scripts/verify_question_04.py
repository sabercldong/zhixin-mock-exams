"""双球穿孔绳：符号展开、原始径向/角向方程、能量积分及变式核验。"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

ROOT=Path(__file__).resolve().parents[1]

def full_equations(m1,m2):
    # 未使用已消元的单坐标最终方程；共同张力由长度加速度约束解出。
    def system(t,z):
        r1,v1,th1,w1,r2,v2,th2,w2=z
        tension=(r1*w1*w1+r2*w2*w2)/(1/m1+1/m2)
        return [v1,r1*w1*w1-tension/m1,w1,-2*v1*w1/r1,
                v2,r2*w2*w2-tension/m2,w2,-2*v2*w2/r2]
    return system

def period_from_energy(amplitude):
    # x=A sin eta消去端点平方根奇性；无量纲取l=omega=m=1。
    a2=amplitude**2
    def smooth(eta):
        s2=a2*math.sin(eta)**2
        return (1-a2)*(1-s2)/math.sqrt(3-a2-s2-a2*s2)
    return 4*quad(smooth,0,math.pi/2,epsabs=1e-12,epsrel=1e-12)[0]

def integrate_orbit(amplitude,m1=1.,m2=1.,velocity=0.,periods=3):
    equilibrium_w1=1.
    equilibrium_w2=math.sqrt(m1/m2)
    r1,r2=1+amplitude,1-amplitude
    initial=[r1,velocity,0.,equilibrium_w1/r1**2,
             r2,-velocity,0.,equilibrium_w2/r2**2]
    kappa=math.sqrt(6*m1/(m1+m2))
    def turning(t,z):return z[1]
    turning.direction=1;turning.terminal=False
    sol=solve_ivp(full_equations(m1,m2),[0,periods*2*math.pi/kappa],initial,
                  events=turning,dense_output=True,rtol=2e-12,atol=2e-13,max_step=.008)
    times=np.linspace(0,sol.t[-1],5001);z=sol.sol(times)
    energy=.5*m1*(z[1]**2+z[0]**2*z[3]**2)+.5*m2*(z[5]**2+z[4]**2*z[7]**2)
    checks=dict(max_length_error=float(np.max(abs(z[0]+z[4]-2))),
                max_velocity_constraint_error=float(np.max(abs(z[1]+z[5]))),
                max_J1_error=float(np.max(abs(m1*z[0]**2*z[3]-m1))),
                max_J2_error=float(np.max(abs(m2*z[4]**2*z[7]-m2*equilibrium_w2))),
                max_relative_energy_error=float(np.max(abs(energy/energy[0]-1))))
    assert max(checks.values())<2e-8
    return sol,times,z,checks,kappa

def main():
    x,l,w,m=sp.symbols('x l w m',positive=True)
    acceleration=w**2*l**4/2*((l+x)**-3-(l-x)**-3)
    expansion=sp.series(acceleration,x,0,6).removeO()
    assert sp.simplify(expansion+3*w**2*x+10*w**2*x**3/l**2+21*w**2*x**5/l**4)==0
    potential=m*w**2*l**4/2*((l+x)**-2+(l-x)**-2)
    assert sp.simplify(-sp.diff(potential,x)/(2*m)-acceleration)==0
    eps,a=sp.symbols('eps a',real=True)
    u=lambda s:(1+s*s)/(1-s*s)**2
    difference=(a*a-eps*eps)*(3-a*a-eps*eps-a*a*eps*eps)/((1-a*a)**2*(1-eps*eps)**2)
    assert sp.factor(u(a)-u(eps)-difference)==0
    periods=[]
    for amplitude in [.001,.01,.05,.1]:
        sol,times,z,checks,kappa=integrate_orbit(amplitude)
        numerical=2*float(sol.t_events[0][0])
        integral=period_from_energy(amplitude)
        linear=2*math.pi/math.sqrt(3)
        assert abs(numerical/integral-1)<2e-8
        frequency_ratio=linear/integral
        first_correction=1+1.25*amplitude**2
        assert abs(frequency_ratio-first_correction)<3*amplitude**4
        periods.append(dict(amplitude_over_l=amplitude,period_from_full_8_state_ODE=numerical,
                            period_from_energy_quadrature=integral,small_amplitude_period=linear,
                            finite_amplitude_frequency_ratio=frequency_ratio,
                            quadratic_frequency_prediction=first_correction,conservation=checks))
    sol,times,z,checks,kappa=integrate_orbit(.002,m1=1.,m2=2.)
    numerical=2*float(sol.t_events[0][0])
    expected=period_from_energy(.002)*math.sqrt(1.5)
    assert abs(numerical/expected-1)<2e-8 and abs(kappa-math.sqrt(2))<1e-14
    variant=dict(masses=[1,2],initial_equilibrium_angular_speed_ratio=1/math.sqrt(2),
                 linear_radial_frequency=math.sqrt(2),full_ODE_period=numerical,
                 energy_quadrature_period=expected,conservation=checks)
    initial_checks=[]
    for delta in [.004,.002]:
        velocity=.7*delta
        sol,times,z,checks,kappa=integrate_orbit(delta,velocity=velocity,periods=2)
        expected_x=delta*np.cos(kappa*times)+velocity/kappa*np.sin(kappa*times)
        integral_x=delta/kappa*np.sin(kappa*times)+velocity/kappa**2*(1-np.cos(kappa*times))
        angle_prediction1=times-2*integral_x
        angle_prediction2=times+2*integral_x
        error_x=float(np.max(abs(z[0]-1-expected_x)))
        error_angle=float(max(np.max(abs(z[2]-angle_prediction1)),np.max(abs(z[6]-angle_prediction2))))
        initial_checks.append(dict(delta=delta,radial_velocity=velocity,max_linear_radial_error=error_x,
                                   max_linear_angle_error=error_angle,conservation=checks))
    assert initial_checks[1]['max_linear_radial_error']<initial_checks[0]['max_linear_radial_error']/6
    assert initial_checks[1]['max_linear_angle_error']<initial_checks[0]['max_linear_angle_error']/3
    files=['scripts/verify_question_04.py','drafts/question-04.md','figures/题04_图稿源文件.tex']
    report=dict(question=4,pass_all=True,normalization='l=m=omega=1 unless specified',
                exact_acceleration_latex=sp.latex(acceleration),acceleration_series_latex=sp.latex(expansion),
                periods=periods,unequal_mass_variant=variant,initial_value_variant_checks=initial_checks,
                source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    (ROOT/'build'/'verification-q04.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
