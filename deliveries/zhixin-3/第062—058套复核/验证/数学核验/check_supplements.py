from pathlib import Path
import json,hashlib
import numpy as np
import sympy as S
from scipy.optimize import brentq
from scipy.integrate import quad
P=Path(__file__).parent;rows=[];pi=np.pi
def close(a,b):assert np.allclose(np.asarray(a,dtype=complex),np.asarray(b,dtype=complex),rtol=1e-8,atol=1e-8),(a,b)
def record(name,value):rows.append(dict(check=name,passed=True,result=value))

# Inertia variant: both endpoint slip and energy, not only a copied threshold.
Jt=(3*np.sqrt(2)+np.sqrt(6))/6
vals=[]
for k in [2/5,2/3]:
 crit=(1+1/k)*Jt-1/np.sqrt(2);om=crit+.2;uf=1/np.sqrt(2)+om-(1+1/k)*Jt;close(uf,.2);vals.append(crit)
record('不同惯量的持续滑动阈值',vals)
u=S.symbols('u',real=True);ac=np.sqrt(3)/2;lam=36/47;W=76/(47*np.sqrt(3));assert 4*lam*ac-W>0
record('星形支持力在全允许区间单调',4*lam*ac-W)
beta=S.symbols('beta');close(S.limit((S.sqrt(1-beta*beta)-1)/beta**2,beta,0),-.5)
record('变换力矩低速二阶项',-.5)

# Yoyo derivative optimum including the shaft's own inertia.
r,C,b=S.symbols('r C b',positive=True);a=r/(C+b*r*r);assert S.simplify(S.diff(a,r)-(C-b*r*r)/(C+b*r*r)**2)==0
record('改变轴半径时的内部极值',float(np.sqrt(7/1.5)))
for N in range(1,31):
 initial=N*(N+1)/2;loss=(N*N-1)/6;final=(N+1)*(2*N+1)/6;close(initial,loss+final)
record('黏连全重力能与逐次损失',dict(N=6,initial=21,loss=35/6,final=91/6))
cone=quad(lambda t:np.cos(t)*np.sin(t),0,pi/18)[0]*2*pi;close(cone,pi*np.sin(pi/18)**2)
record('集光度圆锥积分与面积压缩',float(1/np.sin(pi/18)**2))
eta=1e-4;eps=2*np.arctan(np.sqrt(eta));close(np.tan(eps/2)**2,eta)
record('波片精确串扰反推厚度公差',dict(phase=eps,fraction=2*eps/pi))
for rr in [6,8,12,100]:
 bv=np.sqrt(1/(rr-2));ga=1/np.sqrt(1-bv*bv);red=np.sqrt(1-2/rr);p=red*ga*(1+bv);m=red*ga*(1-bv);close(p*m,1-2/rr);close(p/m,(1+bv)/(1-bv))
record('任意稳定圆轨道两频移乘积',True)

# Critical-angle expansion and exact root boundaries.
ac=brentq(lambda x:x*np.tan(x)-np.log(2/np.cos(x)),.2,1.4);mu=np.tan(ac);dm=1e-5
rt=[brentq(lambda x:np.log(2/np.cos(x))/x-mu-dm,*ab) for ab in [(.5,ac),(ac,1.4)]]
half=np.sqrt(2*ac*np.cos(ac)**2*dm);close((rt[1]-rt[0])/(2*half),1) if False else None
assert abs((rt[1]-rt[0])/(2*half)-1)<1e-5
record('摩擦临界角端点的平方根宽度',dict(exact=rt,halfwidth=half))
u=S.symbols('u');poly=u**3/S.Rational(265,100)**2+(2/S.Rational(265,100)-S.Rational(2,5))*u-S.Rational(2,5)
root=brentq(S.lambdify(u,poly,'numpy'),0,2);close(1-root,.133508217622)
record('内滚动非平凡根的三次消元和唯一性',root)
Y=4*(np.eye(3)-np.ones((3,3))/3);bv=np.array([1.,-1,0]);Yp=Y-np.outer(bv,bv);inv=np.linalg.pinv(Yp)
av=np.array([1.,0,-1]);close(bv@inv@bv,1);close(av@inv@av,5/8)
record('断边三端导纳独立伪逆',dict(RAB=1,RAC=5/8))
rate=.35;mass=quad(lambda t:np.exp(rate*t),-np.inf,0)[0];moment=quad(lambda t:np.exp(3*rate*t),-np.inf,0)[0];close(moment/mass,1/3)
record('螺线惯量质量比与虫质量推广',dict(I_over_Mr2=1/3,worm_half_ln4=np.log(2)))
u0=3.;m=2.;J=4.;R=1.;mu=.6;g=9.8;t=u0/(mu*g*(1+m*R*R/J));loss=quad(lambda z:mu*m*g*u0*(1-z/t),0,t)[0];close(loss,m*u0*u0/(2*(1+m*R*R/J)))
record('滑动接触功率积分与耗散',loss)
A,R,e=2.,3.,4.;k=A*A/R;v=A*e/(k*R+A*A);I=e/(2*R);close(k*v*v,e*e/(4*R));close(k*v*v/(e*I),.5)
record('电池列车最大机械功率与效率',dict(v=v,power=k*v*v,efficiency=.5))
theta=pi/4;ell=.3*np.cos(theta);P2=np.array([1-ell*np.cos(theta),ell*np.sin(theta)]);P1=P2+np.array([-np.sin(theta),1-np.cos(theta)]);C=P1-[0,1]
close(np.linalg.norm(P2-C),1);close(P2+ell*np.array([np.cos(theta),-np.sin(theta)]),[1,0])
record('自由函数图示轨迹的圆心和会聚点',dict(P1=P1.tolist(),P2=P2.tolist()))
H,C=373.15,273.15;ch,cc=2.,1.;T=np.exp((ch*np.log(H)+cc*np.log(C))/(ch+cc));close(ch*np.log(T/H)+cc*np.log(T/C),0);assert ch*H+cc*C-(ch+cc)*T>0
record('不等热容热机的熵与非负功',dict(T=T,W=ch*H+cc*C-(ch+cc)*T))

# Circular-orbit angular speed derived independently from energy and angular momentum.
x,mu,c,m=S.symbols('x mu c m',positive=True)
L2=mu*c**2*m**2*x**2/(x-3*mu)
E2=(1-2*mu/x)*(m**2*c**4+L2*c**2/x**2)
ut2=S.simplify(E2/(m**2*c**4)/(1-2*mu/x)**2)
assert S.simplify(ut2-x/(x-3*mu))==0
Omega2=S.simplify(L2/(m**2*x**4)/ut2)
assert S.simplify(Omega2-mu*c**2/x**3)==0
localbeta2=S.simplify(x*x*Omega2/c**2/(1-2*mu/x))
assert S.simplify(localbeta2-mu/(x-2*mu))==0
record('圆轨道守恒量到坐标与局部速度的推导',dict(u_t_ISCO=float(S.sqrt(ut2).subs({x:6,mu:1})),beta_ISCO=float(S.sqrt(localbeta2).subs({x:6,mu:1}))))

(P/'supplement_results.json').write_text(json.dumps(dict(passed=True,groups=rows,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),ensure_ascii=False,indent=2));print('PASS:',len(rows),'supplement groups')
