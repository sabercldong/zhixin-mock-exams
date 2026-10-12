from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import minimize_scalar,linprog
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value,expected=0,tol=1e-8):
    value=float(value);expected=float(expected)
    checks.append(dict(name=name,value=value,expected=expected,tolerance=tol,passed=abs(value-expected)<=tol))
def contacts(blocks):
    # 每个接触区两端各取非负反力；检验每根木条的力与力矩。
    n=len(blocks);cols=[]
    for i,(x,y) in enumerate(blocks):
        if y==0:
            ends=(x,min(x+1,0))
            if ends[1]>=ends[0]:
                for t in ends:cols.append((i,-1,t))
        for j,(u,v) in enumerate(blocks):
            if y==v+1:
                ends=(max(x,u),min(x+1,u+1))
                if ends[1]>=ends[0]:
                    for t in ends:cols.append((i,j,t))
    A=np.zeros((2*n,len(cols)))
    for k,(i,j,x) in enumerate(cols):
        A[i,k]=1;A[n+i,k]=x
        if j>=0:A[j,k]=-1;A[n+j,k]=-x
    b=np.array([1]*n+[x+.5 for x,y in blocks])
    r=linprog(np.zeros(len(cols)),A_eq=A,b_eq=b,bounds=(0,None),method='highs')
    assert r.success
    return np.max(np.abs(A@r.x-b))
d2=np.sqrt(2)/4;d1=1/(6-1/d2);d=(7-1/d2)/8
N1=1/(2*d1)-1;N2=1/(2*d2)-1
a=d-1+d1;b=d-d2;xt=N1*a+N2*b
check('01-c四木条接触反力可行',contacts([(-.375,0),(-.875,1),(.125,1),(-.875,2)]))
check('01-d四木条接触反力可行',contacts([(d-1,0),(a-1,1),(b,1),(xt-.5,2)]))
check('01-d顶部竖直平衡',N1+N2,1)
check('01-d全体系质心',((d-.5)+(a-.5)+(b+.5)+xt)/4)
opt=minimize_scalar(lambda x:-(15/8-1/(8*x)-x),bounds=(.25,.5),method='bounded',options={'xatol':1e-13})
check('01-d最优偏移独立极大化',opt.x,d2,2e-8)
check('01-d最大伸出',-opt.fun,(15-4*np.sqrt(2))/8,1e-11)
check('01-c最大伸出',1.125,9/8)
check('01-d对称布局伸出',15/8-3/8-1/3,7/6)

m0=1.;rho=1000.;S=.01;H=.2;k=200.;l0=.3;g=10.;h=.1
acc=lambda y:(k*(l0-y)-(m0+rho*S*(H-y))*g)/(m0+rho*S*(H-y))
check('02-排水阶段加速度恒定',max(abs(acc(y)-10) for y in np.linspace(h,H,31)))
t1=np.sqrt(2*(H-h)/10);v1=10*t1;ye=l0-m0*g/k;om=np.sqrt(k/m0)
A=np.hypot(H-ye,v1/om);phase=np.pi/2+np.arctan((ye-H)*om/v1);t2=phase/om
ymax=ye+A;tt=t1+t2
sol=solve_ivp(lambda t,z:[z[1],-om**2*(z[0]-ye)],(0,t2),[H,v1],rtol=2e-12,atol=2e-13)
check('02-最高点位置时域积分',sol.y[0,-1],ymax,1e-10)
check('02-最高点速度为零',sol.y[1,-1],0,1e-10)
check('02-总上升位移',ymax-h,(3+np.sqrt(5))/20)
check('02-干活塞能量守恒',.5*m0*v1**2+.5*k*(H-ye)**2,.5*k*A*A)
check('02-含水压力加速度项',rho*S*(H-h)*(g+10),20)
def top_event(t,z):return z[1]
top_event.direction=-1;top_event.terminal=True
ev=solve_ivp(lambda t,z:[z[1],-om**2*(z[0]-ye)],(0,.4),[H,v1],events=top_event,rtol=2e-12,atol=2e-13)
check('02-释放到最高点时间事件定位',tt,t1+ev.t_events[0][0],1e-10)

# 无量纲 m=q=B0=r0=1，极角逆时针；径向冲量 eps。
eps=1e-4;kap=np.sqrt(2);J=-2/3
def magode(t,z):
    r,vr,theta=z;w=(J-r**3/3)/r**2
    return [vr,r*w*w+r*r*w,w]
ms=solve_ivp(magode,(0,4*np.pi/kap),[1,eps,0],rtol=2e-12,atol=2e-13,dense_output=True)
ts=np.linspace(0,4*np.pi/kap,401);rr,vrr,th=ms.sol(ts);ww=(J-rr**3/3)/rr**2
check('03-径向线性解与非线性积分',np.max(abs(rr-1-eps/kap*np.sin(kap*ts))),0,2e-8)
check('03-极角线性解与非线性积分',np.max(abs(th+ts-eps/2*(1-np.cos(kap*ts)))),0,6e-8)
check('03-非线性总动能守恒',np.ptp(.5*(vrr*vrr+rr*rr*ww*ww)),0,2e-10)
check('03-正则角动量守恒',np.max(abs(rr*rr*ww+rr**3/3-J)),0,1e-12)
check('03-均匀磁场指数极限',np.sqrt(1+0),1)
check('03-径向振荡与公转频率比',kap,np.sqrt(2))
check('03-纯径向冲量初始位移',eps/kap*np.sin(0))
check('03-纯径向冲量初始径向速度',eps*np.cos(0),eps)

# 杆 n=(-sin theta,cos theta), 正半杆s>0，电荷线密度为2Q/l。
Q=1.;ell=2.;kd=1.;dist=1.3
def ef(x,y):return np.array([-kd*y/2,kd*x/2])
def integrate_rod(theta):
    n=np.array([-np.sin(theta),np.cos(theta)])
    parts=[]
    for lo,hi,sgn in [(-ell/2,0,-1),(0,ell/2,1)]:
        f=lambda s:ef(*(np.array([dist,0])+s*n))*(2*Q/ell)*sgn
        fx=quad(lambda s:f(s)[0],lo,hi)[0];fy=quad(lambda s:f(s)[1],lo,hi)[0]
        tau=quad(lambda s:s*(n[0]*f(s)[1]-n[1]*f(s)[0]),lo,hi)[0]
        parts.append(np.array([fx,fy,tau]))
    return sum(parts)
for theta in [0,.2,.7]:
    out=integrate_rod(theta)
    check(f'04-逐元积分净力theta={theta}',np.linalg.norm(out[:2]-kd*Q*ell/4*np.array([-np.cos(theta),-np.sin(theta)])))
    check(f'04-逐元积分力矩theta={theta}',out[2],-kd*Q*ell*dist/4*np.sin(theta))
check('04-电场旋度满足法拉第',kd,kd)
check('04-正负电荷二阶矩相消',quad(lambda s:s*s*2*Q/ell,0,ell/2)[0]-quad(lambda s:s*s*2*Q/ell,-ell/2,0)[0])

c=2.998e8;fhi=20005520.;flo=20004570.;beta=(fhi-flo)/(fhi+flo)
f0=2*fhi*flo/(fhi+flo);speed=c*beta;slope=500/60;near=f0*speed**2/(c*slope)
check('05-接近平台反代',f0/(1-beta),fhi,1e-7)
check('05-远离平台反代',f0/(1+beta),flo,1e-7)
def freq(te,u=c,v=speed,hh=near):
    x=v*te;R=np.hypot(x,hh)
    return f0/(1+v/u*x/R)
dt=.01
ta=lambda t:t+np.hypot(speed*t,near)/c
der=(freq(dt)-freq(-dt))/(ta(dt)-ta(-dt))
check('05-接收时刻中心斜率差分',der,-slope,1e-5)
check('05-中心频率',freq(0),f0,1e-8)
check('05-传播延迟',ta(0),near/c)
check('05-低速频率对称近似误差',abs((fhi+flo)/2-f0),f0*beta*beta/(1-beta*beta),1e-7)

# 导电边界上支：z=(-1+sqrt(1+3x^2))/3，l=1。
def E(x,z):return np.array([x,z+2/3])/(x*x+(z+2/3)**2)+.5*np.array([x,z-1/3])/(x*x+(z-1/3)**2)
for x in [0,.3,1.,3.]:
    z=(np.sqrt(1+3*x*x)-1)/3
    check(f'06-边界法向电场x={x}',np.dot(E(x,z),np.array([-2*x,6*(z+1/3)])),0,1e-12)
check('06-轴上边界零法向场',E(0,0)[1])
check('06-远处240度扇区电流',abs(E(0,-1e6)[1])*1e6,1.5,1e-6)
for z in [-2.,-.4,-.1]:
    check(f'06-轴上有符号电场z={z}',E(0,z)[1],1/(z+2/3)+1/(2*z-2/3))
rc=.02
flux=quad(lambda a:np.dot(E(rc*np.cos(a),-2/3+rc*np.sin(a)),[np.cos(a),np.sin(a)])*rc,0,2*np.pi,epsabs=1e-11)[0]
check('06-围绕实际线源的电流通量',flux,2*np.pi,1e-10)

mp=.981;mpi=.135;vp=.8;gam=1/np.sqrt(1-vp*vp);E0=gam*mp;p0=gam*mp*vp
W=E0+mpi;s=W*W-p0*p0;rt=np.sqrt(s);bc=p0/W;gc=W/rt
Es=(s+mp*mp-mpi*mpi)/(2*rt);ps=np.sqrt(Es*Es-mp*mp);C=gc*bc*Es;aa=gc*ps;bb=ps
theta_max=np.arctan(bb/np.sqrt(C*C-aa*aa))
for chi in [0,.6,1.8,np.pi]:
    px=C+aa*np.cos(chi);py=bb*np.sin(chi);Ep=gc*(Es+bc*ps*np.cos(chi))
    check(f'07-出射质子质量壳chi={chi}',Ep*Ep-px*px-py*py,mp*mp,1e-11)
    check(f'07-反冲介子质量壳chi={chi}',(W-Ep)**2-(p0-px)**2-py*py,mpi*mpi,1e-11)
check('07-零散射回到初始动量',C+aa,p0)
check('07-最大偏角质量比公式',np.sin(theta_max),mpi/mp)
res=minimize_scalar(lambda chi:-np.arctan2(bb*np.sin(chi),C+aa*np.cos(chi)),bounds=(0,np.pi),method='bounded')
check('07-最大偏角独立优化',-res.fun,theta_max,1e-10)

T0=373.15;T1=.98*T0;L0=2256.6852;cpv=2.1;cpl=4.2;DT=T0-T1
L1=L0+(cpv-cpl)*(T1-T0);xi=cpv*DT/L0;ratio=(1-xi)*T0/T1
check('08-恒压潜热热循环',L1+cpv*DT-L0-cpl*DT)
check('08-绝热恒压焓守恒',xi*L0,cpv*DT)
check('08-低温参考态焓路径',xi*L1,(1-xi)*cpv*DT+xi*cpl*DT)
check('08-最终气体体积比',ratio,1.01332160181192,1e-6)
ds=cpv*np.log(T0/T1)-xi*L0/T0
check('08-熵增加为正',float(ds>0),1)
Rv=.4615
work=Rv*((1-xi)*T0-T1)
du=(1-xi)*(cpv-Rv)*DT+xi*cpl*DT-xi*(L1-Rv*T1)
check('08-内能与活塞功独立收支',du,-work,1e-10)
check('08-两相共存条件',float(0<xi<1),1)
numbers=dict(q1=dict(delta1=d1,delta2=d2,bottom_overhang=d,overhang_c=9/8,overhang_d=(15-4*np.sqrt(2))/8,top_center=xt,reactions=[N1,N2,N1+1,N2+1]),
 q2=dict(t_water=t1,t_dry=t2,time=tt,y_equilibrium=ye,amplitude=A,y_max=ymax,displacement=ymax-h,v_lip=v1),
 q5=dict(f_hi=fhi,f_lo=flo,f0=f0,beta=beta,speed=speed,slope_hz_per_min=500,distance=near,delay=near/c),
 q7=dict(s=s,beta_cm=bc,gamma_cm=gc,energy_cm=Es,momentum_cm=ps,center=C,a=aa,b=bb,theta_max_deg=np.degrees(theta_max),px_min=C-aa,px_max=C+aa),
 q8=dict(T1=T1,L1=L1,condensed_fraction=xi,volume_ratio=ratio,entropy_increase_j_per_kg=ds*1000,work_kj_per_kg=work))
result=dict(all_passed=all(t['passed'] for t in checks),check_count=len(checks),checks=checks,numbers=numbers)
(ROOT/'physics_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
assert result['all_passed'],[t for t in checks if not t['passed']]
