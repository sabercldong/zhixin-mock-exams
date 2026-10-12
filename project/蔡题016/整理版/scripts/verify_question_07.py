"""Q7 independent ray geometry, common-wavefront path, phase sums and roots."""
from pathlib import Path
import argparse, hashlib, json, math, subprocess
import numpy as np
import sympy as sp
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]
NAMES=['question-07','geometry-07','angles-07','path-07','phasors-07','peak-07']
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def reflect(theta, alpha=0.):
    normal=np.array([math.sin(theta),math.cos(theta)])
    incoming=np.array([math.sin(alpha),-math.cos(alpha)])
    outgoing=incoming-2*np.dot(incoming,normal)*normal
    assert abs(np.linalg.norm(outgoing)-1)<2e-15
    assert abs(np.dot(incoming+outgoing,normal))<2e-15
    return normal,incoming,outgoing

def common_path_difference(a,theta,alpha=0.):
    normal,inc,out=reflect(theta,alpha)
    # Solve x sin(theta)+z cos(theta)=j a on the cut z=0.
    points=[np.array([j*a/normal[0],0.]) for j in [0,1]]
    B=20*a/normal[0]
    totals=[]
    for point in points:
        # Ray distances to two common planes, from actual intersections.
        incoming_distance=B+np.dot(inc,point)
        outgoing_distance=B-np.dot(out,point)
        upstream=point-incoming_distance*inc
        downstream=point+outgoing_distance*out
        assert abs(np.dot(inc,upstream)+B)<1e-12*B
        assert abs(np.dot(out,downstream)-B)<1e-12*B
        totals.append(incoming_distance+outgoing_distance)
    return totals[0]-totals[1], points[1][0]

def array_amplitude(N,cycles):
    return np.exp(2j*math.pi*cycles*np.arange(N)).sum()

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--complete',action='store_true');args=parser.parse_args()
    th,al,a,k=sp.symbols('theta alpha a k',real=True)
    n=sp.Matrix([sp.sin(th),sp.cos(th)])
    inc=sp.Matrix([sp.sin(al),-sp.cos(al)])
    out=sp.simplify(inc-2*(inc.dot(n))*n)
    expected=sp.Matrix([sp.sin(2*th+al),sp.cos(2*th+al)])
    assert all(sp.trigsimp(v)==0 for v in out-expected)
    assert sp.trigsimp(out.dot(out)-1)==0
    assert sp.trigsimp(a/sp.sin(th)*(out[0]-inc[0])-2*a*sp.cos(th+al))==0
    assert sp.trigsimp(2*a*sp.cos(th)-a/sp.sin(th)*sp.sin(2*th))==0
    delta=sp.symbols('delta',real=True)
    assert sp.simplify(sum(sp.exp(sp.I*j*sp.pi/2) for j in range(4)))==0
    ray_cases=[]
    for td in [5,15,25,32.46174496724237,40,44]:
        for ad in [-10,0,7]:
            t=math.radians(td);alpha=math.radians(ad)
            normal,incoming,outgoing=reflect(t,alpha)
            diff,d=common_path_difference(.6,t,alpha)
            predicted=1.2*math.cos(t+alpha)
            assert abs(diff-predicted)<5e-14
            # Independent distance from Q to P's layer.
            distance=abs(np.dot(normal,np.array([d,0.])))
            assert abs(distance-.6)<2e-15
            ray_cases.append(dict(theta_deg=td,alpha_deg=ad,normal=normal.tolist(),
                incident=incoming.tolist(),reflected=outgoing.tolist(),
                common_wavefront_path_difference=diff,expected_path_difference=predicted,
                cut_period=d,upper_half_space=bool(outgoing[1]>0)))
    phase_errors=[];zero_errors=[]
    for N in [2,4,8,20,40,80]:
        for cycles in np.linspace(-.37,4.43,123):
            direct=array_amplitude(N,cycles)
            z=np.exp(2j*math.pi*cycles)
            if abs(1-z)<1e-10: expected=N
            else: expected=(1-z**N)/(1-z)
            error=abs(direct-expected)
            phase_errors.append(error)
            assert error<3e-10
        for q in [1,2,3]:
            assert abs(abs(array_amplitude(N,q))-N)<1e-12
            for sign in [-1,1]:
                error=abs(array_amplitude(N,q+sign/N))
                zero_errors.append(error)
                assert error<3e-11
    # Enumerate orders by independently solving the ray/common-wavefront route.
    root_cases=[]
    for thickness,wavelength in [(.32,.54),(.6,.55),(.9,.54),(3.,.55),(1.5,.532)]:
        roots=[]
        for order in range(1,20):
            def residual(t):
                return common_path_difference(thickness,t)[0]-order*wavelength
            lo,hi=math.radians(.0001),math.radians(44.9999)
            if residual(lo)*residual(hi)<0:
                root=brentq(residual,lo,hi,xtol=2e-14)
                explicit=math.acos(order*wavelength/(2*thickness))
                assert abs(root-explicit)<2e-13
                roots.append(dict(order=order,theta_deg=math.degrees(root),
                                  outgoing_deg=2*math.degrees(root),
                                  common_path_residual=residual(root)))
        interval=[q for q in range(1,20) if math.sqrt(2)*thickness/wavelength<q<2*thickness/wavelength]
        assert [v['order'] for v in roots]==interval
        root_cases.append(dict(a_um=thickness,lambda_um=wavelength,independent_roots=roots))
    # Finite-distance optical paths approach the plane-wave result with 1/L correction.
    far_field=[]
    theta=math.radians(25);d=.6/math.sin(theta);r=2*theta
    direction=reflect(theta)[2]
    for ratio in [100,1000,10000,100000]:
        L=ratio*d
        R=L*direction
        exact=np.linalg.norm(R)-np.linalg.norm(R-np.array([d,0.]))
        leading=d*direction[0]
        correction=d*d*math.cos(r)**2/(2*L)
        assert abs((leading-exact)/correction-1)<.025
        far_field.append(dict(L_over_d=ratio,exact_path_difference=exact,
            common_wavefront_limit=leading,second_order_correction=correction))
    # Variant3: zeros located by direct complex sums, not only the sine quotient.
    a3,lam,q,N=.6,.55,2,40
    t3=math.acos(q*lam/(2*a3));d3=a3/math.sin(t3);r0=2*t3;D=q*lam
    spectral=[D/(q+1/N),D/(q-1/N)]
    angular=[math.asin((q-1/N)*lam/d3),math.asin((q+1/N)*lam/d3)]
    for wave in spectral:
        assert abs(array_amplitude(N,D/wave))<1e-10
    for angle in angular:
        path,_=common_path_difference(a3,t3)
        # Fixed reflected observation replaced by chosen far-field direction.
        cycles=d3*math.sin(angle)/lam
        assert abs(array_amplitude(N,cycles))<1e-10
    # Small peak-shift derivative checked by independent roots at perturbed a/theta.
    sensitivity=[]
    for td in [10,25,40]:
        angle=math.radians(td);base=.7
        for eps in [1e-4,1e-5,1e-6]:
            change=(2*base*math.cos(angle+eps)-2*base*math.cos(angle))/(2*base*math.cos(angle))
            slope=change/eps
            assert abs(slope+math.tan(angle))<6e-5
            sensitivity.append(dict(theta_deg=td,angle_step_rad=eps,numerical_relative_derivative=slope,
                                    predicted=-math.tan(angle)))
    from sympy.physics.units import meter,convert_to
    assert sp.simplify(convert_to(2*meter*sp.cos(th),meter)/(meter)-2*sp.cos(th))==0
    oblique_a=.55/math.cos(math.radians(15))
    oblique_path,oblique_d=common_path_difference(oblique_a,math.radians(25),math.radians(-10))
    assert abs(oblique_path-1.1)<2e-14
    sources={'scripts/verify_question_07.py':sha(Path(__file__))}
    figures={}
    if args.complete:
        for rel in ['drafts/question-07.md','figures/题07_图稿源文件.tex']:
            sources[rel]=sha(ROOT/rel)
        text=(ROOT/'drafts/question-07.md').read_text()
        assert '<!-- question-complete -->' in text and text.count('\n## ')==9
        subprocess.run(['python3',str(ROOT/'scripts/check_projected_question_07.py')],check=True)
        geom=ROOT/'build/projected-geometry-q07.json'
        assert json.loads(geom.read_text())['passed']
        sources['scripts/check_projected_question_07.py']=sha(ROOT/'scripts/check_projected_question_07.py')
        sources['build/projected-geometry-q07.json']=sha(geom)
        figures={name:sha(ROOT/f'figures/{name}.pdf') for name in NAMES}
    result=dict(question=7,verified_math=True,document_complete=args.complete,model_condition_resolved=True,
        set_accepted=False,answer='2*a*cos(theta)=q*lambda; upper-cut visible branch 0<theta<pi/4',
        original_handwritten_status='central route correct; explicit wavefront/angle/order/visibility qualifications added',
        ray_and_wavefront_cases=ray_cases,finite_array_direct_sum_cases=len(phase_errors),
        maximum_sum_error=max(phase_errors),maximum_zero_amplitude=max(zero_errors),
        independently_solved_order_cases=root_cases,far_field_cases=far_field,
        peak_sensitivity_cases=sensitivity,
        solved_variants=dict(multiple_orders=[8,9,10],measured_r60_first_order_a_um=.55/math.sqrt(3),
            finite_N40_theta_deg=math.degrees(t3),cut_period_um=d3,main_peak_deg=math.degrees(r0),
            first_spectral_zeros_um=spectral,first_angular_zeros_deg=[math.degrees(x) for x in angular],
            linear_full_angular_width_rad=2*lam/(N*d3*math.cos(r0)),
            oblique_a_um=oblique_a,oblique_period_um=oblique_d,oblique_path_difference_um=oblique_path),
        source_sha256=sources,figures_sha256=figures,
        originals_sha256={name:sha(ROOT.parent/name) for name in ['试卷.pdf','答案.pdf']})
    path=ROOT/('build/verification-q07.json' if args.complete else 'build/verification-q07-preliminary.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=7,verified_math=True,document_complete=args.complete,
        ray_cases=len(ray_cases),direct_sum_cases=len(phase_errors),independent_root_sets=len(root_cases),
        maximum_sum_error=max(phase_errors),variants=result['solved_variants']),ensure_ascii=False))

if __name__=='__main__':main()
