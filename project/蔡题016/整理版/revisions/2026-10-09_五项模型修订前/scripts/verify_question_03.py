"""016 Q3 preliminary: cone geodesics, ring topology and missing mass contact.

This verifies the handwritten route under its necessary surface-contact model.
It does not assert that the printed statement specifies that model. No complete
question or whole-set acceptance is produced while this condition is unresolved.
"""
from pathlib import Path
import argparse,hashlib,json,math,subprocess
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_bvp
from scipy.optimize import brentq,root

ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def cone_bvp(theta,a=1.,b=1.,delta=math.pi):
    """Solve surface geodesic equations, not the proposed unfolded chord."""
    sine=math.sin(theta)
    mesh=np.linspace(0.,1.,101)
    radius=a+(b-a)*mesh-.6*min(a,b)*mesh*(1-mesh)
    dr=(b-a)-.6*min(a,b)*(1-2*mesh)
    guess=np.vstack([radius,delta*mesh,dr,np.full_like(mesh,delta)])
    def ode(t,y):
        r,phi,rp,pp=y
        return np.vstack([rp,pp,sine*sine*r*pp*pp,-2*rp*pp/r])
    def bc(ya,yb):return np.array([ya[0]-a,ya[1],yb[0]-b,yb[1]-delta])
    solution=solve_bvp(ode,bc,mesh,guess,tol=2e-9,max_nodes=18000)
    assert solution.success,solution.message
    values=solution.sol(np.linspace(0.,1.,501))
    assert np.min(values[0])>0 and np.min(values[3])>0
    speed=np.sqrt(values[2]**2+sine*sine*values[0]**2*values[3]**2)
    assert np.ptp(speed)<3e-8*max(a,b)
    length=quad(lambda t:math.hypot(solution.sol(t)[2],
                    sine*solution.sol(t)[0]*solution.sol(t)[3]),0.,1.,
                    epsabs=3e-10,epsrel=3e-10)[0]
    ya=solution.sol(0.);yb=solution.sol(1.)
    ca=-ya[2]/math.hypot(ya[2],sine*ya[0]*ya[3])
    cb=yb[2]/math.hypot(yb[2],sine*yb[0]*yb[3])
    return solution,length,ca,cb

def cartesian(r,phi,theta):
    return np.array([r*math.sin(theta)*math.cos(phi),
                     r*math.sin(theta)*math.sin(phi),-r*math.cos(theta)])

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--complete',action='store_true')
    args=parser.parse_args()
    theta,r,p=sp.symbols('theta r p',positive=True)
    phi=sp.symbols('phi',real=True)
    position=sp.Matrix([r*sp.sin(theta)*sp.cos(phi),
                      r*sp.sin(theta)*sp.sin(phi),-r*sp.cos(theta)])
    es=position.diff(r);ephi=position.diff(phi)/(r*sp.sin(theta))
    normal=es.cross(ephi)
    assert sp.trigsimp(es.dot(es))==1
    assert sp.trigsimp(ephi.dot(ephi))==1
    assert sp.trigsimp(es.dot(ephi))==0
    assert sp.trigsimp(normal.dot(normal))==1
    assert sp.trigsimp(sp.Matrix([0,0,-1]).dot(es)-sp.cos(theta))==0
    assert sp.trigsimp(sp.Matrix([0,0,-1]).dot(normal)+sp.sin(theta))==0
    a,b,alpha=sp.symbols('a b alpha',positive=True)
    distance=sp.sqrt(a*a+b*b-2*a*b*sp.cos(alpha))
    ca=sp.diff(distance,a);cb=sp.diff(distance,b)
    assert sp.simplify(ca-(a-b*sp.cos(alpha))/distance)==0
    assert sp.simplify(cb-(b-a*sp.cos(alpha))/distance)==0
    assert sp.simplify(ca-cb-(a-b)*(1+sp.cos(alpha))/distance)==0
    beta=sp.symbols('beta',positive=True)
    # Equal endpoint radii: alpha=2 beta and 0<beta<pi/2.
    assert sp.trigsimp((2*r*sp.sin(beta))**2-
                        distance.subs({a:r,b:r,alpha:2*beta})**2)==0
    LA,LB,m,g=sp.symbols('L_A L_B m g',positive=True)
    # The printed statement does not require the two ropes to have equal length.
    Ucontact=-m*g*sp.cos(theta)*(2*r+LA+LB-4*r*sp.sin(beta))
    Uformal=-m*g*(2*r*sp.cos(theta)+LA+LB-4*r*sp.sin(beta))
    assert sp.simplify(sp.diff(Ucontact,r)+
                       2*m*g*sp.cos(theta)*(1-2*sp.sin(beta)))==0
    assert sp.simplify(sp.diff(Uformal,r)+
                       2*m*g*(sp.cos(theta)-2*sp.sin(beta)))==0
    assert sp.simplify(sp.diff(Ucontact,r,2))==0
    critical=sp.asin(sp.Rational(1,3))
    assert sp.simplify(sp.cos(critical)-2*sp.sqrt(2)/3)==0
    beta0=sp.pi/6
    assert sp.simplify(2*sp.sin(beta0)-1)==0
    assert sp.simplify(m*g*sp.cos(critical)/(2*sp.sin(beta0))-
                       2*sp.sqrt(2)*m*g/3)==0
    # A straight vertical tail immediately penetrates the solid cone: at
    # depth r*cos(theta)+h its boundary radius exceeds the tail radius.
    h=sp.symbols('h',positive=True)
    excess=sp.expand((r*sp.cos(theta)+h)*sp.tan(theta)-r*sp.sin(theta))
    assert sp.trigsimp(excess-h*sp.tan(theta))==0
    geodesics=[];normal_checks=[];force_checks=[]
    for theta_value in [.12,.25,.45,.7,1.,1.22]:
        for scale in [.7,1.9]:
            sol,length,ca_num,cb_num=cone_bvp(theta_value,scale,scale)
            beta_value=math.pi*math.sin(theta_value)/2
            expected=2*scale*math.sin(beta_value)
            assert abs(length-expected)<2e-8*scale
            assert abs(ca_num-math.sin(beta_value))<2e-8
            assert abs(cb_num-math.sin(beta_value))<2e-8
            geodesics.append(dict(theta=theta_value,radius=scale,
                BVP_length=length,chord_length=expected,
                endpoint_upward_components=[ca_num,cb_num]))
            # Actual mapped space curves: lengths by Cartesian finite differences,
            # and outwards normal pressure from differentiated unit tangent.
            u=np.linspace(0.,1.,5001);ys=sol.sol(u)
            xyz=np.array([cartesian(z[0],z[1],theta_value) for z in ys.T])
            polygon=float(np.sum(np.linalg.norm(np.diff(xyz,axis=0),axis=1)))
            assert abs(polygon-length)<2e-7*scale
            curve_prime=np.gradient(xyz,u,axis=0,edge_order=2)
            tangent=curve_prime/np.linalg.norm(curve_prime,axis=1)[:,None]
            derivative=np.gradient(tangent,u,axis=0,edge_order=2)/length
            normals=np.column_stack([math.cos(theta_value)*np.cos(ys[1]),
                math.cos(theta_value)*np.sin(ys[1]),
                np.full(len(u),math.sin(theta_value))])
            pressure=-np.sum(derivative*normals,axis=1)
            assert np.min(pressure[5:-5])>0
            es_values=np.column_stack([math.sin(theta_value)*np.cos(ys[1]),
                math.sin(theta_value)*np.sin(ys[1]),
                np.full(len(u),-math.cos(theta_value))])
            ep_values=np.column_stack([-np.sin(ys[1]),np.cos(ys[1]),np.zeros(len(u))])
            tangential_residual=np.max(abs(np.sum(derivative*es_values,axis=1))[5:-5])
            tangential_residual=max(tangential_residual,
                np.max(abs(np.sum(derivative*ep_values,axis=1))[5:-5]))
            assert tangential_residual<2e-5/scale
            normal_checks.append(dict(theta=theta_value,radius=scale,
                polygon_3d_length=polygon,positive_normal_pressure_min=float(np.min(pressure[5:-5])),
                pressure_max=float(np.max(pressure[5:-5])),
                tangential_curvature_residual=float(tangential_residual)))
            # First loop, mass in contact: assemble full 3D forces, including N.
            ep=np.array([0.,1.,0.]);es0=np.array([math.sin(theta_value),0.,-math.cos(theta_value)])
            n0=np.array([math.cos(theta_value),0.,math.sin(theta_value)])
            t1=-ca_num*es0+math.cos(beta_value)*ep
            t2=-ca_num*es0-math.cos(beta_value)*ep
            tension=math.cos(theta_value)/(2*ca_num)
            net=tension*(t1+t2)+np.array([0.,0.,-1.])+math.sin(theta_value)*n0
            assert np.linalg.norm(net)<3e-9
            force_checks.append(dict(theta=theta_value,radius=scale,
                first_loop_T_per_mg=tension,normal_per_mg=math.sin(theta_value),
                net_3d_force_per_mg=net.tolist()))
    # Independent root: endpoint force is recovered from the cone geodesic BVP.
    def contact_residual(t):return 2*cone_bvp(t)[2]-1
    theta_bvp=brentq(contact_residual,.15,.55,xtol=3e-12)
    assert abs(theta_bvp-math.asin(1/3))<3e-9
    _,_,ca0,_=cone_bvp(theta_bvp)
    tail=math.cos(theta_bvp)
    assert abs(2*ca0*tail-tail)<1e-10
    # Independent virtual-work finite differences using BVP lengths.
    virtual=[]
    for t in [.2,theta_bvp,.48]:
        eps=1e-4;ell=4.
        lengths=[cone_bvp(t,1+dr,1+dr)[1] for dr in [-eps,eps]]
        U=[-2*math.cos(t)*(1+dr+ell-d) for dr,d in zip([-eps,eps],lengths)]
        derivative=(U[1]-U[0])/(2*eps)
        expected=-2*math.cos(t)*(1-2*math.sin(math.pi*math.sin(t)/2))
        assert abs(derivative-expected)<3e-7
        virtual.append(dict(theta=t,BVP_energy_derivative=derivative,
            independent_force_derivative=expected))
    # Away from equal height, endpoint derivatives are checked through BVP
    # lengths, not by copying the force formula into the numerical test.
    unequal=[]
    for t in [.18,.32,.7]:
        av,bv=.8,1.4;eps=1e-4
        sol,d,ca_num,cb_num=cone_bvp(t,av,bv)
        da=(cone_bvp(t,av+eps,bv)[1]-cone_bvp(t,av-eps,bv)[1])/(2*eps)
        db=(cone_bvp(t,av,bv+eps)[1]-cone_bvp(t,av,bv-eps)[1])/(2*eps)
        assert abs(da-ca_num)<2e-7 and abs(db-cb_num)<2e-7
        assert abs(ca_num-cb_num)>1e-3
        unequal.append(dict(theta=t,a=av,b=bv,
            radial_derivatives=[da,db],endpoint_force_components=[ca_num,cb_num]))
    # Static equilibrium need not be stable: azimuth displacement reduces U.
    stability=[]
    for deviation in [.01,.02,.04]:
        th=math.asin(1/3);radius=1.2
        dp=cone_bvp(th,radius,radius,math.pi+deviation)[1]
        dm=cone_bvp(th,radius,radius,math.pi-deviation)[1]
        symmetric=2*cone_bvp(th,radius,radius)[1]
        deltaU=math.cos(th)*(dp+dm-symmetric)
        coefficient=-math.cos(th)*radius/36
        assert deltaU<0 and abs(deltaU/deviation**2/coefficient-1)<2e-4
        stability.append(dict(azimuth_displacement=deviation,
            BVP_potential_change=deltaU,quadratic_coefficient=coefficient))
    # Formal alternative, only a force-model illustration: vertical tails inside
    # the cone are not a valid printed topology without new routing conditions.
    formal_s=brentq(lambda v:2*math.sin(math.pi*v/2)-math.sqrt(1-v*v),0.,1.)
    confirmation=ROOT/'build/question-03-条件确认.json'
    approval=json.loads(confirmation.read_text())
    assert approval['confirmed_by']=='human_user' and approval['condition_resolved']
    # Four solved variants, each checked by actual cone BVP geometry/forces.
    x1=1.2/(4*math.sin(math.pi/4));th1=math.pi/6
    sol1,d1,c1,_=cone_bvp(th1,x1,x1)
    T1=.2*9.8*math.cos(th1)/(2*c1)
    midpoint=sol1.sol(.5)[0]
    dz1=(x1-midpoint)*math.cos(th1)
    assert abs(d1-.6)<2e-9 and abs(midpoint-.3)<2e-9
    assert abs(T1-math.sqrt(6)/4*.2*9.8)<2e-9 and x1<.8
    variant2=[]
    for x2 in [.2,.5]:
        _,d2,c2,_=cone_bvp(theta_bvp,x2,x2)
        ends=[x2+.8-d2,x2+1.1-d2]
        T2=.3*9.8*math.cos(theta_bvp)
        assert max(ends)<1.5 and min(.8-d2,1.1-d2)>0
        assert np.max(abs(np.array(ends)-[.8,1.1]))<3e-9
        assert abs(2*T2*c2-T2)<1e-9
        variant2.append(dict(ring_radius=x2,BVP_arc_length=d2,
            tail_lengths=[.8-d2,1.1-d2],mass_radii=ends,T=T2))
    # Unequal masses require the explicitly added azimuth guide reactions.
    pA=.75
    def residual(z):
        theta3,log_ratio=z
        _,_,ca3,cb3=cone_bvp(theta3,math.exp(log_ratio),1.)
        return [ca3-pA,cb3-(1-pA)]
    solved=root(residual,[.36,math.log(1.45)],tol=2e-9)
    assert solved.success and np.linalg.norm(residual(solved.x))<3e-9
    theta3,log_ratio=solved.x;ratio3=math.exp(log_ratio)
    alpha3=math.pi-math.acos(.75)-math.acos(.25)
    assert abs(theta3-math.asin(alpha3/math.pi))<3e-9
    assert abs(ratio3-math.sqrt(15/7))<3e-9
    _,_,ca3,cb3=cone_bvp(theta3,ratio3,1.)
    TA3=3*math.cos(theta3);TB3=math.cos(theta3)
    guide3=[]
    for c,tail3 in [(ca3,TA3),(cb3,TB3)]:
        azimuth=math.sqrt(1-c*c)
        net_without_guide=np.array([(TA3+TB3)*(-c)+tail3,
                                    (TA3-TB3)*azimuth,0.])
        guide_force=np.array([0.,-(TA3-TB3)*azimuth,0.])
        assert np.linalg.norm(net_without_guide+guide_force)<2e-9
        assert abs(net_without_guide[1])>.1
        guide3.append(dict(guide_force_per_mg=guide_force.tolist(),
            force_without_guide_per_mg=net_without_guide.tolist(),
            net_with_guide_per_mg=(net_without_guide+guide_force).tolist()))
    def T_BVP(t):
        return .2*9.8*math.cos(t)/(2*cone_bvp(t)[2])
    threshold=brentq(lambda t:T_BVP(t)-2.,.2,.4,xtol=2e-12)
    assert abs(threshold-.3137879435529221)<3e-9
    monotone=[(t,T_BVP(t)) for t in [.08,.15,.25,.4,.65,.9,1.2]]
    assert all(v[1]>w[1] for v,w in zip(monotone,monotone[1:]))
    assert T_BVP(math.radians(18))<2<T_BVP(math.radians(17.9))
    bound_sources={'scripts/verify_question_03.py':sha(Path(__file__)),
        'build/question-03-条件确认.json':sha(confirmation)}
    if not args.complete:
        bound_sources['drafts/question-03-核验备忘.md']=sha(ROOT/'drafts/question-03-核验备忘.md')
    figures={};projected_geometry=None
    if args.complete:
        source=ROOT/'drafts/question-03.md';text=source.read_text()
        assert '<!-- question-complete -->' in text
        assert text.count('\n## ')==9 and '题干修订' in text
        assert '导槽能够提供环向约束力' in text
        tex=ROOT/'figures/题03_图稿源文件.tex';assert tex.exists()
        bound_sources['drafts/question-03.md']=sha(source)
        bound_sources['figures/题03_图稿源文件.tex']=sha(tex)
        for name in ['question-03','unfold-03','forces-03','rings-03','asymmetric-03']:
            path=ROOT/f'figures/{name}.pdf';assert path.exists();figures[name]=sha(path)
        program=ROOT/'scripts/check_projected_question_03.py'
        projected_geometry=json.loads(subprocess.check_output(
            ['python3',str(program)],text=True))
        assert projected_geometry['passed']
        bound_sources['scripts/check_projected_question_03.py']=sha(program)
    result=dict(question=3,verified_math=True,document_complete=args.complete,
        set_accepted=False,model_condition_resolved=True,
        scope='cone mechanics with user-confirmed contact; PDF visual review is separate',
        contact_model=dict(sin_theta=1/3,theta=math.asin(1/3),
            theta_degrees=math.degrees(math.asin(1/3)),
            first_loop_T='mg*cos(theta)/(2*sin(pi*sin(theta)/2))',
            crossed_ropes_T_per_mg=2*math.sqrt(2)/3,
            mass_normal_per_mg=1/3,scale_equilibrium='neutral',
            unrestricted_azimuth_equilibrium='unstable'),
        hanging_mass_check=dict(free_static_tail_T_per_mg=1,
            printed_handwritten_tail_T_per_mg=2*math.sqrt(2)/3,
            incompatible_without_surface_contact=True,
            direct_vertical_tail_penetrates_solid_cone=True,
            formal_direct_vertical_ring_sin_theta=formal_s,
            formal_direct_vertical_ring_theta_degrees=math.degrees(math.asin(formal_s)),
            formal_alternative_not_a_realized_topology=True,
            base_edge_routing_requires_additional_description=True),
        cone_geodesic_BVPs=geodesics,space_contact_checks=normal_checks,
        first_loop_vector_force_checks=force_checks,
        contact_critical_angle_from_BVP=theta_bvp,
        virtual_work_BVP_checks=virtual,unequal_height_endpoint_checks=unequal,
        azimuth_stability_checks=stability,
        solved_variants=dict(
            first_loop_numerical=dict(x=x1,arc_BVP_length=d1,
                midpoint_radius=midpoint,height_rise=dz1,T=T1),
            different_rope_lengths=variant2,
            unequal_masses_with_azimuth_guides=dict(theta=float(theta3),
                ratio=float(ratio3),T_A_per_mg=TA3,T_B_per_mg=TB3,
                guide_force_checks=guide3),
            tension_limit=dict(root_theta=threshold,
                root_degrees=math.degrees(threshold),T_from_BVP=T_BVP(threshold),
                monotonic_samples=monotone)),
        projected_vector_geometry=projected_geometry,
        source_sha256=bound_sources,figures_sha256=figures,
        originals_sha256={name:sha(ROOT.parent/name) for name in ['试卷.pdf','答案.pdf']})
    report=ROOT/('build/verification-q03.json' if args.complete else 'build/verification-q03-preliminary.json')
    report.write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['question','verified_math','document_complete',
        'model_condition_resolved','contact_critical_angle_from_BVP']},ensure_ascii=False))
    print('BVP lengths/3D pressures/full forces:',len(geodesics),len(normal_checks),len(force_checks))
    print('Independent energy/unequal-endpoint/stability checks:',len(virtual),len(unequal),len(stability))

if __name__=='__main__':main()
