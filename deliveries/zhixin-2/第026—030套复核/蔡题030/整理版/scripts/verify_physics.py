"""第030套独立数值核验，从动力学、边值与四动量重建结果。"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad,solve_ivp,solve_bvp
from scipy.optimize import brentq,minimize_scalar
from scipy.special import ellipk

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'build'
def close(a,b,rtol=2e-7,atol=2e-9):
    assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
def save(q,method,checks,limitations=None):
    data=dict(status='pass',method=method,checks=checks)
    if limitations:data['model_limitations']=limitations
    (DEST/f'question{q:02}-verification.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(f'第{q}题通过：{method}',flush=True)

def q1():
    mu,R,b=1.,1.,.4
    va=np.sqrt(2*mu*b/(R*(R+b)))
    # 直接积分日心牛顿方程，以 y=0 再穿越事件确定近日点时间。
    def rhs(t,z):
        x=z[:2];return np.r_[z[2:],-mu*x/np.linalg.norm(x)**3]
    def event(t,z):return z[1] if t>1e-5 else 1.
    event.terminal=True;event.direction=-1
    sol=solve_ivp(rhs,(0,10),[R,0,0,va],events=event,rtol=2e-11,atol=2e-12,max_step=.01)
    time=sol.t_events[0][0];end=sol.y_events[0][0]
    close(np.linalg.norm(end[:2]),b);close(time,np.pi*np.sqrt(((R+b)/2)**3/mu))
    vp=np.linalg.norm(end[2:]);vm=np.sqrt(mu/b);relative=vp-vm
    angles=np.linspace(0,2*np.pi,1001)
    tangent=vm+relative*np.cos(angles)
    assert tangent.min()>0
    # 在包含径向速度的可达域中独立数值最小化地球速度改变量。
    VE=np.sqrt(mu/R);A=R*R/(b*b)-1;C=2*mu*(1/b-1/R)
    result=minimize_scalar(lambda w:max(0,A*w*w-C)+(w-VE)**2,bounds=(0,2),method='bounded',options={'xatol':1e-13})
    close(result.x,va,rtol=1e-7)
    save(1,'日心轨道ODE、近日点事件求根、含径向速度的约束最小化及散射速度圆',dict(transfer_time=time,perihelion_radius=float(np.linalg.norm(end[:2])),perihelion_speed=vp,mercury_speed=vm,minimal_tangential_speed=float(result.x),minimum_scattered_tangent=float(tangent.min())),
         '拼接圆锥及单次点火模型；进入水星轨道不自动保证与水星交会。')

def q2():
    R,r,D,rho0,rho=.8,.27,.018,.05,3.4
    rho1=.56*rho;MA,MC,MB=.056,.044,.100
    close(MA/rho1,MB/rho)
    grid=np.linspace(r,R,80)
    sol=solve_bvp(lambda x,y:np.array([y[1],-2*y[1]/x]),lambda a,b:np.array([a[0],b[0]-rho0]),grid,np.array([rho0*(grid-r)/(R-r),np.ones_like(grid)*rho0/(R-r)]),tol=1e-9,max_nodes=6000)
    assert sol.success
    x=np.linspace(r,R,41);massflux=4*np.pi*x*x*D*sol.sol(x)[1]
    close(massflux,np.ones_like(x)*4*np.pi*D*rho0/(1/r-1/R),rtol=3e-7)
    ninit=4*np.pi*R**3*rho1/(3*MA)
    K=3*D*rho0*MA/(rho1*MC*R**2)
    def dt_dr(s):
        # 未反应摩尔数对半径的导数 / 当前气体摩尔流量。
        if s==0 or s==R:return 0.
        molflux=4*np.pi*D*rho0/(MC*(1/s-1/R))
        return (4*np.pi*rho1*s*s/MA)/molflux
    total=quad(dt_dr,0,R,epsabs=1e-10)[0]
    close(total,1/(2*K))
    partial=quad(dt_dr,r,R)[0];y=r/R
    close(partial/total,1-3*y*y+2*y**3)
    ks=.07
    finite=quad(lambda s:rho1*MC/(rho0*MA)*((s-s*s/R)/D+1/ks),0,R)[0]
    close(finite,total+rho1*MC*R/(rho0*MA*ks))
    save(2,'球壳浓度边值数值解、各半径通量检查、固体摩尔守恒及时间独立积分',dict(total_time=total,partial_time=partial,conversion=1-y**3,initial_moles=ninit,finite_reaction_time=finite),
         '初始零厚度处为扩散控制模型的奇异极限；有限界面反应变式使其正则化。')

def q3():
    k,m,r0,v0=.7,1.2,.9,.6
    masses=np.array([m,2*m,3*m]);position=np.array([[3*r0,0],[0,np.sqrt(3)*r0],[-r0,0]])
    velocity=np.array([[0,0],[0,v0],[0,0]])
    def rhs(t,z):
        a=z[:6].reshape(3,2);vel=z[6:].reshape(3,2)
        acceleration=np.zeros((3,2))
        for i in range(3):
            for j in range(3):
                if i!=j:acceleration[i]-=k*masses[j]*(a[i]-a[j])
        return np.r_[vel.ravel(),acceleration.ravel()]
    sol=solve_ivp(rhs,(0,2),np.r_[position.ravel(),velocity.ravel()],rtol=1e-11,atol=1e-12,dense_output=True)
    M=masses.sum();w=np.sqrt(k*M);C0=np.sum(masses[:,None]*position,axis=0)/M;Vc=np.sum(masses[:,None]*velocity,axis=0)/M
    maximum=0.
    for t in np.linspace(0,2,31):
        analytic=C0+Vc*t+(position-C0)*np.cos(w*t)+(velocity-Vc)*np.sin(w*t)/w
        direct=sol.sol(t)[:6].reshape(3,2)
        maximum=max(maximum,float(np.max(abs(direct-analytic))));close(direct,analytic)
        close(np.sum(masses[:,None]*direct,axis=0)/M,C0+Vc*t)
    # 二体也由真实两两作用积分，避免仅拿三体表达式自证。
    Mb=2*m;w2=np.sqrt(k*(Mb+m))
    def two(t,z):
        q=z[2:4]-z[:2];return np.r_[z[4:6],z[6:8],k*m*q,-k*Mb*q]
    twosol=solve_ivp(two,(0,1),[0,0,r0,0,0,0,0,v0],rtol=1e-11,atol=1e-12,dense_output=True)
    for t in (.2,.5,1.):
        expected=np.array([r0/3+2*r0*np.cos(w2*t)/3,v0*t/3+2*v0*np.sin(w2*t)/(3*w2)])
        close(twosol.sol(t)[2:4],expected)
    for point in ([.4,.8,0],[2,-3,0],[0,0,.4]):
        q=np.array(point);gravity=-k*(Mb+m)*q;required=-w2*w2*q*np.array([1,1,0])
        close(gravity[:2],required[:2])
        if q[2]==0:close(gravity,required)
        else:assert abs(gravity[2])>0
    save(3,'二体与三体两两牛顿方程独立积分、质心检查及平面内外共转加速度逐分量比较',dict(frequency=w,maximum_position_error=maximum,center_velocity=Vc.tolist(),relative_equilibrium_set='轨道平面的连续集合，非整个三维空间'))

def q4():
    J,mu,B=1.3,.8,2.1
    def period(field,amplitude):
        def ev(t,y):return y[0]
        ev.terminal=True;ev.direction=-1
        sol=solve_ivp(lambda t,y:[y[1],-mu*field*np.sin(y[0])/J],(0,10),[amplitude,0],events=ev,rtol=1e-11,atol=1e-12,max_step=.015)
        return 4*sol.t_events[0][0]
    p0=period(B,.001);p=period(B+.7,.001)
    inferred=.7*p*p/(p0*p0-p*p)
    close(inferred,B,rtol=1e-8)
    amp=.2;full=period(B,amp);exact=4*np.sqrt(J/(mu*B))*ellipk(np.sin(amp/2)**2)
    close(full,exact)
    save(4,'非线性磁矩摆动ODE的过零周期、周期比反演及有限振幅积分核验',dict(period=p0,added_field_period=p,inferred_field=inferred,finite_amplitude_period=full,elliptic_integral_period=exact),
         '磁矩同向稳定平衡；测量为该转动自由度中的有效地磁场。')

def q5():
    L0,ur,I0,m,l=.7,4.,1.3,1.1,2.
    a=(ur-1)/l
    def L(x):return L0*(1+a*x)
    def rhs(t,z):
        x,v,I=z;return [v,I*I*L0*a/(2*m),-I*L0*a/L(x)*v]
    def event(t,z):return z[0]-l
    event.terminal=True;event.direction=1
    sol=solve_ivp(rhs,(0,20),[0,0,I0],events=event,rtol=1e-11,atol=1e-12,max_step=.01,dense_output=True)
    time=sol.t_events[0][0];end=sol.y_events[0][0]
    close(end[2],I0/ur);close(end[1],I0*np.sqrt(L0/m*(1-1/ur)))
    for t in np.linspace(0,time,31):
        x,v,I=sol.sol(t);close(L(x)*I,L0*I0);close(.5*m*v*v+.5*L(x)*I*I,.5*L0*I0*I0)
    mechanical=quad(lambda x:(L0*I0/L(x))**2*L0*a/2,0,l)[0]
    close(mechanical,.5*m*end[1]**2)
    source=quad(lambda x:I0*I0*L0*a,0,l)[0]
    stored=.5*(L(l)-L0)*I0*I0
    close(source,2*stored)
    save(5,'耦合机械运动与可变电感电流ODE、磁链/总能量逐时刻检查及恒流电源功积分',dict(full_insertion_time=time,final_velocity=float(end[1]),final_current=float(end[2]),mechanical_work=mechanical,constant_current_source_work=source),
         '长螺线管分段电感、线性磁介质及无损耗近似；局部入口力不作精确端部场解释。')

def q6():
    f,D,u,limit,lam=.05,.01,2.,20e-6,550e-9
    v=f*u/(u-f)
    # 直接计算每一物点最佳像面的上下边缘光线，再截在固定感光面。
    def blur(obj):
        vp=1/(1/f-1/obj)
        top=D/2*(1-v/vp);bottom=-D/2*(1-v/vp)
        return abs(top-bottom)
    near=brentq(lambda obj:blur(obj)-limit,f*1.01,u)
    far=brentq(lambda obj:blur(obj)-limit,u,20.)
    q=limit*(u-f)/(D*f)
    close(near,u/(1+q));close(far,u/(1-q))
    span=far-near;close(span,2*u*q/(1-q*q))
    S=np.pi*(1.22*f*lam/D)**2;gain=(np.pi*D*D/(4*S))**.25
    close(gain,D/np.sqrt(2.44*f*lam))
    geom=2*u*(u-f)*limit/(f*D)
    save(6,'上下边缘光线直接截取感光面与近远界独立求根、功率面积比及直径系数检查',dict(near=near,far=far,depth=span,narrow_depth=geom,diffraction_diameter=2*1.22*f*lam/D,ideal_temperature_gain=gain),
         '模糊圆阈值按直径；聚光温度采用点光源及相同吸放热面积的理想模型，非实际扩展太阳精确温度。')

def sphere_images(R,r,l):
    # 交替球反演同时修复外球与有限内电极两条边界。
    inside=[(1.,l)];outside=[]
    current,pos=inside[0]
    for count in range(200):
        ext=-R/pos*current;extpos=R*R/pos;outside.append((ext,extpos))
        next_current=-r/abs(extpos-l)*ext
        next_pos=l+r*r*(extpos-l)/abs(extpos-l)**2
        if abs(next_current)<1e-17:break
        inside.append((next_current,next_pos));current,pos=next_current,next_pos
    sources=inside+outside
    def potential(x,y):
        return sum(q/np.sqrt((x-p)**2+y*y) for q,p in sources)
    for theta in np.linspace(0,np.pi,51):
        close(potential(R*np.cos(theta),R*np.sin(theta)),0,atol=2e-10)
        close(potential(l+r*np.cos(theta),r*np.sin(theta)),1/r,rtol=2e-10)
    return 1/(r*sum(q for q,p in inside)),len(sources)

def q7():
    R,r,rho,I=1.,.01,2.7,.8
    voltage=quad(lambda x:rho*I/(4*np.pi*x*x),r,R)[0]
    power=quad(lambda x:rho*(I/(4*np.pi*x*x))**2*4*np.pi*x*x,r,R)[0]
    resistance=rho/(4*np.pi)*(1/r-1/R)
    close(voltage/I,resistance);close(power,I*I*resistance)
    samples=[]
    for l in (.08,.2,.4):
        exact,count=sphere_images(R,r,l)
        approximate=1/r-R/(R*R-l*l)
        close(exact,approximate,rtol=5e-7)
        assert exact<1/r-1/R
        samples.append(dict(offset=l,normalized_exact_resistance=exact,small_electrode_approximation=approximate,image_sources=count))
    save(7,'同心场强/焦耳热独立积分及交替球反演的有限电极边值数值解',dict(concentric_resistance=resistance,offcenter_samples=samples),
         '一个镜像的主答案只为小电极、远离球壳边界的近似；有限电极以多镜像交叉核验。')

def q8():
    q=.1;eta=np.arcsinh(q);beta=np.tanh(eta)
    ratio=np.exp(2*eta);fuel=1-1/ratio
    close(ratio,(1+beta)/(1-beta))
    constant_eta=brentq(lambda x:(np.cosh(x)-1)/x-q,.01,.5)
    assert constant_eta>eta
    constant_fuel=1-np.exp(-2*constant_eta)
    # 有限微小事件完整四动量守恒，不直接重复微分加速度式。
    samples=[]
    for b in (.1,.6,.9):
        gam=1/np.sqrt(1-b*b);M=2.;density=.003;S=.7;proper_dt=1e-5
        dm=gam*density*S*b*proper_dt
        A=M+gam*dm;P=-gam*b*dm;Mf=M-dm
        photon=(A*A-P*P-Mf*Mf)/(2*(A+P))
        final_beta_local=(P+photon)/(A-photon)
        final_beta_lab=(b+final_beta_local)/(1+b*final_beta_local)
        accel=(final_beta_lab-b)/(gam*proper_dt)
        expected=density*S*b/(M*gam*gam)*(1+gam*(1-b))
        close(accel,expected,rtol=3e-5,atol=2e-9)
        Elab=gam*(1-b)*photon;gfinal=1/np.sqrt(1-final_beta_lab**2)
        close(gam*M+dm,gfinal*Mf+Elab,rtol=1e-12)
        close(gam*M*b,gfinal*Mf*final_beta_lab-Elab,rtol=1e-12)
        samples.append(dict(beta=b,finite_event_acceleration=accel,differential_maximum=expected))
    save(8,'有限光子发射四动量、质量比两次推进、恒固有加速变式求根及收集湮灭有限事件核验',dict(cruise_beta=beta,peak_rapidity=eta,minimum_mass_ratio=ratio,total_fuel_fraction=fuel,antimatter_only_fraction=fuel/2,constant_acceleration_peak_rapidity=constant_eta,constant_acceleration_fuel_fraction=constant_fuel,collection_samples=samples),
         '燃料理论下限为无推力上限的巡航极限；全部湮灭耗材与反物质份额分开。收集加速度为地面坐标加速度。')

if __name__=='__main__':
    DEST.mkdir(exist_ok=True)
    for function in (q1,q2,q3,q4,q5,q6,q7,q8):function()
