"""017 Q2: independent field integrals, finite-thickness regularization and Newton sectors."""
from pathlib import Path
import hashlib,json,math,re
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    r,sigma,eps0,mu0,omega,mass,limit=sp.symbols('r sigma eps0 mu0 omega mass limit',positive=True)
    pe=sigma**2/(2*eps0);pm=mu0*sigma**2*omega**2*r**2/2
    traction=mass*omega**2*r**2+r*(pe+pm)
    squared=sp.solve(traction-limit,omega**2)[0]
    handwritten=(2*limit-r*sigma**2/eps0)/(r**2*(2*mass+mu0*r*sigma**2))
    assert sp.simplify(squared-handwritten)==0
    eta=mu0*sigma**2*r/(2*mass)
    noB=(limit-r*pe)/(mass*r*r)
    assert sp.simplify(squared-noB/(1+eta))==0
    assert sp.simplify(pm/pe-mu0*eps0*(omega*r)**2)==0
    # SI exponents ordered (mass, length, time, charge). No numerical constants needed.
    dimensions={'mass':np.array([1,-2,0,0]),'r':np.array([0,1,0,0]),
                'omega':np.array([0,0,-1,0]),'sigma':np.array([0,-2,0,1]),
                'eps0':np.array([-1,-3,2,2]),'mu0':np.array([1,1,0,-2]),
                'traction':np.array([1,0,-2,0])}
    dd=dimensions
    assert np.array_equal(dd['mass']+2*dd['omega']+2*dd['r'],dd['traction'])
    assert np.array_equal(dd['r']+2*dd['sigma']-dd['eps0'],dd['traction'])
    assert np.array_equal(dd['mu0']+2*dd['sigma']+2*dd['omega']+3*dd['r'],dd['traction'])
    assert np.array_equal(dd['mu0']+2*dd['sigma']+dd['r'],dd['mass'])
    # Coulomb and Biot-Savart: integrate an infinite source line in z analytically,
    # then numerically integrate over source azimuth. Observation radius is t*r.
    def field_kernels(t):
        def values(phi):
            ss=math.sin(phi/2)**2
            denominator=(t-1)**2+4*t*ss
            return ((t-1+2*ss)/denominator,(1-t+2*t*ss)/denominator)
        ee=quad(lambda p:values(p)[0],0,math.pi,epsabs=2e-11,epsrel=2e-11)[0]/math.pi
        bb=quad(lambda p:values(p)[1],0,math.pi,epsabs=2e-11,epsrel=2e-11)[0]/math.pi
        return ee,bb
    field_rows=[]
    observations=[.3,.8,.98,.9999,1.0001,1.02,1.2,2.5]
    for t in observations:
        ee,bb=field_kernels(t)
        expected_e=0 if t<1 else 1/t
        expected_b=1 if t<1 else 0
        assert abs(ee-expected_e)<2e-9 and abs(bb-expected_b)<2e-9
        field_rows.append(dict(radius_ratio=t,coulomb_normalized_E=ee,biot_savart_normalized_B=bb))
    averages=[]
    for delta in [.02,.005,.001,.0001]:
        ein,bin_=field_kernels(1-delta);eout,bout=field_kernels(1+delta)
        avg_e=(ein+eout)/2;avg_b=(bin_+bout)/2
        assert abs(avg_e-.5/(1+delta))<2e-9 and abs(avg_b-.5)<2e-9
        averages.append(dict(relative_distance=delta,mean_E=avg_e,mean_B=avg_b))
    # Keep surface charge per mid-surface area fixed while spreading it across a
    # symmetric layer. Integrate actual volume Lorentz force, including area s/r.
    thick,s=sp.symbols('thick s',positive=True)
    aa=r-thick/2;bb=r+thick/2;rho=sigma/thick
    Ebulk=rho*(s*s-aa*aa)/(2*eps0*s)
    Bbulk=mu0*rho*omega*(bb*bb-s*s)/2
    pe_thick=sp.integrate(rho*Ebulk*s/r,(s,aa,bb))
    pm_thick=sp.integrate(rho*omega*s*Bbulk*s/r,(s,aa,bb))
    assert sp.simplify(sp.limit(pe_thick,thick,0)-pe)==0
    assert sp.simplify(sp.limit(pm_thick,thick,0)-pm)==0
    assert sp.simplify(pe_thick-pe*(1-thick/(6*r)))==0
    magnetic_exact=mu0*sigma**2*omega**2*(r*r/2-r*thick/12+thick**2/24+thick**3/(240*r))
    assert sp.simplify(pm_thick-magnetic_exact)==0
    u=sp.symbols('u',positive=True)
    integral_polynomial=bb**2*(bb**3-aa**3)/3-(bb**5-aa**5)/5
    assert sp.simplify(integral_polynomial-(r**3*thick**2-r*r*thick**3/6+r*thick**4/12+thick**5/120))==0
    thick_rows=[]
    for width in [.1,.02,.005,.001]:
        a=1-width/2;b=1+width/2;density=1/width
        actual_pe=quad(lambda radius:density**2*(radius*radius-a*a)/2,a,b,epsabs=2e-11)[0]
        actual_pm=quad(lambda radius:density**2*radius*radius*(b*b-radius*radius)/2,a,b,epsabs=2e-11)[0]
        subs={r:1,sigma:1,eps0:1,mu0:1,omega:1,thick:width}
        assert abs(actual_pe-float(pe_thick.subs(subs)))<2e-10
        assert abs(actual_pm-float(pm_thick.subs(subs)))<2e-10
        thick_rows.append(dict(width_over_radius=width,volume_electric_pressure=actual_pe,volume_magnetic_pressure=actual_pm))
    assert abs(thick_rows[-1]['volume_electric_pressure']-.5)<1e-4
    assert abs(thick_rows[-1]['volume_magnetic_pressure']-.5)<1e-4
    # Finite sector, no infinitesimal-force or fictitious-force approximation.
    sector_rows=[]
    for angle in [.015,.15,.4,1.1]:
        rr=.8;height=1.7;mm=.4;ww=.6;electric=.35;magnetic=.12
        cosine_integral=quad(math.cos,-angle,angle,epsabs=1e-13)[0]
        outward=(electric+magnetic)*rr*height*cosine_integral
        demanded=mm*ww**2*rr**2*height*cosine_integral
        tension=demanded/(2*height*math.sin(angle))+outward/(2*height*math.sin(angle))
        expected=mm*ww**2*rr**2+rr*(electric+magnetic)
        assert abs(tension-expected)<2e-13
        # Newton right-hand side is inward. Edge-tension radial resultant negative.
        residual=outward-2*tension*height*math.sin(angle)+demanded
        assert abs(residual)<2e-13
        sector_rows.append(dict(half_angle=angle,integrated_traction=tension,newton_residual=residual))
    thresholds=[]
    for rr in [.4,1,2.2]:
        for mm in [.15,1,4]:
            for charge in [.05,.3,.8]:
                for margin in [.001,.01,.1]:
                    base=rr*charge**2/2;strength=base*(1+margin)
                    def original_balance(ww):
                        return mm*ww*ww*rr*rr+rr*(charge*charge/2+charge*charge*ww*ww*rr*rr/2)-strength
                    velocity_guess=math.sqrt((strength-base)/mm)
                    numeric=brentq(original_balance,0,2*velocity_guess/rr,xtol=1e-14)
                    analytic=math.sqrt((2*strength-rr*charge**2)/(2*mm+rr*charge**2))/rr
                    assert abs(numeric/analytic-1)<2e-10
                    assert original_balance(numeric*.99)<0 and original_balance(numeric*1.01)>0
                    thresholds.append(dict(r=rr,mu=mm,sigma=charge,relative_static_margin=margin,
                                           omega_from_newton_root=numeric,omega_from_handwritten=analytic,
                                           speed_over_c=numeric*rr,eta=charge*charge*rr/(2*mm)))
    counterexample=dict(r=1,mu=.5,sigma=1,lambda_max=.500001,c=1)
    reserve=counterexample['lambda_max']-.5
    v_exact=math.sqrt(reserve/(counterexample['mu']+.5))
    v_noB=math.sqrt(reserve/counterexample['mu'])
    counterexample.update(speed_exact=v_exact,speed_no_magnetic=v_noB,
                          magnetic_over_electric=v_exact*v_exact,
                          relative_threshold_overestimate=v_noB/v_exact-1)
    assert abs(counterexample['relative_threshold_overestimate']-(math.sqrt(2)-1))<1e-12
    assert v_exact<.001001
    # Re-evaluate the four solved variants from their defining force equations.
    mechanical_omega=brentq(lambda w:.8*w*w*.2**2-320,0,200)
    assert abs(mechanical_omega-100)<1e-11
    charge_fraction=.8
    assert abs(charge_fraction**2-.64)<1e-15
    tolerances=[]
    for q in [.01,.05]:
        numerical_eta=brentq(lambda e:math.sqrt(1+e)-1-q,0,1,xtol=1e-14)
        assert abs(numerical_eta-(2*q+q*q))<2e-14
        tolerances.append(dict(relative_tolerance=q,eta_from_root=numerical_eta))
    # A direct cross product checks both signs independently of the scalar pressure.
    direction_rows=[]
    for charge in [-1,1]:
        for angular_speed in [-.6,.6]:
            velocity=np.array([0,angular_speed,0])
            magnetic=np.array([0,0,charge*angular_speed/2])
            force=charge*np.cross(velocity,magnetic)
            assert abs(force[0]-angular_speed**2/2)<1e-15 and np.all(force[1:]==0)
            direction_rows.append(dict(sigma=charge,omega=angular_speed,radial_magnetic_force=float(force[0])))
    doc=ROOT/'drafts/question-02.md'
    figure_names=['question-02','fields-02','mean-02','sector-02','strength-02']
    present=doc.exists() and '<!-- question-complete -->' in doc.read_text() and all((ROOT/f'figures/{name}.pdf').exists() for name in figure_names)
    source_hashes={'scripts/verify_question_02.py':sha(Path(__file__))}
    figure_hashes={}
    if present:
        source_hashes['drafts/question-02.md']=sha(doc)
        source_hashes['figures/\u989802_\u56fe\u7a3f\u6e90\u6587\u4ef6.tex']=sha(ROOT/'figures/\u989802_\u56fe\u7a3f\u6e90\u6587\u4ef6.tex')
        figure_hashes={name:sha(ROOT/f'figures/{name}.pdf') for name in figure_names}
        text=doc.read_text()
        assert len(re.findall(r'^## ',text,re.M))==9
        assert all(f'../figures/{name}.png' in text for name in figure_names)
        assert r'\frac{t^3}{240r}' in text
    report=dict(question=2,verified_math=True,document_complete=present,set_accepted=False,
                scope='independent mathematical checks bound to question source and figures; PDF review remains separate' if present else 'independent preliminary verification, not complete solution or PDF acceptance',
                field_integrals=field_rows,wall_mean_field_limits=averages,
                finite_thickness_integrals=thick_rows,finite_sector_force_balance=sector_rows,
                independent_newton_threshold_roots=thresholds,low_speed_threshold_counterexample=counterexample,
                solved_variants=dict(mechanical_omega=mechanical_omega,period=2*math.pi/mechanical_omega,
                                     wall_speed=.2*mechanical_omega,charge_fraction_static_traction=charge_fraction**2,
                                     tolerance_roots=tolerances),
                signed_vector_cross_products=direction_rows,
                finite_thickness_magnetic_exact=str(sp.expand(pm_thick)),
                finite_thickness_magnetic_series=str(sp.series(pm_thick,thick,0,3)),
                hoop_traction=str(traction),handwritten_omega_squared=str(handwritten),
                direction='electric and magnetic self-forces are radially outward, even for negative sigma',
                source_sha256=source_hashes,figures_sha256=figure_hashes,
                originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')})
    (ROOT/'build').mkdir(exist_ok=True)
    out=ROOT/('build/verification-q02.json' if present else 'build/verification-q02-preliminary.json')
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'verified_math':True,'document_complete':present,'field_integrals':len(field_rows),
                      'finite_thickness_samples':len(thick_rows),'finite_sectors':len(sector_rows),
                      'threshold_roots':len(thresholds),'magnetic_series':report['finite_thickness_magnetic_series'],
                      'low_speed_counterexample':counterexample},ensure_ascii=False))
if __name__=='__main__':main()
