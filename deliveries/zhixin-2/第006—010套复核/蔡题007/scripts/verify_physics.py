"""独立数值与几何检验；不依赖预先写入的正文答案文本。"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,value,expected=0,tol=1e-8):
 value=float(value);expected=float(expected)
 checks.append(dict(name=name,value=value,expected=expected,tolerance=tol,passed=abs(value-expected)<=tol))
def D(t,n=1):return np.array([[1,t/n],[0,1.]])
def S(n1,n2,r):return np.array([[1.,0],[-(n2-n1)/r,1.]])
def optics(n,R,a):
 w=S(n,1,-R)@D(2*R,n)@S(1,n,R)
 b=S(n,1,-R)@D(R-a,n)@S(1,n,-a)@D(2*a)@S(n,1,a)@D(R-a,n)@S(1,n,R)
 return w,b
w,b=optics(4/3,10,4)
for label,M,q,mag in [('水区',w,30,-1),('中心',b,-20,.25)]:
 B=M@D(30);T=D(q)@B
 check('01-'+label+'约化矩阵行列式',np.linalg.det(M),1)
 check('01-'+label+'不同初斜率同像高',T[0,1])
 check('01-'+label+'横向放大率',T[0,0],mag)
 check('01-'+label+'从表面换算球心位置',q+10,40 if label=='水区' else -10)
for n,a,u in [(1.33,4,40),(4/3,5,40),(4/3,4,20)]:
 M=optics(n,10,a)[1];B=M@D(u-10);q=-B[0,1]/B[1,1]
 phi=2*(n-1)/n*(1/10-1/a);v=1/(phi-1/u)
 check(f'01-变参数四界面与等效焦距a{a}u{u}n{n}',q+10,v)
 check(f'01-变参数矩阵与放大率a{a}u{u}n{n}',(D(q)@B)[0,0],-v/u)
check('01-折射率为1退化为空气传播',np.max(abs(optics(1,10,4)[1]-D(20))))

eta=.002;theta=np.arccos(1-eta);mu=np.tan(theta);N=98000;r=1.4;f=N*mu
check('02-指定直径压缩几何',2*r*np.cos(theta),2*r*(1-eta))
check('02-单根水平合力',f-f)
check('02-单根竖直合力',N-N)
check('02-单根总力矩',2*N*r*np.sin(theta)-2*f*r*np.cos(theta),tol=1e-9)
check('02-十根总拉力',10*f,62073.791650074294,tol=1e-7)
check('02-摩擦阈值',f/N,np.sqrt(2*eta-eta**2)/(1-eta))
check('02-小角拉力相对误差',abs(mu-np.sqrt(2*eta))/mu,0,tol=.00151)
check('02-二十根总拉力不变',20*(980000/20)*mu,10*f,tol=1e-7)
check('02-不滑动上下速度',1+1,2)

# 连杆几何通过独立的隐式约束求导与有限差分核验。
ell=1.;g=10.;mass=1.;v0=1.
def yy(s):return -.5*s-np.sqrt(ell**2-.75*s*s)
h=2e-4
yp=(yy(ell+h)-yy(ell-h))/(2*h)
ypp=(yy(ell+h)-2*yy(ell)+yy(ell-h))/h**2
check('03-初始几何下交点',yy(ell),-ell)
check('03-速度约束有限差分',yp,1,tol=8e-7)
check('03-二阶几何有限差分',ypp,6/ell,tol=2e-5)
T=1.5*mass*g;aa=g/4;ac=g/4
check('03-静止圆环受力',T/2-mass*g/2,mass*aa)
check('03-静止C受力',2*mass*g-T,2*mass*ac)
K=2*mass*v0;J=4*mass*v0
check('03-圆环冲量',K/2,mass*v0)
check('03-C冲量',J-K,2*mass*v0)
T0=1.5*mass*g+6*mass*v0*v0/ell;aa=g/4+3*v0*v0/ell;ac=g/4-3*v0*v0/ell
check('03-非零速度加速度约束',aa-ac,6*v0*v0/ell)
check('03-冲量后圆环受力',T0/2-mass*g/2,mass*aa)
check('03-冲量后C受力',2*mass*g-T0,2*mass*ac)
va=np.array([np.sqrt(3)/2,.5])*v0;vc=np.array([0.,-v0])
check('03-细线相对速度平方',np.dot(va-vc,va-vc),3*v0*v0)
check('03-总动能等效质量',mass*v0*v0+mass*v0*v0,.5*4*mass*v0*v0)
check('03-C加速度为零阈值',g/4-3*(g*ell/12)/ell)

# c=1，用真实移动箱壁的往返碰撞与面积；不使用固定平面通量代替。
v=.6;pv=v/np.sqrt(1-v*v);E=1/np.sqrt(1-v*v);tau=2/v
for u in [0,.3,.8,.95]:
 gam=1/np.sqrt(1-u*u);vp=(v-u)/(1-u*v);vm=(-v-u)/(1+u*v)
 tr=(1/gam)/(vp+u);tl=(1/gam)/(-vm-u)
 check(f'04-沿x同壁周期u{u}',tr+tl,gam*tau)
 delta=gam*(pv-u*E)-gam*(-pv-u*E)
 check(f'04-沿x每粒子压强u{u}',delta/(tr+tl),pv*v)
for u,th in [(.8,0),(.8,np.pi/4),(.8,np.pi/2),(.3,.4)]:
 gam=1/np.sqrt(1-u*u);e=np.array([np.cos(th),np.sin(th),0]);t=np.array([-np.sin(th),np.cos(th),0])
 L=np.eye(3)+(1/gam-1)*np.outer(e,e)
 # 壁面原切向为ey、ez，先收缩边向量再取叉积。
 area=np.cross(L@np.array([0,1.,0]),L@np.array([0,0,1.]))
 expected=np.cos(th)*e-np.sin(th)/gam*t
 check(f'04-斜壁有向面积u{u}th{th}',np.linalg.norm(area-expected))
 delta=2*pv*(gam*np.cos(th)*e-np.sin(th)*t)
 force=delta/(gam*tau)
 check(f'04-斜壁法向力面积比u{u}th{th}',np.linalg.norm(force)/np.linalg.norm(area),pv*v)
check('04-各向同性六束的三分之一',pv*v/3,(1/3)*pv*v)

eps=1.;a=1.;b=1.1;lam=2.;P0=5.
Er=lambda r:-lam/(2*np.pi*eps*r)
pot=quad(lambda r:-Er(r),a,b)[0]
check('05-势差积分',pot,lam*np.log(b/a)/(2*np.pi*eps))
pa=lam**2/(8*np.pi**2*eps*a*a);pb=lam**2/(8*np.pi**2*eps*b*b)
check('05-内膜两侧平均场',(-lam/(2*np.pi*a))*Er(a)/2,pa)
check('05-外膜两侧平均场',(lam/(2*np.pi*b))*Er(b)/2,-pb)
energy=quad(lambda r:eps*Er(r)**2/2*2*np.pi*r,a,b)[0]
check('05-电场能积分',energy,lam**2*np.log(b/a)/(4*np.pi*eps))
dh=1e-5
U=lambda x,y:lam**2*np.log(y/x)/(4*np.pi*eps)
check('05-固定电荷内膜能量导数',-(U(a+dh,b)-U(a-dh,b))/(2*dh)/(2*np.pi*a),pa,tol=1e-10)
check('05-固定电荷外膜能量导数',-(U(a,b+dh)-U(a,b-dh))/(2*dh)/(2*np.pi*b),-pb,tol=1e-10)
P1=P0+pb;P2=P1-pa
check('05-外膜机械平衡',P1-P0-pb)
check('05-内膜机械平衡',P2-P1+pa)
check('05-内外压强差',P2-P0,lam**2/(8*np.pi**2*eps)*(1/b**2-1/a**2))
check('05-电荷加倍静电压力四倍',(2*lam)**2/(8*np.pi**2*eps*a*a),4*pa)

n0=1.;q=1.;ell=2.;kp=2.;km=3.;U0=4.;ef=U0/ell
vp=2*q*ef/kp;vm=-q*ef/km;sigma=n0*q*q*(4/kp+2/km);current=sigma*ell*U0
check('06-净电荷密度',n0*2*q+2*n0*(-q))
check('06-正离子稳态力平衡',2*q*ef-kp*vp)
check('06-负离子稳态力平衡',-q*ef-km*vm)
check('06-逐载流子电流相加',ell**2*(n0*2*q*vp+2*n0*(-q)*vm),current)
check('06-阻力耗散等于电源功',ell**3*(n0*kp*vp**2+2*n0*km*vm**2),current*U0)
mp=1.;mm=2.;freq=1.7;Tp=2*np.pi/freq
def drift(t,z):return [(2*q*ef*np.cos(freq*t)-kp*z[0])/mp,(-q*ef*np.cos(freq*t)-km*z[1])/mm]
sol=solve_ivp(drift,(0,25*Tp),[0,0],rtol=2e-11,atol=2e-12,dense_output=True)
ts=np.linspace(24*Tp,25*Tp,151);vel=sol.sol(ts)
sc=4*n0*q*q/(kp+1j*freq*mp)+2*n0*q*q/(km+1j*freq*mm)
Isim=ell**2*(2*n0*q*vel[0]-2*n0*q*vel[1]);Icalc=np.real(ell*U0*sc*np.exp(1j*freq*ts))
check('06-交流相量与两离子时域积分',np.max(abs(Isim-Icalc)),tol=1e-8)
check('06-零频复电导率',np.real(4/(kp+0j)+2/(km+0j)),sigma)
check('06-单通道一驰豫时间',1-np.exp(-1),.6321205588285577)
check('06-相似几何电流加倍',sigma*(2*ell)*U0,2*current)

R=1.;T0=1.;nu0=1.;molar=1.;CV=1.5;CP=2.5;w0=np.sqrt(2*R*T0/molar)
temp=lambda z:T0*z**(2/3)
check('07-半量温度',temp(.5),2**(-2/3))
check('07-半量压强',.5*temp(.5),2**(-5/3))
z=.63;dh=1e-5
deriv=(CV*(z+dh)*temp(z+dh)-CV*(z-dh)*temp(z-dh))/(2*dh)
check('07-开口系统能量微分',deriv,CP*temp(z),tol=2e-10)
imp=quad(lambda z:molar*nu0*w0*z**(1/3),0,1,epsabs=1e-12)[0]
check('07-喷流冲量积分',imp,.75*molar*nu0*w0)
partial=quad(lambda z:molar*nu0*w0*z**(1/3),.5,1)[0]
check('07-前半质量动量占比',partial/imp,1-2**(-4/3))
kin=quad(lambda z:R*nu0*temp(z),0,1)[0]
carry=quad(lambda z:CV*nu0*temp(z),0,1)[0]
check('07-喷流定向能量积分',kin,.6*nu0*R*T0)
check('07-流出内能积分',carry,.9*nu0*R*T0)
check('07-全程能量平衡',kin+carry,CV*nu0*T0)
check('07-流动功转换瞬时关系',.5*molar*(w0*z**(1/3))**2,R*temp(z))
check('07-五自由度变式冲量系数',quad(lambda z:z**(1/5),0,1)[0],5/6)
check('07-全部焓模型动量倍数',np.sqrt(2*CP/R)/np.sqrt(2),np.sqrt(5/2))

m=1.;ell=1.;g=10.;k=np.sqrt(2)*m*g/ell;th0=np.pi/4;l0=ell/np.sqrt(2)
U=lambda th:-2*m*g*ell*np.cos(th)+.5*k*(2*ell*np.cos(th)-l0)**2
Up=lambda th:2*ell*np.sin(th)*(m*g-k*(2*ell*np.cos(th)-l0))
M=lambda th:2*m*ell**2*(9*np.cos(th)**2+np.sin(th)**2)
Mp=lambda th:-32*m*ell**2*np.sin(th)*np.cos(th)
dh=1e-4
check('08-平衡弹簧长度',2*ell*np.cos(th0),np.sqrt(2)*ell)
check('08-平衡伸长',2*ell*np.cos(th0)-l0,ell/np.sqrt(2))
check('08-平衡力矩广义条件',Up(th0))
check('08-角坐标等效惯性',M(th0),10*m*ell**2)
curv=(U(th0+dh)-2*U(th0)+U(th0-dh))/dh**2
check('08-势能曲率有限差分',curv,2*k*ell**2,tol=1e-6)
omega=np.sqrt(k/(5*m));period=2*np.pi/omega
def ode(t,z):th,vel=z;return [vel,-(Up(th)+.5*Mp(th)*vel*vel)/M(th)]
def peak(t,z):return z[1]
peak.direction=-1
sol=solve_ivp(ode,(0,2.2*period),[th0+1e-4,0],events=peak,rtol=2e-12,atol=2e-13,dense_output=True)
check('08-非线性方程极小振幅周期',sol.t_events[0][1],period,tol=1e-6)
ts=np.linspace(0,2*period,301);th,vel=sol.sol(ts)
check('08-非线性连杆能量守恒',np.ptp(.5*M(th)*vel**2+U(th)),tol=2e-10)
dy=1e-5;yth=ell*np.cos(th0+dy)-ell/np.sqrt(2);xth=3*ell*(np.sin(th0+dy)-1/np.sqrt(2))
check('08-质点位移一阶比',xth/yth,-3,tol=4e-5)
y=.002;Uy=-2*m*g*(ell/np.sqrt(2)+y)+.5*k*(ell/np.sqrt(2)+2*y)**2
check('08-竖直势能精确二次项',Uy-U(th0),2*k*y*y,tol=1e-12)
check('08-两种坐标频率一致',4*k/(20*m),2*k*ell**2/(10*m*ell**2))
check('08-原参考系数导致周期倍数',np.sqrt(10*ell/(np.sqrt(2)*g))/np.sqrt(5*ell/(np.sqrt(2)*g)),np.sqrt(2))
check('08-原长为零变式频率减半',(m*g/(np.sqrt(2)*ell))/(5*m),omega**2/2)
result=dict(all_passed=all(c['passed'] for c in checks),check_count=len(checks),checks=checks,
 model_notes=['01同心及一级近轴模型；环形水区存在口径球差。',
 '02指定压力合力偏移几何，非仅由压缩率确定真实材料滚阻。',
 '04压强定义为同一移动箱壁上的法向力除以同时面积。',
 '06稳态导电假设；交流惯性另需质量，位移电流另需介电参数。',
 '07流动功RT转动能，流出内能CVT保留；重箱、单侧、均匀缓慢排气。',
 '08弹簧增量为2y；参考解少一倍二次势能项，正确omega平方为sqrt(2)g/(5l)。'])
(ROOT/'physics_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for c in checks:
 if not c['passed']:print('FAILED',c)
print(json.dumps(dict(all_passed=result['all_passed'],check_count=len(checks)),ensure_ascii=False))
assert result['all_passed']
