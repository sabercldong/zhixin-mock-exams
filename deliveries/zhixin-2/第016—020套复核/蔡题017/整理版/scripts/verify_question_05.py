"""017 Q5: independently integrate both electrons' Cartesian Newton equations.

This is a preliminary calculation until the nine-module text and vector figures
are present. Planar orbital/radial stability is distinct from exact phase tracking.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq,minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
J=np.array([[0.,-1.],[1.,0.]])
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def rhs_planar(Omega,C):
    def ode(time,state):
        r1=state[:2];r2=state[2:4];v1=state[4:6];v2=state[6:8]
        separation=r1-r2;distance=float(np.linalg.norm(separation))
        repel=C/2*separation/distance**3
        return np.r_[v1,v2,repel+Omega*(J@v1),-repel+Omega*(J@v2)]
    return ode
def state_circle(length,w,V=np.zeros(2)):
    return np.r_[[length/2,0],[-length/2,0],
                 V+[0,w*length/2],V-[0,w*length/2]]
def invariants(states,C,Omega):
    R=states[:2]-states[2:4];W=states[4:6]-states[6:8]
    r=np.sqrt(np.sum(R*R,axis=0))
    j=R[0]*W[1]-R[1]*W[0]-Omega*r*r/2
    E=np.sum(states[4:8]**2,axis=0)/2+C/(2*r)
    return r,j,E
def main():
    r,w,Omega,C,j=sp.symbols('r w Omega C j',positive=True)
    rr,jj=sp.symbols('rr jj',real=True)
    U=Omega**2*r**2/8+j**2/(2*r**2)+C/r
    assert sp.simplify(-sp.diff(U,r)-(-Omega**2*r/4+j**2/r**3+C/r**2))==0
    curvature=sp.diff(U,r,2)
    # Circular balance has C/r^3 = Omega*w - w^2.
    kappa2=sp.simplify(curvature.subs(j,r**2*(w-Omega/2)).subs(C,r**3*(Omega*w-w**2)))
    assert sp.simplify(kappa2-(Omega**2-Omega*w+w**2))==0
    x,v0,m,l=sp.symbols('x v0 m l',positive=True)
    rho=l/2;speed=(v0+Omega*l*((1+x)**2-1)/4)/(1+x)
    outward=m*speed**2/(rho*(1+x))+m*C/(2*l**2*(1+x)**2)-m*Omega*speed
    linear_coefficient=sp.diff(outward,x).subs(x,0)
    linear_coefficient=sp.simplify(linear_coefficient.subs(v0,w*l/2).subs(C,l**3*(Omega*w-w**2)))
    assert sp.simplify(linear_coefficient+m*l/2*kappa2)==0
    gamma=Omega-2*w;s=Omega*w-w*w
    A=sp.Matrix([[0,0,1,0],[0,0,0,1],[-3*s,0,0,-gamma],[0,0,gamma,0]])
    lam=sp.symbols('lam')
    assert sp.simplify(A.charpoly(lam).as_expr()-lam**2*(lam**2+kappa2))==0
    # Derive rotating-coordinate terms rather than merely quoting a Jacobian.
    time=sp.symbols('time',real=True)
    Q=sp.Matrix([[sp.cos(w*time),-sp.sin(w*time)],
                 [sp.sin(w*time),sp.cos(w*time)]])
    Js=sp.Matrix([[0,-1],[1,0]])
    assert (Q.T*Q-sp.eye(2)).applyfunc(sp.simplify)==sp.zeros(2)
    assert (sp.diff(Q,time)-w*Js*Q).applyfunc(sp.simplify)==sp.zeros(2)
    assert (sp.diff(Q,time,2)+w*w*Q).applyfunc(sp.simplify)==sp.zeros(2)
    assert (Q.T*Js*Q-Js).applyfunc(sp.simplify)==sp.zeros(2)
    uu,vv=sp.symbols('uu vv',real=True)
    force_vector=sp.Matrix([uu,vv])/(uu*uu+vv*vv)**sp.Rational(3,2)
    coulomb_jacobian=force_vector.jacobian([uu,vv]).subs({uu:r,vv:0})
    assert sp.simplify(coulomb_jacobian-sp.diag(-2,1)/r**3)==sp.zeros(2)
    position_block=(w*w-Omega*w)*sp.eye(2)+C*coulomb_jacobian
    assert sp.simplify(position_block.subs(C,r**3*s)-sp.diag(-3*s,0))==sp.zeros(2)

    root_rows=[];orbit_rows=[];radial_rows=[];rest_rows=[];linear_rows=[]
    for Om,length in [(.7,.6),(1.8,1.4)]:
        for eta in [.02,.1,.24,.25,.27]:
            interaction=eta*Om**2*length**3;ode=rhs_planar(Om,interaction)
            def actual_balance(rate):
                state=state_circle(length,rate)
                return ode(0,state)[4]+rate*rate*length/2
            if eta>.25:
                opt=minimize_scalar(actual_balance,bounds=(0,Om),method='bounded')
                assert opt.fun>0
                root_rows.append(dict(Omega=Om,l=length,eta=eta,
                    exists=False,minimum_actual_radial_residual=float(opt.fun)))
                continue
            if eta==.25:
                branches=[('merged',Om/2)]
            else:
                branches=[('lower',brentq(actual_balance,0,Om/2,xtol=1e-14)),
                          ('upper',brentq(actual_balance,Om/2,Om,xtol=1e-14))]
            for branch,rate in branches:
                D=math.sqrt(max(0,Om**2/4-interaction/length**3))
                expected=Om/2+(-D if branch=='lower' else D if branch=='upper' else 0)
                assert abs(rate-expected)<2e-13*Om
                assert abs(actual_balance(rate))<3e-13*length*Om**2
                root_rows.append(dict(Omega=Om,l=length,eta=eta,branch=branch,
                    exists=True,rate_from_actual_Cartesian_force=rate,rate_formula=expected))
                period=2*math.pi/rate
                sol=solve_ivp(ode,[0,period],state_circle(length,rate),
                    method='DOP853',rtol=3e-12,atol=1e-13,max_step=.12/Om,
                    t_eval=np.linspace(0,period,501))
                distance,canonical,energy=invariants(sol.y,interaction,Om)
                actual=np.vstack([length/2*np.cos(rate*sol.t),length/2*np.sin(rate*sol.t)])
                assert np.max(abs(distance/length-1))<3e-8
                assert np.max(abs(sol.y[:2]-actual))/length<3e-8
                assert np.max(abs(sol.y[:4,-1]-sol.y[:4,0]))/length<3e-8
                assert np.ptp(canonical)/(length*length*Om)<3e-8
                assert np.ptp(energy)/max(abs(energy[0]),1e-10)<3e-8
                orbit_rows.append(dict(Omega=Om,l=length,eta=eta,branch=branch,
                    period=period,separation_relative_error=float(np.max(abs(distance/length-1))),
                    Cartesian_position_relative_error=float(np.max(abs(sol.y[:2]-actual))/length),
                    canonical_angular_drift=float(np.ptp(canonical)),
                    total_energy_relative_drift=float(np.ptp(energy)/energy[0])))
                # Perturb separation while conserving actual canonical angular momentum.
                target_j=length**2*(rate-Om/2)
                perturbed=length*(1+2e-5)
                pert_rate=Om/2+target_j/perturbed**2
                expected_kappa=math.sqrt(Om**2-interaction/length**3)
                radial_period=2*math.pi/expected_kappa
                def radial_max(time,state):
                    R=state[:2]-state[2:4];W=state[4:6]-state[6:8]
                    return float(R@W)
                radial_max.direction=-1
                solution=solve_ivp(ode,[0,3.2*radial_period],state_circle(perturbed,pert_rate),
                    method='DOP853',rtol=4e-13,atol=1e-14,max_step=radial_period/180,
                    events=radial_max,t_eval=np.linspace(0,3.2*radial_period,801))
                events=solution.t_events[0];events=events[events>radial_period*1e-5]
                assert len(events)>=3
                recovered=float(np.mean(np.diff(events)))
                assert abs(recovered/radial_period-1)<3e-7
                distances,js,energies=invariants(solution.y,interaction,Om)
                assert max(abs(distances-length))/length<2.1e-5
                assert np.ptp(js)/(length*length*Om)<1e-10
                radial_rows.append(dict(Omega=Om,l=length,eta=eta,branch=branch,
                    radial_period_from_Newton_peaks=recovered,linear_radial_period=radial_period,
                    max_relative_radial_excursion=float(max(abs(distances-length))/length),
                    canonical_angular_drift=float(np.ptp(js))))
                # Recover the rotating-frame Jacobian from vector force probes.
                def rotating_force(state):
                    pos=state[:2];vel=state[2:]
                    physical=interaction*pos/np.linalg.norm(pos)**3
                    return np.r_[vel,physical+(rate*rate-Om*rate)*pos+(Om-2*rate)*(J@vel)]
                center=np.array([length,0,0,0.]);h=length*1e-5
                jac=np.column_stack([(rotating_force(center+np.eye(4)[i]*h)
                                     -rotating_force(center-np.eye(4)[i]*h))/(2*h) for i in range(4)])
                eigen=np.linalg.eigvals(jac)
                oscillatory=max(abs(eigen.imag))
                assert abs(oscillatory/expected_kappa-1)<2e-9
                assert max(abs(eigen.real))/Om<2e-5
                linear_rows.append(dict(Omega=Om,l=length,eta=eta,branch=branch,
                    eigenvalues=[[float(z.real),float(z.imag)] for z in eigen],
                    independently_recovered_radial_frequency=float(oscillatory)))
                # Case (2): one electron moving, the other initially stationary.
                initial_speed=rate*length
                V=np.array([0,initial_speed/2])
                initial=state_circle(length,rate,V)
                assert np.linalg.norm(initial[6:8])<1e-14
                expected_stop=math.pi/(Om-rate)
                def minimum_speed(time,state):
                    acceleration=ode(time,state)[4:6]
                    return float(state[4:6]@acceleration)
                minimum_speed.direction=1
                solution=solve_ivp(ode,[0,1.05*expected_stop],initial,
                    method='DOP853',rtol=3e-12,atol=1e-13,max_step=.12/Om,
                    dense_output=True,events=minimum_speed,
                    t_eval=np.linspace(0,1.05*expected_stop,601))
                candidates=solution.t_events[0]
                candidates=candidates[candidates>1e-6/Om]
                first=float(candidates[0])
                at_stop=solution.sol(first)
                assert abs(first/expected_stop-1)<3e-9
                assert np.linalg.norm(at_stop[4:6])/initial_speed<3e-8
                distances,js,energies=invariants(solution.y,interaction,Om)
                CM=(solution.y[:2]+solution.y[2:4])/2
                Rc=initial_speed/(2*Om)
                center_CM=np.array([-Rc,0])
                radius=np.linalg.norm(CM-center_CM[:,None],axis=0)
                assert np.max(abs(radius/Rc-1))<3e-8
                assert np.max(abs(distances/length-1))<3e-8
                # At the first electron's rest instant the other speed is v0,
                # and the first electron accelerates again due to repulsion.
                assert abs(np.linalg.norm(at_stop[6:8])/initial_speed-1)<3e-8
                assert np.linalg.norm(ode(first,at_stop)[4:6])>0
                rest_rows.append(dict(Omega=Om,l=length,eta=eta,branch=branch,
                    initial_speed=initial_speed,
                    first_speed_minimum_from_Newton_event=first,first_rest_formula=expected_stop,
                    speed_residual_relative=float(np.linalg.norm(at_stop[4:6])/initial_speed),
                    center_of_mass_circle_radius=Rc,
                    fitted_CM_radius_relative_error=float(np.max(abs(radius/Rc-1))),
                    separation_relative_error=float(np.max(abs(distances/length-1))),
                    acceleration_at_rest=float(np.linalg.norm(ode(first,at_stop)[4:6]))))
    # Variant (3): both initial speeds nonzero, with the same relative circle.
    unequal_rows=[]
    Om=1.2;length=.8
    for eta in [.1,.24]:
        interaction=eta*Om**2*length**3;ode=rhs_planar(Om,interaction)
        for branch in [-1,1]:
            rate=Om/2+branch*math.sqrt(Om*Om/4-interaction/length**3)
            difference=rate*length
            for fraction in [0.,.2,.6]:
                b=fraction*difference;a=b+difference
                initial=state_circle(length,rate,np.array([0,(a+b)/2]))
                def minimum_speed(time,state):
                    return float(state[4:6]@ode(time,state)[4:6])
                minimum_speed.direction=1
                expected_time=math.pi/(Om-rate)
                sol=solve_ivp(ode,[0,1.05*expected_time],initial,method='DOP853',
                    rtol=3e-12,atol=1e-13,max_step=.1/Om,events=minimum_speed,
                    dense_output=True,t_eval=np.linspace(0,1.05*expected_time,501))
                events=sol.t_events[0];events=events[events>1e-6/Om]
                recovered=float(events[0]);at_min=sol.sol(recovered)
                assert abs(recovered/expected_time-1)<3e-9
                assert abs(np.linalg.norm(at_min[4:6])-b)/a<3e-8
                assert abs(np.linalg.norm(at_min[6:8])-a)/a<3e-8
                distances,js,energies=invariants(sol.y,interaction,Om)
                assert np.max(abs(distances/length-1))<3e-8
                assert np.ptp(energies)/energies[0]<3e-8
                unequal_rows.append(dict(eta=eta,branch='lower' if branch<0 else 'upper',
                    initial_speed1=a,initial_speed2=b,
                    first_speed_minimum_time=recovered,predicted_time=expected_time,
                    actual_minimum_speed=float(np.linalg.norm(at_min[4:6])),
                    predicted_minimum_speed=b,can_stop=(b==0)))
    # Variant (4): critical-field splitting, tested with actual forces and ODE events.
    critical_rows=[]
    Omc=1.7;length=.9;interaction=Omc*Omc*length**3/4
    for epsilon in [1e-5,1e-4,.001,.01]:
        Om=Omc*(1+epsilon);ode=rhs_planar(Om,interaction)
        def balance(rate):
            state=state_circle(length,rate)
            return ode(0,state)[4]+rate*rate*length/2
        for branch in [-1,1]:
            left,right=(0,Om/2) if branch<0 else (Om/2,Om)
            rate=brentq(balance,left,right,xtol=1e-14)
            exact_rate=Omc/2*(1+epsilon+branch*math.sqrt(2*epsilon+epsilon**2))
            assert abs(rate/exact_rate-1)<3e-12
            initial_speed=rate*length
            initial=state_circle(length,rate,np.array([0,initial_speed/2]))
            exact_stop=2*math.pi/Omc*(1+epsilon+branch*math.sqrt(2*epsilon+epsilon**2))
            def minimum_speed(time,state):
                return float(state[4:6]@ode(time,state)[4:6])
            minimum_speed.direction=1
            sol=solve_ivp(ode,[0,1.05*exact_stop],initial,method='DOP853',
                rtol=3e-12,atol=1e-13,max_step=.1/Om,events=minimum_speed,dense_output=True)
            events=sol.t_events[0];events=events[events>1e-6/Om]
            recovered=float(events[0])
            assert abs(recovered/exact_stop-1)<3e-9
            kappa=math.sqrt(Om*Om-interaction/length**3)
            approx_kappa=math.sqrt(3)*Omc/2*(1+4*epsilon/3)
            assert abs(approx_kappa/kappa-1)<epsilon**2
            stop_approx=2*math.pi/Omc*(1+branch*math.sqrt(2*epsilon)+epsilon)
            assert abs((stop_approx-exact_stop)/(2*math.pi/Omc))<epsilon**1.5
            # Independently recover radial frequency from a Cartesian vector Jacobian.
            def rotating_force(state):
                pos=state[:2];vel=state[2:]
                return np.r_[vel,interaction*pos/np.linalg.norm(pos)**3
                    +(rate*rate-Om*rate)*pos+(Om-2*rate)*(J@vel)]
            center=np.array([length,0,0,0.]);h=length*1e-5
            jac=np.column_stack([(rotating_force(center+np.eye(4)[i]*h)
                -rotating_force(center-np.eye(4)[i]*h))/(2*h) for i in range(4)])
            eigen=np.linalg.eigvals(jac)
            recovered_kappa=float(max(abs(eigen.imag)))
            assert abs(recovered_kappa/kappa-1)<2e-9
            critical_rows.append(dict(epsilon=epsilon,branch='lower' if branch<0 else 'upper',
                omega_actual_force_root=rate,omega_formula=exact_rate,
                first_minimum_from_Newton=recovered,exact_first_rest=exact_stop,
                kappa_from_vector_Jacobian=recovered_kappa,kappa_formula=kappa,
                kappa_leading_expansion=approx_kappa,first_rest_expansion=stop_approx))

    # Optional scope check: the stipulated plane must not be confused with 3D stability.
    vertical_rows=[]
    for eta in [.02,.1,.24]:
        Om=1.2;length=.8;interaction=eta*Om**2*length**3
        for branch in [-1,1]:
            rate=Om/2+branch*math.sqrt(Om*Om/4-interaction/length**3)
            def ode3(time,state):
                R=state[:3]-state[3:6];v1=state[6:9];v2=state[9:12]
                force=interaction/2*R/np.linalg.norm(R)**3
                lorentz=lambda v:Om*np.array([-v[1],v[0],0.])
                return np.r_[v1,v2,force+lorentz(v1),-force+lorentz(v2)]
            eps=length*1e-6
            initial=np.r_[[length/2,0,eps/2],[-length/2,0,-eps/2],
                           [0,rate*length/2,0],[0,-rate*length/2,0]]
            times=np.linspace(0,4/Om,301)
            sol=solve_ivp(ode3,[0,times[-1]],initial,method='DOP853',
                rtol=1e-12,atol=1e-15,t_eval=times,max_step=.05/Om)
            relative_z=sol.y[2]-sol.y[5]
            expected=eps*np.cosh(math.sqrt(interaction/length**3)*times)
            assert max(abs(relative_z/expected-1))<1e-8
            vertical_rows.append(dict(eta=eta,branch='lower' if branch<0 else 'upper',
                exponential_rate=math.sqrt(interaction/length**3),
                growth_factor=float(relative_z[-1]/eps),
                linear_growth_relative_error=float(max(abs(relative_z/expected-1)))))
    # Figure 5-4 is a true state of the two-electron model, not arbitrary circles.
    Om=1.;length=4.;rate=.4;interaction=(Om*rate-rate*rate)*length**3
    time=math.radians(50);a_c=rate*length/(2*Om)
    initial=state_circle(length,rate,np.array([0,rate*length/2]))
    sample=solve_ivp(rhs_planar(Om,interaction),[0,time],initial,
        method='DOP853',rtol=1e-13,atol=1e-14,max_step=.02)
    CM=a_c*np.array([math.cos(Om*time)-1,math.sin(Om*time)])
    rel=length*np.array([math.cos(rate*time),math.sin(rate*time)])
    positions=np.r_[CM+rel/2,CM-rel/2]
    assert np.max(abs(sample.y[:4,-1]-positions))<2e-12
    assert abs(math.degrees(rate*time)-20)<1e-14
    diagram_geometry=dict(Omega=Om,omega=rate,l=length,a_c=a_c,
        Omega_t_degrees=50,omega_t_degrees=20,
        current_CM=CM.tolist(),electron1=positions[:2].tolist(),
        electron2=positions[2:].tolist(),
        Cartesian_Newton_position_error=float(np.max(abs(sample.y[:4,-1]-positions))),
        circled_relative_positions_are_not_absolute_particle_trajectories=True)

    # Dimensional and physical numerical checks for electrons.
    me=9.1093837139e-31;qe=1.602176634e-19;ke=8.9875517923e9;c=299792458.
    B=1.;length=1e-6;Om=qe*B/me;interaction=2*ke*qe*qe/me
    critical=(4*interaction/(Om*Om))**(1/3)
    assert abs(critical/(2*(ke*me/B**2)**(1/3))-1)<1e-14
    physical=[]
    for branch in [-1,1]:
        rate=Om/2+branch*math.sqrt(Om*Om/4-interaction/length**3)
        physical.append(dict(branch='lower' if branch<0 else 'upper',Omega=Om,l=length,
            omega=rate,speed_case1=rate*length/2,speed_case2=rate*length,
            speed_case2_over_c=rate*length/c,
            CM_radius_case2=rate*length/(2*Om),first_rest=math.pi/(Om-rate),
            radial_frequency=math.sqrt(Om*Om-interaction/length**3)))
    # Variant: l = 2*l_critical, two positive frequencies.
    fractions=[(1-math.sqrt(7/8))/2,(1+math.sqrt(7/8))/2]
    assert all(abs(f*f-f+1/32)<1e-15 for f in fractions)
    assert all(0<f<1 for f in fractions)
    figures=['question-05','force-05','radial-05','com-05','velocity-05']
    sources=['scripts/verify_question_05.py','drafts/question-05.md','figures/题05_图稿源文件.tex']
    complete=all((ROOT/path).exists() for path in sources) and all(
        (ROOT/f'figures/{name}.{extension}').exists()
        for name in figures for extension in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-05.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察',
                 '易错点','课堂讲解建议','变式训练']
        assert [s.split('、',1)[1] for s in text.splitlines() if s.startswith('## ')]==modules
        assert text.count('<!-- question-complete -->')==1
        assert all(text.count(f'../figures/{name}.png')==1 for name in figures)
    report=dict(question=5,verified_math=True,document_complete=complete,set_accepted=False,
        scope='preliminary independent Cartesian Newton integration; no visual or whole-set acceptance' if not complete else 'independent Cartesian Newton integration and source binding; no visual or whole-set acceptance',
        exact_effective_potential_per_reduced_mass=str(U),
        exact_circular_radial_frequency_squared=str(kappa2),
        corrected_handwritten_outward_force_coefficient=str(linear_coefficient),
        rotating_frame_characteristic=str(A.charpoly(lam).as_expr().factor()),
        rotating_coordinate_derivatives_and_Coulomb_Jacobian_verified=True,
        circular_roots_from_actual_vectors=root_rows,
        two_electron_Newton_circles=orbit_rows,
        radial_stability_Newton_peak_tests=radial_rows,
        rotating_frame_vector_jacobian_tests=linear_rows,
        CM_and_first_rest_Newton_event_tests=rest_rows,
        unequal_initial_speeds_Newton_events=unequal_rows,
        critical_field_Newton_roots_events_and_vector_Jacobians=critical_rows,
        out_of_plane_scope_tests=vertical_rows,
        exact_drawn_CM_and_relative_circle_geometry=diagram_geometry,
        solved_variants=dict(two_critical_length_omega_over_Omega=fractions,
            physical_electron_parameters=dict(m=me,q=qe,k=ke,B=B,l=length,l_critical=critical,
                                             cases=physical),
            planar_stability=dict(kappa_squared_min_over_Omega_squared=.75,
                radial_mode_equal_for_both_branches=True,neutral_phase=True),
            unequal_initial_speeds=unequal_rows,
            critical_field=critical_rows,
            out_of_plane=dict(relative_z_growth_rate='sqrt(C/l^3)',samples=vertical_rows)),
        dimensional_checks=dict(order=['mass','length','time'],
            Omega=[0,0,-1],C=[0,3,-2],canonical_j=[0,2,-1],
            effective_potential_per_reduced_mass=[0,2,-2],first_rest=[0,0,1],
            critical_length=[0,1,0],passed=True),
        assumptions=['q > 0, B0 > 0 along +z, electron charge -q',
                     'classical point charges, Coulomb interaction and prescribed uniform Lorentz field only',
                     'positive angular speed means counterclockwise seen from +z',
                     'planar radial/orbital stability allows phase drift and small displacement of orbit center',
                     'the problem stipulates motion in x-y plane; unrestricted 3D transverse stability is different',
                     'case (2) initial moving-electron speed is twice case (1) speed at equal l and branch'],
        handwritten_notes=['circular discriminant and CM cyclotron equation are correct',
            'preserve canonical angular momentum and speed expansion, but correct the final radial-force simplification',
            'the lower branch is also radially/orbitally stable in the stipulated plane for every allowed l',
            'part (2) omega=v0/l, not 2v0/l; first-rest denominator sign must remain tied to the branch'],
        source_sha256={path:sha(ROOT/path) for path in sources if (ROOT/path).exists()},
        figures_sha256={name:sha(ROOT/f'figures/{name}.pdf') for name in figures} if complete else {},
        originals_sha256={path.name:sha(path) for path in ROOT.parent.glob('*.pdf')})
    record='verification-q05.json' if complete else 'verification-q05-preliminary.json'
    (ROOT/'build'/record).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,
        circular_force_tests=len(root_rows),circular_Newton_cases=len(orbit_rows),
        radial_peak_tests=len(radial_rows),vector_Jacobians=len(linear_rows),
        CM_and_first_rest_cases=len(rest_rows),out_of_plane_scope_tests=len(vertical_rows),
        unequal_initial_speed_cases=len(unequal_rows),critical_field_cases=len(critical_rows),
        critical_l_physical=critical,physical_cases=physical),ensure_ascii=False))
if __name__=='__main__':main()
