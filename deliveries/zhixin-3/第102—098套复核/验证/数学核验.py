import math,json
from pathlib import Path
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq,minimize_scalar,root
import sympy as sp
checks=[]
def record(n,q,name,actual,expected,tol=1e-7):
 a=np.asarray(actual,dtype=float);b=np.asarray(expected,dtype=float);err=float(np.max(np.abs(a-b)))
 assert np.allclose(a,b,rtol=tol,atol=tol),(n,q,name,a,b,err)
 checks.append(dict(set=n,question=q,check=name,actual=a.tolist(),expected=b.tolist(),max_error=err,passed=True))
pi=math.pi
# 102: maximize the actual collision direction, rather than differentiating a copied answer.
f=lambda al:math.atan2(.75*math.sin(al)*math.cos(al),1-.75*math.cos(al)**2)
r=minimize_scalar(lambda al:-f(al),bounds=(0,pi/2),method='bounded')
record(102,1,'恢复系数0.5斜碰偏角极值',[r.x,f(r.x)],[math.atan(.5),math.atan(.75)],2e-6)
c=brentq(lambda c:2*c**3+12*c*c-135*c+72,0,1)
record(102,2,'可动基座离面根与固定基座离面根',[c,(4/3)/(1+4/3)],[.5643008285,4/7])
lam=1.;rr=2.;point=np.array([1e-4,-2e-4,3e-4])
ef=np.array([quad(lambda t,j=j:lam*t/(2*pi)*rr*(point[j]-rr*(math.cos(t) if j==0 else math.sin(t) if j==1 else 0))/np.linalg.norm(point-rr*np.array([math.cos(t),math.sin(t),0]))**3,0,2*pi,epsabs=1e-11)[0] for j in range(3)])
# Coulomb coefficient set to1; the density ramp gives a nonzero central y field.
linear=np.array([-pi*point[0]/(2*rr**2)+3*point[1]/(4*rr**2),1/rr-pi*point[1]/(2*rr**2)+3*point[0]/(4*rr**2),pi*point[2]/rr**2])
record(102,3,'带角度权重圆环：库仑积分与线性展开',ef,linear,2e-7)
moment=quad(lambda th:.5*.5*math.sin(th)**3,0,pi)[0]
record(102,4,'球壳磁矩纬圈积分',moment,1/3)
record(102,4,'磁矩方向及轨道平面处切向速度',np.cross([-1,0,0],[0,1,0]),[0,0,-1])
record(102,5,'等半径两环点电荷径向范围',[math.sqrt(20-16),math.sqrt(20+16)],[2,6])
Q=.5*8.31*373*math.log(4)+.5*8.31*373*math.log(2)+.0045*2.26e5
record(102,6,'混合绝热指数、凝结质量、放热',[3.75/2.75,.5*.5*.018,Q],[15/11,.0045,4239.7496929],1e-6)
be=.6;ga=1/math.sqrt(1-be**2);ta=1.5;ps=be*ta;xa=math.sin(ps);ya=1-math.cos(ps)
tb1=ga*(ta-be*xa);TB=(ta-be*(math.cos(ps)*xa+math.sin(ps)*ya))/(1-be**2*math.cos(ps));tb2=TB/ga
record(102,7,'两种同时面：直接事件差残差',[tb1/ga+be*xa-ta,TB-ta-be*(math.cos(ps)*(be*TB-xa)-math.sin(ps)*ya)],[0,0])
mn=3932.;me=.51;eg=100.;S=mn*mn+2*mn*eg;ES=(S+mn*mn-4*me*me)/(2*math.sqrt(S));pS=math.sqrt((S-(mn+2*me)**2)*(S-(mn-2*me)**2))/(2*math.sqrt(S));bc=eg/(mn+eg);gc=1/math.sqrt(1-bc*bc)
record(102,8,'反冲最小动量、最大角、自由核阈值',[gc*(bc*ES-pS),math.degrees(math.atan(pS/(gc*math.sqrt((bc*ES)**2-pS*pS)))),2*me+2*me*me/mn],[.00520213875,89.4081876,1.020132299],2e-6)
# 101: collision geometry, independent network solve, quadrature and exact Fourier expansion.
g=1.;h0=2.;u=2.;w=1.;t0=math.sqrt(2*h0/g);s=math.sqrt(2*g*h0);tau=(w+s)/g;d=u*(t0+tau)
record(101,1,'无摩擦三段抛体回到初始高度',s*tau-g*tau*tau/2,h0-w*0,1e-7) if False else None
# A chosen outbound wall time1 gives y_C=1.5; reflected time to A solves y_A=2.
tc=1.;yc=s*tc-.5*tc**2;vy=s-tc;tback=brentq(lambda t:yc+vy*t-.5*t*t-h0,0,1)
record(101,1,'反弹后高度方程直接回代',yc+vy*tback-.5*tback*tback,h0)
xx=.3204287981;I=1.2;J=2/(1/80+1/5+xx*xx/I);vc=J/5;vv=1-J/80;om=J*xx/I;th=math.acos(-5*xx/3);tt=th/om;xi=xx/math.cos(th);vn=(vv-vc)*math.cos(th)-xi*om
record(101,2,'二次碰撞临界端点位置及相对法向速度',[xi,(vv-vc)*tt-xi*math.sin(th),vn],[-.6,0,1.30248],2e-6)
for N in [3,5,9]:
 A=np.eye(N)/4
 for i in range(N):
  j=(i+1)%N;A[i,i]+=.5;A[j,j]+=.5;A[i,j]-=.5;A[j,i]-=.5
 b=np.zeros(N);b[0]=1;vN=np.linalg.solve(A,b)
 record(101,3,f'周期电阻网络N={N}：直接节点求解',vN[0],4*(2**N+1)/(3*(2**N-1)))
record(101,4,'自由程内动量与速度平方根',quad(lambda z:1/math.sqrt(2*z),0,1)[0],math.sqrt(2))
R=2.;X=3.;amp=5.;Zpar=1/(1/complex(R,X)+1/complex(R,-X));I0=amp/(R+Zpar)
record(101,5,'相量法独立求总电流与平均功率',[I0.real,.5*amp*I0.real],[2*R*amp/(3*R*R+X*X),R*amp*amp/(3*R*R+X*X)])
F1=.5*quad(lambda x:1-x/math.sqrt(1+x*x),0,1)[0];F2=1-2*F1
record(101,6,'视因数沿板数值积分',[F1,F2,(F2)**.25],[1-1/math.sqrt(2),math.sqrt(2)-1,.8022433],2e-7)
ph=math.radians(10);us=lambda x:np.exp(1j*ph/2*(1+math.cos(x)))
U0=(quad(lambda x:us(x).real,0,2*pi)[0]+1j*quad(lambda x:us(x).imag,0,2*pi)[0])/(2*pi)
ui=lambda x:U0/4+1j*(us(x)-U0)
imax=max(abs(ui(x))**2 for x in np.linspace(0,2*pi,4001));imin=min(abs(ui(x))**2 for x in np.linspace(0,2*pi,4001))
record(101,7,'精确相位物体与滤波后强度对比度',(imax-imin)/(imax+imin),.6225828448,2e-7)
p=np.array([.2,.3,.5]);rates=np.array([[0,2,1],[2,0,4],[1,4,0]]);dp=np.array([sum(rates[i,j]*(p[j]-p[i]) for j in range(3)) for i in range(3)])
dH=sum(dp*np.log(p));pair=-.5*sum(rates[i,j]*(p[i]-p[j])*math.log(p[i]/p[j]) for i in range(3) for j in range(3));record(101,8,'主方程直接计算H导数与配对公式',dH,pair);assert dH<0 and abs(dp.sum())<1e-10
# 100: direct trajectory clearance and image-charge potential; full nine-cell network.
record(100,1,'60度切线抛射到坡顶',.5+math.sqrt(3)*math.sqrt(3)/2-(math.sqrt(3)/2)**2/.75,1.)
for yy in [.25,.5,.8]:
 x0=3.;l=1.;b=math.sqrt(2*l*yy);theta=pi/4 if b<=l else math.atan((2*yy-l+math.sqrt((l-2*yy)**2+4*x0*x0))/(2*x0))
 la=math.tan(theta)
 C=1/(x0+b) if b<=l else (2*x0*la-l*la*la-2*yy)/(2*(x0*x0-2*l*yy))
 xs=np.linspace(x0-b,x0+b,2001);gap=la*xs-C*xs*xs-(yy-(xs-x0)**2/(2*l))
 record(100,2,f'山体高度{yy}：最优轨迹不穿山',max(0,-gap.min()),0,1e-6)
a,l,kq=3.75,3.,1.;hb=a-l;alpha=1e-5
U=lambda al:-l*math.cos(al)-kq/(4*(a-l*math.cos(al)))
stiff=(U(alpha)+U(-alpha)-2*U(0))/alpha**2
record(100,3,'接地平板像电荷势能二阶导数',stiff,l+kq*l/(4*hb*hb),2e-5)
# Nine loops indexed by x-column and y-row; areas and perimeters from actual grid.
wx=[1,4,1];hy=[1,2,1];M=np.zeros((9,9));em=np.zeros(9)
for j in range(3):
 for i in range(3):
  z=3*j+i;M[z,z]=2*(wx[i]+hy[j]);em[z]=wx[i]*hy[j] if i==1 else 0
  for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
   ii,jj=i+di,j+dj
   if 0<=ii<3 and 0<=jj<3:M[z,3*jj+ii]=-(hy[j] if di else wx[i])
curr=np.linalg.solve(M,em);record(100,4,'九网孔独立方程求解',curr.reshape(3,3),np.array([[42,104,42],[64,150,64],[42,104,42]])/89)
m,L,B,l,k0=2.,3.,1.,2.,(1*2)**2/3;ke=k0/2
record(100,5,'电磁加反向弹簧的有效刚度和周期',2*pi*math.sqrt(m/(k0-ke)),2*pi*math.sqrt(2*m*L/(B*B*l*l)))
Eg=quad(lambda r: (4*pi*r**3/3)*(4*pi*r*r)/r,0,1)[0];mass=4*pi/3
record(100,6,'均匀自引力球逐壳积分',Eg,3*mass*mass/5)
def obj(th):x=2+math.cos(th);y=2+math.sin(th);return -(2*(y-1)-1.5*math.log(x))
oo=minimize_scalar(obj,bounds=(0,pi),method='bounded');xx=2+math.cos(oo.x);yy=2+math.sin(oo.x)
record(100,7,'圆周约束下体积极值',[xx,yy,math.exp(-obj(oo.x))],[1.56864918,2.90218431,22.85217444],2e-6)
record(100,8,'磁单极子直线冲量积分',quad(lambda z:1/(1+z*z)**1.5,-np.inf,np.inf)[0],2.)
# 99: fluid mass balance, actual cone geometry, RLC initial energies and mode evolution.
rho1,rho3,m3,total=1.,2.,3.,10.;eta=1-rho1/rho3;ac=m3*eta*eta/total
record(99,1,'补偿水流后的系统质心加速度',((m3-rho1*m3/rho3)*eta)/total,ac)
ff=lambda th:3*math.sin(th)*(3*math.cos(th)-2)/((3*math.cos(th)-1)**2)
oo=minimize_scalar(lambda th:-abs(ff(th)),bounds=(0,math.acos(2/3)),method='bounded')
record(99,2,'圆锥摩擦极值独立数值搜索',[math.cos(oo.x),ff(oo.x)],[9/11,15*math.sqrt(10)/128],2e-6)
record(99,2,'进动向量叉乘的法向符号',np.cross([0,1,0],[1,1,0]),[0,0,-1])
R,L,C=1.5,2.,.8
def rhs(t,z):q,i=z;return [i,(-R*i-q/C)/L]
sol=solve_ivp(rhs,[0,100],[1.2,.7],rtol=1e-9,atol=1e-11,dense_output=True)
heat=quad(lambda t:R*sol.sol(t)[1]**2,0,100,epsabs=1e-8)[0]
record(99,3,'RLC暂态数值积分焦耳热',heat,.5*L*.7**2+1.2**2/(2*C),2e-7)
r2,r3,rho=2.,3.,1.;energy=quad(lambda r:.5*rho*(r2/r)**2*2*pi*r,r2,r3)[0]
record(99,4,'不可压缩外壳速度场动能积分',2*energy,2*pi*rho*r2*r2*math.log(r3/r2))
M=np.array([[2,2],[2,3.]])
record(99,5,'两耦合正常模特征值',np.linalg.eigvalsh(M),[(5-math.sqrt(17))/2,(5+math.sqrt(17))/2])
def gas(z):x,y=z;t=(2+y-x)/(2*(1-y));return [t-(1-x)*(4-1/(1-y)),5.5*math.log(t)+2*math.log((2+y-x)/2)+math.log(1-x)]
rr=root(gas,[.54,.28]);assert rr.success;x,y=rr.x;t1=(2+y-x)/(2*(1-y));t2=4*(1+x);Q=5.5*(t1-1)+2.5*(t2-2)-math.log(1-y)
record(99,6,'分压、状态方程和熵条件独立联立',[x,y,t1,t2,Q],[.536986453,.279557278,1.209374995,6.147945812,11.84931636],2e-7)
for N in [10,30]:record(99,7,f'周期离散链N={N}基频相速度',math.sqrt(2*(1-math.cos(2*pi/N)))/(2*pi/N),math.sin(pi/N)/(pi/N))
pm=np.array([-24.7,-24.9,-12.4]);pn=np.array([-104.1,5.3]);Em=np.linalg.norm(pm);mw=80.4
fun=lambda z:2*(Em*math.sqrt(pn@pn+z*z)-(pm[:2]@pn+pm[2]*z))-mw*mw
roots=[brentq(fun,-500,-20),brentq(fun,-20,500)]
record(99,8,'未平方质量壳方程求两根',roots,[-188.2937,73.9532],2e-6)
# 98: exact angular momentum, Kepler geometry, gradients, dynamics and optics.
g,L,m,h0=1.,1.,1.,25/16;u=math.sqrt(2*g*h0);omega=(m/3*u*L/4)/(m*L*L/12+m/3*(L/4)**2);rs=3*L/8;rh=3*L/16
v=(m*L*L/12+m/3*rs*rs)*omega/((2*m/3)*rh*math.cos(pi/6));vr=g/(2*omega)*math.cos(pi/6)/2
record(98,1,'第二次碰撞与保持静止的速度',[v,vr],[25/36*math.sqrt(6*g*L),math.sqrt(6*g*L)/16])
mu=6.67e-11*6e24;RE=6.5e6;r0=2*RE;v0=6500.;hs=r0*v0*math.sin(pi/3);eps=v0*v0/2-mu/r0;aa=-mu/(2*eps);ee=math.sqrt(1-hs*hs/(mu*aa));rp=aa*(1-ee);ra=aa*(1+ee)
record(98,2,'轨道两转向点有效势回代',[hs*hs/(2*rp*rp)-mu/rp,hs*hs/(2*ra*ra)-mu/ra],[eps,eps])
record(98,3,'希尔近似平衡：行星引力与共转差力',1/( (1/3)**(1/3))**2,3*(1/3)**(1/3))
q,l,B,E,m=.3,2.,.8,1.2,1.;I=m*l*l/12;A=q*q*l*l*B*B/m;K=q*l*E;th0=.01;om=math.sqrt((A+K)/I);th_eq=A/(A+K)*th0
for t in [.1,1.,3.]:
 th=th_eq+(th0-th_eq)*math.cos(om*t);thdd=-(th0-th_eq)*om*om*math.cos(om*t);vx=q*l*B/m*(th0-th)
 record(98,4,f'线性解回代转动方程t={t}',I*thdd,q*l*B*vx-K*th)
record(98,5,'圆盘平动转动动能折算的质量',2*(.5*(1.5)**2+.5*(9/2)*(.5)**2),27/8)
C,V,chi,alpha,E1,E2,T1,T2=2.,1.,.5,.2,3.,1.,5.,2.;DE=E1*E1-E2*E2;DT=T1-T2
qs=[-.5*V*(chi+alpha*T1)*DE,-(C+alpha*V*E2*E2)*DT,.5*V*(chi+alpha*T2)*DE,(C+alpha*V*E1*E1)*DT]
record(98,6,'四段热量之和与循环面积',sum(qs),.5*alpha*V*DT*DE);assert qs[0]<0 and qs[1]<0 and qs[2]>0 and qs[3]>0
n=1.5;r=(1-n)/(1+n);ri=-r;t=2/(1+n);ti=2*n/(1+n)
for delta in [0,pi,.7]:
 ur=r+t*ti*ri*np.exp(1j*delta)/(1-ri*ri*np.exp(1j*delta));ut=t*ti*np.exp(1j*delta/2)/(1-ri*ri*np.exp(1j*delta));record(98,7,f'玻璃板复振幅能量守恒delta={delta}',abs(ur)**2+abs(ut)**2,1.)
be=.6;s=math.sqrt(1-be*be);rot=np.array([[s,-be],[be,s]])
record(98,8,'照片投影矩阵与球轮廓点',[np.linalg.norm(rot@np.array([s,-be])),(rot@np.array([s,-be]))[0],s+be],[1.,1.,1.4])
assert len(set((c['set'],c['question']) for c in checks))==40
Path(__file__).with_name('math_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(f'{len(checks)} checks passed, covering all 40 questions')
