"""第3题多匝主阶连续模型核验；正文及实际PDF审读另以当前校验和记录。"""
from pathlib import Path
import hashlib,json,math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
def main():
    x,L,M,R,g,v0=sp.symbols('x L M R g v0',positive=True)
    s=L-x;lam=M/L
    remaining=sp.symbols('remaining',positive=True)
    def S(expr):
        # sqrt(s)*sqrt(1/s)=1只在实际s>0域内化简，不对x>=L偷用实根。
        return sp.simplify(expr.subs(x,L-remaining)).subs(remaining,L-x)
    r=R*sp.sqrt(s/L);mass=lam*s
    v=v0*sp.sqrt(L/s)
    accel=S(v*sp.diff(v,x))
    U=mass*g*r
    hold=S(-sp.diff(U,x).subs(x,0))
    assert hold==3*M*g*R/(2*L)
    kinetic=S(sp.Rational(3,4)*mass*v*v)
    assert S(kinetic-sp.Rational(3,4)*M*v0*v0)==0
    first_x=M*(x-x*x/(2*L))
    first_y=mass*r
    Px=S(sp.diff(first_x,x)*v)
    Py=S(sp.diff(first_y,x)*v)
    friction=S(sp.diff(Px,x)*v)
    normal_total=S(M*g+sp.diff(Py,x)*v)
    normal_coil=S(normal_total-lam*x*g)
    assert S(Px-mass*v)==0
    assert S(Py+sp.Rational(3,2)*lam*r*v)==0
    assert S(friction+M*v0*v0/(2*s))==0
    assert S(normal_coil-mass*g)==0
    # 逆时针物理角动量为正，x是向左位移，故公转项r*Px-x*Py。
    spin=S(mass*r*v/2)
    angular=S(spin+r*Px-x*Py)
    torque=S(x*(mass*g-normal_coil))
    assert S(angular-sp.Rational(3,2)*M*R*v0)==0
    assert S(v*sp.diff(angular,x)-torque)==0
    # 移动圆心作为参考点时，必须保留V_G×P；不是固定铰链。
    moving_correction=S(sp.diff(r,x)*v*Px-v*Py)
    torque_center=S(-r*friction)
    assert S(v*sp.diff(spin,x)-(torque_center-moving_correction))==0
    # 直接忽略竖直动量会与固定O点零外力矩相矛盾，显式检出这个错误。
    incorrect_angular=S(spin+r*Px)
    wrong_derivative=S(v*sp.diff(incorrect_angular,x))
    assert wrong_derivative!=0
    mu=S(-friction/normal_coil)
    assert S(mu-v0*v0*L/(2*g*s*s))==0
    elapsed=2*L/(3*v0)*(1-(s/L)**sp.Rational(3,2))
    assert S(sp.diff(elapsed,x)*v-1)==0
    held=S(-sp.diff(U,x))
    assert S(held-3*M*g*R/(2*L)*sp.sqrt(s/L))==0
    half={x:L/2}
    assert S(spin.subs(half)-M*R*v0/4)==0
    assert S(friction.subs(half)+M*v0*v0/L)==0
    assert S(normal_coil.subs(half)-M*g/2)==0
    d=sp.symbols('d',real=True)
    shifted=S(spin+r*Px-(x-d)*Py)
    assert S(shifted-sp.Rational(3,2)*M*R*v0*(1-d/L))==0
    assert S(v*sp.diff(shifted,x))==0
    numerical=[]
    # 不调用解析速度，独立积分由能量微分得到的主阶牛顿加速度。
    def ode(t,y):return [y[1],y[1]*y[1]/(2*(1-y[0]))]
    def event(t,y):return y[0]-.8
    event.terminal=True;event.direction=1
    sol=solve_ivp(ode,[0,1],[0,1],events=event,method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True,max_step=.004)
    assert abs(sol.y[1,-1]-math.sqrt(5))<1e-11
    expected_time=2/3*(1-.2**1.5)
    assert abs(sol.t[-1]-expected_time)<1e-12
    for z in [0,.2,.5,.8]:
        time=2/3*(1-(1-z)**1.5)
        zz,vv=sol.sol(time);rr=.002*math.sqrt(1-zz);mm=1-zz
        px=mm*vv;py=-1.5*.002*vv*math.sqrt(1-zz)
        lo=.5*mm*rr*vv+rr*px-zz*py
        numerical.append(dict(x=float(zz),speed=float(vv),Px=float(px),Py=float(py),angular_O=float(lo),
                              remaining_turn_lower_estimate=float((1-zz)/(2*math.pi*rr))))
        assert abs(zz-z)<1e-11 and abs(vv-1/math.sqrt(1-z))<1e-11
        assert abs(lo-.003)<1e-13 and abs(py+.003)<1e-13
    # 独立积分空间分布的一阶矩，再用ODE轨迹中心差分检查动量；
    # 不是把解析Px、Py重新代入同一公式自证。
    def moments_at(time):
        xx,vv=sol.sol(time);mm=1-xx;rr=.002*math.sqrt(1-xx)
        density=mm/(math.pi*rr*rr)
        disk_x=quad(lambda u:quad(lambda ang:(xx+u*math.cos(ang))*density*u,
                    0,2*math.pi,epsabs=1e-12)[0],0,rr,epsabs=1e-12)[0]
        disk_y=quad(lambda u:quad(lambda ang:(rr+u*math.sin(ang))*density*u,
                    0,2*math.pi,epsabs=1e-12)[0],0,rr,epsabs=1e-12)[0]
        tail_x=quad(lambda position:position,0,xx,epsabs=1e-12)[0]
        return np.array([disk_x+tail_x,disk_y])
    finite_difference=[]
    for z in [.2,.5,.75]:
        time=2/3*(1-(1-z)**1.5);h=1e-5
        mid=moments_at(time);plus=moments_at(time+h);minus=moments_at(time-h)
        momentum=(plus-minus)/(2*h);force=(plus-2*mid+minus)/(h*h)
        expected_p=np.array([math.sqrt(1-z),-.003])
        expected_force=np.array([-1/(2*(1-z)),0.])
        assert np.max(abs(momentum-expected_p))<2e-8
        assert np.max(abs(force-expected_force))<3e-6
        finite_difference.append(dict(x=z,momentum=momentum.tolist(),net_force=force.tolist(),
                                      momentum_error=float(np.max(abs(momentum-expected_p))),
                                      force_error=float(np.max(abs(force-expected_force)))))
    expr={k:sp.sstr(z) for k,z in dict(radius=r,mass=mass,speed=v,acceleration=accel,
                  initial_holding_force=hold,Px=Px,Py=Py,ground_friction_left_positive=friction,
                  normal_coil=normal_coil,spin=spin,angular_O=angular,torque_O=torque,
                  moving_center_correction=moving_correction,wrong_zero_Py_derivative=wrong_derivative,
                  minimum_mu_at_x=mu,elapsed_time=elapsed,quasistatic_holding=held,
                  shifted_fixed_origin_angular=shifted).items()}
    sources=['scripts/verify_question_03.py']
    complete=False
    draft=ROOT/'drafts/question-03.md'
    if draft.exists():
        sources.append('drafts/question-03.md')
        complete='<!-- question-complete -->' in draft.read_text()
    note=ROOT/'drafts/question-03-核验备忘.md'
    if note.exists():sources.append('drafts/question-03-核验备忘.md')
    fig=ROOT/'figures/题03_图稿源文件.tex'
    if fig.exists():sources.append('figures/题03_图稿源文件.tex')
    result=dict(question=3,verified_math=True,document_complete=complete,
        scope='多匝主阶模型；不等于有限线径、重力动力修正及末端展开的精确解',
        coordinates='x positive to left; y upwards; physical angular momentum counterclockwise positive',
        expressions=expr,numerical=numerical,spatial_integral_finite_difference=finite_difference,
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources})
    (ROOT/'build').mkdir(exist_ok=True)
    path=ROOT/'build'/('verification-q03.json' if complete else 'verification-q03-preliminary.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
