"""直接镜像电势边界、库仑力、势能有限差分与完整摆ODE交叉核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
ROOT=Path(__file__).resolve().parents[1]
def main():
    S3=float(7*sp.zeta(3)/8);S5=float(31*sp.zeta(5)/32)
    n=np.arange(10000,dtype=float);d=2*n+1
    def force(x):return float(np.sum(d*x/(d*d-x*x)**2))
    def energy(x):return -.5*float(np.sum(x*x/(d*(d*d-x*x))))
    # 全镜像序列位置独立构造，真实电荷x；正像x+4n，负像-x+4n+2。
    ni=np.arange(-2000,2001,dtype=float)
    boundary=[]
    for x in [-.4,0,.35]:
        for X in [-1,1]:
            for transverse in [0,.7,2.]:
                potential=float(np.sum(1/np.sqrt((X-x-4*ni)**2+transverse**2)-1/np.sqrt((X+x-4*ni-2)**2+transverse**2)))
                assert abs(potential)<8e-8
                boundary.append(dict(charge_x=x,plate_x=X,transverse=transverse,residual=potential))
    forces=[]
    for x in [.02,.15,.5,.9]:
        images_neg=-x+4*ni+2;sep=x-images_neg
        direct=float(np.sum(-sep/abs(sep)**3))
        assert abs(direct-force(x))<2e-8
        step=2e-6;gradient=-(energy(x+step)-energy(x-step))/(2*step)
        assert abs(gradient-force(x))<2e-7
        forces.append(dict(x=x,direct_coulomb=direct,pair_sum=force(x),negative_energy_gradient=gradient))
    stiffness=force(1e-5)/1e-5;assert abs(stiffness-S3)<3e-9
    h=.3;chi=.4;kq2=chi/(h*S3);T0=2*math.pi*math.sqrt(h/(1-chi))
    periods=[]
    for amplitude in [.04,.02,.01]:
        def rhs(t,state):
            theta,omega=state;x=h*math.sin(theta)
            return [omega,(kq2*force(x)*math.cos(theta)-math.sin(theta))/h]
        def zero(t,state):return state[0]
        zero.terminal=True;zero.direction=-1
        sol=solve_ivp(rhs,[0,T0],[amplitude,0],events=zero,rtol=3e-11,atol=2e-13)
        assert len(sol.t_events[0])==1
        T=4*float(sol.t_events[0][0]);periods.append(dict(angle_amplitude=amplitude,nonlinear_T=T,linear_T=T0,relative_error=T/T0-1))
    assert abs(periods[-1]['relative_error'])<2e-5
    error_ratios=[abs(periods[i]['relative_error']/periods[i+1]['relative_error']) for i in range(2)]
    assert all(3.9<x<4.1 for x in error_ratios)
    critical=[]
    for hcrit in [.2,.8]:
        x=.001*hcrit;kq=1/(hcrit*S3)
        # U/mg = h(1-sqrt(1-x²/h²))+kq*Uelectric, g=m=l=1。
        actual=hcrit*(-math.expm1(.5*math.log1p(-(x/hcrit)**2)))+kq*energy(x)
        coefficient=1/(8*hcrit**3)-S5/(2*hcrit*S3)
        assert actual*coefficient>0
        assert abs(actual/x**4/coefficient-1)<.004
        critical.append(dict(h_over_l=hcrit,quartic_coefficient=coefficient,sign='stable_quartic' if coefficient>0 else 'unstable_quartic'))
    m,g,h,l,K=.01,9.8,.2,.1,9e9
    qcrit=math.sqrt(m*g*l**3/(h*K*S3));q=.5*qcrit
    Tneutral=2*math.pi*math.sqrt(h/g);Tcharged=2*math.pi/math.sqrt(g/h-K*q*q*S3/(m*l**3))
    assert abs(Tcharged/Tneutral-2/math.sqrt(3))<1e-12
    x,dv=sp.symbols('x d',positive=True)
    pairF=((dv-x)**-2-(dv+x)**-2)/4
    pairU=-x*x/(2*dv*(dv*dv-x*x))
    assert sp.simplify(pairF+sp.diff(pairU,x))==0
    # 临界四次势能积分：变量替换消除端点奇性，再与完整摆方程比较。
    I=quad(lambda v:2/math.sqrt(4-6*v*v+4*v**4-v**6),0,1,epsabs=2e-12)[0]
    assert abs(I-1.31102877714606)<1e-11
    hc=.2;kc=1/(hc*S3);Ac=1/(8*hc**3)-S5/(2*hc*S3)
    linear_tail=S3-float(np.sum(1/d**3))
    nonlinear_critical=[]
    for amplitude in [.003,.0015]:
        theta0=math.asin(amplitude/hc)
        predicted=4*I/amplitude*math.sqrt(1/(2*Ac))
        def critical_rhs(t,state):
            angle,speed=state;xx=hc*math.sin(angle)
            # 临界时线性项抵消，补上已知的线性尾和；未补高阶尾远小于ODE误差。
            return [speed,(kc*(force(xx)+linear_tail*xx)*math.cos(angle)-math.sin(angle))/hc]
        sol=solve_ivp(critical_rhs,[0,predicted],[theta0,0],events=zero,rtol=3e-10,atol=1e-13)
        actualT=4*float(sol.t_events[0][0]);assert abs(actualT/predicted-1)<.001
        nonlinear_critical.append(dict(horizontal_amplitude=amplitude,quartic_T=predicted,full_equation_T=actualT))
    assert abs(nonlinear_critical[1]['full_equation_T']/nonlinear_critical[0]['full_equation_T']/2-1)<.001
    variant_q_ratio=math.sqrt(3)/2;assert abs(1/math.sqrt(1-variant_q_ratio**2)-2)<1e-12
    variant_distance_ratio=math.sqrt((1-.8)/(1-.8/8));assert abs(variant_distance_ratio-math.sqrt(2)/3)<1e-12
    curves=json.loads((ROOT/'build/curve-q02.json').read_text());curve_error=0
    for point in curves['points']:
        u=point['u'];xx=curves['h_over_l']*u
        # 用10000项与图稿4000项独立核对，不复用坐标生成函数。
        gravity=-math.expm1(.5*math.log1p(-u*u))
        val=gravity+point['chi']*energy(xx)/(curves['h_over_l']**2*S3)
        curve_error=max(curve_error,abs(val-point['U_over_mgh']))
    assert curve_error<2e-9
    source=['scripts/verify_question_02.py','scripts/generate_question_02_curve.py','figures/effective-02-coordinates.tex'];draft=ROOT/'drafts/question-02.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():source+=['drafts/question-02.md']
    tikz=ROOT/'figures/题02_图稿源文件.tex'
    if tikz.exists():source+=['figures/题02_图稿源文件.tex']
    result=dict(question=2,verified_math=True,document_complete=complete,S3=S3,S5=S5,
                boundary_potential=boundary,image_forces=forces,small_displacement_stiffness=stiffness,
                nonlinear_periods=periods,error_ratios=error_ratios,critical_quartic=critical,
                critical_h_over_l=.5*math.sqrt(S3/S5),qcrit_C=qcrit,Tneutral_s=Tneutral,Tcharged_s=Tcharged,
                S5_over_S3=S5/S3,critical_brackets={str(a):1-4*a*a*S5/S3 for a in [.2,.8]},
                nonlinear_critical_periods=nonlinear_critical,quartic_integral=I,curve_error=curve_error,
                variants=dict(q_over_qcrit=variant_q_ratio,plate_distance_T_ratio=variant_distance_ratio),
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source})
    (ROOT/'build').mkdir(exist_ok=True)
    filename='verification-q02.json' if complete else 'verification-q02-preliminary.json'
    (ROOT/'build'/filename).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
