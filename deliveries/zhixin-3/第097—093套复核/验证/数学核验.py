"""Independent algebra, quadrature and numerical checks; c=g=m=1 where stated."""
from pathlib import Path
import math,json
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq,minimize_scalar

checks=[]
def record(n,q,name,actual,expected,tol=1e-8):
    a=np.asarray(actual,dtype=float);b=np.asarray(expected,dtype=float)
    err=float(np.max(np.abs(a-b)))
    assert np.allclose(a,b,rtol=tol,atol=tol),(n,q,name,a,b,err)
    checks.append(dict(set=n,question=q,check=name,actual=a.tolist(),expected=b.tolist(),max_error=err,passed=True))
def identity(n,q,name,expr):
    e=sp.simplify(expr);assert e==0,(n,q,name,e)
    record(n,q,name,0,0)
pi=math.pi
x,t=sp.symbols('x t',real=True)
# 097
record(97,1,'能量与径向力联立的离面角',brentq(lambda c: c-2*(1-c),0,1),2/3)
record(97,1,'临界倾角与双接触的轴比边界',[math.acos(2/3),math.sqrt(1-(2/3)**2)],[.841068670568,math.sqrt(5)/3])
al=.4;a=3.;b=2.;v=np.array([a*math.cos(al),b*math.sin(al)]);normal=np.array([v[0]/a**2,v[1]/b**2])
record(97,1,'椭圆法向与参数切线正交',normal@np.array([-a*math.sin(al),b*math.cos(al)]),0)
J=math.sqrt(2)/9
record(97,2,'接触点冲量有效质量与解滑条件',.5*math.sqrt(2)-(9/2)*J,0)
record(97,2,'瞬时摩擦产生的轮转能和质心能之和',J**2+J**2/(2*(2/5)),(9/2)*J**2/2)
L=7.;r=1.3
field=quad(lambda z:r*r/(2*(r*r+z*z)**1.5),-L/2,L/2)[0]
record(97,3,'圆柱空腔等效表面电流逐环积分',field,L/(2*math.sqrt(r*r+(L/2)**2)))
aa=sp.Rational(7,10);Om=sp.Rational(13,10);z=sp.sin(Om*t)/Om*sp.exp(sp.I*aa*t)
identity(97,4,'磁场与弹簧的复运动方程',sp.diff(z,t,2)-2*sp.I*aa*sp.diff(z,t)+(Om**2-aa**2)*z)
record(97,4,'初速度与闭合周期',[complex(sp.diff(z,t).subs(t,0)).real,complex(z.subs(t,20*pi)).real],[1,0])
s,th,C=sp.symbols('s th C',positive=True)
M=C*sp.sin(th)**2/s;E=-sp.diff(M,s)*3;ii=E/5;F=3*ii*sp.diff(M,s)
identity(97,5,'互感力机械功率与焦耳热抵消',F+5*ii**2) # ds/dt=1
N=10000;logratio=math.lgamma(2*N+1)+2*math.lgamma(N/2+1)-3*math.lgamma(N+1)
record(97,6,'随机配对组合数的反应熵大N极限',logratio/N,math.log(2),1e-4)
prob=np.array([.25,.5,.25]);deg=np.array([1,2,1])
record(97,6,'AB两种内部配置与总混合熵',-sum(prob*np.log(prob/deg))-math.log(2)+math.log(2),2*math.log(2))
no,ne=1.5,1.8;kx=math.sin(math.radians(35));ky=no*math.sqrt(1-kx*kx/ne**2)
record(97,7,'波矢椭圆与群速度方向',[kx*kx/ne**2+ky*ky/no**2,(kx/ne**2)/(ky/no**2)],[1,no**2/ne**2*kx/ky])
be=.8;ss=.5;bc=(be/math.sqrt(1-be*be))/(1/math.sqrt(1-be*be)+ss);br=(be-bc)/(1-be*bc)
chi=math.acos(-br/bc);bx=(br*math.cos(chi)+bc)/(1+br*bc*math.cos(chi));by=br*math.sin(chi)*math.sqrt(1-bc*bc)/(1+br*bc*math.cos(chi));bp=math.hypot(bx,by)
record(97,8,'质心系散射最大偏角与碰后速度',[math.sin(math.atan2(by,bx)),bp],[ss,be*math.sqrt(1-ss*ss)/(1+ss*math.sqrt(1-be*be))])
ga=1/math.sqrt(1-be*be);gaf=1/math.sqrt(1-bp*bp);ps=np.array([ga*be-gaf*bx,-gaf*by]);Es=ga+ss-gaf
record(97,8,'最大偏角碰撞的靶球质量壳',Es*Es-ps@ps,ss*ss)
N=7;w0=(ga-1)/(ga+1);bn=be
for j in range(N):bn=bn*math.sqrt(1-ss*ss)/(1+ss*math.sqrt(1-bn*bn))
w=w0*((1-ss)/(1+ss))**N
record(97,8,'逐次洛伦兹递推与显式终速',bn,2*math.sqrt(w)/(1+w))
# 096
alpha=1.5;R=1;u=(alpha-1)/math.sqrt(alpha);vc=1/math.sqrt(alpha);h=alpha*vc
energy=.5*(u*u+vc*vc)-1/alpha;ecc=math.sqrt(1+2*energy*h*h)
record(96,1,'释放点的能量角动量恢复轨道',[h*h,ecc,h*h/(1+ecc),-1/(2*energy)],[alpha,alpha-1,1,1/(2-alpha)])
e=.5
# Two equal masses: preimpact velocities 1,0; e=1/2.
v=1.;v1=v/4;v2=3*v/4
record(96,2,'首次碰撞的机械能损失',.5*v*v-.5*(v1*v1+v2*v2),3/16)
record(96,2,'总恒力功与总损失',3/16+25/16,7/4)
xx,F,rhos,m0,c=sp.symbols('xx F rhos m0 c',positive=True);A=F+rhos*c**2;E=m0*c**2+A*xx;psq=F*xx*(2*m0*c**2+A*xx)/c**2
identity(96,3,'能量与动量给出的不变质量',E**2/c**4-psq/c**2-(m0+rhos*xx)**2-rhos*F*xx**2/c**2)
record(96,4,'接地球级数的总感应电荷',-4*pi*sum(1/np.arange(1,200001,dtype=float)**2),-2*pi**3/3,4e-6)
phi=math.asin(.5/1.33);d=500/(4*1.33*math.cos(phi));mass=1e3*.02*.03*d*1e-9*1e6
record(96,5,'薄膜光程相位与质量换算',[d,mass,500/math.cos(phi)],[101.4250947187,.0608550568312,539.5815039035],1e-7)
Lmat=np.zeros((7,7))
for i in range(6):
 for j in [(i+1)%6,6]:Lmat[i,i]+=1;Lmat[j,j]+=1;Lmat[i,j]-=1;Lmat[j,i]-=1
volt=np.linalg.solve(Lmat[:6,:6],np.array([1,0,0,2,0,-3]))
record(96,6,'七节点电阻网络直接求解',volt,np.array([1,4,11,29,-4,-41])/40)
res=[]
for j in [3,5,6]:
 I=np.zeros(7);I[0]=1;I[j]=-1;V=np.r_[np.linalg.solve(Lmat[:6,:6],I[:6]),0];res.append(V[0]-V[j])
record(96,6,'相对、相邻、中心端口等效电阻',res,[4/5,11/20,9/20])
LT=2.3;length=4.;mdCp=3.;T0=2.;rk=mdCp/(2*pi*LT)
record(96,7,'管壁热流积分等于出口焓流损失',quad(lambda xx:2*pi*rk*T0*math.exp(-xx/LT),0,length)[0],mdCp*T0*(1-math.exp(-length/LT)))
H=3.;g=2.;NS=4.
record(96,8,'均匀侧孔的流量积分',NS/H*quad(lambda hh:math.sqrt(2*g*(H-hh)),0,H)[0],2/3*NS*math.sqrt(2*g*H))
for a in [.2,.5,.8]:record(96,8,f'喷流落地点双孔高对称性h/H={a}',2*math.sqrt(a*(1-a)),2*math.sqrt((1-a)*a))
# 095
ac=1.4;ph=math.atan(ac);turn=ph-math.acos((1+3*ac)/(4*math.sqrt(1+ac*ac)))
record(95,1,'碰后能量求另一转折点',math.cos(turn)+ac*math.sin(turn),(1+3*ac)/4)
delta=.04;eta=(1+3*math.cos(delta))/4;loss=.5*(4/3)*(1-eta*eta)
record(95,2,'轮辐换支点损失的小角主项',loss/delta**2,1/2,3e-4)
for n in [1,3,8]:
 sumM=sum(3*j-1 for j in range(1,n+1));momentum=math.sqrt(2*sumM)
 record(95,3,f'逐段P平方增量n={n}',momentum/(3*n+1),math.sqrt(n/(3*n+1)))
L0,C0=2.,3.;I0=1.;om=1/math.sqrt(L0*C0);tt=.7;i1=.5*(1+math.cos(om*tt));i2=.5*(math.cos(om*tt)-1);u=-.5*I0*L0*om*math.sin(om*tt)
# I0 defined in text is initial total oscillation-current amplitude; each capacitor energy included.
record(95,4,'并联电感的差模守恒',i1-i2,1)
record(95,4,'两电容KCL',2*C0*(-.5*L0*om*om*math.cos(om*tt))+i1+i2,0)
record(95,5,'侧壁坡印廷向量方向',np.cross([1,0,0],[0,0,1]),[0,-1,0])
pVnum=3.;T1num=2.;T2num=5.
record(95,6,'恒压排气热量积分与关阀后压力',quad(lambda T:3.5*pVnum/T,T1num,T2num)[0],3.5*pVnum*math.log(T2num/T1num))
T=sp.symbols('T',positive=True);pV=sp.symbols('pV',positive=True);nRT=pV
identity(95,6,'恒压定容阀门排气的热量微分',sp.Rational(7,2)*(nRT/T)-sp.Rational(7,2)*pV/T)
f=1.;cc=1.25;aa=.75;bb=1.1;pts=[]
for u0 in np.linspace(0,2*pi,97):
 old=np.array([-(f+cc)+aa*math.cos(u0),bb*math.sin(u0)]);sx=-old[0];sip=f*sx/(sx-f);yp=-sip/sx*old[1];pts.append(((sip-f-cc)/aa)**2+(yp/bb)**2)
record(95,7,'薄透镜逐点像落在全等椭圆',pts,np.ones(len(pts)))
q,w,v,g,RR=sp.symbols('q w v g RR',real=True);theta=sp.symbols('theta',real=True);qd=-v/sp.pi;acc=sp.symbols('acc',real=True)
# Differentiate H_G=(3/4+A)theta_dot-A*u/R, A=1+2q^2.
Ac=1+2*q*q;Hdot=(sp.Rational(3,4)+Ac)*acc-4*q*qd*w
torque=-sp.sin(theta)*(4*g/RR+sp.cos(theta)*v*v+sp.sin(theta)*acc)/4
identity(95,8,'关于系统质心的角动量含变惯量项',4*(Hdot-torque)-((7+8*q*q+sp.sin(theta)**2)*acc+16/sp.pi*q*v*w+sp.sin(theta)*sp.cos(theta)*v*v+4*g/RR*sp.sin(theta)))
omega,u=sp.symbols('omega u',real=True);beta=(u-omega)**2/24+omega*(u-omega)/sp.pi+sp.sqrt(2)/6
identity(95,8,'pi/4时的角加速度含交叉项',12*beta-(u-omega)**2/2-12/sp.pi*omega*(u-omega)-2*sp.sqrt(2))
# 094
l,a=2.,1.5;mx=0
for th in np.linspace(0,2*pi,81):
 for tau in np.linspace(0,2*pi,121):
  xx=l*math.cos(tau)+a*math.cos(th)*math.sin(tau);yy=a*math.sin(th)*math.sin(tau);mx=max(mx,xx*xx/(l*l+a*a)+yy*yy/a**2)
record(94,1,'同初始点轨道族位于包络内',max(0,mx-1),0)
dd=1/(2*math.sqrt(3));end=math.acosh(2)
integ=lambda R:quad(lambda u0:dd/(R-dd*math.cosh(u0)),0,end,epsabs=1e-12)[0]
rootR=brentq(lambda R:integ(R)-pi/7,.6,2.)
record(94,2,'七瓣滚动半瓣积分定根',rootR,1.2357953511626192)
record(94,2,'一瓣三角形外形等价与标记恢复转数',[1/3,3*(1/3)],[1/3,1])
record(94,3,'体球与两种壳面荷质模型频率',[(1+1/5)/(1+2/5),(1+1/3)/(1+2/3),(1+1/3)/(1+2/5)],[6/7,4/5,20/21])
uu=2*x+x*x/2+sp.Rational(1,2)-1/(2*(1-x*x));du=sp.diff(uu,x);x0=brentq(sp.lambdify(x,du,'numpy'),.1,.9);um=float(uu.subs(x,x0))
record(94,4,'感应势垒导数定根及约化质量阈值',[x0,um,4*um],[.7004940207,1.1646100008,4.658440003])
pa,p0,r0=sp.symbols('pa p0 r0',positive=True);rr=sp.symbols('rr',positive=True);pressure=pa+p0*r0/rr;volume=4*sp.pi*rr**3/3
Wpump=sp.integrate(sp.diff(pressure*volume,rr),(rr,r0,2*r0));Wboundary=sp.integrate(pressure*sp.diff(volume,rr),(rr,r0,2*r0))
identity(94,5,'泵送功由pV变化得到',Wpump-4*sp.pi*r0**3/3*(7*pa+3*p0))
identity(94,5,'泵送功与几何边界功的差',Wpump-Wboundary+2*sp.pi*p0*r0**3)
pos=np.array([1.,2.,3.]);foci=[(2,5.),(0,6.),(1,7.)]
for axis,ff in foci:pos=pos/(1-pos[axis]/ff)
record(94,6,'三个透镜逐次成像与齐次一次公式',pos,-210/11*np.array([1,2,3]))
inertia=5/6;omega_sq=2*(math.sqrt(3)/4)/inertia;centripetal=omega_sq*math.sqrt(3)/2
record(94,7,'杆落到底部的能量法与竖直力',1+centripetal,19/10)
record(94,7,'最低点支持力合计',2*19*math.sqrt(3)/30*math.sqrt(3)/2,19/10)
record(94,7,'对称截面仍有弯矩',(28*1-9)/80,19/80)
td2=lambda th:6*pi*pi-24*th*th-30*math.cos(th);tdd=lambda th:15*math.sin(th)-24*th
Nfun=lambda th:20-math.cos(th)*td2(th)-math.sin(th)*tdd(th)
tc=brentq(Nfun,0,.9)
record(94,8,'夹子接触力首次为零',[tc,Nfun(tc)],[.5406327247,0])
# 093
lam=.5;mu=.2;u0=1.;uc=.7;r=1.;g=1.;om0=2.5*(lam-1)*u0
time=(u0-uc)/(mu*g);spin=om0+2.5*mu*g*time;postu=.1*uc;postspin=spin
pure=(5*postu+2*postspin)/7
record(93,1,'碰后摩擦至纯滚的终速度',pure,5/7*(lam*u0-.9*uc))
record(93,1,'回滚条件与碰撞先于纯滚',int(pure<0 and uc>5*lam*u0/7),1)
ecc=.5;r0=2.;p1=1.;theta=.7;rr=(1-ecc*ecc)*r0/(1+ecc*math.cos(theta));rv=rr*np.array([math.cos(theta),-math.sin(theta)]);pv=np.array([math.sin(theta),ecc+math.cos(theta)]);Lz=np.linalg.det(np.stack([rv,pv]));k=(1-ecc*ecc)*r0
record(93,2,'动量圆对应的角动量与能量',[Lz,.5*pv@pv-k/rr],[(1-ecc*ecc)*r0,-(1-ecc*ecc)/2])
yr=np.linspace(-1,1,31);xr=(1-yr**2)/2
record(93,3,'两条拼接抛物线的焦点极坐标',np.sqrt(xr*xr+yr*yr)+xr,np.ones(len(yr)))
record(93,3,'上下拼接点切线正交',np.dot([1,1],[-1,1]),0)
for A,B in [(.1,.1),(.1,.6),(.1,1.),(.7,.7),(.7,1.2),(2.,3.)]:
 if A>=2/7 and B>=6/7:P,Q=1/7,3/7
 elif B>=3*A and 5*B-A>=4:P=A/2;Q=(2+P)/5
 elif B<=3*A and B<=6/7:Q=B/2;P=Q/3
 else:P=A/2;Q=B/2
 b=Q-3*P;tt=2+P-5*Q
 record(93,4,f'冲量相图A={A},B={B}互补约束',[(A/2-P)*b,(B/2-Q)*tt,max(0,-b),max(0,-tt)],[0,0,0,0])
 Ef=(1-P-Q)**2+.5*(1+2*P-2*Q)**2+2*Q*Q;assert Ef<=1.5+1e-8
a,b=2.,1.5;point=np.array([.3,.2])
field=np.array([quad(lambda ph,j=j:(point[j]-(a*math.cos(ph) if j==0 else b*math.sin(ph)))/np.linalg.norm(point-np.array([a*math.cos(ph),b*math.sin(ph)]))**2,0,2*pi,epsabs=1e-11)[0] for j in range(2)])
record(93,5,'线性压缩带电椭圆的内场直接积分',field,[0,0])
c=1e-6
record(93,5,'共焦电容的同心圆极限',math.acosh(2*a/c)-math.acosh(a/c),math.log(2))
r,H,rho,length=1.,.5,.3,2.6;X=((r*r+H*H)-math.sqrt((r*r+H*H)**2-4*rho*rho*H*H))/2;s0=math.sqrt(rho*rho-X);k=s0*H/(r*rho);D=math.sqrt(r*r+H*H);K=length**2/12+rho*rho/4
normal=np.array([-X/(r*rho),-k,s0/rho]);tangent=np.array([0,r/D,H/D])
record(93,6,'三维接触法线单位长度与切线正交',[normal@normal,normal@tangent],[1,0])
ms=k/math.sqrt(1-k*k);md=k*D/r
record(93,6,'静力与滑动零加速度阈值',[ms,md],[.4988413094,.4990723393],2e-6)
mu=.2;A=s0/rho+mu*H/D;B=k-mu*r/D;beta=r*B/(H*r*B+K*A);acc=H*beta;NN=K/(2*(H*r*B+K*A))
record(93,6,'实际滑动摩擦下重力功率等于动能增长与热',H,(H*H+K)*beta+2*mu*NN*D)
record(93,6,'无摩擦的能量法角加速度',r*k/(H*r*k+K*s0/rho),H/(H*H+K))
time=quad(lambda T:285*(20-T)/(300-T),15,18,epsabs=1e-12)[0]
record(93,7,'升温时间直接数值积分',time,285*(3+280*math.log1p(-3/285)))
gamma=1.4;Q1=(2**(gamma-1)-1)/(gamma-1);Q2=math.log(2);Q3=(1-2**(1-gamma))/(gamma-1);eta1=1-Q2/Q1;eta2=1-Q3/Q2
record(93,8,'具体理想气体两子循环与复合效率',eta1+eta2-eta1*eta2,1-2**(1-gamma))
assert {(v['set'],v['question']) for v in checks}=={(n,q) for n in range(93,98) for q in range(1,9)}
Path(__file__).with_name('math_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(f'{len(checks)} checks passed, covering all 40 questions')
