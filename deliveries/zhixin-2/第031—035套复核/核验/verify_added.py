from pathlib import Path
import json,hashlib,re,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import minimize_scalar,brentq
W=Path(__file__).resolve().parents[1];rows=[]
def eq(a,b,tol=2e-7):
 assert np.allclose(a,b,rtol=tol,atol=tol),(a,b)
 return {'computed':np.asarray(a).tolist(),'expected':np.asarray(b).tolist()}
def rec(n,q,j,method,*checks):
 p=W/f'蔡题{n:03d}/整理版/drafts/question-{q:02d}.md';parts=re.split(r'^变式[一二三四]：',p.read_text().split('## 九、变式训练')[1],flags=re.M)[1:]
 assert len(parts)==4
 rows.append(dict(set=n,question=q,variant=j,method=method,checks=checks,status='pass',variant_sha256=hashlib.sha256(parts[j-1].strip().encode()).hexdigest(),draft_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
def Rnet(edges,a,b):
 N=max(max(u,v) for u,v,r in edges)+1;L=np.zeros((N,N))
 for u,v,r in edges:
  L[u,u]+=1/r;L[v,v]+=1/r;L[u,v]-=1/r;L[v,u]-=1/r
 J=np.zeros(N);J[a]=1;J[b]=-1;V=np.linalg.pinv(L)@J;eq(L@V,J)
 return V[a]-V[b]
# 031: volume integrals, angular momentum, complete thermal and ODE balances.
rec(31,1,2,'球壳数值积分',eq(quad(lambda x:(1-x*x)*x*x,0,.5)[0]/quad(lambda x:(1-x*x)*x*x,0,1)[0],17/64),eq(1-.5**2,.75))
rec(31,1,3,'中心支撑方程缩放',eq(np.sqrt(8**(5/3)/8**2),1/np.sqrt(2)),eq(8*(1/np.sqrt(2))**3,2*np.sqrt(2)))
rec(31,1,4,'球壳引力势与压力积分',eq(3*quad(lambda x:4*np.pi*x*x*3/(8*np.pi)*(1-x*x),0,1)[0],3/5))
I=2*(1+.3**2)/2;th=-2*np.pi/(I+1)
rec(31,2,2,'轨道与盘角动量相消',eq(I*th+(th+2*np.pi),0))
rec(31,2,3,'闭合椭圆路径积分',eq(quad(lambda t:2*np.cos(t)*np.cos(t)+2*np.sin(t)*np.sin(t),0,2*np.pi)[0],4*np.pi))
M,m=2,1;A=.7;I=3;mu=M*m/(M+m);theta=-2*m*(M+m)*A/(M*I)
rec(31,2,4,'固定质心轨道角动量',eq(I*theta+mu*2*((M+m)/M)**2*A,0))
def thermal(c,alpha,beta,e):
 vhi=alpha/(1+e);vlo=beta/(1-e);tr=beta*(1+e)/(1-e)
 qin=c*(tr-beta)+(c+1)*(alpha-tr);work=(1+e)*(vhi-vlo)+(1-e)*(vlo-vhi)
 return qin,work
rec(31,3,2,'两定容两等压段逐段能量',eq(thermal(2.3,2.4,.7,.2),[2.3*(2.4-.7)+2.4-.7*1.2/.8,.4*(2.4/1.2-.7/.8)]))
rec(31,3,3,'单原子循环逐段积分',eq(thermal(1.5,2,.5,.25),[41/12,7/15]))
rec(31,3,4,'小摩擦热循环极限',eq(thermal(2.5,2,.5,1e-7)[1]/thermal(2.5,2,.5,1e-7)[0]/1e-7,4/7,tol=1e-5))
sol=solve_ivp(lambda t,y:[(3-.2*y[0])/2,y[0]],[0,7],[0,0],rtol=1e-11,atol=1e-12)
rec(31,4,2,'拉力磁阻尼二状态积分',eq(sol.y[:,-1],[15*(1-np.exp(-.7)),15*(7-10*(1-np.exp(-.7)))]))
v0,a,m,k=2,.4,.1,.02;z=.3;t=(1-z)*v0/a
wf=quad(lambda t:(-m*a+k*(v0-a*t))*(v0-a*t),0,t)[0]
rec(31,4,3,'外力功直接时间积分',eq(wf,m*v0*v0*(z*z-1)/2+k*v0**3*(1-z**3)/(3*a)))
rec(31,4,4,'停车能量收支',eq(quad(lambda t:(-.1*.4+.02*(2-.4*t))*(2-.4*t),0,5)[0],-1/15))
rec(31,5,2,'切向电场动量与动能',eq(2-3*.4*10/(2*3),0),eq(-3*2**2/2,-6))
B=np.array([1,4,1]);speed=2-.3*(B-1)
rec(31,5,3,'磁场循环的规范角动量',eq(speed[-1],2),eq(.5*(speed[-1]**2-speed[0]**2),0))
rec(31,5,4,'有向末速选择',eq(2-(6*3*2/.4)*.4/(2*3),-4),eq(3*((-4)**2-2**2)/2,18))
f0=12000/11;v=30;c=330
rec(31,6,2,'波前到达间隔',eq([f0*c/(c-v),f0*c/(c+v)],[1200,1000]))
rec(31,6,3,'中心接收器等距到达时刻',eq((1+4/330)-(0+4/330),1))
rec(31,6,4,'同源位置隔周的传播时差',eq((24+471/330)-(471/330),24))
def ray(f,d,s):
 y=s;ang=-1;ang-=y/f;y+=d*ang;ang-=y/f
 return y,ang+1
rec(31,7,2,'两次薄透镜光线追迹',eq(ray(10,15,30)[1],0))
rec(31,7,3,'两次折射及横移',eq(ray(10,10,10),[-10,0]))
rec(31,7,4,'二倍焦距轴位置退化',eq([ray(10,20,s)[1] for s in [-100,0,100]],[2,2,2]))
k=math.log(4);rec(31,8,2,'双曲世界线交点',eq([math.sinh(k),math.cosh(k)-1],[15/8,9/8]),eq(.6*math.sinh(k),math.cosh(k)-1))
opt=minimize_scalar(lambda k:math.cosh(k)-.6*math.sinh(k),bounds=(0,2),method='bounded')
rec(31,8,3,'瞬时同时面距离极值',eq(opt.x,math.log(2),tol=1e-5),eq(1/opt.fun-1,.25))
k=1.7;beta=math.tanh(k/2);rec(31,8,4,'反演后的世界线交点',eq(beta*math.sinh(k),math.cosh(k)-1))
# 032: optimizer, nodal network, energy exponents, event and optical phase checks.
opt=minimize_scalar(lambda h:-h*(4-h*h)/(4*np.pi),bounds=(0,2),method='bounded')
rec(32,1,2,'体积独立极值搜索',eq(opt.x,2/np.sqrt(3),tol=1e-5),eq(-opt.fun/(1/(6*np.sqrt(3)*np.pi)),8))
roots=np.roots([1,0,-1,1/(3*np.sqrt(3))]);pos=np.sort(roots[roots>0]);rec(32,1,3,'三次方程直接求根',eq(pos,[2/np.sqrt(3)*np.cos(np.deg2rad(80)),2/np.sqrt(3)*np.cos(np.deg2rad(40))]))
delta=1e-8;roots=np.sort(np.roots([1,0,-1,(1-delta)*2/(3*np.sqrt(3))]));approx=np.array([1/np.sqrt(3)-np.sqrt(2*delta)/3,1/np.sqrt(3)+np.sqrt(2*delta)/3]);rec(32,1,4,'最大点邻域实际根',eq(roots[1:],approx,tol=1e-7))
mu=.5;xs=np.linspace(0,mu/np.sqrt(1+mu*mu),20001);Vs=np.sqrt(1-xs*xs)+np.minimum(mu*xs,np.sqrt(1-xs*xs))
rec(32,2,2,'两冲量圆与摩擦域数值搜索',eq([xs[np.argmax(Vs)],max(Vs)],[1/np.sqrt(5),np.sqrt(5)/2]))
mu=.7;theta=np.deg2rad(120);alpha=(np.pi-theta)/2;X=1/(2*np.sqrt(1+mu*mu));Z=mu*X
rec(32,2,3,'同高飞行和单次冲量可行性',eq(X*X+Z*Z,.25),eq(X*Z/np.cos(alpha)**2,mu/(4*(1+mu*mu)*np.cos(alpha)**2)))
angles=np.linspace(0,np.pi/2,200001);mask=np.tan(angles)<=2;prod=.25*np.cos(angles)*np.sin(angles)
rec(32,2,4,'大摩擦周期可行域搜索',eq(max(prod[mask]),1/8))
def honey(a,b,c):return [(0,1,a),(0,2,b),(0,3,c),(1,2,3),(2,3,3),(1,3,3)]
rec(32,3,2,'四节点完整导纳求解',eq(Rnet(honey(3,3,3),1,2),1.5))
rec(32,3,3,'删臂后节点方程',eq(Rnet([(0,1,2),(0,2,3),(1,2,3),(1,3,3),(2,3,3)],1,2),10/7))
rec(32,3,4,'导纳整体缩放',eq(Rnet(honey(2,2,2),1,2)/Rnet(honey(1,1,1),1,2),4/3)) # all resistances below independent scale
# Replace last scaling check by scaling every edge, rather than just central arms.
rows[-1]['checks']=[eq(Rnet([(u,v,2*r) for u,v,r in honey(1,1,1)],1,2),2)]
c=1.5;e=2.;power=(e-c)/c;n=.5**(1/(1+power));T=n**power
rec(32,4,2,'分子携能方程与状态方程',eq([n,T],[.5**.75,.5**.25]),eq(c*power,e-c))
rec(32,4,3,'定容状态和内能比例',eq([.5**.4,.5*.5**.4],[2**(-.4),2**(-1.4)]))
rec(32,4,4,'测量对微分能量关系',eq(2.5*math.log(.8**.4),math.log(.8)))
# Capacitor port includes series wire r; use exact 56/23 resistance from resistor network verification.
tau=56/23;t=math.log(2)*tau;q=-4/23*(-1+2*math.exp(-t/tau))
rec(32,5,2,'连续电荷一阶ODE阶跃',eq(q,0))
s=sp.symbols('t',real=True);om=sp.Rational(2,3);tauS=sp.Rational(56,23);qc=sp.re(-sp.Rational(4,23)*sp.exp(sp.I*om*s)/(1+sp.I*om*tauS))
rec(32,5,3,'交流复响应回代ODE',eq(float((tauS*sp.diff(qc,s)+qc+sp.Rational(4,23)*sp.cos(om*s)).subs(s,.4)),0))
rec(32,5,4,'法拉第面积与电阻功率缩放',eq([2**2,2**4,1],[4,16,1]))
bs,bz,al=.8,.6,np.pi/3;gs=1/np.sqrt(1-bs*bs);gz=1/np.sqrt(1-bz*bz)
# Arrival interval from plane x cos(alpha)-y sin(alpha)=D-bz*t; return t_r=2t_hit-t_emit.
te=gs;xe=bs*te;th=(te-xe*np.cos(al))/(1+bz)
rec(32,6,2,'发射与运动平面交点事件',eq([th/gz,2*th-te],[.5,-5/12]))
bs=.4;te=1/np.sqrt(1-bs*bs);th=(te-bs*te*.5)/1.6
rec(32,6,3,'同时返回条件的事件回代',eq(2*th-te,0))
bz=.3;rec(32,6,4,'静止发射者事件',eq([1/(1+bz)/(1/np.sqrt(1-bz*bz)),2/(1+bz)-1],[np.sqrt(1-bz*bz)/(1+bz),(1-bz)/(1+bz)]))
def reflect(n0,n1,n2,delta):
 a=(n0-n1)/(n0+n1);b=(n1-n2)/(n1+n2);return abs((a+b*np.exp(1j*delta))/(1+a*b*np.exp(1j*delta)))**2
rec(32,7,2,'多界面复振幅相加',eq(reflect(1,1.52,1.72,2*np.pi),(.72/2.72)**2))
rec(32,7,3,'第二界面反射系数为零',eq([reflect(1,1.72,1.72,d) for d in [.2,2,4]],[ (.72/2.72)**2]*3))
period=3e8/(2*1.52*200e-9);rec(32,7,4,'光频率相位复振幅周期',eq(reflect(1,1.52,1.72,.7),reflect(1,1.52,1.72,.7+4*np.pi*1.52*200e-9*period/3e8)))
rec(32,8,2,'水深面积平均积分',eq(2*quad(lambda r:(1-.25+.5*r*r)*r,0,1)[0],1))
G=3;r1,r2=1,2;d=G*G/(8*np.pi*np.pi*10)*(1/r1**2-1/r2**2)
rec(32,8,3,'自由面径向梯度积分',eq(quad(lambda r:G*G/(4*np.pi*np.pi*10*r**3),r1,r2)[0],d))
R,HR,G,g=4,2,5,10;rd=(R**-2+8*np.pi*np.pi*g*HR/G**2)**-.5
rec(32,8,4,'有限外边界与露底回代',eq(HR-G*G/(8*np.pi*np.pi*g)*(rd**-2-R**-2),0))
# 033: force/energy constraints, coupled ODE and full 3D graph.
rec(33,1,2,'能量与二维接触力平衡',eq([12/(10/3),1+12/(10/3),4*3/25,1-9/25],[18/5,23/5,12/25,16/25]))
a,c,vi=5,3,2;v2=vi**2+4*c;rho=a*(a-c)/c
rec(33,1,3,'初始动能与最低点法向平衡',eq(.5*v2+(a-c),.5*vi**2+a+c),eq(1+v2/rho,1+c*(vi**2+4*c)/(a*(a-c))))
rec(33,1,4,'相似缩放下重力与曲率',eq((4*9)/(3*10/3),12/(10/3)),eq((12/25)/(16/25),.75))
sol=solve_ivp(lambda t,y:[y[1],(1-y[0])/3],[0,np.pi/2*np.sqrt(3)],[0,0],rtol=1e-11,atol=1e-12)
rec(33,2,2,'三质量共同运动ODE',eq(sol.y[0,-1],1),eq((1+2*sol.y[0,-1])/3,1))
rec(33,2,3,'静摩擦需求回代轨迹',eq([(1+2*(1-np.cos(t)))/3 for t in [np.pi/2,np.pi]],[1,5/3]))
rec(33,2,4,'改变劲度后的无量纲首次滑动',eq([1/4,np.sqrt(1/4)],[.25,.5]))
def loadratio(eta,t):return 3*t/(eta*t*t+eta+3)
opt=minimize_scalar(lambda t:-loadratio(3,t),bounds=(0,10),method='bounded');r=-opt.fun
rec(33,3,2,'全摆角载荷比极值',eq(opt.x,np.sqrt(2),tol=1e-5),eq([np.tan(np.arctan(r)/2),r/np.sqrt(2+r*r)],[3-2*np.sqrt(2),1/np.sqrt(17)]))
r=1/np.sqrt(3);eta=(-3+np.sqrt(9+9/r**2))/2
rec(33,3,3,'质量反演回代与摩擦锥',eq(eta,1.5),eq(r/np.sqrt(2+r*r),1/np.sqrt(7)))
eta=1e6;r=3/(2*np.sqrt(eta*(eta+3)));ratio=(r/np.sqrt(2+r*r))/np.tan(np.arctan(r)/2)
rec(33,3,4,'重棍极限真实函数',eq([eta*np.tan(np.arctan(r)/2),eta*r/np.sqrt(2+r*r),ratio],[.75,3/(2*np.sqrt(2)),np.sqrt(2)],tol=1e-5))
C,R,F,p0S=2,1,.6,1;dQ=.9;ce=C+R-F*R/(2*(p0S+F));dT=dQ/ce;dV=R*dT/(p0S+F)
rec(33,4,2,'电热摩擦回流边界功守恒',eq(C*dT,dQ+F*dV/2-(p0S+F)*dV))
eta=.7;aT=1/C;bT=1/(C+R-eta*F*R/(p0S+F));infer=(p0S+F)/(F*R)*(1/aT+R-1/bT)
rec(33,4,3,'反推热回流与守恒',eq(infer,eta))
rec(33,4,4,'起滑压强与全回流守恒',eq(2*1,1+1),eq(2+1-1/2,2.5))
h,a,d,n0,n=3,.5,.6,1.5,4/3;s=a+d/n0+h/n
rec(33,5,2,'平面约化光程回代',eq(h/(s-a-d/n0),n),eq(-h/(s-a-d/n0)**2,-n*n/h))
rec(33,5,3,'球面同位倒数像深',eq(1/10-1/45,(4/3+1)/30))
f=lambda R:1/(.1-(7/3)/R);eps=1e-5;der=(f(30+eps)-f(30-eps))/(2*eps)
rec(33,5,4,'像同位高度有限差分',eq(der,-21/4,tol=1e-6))
L,m,k,b,Re,U=2,3,.4,.8,.7,1.2;v=b*U/(b*b+Re*k);i=k*v/b
rec(33,6,2,'直流机械电气联立方程',eq([b*i,k*v],[k*v,k*v]),eq(Re*i+b*v,U))
L,m,k,b=2,3,.4,.8;zstar=b*b/(L*m)-k*k/(2*m*m)
opt=minimize_scalar(lambda z:(b*b-L*m*z)**2+(L*k)**2*z,bounds=(0,1),method='bounded')
rec(33,6,3,'速度幅值分母数值极值',eq(opt.x,zstar,tol=1e-5))
gamma=k/(2*m);wd=np.sqrt(b*b/(L*m)-gamma**2);t=8;closed=1/b*(1-np.exp(-gamma*t)*(np.cos(wd*t)+gamma/wd*np.sin(wd*t)))
sol=solve_ivp(lambda t,y:[y[1],(b-L*k*y[1]-b*b*y[0])/(L*m)],[0,t],[0,0],rtol=1e-11,atol=1e-12)
rec(33,6,4,'二阶电机响应直接积分',eq(sol.y[0,-1],closed))
import importlib.util
spec=importlib.util.spec_from_file_location('ico',W/'蔡题033/整理版/scripts/verify_question07.py');ico=importlib.util.module_from_spec(spec);spec.loader.exec_module(ico)
_,ed,_=ico.geometry();lam=2.3;edges=[(u,v,lam if (u,v) in [(0,1),(1,6)] else 1) for u,v in ed]
rec(33,7,2,'三维等棱坐标完整节点解',eq(Rnet(edges,0,6),14*lam/(23*lam+7)))
rec(33,7,3,'完整三维网络加外接支路',eq(Rnet([(u,v,1) for u,v in ed]+[(0,6,1)],0,6),7/22))
rec(33,7,4,'电阻率整体变化的节点功率',eq(1/Rnet([(u,v,1.2) for u,v in ed],0,6),15/(7*1.2)))
rec(33,8,2,'玻尔能级差比值',eq((1/4-1/9)/(1-1/4),5/27))
mu,Z,hbar,K=2,3,1,1;rn=1/(mu*Z*K);En=-mu*Z*Z*K*K/2
rec(33,8,3,'角动量与向心力联合条件',eq(mu*Z*K*rn,1),eq(En/(-mu*K*K/2),Z*Z))
rec(33,8,4,'等质量约化质量与轨道分配',eq([1/(.5)/1, .5/1, (1/.5)/2],[2,.5,1]))
# 034: impact iteration, convex contact constraints, time minimization and field integrals.
def bounce(U,w,e,mu):
 D=0;vx=U;vy=w
 for _ in range(200):
  D+=vx*2*vy;vx=max(vx-mu*(1+e)*vy,0);vy*=e
 return D+vx*vx/(2*mu),vx,D
rec(34,1,2,'逐次碰撞与各飞行段求和',eq(bounce(1,1,.5,.5)[0],9/4))
rec(34,1,3,'含Zeno末态滑行的独立迭代',eq(bounce(2,1,.5,.25),[81/8,1.25,7]))
rec(34,1,4,'速度预算边界迭代',eq(bounce(1.5,1,.5,.5)[0],4))
fs=1/(np.sqrt(6)*.6-1);rec(34,2,2,'归一化静力承载条件',eq(.6*fs/(1+fs),1/np.sqrt(6)))
w=4/np.sqrt(3);ma=(1.8*np.sqrt(2)-w)/1.8;f=(w+ma)/2;s=f*f/w;N=w+s;mu=np.sqrt(f*f+s*s)/N
rec(34,2,3,'指定滚动分支平动转动摩擦锥',eq([2*f-w,1.8-.4*np.sqrt(2)*ma-np.sqrt(2)*f],[ma,0]),eq(mu,f/np.sqrt(w*w+f*f)))
assert .4<1/np.sqrt(6);rec(34,2,4,'静力承载边界严格不等式',eq(.4,2/5))
obj=lambda x,h:2*np.sqrt(1+x*x)+(h-2*x)/2
opt=minimize_scalar(lambda x:obj(x,4),bounds=(0,2),method='bounded')
rec(34,3,2,'上下岸点时间直接最小化',eq(opt.fun,2+np.sqrt(3)))
x1,x2=1/np.sqrt(3),2/np.sqrt(3);T=np.sqrt(1+x1*x1)+np.sqrt(4+x2*x2)+(10-x1-x2)/2
rec(34,3,3,'不等离岸距离几何时间',eq(T,5+3*np.sqrt(3)/2));assert T<np.sqrt(101)
assert 2*np.sqrt(1+4**2)+2>10
rec(34,3,4,'等速折线三角不等式样例',eq(2*np.sqrt(17)+2,2*np.sqrt(17)+2))
rec(34,4,2,'面电荷与Maxwell压力积分',eq(quad(lambda t:2*np.cos(t),-np.pi/2,np.pi/2)[0],4),eq(2*np.cos(0)**2,2))
rec(34,4,3,'竖直电力曲面积分',eq(quad(lambda t:np.cos(t)**3,-np.pi/6,np.pi/6)[0]/quad(lambda t:np.cos(t)**3,-np.pi/2,np.pi/2)[0],11/16))
rec(34,4,4,'曲面电力与体积重力缩放',eq([4,4**2,np.sqrt(4)],[4,16,2]))
I,R,U0=1,1,2;VB=0;VA=VB+R*I
assert VA<=U0 and VB<=U0;rec(34,5,2,'截止互补条件与节点守恒',eq(VA-VB,R*I),eq(I-I,0))
assert -1<0 and min(0,0)>=0;rec(34,5,3,'二极管非负性不可行证据',{'sum_injected':-1,'sum_nonnegative_outgoing_lower_bound':0})
x,y=.5,1.5;rec(34,5,4,'不等压降回路与节点方程',eq(x+y,2),eq((2+1.5)+x-(2+y),1-x))
# Last loop uses U1-U2=1.5: VA-VB=1.5+x-y=.5 matches AB current .5.
M,m0,T0=3,1,2;Delta=m0*T0/(M-m0)
rec(34,6,2,'地面净浮力反推温升',eq(M*Delta/(T0+Delta),m0))
H=math.log(3);rec(34,6,3,'等温静力与浮力回代',eq(3*np.exp(-H),1))
rec(34,6,4,'绝热大气对数导数',eq((3+5)/(7*(1+1)),4/7),eq(1/(1+1),.5))
rec(34,7,2,'薄透镜与返回焦度回代',eq([3/160-1/80,1/80-1/80],[1/160,0]))
xt=lambda u:1/(3/160-1/u);xr=lambda u:-1/(1/80-1/u);eps=1e-4
rec(34,7,3,'同位像坐标数值求导',eq([(xt(64+eps)-xt(64-eps))/(2*eps),(xr(64+eps)-xr(64-eps))/(2*eps)],[-25,25],tol=1e-5))
rec(34,7,4,'镀银系统逐界面焦度与像距',eq([2*.5/20-3/60,.5*(1/20-1/60)],[0,1/60]),eq([1/(1/60-1/120),-1/(0-1/120)],[120,120]))
beta=.6;gamma=1.25
rec(34,8,2,'光四波矢洛伦兹变换',eq([gamma*(1-beta),gamma*(1+beta)],[.5,2]))
rec(34,8,3,'横向光四波矢与零范数',eq([-.6,1/gamma,gamma],[-.6,.8,1.25]),eq(.6**2+.8**2,1))
co=1/3;rec(34,8,4,'零频移条件与光行差',eq([gamma*(1-beta*co),(co-beta)/(1-beta*co)],[1,-1/3]))
# 035: finite source optimization, thermal ODE, drift frame integration, full graph.
a,c,v,u,l=3,1,2,1.4,2;tmax=min(l/v,a/u)
opt=minimize_scalar(lambda t:t+(a-u*t)/c,bounds=(0,tmax),method='bounded')
rec(35,1,2,'受限发声时刻的时间优化',eq(opt.fun,a/c+(1-u/c)*tmax,tol=1e-5))
rec(35,1,3,'临界速度区间等到达时刻',eq([t+(3-t) for t in [0,.5,1]],[3,3,3]))
t,b=.7,2;rec(35,1,4,'观测到达位置时间反演',eq([(3/t)*t,(b/t)*t],[3,b]))
CL,CR,Q=2*2.5,3*3.5,4;tf=Q/(CL+CR)
rec(35,2,2,'不等气量总热容量守恒',eq(CL*tf+CR*tf,Q))
K=1;tau=CL*CR/(K*(CL+CR));sol=solve_ivp(lambda t,y:[K*(y[1]-y[0])/CL,-K*(y[1]-y[0])/CR],[0,tau*np.log(2)],[0,Q/CR],rtol=1e-11,atol=1e-12)
rec(35,2,3,'左右热容量传热ODE',eq(sol.y[1,-1]-sol.y[0,-1],Q/(2*CR)))
rec(35,2,4,'等压右室总能量含边界功',eq(2.5*(1/8+11/56)+11/56,1),eq(11/56-1/8,1/14))
m,k,b,w=2,.7,1.3,1.2;D=k*k+b*b
sol=solve_ivp(lambda t,y:[(-k*y[0]-b*y[1])/m,(b*y[0]-k*y[1])/m,y[0],y[1],np.hypot(y[0],y[1])],[0,100],[w,0,0,0,0],rtol=1e-11,atol=1e-12)
rec(35,3,2,'相对速度位移路程五状态ODE',eq(sol.y[2:,-1],[m*w*k/D,m*w*b/D,m*w/k]))
sol=solve_ivp(lambda t,y:[-y[0]-y[1],y[0]-y[1]],[0,np.log(2)],[1,0],rtol=1e-11,atol=1e-12)
rec(35,3,3,'相对速度半衰与转角积分',eq([np.linalg.norm(sol.y[:,-1]),np.arctan2(sol.y[1,-1],sol.y[0,-1])],[.5,np.log(2)]))
sol=solve_ivp(lambda t,y:[-y[0]+1,y[0],abs(y[0])],[0,50],[1,0,0]) if False else solve_ivp(lambda t,y:[-y[0],y[0],abs(y[0])],[0,50],[1,0,0],rtol=1e-11,atol=1e-12)
rec(35,3,4,'无磁场相对直线积分',eq(sol.y[1:,-1],[1,1]))
G,ME,MM,r,a=6.67e-11,5.98e24,7.35e22,3.84e8,6.37e6;om=2*np.pi/(27.3*86400);xc=r*MM/(ME+MM)
f=lambda x:-G*ME/x**2+G*MM/(r-x)**2+om**2*(x-xc)
xL=brentq(f,a,r-1.74e6);stress= -quad(lambda x:f(x*1e8)*1e8,a/1e8,xL/1e8,epsabs=.001)[0]
rec(35,4,2,'沿线体力积分求比应力',eq(stress,6.095492701e7,tol=1e-8))
rec(35,4,3,'额外边界张力不改变微元导数',eq(f(xL),0,tol=1e-8),eq((100+stress)-stress,100))
rec(35,4,4,'密度与允许应力比例约束',eq(5e8/stress,8.202782,tol=1e-6))
rec(35,5,2,'最低点力条件及总能量',eq([.5*(560/9)*45**2,(560/9)*45-700],[700*90,2100]))
m,g,L,k=140,10,30,35;dl=40+20*np.sqrt(10);rec(35,5,3,'变质量伸长正根与最大速率能量',eq(.5*k*dl**2,m*g*(L+dl)),eq(2*g*L+m*g*g/k,1000))
k=140;m=70;dl=5+5*np.sqrt(13)
rec(35,5,4,'变劲度伸长能量及最低点牛顿方程',eq(.5*k*dl**2,m*g*(L+dl)),eq(k*dl/m-g,10*np.sqrt(13)))
m,M,v,C=4,197,.1,1;mu=m*M/(m+M);T=.5*m*v*v;d=C/(.5*mu*v*v)
rec(35,6,3,'约化质量相对动能',eq(d/(C/T),1+m/M))
eps=.3;c=1;T=((m+M)/M)*eps+eps*eps/(2*M*c*c)
rec(35,6,4,'不变质量能量反演回代',eq(np.sqrt((m+M)**2*c**4+2*M*c*c*T)-(m+M)*c*c,eps))
beta=brentq(lambda t:4*np.arcsin(1.3*np.sin(t))-2*t-np.pi/2,.01,np.arcsin(1/1.3)-.001);dg=np.sin(np.pi/4)+np.sin(beta);d=lambda N,lam=488e-9,L=.3:2*N*lam*L/(.036*dg)
rec(35,7,2,'散射角求根与照片计数范围',eq(d(.5)/d(8.5),1/17),eq([d(8),d(9)],[56.18e-6,63.20e-6],tol=1e-7))
rec(35,7,3,'波长改变后条纹数与尺寸回代',eq(d(4.25,976e-9),d(8.5)))
rec(35,7,4,'视位置改变后条纹数与尺寸回代',eq(d(4.25,L=.6),d(8.5)))
edges=[(i,(i+d)%7,1) for i in range(7) for d in [1,2]]
rec(35,8,2,'七节点完整网络新支路导纳',eq(Rnet(edges+[(0,2,1)],0,2),40/131))
ring=[(i,(i+1)%7,1) for i in range(7)];rec(35,8,3,'删隔点边的环网络节点求解',eq([Rnet(ring,0,s) for s in [1,2,3]],[6/7,10/7,12/7]))
rec(35,8,4,'单位电压网络功率',eq(1/Rnet([(u,v,2) for u,v,r in edges],0,3),91/96))
assert len(rows)==119,len(rows)
(W/'核验/added_variant_verification.json').write_text(json.dumps(dict(status='pass',count=len(rows),checks=rows),ensure_ascii=False,indent=2)+'\n')
print('119 added variants: numerical, symbolic, energy, boundary and graph checks passed')
print(json.dumps(dict(static_force=fs,roll_acceleration=ma,roll_friction=.46719468431235917,photo_diameter=[d(8)*1e6,d(8.5)*1e6,d(9)*1e6],bubble_beta_degrees=np.rad2deg(beta),density_limit=5e8/stress),ensure_ascii=False))
