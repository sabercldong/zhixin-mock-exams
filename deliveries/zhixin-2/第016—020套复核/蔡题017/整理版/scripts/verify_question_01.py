"""Set 017 question 1: symbolic conics, independent Newton ODE and radial quadrature."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    d,tau=sp.symbols('d tau',positive=True)
    aq=-(1+tau**2)/(4*d);bq=tau
    xv=-bq/(2*aq);yv=-bq*bq/(4*aq);par=1/(4*aq)
    xf=xv;yf=yv+par;directrix=yv-par
    assert sp.factor(xf*xf+yf*yf-d*d)==0
    assert sp.factor(directrix-d)==0
    x,y=sp.symbols('x y',real=True)
    poly=x*x*tau*tau/(4*d)-x*tau+y+x*x/(4*d)
    disc=sp.discriminant(poly,tau)
    assert sp.factor(disc-x*x*(1-y/d-x*x/(4*d*d)))==0
    u,R=sp.symbols('u R',positive=True)
    a=R/(2-u);D=R*u/(2-u);S=4*a-R
    assert sp.simplify(D-(2*a-R))==0
    assert sp.simplify(S-(R+2*D))==0
    b2=sp.simplify((S*S-R*R)/4)
    assert sp.simplify(b2-2*R*R*u/(2-u)**2)==0
    ct,st=sp.symbols('ct st',real=True)
    ecc=sp.Matrix([u*ct*ct-1,-u*ct*st])
    F=-2*a*ecc
    focus_distance_squared=sp.expand((F-sp.Matrix([R,0])).dot(F-sp.Matrix([R,0])))
    assert sp.factor((focus_distance_squared-D*D).subs(st**2,1-ct**2))==0
    e2=sp.expand(ecc.dot(ecc)).subs(st**2,1-ct**2)
    assert sp.factor(e2-(1+u*(u-2)*ct**2))==0
    # Independent parabolic/hyperbolic coverage proof: angular integral grows with h.
    h,s,E,mu=sp.symbols('h s E mu',positive=True)
    integrand=h/(s*s*sp.sqrt(2*E+2*mu/s-h*h/s**2))
    derivative=sp.diff(integrand,h)
    target=(2*E+2*mu/s)/(s*s*(2*E+2*mu/s-h*h/s**2)**sp.Rational(3,2))
    assert sp.simplify(derivative-target)==0
    def rhs(time,z):
        radius=math.hypot(z[0],z[1])
        return [z[2],z[3],-z[0]/radius**3,-z[1]/radius**3]
    def hit_ground(time,z):return math.hypot(z[0],z[1])-1
    hit_ground.direction=-1;hit_ground.terminal=True
    def solve_at_angle(speed2,angle,target_phi):
        v=math.sqrt(speed2)
        def hit_angle(time,z):
            return z[1]*math.cos(target_phi)-z[0]*math.sin(target_phi)
        hit_angle.direction=1;hit_angle.terminal=True
        max_time=2*math.pi/(2-speed2)**1.5 if speed2<2 else 2e4
        events=[hit_angle,hit_ground] if speed2<2 and angle>1e-9 else [hit_angle]
        sol=solve_ivp(rhs,(0,max_time),[1,0,v*math.sin(angle),v*math.cos(angle)],
                      method='DOP853',rtol=3e-12,atol=3e-13,events=events,max_step=.15)
        assert sol.success
        assert len(sol.t_events[0])==1,('target_not_reached',speed2,angle,target_phi)
        zz=sol.y_events[0][0]
        return math.hypot(zz[0],zz[1]),sol
    bound_rows=[]
    for uu in [.05,.5,1.,1.25,1.75,1.95]:
        ss=(2+uu)/(2-uu)
        for phi in [.05,.2,.6,1.2,2.,math.pi]:
            rb=(ss*ss-1)/(2*(ss-math.cos(phi)))
            if rb<1+1e-9:continue
            for fraction in [.25,.7,1.]:
                rr=1+fraction*(rb-1)
                qa=1-math.cos(phi)
                qb=-uu*math.sin(phi)
                qc=qa+uu*math.cos(phi)-uu/rr
                discriminant=qb*qb-4*qa*qc
                assert discriminant>-2e-12
                if fraction==1:
                    # The exact envelope has a double launch-angle root. Avoid
                    # amplifying round-off by taking sqrt of a residual ~1e-16.
                    assert abs(discriminant)<2e-12
                    tangent=-qb/(2*qa)
                else:
                    tangent=(-qb+math.sqrt(max(0,discriminant)))/(2*qa)
                angle=math.atan(tangent)
                actual,sol=solve_at_angle(uu,angle,phi)
                error=abs(actual/rr-1)
                assert error<3e-8,(uu,phi,rr,error)
                radii=np.hypot(sol.y[0],sol.y[1])
                distances=np.hypot(sol.y[0]-1,sol.y[1])
                ee=.5*(sol.y[2]**2+sol.y[3]**2)-1/radii
                angular=sol.y[0]*sol.y[3]-sol.y[1]*sol.y[2]
                assert np.max(np.abs(ee-(uu/2-1)))<2e-10
                assert np.max(np.abs(angular-angular[0]))<2e-10
                assert min(radii)>1-2e-10
                assert np.max(radii+distances-ss)<3e-8
                if fraction==1:
                    A=np.array([1.,0]);P=np.array([rr*math.cos(phi),rr*math.sin(phi)])
                    focus=A+uu/(2-uu)*(P-A)/np.linalg.norm(P-A)
                    ev=np.array([uu*math.cos(angle)**2-1,-uu*math.sin(angle)*math.cos(angle)])
                    focus_error=np.linalg.norm(focus+2/(2-uu)*ev)
                    assert focus_error<2e-7,(uu,phi,rr,discriminant,focus_error,focus,ev,angle)
                bound_rows.append(dict(u=uu,phi=phi,r=rr,envelope_radius=rb,
                                       fraction=fraction,launch_angle=angle,
                                       ode_radius_relative_error=error))
    unbound_rows=[]
    for uu in [2.,2.25,3.,6.]:
        asymptote=math.acos(-1/(uu-1))
        for fraction_angle in [.15,.5,.85]:
            phi=asymptote*fraction_angle
            rtan=uu/(1+(uu-1)*math.cos(phi))
            for scale in [1.,1.5,4.]:
                rr=rtan*scale
                qa=1-math.cos(phi);qb=-uu*math.sin(phi)
                qc=qa+uu*math.cos(phi)-uu/rr
                discriminant=qb*qb-4*qa*qc
                tangent=(-qb-math.sqrt(discriminant))/(2*qa)
                assert tangent>-3e-14
                angle=math.atan(max(0,tangent))
                actual,sol=solve_at_angle(uu,angle,phi)
                error=abs(actual/rr-1)
                assert error<3e-8
                radii=np.hypot(sol.y[0],sol.y[1])
                assert min(radii)>1-2e-10
                assert np.min(np.diff(radii))>-1e-10
                unbound_rows.append(dict(u=uu,phi=phi,r=rr,tangent_boundary=rtan,
                                         launch_angle=angle,ode_radius_relative_error=error))
            # Quadrature uses conserved energy and angular momentum, not conic interpolation.
            def angular_integrand(rad):
                val=uu-2+2/rad-uu/(rad*rad)
                return math.sqrt(uu)/(rad*rad*math.sqrt(val))
            integral,error=quad(angular_integrand,1,rtan,epsabs=2e-10,epsrel=2e-10)
            assert abs(integral-phi)<5e-9,(uu,phi,integral)
    # Flat-Earth limit at fixed launch speed: R grows, surface g stays one.
    limits=[]
    for big_R in [1e3,1e4,1e5]:
        v2=2.;uu=v2/big_R
        SS=big_R*(2+uu)/(2-uu)
        max_error=0
        for xx in [0.,.4,.8,1.2,1.8]:
            aa=SS/2;bb2=(SS*SS-big_R*big_R)/4
            yy=aa*math.sqrt(1-xx*xx/bb2)-big_R/2
            planar=1-xx*xx/4
            max_error=max(max_error,abs(yy-planar))
        limits.append(dict(R=big_R,max_height_error=max_error))
    assert limits[-1]['max_height_error']<2e-5
    variants=[]
    for uu in [.5,1.,1.5]:
        ss=(2+uu)/(2-uu);DD=uu/(2-uu)
        if uu<1:
            phi_max=math.acos(max(-1,min(1,(2*ss-ss*ss+1)/2)))
        else:phi_max=math.pi
        variants.append(dict(u=uu,radial_height_over_R=DD,envelope_S_over_R=ss,
                             surface_angular_range=phi_max))
    # Ground footprint: sin(phi/2)<=u/(2-u), for 0<u<1.
    for row in variants:
        uu=row['u']
        if uu<1:
            predicted=2*math.asin(uu/(2-uu))
            assert abs(predicted-row['surface_angular_range'])<1e-12
    # Verify worked numerical examples, including both launch roots.
    worked={}
    for sign in [-1,1]:
        tangent=(5+sign*math.sqrt(6))/3
        theta=math.atan(tangent)
        time=24/(20*math.cos(theta))
        height=20*math.sin(theta)*time-5*time*time
        assert abs(height-8)<2e-13
        worked['uniform_'+str(sign)]=dict(tan_theta=tangent,angle_deg=math.degrees(theta),time=time,height=height)
    uu=.5;phi=.2;rr=1.1
    qa=1-math.cos(phi);qb=-uu*math.sin(phi);qc=qa+uu*math.cos(phi)-uu/rr
    disc=qb*qb-4*qa*qc
    example=[]
    for sign in [-1,1]:
        tangent=(-qb+sign*math.sqrt(disc))/(2*qa)
        actual,sol=solve_at_angle(uu,math.atan(tangent),phi)
        assert abs(actual/rr-1)<3e-9
        example.append(dict(tan_theta=tangent,angle_deg=math.degrees(math.atan(tangent)),ode_radius=actual))
    worked['bound_numeric_example']=dict(coefficients=[qa,qb,qc],discriminant=disc,roots=example)
    for uu,phi,rr,tangent in [(1.5,math.pi,1,1/math.sqrt(2)),(3,math.pi/2,4,(3-2*math.sqrt(2))/2)]:
        actual,sol=solve_at_angle(uu,math.atan(tangent),phi)
        assert abs(actual/rr-1)<3e-8
        assert min(np.hypot(sol.y[0],sol.y[1]))>1-2e-10
    # Independently test both positive roots in the hyperbolic worked example.
    # Integrate Newton's equation up to r=1000, rather than sampling the conic.
    hyperbolic_roots=[]
    for label,tangent in [('minus',(3-2*math.sqrt(2))/2),('plus',(3+2*math.sqrt(2))/2)]:
        angle=math.atan(tangent)
        kk=3/(1+tangent*tangent);cc=3*tangent/(1+tangent*tangent)
        ee=math.hypot(kk-1,cc)
        delta=math.atan2(-cc,kk-1)
        phi_infinity=delta+math.acos(-1/ee)
        assert phi_infinity>0
        def reach_large_radius(time,z):return math.hypot(z[0],z[1])-1000
        reach_large_radius.direction=1;reach_large_radius.terminal=True
        sol=solve_ivp(rhs,(0,2000),[1,0,math.sqrt(3)*math.sin(angle),math.sqrt(3)*math.cos(angle)],
                      method='DOP853',rtol=3e-12,atol=3e-13,events=reach_large_radius,max_step=1)
        assert sol.success and len(sol.t_events[0])==1
        zz=sol.y_events[0][0];actual_phi=math.atan2(zz[1],zz[0])
        assert 0<phi_infinity-actual_phi<.005
        physical_target_root=phi_infinity>math.pi/2
        assert physical_target_root==(label=='minus')
        radii=np.hypot(sol.y[0],sol.y[1])
        assert min(radii)>1-2e-10
        assert np.min(np.diff(radii))>-1e-10
        energy=.5*(sol.y[2]**2+sol.y[3]**2)-1/radii
        angular=sol.y[0]*sol.y[3]-sol.y[1]*sol.y[2]
        assert np.max(np.abs(energy-.5))<2e-10
        assert np.max(np.abs(angular-angular[0]))<2e-10
        hyperbolic_roots.append(dict(label=label,tan_theta=tangent,k=kk,c0=cc,e=ee,
                                    asymptote_deg=math.degrees(phi_infinity),
                                    independent_ode_angle_at_1000R_deg=math.degrees(actual_phi),
                                    target_90deg_reachable=physical_target_root))
    worked['hyperbolic_root_selection']=hyperbolic_roots
    report=dict(question=1,verified_math=True,document_complete=False,set_accepted=False,
                scope='question 1 independent physics verification; not PDF acceptance',
                bound_reachable_samples=bound_rows,unbound_reachable_samples=unbound_rows,
                flat_earth_limits=limits,variant_values=variants,worked_examples=worked,
                uniform_focus_distance='v0^2/(2g)',uniform_directrix='y=v0^2/(2g)',
                elliptic_second_focus_distance='R*u/(2-u)',
                elliptic_reachable='r>=R and |AP|+r<=R*(2+u)/(2-u)',
                nonreturning_coverage='u>=2: r>=R*u/[1+(u-1)*cos(phi)] and denominator>0',
                hyperbolic_focus_distance='R*u/(u-2); u=2 has no second finite focus',
                originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')},
                source_sha256={'scripts/verify_question_01.py':sha(Path(__file__))})
    source=ROOT/'drafts/question-01.md'
    if source.exists():
        report['document_complete']='<!-- question-complete -->' in source.read_text()
        report['source_sha256']['drafts/question-01.md']=sha(source)
    figures=ROOT/'figures'
    if (figures/'question-01.pdf').exists():
        report['figures_sha256']={p.stem:sha(p) for p in figures.glob('*-01.pdf')}
        report['source_sha256']['figures/\u989801_\u56fe\u7a3f\u6e90\u6587\u4ef6.tex']=sha(figures/'\u989801_\u56fe\u7a3f\u6e90\u6587\u4ef6.tex')
    (ROOT/'build').mkdir(exist_ok=True)
    target=ROOT/('build/verification-q01.json' if report['document_complete'] else 'build/verification-q01-preliminary.json')
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['bound_reachable_samples','unbound_reachable_samples']},ensure_ascii=False))
    print('bound_samples',len(bound_rows),'unbound_samples',len(unbound_rows),flush=True)
if __name__=='__main__':main()
