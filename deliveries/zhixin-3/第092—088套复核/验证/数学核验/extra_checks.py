from pathlib import Path
import importlib.util,json,math
from fractions import Fraction
from itertools import product
from scipy.optimize import brentq
from scipy.integrate import quad
import sympy as sp
W=Path(__file__).parent
checks=[]
def record(n,q,name,actual,expected,tol=1e-8):
 passed=abs(float(actual)-float(expected))<=tol*max(1,abs(float(expected)))
 checks.append(dict(set=n,question=q,check=name,actual=str(actual),expected=str(expected),passed=passed));assert passed,checks[-1]
# Root enumeration scans every monotone branch and includes rim entry/exit.
lam=.3;D=math.pi/6;A=math.acos(lam);T=math.acos(math.sqrt(lam));rim=math.sqrt(1-lam*lam)
g=T-math.sqrt(lam*(1-lam));pstar=g-D

def window(p):
 ev=[p-rim,p+rim]
 for k in range(-4,5):
  z=p-k*D
  for lo,hi in zip([-A,-T,T,A],[-T,T,A]):
   fn=lambda u:u-lam*math.tan(u)-z
   if fn(lo)*fn(hi)<0:ev.append(brentq(fn,lo,hi)+k*D)
 ev=sorted(ev)
 return max(b-a for a,b in zip(ev,ev[1:]))
u=brentq(lambda u:u-lam*math.tan(u)-pstar,0,.1);bound=rim-lam*math.tan(u)
scan=max(window(D*i/10000) for i in range(10000))
record(92,1,'10000相位、三单调支与轮缘边界的独立事件扫描',scan,bound,3e-5)
assert window(pstar+1e-9)>window(pstar-1e-9)
record(92,1,'单侧极限下确界',1/bound,1.05268360521)
# Fourth-order axial expansion; transverse coefficient from harmonic reconstruction.
z=sp.symbols('z');half=sp.Rational(1,2)
f=sum((1+(z+a)**2)**sp.Rational(-3,2) for a in [-half,half]);norm=f/f.subs(z,0)
c4=sp.simplify(sp.diff(norm,z,4).subs(z,0)/24)
record(92,6,'亥姆霍兹临界轴向四阶',c4,-sp.Rational(144,125))
record(92,6,'无源区径向四阶重构',c4*sp.Rational(24,64),-sp.Rational(54,125))
# Charging heat from an independent RC current integration.
beta=.8;R=.7;C=.3;ab=math.sqrt(beta/C);J=1.;om=2.;tau=R*C/(1+beta)
heat=quad(lambda t:R*(C*ab*om/(1+beta)/tau*math.exp(-t/tau))**2,0,40*tau)[0]
record(92,3,'充电电阻耗散积分',heat,.5*J*om**2*beta/(1+beta))
# Nodal KCL, independent of the spectral counting in the newly solved exercises.
spec=importlib.util.spec_from_file_location('v89',W/'verify_089.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for m,target in [(1,Fraction(15,32)),(2,Fraction(7,12))]:
 record(89,4,f'四维汉明距离{m}节点方程',v.hypercube_resistance(4,(0,0,0,0),tuple([1]*m+[0]*(4-m))),target)
# Arbitrary mass distribution: numerical integration vs moment expression.
h=1.4;radius=6.;th=.8;gravity=9.8
rho=lambda s:2+s/h
M1=quad(lambda s:s*rho(s),0,h)[0];M2=quad(lambda s:s*s*rho(s),0,h)[0]
w2=gravity/math.tan(th)/(radius-M2/M1*math.cos(th))
torque=quad(lambda s:w2*(radius-s*math.cos(th))*s*math.sin(th)*rho(s)-gravity*s*math.cos(th)*rho(s),0,h)[0]
record(89,5,'线性密度杆逐元力矩平衡',torque,0)
for x2 in [2.,-1.01]:
 y1=3.;y2=4-x2*x2
 def height(y):return (x2*x2*y1-y)/(x2*x2-1)
 record(89,6,f'像顶点误差放大x2={x2}',height(y2+.01)-height(y2),-.01/(x2*x2-1))
# Analytic power derivative and endpoint comparison on the physical liquid interval.
k=1.380649e-23;T0=293.15;mass=.01801528/6.02214076e23
C0=2.45e6*mass*(2340/(k*T0))*math.sqrt(8*k*T0/(math.pi*mass))/4
E=lambda d:C0*math.exp(-.06*d)*math.sqrt(T0/(T0-d))
def dW(d):
 t=T0-d;ep=E(d)*(-.06+1/(2*t))
 return T0/t**2*(E(d)-20*d)+d/t*(ep-20)
root=brentq(dW,10,20)
record(90,7,'解析导数根与数值优化交叉核验',root,18.328025536718002)
assert all(dW(20*i/1000)>0 for i in range(917))
assert all(dW(20*i/1000)<0 for i in range(917,1001))
# Four-dimensional force exponent/potential degree consistency in Q88 variation.
scale,degree=1.3,2.2
force=lambda r:degree*r**(-degree-1)
dU=( -(scale+1e-6)**(-degree)+(scale-1e-6)**(-degree))/(2e-6)
record(88,2,'r^(-s)势能对应r^(-s-1)力',dU,force(scale),1e-7)
(W/'extra_results.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(len(checks),'additional independent checks passed')
