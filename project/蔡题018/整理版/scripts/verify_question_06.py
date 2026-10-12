"""自由滑块—预压弹簧：分阶段动量/能量、一般初值及独立ODE核验。"""
from pathlib import Path
import hashlib,json,math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]

def main():
    M,m,g,h,k,x0=sp.symbols('M m g h k x0',positive=True)
    mu=M*m/(M+m)
    u=sp.sqrt(2*g*h*(M+m)/M)
    v=M*u/(M+m);V=m*u/(M+m)
    assert sp.simplify(m*v-M*V)==0
    assert sp.simplify(m*v*v/2+M*V*V/2-m*g*h)==0
    assert sp.simplify(v+V-u)==0
    outgoing=sp.sqrt(v*v+k*x0*x0/m)
    critical_sq=sp.simplify(m/k*((u+V)**2-v*v))
    assert sp.simplify(critical_sq-8*m*m*g*h/(k*M))==0
    # 反弹之后不再有零总动量；质心平动能须扣除。
    recoil_momentum=-m*outgoing-M*V
    relative_energy=sp.simplify(m*outgoing**2/2+M*V**2/2-recoil_momentum**2/(2*(M+m)))
    assert sp.simplify(relative_energy-mu*(outgoing-V)**2/2)==0
    xc=sp.sqrt(critical_sq)
    Wc=sp.simplify(u+V)
    assert sp.simplify(Wc**2-v*v-k*xc**2/m)==0
    omega=sp.sqrt(k/m);time=sp.symbols('time',real=True)
    xi=x0*sp.cos(omega*time)+v/omega*sp.sin(omega*time)
    displacement=xi-x0
    assert sp.simplify(sp.diff(xi,time,2)+omega**2*xi)==0
    assert sp.simplify(xi.subs(time,0)-x0)==0
    assert sp.simplify(sp.diff(xi,time).subs(time,0)-v)==0
    assert sp.simplify(displacement.subs(time,0))==0
    assert sp.simplify(sp.diff(displacement,time).subs(time,0)-v)==0
    # 手写后两问将x0取临界值；只有在该特例下时间仅含质量比。
    ratio=sp.simplify(omega*xc/Wc)
    expected=2*sp.sqrt(m*(M+m))/(M+2*m)
    assert sp.simplify(ratio-expected)==0
    assert sp.simplify((M+2*m)**2-4*m*(M+m)-M**2)==0
    # 独立由两坐标Lagrange方程解加速度，不以高度结果代回自身。
    alpha=sp.symbols('alpha',real=True)
    ax,aq=sp.symbols('ax aq',real=True)
    equations=[(M+m)*ax-m*sp.cos(alpha)*aq,
               m*aq-m*sp.cos(alpha)*ax+m*g*sp.sin(alpha)]
    acceleration=sp.solve(equations,(ax,aq))
    assert sp.trigsimp(acceleration[aq]+g*(M+m)*sp.sin(alpha)/(M+m*sp.sin(alpha)**2))==0
    pc,qdot=sp.symbols('pc qdot',real=True)
    xdot=(pc+m*sp.cos(alpha)*qdot)/(M+m)
    exact_K=(M+m)*xdot**2/2-m*sp.cos(alpha)*xdot*qdot+m*qdot**2/2
    effective_mass=m*(M+m*sp.sin(alpha)**2)/(M+m)
    assert sp.trigsimp(exact_K-pc**2/(2*(M+m))-effective_mass*qdot**2/2)==0
    # 位移Taylor系数及相位冲量积分交叉检查。
    assert sp.simplify(sp.diff(displacement,time,2).subs(time,0)+k*x0/m)==0
    assert sp.simplify(sp.diff(displacement,time,3).subs(time,0)+omega**2*v)==0
    vv_sym,VV_sym=sp.symbols('vv VV',positive=True)
    assert sp.expand((vv_sym+2*VV_sym)**2-vv_sym**2-4*VV_sym*(vv_sym+VV_sym))==0
    rows=[]
    for mass_ratio in [.01,.1,1,10,100]:
        mm=mass_ratio;MM=1.;gg=9.8;hh=.4;kk=30.
        uu=math.sqrt(2*gg*hh*(MM+mm)/MM)
        vv=MM*uu/(MM+mm);VV=mm*uu/(MM+mm)
        xxcrit=math.sqrt(8*mm*mm*gg*hh/(kk*MM));ww=math.sqrt(kk/mm)
        for factor in [0,.5,1,1.5,3]:
            xx=factor*xxcrit;out=math.hypot(vv,ww*xx)
            theta=math.atan2(ww*xx,vv);sep=(math.pi-theta)/ww
            def ode(t,z):return [z[1],-kk*z[0]/mm, -kk*z[0]]
            def release(t,z):return z[0]
            release.direction=-1;release.terminal=True
            sol=solve_ivp(ode,(0,sep*1.01),[xx,vv,0],events=release,
                          method='DOP853',rtol=1e-12,atol=1e-13,max_step=sep/100)
            assert len(sol.t_events[0])==1
            measured=sol.t_events[0][0];end=sol.y_events[0][0]
            assert abs(measured-sep)<1e-9
            assert abs(end[1]+out)<2e-9
            assert abs(end[2]+mm*(vv+out))<1e-8
            energy_error=abs(.5*mm*end[1]**2-(.5*mm*vv**2+.5*kk*xx**2))
            assert energy_error<1e-8
            momentum_after=-mm*out-MM*VV
            assert abs(momentum_after+mm*(vv+out))<1e-9
            relative_climb=out-VV
            catches_wedge=relative_climb>0
            max_height=(MM/(MM+mm))*relative_climb**2/(2*gg) if catches_wedge else None
            # 通过斜面Lagrange质量矩阵与能量守恒独立核对上升高度。
            incline_checks=[]
            if catches_wedge:
                for alpha in [.2,.6,1.0]:
                    sine=math.sin(alpha)
                    metric=mm*(MM+mm*sine*sine)/(MM+mm)
                    qdot=relative_climb*math.sqrt((MM*mm/(MM+mm))/metric)
                    qacc=-gg*sine*(MM+mm)/(MM+mm*sine*sine)
                    peak_from_integrated_acc=-qdot*qdot/(2*qacc)*sine
                    assert abs(peak_from_integrated_acc-max_height)<1e-10
                    incline_checks.append(dict(angle_radians=alpha,peak_height=peak_from_integrated_acc))
            if factor==1:
                assert catches_wedge and abs(max_height-hh)<1e-11
                special_sep=(math.pi-math.asin(2*math.sqrt(mm*(MM+mm))/(MM+2*mm)))/ww
                assert abs(special_sep-sep)<2e-12
            if factor>1:assert catches_wedge and max_height>hh
            # 即便能量充足，方向也必须朝滑块；绝不将负相对速度平方冒充可上坡。
            rows.append(dict(m_over_M=mass_ratio,x0_over_critical=factor,
                             speed_in=vv,wedge_left_speed=VV,speed_out=out,
                             returns_to_wedge=catches_wedge,maximum_height=max_height,
                             clears_crest_strictly=catches_wedge and max_height>hh+1e-10,
                             separation_time=sep,ode_separation_error=measured-sep,
                             ode_outgoing_velocity_error=end[1]+out,energy_error=energy_error,
                             wall_impulse=end[2],total_momentum_after=momentum_after,
                             independent_incline_checks=incline_checks))
    # 四个带解变式；有限间距独立采样并求首次零点。
    mm=MM=1.;gg=9.8;hh=.5;kk=100.;om=10.
    vv=math.sqrt(2*gg*hh*MM/(MM+mm));VV=mm*vv/MM
    xx=math.sqrt(8*mm*mm*gg*hh/(kk*MM))
    ww=vv+2*VV;A=ww/om;theta=math.atan2(om*xx,vv)
    sep=(math.pi-theta)/om
    assert abs(xx-.6260990336999411)<1e-12
    assert abs(A-.6640783086353597)<1e-12
    assert abs(sep-.19106332362490183)<1e-12
    lam=1.5;compression=lam*xx
    out=math.hypot(vv,om*compression)
    sep2=(math.pi-math.atan2(om*compression,vv))/om
    available_height=MM*(out-VV)**2/(2*gg*(MM+mm))
    assert abs(available_height/hh-(5-math.sqrt(19)/2))<1e-12
    gap_minimum=compression-VV*sep2
    gap_reports=[]
    for initial_gap in [.4,.6]:
        def gap(t):return initial_gap+compression*(math.cos(om*t)-1)+vv/om*math.sin(om*t)+VV*t
        sample_minimum=min(gap(sep2*j/1000) for j in range(1001))
        assert abs(sample_minimum-min(initial_gap,initial_gap-gap_minimum))<1e-12
        collision=brentq(gap,0,sep2,xtol=1e-14) if gap(sep2)<0 else None
        newton=[]
        compression_at_collision=None
        if collision is not None:
            assert 0<collision<sep2 and abs(gap(collision))<1e-12
            assert gap(.160)>0 and gap(.162)<0
            t=.160
            for _ in range(2):
                derivative=-om*compression*math.sin(om*t)+vv*math.cos(om*t)+VV
                t=t-gap(t)/derivative
                newton.append(dict(time=t,residual=gap(t)))
            assert abs(t-collision)<1e-10
            compression_at_collision=compression*math.cos(om*collision)+vv/om*math.sin(om*collision)
            assert abs(compression_at_collision-.18226562122928042)<1e-10
        gap_reports.append(dict(D0=initial_gap,end_gap=gap(sep2),sample_minimum=sample_minimum,
                                early_collision_time=collision,newton_iterations=newton,
                                compression_at_collision=compression_at_collision))
    assert .5*((3-1)/(3+1))**2==.125 # M=3m、h=.5的无预压回坡高度。
    files=['scripts/verify_question_06.py','drafts/question-06-核验备忘.md',
           'drafts/question-06.md','figures/题06_图稿源文件.tex']
    complete=(ROOT/'drafts/question-06.md').exists()
    if complete:
        source=(ROOT/'drafts/question-06.md').read_text()
        assert '<!-- question-complete -->' in source
        assert source.count('\n## ')==9
    names=['question-06','velocities-06','contact-06','return-06','phase-06']
    figures={name:hashlib.sha256((ROOT/f'figures/{name}.pdf').read_bytes()).hexdigest()
             for name in names if (ROOT/f'figures/{name}.pdf').exists()}
    complete=complete and len(figures)==5
    report=dict(question=6,verified_math=True,document_complete=complete,set_accepted=False,
                scope='四问与九模块独立核验；工作分题源稿不代表整套验收',
                relative_velocity=str(u),ground_particle_velocity=str(v),
                wedge_velocity='-'+str(V),minimum_compression_squared=str(critical_sq),
                general_spring_coordinate=str(xi),displacement_from_first_contact=str(displacement),
                general_separation_time='sqrt(m/k)*(pi-atan2(sqrt(k/m)*x0,v))',
                interpretation=['第三、四问默认保留一般x0，手写所给质量比时间式是x0=xcrit的特例',
                                '第4问要求位移，须扣除初接触位置；手写X(t)实际为相对自然长端点的位置',
                                '临界压缩给恰能到达峰顶的阈值；严格翻过需大于临界，圆滑峰顶临界可渐近到达',
                                '弹簧接触时墙施外力，整体水平动量不守恒；分离后再上坡才重新守恒',
                                '按题设分阶段运动，分离前不再次碰到滑块；若弹簧过长须额外检查间距'],
                critical_phase_sine=str(ratio),numerical_checks=rows,
                lagrange_q_acceleration=str(acceleration[aq]),
                finite_gap_variant=gap_reports,variants_checked=4,
                figures_sha256=figures,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                               for p in files if (ROOT/p).exists()})
    destination='verification-q06.json' if complete else 'verification-q06-preliminary.json'
    (ROOT/'build'/destination).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=6,verified_math=True,numerical_trajectories=len(rows),
                         max_energy_error=max(v['energy_error'] for v in rows),
                         max_velocity_error=max(abs(v['ode_outgoing_velocity_error']) for v in rows),
                         max_event_time_error=max(abs(v['ode_separation_error']) for v in rows)),ensure_ascii=False))
if __name__=='__main__':main()
