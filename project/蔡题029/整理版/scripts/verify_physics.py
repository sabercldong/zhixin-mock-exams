"""第029套独立数值核验；由力、光线、守恒或边值方程复算。"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import minimize,brentq

ROOT=Path(__file__).resolve().parents[1]

def record(q,data):
    data['status']='pass'
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build'/f'question{q:02}-verification.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(q,data,flush=True)

def q1():
    mu,g,l,u,v0=.25,10.,2.,1.,1.5
    om=(2*mu*g/l)**.5;xs=(v0*v0-u*u)/(2*mu*g);A=(xs*xs+u*u/om**2)**.5
    def ev1(t,y):return y[1]-u
    ev1.terminal=True;ev1.direction=-1
    a=solve_ivp(lambda t,y:[y[1],-mu*g],[0,10],[0,v0],events=ev1,rtol=1e-11,atol=1e-12)
    def ev2(t,y):return y[1]+u
    ev2.terminal=True;ev2.direction=-1
    b=solve_ivp(lambda t,y:[y[1],-om*om*y[0]],[0,10],a.y[:,-1],events=ev2,rtol=1e-11,atol=1e-12)
    tnum=a.t[-1]+b.t[-1]+b.y[0,-1]/u
    tformula=(v0-u)/(mu*g)+2/om*np.arccos(xs/A)+xs/u
    assert abs(tnum-tformula)<1e-9
    assert abs(b.y[0,-1]-xs)<1e-9
    vmax=(u*u+2*mu*g*np.sqrt(l*l/4-l*u*u/(2*mu*g)))**.5
    xc=(vmax*vmax-u*u)/(2*mu*g)
    assert abs(np.hypot(xc,u/om)-l/2)<1e-12
    record(1,dict(return_time=tnum,analytic_time=tformula,max_velocity=vmax,
                  conditions='辊面相对速度决定滑动方向；v=-u返程采用可行静摩擦约束。'))

def q2():
    G,m1,m2,r=1.,1.,1.,1.;m3=(104*m1+63*m2)/19
    masses=np.array([m1,m2,m3]);k=G*(m1+m2-5*m3/36)
    def fun(t,y):
        xx=y[:3];acc=np.zeros(3)
        for i in range(3):
            for j in range(3):
                if i!=j:acc[i]+=G*masses[j]*(xx[j]-xx[i])/abs(xx[j]-xx[i])**3
        return np.r_[y[3:],acc]
    # 在奇异碰撞前终止全三体ODE，避免浮点扰动在无穷加速度处放大。
    # 最后0.3%的间距采用独立时间积分补足，并保存比例误差。
    eps=3e-3
    def event(t,y):return y[1]-y[0]-eps
    event.terminal=True;event.direction=-1
    sol=solve_ivp(fun,[0,3],[0,r,3*r,0,0,0],events=event,rtol=1e-12,atol=1e-13,max_step=.005)
    s=sol.y[1]-sol.y[0];ratio=(sol.y[2]-sol.y[1])/s
    assert np.max(abs(ratio-2))<3e-7
    cm=masses@sol.y[:3]/sum(masses);assert np.max(abs(cm-cm[0]))<1e-12
    rem=quad(lambda z:1/np.sqrt(2*k*(1/z-1/r)),0,eps,epsabs=1e-13)[0]
    exact=np.pi*np.sqrt(r**3/(8*k));assert abs(sol.t[-1]+rem-exact)<2e-9
    record(2,dict(m3=m3,kappa=k,collision_time=exact,three_body_time=sol.t[-1]+rem,
                  max_distance_ratio_error=float(max(abs(ratio-2))),max_cm_drift=float(max(abs(cm-cm[0])))))

def q3():
    rng=np.random.default_rng(29);worst=0.
    for mu2,mu3 in rng.uniform(.1,2,(15,2)):
        def F(z):a,b,c=z;return a*a+b*b+a*b
        con=[{'type':'ineq','fun':lambda z:mu2**2-z[0]**2-z[2]**2-z[0]*z[2]},
             {'type':'ineq','fun':lambda z:mu3**2-z[1]**2-z[2]**2-z[1]*z[2]}]
        res=minimize(lambda z:-F(z),[mu2*.7,mu3*.7,0],bounds=[(0,None)]*3,constraints=con,
                     method='SLSQP',options={'ftol':1e-10,'maxiter':500})
        assert res.success
        worst=max(worst,abs(F(res.x)-(mu2**2+mu3**2+mu2*mu3)))
    assert worst<2e-8
    xs=np.linspace(-1/(2*np.sqrt(3)),1/(2*np.sqrt(3)),101)
    ys=-3+np.sqrt(12+3*xs*xs);d1=ys;d2=(1-ys+np.sqrt(3)*xs)/2;d3=(1-ys-np.sqrt(3)*xs)/2
    assert max(abs(d1*d1-d2*d2-d3*d3-d2*d3))<2e-15
    record(3,dict(constrained_maximum_error=worst,boundary_middle_height=float(ys[50]),
                  boundary_interpretation='严格安全区不包括等号临界弧。'))

def q4():
    latent,m,rl,rs,T0=2.4e4,9.,1000.,900.,310.
    dv=m/rl-m/rs;L=m*latent;linear=L/(T0*dv)*(-1)
    numerical=quad(lambda T:L/(T*dv),T0,T0-1,epsabs=1e-8)[0]
    exact=L/dv*np.log((T0-1)/T0)
    assert abs(numerical-exact)<1e-7 and numerical>0
    R,lam,Tstar,pstar=8.314,4.0e4,373.,1e5
    ode=solve_ivp(lambda t,y:[lam*y[0]/(R*t*t)],[Tstar,380],[pstar],rtol=1e-12,atol=1e-8)
    vap=pstar*np.exp(lam/R*(1/Tstar-1/380))
    assert abs(ode.y[0,-1]/vap-1)<1e-11
    record(4,dict(delta_volume=dv,linear_pressure_increment=linear,integrated_pressure_increment=exact,
                  saturation_pressure_ode_error=abs(ode.y[0,-1]/vap-1),
                  model='按题设固液相变模型；T0=310K是人体温度估算；密度按10^3kg/m^3。'))

def q5():
    e,r,R,C=4.,5e4,1.5e5,.002;Ue=e*R/(R+r);tau=r*R/(r+R)*C
    H1,H2=.00743,.001
    qsource=(H1+H2)/e;qcap=np.sqrt(2*C*H2);qR=qsource-qcap
    Uf=qcap/C;tc=-tau*np.log(1-Uf/Ue)
    def f(t,y):
        U=y[0];Is=(e-U)/r;Ir=U/R
        return [(Is-Ir)/C,Is,Ir,Is*Is*r+Ir*Ir*R]
    one=solve_ivp(f,[0,tc],[0,0,0,0],rtol=1e-12,atol=1e-14)
    assert abs(one.y[0,-1]-Uf)<1e-11
    # 题给热量有三位有效数字，允许其舍入范围。
    assert abs(one.y[3,-1]-H1)<5e-6
    a=np.exp(-.1/tau);b=np.exp(-.2/(R*C));lo=Ue*b*(1-a)/(1-a*b);hi=Ue+(lo-Ue)*a
    exactWork=e/r*((e-Ue)*.1+(Ue-lo)*tau*(1-a))
    approxWork=e*e*.1*.3/(r*.3+R*.1)
    loop=solve_ivp(f,[0,.1],[lo,0,0,0],rtol=1e-12,atol=1e-14)
    discharged=loop.y[0,-1]*np.exp(-.2/(R*C))
    assert abs(discharged-lo)<1e-12 and abs(e*loop.y[1,-1]-exactWork)<1e-12
    assert abs(exactWork/approxWork-1)<2e-7
    record(5,dict(total_charge_R=qR,heat_inferred_source_charge=qsource,inferred_closed_time=tc,
                  predicted_heat=one.y[3,-1],steady_voltage_low=lo,steady_voltage_high=hi,
                  periodic_energy_exact=exactWork,periodic_energy_approx=approxWork,
                  model='周期稳态；另保留从初始无电流出发的任意周期递推式。'))

def q6():
    f,h=2.,3.;rad=np.sqrt(h*h-f*f);angles=np.linspace(0,2*np.pi,500)
    xx=h+rad*np.cos(angles);yy=rad*np.sin(angles)
    # 用实际轴坐标X与两条经过薄透镜的光线求交，不重复套牛顿形式。
    X=-f-xx;Y=yy;u=-X
    v=1/(1/f-1/u);Yim=-v/u*Y;x2=v-f
    assert max(abs(x2-f*f/xx))<1e-14
    assert max(abs((x2-h)**2+Yim**2-rad**2))<1e-13
    theta,om=.7,.4;dt=1e-5
    def image(t):
        a=h+rad*np.cos(t);b=rad*np.sin(t);return np.array([f*f/a,-f*b/a])
    fd=(image(theta+om*dt)-image(theta-om*dt))/(2*dt)
    den=h+rad*np.cos(theta)
    analytic=np.array([om*f*f*rad*np.sin(theta)/den**2,-om*f*rad*(h*np.cos(theta)+rad)/den**2])
    assert max(abs(fd-analytic))<1e-10
    f1,f2,h2=2.,3.,4.;r=np.sqrt(h2*h2-f2*f2)
    xx=h2+r*np.cos(angles);yy=r*np.sin(angles)
    # 由不同介质的光线斜率转换求像，再与焦点公式核对。
    n1,n2,P=1.,1.5,.5
    u=f1+xx;vv=n2/(P-n1/u);a=vv-f2;b=-n1*vv/(n2*u)*yy
    assert max(abs(a-f1*f2/xx))<1e-13
    assert max(abs((a-h2*f1/f2)**2+b*b-(r*f1/f2)**2))<1e-13
    record(6,dict(ray_mapping_error=float(max(abs(x2-f*f/(h+rad*np.cos(angles))))),
                  velocity_finite_difference_error=float(max(abs(fd-analytic))),
                  unequal_foci_center=h2*f1/f2,unequal_foci_radius=r*f1/f2,
                  brightness='几何压缩结论需等长物段输入同等光通量；真实有限孔径辐射条件不足时不能唯一判断。'))

def q7():
    M,m,c,v=5.,1.,1.,.6;beta=v/c;gamma=1/np.sqrt(1-beta*beta)
    E=M*c*c/2;p=np.sqrt(E*E/c**2-m*m*c*c);us=p*c*c/E
    angles=np.linspace(-1,1,10001);energy=gamma*(E+v*p*angles)
    px=gamma*(p*angles+v*E/c**2);py=p*np.sqrt(1-angles*angles)
    speed=c*c*np.sqrt(px*px+py*py)/energy
    vmx=(v+us)/(1+v*us/c**2);vmn=abs(v-us)/(1-v*us/c**2)
    assert abs(max(speed)-vmx)<1e-13 and abs(min(speed)-vmn)<1e-13
    assert max(abs(energy**2-c*c*(px*px+py*py)-m*m*c**4))<1e-13
    record(7,dict(rest_speed=us,lab_speed_min=vmn,lab_speed_max=vmx,
                  proof='全角度洛伦兹能量及动量扫描，最小值保留绝对值。'))

def q8():
    q,h,v,A=2.,3.,.4,.7
    def sigma(r,H):return -q*H/(2*np.pi*(r*r+H*H)**1.5)
    maxerr=0.
    for r in [.2,1.,4.,10.]:
        dh=1e-4
        chargeDerivative=quad(lambda z:(sigma(z,h+dh)-sigma(z,h-dh))/(2*dh)*v*2*np.pi*z,0,r,epsabs=1e-11)[0]
        K=-q*v*r/(2*np.pi*(r*r+h*h)**1.5)
        maxerr=max(maxerr,abs(chargeDerivative+2*np.pi*r*K))
    assert maxerr<1e-9
    total=quad(lambda r:2*np.pi*r*r*(-q*v*r/(2*np.pi*(r*r+h*h)**1.5))*A/(r*r),0,np.inf,epsabs=1e-11)[0]
    assert abs(total+q*v*A/h)<1e-12
    induced=quad(lambda r:sigma(r,h)*2*np.pi*r,0,np.inf)[0];assert abs(induced+q)<1e-12
    record(8,dict(total_induced_charge=induced,continuity_residual=maxerr,torque_signed_z=total,
                  torque_magnitude=abs(q*v*A/h),
                  convention='径向向外为电流正向，垂直板向上为力矩正向；q>0上移产生向内常规电流。'))

if __name__=='__main__':
    for f in (q1,q2,q3,q4,q5,q6,q7,q8):f()
