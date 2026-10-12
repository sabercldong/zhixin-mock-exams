"""016 Q5: integrate the actual two-branch electromechanical system.

The user approved the explicit initial conditions on 2026-10-09.
General initial velocities are also independently checked as variants.
"""
from pathlib import Path
import argparse,hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from sympy.physics.units import henry,farad,tesla,meter,kilogram,coulomb,second
from sympy.physics.units.systems.si import SI

ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def frequencies(m,L,C,k):return k/math.sqrt(m*L),math.sqrt(k*k/(m*L)+2/(L*C))
def rhs(m,L,C,k):
    def fn(t,y):
        q,i1,i2,v1,v2,x1,x2=y
        return [i1+i2,(k*v1-q/C)/L,(k*v2-q/C)/L,
                -k*i1/m,-k*i2/m,v1,v2]
    return fn
def closed(t,m,L,C,k,Q,u1,u2):
    w,O=frequencies(m,L,C,k);Pi=m*(u1+u2)+k*Q
    qe=k*C*Pi/(2*m+k*k*C);drift=Pi/(2*m+k*k*C)
    q=qe+(Q-qe)*np.cos(O*t);qd=-(Q-qe)*O*np.sin(O*t)
    vc=Pi/(2*m)-k*q/(2*m);delta=(u2-u1)*np.cos(w*t)
    idiff=m*(u2-u1)*w*np.sin(w*t)/k
    xc=drift*t-k*(Q-qe)/(2*m*O)*np.sin(O*t)
    dx=(u2-u1)/w*np.sin(w*t)
    return np.array([q,(qd-idiff)/2,(qd+idiff)/2,
                     vc-delta/2,vc+delta/2,xc-dx/2,xc+dx/2])
def energy(y,m,L,C):
    q,i1,i2,v1,v2=y[:5]
    return q*q/(2*C)+L*(i1*i1+i2*i2)/2+m*(v1*v1+v2*v2)/2
def run_case(m,L,C,k,Q,u1,u2,periods=2):
    w,O=frequencies(m,L,C,k)
    times=np.linspace(0,periods*2*math.pi/w,101)
    y0=[Q,0,0,u1,u2,0,0]
    result=solve_ivp(rhs(m,L,C,k),[0,times[-1]],y0,
                    t_eval=times,method='DOP853',rtol=2e-10,atol=2e-12)
    assert result.success
    expected=closed(times,m,L,C,k,Q,u1,u2)
    scales=np.maximum(np.max(np.abs(expected),axis=1),.1)
    err=np.max(np.abs(result.y-expected)/scales[:,None])
    E0=energy(np.array(y0),m,L,C)
    eerr=np.max(np.abs(energy(result.y,m,L,C)-E0))/max(E0,.1)
    mom=m*(result.y[3]+result.y[4])+k*result.y[0]
    perr=np.max(np.abs(mom-(m*(u1+u2)+k*Q)))
    common=L/4*((result.y[1]+result.y[2])**2+O**2*
                (result.y[0]-k*C*(m*(u1+u2)+k*Q)/(2*m+k*k*C))**2)
    diff=m/4*(result.y[4]-result.y[3])**2+L/4*(result.y[2]-result.y[1])**2
    merr=max(np.max(np.abs(common-common[0])),np.max(np.abs(diff-diff[0])))
    assert err<2e-7 and eerr<2e-8 and perr<2e-9 and merr<2e-8*max(E0,1)
    # Eigenvalues of the actual five-state electrical/mechanical operator.
    A=np.array([[0,1,1,0,0],[-1/(C*L),0,0,k/L,0],
                [-1/(C*L),0,0,0,k/L],[0,-k/m,0,0,0],[0,0,-k/m,0,0]],float)
    eig=np.linalg.eigvals(A)
    target=[0,1j*w,-1j*w,1j*O,-1j*O]
    eigen_error=max(min(abs(z-e) for e in eig) for z in target)
    assert eigen_error<1e-8*max(O,1)
    return dict(m=m,L=L,C=C,Bl=k,Q0=Q,u_left=u1,u_right=u2,
                omega0=w,Omega=O,actual_ODE_relative_error=err,
                relative_total_energy_error=eerr,
                canonical_momentum_error=perr,independent_mode_energy_error=merr,
                actual_five_state_eigenvalue_error=eigen_error)
def main():
    p=argparse.ArgumentParser();p.add_argument('--complete',action='store_true');args=p.parse_args()
    m,L,C,k,Q,t,w,O=sp.symbols('m L C k Q t w O',positive=True)
    x=Q*k/(2*m)*(sp.sin(w*t)/w-sp.sin(O*t)/O)
    operator=sp.diff(x,t,2)+w*w*x-Q*k/(m*L*C*O)*sp.sin(O*t)
    assert sp.simplify(operator.subs(O**2,w*w+2/(L*C)))==0
    assert sp.simplify(x.subs(t,0))==0 and sp.simplify(sp.diff(x,t).subs(t,0))==0
    cubic=sp.simplify(sp.diff(x,t,3).subs(t,0).subs(O**2,w*w+2/(L*C)))
    assert cubic==Q*k/(m*L*C)
    q,i1,i2,v1,v2=sp.symbols('q i1 i2 v1 v2',real=True)
    deriv=[i1+i2,(k*v1-q/C)/L,(k*v2-q/C)/L,-k*i1/m,-k*i2/m]
    E=q*q/(2*C)+L*(i1*i1+i2*i2)/2+m*(v1*v1+v2*v2)/2
    assert sp.simplify(sum(sp.diff(E,s)*d for s,d in zip([q,i1,i2,v1,v2],deriv)))==0
    units=dict(CL=SI.get_dimensional_expr(henry*farad),
               BlQ=SI.get_dimensional_expr(tesla*meter*coulomb),
               Bl_squared_over_mL=SI.get_dimensional_expr((tesla*meter)**2/(kilogram*henry)))
    ds=SI.get_dimension_system()
    for actual,expected in [(henry*farad,second**2),
                            (tesla*meter*coulomb,kilogram*meter/second),
                            ((tesla*meter)**2/(kilogram*henry),second**-2)]:
        assert ds.equivalent_dims(SI._collect_factor_and_dimension(actual)[1],
                                  SI._collect_factor_and_dimension(expected)[1])
    original=[];general=[];cubic_checks=[]
    for mv in [.12,.4,1.1]:
        for kv in [.05,.8,1.7]:
            for Cv,Lv in [(.03,.07),(.2,.5)]:
                Qv=.4;v0=Qv*kv/mv
                original.append(run_case(mv,Lv,Cv,kv,Qv,0,-v0))
                general.append(run_case(mv,Lv,Cv,kv,Qv,.35*v0,-1.2*v0,periods=1))
                wv,Ov=frequencies(mv,Lv,Cv,kv)
                tt=1e-3/Ov
                sol=solve_ivp(rhs(mv,Lv,Cv,kv),[0,tt],[Qv,0,0,0,-v0,0,0],
                              method='DOP853',rtol=1e-12,atol=1e-16)
                expected=v0*tt**3/(6*Lv*Cv)
                rel=abs(sol.y[5,-1]/expected-1)
                assert rel<2e-6
                cubic_checks.append(dict(m=mv,Bl=kv,C=Cv,L=Lv,
                    actual_ODE_small_time_x1=sol.y[5,-1],cubic_ratio_error=rel))
    # Read the correct final handwritten expression separately from its erroneous intermediate sign.
    wrong_A=1/(O*(O*O+w*w));correct_A=1/(O*(w*w-O*O))
    assert sp.simplify((w*w-O*O)*correct_A-1/O)==0
    wrong_residual=sp.simplify((w*w-O*O)*wrong_A-1/O)
    assert wrong_residual!=0
    mv,Lv,Cv,kv,Qv=.2,.08,.02,.4,.5
    v0=Qv*kv/mv;wv,Ov=frequencies(mv,Lv,Cv,kv)
    var1=dict(v0=v0,omega0=wv,Omega=Ov,
              center_at_t_point05=closed(.05,mv,Lv,Cv,kv,Qv,0,-v0)[5:7].mean(),
              left_at_t_point08=closed(.08,mv,Lv,Cv,kv,Qv,0,-v0)[5],
              initial_energy=Qv**2/(2*Cv)+mv*v0*v0/2)
    numeric_solution=solve_ivp(rhs(mv,Lv,Cv,kv),[0,.08],
        [Qv,0,0,0,-v0,0,0],t_eval=[.05,.08],
        method='DOP853',rtol=1e-12,atol=1e-14)
    assert numeric_solution.success
    actual_center=numeric_solution.y[5:7,0].mean()
    actual_left=numeric_solution.y[5,1]
    assert abs(actual_center-var1['center_at_t_point05'])<1e-11
    assert abs(actual_left-var1['left_at_t_point08'])<1e-11
    var1['independent_ODE_center_at_t_point05']=actual_center
    var1['independent_ODE_left_at_t_point08']=actual_left
    collisions=[];d0=.2;amp=v0/wv
    tc=math.asin(d0/amp)/wv
    for cap in [.01,.02,.1]:
        def event(t,y):return d0+y[6]-y[5]
        event.terminal=True;event.direction=-1
        res=solve_ivp(rhs(mv,Lv,cap,kv),[0,math.pi/wv],
                [Qv,0,0,0,-v0,0,0],events=event,method='DOP853',rtol=1e-11,atol=1e-13)
        actual=res.t_events[0][0]
        assert abs(actual-tc)<2e-9
        collisions.append(dict(C=cap,first_actual_contact_seconds=actual,
             predicted_contact_seconds=tc,minimum_initial_separation_for_no_collision=amp))
    ul=.4;ur=-1;Pi=mv*(ul+ur)+kv*Qv
    qe=kv*Cv*Pi/(2*mv+kv*kv*Cv);drift=Pi/(2*mv+kv*kv*Cv)
    cycle=2*math.pi/Ov;at_cycle=closed(cycle,mv,Lv,Cv,kv,Qv,ul,ur)
    assert abs(at_cycle[5:7].mean()-drift*cycle)<1e-12
    var3=dict(Pi=Pi,q_equilibrium=qe,center_drift_velocity=drift,
              common_mode_cycle=cycle,center_displacement_after_cycle=at_cycle[5:7].mean())
    general_solution=solve_ivp(rhs(mv,Lv,Cv,kv),[0,cycle],
        [Qv,0,0,ul,ur,0,0],method='DOP853',rtol=1e-12,atol=1e-14)
    assert general_solution.success
    actual_cycle_center=general_solution.y[5:7,-1].mean()
    assert abs(actual_cycle_center-drift*cycle)<1e-11
    var3['independent_ODE_center_displacement_after_cycle']=actual_cycle_center
    c_res=2*mv/(3*kv*kv);w_res,O_res=frequencies(mv,Lv,c_res,kv)
    assert abs(O_res-2*w_res)<1e-12
    whole=2*math.pi/w_res;half=closed(whole/2,mv,Lv,c_res,kv,Qv,0,-v0)
    full=closed(whole,mv,Lv,c_res,kv,Qv,0,-v0)
    assert np.linalg.norm(full-np.array([Qv,0,0,0,-v0,0,0]))<1e-12
    assert abs(half[3]+v0)<1e-12 and abs(half[4])<1e-12
    tuned_solution=solve_ivp(rhs(mv,Lv,c_res,kv),[0,whole],
        [Qv,0,0,0,-v0,0,0],t_eval=[whole/2,whole],
        method='DOP853',rtol=1e-12,atol=1e-14)
    assert tuned_solution.success
    assert np.max(np.abs(tuned_solution.y[:,0]-half))<1e-10
    assert np.max(np.abs(tuned_solution.y[:,1]-full))<1e-10
    sources={'scripts/verify_question_05.py':sha(Path(__file__))};figures={}
    approved_path=ROOT/'build/question-05-条件确认.json'
    approved=json.loads(approved_path.read_text())
    resolved=approved.get('approved') is True and approved.get('document_revision_implemented') is True
    assert resolved
    sources['build/question-05-条件确认.json']=sha(approved_path)
    if args.complete:
        source=ROOT/'drafts/question-05.md';body=source.read_text()
        assert '<!-- question-complete -->' in body and body.count('\n## ')==9
        stem=body.split('<!-- question-end -->')[0]
        assert '初始时左杆静止' in stem and '两个金属杆支路的电流分别为零' in stem and '修订说明' in stem
        sources['drafts/question-05.md']=sha(source)
        sources['figures/题05_图稿源文件.tex']=sha(ROOT/'figures/题05_图稿源文件.tex')
        geometry_path=ROOT/'build/projected-geometry-q05.json'
        geometry=json.loads(geometry_path.read_text())
        assert geometry['passed']
        assert geometry['script_sha256']==sha(ROOT/'scripts/check_projected_question_05.py')
        assert geometry['tikz_source_sha256']==sources['figures/题05_图稿源文件.tex']
        sources['scripts/check_projected_question_05.py']=sha(ROOT/'scripts/check_projected_question_05.py')
        sources['build/projected-geometry-q05.json']=sha(geometry_path)
        for name in ['question-05','forces-05','circuit-05','motion-05','modes-05','energy-05']:
            figures[name]=sha(ROOT/f'figures/{name}.pdf')
        assert figures==geometry['figures_sha256']
    result=dict(question=5,verified_math=True,document_complete=args.complete,set_accepted=False,
        model_condition_resolved=resolved,
        pending_condition=None if resolved else 'Left rod initially at rest and both branch currents initially zero; handwritten initial data, printed left velocity unstated',
        original_initial_value_ODEs=original,general_initial_value_ODEs=general,
        small_time_cubic_ODE_checks=cubic_checks,dimensional_checks={n:str(u) for n,u in units.items()},
        handwritten_final_result_correct=True,
        handwritten_particular_second_derivative_sign_corrected=True,
        handwritten_wrong_intermediate_operator_residual=str(wrong_residual),
        solved_variants=dict(numerical=var1,collision_checks=collisions,general_initial_velocity=var3,
            commensurate=dict(C=c_res,omega0=w_res,Omega=O_res,full_return_period=whole,
                             half_period_state=half.tolist(),full_period_state=full.tolist(),
                             independent_ODE_half_period_state=tuned_solution.y[:,0].tolist(),
                             independent_ODE_full_period_state=tuned_solution.y[:,1].tolist())),
        source_sha256=sources,figures_sha256=figures,
        originals_sha256={name:sha(ROOT.parent/name) for name in ['试卷.pdf','答案.pdf']})
    path=ROOT/('build/verification-q05.json' if args.complete else 'build/verification-q05-preliminary.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=5,verified_math=True,document_complete=args.complete,
        model_condition_resolved=resolved,original_ODEs=len(original),general_ODEs=len(general),
        cubic_checks=len(cubic_checks),variants=result['solved_variants']),ensure_ascii=False))
if __name__=='__main__':main()
