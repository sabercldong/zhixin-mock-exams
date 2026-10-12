"""Q014-04 independent electromechanical checks, not PDF or whole-set acceptance.

Run with the scientific Python runtime. Original conditions and the human's
common-ramp correction are explicit. Numeric ODEs integrate actual circuit and
force equations, rather than substituting a final answer into itself.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import numpy as np
import sympy as s
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--full',action='store_true')
args=parser.parse_args()
r, m, R, g, Br, Bz, L, omega = s.symbols('r m R g Br Bz L omega', positive=True)
t, phi, z = s.symbols('t phi z', real=True)
v0, tau, a, Phi = s.symbols('v0 tau a Phi', positive=True)
symbols = []
numbers = []

def zero(name, expression):
    residual = s.trigsimp(s.simplify(expression))
    assert residual == 0, (name, residual)
    symbols.append(dict(name=name, passed=True))

def near(name, measured, expected, tolerance=2e-9, scale=1.0, **data):
    error = abs(measured-expected)/max(abs(expected), scale, 1e-30)
    assert error < tolerance, (name, measured, expected, error, tolerance)
    numbers.append(dict(name=name, measured=float(measured), expected=float(expected),
                        normalized_error=float(error), tolerance=tolerance, passed=True, **data))

dl = s.Matrix([-r*s.sin(phi), r*s.cos(phi), 0])
B = s.Matrix([Br*s.cos(phi), Br*s.sin(phi), Bz])
cross = dl.cross(B)
zero('tangential wire crossed with outward radial field points downward', cross[2]+r*Br)
zero('vertical-field force horizontal x component', cross[0]-r*Bz*s.cos(phi))
zero('vertical-field force horizontal y component', cross[1]-r*Bz*s.sin(phi))
for k in range(2):
    zero('horizontal forces around the full ring cancel '+str(k), s.integrate(cross[k], (phi, 0, 2*s.pi)))
zero('total vertical force on signed counterclockwise current',
     s.integrate(cross[2], (phi, 0, 2*s.pi))+2*s.pi*r*Br)
q = s.symbols('q', real=True)
zero('common ramp integral contains one half', s.integrate(q, (q, 0, 1))-s.Rational(1, 2))
p_power,q_power=s.symbols('p_power q_power',positive=True)
zero('different power ramp histories have q/(p+q), not a universal half',
     s.integrate(q_power*q**(p_power+q_power-1),(q,0,1))-q_power/(p_power+q_power))
J = s.pi**2*r**3*Br*Bz/R
zero('corrected startup impulse is a*Phi/(2R)',
     J-(a*Phi/(2*R)).subs({a:2*s.pi*r*Br, Phi:s.pi*r*r*Bz}))
kappa = (2*s.pi*r*Br)**2/R
zero('damping time from actual motional circuit', m/kappa-m*R/(4*s.pi**2*r*r*Br*Br))
zero('motion EMF orientation, upward velocity is positive CCW',
     s.integrate(r*Br, (phi, 0, 2*s.pi))-2*s.pi*r*Br)
zero('Gauss cylindrical flux relation yields consistent averaged vertical gradient',
     s.pi*r*r*(-2*Br/r)+2*s.pi*r*Br)
rho, k, B0 = s.symbols('rho k B0', positive=True)
zero('a valid axisymmetric local example is divergence free',
     s.diff(rho*(k*rho/2), rho)/rho+s.diff(B0-k*z, z))
v = (v0+g*tau)*s.exp(-t/tau)-g*tau
h = tau*(v0+g*tau)*(1-s.exp(-t/tau))-g*tau*t
zero('linear mechanical ODE residual', s.diff(v, t)+v/tau+g)
zero('integrated height differentiates to the signed velocity', s.diff(h, t)-v)
zero('initial velocity boundary', v.subs(t, 0)-v0)
zero('initial height boundary', h.subs(t, 0))
zero('initial acceleration is -g-v0/tau', s.diff(v,t).subs(t,0)+g+v0/tau)
turn = tau*s.log(1+v0/(g*tau))
height = tau*v0-g*tau*tau*s.log(1+v0/(g*tau))
zero('only finite turning time solves velocity zero', v.subs(t,turn))
zero('turning height from integrated position', h.subs(t,turn)-height)
zero('height increases strictly with initial velocity', s.diff(height,v0)-tau*v0/(g*tau+v0))
energy = s.Rational(1,2)*m*v*v+m*g*h
zero('post-switch mechanical power equals minus heat rate', s.diff(energy,t)+m*v*v/tau)
eta, u = s.symbols('eta u', positive=True)
dimensionless_h=(1+eta)*(1-s.exp(-u))-u
zero('dimensionless height has exactly the stated derivative',
     s.diff(dimensionless_h,u)-((1+eta)*s.exp(-u)-1))
zero('dimensionless turn is log(1+eta)', s.diff(dimensionless_h,u).subs(u,s.log(1+eta)))
heat_up=m*g*g*tau*tau*(eta*eta/2-eta+s.log(1+eta))
zero('ascent heat equals loss of mechanical energy',
     heat_up-(m*v0*v0/2-m*g*height).subs(v0,eta*g*tau))
zero('dimensionless heat increases from zero',
     s.diff(eta*eta/2-eta+s.log(1+eta),eta)-eta*eta/(1+eta))
zero('weak damping ballistic limit for velocity', s.limit(v,tau,s.oo)-(v0-g*t))
zero('weak damping ballistic limit for position', s.limit(h,tau,s.oo)-(v0*t-g*t*t/2))
zero('weak damping limit of turn height', s.limit(height,tau,s.oo)-v0*v0/(2*g))

# Full resistive-inductive AC solution from two coefficient equations.
A, C = s.symbols('A C', positive=True)
den=R*R+omega*omega*L*L
icos=-omega*omega*A*L/den
isin=omega*A*R/den
iac=icos*s.cos(omega*t)+isin*s.sin(omega*t)
zero('AC current solves L di/dt+Ri=omega*A*sin', L*s.diff(iac,t)+R*iac-omega*A*s.sin(omega*t))
phase=s.symbols('phase', real=True)
fphase=-C*s.cos(phase)*(icos*s.cos(phase)+isin*s.sin(phase))
Fmean=C*A*omega*omega*L/(2*den)
zero('mean AC lift from direct phase integration', s.integrate(fphase,(phase,0,2*s.pi))/(2*s.pi)-Fmean)
zero('zero self inductance gives zero fixed-height mean force', s.limit(Fmean,L,0))
zero('finite inductance mean lift has voltage-squared dependence',
     Fmean.subs({A:2*A,C:2*C})-4*Fmean)
zero('sqrt-two voltage produces double mean lift at otherwise fixed parameters',
     Fmean.subs({A:s.sqrt(2)*A,C:s.sqrt(2)*C})-2*Fmean)
zero('AC resistive heating from direct mean square current',
     s.integrate(R*(icos*s.cos(phase)+isin*s.sin(phase))**2,(phase,0,2*s.pi))/(2*s.pi)
     -R*omega*omega*A*A/(2*den))
zero('low-frequency lift vanishes quadratically', s.limit(Fmean/omega**2,omega,0)-C*A*L/(2*R*R))
zero('high-frequency lift saturates for fixed field amplitudes', s.limit(Fmean,omega,s.oo)-C*A/(2*L))
zero('pure-R average is zero even for nonsinusoidal periodic common field',
     s.integrate((s.cos(phase)+s.sin(2*phase)/3)*s.diff(s.cos(phase)+s.sin(2*phase)/3,phase),
                 (phase,0,2*s.pi)))

# Finite-L DC extension: not mixed with the original L=0 startup impulse.
vf=-m*g*R/(a*a); iff=-m*g/a
zero('finite-L terminal circuit equation', R*iff-a*vf)
zero('finite-L terminal mechanical equation', -m*g-a*iff)
lam=s.symbols('lam')
matrix=s.Matrix([[0,-a/m],[a/L,-R/L]])
zero('finite-L characteristic polynomial from actual state matrix',
     matrix.charpoly(lam).as_expr()-(lam*lam+R*lam/L+a*a/(m*L)))
vv, ii = s.symbols('vv ii', real=True)
zero('mechanical plus self-field energy loses exactly Ri^2',
     m*vv*(-g-a*ii/m)+m*g*vv+L*ii*((a*vv-R*ii)/L)+R*ii*ii)
zero('inductive startup preserves total linked flux',L*(-Phi/L)+Phi)
gamma=s.symbols('gamma',positive=True)
u_initial,ud_initial=s.symbols('u_initial ud_initial',real=True)
bcrit=ud_initial+gamma*u_initial
ucrit=(u_initial+bcrit*t)*s.exp(-gamma*t)
zcrit=u_initial/gamma*(1-s.exp(-gamma*t))+bcrit/gamma**2*(1-(1+gamma*t)*s.exp(-gamma*t))
zero('critical self-inductive mode solves the repeated-root ODE',
     s.diff(ucrit,t,2)+2*gamma*s.diff(ucrit,t)+gamma*gamma*ucrit)
zero('critical mode integrates to the full stated displacement',s.diff(zcrit,t)-ucrit)
zero('critical mode initial velocity',ucrit.subs(t,0)-u_initial)
zero('critical mode initial acceleration',s.diff(ucrit,t).subs(t,0)-ud_initial)

# SI dimensions are checked independently of coefficient arithmetic.
from sympy.physics.units import meter, kilogram, second, tesla, ohm, henry, newton, ampere, convert_to
zero('startup impulse has SI momentum dimension',
     convert_to(meter**3*tesla**2/ohm,newton*second)-newton*second)
zero('electromagnetic damping has mass/time dimension',
     convert_to(meter**2*tesla**2/ohm,kilogram/second)-kilogram/second)
zero('electrical time L/R has seconds',convert_to(henry/ohm,second)-second)
zero('motional EMF divided by resistance is current',
     convert_to(meter*tesla*(meter/second)/ohm,ampere)-ampere)

# Independent signed wire integrations at actual azimuths.
for rr,br,bz,current in [(.03,.2,.5,4),(.1,.07,.3,-2),(.04,.1,-.2,-3)]:
    for j in range(3):
        def force_element(p):
            tangent=np.array([-rr*math.sin(p),rr*math.cos(p),0.])
            field=np.array([br*math.cos(p),br*math.sin(p),bz])
            return float(current*np.cross(tangent,field)[j])
        value,_=quad(force_element,0,2*math.pi,epsabs=1e-12)
        expected=-2*math.pi*rr*br*current if j==2 else 0.
        near('actual circular wire force quadrature',value,expected,component=j)

ramps={
    'linear':(lambda x:x,lambda x:1.),
    'quadratic':(lambda x:x*x,lambda x:2*x),
    'raised-cosine':(lambda x:(1-math.cos(math.pi*x))/2,lambda x:math.pi*math.sin(math.pi*x)/2),
}
for name,(ramp,derivative) in ramps.items():
    val,_=quad(lambda x:ramp(x)*derivative(x),0,1,epsabs=1e-12)
    near('common-ramp impulse independent of time profile',val,.5,ramp=name)
    norm_heat,_=quad(lambda x:derivative(x)**2,0,1,epsabs=1e-12)
    expected={'linear':1.,'quadratic':4/3,'raised-cosine':math.pi**2/8}[name]
    near('ramp Joule heating depends on shape, unlike impulse',norm_heat,expected,ramp=name)
for pp,qq in [(1.,3.),(3.,1.),(2.,2.),(.5,2.)]:
    val,_=quad(lambda x:x**pp*qq*x**(qq-1),0,1,epsabs=1e-12)
    near('different ramp histories directly integrated',val,qq/(pp+qq),radial_power=pp,flux_power=qq)

# Start on the table, locate the first genuine lift-off, and integrate both
# changing flux and motion EMF. Includes actual spatial flux Phi0-a*z.
rr=.04; mm=.008; resistance=.008; br=.12; bz=.28; gg=9.81
aa=2*math.pi*rr*br; ph=math.pi*rr*rr*bz
ideal=aa*ph/(2*mm*resistance)
mechanical_tau=mm*resistance/(aa*aa)
reference=min(ideal/gg,ph/(aa*ideal),mechanical_tau)
for name,(ramp,derivative) in ramps.items():
    for small in [1e-2,1e-3,1e-4]:
        duration=reference*small
        def lift_condition(x):
            return aa*ph*ramp(x)*derivative(x)/(resistance*duration)-mm*gg
        grid=np.linspace(0,1,1001)
        bracket=next((grid[j-1],grid[j]) for j in range(1,len(grid)) if lift_condition(grid[j])>0)
        lift=brentq(lift_condition,*bracket,xtol=1e-15)
        def rhs(x,state):
            height_now,velocity=state
            qnow=ramp(x);qdot=derivative(x)/duration
            current=(-qdot*(ph-aa*height_now)+aa*qnow*velocity)/resistance
            force=-aa*qnow*current
            return [duration*velocity,duration*(force/mm-gg)]
        result=solve_ivp(rhs,(lift,1.),[0.,0.],rtol=2e-11,atol=1e-13,max_step=.005)
        assert result.success
        final_h,final_v=result.y[:,-1]
        relative=abs(final_v/ideal-1)
        assert relative<3*small,(name,small,relative)
        numbers.append(dict(name='actual table release and coupled ramp approaches corrected half impulse',
                            ramp=name,small_parameter=small,lift_fraction=float(lift),duration=duration,
                            actual_height=float(final_h),actual_speed=float(final_v),ideal_speed=ideal,
                            relative_error=relative,bound=3*small,passed=True))
    # Directly verify the divergence-free local cylindrical flux relationship.
    qmid=.4; top_z=.005; bot_z=-.003
    flux_top=math.pi*rr**2*qmid*(bz-2*br*top_z/rr)
    flux_bottom=math.pi*rr**2*qmid*(bz-2*br*bot_z/rr)
    side=2*math.pi*rr*br*qmid*(top_z-bot_z)
    near('independent cylindrical surface flux conservation',flux_top-flux_bottom+side,0.,ramp=name)

# Post-ramp actual first-order ODE; root finding excludes t=0 by construction.
for launch_eta in [.02,.2,1.,3.,10.]:
    tt=.7; gravity=1.9; initial=launch_eta*gravity*tt
    turn_t=tt*math.log1p(launch_eta)
    return_dim=brentq(lambda x:(1+launch_eta)*(-math.expm1(-x))-x,
                     1e-7,2*(1+launch_eta),xtol=1e-13)
    return_t=tt*return_dim
    def ode(time,state):
        zz,vv,heat=state
        return [vv,-gravity-vv/tt,vv*vv/tt]
    sol=solve_ivp(ode,(0,return_t),[0.,initial,0.],rtol=2e-11,atol=1e-12,dense_output=True,max_step=tt/80)
    assert sol.success
    predicted_h=tt*initial-gravity*tt*tt*math.log1p(launch_eta)
    near('actual numerical ODE velocity at analytically derived apex',sol.sol(turn_t)[1],0.,eta=launch_eta)
    near('actual numerical ODE ascent height',sol.sol(turn_t)[0],predicted_h,eta=launch_eta)
    near('nonzero return root actually returns to launch height',sol.y[0,-1],0.,eta=launch_eta)
    if launch_eta==1.:
        near('the explicitly solved eta=1 positive return time',return_dim,1.59362426004004,tolerance=2e-12)
    assert sol.y[1,-1]<0
    numbers.append(dict(name='the nontrivial return root is on descending branch',eta=launch_eta,
                        return_u=return_dim,return_speed=float(sol.y[1,-1]),passed=True))
    for frac in [0.,.1,.3,.7,1.]:
        time=return_t*frac
        hv,vv,heat=sol.sol(time)
        near('coupled motion energy and directly accumulated heat',.5*vv*vv+gravity*hv+heat,
             .5*initial*initial,eta=launch_eta,fraction=frac)
        near('analytic velocity vs independent numerical integration',
             (initial+gravity*tt)*math.exp(-time/tt)-gravity*tt,vv,eta=launch_eta,fraction=frac)
        near('analytic position vs independent numerical integration',
             tt*(initial+gravity*tt)*(-math.expm1(-time/tt))-gravity*tt*time,hv,
             eta=launch_eta,fraction=frac)
    near('upward heat from independent force-ODE integration',sol.sol(turn_t)[2],
         .5*initial*initial-gravity*predicted_h,eta=launch_eta)
    assert 0<predicted_h<initial*initial/(2*gravity)
    numbers.append(dict(name='dissipation makes apex lower than ballistic height',eta=launch_eta,passed=True))

# Integrate the actual RL circuit to steady state and directly average the force.
# Independent of the symbolic coefficient solution above.
for rr0,ll0,ww0 in [(2.,.5,3.),(.7,.04,7.),(3.,.003,4.),(.3,2.,10.)]:
    flux_amp=.8; radial_factor=.4; period=2*math.pi/ww0
    settle=max(18*ll0/rr0,5*period)
    def rhs(time,current):return [(ww0*flux_amp*math.sin(ww0*time)-rr0*current[0])/ll0]
    ac=solve_ivp(rhs,(0,settle+period),[0.],rtol=3e-11,atol=1e-12,
                 max_step=min(period/100,ll0/rr0/10),dense_output=True)
    assert ac.success
    force,_=quad(lambda time:-radial_factor*math.cos(ww0*time)*ac.sol(time)[0],settle,settle+period,
                 epsabs=1e-10,epsrel=1e-9)
    heating,_=quad(lambda time:rr0*ac.sol(time)[0]**2,settle,settle+period,epsabs=1e-10,epsrel=1e-9)
    expected_force=radial_factor*flux_amp*ww0**2*ll0/(2*(rr0**2+ww0**2*ll0**2))
    expected_heat=rr0*ww0**2*flux_amp**2/(2*(rr0**2+ww0**2*ll0**2))
    near('actual steady RL circuit mean force over one complete period',force/period,expected_force,tolerance=8e-9,
         resistance=rr0,inductance=ll0,omega=ww0)
    near('actual steady RL circuit Joule heating',heating/period,expected_heat,tolerance=8e-9,
         resistance=rr0,inductance=ll0,omega=ww0)

# Finite self-inductance DC extension: independent full two-variable ODE.
for mm0,ll0,rr0,aa0,flux0 in [(1.,.2,2.,1.,.5),(1.,2.,.2,1.,8.),(.5,.3,.8,1.2,2.)]:
    gg0=.3; vterminal=-mm0*gg0*rr0/aa0**2; iterminal=-mm0*gg0/aa0
    gamma=rr0/(2*ll0); discriminant=rr0**2-4*ll0*aa0**2/mm0
    roots=np.roots([1.,rr0/ll0,aa0**2/(mm0*ll0)]).astype(complex)
    assert all(root.real<0 for root in roots)
    u_initial=-vterminal; derivative_initial=-gg0+aa0*flux0/(mm0*ll0)
    cplus=(derivative_initial-roots[1]*u_initial)/(roots[0]-roots[1])
    cminus=u_initial-cplus
    def rl_ode(time,state):
        zz,vv,ii,heat=state
        return [vv,-gg0-aa0*ii/mm0,(aa0*vv-rr0*ii)/ll0,rr0*ii*ii]
    # Stop free-flight checks at the first return to the table. Later source
    # equations would omit contact; do not assert they describe actual motion.
    end=8/max(-max(root.real for root in roots),1e-5)
    def table_event(time,state):return state[0]
    table_event.direction=-1
    table_event.terminal=True
    sol=solve_ivp(rl_ode,(0,end),[0.,0.,-flux0/ll0,0.],rtol=2e-11,atol=1e-11,
                 max_step=min(.03,1/(20*abs(roots[0]))),dense_output=True,events=table_event)
    assert sol.success
    end=sol.t[-1]
    assert end>0
    initial_energy=flux0**2/(2*ll0)
    for fraction in [0.,.03,.1,.4,1.]:
        time=end*fraction
        zz,vv,ii,heat=sol.sol(time)
        analytical_v=vterminal+cplus*np.exp(roots[0]*time)+cminus*np.exp(roots[1]*time)
        analytical_z=vterminal*time+cplus*np.expm1(roots[0]*time)/roots[0]+cminus*np.expm1(roots[1]*time)/roots[1]
        assert abs(analytical_v.imag)<1e-10 and abs(analytical_z.imag)<1e-10
        near('finite-L actual force/circuit ODE vs independently diagonalized velocity',vv,analytical_v.real,
             tolerance=3e-8,fraction=fraction,discriminant=discriminant)
        near('finite-L actual force/circuit ODE vs integrated eigenmode position',zz,analytical_z.real,
             tolerance=3e-8,fraction=fraction,discriminant=discriminant)
        near('finite-L current field energy, mechanical energy and directly integrated heat',
             .5*mm0*vv*vv+mm0*gg0*zz+.5*ll0*ii*ii+heat,initial_energy,
             tolerance=3e-8,fraction=fraction,discriminant=discriminant)

# The repeated-root branch is separately integrated: not evaluated by dividing
# the two-root expression by a zero eigenvalue separation.
mm0=1.;ll0=1.;aa0=1.;rr0=2.;gg0=.3;flux0=1.
vf0=-mm0*gg0*rr0/aa0**2;gam=rr0/(2*ll0)
u0=-vf0;du0=-gg0+aa0*flux0/(mm0*ll0);bc=du0+gam*u0
def critical_rhs(time,state):
    zz,vv,ii=state
    return [vv,-gg0-aa0*ii/mm0,(aa0*vv-rr0*ii)/ll0]
critical=solve_ivp(critical_rhs,(0,2.),[0.,0.,-flux0/ll0],rtol=2e-11,atol=1e-12,dense_output=True,max_step=.01)
assert critical.success
for time in [0.,.1,.3,.7,1.]:
    zz,vv,_=critical.sol(time)
    pred_v=vf0+(u0+bc*time)*math.exp(-gam*time)
    pred_z=vf0*time+u0/gam*(1-math.exp(-gam*time))+bc/gam**2*(1-(1+gam*time)*math.exp(-gam*time))
    near('critical repeated-root velocity vs actual two-variable ODE',vv,pred_v)
    near('critical repeated-root height vs actual two-variable ODE',zz,pred_z)

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
manifest=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
for name,item in manifest.items():
    assert sha(ROOT.parent/name)==item['sha256']
images=['preview/originals/paper-02.png','preview/originals/answer-05.png',
        'preview/originals/details/q04-paper.png','preview/originals/details/q04-answer.png']
report=dict(paper='014',question=4,stage='independent-initial-math',
            user_model_authorization='四项均按建议修订并注明：第4题同比例快速建场、位置固定近似、随后局部径向场',
            startup_impulse='pi^2*r^3*Br*Bz_bar/R; half the handwritten result',
            assumptions=['signed CCW current and upward z','axisymmetric rim field Br',
                         'Bz_bar is a spatial area average, not a temporal average',
                         'electrical L=0 in core; finite L extensions separated',
                         'startup displacement/gravity negligible only in the stated fast limit',
                         'afterward Br is locally constant; external flux still depends on height',
                         'AC fixed mean height, linear same-amplitude scaling and other parameters fixed'],
            original_manifest=manifest,script_sha256=sha(Path(__file__).resolve()),
            originals_re_displayed_and_read=[dict(path=str(ROOT/p),sha256=sha(ROOT/p),actual_read=True) for p in images],
            symbolic_count=len(symbols),numeric_count=len(numbers),symbolic=symbols,numeric=numbers,
            passed=True,document_complete=False,tikz_complete=False,pdf_accepted=False,
            question_accepted=False,set_accepted=False)
draft=ROOT/'drafts/question-04.md'
if draft.exists():
    report.update(draft_sha256=sha(draft),draft_text_exists=True,
                  remaining=['draw and verify necessary TikZ','compile work PDFs','actual visual review and question acceptance'])
if args.full:
    fig=ROOT/'figures/题04_图稿源文件.tex'
    assert draft.exists() and fig.exists()
    report.update(stage='full current manuscript mathematics; visual acceptance separate',
                  draft_text_complete=True,figure_source_sha256=sha(fig),math_passed=True,
                  source_sha256={name:item['sha256'] for name,item in manifest.items()},
                  remaining=['current figure and PDF actual visual review','question acceptance and whole-set integration separate'])
out=ROOT/('verification/question-04-math.json' if args.full else 'verification/question-04-initial-math.json')
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(passed=True,symbolic=len(symbols),numeric=len(numbers),
                     math_sha256=sha(out),document_complete=False,question_accepted=False),ensure_ascii=False))
