"""第028套独立数值与物理检查；原件无手写答案，不用最终公式重复自证。"""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'build';DEST.mkdir(exist_ok=True)
def save(q,details):
    (DEST/f'question{q:02}-verification.json').write_text(json.dumps(
        dict(status='pass',method='独立数值/物理交叉核验',details=details),ensure_ascii=False,indent=2)+'\n')
    print(f'第{q}题通过',flush=True)
def close(a,b,tol=1e-8):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b)))<tol,(a,b,tol)

# 1：两条初始光线逐段传播，而非再次计算同一个成像公式。
f=.2;F=1.5*f;b=2*f
maxerr=0.
for u in [0,.12,.5,.83,1.1,1.29,1.7,2,5,20]:
    d=u*f;x=f*(u*u+u-3)/(u*u-2.5)
    assert x>0
    def trace(slope):
        h=.001+x*slope
        slope-=h/f;h+=d*slope
        slope+=h/F;h+=d*slope
        slope-=h/f;h+=b*slope
        return h
    error=abs(trace(.0003)-trace(-.0005))
    maxerr=max(maxerr,error)
close(maxerr,0.,1e-12)
tn=brentq(lambda t:t*t+.2*t-.12,0,.3)
td=brentq(lambda t:t*t-.1,.3,.4)
close(tn,.1*(math.sqrt(13)-1));close(td,math.sqrt(.1))
save(1,dict(ray_trace_max_image_difference=maxerr,t_zero_m=tn,t_infinite_m=td,
            source_typo='用户确认像距按2f，不按原件的2v'))

# 2：直接解冲量/滚动线性方程，积分上行轨迹，几何距离与取矩核对。
m=.3;l=1.2;r=.12;g=9.8
t=np.array([.5,math.sqrt(3)/2]);n=np.array([-math.sqrt(3)/2,.5])
H=math.sqrt(3)*l/2-r;omega0=math.sqrt(3*g*H)/r;u=r*omega0
jn=m*math.sqrt(3)*u/2
# 未知[w,Jt,Omega]；切向冲量、角冲量、接触速度三方程
mat=np.array([[m,-1,0],[0,-r,.5*m*r*r],[1,0,r]])
rhs=np.array([m*u/2,-.5*m*r*u,0])
w,jt,om=np.linalg.solve(mat,rhs)
close([w,om],[2*u/3,-2*omega0/3])
close(jt/jn,1/(3*math.sqrt(3)))
acc,fric=np.linalg.solve([[m,-1],[.5*m,1]],[-m*g*math.sqrt(3)/2,0])
s0=r/math.sqrt(3);sstar=l-r/math.sqrt(3)
T=-w/acc
sol=solve_ivp(lambda z,y:[y[1],acc],[0,T],[s0,w],rtol=1e-12,atol=1e-13)
close(sol.y[:, -1],[sstar,0])
A=np.array([l/2,0]);B=A+l*t;O=A+sstar*t+r*n
close(np.linalg.norm(O-(A+sstar*t)),r)
close(np.dot(np.array([-math.sqrt(3)/2,-.5]),O-B),r)
M=m*sstar/l;N=m*g/2
force=-N*n-fric*t
torque_max=0.
for s0i in np.linspace(s0,sstar,101):
    P=s0i*t
    torque=P[0]*force[1]-P[1]*force[0]+M*g*l/2
    assert torque>=-1e-12
    torque_max=max(torque_max,abs(torque) if abs(s0i-sstar)<1e-9 else 0.)
close(torque_max,0,1e-12)
save(2,dict(mu_impulse=jt/jn,mu_rolling=fric/N,omega0=omega0,M_limit=M,
            stopping_contact_s=float(sol.y[0,-1]),max_torque_at_limit=torque_max))

# 3：积分两个质点的实际力学方程；杆内力由约束求出。
errors=[]
for Phi in [1.2,5.]:
    m=1.;k=1.;l=1.;v0=Phi
    def rhs(t,y):
        rvec=y[:2]-y[2:4];vrel=y[4:6]-y[6:8]
        unit=rvec/np.linalg.norm(rvec)
        inward=np.dot(vrel,vrel)/(2*np.linalg.norm(rvec))*unit
        return np.r_[y[4:8],-y[4:6]-inward,-y[6:8]+inward]
    initial=[0,1,0,0,v0,0,0,0]
    ode=solve_ivp(rhs,[0,28],initial,rtol=2e-11,atol=2e-13,dense_output=True,max_step=.02)
    expected=[Phi/2+.5*math.sin(Phi),.5*(1+math.cos(Phi))]
    error=np.max(abs(ode.y[:2,-1]-expected));assert error<1e-8;errors.append(float(error))
    if Phi>math.pi:
        tstar=-math.log(1-math.pi/Phi);state=ode.sol(tstar)
        close(state[:2],[math.pi/2,0],1e-8);close(state[4:6],[0,0],1e-8)
save(3,dict(individual_mass_ODE_final_errors=errors,finite_zero_velocity_condition='Phi>pi；不是系统终态'))

# 4：数值求状态交点并对各段压力积分；只验证明确声明的等摩擦模型。
results=[]
for alpha in [0,.0001,.05,1,10,1000]:
    pplus=lambda u:1.1+alpha*(u-1)
    pminus=lambda u:.9+alpha*(u-1)
    umax=brentq(lambda u:pplus(u)*u-1.5,1,2,xtol=1e-14)
    umin=brentq(lambda u:pminus(u)*u-.5,max(1e-8,1-1/max(alpha,1e-8)),1,xtol=1e-14)
    integral=quad(pplus,umin,umax)[0]+quad(pminus,umax,umin)[0]
    heat=.2*(umax-umin);close(integral,heat,1e-10)
    assert .5<1.5-.2*umax<1.5 and .5<.5+.2*umin<1.5
    results.append(dict(alpha=alpha,umin=umin,umax=umax,normalized_work=integral))
save(4,dict(cycle_results=results,assumption='滑动摩擦等于最大静摩擦；原题单给静摩擦不足以唯一决定循环'))

# 5：直接积分电路—力学耦合系统，并同步积累位移、焦耳热。
m=.2;L=.5;Bl=.3;v0=.8;Omega=Bl/math.sqrt(m*L);Rcrit=2*L*Omega
checks=[]
for R in [0,.08,Rcrit,3*Rcrit]:
    gam=R/(2*L)
    if R==0:tf=20/Omega
    elif gam>Omega:tf=24/(gam-math.sqrt(gam*gam-Omega*Omega))
    else:tf=24/gam
    def eq(t,y):v,I,x,h=y;return [-Bl*I/m,(Bl*v-R*I)/L,v,R*I*I]
    ode=solve_ivp(eq,[0,tf],[v0,0,0,0],rtol=1e-11,atol=1e-13,dense_output=True,max_step=.1/Omega)
    ts=np.linspace(0,min(tf,12/Omega),151)
    if gam<Omega:
        w=math.sqrt(Omega*Omega-gam*gam)
        va=v0*np.exp(-gam*ts)*(np.cos(w*ts)+gam/w*np.sin(w*ts))
    elif abs(gam-Omega)<1e-12:va=v0*np.exp(-gam*ts)*(1+gam*ts)
    else:
        sig=math.sqrt(gam*gam-Omega*Omega)
        va=v0/2*((1+gam/sig)*np.exp((-gam+sig)*ts)+(1-gam/sig)*np.exp((-gam-sig)*ts))
    error=float(max(abs(ode.sol(ts)[0]-va)));assert error<1e-8
    states=ode.y;energy=.5*m*states[0]**2+.5*L*states[1]**2+states[3]
    close(energy,.5*m*v0*v0,2e-9)
    if R>0:close(states[2,-1],m*R*v0/Bl**2,1e-7)
    checks.append(dict(R=R,velocity_error=error,energy_error=float(max(abs(energy-.5*m*v0*v0)))))
save(5,dict(coupled_ODE=checks))

# 6：节点压力线性求解与半球表面压力数值积分。
J=5e-3/60;ra=.015;rc=4e-6;v=J/(math.pi*ra**2);rho=1060
N=(ra/rc)**3;vc=J/(N*math.pi*rc**2)
close(vc/v,rc/ra,1e-12)
def network(gmiddle):
    p1,p2=np.linalg.solve([[1+gmiddle,-gmiddle],[-gmiddle,1+gmiddle]],[1,0])
    return 1-p1
qnormal=network(1);qnarrow=network(1/16);qrestored=network(1/16+15/16)
close(qnarrow/qnormal,1/6);close(qrestored,qnormal)
pressure=2.3;rad=.8
fp=quad(lambda th:pressure*math.cos(th)*2*math.pi*rad**2*math.sin(th),0,math.pi/2)[0]
close(fp,pressure*math.pi*rad**2,1e-12)
pulse_factor=quad(lambda th:(1+.6*math.cos(th))**2,0,2*math.pi)[0]/(2*math.pi)
close(pulse_factor,1+.6**2/2,1e-12)
save(6,dict(J=J,v=v,capillary_number=N,capillary_v=vc,momentum_up_N=2*rho*J*v,
            radius_ratio_equal_length=(15/16)**.25,whole_section_fibre_increase=.44,
            pressure_integral=fp,pulsatile_mean_force_factor=pulse_factor,
            limitations=['总力另需端面压力和液体重量','旁路半径数值以等长度为前提']))

# 7：Lorentz事件、同时测长、固有时及实际光到达的光锥核验。
beta=.6;gam=1/math.sqrt(1-beta*beta);l=1.;c=1.
def boost(event):
    ct,x,y=event
    return np.array([gam*(ct-beta*x),gam*(x-beta*ct),y-l])
a=boost([0,0,0]);d=boost([beta*l,l,0]);close(a[0],d[0]);close(d[1]-a[1],l/gam)
events=[boost([0,0,0]),boost([0,l,0]),boost([0,l,l])]
close([e[0] for e in events],[0,-gam*beta*l,-gam*beta*l])
arrivals=[]
for e in events:
    arrival=e[0]+np.linalg.norm(e[1:]);arrivals.append(float(arrival))
    # 反变换接收事件，与地面发射事件构成零光锥间隔
    ct=gam*arrival;rx=beta*ct;ry=l
    source=([0,0,0],[0,l,0],[0,l,l])[len(arrivals)-1]
    close(ct**2-(rx-source[1])**2-(ry-source[2])**2,0,1e-12)
rel_speed2=beta**2+beta**2/gam**2
close(1/math.sqrt(1-rel_speed2),gam*gam)
save(7,dict(B_length=l/gam,C_length=l,zero_events=[float(e[0]) for e in events],
            photon_arrival_times=arrivals,C_relative_gamma=gam*gam))

# 8：势的有限差分核对内外场；球体体积求积检查远场和多极矩。
R=1.;Q=1.;K=1.;a=.5;q=.125
def sphere_potential(pos,center,rad,charge):
    dist=np.linalg.norm(pos-center)
    return charge/dist if dist>=rad else charge*(3*rad*rad-dist*dist)/(2*rad**3)
center=np.array([0,0,a])
def potential(pos,withq=False):
    ans=sphere_potential(pos,np.zeros(3),1,1)-sphere_potential(pos,center,a,q)
    if withq:ans+=q/np.linalg.norm(pos-center)
    return ans
def numeric_field(pos,withq=False,step=1e-5):
    out=[]
    for j in range(3):
        d=np.eye(3)[j]*step
        out.append(-(potential(pos+d,withq)-potential(pos-d,withq))/(2*step))
    return np.array(out)
def Ez(z):
    if z < -1:return -1/z**2+1/(8*(z-.5)**2)
    if z<0:return z+1/(8*(z-.5)**2)
    if z<=1:return .5
    return 1/z**2-1/(8*(z-.5)**2)
for z in [-3,-1.4,-.8,-.1,.15,.5,.9,1.4,3]:
    close(numeric_field(np.array([0.,0,z])),[0,0,Ez(z)],2e-8)
for x in [-3,-.7,0,.4,2]:
    ex=x if abs(x)<=1 else x/abs(x)**3
    pos=np.array([x,0.,0.])
    electric=numeric_field(pos,True)
    if x==0:
        # 原点是空腔边界，势的一阶导数连续、二阶导数跳变；
        # 中心差分的主误差为O(h)，用两种步长Richardson外推消去，不放宽容差。
        electric=2*numeric_field(pos,True,step=5e-6)-electric
    close(electric,[ex,0,0],2e-8)
zero=brentq(Ez,-1,0)
# 实际三维球体求积，球内坐标以Gauss-Legendre径向与cos极角及均匀方位角生成。
nodes,weights=np.polynomial.legendre.leggauss(20);mus,wm=np.polynomial.legendre.leggauss(24)
phis=np.arange(40)*2*math.pi/40
def cloud(rad,ctr,density):
    radii=(nodes+1)*rad/2;wr=weights*rad/2
    pts=[];wts=[]
    for rr,ww in zip(radii,wr):
        for mu,wi in zip(mus,wm):
            ss=math.sqrt(1-mu*mu)
            for ph in phis:
                pts.append(ctr+rr*np.array([ss*math.cos(ph),ss*math.sin(ph),mu]))
                wts.append(density*rr**2*ww*wi*2*math.pi/len(phis))
    return np.array(pts),np.array(wts)
rho=3/(4*math.pi)
p0,w0=cloud(1,np.zeros(3),rho);ph,wh=cloud(a,center,-rho)
pts=np.r_[p0,ph];wts=np.r_[w0,wh]
close(wts.sum(),7/8,1e-12);close((wts[:,None]*pts).sum(axis=0),[0,0,-1/16],1e-12)
far=[]
for theta in [.2,.9,-.8]:
    er=np.array([math.cos(theta),0,math.sin(theta)])
    residuals=[]
    for rad in [20,40]:
        pos=rad*er;diff=pos-pts;dist=np.linalg.norm(diff,axis=1)
        electric=(wts[:,None]*diff/dist[:,None]**3).sum(axis=0)
        mono=(7/8)*er/rad**2;p=np.array([0,0,-1/16])
        dip=(3*np.dot(p,er)*er-p)/rad**3
        error=np.linalg.norm(electric-mono-dip)/np.linalg.norm(mono)
        assert error<.002
        residuals.append(float(error))
    assert 3.5<residuals[0]/residuals[1]<4.5
    far.append(dict(theta=theta,relative_second_order_errors=residuals))
save(8,dict(z_zero=zero,charge_integral=float(wts.sum()),
            dipole_integral=(wts[:,None]*pts).sum(axis=0).tolist(),farfield_volume_quadrature=far))
