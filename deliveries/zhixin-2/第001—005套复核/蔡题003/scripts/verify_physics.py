"""用数值积分、矩阵恒等式和接触可行性验证第003套的关键结论。"""
from pathlib import Path
import json, numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq,linprog
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,ok,details):
 assert bool(ok), (name,details)
 checks.append(dict(name=name,passed=True,details=details))
e=1.6e-19;m=207*.91e-30;hb=6.64e-34/(2*np.pi);A=9e9*65*e**2;c=3e8
v=A/hb;r=hb**2/(m*A);E=-A/(2*r);gr=1/np.sqrt(1-(v/c)**2);rr=r/gr
check('Q1 牛顿圆轨道与相对论轨道双约束',np.allclose([m*v*v/r,A/r/r],[A/r/r,A/r/r]) and abs(gr*m*v*rr/hb-1)<1e-13 and abs(gr*m*v*v*rr/A-1)<1e-13,dict(gap_eV=-.75*E/e,v=v,r_N=r,r_R=rr,radius_decrease=1-1/gr,recoil_percent=m/(m+2.34e-25)*100))
for n1,n2,r1,r2 in [(50,75,3,8),(1,1,1,1),(2,1,4,7)]:
 # solve three constraints without using derived ratio
 u3=10;n3=30
 d1,d2,i3=np.linalg.solve([[1,1,0],[n1*n1/r1,-n2*n2/r2,0],[n1*n1/r1,0,-n3]],[u3/n3,0,0])
 p1=n1*n1*d1*d1/(2*r1);p2=n2*n2*d2*d2/(2*r2)
 check('Q2 磁通分流及输入功率',abs(d1/d2-n2*n2*r1/(n1*n1*r2))<1e-12 and abs(u3*i3/2-p1-p2)<1e-12,dict(parameters=[n1,n2,r1,r2],flux_ratio=d1/d2,power_ratio=p1/p2))
for a in [.2,1,3]:
 bx=lambda x:.5*(1+np.tanh(x/a));br=lambda x:-.5*.7*.5/a/np.cosh(x/a)**2
 force=quad(lambda x:-2*np.pi*.7*5*2*br(x),-25*a,25*a)[0]
 expected=np.pi*.7**2*5*2
 check('Q3 不同边缘宽度的电流元积分',abs(force/expected-1)<1e-11,dict(width=a,force=force,expected=expected))
gamma=5/3;eta=.25;const=(gamma-1)*eta/gamma
p=lambda s:const+(1-const)*s**-gamma
K=lambda s:(1-const)/(gamma-1)*(1-s**(1-gamma))+(const-.5-eta)*(s-1)
s2=brentq(lambda s:1.5*(1-s**(-2/3))-.5*(s-1),1.01,3)
s3=brentq(K,1.01,2)
sol=solve_ivp(lambda x,y:[((gamma-1)*eta-gamma*y[0])/x,y[0]-.5-eta],[1,2],[1,0],rtol=1e-11,atol=1e-13,dense_output=True)
ys=sol.sol(np.linspace(1,2,50));err=np.max(abs(ys[0]-p(np.linspace(1,2,50))))
check('Q4 含摩擦热的第一定律数值积分',err<1e-9 and abs(sol.sol(s3)[1])<1e-9 and abs(1.5*p(s3)*s3+ .5*(s3-1)-1.5)<1e-12,dict(s1=1.6,s2=s2,s3=s3,p3=p(s3),ODE_error=err,entropy_change_per_molR=1.5*np.log(p(s3)*s3)+np.log(s3)))
for n in [1.2,4/3,1.8,3]:
 r=1;f=n*r/(2*(n-1));D=5*f if n<=2 else 3.5
 S=np.array([[1.,0],[-(n-1)/r,1.]]);T=lambda d:np.array([[1.,d],[0,1.]])
 M=S@T(2*r/n)@S
 roots=np.roots([1,-D,f*D]);mag=[]
 for l in roots:
  total=T(D-l-r)@M@T(l-r);mag.append(total[0,0]);check('Q5 两面折射直接成像检查',abs(total[0,1])<1e-12 and abs(total[0,0]+(D-l)/l)<1e-12,dict(n=n,D=D,l=float(l),magnification=float(total[0,0])))
 check('Q5 两像放大率乘积',abs(np.prod(mag)-1)<1e-12,dict(n=n,product=np.prod(mag)))
def Bx(b):
 g=1/np.sqrt(1-b*b);return np.array([[g,-g*b,0],[-g*b,g,0],[0,0,1.]])
def By(b):
 g=1/np.sqrt(1-b*b);return np.array([[g,0,-g*b],[0,1,0],[-g*b,0,g]])
metric=np.diag([1.,-1.,-1.])
for b in [.001,.05,.2,.5,.8]:
 g=1/np.sqrt(1-b*b);M2=By(b)@Bx(b);M=By(-b)@Bx(-b)@By(b)@Bx(b)
 dX=np.array([-M[0,2]/M[0,0],0,1.]);out=M@dX;Q=g**3-2*g*g+2
 analytic=np.array([(g-2)*(g*g-1),1+g-g*g])/Q
 rot=M2[1:,1:]-np.outer(M2[1:,0],M2[0,1:])/(M2[0,0]+1)
 angle=np.arctan2(rot[1,0],rot[0,0]);expected=np.arctan((g*g-1)/(2*g))
 check('Q6 洛伦兹度规、同时端点和二步转动',np.max(abs(M.T@metric@M-metric))<2e-12 and abs(out[0])<1e-12 and np.max(abs(out[1:]-analytic))<1e-12 and abs(angle-expected)<1e-12,dict(beta=b,clock_vector=out[1:].tolist(),wigner_angle=angle,residual_velocity=(-M[0,1:]/M[0,0]).tolist()))
N=6;mu=.65;theta=(np.arange(N+1)+.5)*np.pi/(2*N+1);w=np.arange(N+1)+.5;h=.5/np.tan(theta[0]);norm=h*np.cos(theta)+w*np.sin(theta);fric=h*np.sin(theta)-w*np.cos(theta)
check('Q7 原拱所有面摩擦比',np.all(np.diff(fric/norm)>0),dict(ratios=(fric/norm).tolist(),mu_min=float(np.max(fric/norm))))
rows=[];rhs=[]
for a,wi in zip(theta,w):
 for sign in [1,-1]:
  rows.append([sign*np.sin(a)-mu*np.cos(a),(sign*np.cos(a)+mu*np.sin(a))/2]);rhs.append((sign*np.cos(a)+mu*np.sin(a))*wi)
 rows.append([-np.cos(a),np.sin(a)/2]);rhs.append(wi*np.sin(a))
res=linprog([0,-1],A_ub=rows,b_ub=rhs,bounds=[(0,None),(0,None)],method='highs')
a=(1+mu*np.tan(theta[0]))/(mu-np.tan(theta[0]));tc=(a+mu*(2*N+1))/(a+mu)
check('Q7 全接触线性规划与候选临界比较',res.success and abs(res.x[1]-tc)<1e-10 and np.all(np.asarray(rhs)-np.asarray(rows)@res.x>-1e-10),dict(h=res.x[0],critical_T_G=res.x[1],slack=(np.asarray(rhs)-np.asarray(rows)@res.x).tolist()))
B0=2.;ell=.7;k=1.3;omega=3.;R=2.;v=.4;time=.8;x=v*time
Phi=lambda t:ell*quad(lambda X:B0*np.cos(omega*t-k*X),v*t,v*t+ell)[0]
eps=-(Phi(time+1e-5)-Phi(time-1e-5))/(2e-5)
xi=omega*time-k*(x+ell/2);analytic=2*B0*ell/k*np.sin(k*ell/2)*(omega-k*v)*np.sin(xi)
F=eps/R*ell*B0*(np.cos(omega*time-k*(x+ell))-np.cos(omega*time-k*x));C=4*B0**2*ell**2/(k*R)*np.sin(k*ell/2)**2
check('Q8 移动面积积分与磁力直接计算',abs(eps-analytic)<1e-9 and abs(F-C*(omega-k*v)*np.sin(xi)**2)<1e-9 and abs((omega/k-v)*F-eps**2/R)<1e-9,dict(emf=eps,force=F))
for phase in [np.pi/3,2*np.pi/3,4*np.pi/3]:
 sums=[sum(np.sin(t-j*phase)**2 for j in range(3)) for t in np.linspace(0,2*np.pi,100)]
 check('Q8 三框瞬时起伏抵消',max(abs(np.asarray(sums)-1.5))<1e-12,dict(phase_spacing=phase,max_error=max(abs(np.asarray(sums)-1.5))))
report=dict(all_passed=True,method='独立数值积分、直接矩阵乘法、全部接触线性规划；不以扫描答案作为判据',checks=checks)
(ROOT/'physics_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'checks; Q4',s2,s3,'Q7',tc)
