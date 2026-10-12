"""017 Q4: recover stiffness and periods from the actual two half-springs.

Preliminary independent calculation only until question text and figures exist.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import root
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def force(l0,extension,k,x,y):
    a=(l0+extension)/2;b=l0/2
    result=np.zeros(2)
    for anchor in [-a,a]:
        vector=np.array([anchor-x,-y])
        length=float(np.linalg.norm(vector))
        result+=2*k*(length-b)*vector/length
    return result
def main():
    L,l0,k,m,x,y=sp.symbols('L l0 k m x y',positive=True)
    left=sp.sqrt((L/2+x)**2+y**2)
    right=sp.sqrt((L/2-x)**2+y**2)
    potential=k*((left-l0/2)**2+(right-l0/2)**2)
    hessian=sp.simplify(sp.hessian(potential,(x,y)).subs({x:0,y:0}))
    assert sp.simplify(hessian[0,0]-4*k)==0
    assert sp.simplify(hessian[1,1]-4*k*(L-l0)/L)==0
    assert hessian[0,1]==hessian[1,0]==0
    transverse=sp.simplify(potential.subs(x,0))
    assert sp.simplify(transverse-k*(sp.sqrt(L**2+4*y**2)-l0)**2/2)==0
    series=sp.series(transverse,y,0,8).removeO().expand()
    assert sp.simplify(series-k*(L-l0)**2/2-2*k*(L-l0)*y**2/L
                       -2*k*l0*y**4/L**3+4*k*l0*y**6/L**5)==0
    stiffness_samples=[];longitudinal=[];transverse_samples=[]
    cases=[(.6,.04,.8*math.pi**2,.05),(.6,.075,.8*math.pi**2,.05),
           (.84,.024,6.,.08),(.4,.2,3.,.12),(.8,.004,12.,.06)]
    for natural,extension,stiffness,mass in cases:
        total=natural+extension;h=total*1e-6
        probes=[(force(natural,extension,stiffness,h,0)-force(natural,extension,stiffness,-h,0))/(2*h),
                (force(natural,extension,stiffness,0,h)-force(natural,extension,stiffness,0,-h))/(2*h)]
        jacobian=np.column_stack(probes)
        expected=np.diag([-4*stiffness,-4*stiffness*extension/total])
        assert np.max(abs(jacobian-expected))/(4*stiffness)<2e-9
        stiffness_samples.append(dict(l0=natural,extension=extension,
            directly_recovered_stiffness=(-np.diag(jacobian)).tolist(),off_diagonal=[float(jacobian[0,1]),float(jacobian[1,0])]))
        amplitude=min(extension/10,total/100)
        def ode(t,state):
            acceleration=force(natural,extension,stiffness,state[0],state[1])/mass
            return [state[2],state[3],acceleration[0],acceleration[1]]
        def cross_x(t,state):return state[0]
        cross_x.direction=-1;cross_x.terminal=True
        Tlong=2*math.pi*math.sqrt(mass/(4*stiffness))
        sol=solve_ivp(ode,[0,Tlong],[amplitude,0,0,0],rtol=2e-11,atol=1e-13,
                      events=cross_x,max_step=Tlong/120)
        recovered=4*sol.t_events[0][0]
        assert abs(recovered/Tlong-1)<2e-10
        longitudinal.append(dict(l0=natural,extension=extension,
                                 T_from_two_vector_forces=recovered,T_formula=Tlong))
        for fraction in [1e-4,1e-3,.01,.03]:
            A=total*fraction
            def cross_y(t,state):return state[1]
            cross_y.direction=-1;cross_y.terminal=True
            Tlinear=2*math.pi*math.sqrt(mass*total/(4*stiffness*extension))
            sol=solve_ivp(ode,[0,Tlinear],[0,A,0,0],rtol=2e-11,atol=1e-13,
                          events=cross_y,max_step=Tlinear/160)
            Tode=4*sol.t_events[0][0]
            D_A=math.sqrt(total**2+4*A*A)
            integrand=lambda angle:math.sqrt(
                (D_A+math.sqrt(total**2+4*A*A*math.sin(angle)**2))/
                (D_A+math.sqrt(total**2+4*A*A*math.sin(angle)**2)-2*natural))
            Tenergy=2*math.sqrt(mass/stiffness)*quad(integrand,0,math.pi/2,epsabs=2e-11)[0]
            assert abs(Tode/Tenergy-1)<2e-8
            assert max(abs(sol.y[0]))<1e-10
            assert Tenergy<Tlinear
            correction=3*natural*A*A/(4*extension*total**2)
            if fraction<=1e-3:
                assert abs(Tenergy/Tlinear-(1-correction))<max(2e-11,4*correction**2)
            transverse_samples.append(dict(l0=natural,extension=extension,amplitude=A,
                T_from_two_vector_forces=Tode,T_from_exact_energy_quadrature=Tenergy,
                T_linear=Tlinear,cubic_to_linear_force_at_amplitude=2*natural*A*A/(extension*total**2),
                leading_relative_period_decrease=correction))
    n1,n2,d=4.,3.,.035
    recovered_l0=d*(n1*n1-1)*(n2*n2-1)/(n1*n1-n2*n2)
    recovered_d1=d*(n2*n2-1)/(n1*n1-n2*n2)
    recovered_d2=recovered_d1+d
    assert abs(recovered_l0-.6)<1e-15
    assert abs(recovered_d1-.04)<1e-15 and abs(recovered_d2-.075)<1e-15
    # Inverse roots use actual vector-force probes, not the written inverse formula.
    inverse_rows=[]
    for first,second,increment in [(4,3,.035),(6,5,.011),(3,2,.02),
                                   (2.5,1.8,.045),(8,4,.01),(1.5,1.2,.07)]:
        def measured_squared(natural,extension):
            total=natural+extension;h=total*1e-7
            long_stiff=-force(natural,extension,1.,h,0)[0]/h
            trans_stiff=-force(natural,extension,1.,0,h)[1]/h
            return long_stiff/trans_stiff
        def residual(logs):
            natural,initial=np.exp(logs)
            return [measured_squared(natural,initial)/first**2-1,
                    measured_squared(natural,initial+increment)/second**2-1]
        solution=root(residual,np.log([.5,.03]),tol=1e-9)
        assert max(abs(np.array(residual(solution.x))))<2e-8
        natural,initial=np.exp(solution.x)
        expected_natural=increment*(first**2-1)*(second**2-1)/(first**2-second**2)
        expected_initial=increment*(second**2-1)/(first**2-second**2)
        assert abs(natural/expected_natural-1)<2e-8
        assert abs(initial/expected_initial-1)<2e-8
        inverse_rows.append(dict(n1=first,n2=second,increment=increment,
            l0_from_vector_force_root=float(natural),extension1_from_root=float(initial),
            formula_l0=expected_natural,formula_extension1=expected_initial))
    # Exact potential gradients independently match forces away from equilibrium.
    gradient_rows=[]
    for xx in [-.005,-.001,.002,.006]:
        for yy in [-.025,-.01,.008,.018]:
            natural,extension,stiffness=.6,.04,5.
            def energy(xvalue,yvalue):
                a=(natural+extension)/2;b=natural/2
                lengths=[math.hypot(a+xvalue,yvalue),math.hypot(a-xvalue,yvalue)]
                return stiffness*sum((s-b)**2 for s in lengths)
            h=2e-6
            gradient=np.array([(energy(xx+h,yy)-energy(xx-h,yy))/(2*h),
                               (energy(xx,yy+h)-energy(xx,yy-h))/(2*h)])
            actual=force(natural,extension,stiffness,xx,yy)
            assert np.linalg.norm(gradient+actual)<2e-9
            gradient_rows.append(dict(x=xx,y=yy,gradient_force_residual=float(np.linalg.norm(gradient+actual))))
    # Zero prestretch is quartic, not a harmonic oscillator of finite frequency.
    integral=quad(lambda u:1/math.sqrt(1-u**4),0,1,epsabs=1e-10)[0]
    assert abs(integral-1.31102877714606)<1e-10
    zero_rows=[]
    natural,stiffness,mass=.6,8.,.05
    for A in [.0006,.0012,.003]:
        def acceleration(t,state):
            return [state[1],force(natural,0,stiffness,0,state[0])[1]/mass]
        def zero(t,state):return state[0]
        zero.direction=-1;zero.terminal=True
        asymptotic=2*natural*math.sqrt(mass/stiffness)*integral/A
        sol=solve_ivp(acceleration,[0,asymptotic],[A,0],rtol=1e-10,atol=1e-13,
                      events=zero,max_step=asymptotic/180)
        measured=4*sol.t_events[0][0]
        assert abs(measured/asymptotic-1)<5*(A/natural)**2
        zero_rows.append(dict(amplitude=A,T_exact_ODE=measured,T_quartic_asymptotic=asymptotic))
    figures=['question-04','halves-04','longitudinal-04','transverse-04']
    sources=['scripts/verify_question_04.py','drafts/question-04.md',
             'figures/题04_图稿源文件.tex']
    complete=all((ROOT/path).exists() for path in sources) and all(
        (ROOT/f'figures/{name}.{extension}').exists()
        for name in figures for extension in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-04.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察',
                 '易错点','课堂讲解建议','变式训练']
        assert [s.split('、',1)[1] for s in text.splitlines() if s.startswith('## ')]==modules
        assert text.count('<!-- question-complete -->')==1
        assert all(text.count(f'../figures/{name}.png')==1 for name in figures)
    stiffness_dimension=np.array([1,0,-2])
    mass_dimension=np.array([1,0,0])
    assert np.array_equal((mass_dimension-stiffness_dimension)/2,[0,0,1])
    v1=dict(k=.8*math.pi**2,half_k=1.6*math.pi**2,
            tension1=.8*math.pi**2*.04,tension2=.8*math.pi**2*.075,
            Tlong=.25,Ttrans1=1.,Ttrans2=.75)
    assert abs(longitudinal[0]['T_from_two_vector_forces']-.25)<1e-10
    assert abs(longitudinal[1]['T_from_two_vector_forces']-.25)<1e-10
    assert abs(v1['tension1']-.3158273408348595)<1e-14
    assert abs(v1['tension2']-.5921762640653615)<1e-14
    report=dict(question=4,verified_math=True,document_complete=complete,set_accepted=False,
        scope='independent vector forces, energy and complete question source; not visual or whole-set acceptance' if complete else 'preliminary independent calculation',
        recovered_original=dict(l0=recovered_l0,extension1=recovered_d1,extension2=recovered_d2),
        exact_potential=str(potential),equilibrium_hessian=str(hessian),transverse_series=str(series),
        vector_force_stiffness=stiffness_samples,longitudinal_ODE=longitudinal,
        transverse_ODE_and_quadrature=transverse_samples,inverse_vector_force_roots=inverse_rows,
        exact_energy_gradient_checks=gradient_rows,
        zero_prestretch_quartic=dict(integral=integral,samples=zero_rows),
        solved_variants=dict(absolute_period_parameters=v1,
            inverse_measurement_case=inverse_rows[1],
            finite_amplitude_case=transverse_samples[2],
            zero_prestretch_case=zero_rows[2]),
        dimensional_checks=dict(order=['mass','length','time'],
            stiffness=stiffness_dimension.tolist(),period=[0,0,1],passed=True),
        assumptions=['uniform symmetric massless Hookean spring, half-spring stiffness 2k',
                     'frictionless horizontal support, no damping, positive prestretch for harmonic transverse mode',
                     'small amplitude around a fixed positive prestretch; no assumption extension much smaller than natural length',
                     'longitudinal amplitude less than extension/2 keeps both flexible halves in tension'],
        handwritten_notes=['the energy expansion and 60 cm / 4 cm / 7.5 cm conclusions are correct',
                           'supplement half-spring stiffness, prestretch contribution to quadratic energy, geometric signs and expansion remainder',
                           'finite amplitude conditions become nonuniform as prestretch tends to zero'],
        source_sha256={path:sha(ROOT/path) for path in sources if (ROOT/path).exists()},
        figures_sha256={name:sha(ROOT/f'figures/{name}.pdf') for name in figures} if complete else {},
        originals_sha256={path.name:sha(path) for path in ROOT.parent.glob('*.pdf')})
    record='verification-q04.json' if complete else 'verification-q04-preliminary.json'
    (ROOT/'build'/record).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,
        stiffness_cases=len(stiffness_samples),longitudinal_ODE=len(longitudinal),
        transverse_ODE_and_quadrature=len(transverse_samples),
        inverse_roots=len(inverse_rows),energy_gradient_samples=len(gradient_rows),
        zero_prestretch_ODE=len(zero_rows)),ensure_ascii=False))
if __name__=='__main__':main()
