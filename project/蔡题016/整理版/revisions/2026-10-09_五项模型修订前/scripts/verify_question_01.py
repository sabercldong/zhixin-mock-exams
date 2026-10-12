"""016 Q1: direct kinematics, constrained paths and exact stationary root.

The second part lets the runner choose an escape direction. A separately
specified downstream escape is checked as a different model, not silently
identified with the handwritten 0.5*v0 conclusion.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.optimize import minimize,brentq
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def drift(t):return t-.5*math.sqrt(t*t-4)
def cost(t):return t+2*math.hypot(2,drift(t))
def main():
    c,t=sp.symbols('c t',real=True)
    q=8-4*c-3*c*c
    F=2*(1+sp.sqrt(q))/sp.sqrt(1-c*c)
    unsquared=c*sp.sqrt(q)+5*c-2*c*c-2
    derivative=2*unsquared/(sp.sqrt(q)*(1-c*c)**sp.Rational(3,2))
    assert sp.simplify(sp.diff(F,c)-derivative)==0
    polynomial=sp.expand((2*c*c-5*c+2)**2-c*c*q)
    assert sp.factor(polynomial)==(c-1)*(7*c-2)*(c*c-c+2)
    cs=sp.Rational(2,7)
    assert sp.simplify(unsquared.subs(c,cs))==0
    assert sp.simplify(F.subs(c,cs)-10*sp.sqrt(5)/3)==0
    assert 2*1**2-5*1+2<0  # c=1 is an extraneous squared boundary root.
    d=t-sp.sqrt(t*t-4)/2
    assert sp.simplify(sp.diff(d,t,2)-2/(t*t-4)**sp.Rational(3,2))==0
    assert sp.limit(d/t,t,sp.oo)==sp.Rational(1,2)
    ts=float(14*sp.sqrt(5)/15)
    displacement=float(4*sp.sqrt(5)/5)
    optimum=float(10*sp.sqrt(5)/3)
    exact=dict(cos_alpha='2/7',sin_alpha='3*sqrt(5)/7',
        alpha_degrees=float(sp.acos(cs)*180/sp.pi),
        water_time_coefficient=ts,total_time_coefficient=optimum,
        drift_coefficient=displacement,entry_x_coefficient=-displacement/2,
        exit_x_coefficient=displacement/2,
        each_land_length_coefficient=float(3*sp.sqrt(5)/5),
        each_land_time_coefficient=float(6*sp.sqrt(5)/5))
    # Optimization uses three independent path variables, not the reduced formula.
    # a,b are bank coordinates; s is the swimming duration, in units h/v0.
    # The equality constraint uses actual relative velocity components.
    rows=[]
    starts=[(-.9,.9,2.1),(-2.,1.,3.),(0.,2.,2.1),(-5.,-2.,4.),
            (1.,5.,5.),(-1.,2.,2.5),(2.,8.,8.),(-4.,3.,6.)]
    for initial in starts:
        def objective(z):
            a,b,s=z
            return s+2*math.hypot(1,a)+2*math.hypot(1,b)
        def constraint(z):
            a,b,s=z
            return ((b-a)/s-1)**2+(1/s)**2-.25
        solution=minimize(objective,initial,method='SLSQP',
            constraints=[{'type':'eq','fun':constraint}],
            bounds=[(-30,30),(-30,30),(2,30)],
            options={'ftol':1e-12,'maxiter':1500})
        assert solution.success,solution.message
        assert abs(constraint(solution.x))<2e-11
        assert abs(solution.fun-optimum)<3e-9
        assert np.linalg.norm(solution.x-np.array([-displacement/2,displacement/2,ts]))<2e-5
        rows.append(dict(initial=initial,bank_coordinates_and_duration=solution.x.tolist(),
                         time=float(solution.fun),relative_speed_residual=constraint(solution.x)))
    one=minimize(lambda z:cost(float(z[0])),[3.],bounds=[(2.000000001,40)],
                 method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-12})
    assert abs(one.fun-optimum)<2e-12
    assert abs(float(one.x[0])-ts)<2e-7
    minimum_drift_result=minimize(lambda z:drift(float(z[0])),[3.],bounds=[(2.000000001,40)],
                           method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-12})
    assert abs(minimum_drift_result.fun-math.sqrt(3))<2e-12
    assert abs(float(minimum_drift_result.x[0])-4/math.sqrt(3))<2e-7
    assert cost(float(minimum_drift_result.x[0]))>optimum
    # Dimensional kinematic reconstruction at unrelated dimensional scales.
    reconstructions=[]
    for height,current in [(1.,1.),(90.,3.),(.007,2.4),(1500.,.07),(7.5,17.)]:
        speed=current/2
        entry=np.array([-displacement*height/2,0.])
        exit=np.array([displacement*height/2,height])
        start=np.array([0.,-height]);target=np.array([0.,2*height])
        first_time=np.linalg.norm(entry-start)/speed
        middle_time=ts*height/current
        last_time=np.linalg.norm(target-exit)/speed
        land1=(entry-start)/first_time
        land2=(target-exit)/last_time
        water=(exit-entry)/middle_time-np.array([current,0.])
        assert abs(np.linalg.norm(water)/speed-1)<1e-13
        assert abs(np.linalg.norm(land1)/speed-1)<1e-13
        assert abs(np.linalg.norm(land2)/speed-1)<1e-13
        assert np.linalg.norm(start+land1*first_time+
                 (water+np.array([current,0.]))*middle_time+land2*last_time-target)<height*2e-13
        total=first_time+middle_time+last_time
        assert abs(total/(height/current)-optimum)<2e-13
        reconstructions.append(dict(h=height,v0=current,total_time=total,
            phase_times=[first_time,middle_time,last_time],
            relative_water_velocity=water.tolist(),land_velocities=[land1.tolist(),land2.tolist()]))
    # Unequal inland distances: optimize all three path variables afresh.
    unequal=[]
    for near,far in [(.5,1.5),(.1,1.9),(1.6,.4),(1.,1.)]:
        def objective(z):return z[2]+2*math.hypot(near,z[0])+2*math.hypot(far,z[1])
        def constraint(z):return ((z[1]-z[0])/z[2]-1)**2+1/z[2]**2-.25
        sol=minimize(objective,[-near*.8,far*.8,2.2],method='SLSQP',
            constraints=[{'type':'eq','fun':constraint}],bounds=[(-20,20),(-20,20),(2,20)],
            options={'ftol':1e-12,'maxiter':1000})
        assert sol.success and abs(sol.fun-optimum)<2e-10
        assert abs(sol.x[0]+near*displacement/2)<2e-6
        assert abs(sol.x[1]-far*displacement/2)<2e-6
        unequal.append(dict(near_height=near,far_height=far,bank_and_time=sol.x.tolist(),total_time=float(sol.fun)))
    # Normal escape at v2<v1: construct a full-speed straight final intercept.
    normal=[]
    for w in [0.,.1,.25,.4,.49]:
        # Near run lasts 2, water-relative perpendicular swim lasts 2.
        # Exit (2,1), pig at (0,2+w*T); solve the remaining land intercept.
        residual=lambda s:.25*s*s-4-(1+w*(4+s))**2
        upper=10.
        while residual(upper)<0:upper*=2
        last=brentq(residual,0,upper,xtol=1e-11)
        total=4+last
        final_velocity=np.array([-2.,1+w*total])/last
        assert abs(np.linalg.norm(final_velocity)-.5)<1e-12
        assert np.linalg.norm(np.array([2.,1.])+final_velocity*last-
                              np.array([0.,2+w*total]))<2e-12
        normal.append(dict(v2_over_v0=w,total_time_coefficient=total,
            final_run_time_coefficient=last,final_run_velocity=final_velocity.tolist()))
    assert abs(normal[2]['final_run_time_coefficient']-8*(1+math.sqrt(7))/3)<2e-12
    # A specified downstream escape is a different, exactly solvable countermodel.
    # Two vertical land legs each last 2; a full-speed single swim can catch
    # every 0.5<=w<1.5. Positive root of the direct relative-speed equation.
    downstream=[]
    for w in [.5,.6,.75,1.,1.25,1.4,1.49,1.499]:
        coefficient=(w-1)**2-.25
        linear=8*w*(w-1);constant=16*w*w+1
        if w==.5:swimming=-constant/linear
        else:
            swimming=(-linear-math.sqrt(linear*linear-4*coefficient*constant))/(2*coefficient)
        total=swimming+4
        relative=np.array([w*total/swimming-1,1/swimming])
        assert abs(np.linalg.norm(relative)-.5)<3e-13
        exit=np.array([(relative[0]+1)*swimming,1.])
        assert np.linalg.norm(exit+np.array([0.,.5])*2-
                              np.array([w*total,2.]))<2e-10
        downstream.append(dict(v2_over_v0=w,swimming=swimming,total_time=total,
            relative_water_velocity=relative.tolist(),catch_x=w*total))
    assert abs(downstream[0]['swimming']-2.5)<1e-15
    assert abs(downstream[0]['total_time']-6.5)<1e-15
    # Jensen/triangle lower bounds on nonconstant swimming headings and extra
    # land bends, derived from the actual component sums rather than the answer.
    rng=np.random.default_rng(1601);controlled=[]
    for count in [2,3,4,8,12,25]:
        angles=rng.uniform(.12,math.pi-.12,count)
        weights=rng.uniform(.2,1.,count);weights/=weights.sum()
        relative=.5*np.column_stack([np.cos(angles),np.sin(angles)])
        mean=weights@relative
        duration=1/mean[1]
        actual_drift=(1+mean[0])*duration
        minimum_drift=drift(duration)
        assert duration>=2-1e-13
        assert np.linalg.norm(mean)<=.5+1e-13
        assert actual_drift>=minimum_drift-1e-12
        land_displacements=np.array([[-actual_drift*.3,.8],[-actual_drift*.7,1.2]])
        actual_land=sum(np.linalg.norm(z) for z in land_displacements)
        assert actual_land>=math.hypot(actual_drift,2)-1e-12
        total=duration+2*actual_land
        assert total>=optimum-1e-12
        controlled.append(dict(pieces=count,average_relative_velocity=mean.tolist(),
            swim_duration=duration,actual_drift=actual_drift,
            minimum_drift_for_duration=minimum_drift,
            bent_land_total_length=actual_land,total_time=total))
    figure_names=['question-01','velocity-01','reflection-01','minimum-01','escape-01','downstream-01']
    sources=['scripts/verify_question_01.py','drafts/question-01.md','figures/题01_图稿源文件.tex']
    complete=all((ROOT/p).exists() for p in sources) and all(
        (ROOT/f'figures/{n}.{ext}').exists() for n in figure_names for ext in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-01.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察','易错点','课堂讲解建议','变式训练']
        assert [line.split('、',1)[1] for line in text.splitlines() if line.startswith('## ')]==modules
        assert text.count('<!-- question-complete -->')==1
        assert all(text.count(f'../figures/{n}.png')==1 for n in figure_names)
    report=dict(question=1,verified_math=True,document_complete=complete,set_accepted=False,
        scope='mathematical checks and current source existence; not PDF/visual or whole-set acceptance',
        exact_optimum=exact,polynomial=str(polynomial),factorization=str(sp.factor(polynomial)),
        original_stationary_residual=str(sp.simplify(unsquared.subs(c,cs))),
        time_optimization_three_path_variables=rows,
        independent_duration_minimum=dict(duration=float(one.x[0]),time=float(one.fun)),
        minimum_drift_contrast=dict(duration=float(minimum_drift_result.x[0]),
            drift=float(minimum_drift_result.fun),total_time=cost(float(minimum_drift_result.x[0]))),
        dimensional_path_reconstruction=reconstructions,unequal_inland_distance_optimization=unequal,
        normal_escape_constructed_intercepts=normal,downstream_escape_constructed_intercepts=downstream,
        nonconstant_heading_and_bent_land_lower_bound_checks=controlled,
        escape_model=dict(original_direction_not_fixed=True,
            chosen_direction_minimum='v1=v0/2: run perpendicularly away from the far bank',
            proof_below_threshold='finite bank crossing followed by faster land pure pursuit; closing rate at least v1-v2',
            threshold_equality='positive vertical separation cannot decrease for the normal escape',
            distinct_specified_downstream_threshold='v0+v1=3*v0/2, not v1'),
        dimensional_checks=dict(order=['length','time'],h=[1,0],v0=[1,-1],h_over_v0=[0,1],passed=True),
        handwritten_notes=['73.4 degrees and 7.45*h/v0 are rounded correct values; exact cos(alpha)=2/7 and time=10*sqrt(5)*h/(3*v0)',
            'the two equal land offsets require a minimization argument, not an unsupported symmetry assertion',
            'the 0.5*v0 escape conclusion requires freedom to choose the away-from-bank direction; it is not a downstream escape result'],
        source_sha256={p:sha(ROOT/p) for p in sources if (ROOT/p).exists()},
        figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in figure_names} if complete else {},
        originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')})
    (ROOT/'build').mkdir(exist_ok=True)
    target=ROOT/'build'/('verification-q01.json' if complete else 'verification-q01-preliminary.json')
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,exact=exact,
        independent_path_optima=len(rows),dimensional_cases=len(reconstructions),unequal_cases=len(unequal),
        normal_intercepts=len(normal),downstream_intercepts=len(downstream),
        nonconstant_control_checks=len(controlled)),ensure_ascii=False))
if __name__=='__main__':main()
