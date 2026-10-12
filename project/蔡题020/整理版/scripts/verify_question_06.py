"""球壳体积、绝热功积分及壳层牛顿方程的独立验证。"""
from pathlib import Path
import math,json,hashlib
import sympy as sp
from scipy.integrate import quad,solve_ivp

ROOT=Path(__file__).resolve().parents[1]

def main():
    alpha=sp.symbols('alpha',positive=True)
    ratio=(1-alpha)**(-3)-1
    series=sp.series(ratio,alpha,0,4)
    assert sp.simplify(series.removeO()-(3*alpha+6*alpha**2+10*alpha**3))==0
    geometry=[]
    for a in [.005,.02,.05,.1]:
        shell=quad(lambda radius:4*math.pi*radius*radius,1-a,1,epsabs=1e-13)[0]
        core=quad(lambda radius:4*math.pi*radius*radius,0,1-a,epsabs=1e-13)[0]
        actual=shell/core;closed=(1-a)**(-3)-1
        assert abs(actual-closed)<1e-12
        geometry.append(dict(alpha=a,shell_volume=shell,core_volume=core,volume_ratio=actual,
                             thin_ratio=3*a,thin_relative_underestimate=1-3*a/closed))
    dynamics=[]
    for h in [.001,.1,1.,10.,100.]:
        # a0=U0=ms=1，gamma=5/3；压力面力由P=2U/(3V)给出F=2U/a。
        def rhs(t,y):
            a,v=y;U=1/(a*a);return [v,2*U/a]
        def stagnation(t,y):return y[1]
        stagnation.terminal=True;stagnation.direction=1
        solution=solve_ivp(rhs,[0,30],[1,-math.sqrt(2*h)],rtol=1e-11,atol=1e-12,
                           events=stagnation,dense_output=True,max_step=.005)
        assert len(solution.t_events[0])==1
        afinal=solution.y_events[0][0,0];temperature=1/(afinal*afinal);density=1/(afinal**3)
        expected=(1+h)**(-.5)
        assert abs(afinal-expected)/expected<1e-9
        v0=math.sqrt(2*h);time=solution.t
        squared_radius=1-2*v0*time+(v0*v0+2)*time*time
        trajectory_error=max(abs(solution.y[0]**2-squared_radius))
        predicted_time=v0/(v0*v0+2)
        assert trajectory_error<1e-9 and abs(solution.t_events[0][0]-predicted_time)<1e-9
        energies=.5*solution.y[1]**2+1/solution.y[0]**2
        conservation=max(abs(energies-(1+h)))/(1+h)
        work=quad(lambda a:-2/a**3,1,afinal,epsabs=1e-10)[0]
        assert abs(work-h)/(1+h)<1e-9 and conservation<1e-9
        dynamics.append(dict(initial_kinetic_to_internal=h,radius_at_zero_shell_speed=afinal,
                             T1_over_T0=temperature,n1_over_n0=density,pressure_work=work,
                             relative_energy_drift=conservation,event_time=float(solution.t_events[0][0])))
        dynamics[-1].update(squared_radius_trajectory_max_error=trajectory_error,predicted_event_time=predicted_time)
    # gamma不同的一般化不沿用3/2指数。
    general=[]
    for gamma in [1.4,5/3,2.]:
        h=2.;power=3*(gamma-1);a=(1+h)**(-1/power)
        work=quad(lambda radius:-power*radius**(-power-1),1,a)[0]
        assert abs(work-h)<1e-10
        general.append(dict(gamma=gamma,radius_ratio=a,temperature_ratio=1+h,
                            density_ratio=a**(-3),density_from_temperature=(1+h)**(1/(gamma-1))))
    kb=1.380649e-23;m0=3.34e-27;T0=1e6;v0=1e6;a=.02
    shell_ratio=(1-a)**(-3)-1
    delta=m0*v0*v0*shell_ratio/(6*kb);thin=m0*v0*v0*3*a/(6*kb)
    numerical=dict(deltaT=delta,T1=T0+delta,n1_over_n0=(1+delta/T0)**1.5,
                   final_radius_over_full_radius=(1-a)/math.sqrt(1+delta/T0),thin_deltaT=thin,
                   thin_final_temperature_relative_underestimate=1-(T0+thin)/(T0+delta),
                   speed_for_density_ratio_8=math.sqrt(18*kb*T0/(m0*shell_ratio)))
    files=['scripts/verify_question_06.py']
    files += [f for f in ['drafts/question-06.md','figures/题06_图稿源文件.tex'] if (ROOT/f).exists()]
    complete=(ROOT/'drafts/question-06.md').exists()
    if complete:
        draft=(ROOT/'drafts/question-06.md').read_text()
        assert len([line for line in draft.splitlines() if line.startswith('## ')])==9 and 'DRAFT' not in draft
    report=dict(question=6,verified_math=True,document_complete=complete,geometry=geometry,
                small_alpha_series=str(series),shell_dynamics=dynamics,general_gamma=general,numerical_variants=numerical,
                source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    (ROOT/'build'/('verification-q06.json' if complete else 'verification-q06-preliminary.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
