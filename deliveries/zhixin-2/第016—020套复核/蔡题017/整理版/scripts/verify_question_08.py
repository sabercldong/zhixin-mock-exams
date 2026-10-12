"""017 Q8: independent photon four-momentum events and proper-time ODE checks.

Numerics use c=1, m0=1. The published units and dimensional checks are separate.
Generation of this report never claims PDF/visual or whole-set acceptance.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def target(z,lam,scheme):
    if scheme==1:
        A=1+z;m=A-lam*z;D=A/m
    else:
        A=1+z/2;X=lam*z;m=A-X;D=(A+X)/m
    eta=math.log(D);g=math.cosh(eta);b=math.tanh(eta)
    accel=(1 if scheme==1 else 1+g*(1-b))/(m*g**3)
    return m,g,b,accel
def photon_event(m,b,dm,scheme):
    # Solve actual rest-frame energy + momentum for unknown recoil momentum.
    g=1/math.sqrt(1-b*b)
    incomingE=0. if scheme==1 else g*dm
    incomingP=0. if scheme==1 else -g*b*dm
    after_mass=m-dm
    plus=m+incomingE+incomingP
    recoil=brentq(lambda p:math.hypot(after_mass,p)+p-plus,
                 0.,m+incomingE+abs(incomingP),xtol=5e-15,rtol=2e-14)
    Er=math.hypot(after_mass,recoil);q=recoil-incomingP
    assert q>=0 and abs(Er+q-(m+incomingE))<2e-10*(m+incomingE)
    assert abs(recoil-q-incomingP)<2e-10*(m+incomingE)
    labE=g*(Er+b*recoil);labP=g*(recoil+b*Er)
    photon_lab=g*q*(1-b)
    oldE=g*m;oldP=g*b*m
    assert abs(labE+photon_lab-(oldE+(dm if scheme==2 else 0)))<5e-10*max(oldE,1)
    assert abs(labP-photon_lab-oldP)<5e-10*max(oldE,1)
    return after_mass,labP/labE,photon_lab,recoil,q
def integrated(z,lam,scheme):
    mass=1+z if scheme==1 else 1+z/2
    def ode(mu,state):
        E,p,m,t,x=state;g=E/m;b=p/E
        # The incoming ambient mass is initially at rest in the lab.
        rest_beam=1. if scheme==1 else 1.+g
        lab_beam=rest_beam*g*(1-b)
        return [(0. if scheme==1 else 1.)-lab_beam,
                lab_beam,-1.,g,p/m]
    return solve_ivp(ode,[0,lam*z],[mass,0.,mass,0.,0.],method='DOP853',
                     rtol=3e-12,atol=2e-12,dense_output=True)
def braking_event(m,b,dm):
    # Exact forward-photon event in the initial instantaneous rest frame.
    g=1/math.sqrt(1-b*b);after=m-dm
    recoil=brentq(lambda p:math.hypot(after,p)+p-m,0.,m,
                 xtol=5e-15,rtol=2e-14)
    Er=math.hypot(after,recoil);q=recoil
    labE=g*(Er-b*recoil);labP=g*(-recoil+b*Er)
    photon=g*q*(1+b)
    assert abs(labE+photon-g*m)<2e-10*max(m*g,1)
    assert abs(labP+photon-g*b*m)<2e-10*max(m*g,1)
    return after,labP/labE,photon
def main():
    A,s,X,Z,L=sp.symbols('A s X Z L',positive=True)
    g1=(A*A+s*s)/(2*A*s);b1=(A*A-s*s)/(A*A+s*s)
    g2=(A*A+X*X)/(A*A-X*X);b2=2*A*X/(A*A+X*X)
    assert sp.simplify(g1*g1*(1-b1*b1)-1)==0
    assert sp.simplify(g2*g2*(1-b2*b2)-1)==0
    assert sp.simplify(g1*(1+b1)*s-A)==0
    assert sp.simplify(g2*(1+b2)*(A-X)-(A+X))==0
    assert sp.simplify(g2*(1-b2)-(A-X)/(A+X))==0
    a1=1/(s*g1**3);a2=(1+g2*(1-b2))/((A-X)*g2**3)
    assert sp.simplify(a1-8*A**3*s*s/(A*A+s*s)**3)==0
    assert sp.simplify(a2-2*A*(A*A-X*X)**2/(A*A+X*X)**3)==0
    assert sp.simplify(sp.diff(a1,s)/a1-2*(A*A-2*s*s)/(s*(A*A+s*s)))==0
    assert sp.simplify(sp.diff(a2,X)/a2+4*X/(A*A-X*X)+6*X/(A*A+X*X))==0
    assert sp.simplify(a1.subs(s,A/sp.sqrt(2))-32/(27*A))==0
    # Direct differentiation of beta(lambda) and laboratory time integrals.
    tt1=(A*sp.log(A/s)+(A*A-s*s)/(2*A))/2
    xx1=(A*sp.log(A/s)-(A*A-s*s)/(2*A))/2
    tt2=A*sp.log((A+X)/(A-X))-X
    xx2=A*sp.log(A*A/(A*A-X*X))
    assert sp.simplify(-sp.diff(tt1,s)-g1)==0
    assert sp.simplify(-sp.diff(xx1,s)-g1*b1)==0
    assert sp.simplify(sp.diff(tt2,X)-g2)==0
    assert sp.simplify(sp.diff(xx2,X)-g2*b2)==0
    assert sp.simplify(-sp.diff(b1,s)/g1-a1)==0
    assert sp.simplify(sp.diff(b2,X)/g2-a2)==0
    # Acceleration transformation from the actual velocity addition map.
    u,w=sp.symbols('u w',real=True)
    velocity=(u+w)/(1+u*w)
    assert sp.simplify(sp.diff(velocity,w).subs(w,0)-(1-u*u))==0
    assert sp.simplify(b1.subs({A:1+Z,s:1})-b2.subs({A:1+Z/2,X:Z/2}))==0
    event_rows=[];global_rows=[];ode_rows=[];local_rows=[];comparison=[]
    for z in [.02,.4,2.,10.,100.]:
        for rho in [.15,.65,1.]:
            for scheme in [1,2]:
                lam=rho if scheme==1 else rho/2
                m,g,b,accel=target(z,lam,scheme)
                initial=1+z if scheme==1 else 1+z/2
                total_initial=initial+(lam*z if scheme==2 else 0)
                # The unknown beta is solved from independent global conservation.
                root=brentq(lambda beta:m*(1+beta)/math.sqrt(1-beta*beta)-total_initial,
                            0.,min(1-1e-13,b+.02),xtol=2e-14,rtol=2e-14)
                assert abs(root-b)<2e-11
                emitted=g*b*m
                assert abs(g*m+emitted-total_initial)<2e-10*total_initial
                global_rows.append(dict(Z=z,rho=rho,scheme=scheme,
                    velocity_root=root,mass=m,photon_energy_over_c2=emitted))
                for steps in [37,211]:
                    dm=lam*z/steps;mass=initial;speed=0.;photons=0.
                    for j in range(steps):
                        mass,speed,beam,_,_=photon_event(mass,speed,dm,scheme)
                        photons+=beam
                    assert abs(speed-b)<4e-10 and abs(mass-m)<2e-10*initial
                    assert abs(photons-emitted)<2e-8*total_initial
                    event_rows.append(dict(Z=z,rho=rho,scheme=scheme,steps=steps,
                        speed=speed,velocity_error=abs(speed-b),
                        total_photon_energy=photons,energy_error=abs(photons-emitted)))
                sol=integrated(z,lam,scheme);assert sol.success
                E,p,mnum,t,x=sol.y[:,-1]
                assert abs(p/E-b)<2e-9 and abs(mnum-m)<2e-9
                assert abs(E*E-p*p-mnum*mnum)<2e-7*initial**2
                qtime=quad(lambda mu:target(z,mu/z,scheme)[1],0,lam*z,
                           epsabs=2e-10,epsrel=2e-11)[0]
                qdistance=quad(lambda mu:target(z,mu/z,scheme)[1]*target(z,mu/z,scheme)[2],
                               0,lam*z,epsabs=2e-10,epsrel=2e-11)[0]
                if scheme==1:
                    texact=.5*(initial*math.log(initial/m)+(initial**2-m**2)/(2*initial))
                    xexact=.5*(initial*math.log(initial/m)-(initial**2-m**2)/(2*initial))
                else:
                    consumed=lam*z
                    texact=initial*math.log((initial+consumed)/(initial-consumed))-consumed
                    xexact=initial*math.log(initial**2/(initial**2-consumed**2))
                assert abs(t-texact)<3e-8*max(texact,1) and abs(x-xexact)<3e-8*max(xexact,1)
                assert abs(t-qtime)<3e-8*max(t,1) and abs(x-qdistance)<3e-8*max(x,1)
                # Coordinate acceleration from E,p derivatives, not beta's closed form.
                rest_beam=1. if scheme==1 else 1.+E/mnum
                lab_beam=rest_beam*(E-p)/mnum
                dE=(0. if scheme==1 else 1.)-lab_beam;dp=lab_beam
                numerical_accel=(dp*E-p*dE)/(E*E)/(E/mnum)
                assert abs(numerical_accel-accel)<3e-9*max(accel,1)
                ode_rows.append(dict(Z=z,rho=rho,scheme=scheme,
                    final_speed=p/E,coordinate_accel=numerical_accel,
                    lab_time=t,lab_distance_over_c=x,
                    independent_time_quadrature=qtime,independent_distance_quadrature=qdistance))
    # Shrinking exact recoil events independently recover the local rates.
    for mass in [1.,4.,20.]:
        for speed in [0.,.3,.8,.97]:
            for scheme in [1,2]:
                g=1/math.sqrt(1-speed**2)
                expected=(1. if scheme==1 else 1.+g*(1-speed))/mass
                errors=[]
                for fraction in [1e-4,5e-5,2.5e-5]:
                    dm=mass*fraction
                    _,_,_,p,q=photon_event(mass,speed,dm,scheme)
                    rest_velocity=p/math.hypot(mass-dm,p)
                    estimate=rest_velocity/dm
                    errors.append(abs(estimate-expected))
                    assert abs(q/dm-(1. if scheme==1 else 1.+g))<.006*(1+g)
                assert errors[-1]<errors[0]*.27+2e-9
                assert errors[-1]<2e-4*max(expected,1)
                local_rows.append(dict(mass=mass,speed=speed,scheme=scheme,
                    proper_accel=expected,exact_event_rate_errors=errors))
    for z in [.02,.5,4.,30.]:
        for rho in np.linspace(0,1,21):
            one=target(z,float(rho),1)[2];two=target(z,float(rho)/2,2)[2]
            assert two+2e-13>=one
            if 0<rho<1:assert two>one
            comparison.append(dict(Z=z,rho=float(rho),scheme1=one,scheme2=two))
    # Complete numerical variants and acceleration/deceleration mass-budget check.
    thresholds=[]
    for speed in [.8,.99]:
        ratio=math.sqrt((1+speed)/(1-speed));z=ratio-1;g=1/math.sqrt(1-speed*speed)
        assert abs(target(z,1.,1)[2]-speed)<1e-12
        assert abs(target(z,.5,2)[2]-speed)<1e-12
        thresholds.append(dict(target_speed=speed,Z_min=z,initial_mass_over_m0=ratio,
                               gamma=g,photon_energy_over_m0c2=g*speed))
    numeric=[]
    for scheme in [1,2]:
        z=4.;lam=.25;m,g,b,a=target(z,lam,scheme)
        sol=integrated(z,lam,scheme)
        numeric.append(dict(scheme=scheme,Z=z,lambda_value=lam,mass_over_m0=m,
            gamma=g,beta=b,coordinate_accel_over_alpha_c_per_m0=a,
            proper_accel_over_alpha_c_per_m0=a*g**3,
            proper_time_over_m0_per_alpha=lam*z,
            lab_time_over_m0_per_alpha=float(sol.y[3,-1]),
            distance_over_m0_c_per_alpha=float(sol.y[4,-1])))
    full=[]
    for scheme in [1,2]:
        lam=1. if scheme==1 else .5
        sol=integrated(4.,lam,scheme)
        full.append(dict(scheme=scheme,proper_time=4.*lam,
            lab_time=float(sol.y[3,-1]),distance_over_c=float(sol.y[4,-1])))
    speed=.8;D=math.sqrt((1+speed)/(1-speed));initial=D*D;mid=D
    m,b,_,_,_=photon_event(initial,0.,initial-mid,1)
    assert abs(b-speed)<1e-12 and abs(m-mid)<1e-12
    # For braking the photon goes forward; global conservation gives m exp(-eta) constant.
    final_mass=1.;final_eta=math.log(mid/final_mass);assert abs(math.tanh(final_eta)-b)<1e-12
    braking=[]
    for steps in [17,89]:
        mass=initial;speed=0.;backward_photons=0.;forward_photons=0.
        for _ in range(steps):
            mass,speed,q,_,_=photon_event(mass,speed,(initial-mid)/steps,1)
            backward_photons+=q
        assert abs(speed-.8)<2e-11 and abs(mass-mid)<2e-11
        for _ in range(steps):
            mass,speed,q=braking_event(mass,speed,(mid-1)/steps)
            forward_photons+=q
        assert abs(speed)<2e-11 and abs(mass-1)<2e-11
        assert abs(backward_photons-forward_photons)<2e-10
        assert abs(mass+backward_photons+forward_photons-initial)<2e-10
        braking.append(dict(events_per_leg=steps,final_mass=mass,final_beta=speed,
            backward_photon_energy=backward_photons,forward_photon_energy=forward_photons))
    names=['question-08','global-08','local-08','capture-08','frames-08','comparison-08']
    sources=['scripts/verify_question_08.py','drafts/question-08.md','figures/题08_图稿源文件.tex']
    complete=all((ROOT/p).exists() for p in sources) and all(
        (ROOT/f'figures/{n}.{ext}').exists() for n in names for ext in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-08.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察','易错点','课堂讲解建议','变式训练']
        assert [s.split('、',1)[1] for s in text.splitlines() if s.startswith('## ')]==modules
        assert text.count('<!-- question-complete -->')==1
        assert all(text.count(f'../figures/{name}.png')==1 for name in names)
    report=dict(question=8,verified_math=True,document_complete=complete,set_accepted=False,
        scope='independent finite photon recoil and collected-particle four-momentum, ODE and quadrature; not visual or whole-set acceptance',
        global_conservation_roots=global_rows,finite_events=event_rows,
        proper_time_energy_momentum_ODE=ode_rows,local_rate_convergence=local_rows,
        equal_total_annihilation_fraction_comparison=comparison,
        exact_forward_photon_braking_cases=braking,
        solved_variants=dict(fuel_thresholds=thresholds,same_lambda=numeric,
                            full_burn_Z4=full,acceleration_and_braking=dict(beta=.8,
                            initial_mass_over_m0=initial,turnover_mass_over_m0=mid,Z=initial-1)),
        symbolic_gamma_velocity_acceleration_and_time_checks_passed=True,
        symbolic_acceleration_extrema_and_admissible_interval_checked=True,
        dimensional_checks=dict(order=['mass','length','time'],alpha=[1,0,-1],
            acceleration=[0,1,-2],alpha_c_over_m0=[0,1,-2],
            recoil_energy_remainder=[1,2,-2],recoil_momentum_remainder=[1,1,-1],
            proper_time=[0,0,1],laboratory_time=[0,0,1],distance=[0,1,0],
            gamma_beta_Z_lambda=[0,0,0],passed=True),
        assumptions=['all photons collimated opposite travel during acceleration',
            'ideal complete conversion and no residual heat, capture loss or gravity',
            'lambda M is consumed onboard fuel mass: total mixture in scheme 1, positive matter alone in scheme 2',
            'alpha is onboard mass consumption per proper time in both schemes; scheme 2 adds equal ambient antimatter mass',
            'ambient antimatter initially stationary in the lab; its incoming kinetic energy and negative momentum in the instantaneous rest frame are retained',
            'distance 1520 light years is context; all-fuel acceleration is not an at-rest arrival'],
        handwritten_notes=['retain global collinear photon energy-momentum and instantaneous-rest-frame route',
            'the five handwritten final formulas agree with independent physical conservation under the onboard-rate convention',
            'scheme 2 annihilated total mass is 2 lambda M and rest-frame beam power is (1+gamma) alpha c^2, not 2 alpha c^2 at finite speed',
            'gamma-cubed acceleration transform includes both velocity increment and time dilation'],
        source_sha256={p:sha(ROOT/p) for p in sources if (ROOT/p).exists()},
        figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in names} if complete else {},
        originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')})
    filename='verification-q08.json' if complete else 'verification-q08-preliminary.json'
    (ROOT/'build'/filename).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,
        global_cases=len(global_rows),finite_event_cases=len(event_rows),ODE_cases=len(ode_rows),
        local_rate_cases=len(local_rows),comparison_cases=len(comparison),
        numerical_variants=report['solved_variants']),ensure_ascii=False))
if __name__=='__main__':main()
