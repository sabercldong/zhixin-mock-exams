"""Q8 toy radiative equilibrium: actual surface integration and energy roots."""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
import sympy as s
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args()
    symbolic=[];numerical=[]
    def zero(name,value):
        assert s.simplify(value)==0,(name,value)
        symbolic.append(dict(test=name,passed=True))
    d,T0,R,S,alpha,eps,sigma=s.symbols('d T0 R S alpha eps sigma',positive=True)
    theta=s.symbols('theta',real=True)
    zero('sphere illuminated hemisphere projected integral',
         s.integrate(2*s.pi*R**2*s.sin(theta)*s.cos(theta),(theta,0,s.pi/2))-s.pi*R**2)
    zero('entire sphere emitting area',s.integrate(2*s.pi*R**2*s.sin(theta),(theta,0,s.pi))-4*s.pi*R**2)
    zero('temperature ratio cancels fixed geometry and optical coefficients',
         (1-d)*alpha*S*s.pi*R**2/(4*s.pi*R**2*eps*sigma)-
         (1-d)*alpha*S/(4*eps*sigma))
    ratio=(1-d)**s.Rational(1,4)
    zero('linear fractional cooling derivative',s.diff(ratio,d).subs(d,0)+s.Rational(1,4))
    zero('quadratic Taylor cooling coefficient',s.diff(ratio,d,2).subs(d,0)/2+s.Rational(3,32))
    zero('third Taylor remainder coefficient',s.diff(ratio,d,3)+s.Rational(21,64)*(1-d)**(-s.Rational(11,4)))
    zero('logarithmic temperature sensitivity to incoming flux',s.diff(s.log(S**s.Rational(1,4)),S)*S-s.Rational(1,4))
    zero('net radiative restoring slope is negative',s.diff(alpha*S*s.pi*R**2-4*s.pi*R**2*eps*sigma*T0**4,T0)+16*s.pi*R**2*eps*sigma*T0**3)
    # These are true quadratures with independent projected-disk geometry.
    for radius in [.5,1.,2.,6371.]:
        hemi=quad(lambda th:2*np.pi*radius**2*np.sin(th)*np.cos(th),0,np.pi/2,epsabs=1e-10)[0]
        disk=quad(lambda u:2*np.sqrt(max(0.,radius**2-u*u)),-radius,radius,epsabs=1e-10)[0]
        rel=abs(hemi-disk)/(np.pi*radius**2)
        assert rel<2e-12
        numerical.append(dict(test='independent surface and projected disk area',radius=radius,relative_difference=rel,passed=True))
    # Use normalized sigma=1; root equations retain all independent factors.
    for reflectivity in [0.,.3,.7]:
        for emissivity in [.5,.9,1.]:
            for drop in [.001,.01,.10]:
                radius=2.;initial=300.;flux=4*emissivity*initial**4/(1-reflectivity)
                absorbed=quad(lambda th:(1-reflectivity)*flux*(1-drop)*2*np.pi*radius**2*np.sin(th)*np.cos(th),0,np.pi/2)[0]
                emitted=lambda temp:4*np.pi*radius**2*emissivity*temp**4
                actual=brentq(lambda temp:(emitted(temp)-absorbed)/emitted(initial),0,initial,xtol=1e-12)
                expected=initial*(1-drop)**.25
                assert abs(actual-expected)<2e-10
                numerical.append(dict(test='actual net energy root with independent albedo and emissivity',
                    reflectivity=reflectivity,emissivity=emissivity,fractional_drop=drop,
                    temperature_K=actual,root_energy_relative_residual=abs(emitted(actual)-absorbed)/absorbed,
                    ratio_formula_difference_K=abs(actual-expected),passed=True))
    exact=300*(.999**.25-1);linear=-300*.001/4;quadratic=linear-300*3*.001**2/32
    bound=300*7*.001**3/(128*(1-.001)**(11/4))
    assert exact<linear<0 and abs(exact-quadratic)<=bound*1.001
    assert float(f'{exact:.1g}')==-.08
    numerical.append(dict(test='one significant digit sign and Taylor remainder',signed_change_K=exact,
        positive_cooling_magnitude_K=-exact,linear_K=linear,quadratic_K=quadratic,
        quadratic_error_K=abs(exact-quadratic),third_order_bound_K=bound,one_significant_digit_K=-.08,passed=True))
    # An explicit extension, not a purported prediction of the year 2030.
    for drop in [.001,.01,.1]:
        eq=(1-drop)**.25;tau=1/(4*eq**3)
        sol=solve_ivp(lambda tm,z:[1-drop-z[0]**4],(0,12*tau),[1.],
                      rtol=2e-12,atol=1e-13,max_step=tau/12,dense_output=True)
        values=sol.sol(np.linspace(0,12*tau,301))[0]
        assert sol.success and np.all(np.diff(values)<=1e-13) and np.min(values)>=eq-1e-12
        assert abs(values[-1]-eq)<7e-6*(1-eq)
        numerical.append(dict(test='nonlinear heat capacity relaxation remains above equilibrium',fractional_drop=drop,
                              final_equilibrium_error=float(values[-1]-eq),normalized_linear_tau=tau,passed=True))
    u=s.symbols('u',positive=True)
    F=s.log((u-1)/(u+1))/4-s.atan(u)/2
    zero('exact cooling primitive derivative',s.diff(F,u)-1/(u**4-1))
    zero('cooling partial fractions',s.Rational(1,4)*(1/(u-1)-1/(u+1))-1/(2*(u**2+1))-1/(u**4-1))
    C,rho,cp=s.symbols('C rho cp',positive=True)
    zero('uniform solid heat capacity relaxation scale',
         (4*s.pi*R**3*rho*cp/3)/(16*s.pi*R**2*eps*sigma*T0**3)-rho*cp*R/(12*eps*sigma*T0**3))
    r=s.symbols('r',real=True)
    equilibrium=((1-r)*S/(4*eps*sigma))**s.Rational(1,4)
    zero('variable albedo logarithmic differential',s.diff(s.log(equilibrium),r)+1/(4*(1-r)))
    zero('variable emissivity logarithmic differential',s.diff(s.log(equilibrium),eps)+1/(4*eps))
    tm,tau,Theta0=s.symbols('tm tau Theta0',positive=True)
    solution=Theta0*s.exp(-tm/tau)
    zero('linear cooling initial value and differential equation',s.diff(solution,tm)+solution/tau)
    zero('ninety percent cooling uses ten percent remaining deviation',solution.subs(tm,tau*s.log(10))/Theta0-s.Rational(1,10))
    # Each extension has independently solved energy balance, not only the published root.
    for flux_ratio,r0,r1 in [(.98,.3,.3),(.999,.3,.3007)]:
        initial=300.;eps0=.8;flux0=4*eps0*initial**4/(1-r0)
        actual=brentq(lambda temp:(4*eps0*temp**4-(1-r1)*flux0*flux_ratio)/(4*eps0*initial**4),0,initial,xtol=1e-12)
        expected=initial*(flux_ratio*(1-r1)/(1-r0))**.25
        assert abs(actual-expected)<2e-10
        numerical.append(dict(test='variant independent power root',flux_ratio=flux_ratio,r0=r0,r1=r1,
                              signed_change_K=actual-initial,formula_difference_K=abs(actual-expected),passed=True))
    v1=300*(.98**.25-1);v1q=-1.5-3*300*.02**2/32
    v1bound=300*7*.02**3/(128*.98**(11/4))
    assert abs(v1-v1q)<v1bound<1.39e-4
    numerical.append(dict(test='variant quadratic remainder',error_K=abs(v1-v1q),bound_K=v1bound,passed=True))
    # Compare implicit primitive with an independently integrated nonlinear ODE.
    # Time below is t/(4 tau_1), so du/dt=1-u^4.
    primitive=lambda x:np.log((x-1)/(x+1))/4-np.arctan(x)/2
    for u0 in [1.001,1.05,1.4]:
        sol=solve_ivp(lambda tm,y:[1-y[0]**4],(0,1),[u0],rtol=2e-12,atol=1e-14,max_step=.005,dense_output=True)
        assert sol.success
        for tm in [.05,.2,.5,1.]:
            value=float(sol.sol(tm)[0]);residual=primitive(u0)-primitive(value)-tm
            assert abs(residual)<2e-9
            numerical.append(dict(test='variant exact implicit cooling vs independent ODE',u0=u0,
                                  dimensionless_time=tm,time_residual=residual,passed=True))
    for radius in [1.,2.]:
        capacity=4*np.pi*radius**3*2*3/3
        restoring=16*np.pi*radius**2*.8*1*300**3
        tau=capacity/restoring
        assert abs(tau/(radius*2*3/(12*.8*300**3))-1)<2e-15
        numerical.append(dict(test='variant radius response time scaling',radius=radius,tau=tau,passed=True))
    readings=[dict(path=p,sha256=sha(ROOT/p),actual_displayed_and_read=True) for p in [
        'preview/originals/paper-03.png','preview/originals/answer-08.png',
        'preview/originals/details/q08-paper.png','preview/originals/details/q08-answer.png']]
    report=dict(paper='014',question='08',math_passed=True,question_accepted=False,set_accepted=False,
        symbolic_count=len(symbolic),numeric_count=len(numerical),symbolic=symbolic,numerical=numerical,
        exact_signed_temperature_change_K=exact,rounding='-0.08 K change, or positive cooling magnitude 0.08 K',
        actual_original_readings=readings,source_sha256={n:sha(ROOT.parent/n) for n in ['试卷.pdf','答案.pdf']},
        script_sha256=sha(Path(__file__)),
        caveats=['题设0.1%变化仅作假想；不宣称2030太阳活动或现实气候预测。',
                 '均匀温度/有效单温度球体，固定反照率与发射率；忽略大气、水循环、地热及反馈。',
                 '太阳波段吸收率不自动等于热红外发射率；两者常量分别保留，比值仍消去。',
                 '无热容量数据不能给降温历时；热容量计算只作为明确新增参数的带解变式。'])
    if args.full:
        report.update(draft_sha256=sha(ROOT/'drafts/question-08.md'),figure_source_sha256=sha(ROOT/'figures/题08_图稿源文件.tex'),
                      working_pdf_checks=json.loads((ROOT/'preview/working-draft-check-q08.json').read_text()))
    target='question-08-math.json' if args.full else 'question-08-initial-math.json'
    (ROOT/'verification'/target).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,symbolic=len(symbolic),numeric=len(numerical),signed_change_K=exact,accepted=False)))
if __name__=='__main__':main()
