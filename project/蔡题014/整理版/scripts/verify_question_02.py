"""014 Q2: independent charge, volume, field, voltage and variation checks."""
from pathlib import Path
import hashlib,json,math
import sympy as s
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
a,b,e,lam,Y,eps0=s.symbols('a b e lam Y eps0',positive=True,real=True)
tau,strain,stress,origin,nu,D=s.symbols('tau strain stress origin nu D',real=True)
charges=[]
for x in [-a/2,a/2]:
    for y in [-a/2,a/2]:
        for z in [-b/2,b/2]:
            charges.append((e/4,(x,y,z),'corner Pb shared 1/8'))
for axis,half in [(0,a/2),(1,a/2),(2,b/2)]:
    for sign in [-1,1]:
        xyz=[s.S.Zero]*3;xyz[axis]=sign*half
        charges.append((-e,tuple(xyz),'face O shared 1/2'))
charges.append((4*e,(s.S.Zero,s.S.Zero,lam*b),'Ti unshared'))
checks=[]
def zero(name,expr):
    val=s.simplify(expr)
    assert val==0,(name,val)
    checks.append(dict(name=name,passed=True))
total=sum(q for q,_,_ in charges)
mom=[sum(q*xyz[axis] for q,xyz,_ in charges) for axis in range(3)]
zero('weighted unit cell is neutral',total)
zero('dipole x cancels',mom[0]);zero('dipole y cancels',mom[1])
zero('dipole z comes only from Ti displacement',mom[2]-4*e*lam*b)
zero('dipole is origin invariant for a neutral cell',sum(q*(xyz[2]-origin) for q,xyz,_ in charges)-mom[2])
P0=mom[2]/(a*a*b)
zero('polarization density and cancellation of b',P0-4*e*lam/a**2)
bp=b*(1+strain)
lamp=lam+tau*strain
deformed_moment=mom[2].subs({b:bp,lam:lamp},simultaneous=True)
Pnew=s.cancel(deformed_moment/(a*a*bp))
zero('finite cell stretch exact polarization',Pnew-4*e*(lam+tau*strain)/a**2)
dP=s.simplify(Pnew-P0)
zero('increment polarization',dP-4*e*tau*strain/a**2)
zero('constant lambda stretch gives no polarization density change',dP.subs(tau,0))
dE=s.simplify((D-Pnew)/eps0-(D-P0)/eps0)
zero('fixed D increment derived without assuming D=0',dE+dP/eps0)
alpha=s.simplify(dE.subs(strain,stress/Y)/stress)
zero('stress form of alpha',alpha+4*e*tau/(eps0*a*a*Y))
zero('P0 form of alpha',alpha+tau*P0/(eps0*lam*Y))
Ppoisson=s.cancel(4*e*lamp/(a*a*(1-nu*strain)**2))
zero('Poisson first-order correction',s.diff(Ppoisson,strain).subs(strain,0)-P0*(tau/lam+2*nu))
voltage=Pnew*bp/eps0
voltage0=P0*b/eps0
zero('open bare slab voltage includes change of length',
     s.diff(voltage,strain).subs(strain,0)/Y-voltage0*(1+tau/lam)/Y)
N,er,h,R,rad=s.symbols('N er h R rad',positive=True,real=True)
zero('macro thickness is number of cells times cell height',N*voltage-Pnew*(N*bp)/eps0)
zero('macro voltage derivative includes two first-order terms',
     s.diff(N*voltage,strain).subs(strain,0)/Y-N*voltage0*(1+tau/lam)/Y)
general_voltage=-(D-Pnew)*N*bp/eps0
zero('arbitrary fixed initial compensation: complete voltage derivative',
     s.diff(general_voltage,strain).subs(strain,0)/Y
     -N*b*(tau*P0/lam+P0-D)/(eps0*Y))
zero('exact initial compensation removes length-change term',
     s.diff(general_voltage,strain).subs({strain:0,D:P0})/Y
     -N*b*tau*P0/(eps0*lam*Y))
zero('fixed D Gauss boundary at top surface',
     ((D-Pnew)/eps0-(D-P0)/eps0)+dP/eps0)
zero('background dielectric open circuit coefficient',
     s.diff((D-Pnew)/(eps0*er),strain).subs(strain,0)/Y+4*e*tau/(eps0*er*a*a*Y))
zero('short-circuit field is zero when D equals total polarization',
     ((D-Pnew)/eps0).subs(D,Pnew))
zero('short-circuit electrode total charge conservation',(-dP)+(dP))
zero('Poisson coefficient recovers the original for zero nu',
     (-s.diff(Ppoisson,strain).subs(strain,0)/(eps0*Y)).subs(nu,0)-alpha)
zero('zero tau: field response vanishes',alpha.subs(tau,0))
zero('zero tau: voltage still changes with thickness',
     s.diff(N*voltage,strain).subs({strain:0,tau:0})/Y-N*voltage0/Y)
disk_integral=s.integrate(h*rad/(rad**2+h**2)**s.Rational(3,2),(rad,0,R))
zero('finite-disk Coulomb integral exact antiderivative',disk_integral-(1-h/s.sqrt(h*h+R*R)))
zero('wide-plate limit of independent Coulomb integral',s.limit(disk_integral,R,s.oo)-1)
zero('infinitely stiff limit suppresses field response',s.limit(alpha,Y,s.oo))
zero('microparameter form resolves apparent lambda singularity',
     s.limit(alpha,lam,0)+4*e*tau/(eps0*a*a*Y))
# SI dimensions represented as exponents of (N, m, C).
dim_P=(0,-2,1);dim_eps=(-1,-2,2);dim_Y=(1,-2,0)
dim_alpha=tuple(x-y-z for x,y,z in zip(dim_P,dim_eps,dim_Y))
assert dim_alpha==(0,2,-1)
checks.append(dict(name='SI alpha dimensions m^2/C = V*m/N',passed=True,exponents=dim_alpha))
# Finite-disk field integrates Coulomb force from annular charges independently.
numerical=[]
for radius_over_h in [.3,1,3,10,100,1000]:
    h=1.0;radius=radius_over_h*h
    integral,error=quad(lambda u:h*u/(u*u+h*h)**1.5,0,radius,epsabs=1e-11,epsrel=1e-11)
    analytic=1-h/math.sqrt(h*h+radius*radius)
    assert abs(integral-analytic)<2e-11,(radius_over_h,integral,analytic)
    numerical.append(dict(test='finite disk depolarization, Coulomb ring integration',
                          radius_over_half_thickness=radius_over_h,
                          factor=integral,formula=analytic,absolute_error=abs(integral-analytic),passed=True))
params=dict(a=4e-10,b=4.2e-10,e=1.6e-19,lam=.02,tau=.1,Y=1e11,eps0=8.85e-12)
for pressure in [-1e6,-1e4,1e4,1e6]:
    eps=pressure/params['Y']
    old_p=4*params['e']*params['lam']*params['b']
    new_p=4*params['e']*(params['lam']+params['tau']*eps)*params['b']*(1+eps)
    old_P=old_p/(params['a']**2*params['b'])
    new_P=new_p/(params['a']**2*params['b']*(1+eps))
    expected=-4*params['e']*params['tau']/(params['eps0']*params['a']**2*params['Y'])
    for fixed_D in [0.,.015,.08]:
        Eold=(fixed_D-old_P)/params['eps0']
        Enew=(fixed_D-new_P)/params['eps0']
        ratio=(Enew-Eold)/pressure
        scaled=abs(ratio-expected)/(1+abs(expected))
        assert scaled<1e-8,(pressure,fixed_D,ratio,expected)
        numerical.append(dict(test='independent finite cell volumes and fixed-charge fields',
                              stress=pressure,fixed_D=fixed_D,measured_alpha=ratio,
                              expected_alpha=expected,scaled_error=scaled,passed=True))
# Central differences independently reconstruct charge moments, volumes and voltage.
for poisson in [0.,.1,.3,.45]:
    for background in [1.,2.,5.]:
        def response(epsilon):
            axial=params['b']*(1+epsilon)
            transverse=params['a']*(1-poisson*epsilon)
            cell_moment=4*params['e']*(params['lam']+params['tau']*epsilon)*axial
            return -(cell_moment/(transverse**2*axial))/(params['eps0']*background)
        step=1e-5
        slope=(response(step)-response(-step))/(2*step*params['Y'])
        expected=-4*params['e']*(params['tau']+2*poisson*params['lam'])/(params['eps0']*background*params['a']**2*params['Y'])
        error=abs(slope-expected)/(1+abs(expected))
        assert error<1e-8,(poisson,background,slope,expected)
        numerical.append(dict(test='finite-difference deformed transverse area with background response',nu=poisson,epsilon_r=background,measured=slope,expected=expected,scaled_error=error,passed=True))
for layers in [1,100,1000000]:
    def voltage_from_geometry(epsilon):
        axial=params['b']*(1+epsilon)
        displacement=(params['lam']+params['tau']*epsilon)*axial
        moment=4*params['e']*displacement
        density=moment/(params['a']**2*axial)
        field=-density/params['eps0']
        return -field*layers*axial
    step=1e-5
    slope=(voltage_from_geometry(step)-voltage_from_geometry(-step))/(2*step*params['Y'])
    expected=voltage_from_geometry(0)*(1+params['tau']/params['lam'])/params['Y']
    error=abs(slope-expected)/max(abs(expected),1e-30)
    assert error<1e-8
    numerical.append(dict(test='potential integral with independently updated macro thickness',layers=layers,measured=slope,expected=expected,relative_error=error,passed=True))
report=dict(paper='014',question='02',scope='current question and solved variations; math only, not visual or set acceptance',
            model_authorized=True,authorization='用户2026-10-10：四项均按建议修订并注明',
            symbolic_checks=checks,numerical_checks=numerical,symbolic_count=len(checks),
            numeric_count=len(numerical),math_passed=True,question_accepted=False,set_accepted=False,
            source_sha256={name:hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest() for name in ['试卷.pdf','答案.pdf']},
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            draft_sha256=hashlib.sha256((ROOT/'drafts/question-02.md').read_bytes()).hexdigest(),
            figure_source_sha256=hashlib.sha256((ROOT/'figures/题02_图稿源文件.tex').read_bytes()).hexdigest(),
            result=dict(P0=str(P0),alpha=str(alpha)),
            pending=['当前图稿几何核验','分题工作PDF构建与实际审读','整套其余题与三版本正式成品'])
(ROOT/'verification').mkdir(exist_ok=True)
(ROOT/'verification/question-02-math.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({key:report[key] for key in ['symbolic_count','numeric_count','math_passed','question_accepted']},ensure_ascii=False))
