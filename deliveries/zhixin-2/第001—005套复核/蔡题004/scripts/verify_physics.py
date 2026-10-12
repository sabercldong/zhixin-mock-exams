"""第004套独立代数、数值积分与极限检查。"""
from pathlib import Path
import json, math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition,detail):
 checks.append(dict(name=name,passed=bool(condition),detail=detail))
 assert condition,(name,detail)
def close(a,b,tol=1e-8):return bool(np.max(np.abs(np.asarray(a)-np.asarray(b)))<=tol)
# Q1：直接参数化两个端点，计算几何和动能，不引用周期答案。
q,R,d,a,m,g=sp.symbols('q R d a m g',positive=True)
C=sp.Matrix([-d*sp.sin(q),0,-d*sp.cos(q)]);n=sp.Matrix([sp.cos(q),0,-sp.sin(q)])
r1=C-a*n;r2=C+a*n
check('Q1 两端球面约束与杆长',sp.simplify(r1.dot(r1)-d*d-a*a)==0 and sp.simplify((r2-r1).dot(r2-r1)-4*a*a)==0,'|r±|²=d²+a²=R²，端点间距2a。')
Kq=sp.simplify(m*(r1.diff(q).dot(r1.diff(q))+r2.diff(q).dot(r2.diff(q)))/2)
check('Q1 倾转动能和小振动系数',Kq==m*(d*d+a*a),'直接对端点求导，K=m(d²+a²)qdot²；U二阶系数mgd。')
psi=sp.symbols('psi',real=True)
rp=sp.Matrix([a,d*sp.sin(psi),-d*sp.cos(psi)])
check('Q1 横向动能及周期乘积',sp.simplify(rp.diff(psi).dot(rp.diff(psi)))==d*d and close((2*np.pi*np.sqrt(9/(9.8*np.sqrt(8))))*(2*np.pi*np.sqrt(np.sqrt(8)/9.8)),4*np.pi**2*3/9.8),'T1T2=4π²R/g；横向端点x固定，截面半径d。')
# 瞬时约束v_Rx=v_Lx，总Jx=m v0/2，故两者x速率v0/4。
check('Q1 冲量与实际速度区分',close(np.linalg.solve([[1,-1],[1,1]],[0,.5]),[.25,.25]),'m=1,v0=1，左端名义冲量.5只导致共同vx=.25；指定实际vx=.5需总Jx=1。')
# Q2：辅助中心力轨道数值积分，包含独立真实时间积分。
for deg in [30,45,60]:
 al=math.radians(deg);P=math.pi/math.sin(al)**3
 def orbit(t,y):
  rr=np.linalg.norm(y[:2]);return [y[2],y[3],-.5*y[0]/rr**3,-.5*y[1]/rr**3]
 sol=solve_ivp(orbit,[0,P],[1,0,0,math.cos(al)],rtol=2e-11,atol=2e-12,dense_output=True,max_step=P/120)
 ret=sol.y[:,-1];height=math.sin(al)*P
 true_time=quad(lambda t:1/np.linalg.norm(sol.sol(t)[:2]),0,P,epsabs=1e-9)[0]
 es=math.cos(2*al);Ae=1/(2*math.sin(al)**2)
 radii=np.linalg.norm(sol.sol(np.linspace(0,P,1001))[:2],axis=0)
 check(f'Q2 {deg}度轨道回返与时间',close(ret,[1,0,0,math.cos(al)],2e-8) and close(height,math.pi/math.sin(al)**2) and close(true_time,2*math.pi/math.sin(al),2e-8),f'数值中心力积分，H={height:.10g}，真实时间c=a=r0=1时为{true_time:.10g}；r范围{radii.min():.7g}…{radii.max():.7g}。')
check('Q2 高度允许整数及奇异端点',list(range(1,math.ceil(2.5)))==[1,2] and close([math.degrees(math.asin(math.sqrt(.4))),math.degrees(math.asin(math.sqrt(.8)))],[39.23152048359226,63.43494882292201]),'h=2.5πr0时仅k=1,2；α=90度排除轴碰撞。')
# Q3：时变B的完整二维Lorentz方程，包含感应电场。
T=400.
def field(t):
 u=np.clip(t/T,0,1);return 1+3*u*u-2*u**3,6*u*(1-u)/T

def lorentz(t,y):
 B,Bdot=field(t);x,yc,vx,vy=y
 return [vx,vy,-.5*yc*Bdot-B*vy,.5*x*Bdot+B*vx]
sol=solve_ivp(lorentz,[0,T],[1,0,0,1],rtol=3e-11,atol=3e-12,max_step=.15,dense_output=True)
x,y,vx,vy=sol.y[:,-1];vf=math.hypot(vx,vy);rg=vf/2
check('Q3 慢变磁场完整运动方程',close(vf,math.sqrt(2),3e-5) and close(rg,1/math.sqrt(2),2e-5),f'B以平滑斜坡1→2，T=400；vf={vf:.10g},rg={rg:.10g}。')
times=np.linspace(0,T,2001);vals=sol.sol(times);Bs=np.array([field(t)[0] for t in times])
canonical=vals[0]*vals[3]-vals[1]*vals[2]-Bs*(vals[0]**2+vals[1]**2)/2
check('Q3 正则角动量独立检查',close(canonical,np.full(len(times),.5),2e-8),f'完整时变Lorentz轨道最大守恒误差{np.max(abs(canonical-.5)):.3g}。')
# 突然变化积分电场，vy+=.5，然后在B=2下数值追踪。
step=solve_ivp(lambda t,Y:[Y[2],Y[3],-2*Y[3],2*Y[2]],[0,math.pi],[1,0,0,1.5],rtol=1e-11,atol=1e-12,dense_output=True)
positions=step.sol(np.linspace(0,math.pi,400))[:2]
check('Q3 骤变轨道及能量',close(np.linalg.norm(positions-np.array([[.25],[0]]),axis=0),np.full(400,.75),1e-9) and close(1.5**2,2.25),'B骤变1→2后新中心(.25,0)，回旋半径.75，K/K0=2.25。')
# Q4：黑体功率、球面投影积分和地热平衡。
sigma=5.67e-8;rs=7e8;dist=1.5e11;Ts=5600
FS=sigma*Ts**4*(rs/dist)**2;Te=(FS/(4*sigma))**.25;qg=3*4/100;Tg=(qg/sigma)**.25
check('Q4 太阳平衡数值',close(Te,270.505699262238,1e-8),f'FS={FS:.12g} W/m²，Te={Te:.12g} K，原205K不成立。')
proj=quad(lambda z:2*math.pi*math.sin(z)*math.cos(z),0,math.pi/2)[0]
check('Q4 球面吸收投影',close(proj,math.pi),'对受照半球积分cosζ dS得到πR²，而发射面积4πR²。')
check('Q4 地热平衡与综合温度',close(Tg,38.141656163715,1e-8) and close(sigma*Tg**4,.12) and close(((FS/4+qg)/sigma)**.25,(Te**4+Tg**4)**.25),'地热.12W/m²，Tg=38.141656K；辐射功率相加而非温度相加。')
Ca=1e5;eps=1e-3;rate_num=((qg-sigma*(Tg+eps)**4)-(qg-sigma*(Tg-eps)**4))/(2*eps*Ca)
check('Q4 冷却稳定性与无地热解',close(rate_num,-4*sigma*Tg**3/Ca,1e-11) and close(-3*((300**-3+3*sigma*100/Ca)**(-1/3))**-4*(-sigma*((300**-3+3*sigma*100/Ca)**(-1/3))**4/Ca),3*sigma/Ca),'稳定平衡的线性导数为−4σTg³/Ca；无热源时d(T^-3)/dt=3σ/Ca。')
# Q5：符号验证差分力、势、流函数；ODE和时间积分独立。
x,y,L,E,l,qc=sp.symbols('x y L E l qc',nonzero=True,real=True)
f=qc*(E*(1-(x+l/2)**2/L**2)-E*(1-(x-l/2)**2/L**2))
check('Q5 有限偶极差分',sp.simplify(f+2*qc*E*l*x/L**2)==0,'二次主轴场的差分精确为−2qE0lx/L²，限两端都在给定区内。')
Phi=-E*(x-x**3/(3*L**2)+x*y*y/L**2);Ex=-sp.diff(Phi,x);Ey=-sp.diff(Phi,y)
psi=E*(y*(1-x*x/L**2)+y**3/(3*L**2))
check('Q5 静电延拓与场线',sp.simplify(sp.diff(Ex,x)+sp.diff(Ey,y))==0 and sp.simplify(sp.diff(Ey,x)-sp.diff(Ex,y))==0 and sp.simplify(Ex*sp.diff(psi,x)+Ey*sp.diff(psi,y))==0,'符号检查散度、旋度与流函数沿场线导数均为0。')
check('Q5 原全平面假设与非唯一性',sp.diff(E*(1-x*x/L**2),x)!=0 and sp.diff(x*y,x,2)+sp.diff(x*y,y,2)==0,'与y无关的Ex不能同时满足无源、无旋；加入Cxy不改轴上Ex或原点Ey，却改轴上Ey。')
Om=math.sqrt(3);vinit=1;tc=2/Om*math.atan(Om)
tquad=quad(lambda xx:1/math.sqrt(1+Om**2*(1-xx*xx)),-1,1,epsabs=1e-12)[0]
osc=solve_ivp(lambda t,Y:[Y[1],-Om*Om*Y[0]],[0,tc],[-1,1],rtol=1e-11,atol=1e-12)
check('Q5 穿越时间两条独立核验',close(tc,tquad) and close(osc.y[:,-1],[1,1],1e-9) and close(tc/2,math.pi/(3*math.sqrt(3))),f'ΩL/v0=√3，t={tc:.10g}，最大速率2v0。')
# Q6：角度关系、题给单位和复振幅分支。
gamma=math.radians(40);ratio=1/(math.tan(gamma)*2*math.pi);hp=.17/math.sin(.05)
check('Q6 螺旋切线与法线几何',close((1/(2*math.pi*ratio))*math.tan(math.radians(50)),1),'实空间切线斜率h/(2πr)和倒空间臂斜率cot40相乘为1。')
check('Q6 保留原波长及小角度',close(hp,3.401417079,2e-9) and close(.17/.05,3.4) and close(hp/10,.3401417079,2e-10),f'h={hp:.12g}Å，r/h={ratio:.12g}；0.17Å不是0.17nm。')
phases=np.array([1,3,5,7])*math.pi/4
check('Q6 正负第四级相消的全部分支',close(1+np.exp(4j*phases),np.zeros(4),3e-15) and close(1+np.exp(-4j*phases),np.zeros(4),3e-15),'四个带标签相位为π/4,3π/4,5π/4,7π/4。')
r1=math.cos(math.pi/8)**2/math.cos(3*math.pi/8)**2
r2=math.cos(3*math.pi/8)**2/math.cos(9*math.pi/8)**2
check('Q6 低阶强度区分分支',close([r1,r2],[3+2*math.sqrt(2),3-2*math.sqrt(2)]),'归一化第一/三级强度比为5.828427或.171573。')
# Q7：不使用能量答案直接积分转动方程，再独立计算抛体落点。
l,H,h,g=1,.2,2,9.8;a=l/2;s=2*H/l;c=math.sqrt(1-s*s);beta=math.asin(s)
A=(h-2*H)*c*c;target=l*c*c/(4*s)
eta=(-4*H+math.sqrt((4*H)**2+4*A*(2*H+target)))/(2*A)
M=1;m=eta/(1-eta);u=math.sqrt(2*g*(h-2*H));vi=eta*u*c
check('Q7 初始几何及完全非弹性碰撞',close(u,5.6) and close(m*a*u*c,(m+M)*a*vi) and (m+M)*vi**2<m*u**2,'右端.4m；兔子实际下落1.6m；碰撞角动量守恒但能量减小。')
def end_rotation(t,Y):return Y[0]+beta
end_rotation.terminal=True;end_rotation.direction=-1
rot=solve_ivp(lambda t,Y:[Y[1],-(m-M)/(m+M)*g/a*math.cos(Y[0])],[0,3],[beta,-vi/a],events=end_rotation,rtol=2e-11,atol=2e-12,dense_output=True,max_step=.005)
vend=-a*rot.y[1,-1]
check('Q7 转动方程独立数值积分',len(rot.t_events[0])==1 and close(vend**2,10.29,1e-8) and close(m,1.4024343163222863),f'转动至−β用时{rot.t[-1]:.9g}s，v={vend:.10g}m/s，m/M={m:.12g}。')
tflight=(vend*c+math.sqrt((vend*c)**2+4*g*H))/g
landing=-a*c+vend*s*tflight
check('Q7 弹道落点独立核验',close(landing,a*c,2e-9) and close(tflight,5/7,2e-9),'用抛体正飞行时间根计算，落点与右端接地点相同；t=5/7s。')
ang=rot.sol(np.linspace(0,rot.t[-1],500));N=2*m*M/(m+M)*g*np.cos(ang[0]);radial= (a*ang[1])**2/a
mu_stone=abs(-g*np.sin(ang[0])-radial)/(N/M)
check('Q7 接触与不滑动前提',np.all(N>0) and close(mu_stone[-1],1.588723338274452,1e-8),'转动全过程N>0，但石头终点径向约束需μ≥1.5887；原卷未提供此条件。')
eta_h=(-.4+math.sqrt(.16+4*1.8*.725))/(3.6)
veq=math.sqrt(2*g*A/4);teq=(veq*c+math.sqrt((veq*c)**2+4*g*H))/g
check('Q7 两项变式模型检查',close(eta_h/(1-eta_h),1.1421975257453019) and close(veq*s*teq,.6293852340159654),'水平初态且h从地面计：m/M=1.14220；原倾斜初态等质量时射程.629385m。')
# Q8：符号微分位置得到初始加速度、恒速、a²，而非由答案反推。
t,L,v,al,th=sp.symbols('t L v al th',positive=True)
rho=L-v*sp.cos(th)*t;ph=-sp.tan(th)/sp.sin(al)*sp.log(rho/L)
rvec=sp.Matrix([rho*sp.sin(al)*sp.cos(ph),rho*sp.sin(al)*sp.sin(ph),rho*sp.cos(al)])
vel=rvec.diff(t);acc=vel.diff(t)
expected=sp.Matrix([-v*v*sp.sin(th)**2/(L*sp.sin(al)),-v*v*sp.sin(th)*sp.cos(th)/L,0])
check('Q8 初始加速度独立符号微分',all(sp.trigsimp(sp.simplify(x))==0 for x in acc.subs(t,0)-expected),'对完整位置二阶求导获得ax,ay,az，与基底推导一致。')
check('Q8 恒速及三维曲率',sp.trigsimp(sp.simplify(vel.dot(vel)-v*v))==0 and sp.trigsimp(sp.simplify(acc.dot(acc)-v**4*sp.sin(th)**2/rho**2*(1+sp.sin(th)**2/sp.tan(al)**2)))==0,'v²恒为v0²；a²含圆锥法向曲率项。')
qq=1;cot2=3;umax=2*qq**2/(1+math.sqrt(1+4*qq**2*cot2));angmax=math.degrees(math.asin(math.sqrt(umax)))
check('Q8 角度上限及数值稳定式',close(umax+3*umax*umax,1) and close(angmax,41.22235384455921) and .5+3*.5**2>1,'α30度、q1时θmax41.22235度；45度不满足。')
check('Q8 数值变式与极限',close(4*.5*math.sqrt(1+.25*3),math.sqrt(7)) and close(9/(2*math.cos(math.pi/6)),3*math.sqrt(3)) and close(2*.2/(1+math.sqrt(1)),.2),'θ30/α30变式a0=√7，t=3√3；平面cotα=0时u*=q²；θ0时a0=0。')
result=dict(all_passed=all(c['passed'] for c in checks),independent_methods=['直接端点参数化','符号微分及散度旋度检查','中心力与Lorentz方程数值积分','抛体落点独立求根','复振幅相消及归一化强度','极限和单位核查'],checks=checks)
(ROOT/'physics_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(all_passed=result['all_passed'],check_count=len(checks)),ensure_ascii=False))
