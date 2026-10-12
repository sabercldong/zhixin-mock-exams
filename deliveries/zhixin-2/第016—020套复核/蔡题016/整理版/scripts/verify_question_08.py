"""Full Q8 verification: approved model, actual pressure integrals and events."""
from pathlib import Path
import hashlib,json,math,subprocess
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
import verify_question_08_preliminary as independent

ROOT=Path(__file__).resolve().parents[1]
NAMES=['question-08','frames-08','pressure-08','events-08','fourforce-08','limits-08']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pressure_ellipsoid(a,b,h,K,p0):
    # Parameterized ellipsoid z=h*cos(theta); oriented n_z*dA =
    # a*b*sin(theta)*cos(theta)dtheta*dphi, not an assumed K*volume.
    # Independently integrate the constant-pressure traction (must cancel),
    # then the smaller varying-pressure part, avoiding large cancellation.
    constant=quad(lambda t:p0*math.sin(t)*math.cos(t),0,math.pi,
        epsabs=1e-7,epsrel=1e-10)[0]
    assert abs(constant)<1e-8
    varying=quad(lambda t:-K*h*math.cos(t)**2*math.sin(t),0,math.pi,
        epsabs=1e-9,epsrel=1e-12)[0]
    return -2*math.pi*a*b*(constant+varying)

def main():
    approval_path=ROOT/'build/question-08-条件确认.json'
    approval=json.loads(approval_path.read_text())
    assert approval['approved'] and approval['document_revision_implemented']
    independent.main()  # Re-run all independent Lorentz, impulse and stress tests.
    prior_path=ROOT/'build/verification-q08-preliminary.json'
    prior=json.loads(prior_path.read_text())
    beta=sp.symbols('b',real=True)
    gam=1/sp.sqrt(1-beta**2)
    assert sp.simplify(1/gam-gam+gam*beta**2)==0
    assert sp.simplify(1-gam**2+gam**2*beta**2)==0
    assert sp.series(gam,beta,0,4).removeO()==1+beta**2/2
    assert sp.series(1/gam,beta,0,4).removeO()==1-beta**2/2
    assert sp.series(gam**2,beta,0,4).removeO()==1+beta**2

    force_cases=[]
    for speed in [0.,.1,.4,.6,.8,.95]:
        gamma=1/math.sqrt(1-speed**2)
        for a,b,h,rho,g in [(2.,.6,.4,1000.,9.8),(.7,.3,.9,760.,9.81),(4.,1.1,.7,1200.,1.62)]:
            V0=4*math.pi*a*b*h/3
            K=rho*g;p0=1e5+2*K*h
            F1=pressure_ellipsoid(a/gamma,b,h,K,p0)
            F2=pressure_ellipsoid(a,b,h,K,p0)
            m0=rho*V0
            G1=gamma*m0*g;G2=gamma*G1
            assert math.isclose(F1,K*V0/gamma,rel_tol=3e-12)
            assert math.isclose(F2,gamma*F1,rel_tol=3e-12)
            assert math.isclose(F2-G2,gamma*(F1-G1),rel_tol=3e-12,abs_tol=1e-8)
            az=(F1-G1)/(gamma*m0);azprime=(F2-G2)/m0
            assert math.isclose(az,-g*speed**2,rel_tol=4e-12,abs_tol=1e-11)
            assert math.isclose(azprime,gamma**2*az,rel_tol=4e-12,abs_tol=1e-11)
            force_cases.append(dict(beta=speed,V0=V0,pressure_surface_integral_S=F1,
                pressure_surface_integral_Sprime=F2,G1=G1,G2=G2,
                instantaneous_acceleration_S=az,instantaneous_acceleration_Sprime=azprime))

    # Independently solve actual surface-integral force equality, not just
    # substitute the closed-form beta_c into itself.
    roots=[]
    for ratio in [.19,.36,.64,.81,.99]:
        a,b,h,rho=1.2,.4,.3,1000.
        V0=4*math.pi*a*b*h/3;g=9.8;K=rho*g
        def residual(s):
            gamma=1/math.sqrt(1-s*s)
            return pressure_ellipsoid(a/gamma,b,h,K,1e5)-gamma*ratio*rho*V0*g
        root=brentq(residual,0,.999,xtol=1e-13)
        assert abs(root-math.sqrt(1-ratio))<2e-13
        roots.append(dict(boat_water_density_ratio=ratio,root_beta=root,
                          actual_surface_force_residual=residual(root)))
    # Numerical variant1 from an actual box top/bottom integral.
    gamma=1.25;rho=1000.;g=9.8;A0=2.;height=.5
    bottom=1e5+rho*g*height;top=1e5
    F1=quad(lambda x:(bottom-top)*.5,0,4/gamma)[0]
    F2=quad(lambda x:(bottom-top)*.5,0,4)[0]
    G1=gamma*rho*g;G2=gamma*G1
    variant1=dict(F1=F1,F2=F2,G1=G1,G2=G2,H1=G1-F1,H2=G2-F2,
        az=(F1-G1)/(gamma*rho),azprime=(F2-G2)/rho)
    for key,val in dict(F1=7840.,F2=9800.,G1=12250.,G2=15312.5,H1=4410.,H2=5512.5,az=-3.528,azprime=-5.5125).items():
        assert abs(variant1[key]-val)<1e-9
    # Variant3 alternative force prescription; deliberately not the main model.
    for speed in [.1,.4,.8,.95]:
        gamma=1/math.sqrt(1-speed**2)
        # Actual integrated pressure and transformed alternate weight.
        alternateF=pressure_ellipsoid(2/gamma,.5,.5,9.8,30)
        m0=4*math.pi*2*.5*.5/3
        alternateG=m0*9.8/gamma
        assert abs(alternateF-alternateG)<2e-13
        assert abs(gamma*alternateG-m0*9.8)<2e-13
    # Variant4 computed from full tensor multiplication.
    speed=.8;gamma=1/math.sqrt(1-speed*speed)
    L=np.array([[gamma,-gamma*speed,0,0],[-gamma*speed,gamma,0,0],
                [0,0,1,0],[0,0,0,1]])
    T=L@np.diag([1.,.02,.02,.02])@L.T
    assert abs(T[0,0]-2.8133333333333333)<2e-15
    assert abs(T[3,3]-.02)<1e-16
    correction=(T[0,0]-gamma**2)/gamma**2
    assert abs(correction-.0128)<3e-16
    from sympy.physics.units import kilogram,meter,second,newton,pascal,convert_to
    assert sp.simplify(convert_to(kilogram/meter**3*meter**3*meter/second**2,newton)/newton)==1
    assert sp.simplify(convert_to(kilogram/meter**3*meter/second**2*meter,pascal)/pascal)==1
    text=(ROOT/'drafts/question-08.md').read_text()
    assert '<!-- question-complete -->' in text and text.count('\n## ')==9
    for term in ['水与潜水艇的静止密度均','理想外力模型','不是狭义相对论','\\boxed{\\rho_0gV_0}']:
        assert term in text,term
    # Geometry source and PDFs are required; visual review is recorded separately.
    geometry=ROOT/'build/projected-geometry-q08.json'
    subprocess.run(['python3',str(ROOT/'scripts/check_projected_question_08.py')],check=True)
    assert json.loads(geometry.read_text())['passed']
    sources={rel:sha(ROOT/rel) for rel in ['drafts/question-08.md',
        'figures/题08_图稿源文件.tex','scripts/verify_question_08.py',
        'scripts/verify_question_08_preliminary.py','scripts/check_projected_question_08.py',
        'build/projected-geometry-q08.json','build/question-08-条件确认.json',
        'build/verification-q08-preliminary.json']}
    result=dict(question=8,verified_math=True,document_complete=True,
        model_condition_resolved=True,set_accepted=False,
        answer='V1=V0/gamma;rho1=rho2=gamma^2*rho0 (stress neglected);G1=gamma*m0*g (given);F1=m0*g/gamma;G2=gamma^2*m0*g;F2=m0*g',
        handwriting_correction='F2 is m0*g, not m0*g/gamma^2; gravity model explicitly prescribed, density definition qualified',
        independent_pressure_surface_cases=force_cases,independent_density_threshold_roots=roots,
        solved_variants=dict(numeric=variant1,critical_beta_for_ratio064=.6,
            alternate_model_neutral=True,finite_pressure_density_ratio=float(T[0,0]),
            finite_pressure_relative_correction=float(correction)),
        preliminary_evidence_sha256=sha(prior_path),
        source_sha256=sources,figures_sha256={name:sha(ROOT/f'figures/{name}.pdf') for name in NAMES},
        originals_sha256={name:sha(ROOT.parent/name) for name in ['试卷.pdf','答案.pdf']})
    (ROOT/'build/verification-q08.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=8,verified_math=True,document_complete=True,
        surface_cases=len(force_cases),independent_roots=len(roots),variants=result['solved_variants']),ensure_ascii=False))
if __name__=='__main__':main()
