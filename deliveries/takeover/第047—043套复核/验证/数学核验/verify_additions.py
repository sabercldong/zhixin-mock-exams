from pathlib import Path
import json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
checks=[]
def check(name,condition,detail=None):
 assert condition,(name,detail)
 checks.append(dict(name=name,pass_=bool(condition),detail=detail))
def near(name,a,b,tol=1e-8):check(name,abs(a-b)<tol,dict(actual=float(a),expected=float(b)))

# Independent Lagrange equation and force reconstruction for the eccentric wheel.
q,qd,qdd,r,h,m,I,g,a=sp.symbols('q qd qdd r h m I g a',real=True)
J=I+m*(r*r+h*h-2*r*h*sp.cos(q))
V=m*g*(r-h*sp.cos(q))+m*a*(r*q-h*sp.sin(q))
lag=J*qdd+sp.diff(J,q)*qd**2/2+sp.diff(V,q)
expected=J*qdd+m*(a*(r-h*sp.cos(q))+g*h*sp.sin(q)+r*h*sp.sin(q)*qd**2)
check('wheel Lagrange equation',sp.simplify(lag-expected)==0)
def wf(q,z):
 J=.5+1.25-np.cos(q);d=1-.5*np.cos(q)
 dd=-(3*d+5*np.sin(q)+.5*np.sin(q)*z)/J
 f=-3-d*dd-.5*np.sin(q)*z;N=10+.5*np.sin(q)*dd+.5*np.cos(q)*z
 return dd,f,N
def zenergy(q):return 2*(5-(10*(1-.5*np.cos(q))+3*(q-.5*np.sin(q))))/(1.75-np.cos(q))
z=zenergy(-.3);dd,f,N=wf(-.3,z)
near('wheel speed squared',z,.5874238150917502)
near('wheel friction ratio',abs(f)/N,.28318975836631427)
near('initial wheel ratio',abs(wf(0,0)[1])/wf(0,0)[2],.2)
slip=brentq(lambda q:abs(wf(q,zenergy(q))[1])/wf(q,zenergy(q))[2]-.25,-.3,0)
check('wheel slip occurs before candidate angle',-.3<slip<0,{'angle':slip})
sol=solve_ivp(lambda t,y:[y[1],wf(y[0],y[1]**2)[0]],(0,.45),[0,0],rtol=1e-11,atol=1e-12)
for k in np.linspace(0,len(sol.t)-1,5,dtype=int):
 qq,qqd=sol.y[:,k];E=.5*(1.75-np.cos(qq))*qqd**2+10*(1-.5*np.cos(qq))+3*(qq-.5*np.sin(qq))
 near('wheel effective energy '+str(k),E,5,1e-9)

# Trace the un-squared finite-source mapping instead of trusting its cubic.
s=brentq(lambda q:q/2/(np.sqrt(1-q*q)*np.sqrt(1-q*q/4)+q*q/2)-.5,.001,.999)
near('finite bright disk cubic',-s**3+2.25*s*s-1,0)
near('bright area',s*s,.7107675827043148)
check('source disk map monotone',all(np.diff([q/2/(np.sqrt(1-q*q)*np.sqrt(1-q*q/4)+q*q/2) for q in np.linspace(0,.99,60)])>0))

# Propagation/refraction matrix checks, including image condition and magnification.
for nw in [1,1.33]:
 B=.5/nw+.003/1.5;v=-B/(1+2*B);my=1/(1+2*B)
 M=np.array([[1,v],[0,1]])@np.array([[1,0],[2,1]])@np.array([[1,B],[0,1]])
 near('lens imaging '+str(nw),M[0,1],0);near('lens magnification '+str(nw),M[0,0],my)
 near('lens determinant '+str(nw),np.linalg.det(M),1)

# Matched load and inverse inertia are different models from the original tasks.
near('matched load current',.8/(.2+.2),2)
near('matched load output power',(.8/.4)**2*.2,.8)
near('inverse inertia',((2**2-1)/(2.5-1)-1),1)
R,E,R0=sp.symbols('R E R0',positive=True)
near_expr=sp.diff(E**2*R0/(R+R0)**2,R0)-E**2*(R-R0)/(R+R0)**3
check('matched load derivative',sp.simplify(near_expr)==0)

# Thermodynamic integrability plus heat capacities; do not substitute this into the original model.
A,T,Vv,Vs=sp.symbols('A T V Vs',positive=True)
U=A*T**2*(3+sp.log(Vv/Vs));p=A*T**2/Vv
check('comparison model integrability',sp.simplify(sp.diff(U,Vv)-(T*sp.diff(p,T)-p))==0)
Cv=sp.diff(U,T);Cp=Cv+T*sp.diff(p,T)**2/(-sp.diff(p,Vv))
check('comparison Cp-Cv',sp.simplify(Cp-Cv-4*A*T)==0)

# Direct focus quadrature, with finite positive transverse momentum on selected branch.
n=1.5;f0=np.pi/(2*np.sqrt(2*(n*n-1)/n));near('paraxial focus',f0,1.2167336027920836)
focus=[]
for amp in [.1,.05,.025]:
 P=(n+amp*amp)/(1+n*amp*amp)
 def kernel(t):
  y=amp*np.sin(t);b=y*y
  py2=(n*n*(1-b*P)**2-(P-b)**2)/(1-b*b)
  return (n*n*b*(1-b*P)+(P-b))*amp*np.cos(t)/((1-b*b)*np.sqrt(py2))
 fexact=quad(kernel,0,np.pi/2,epsabs=1e-9)[0];D=(fexact/f0-1)/(amp*amp)
 focus.append(dict(amplitude=amp,focus=fexact,coefficient=D))
 check('focus coefficient '+str(amp),abs(D-.8125)<.002,focus[-1])
check('focus coefficient converges',abs(focus[-1]['coefficient']-.8125)<abs(focus[0]['coefficient']-.8125))

# Integral geometric checks for spiral cap and the two principal moments.
rmin=4/(20*np.sqrt(1.25));near('spiral minimum radius',rmin,.17888543819998318)
near('spiral terminal angle',np.log(1/rmin)/.5,3.4420193761824107)
near('spiral time',np.sqrt(1.25)/(.5*2)*(1-rmin),.9180339887498949)
d=1/np.sqrt(2);K=1+d
S=quad(lambda x:(K*K-x*x)/K,-d,d)[0]
Jx=quad(lambda x:(K*K-x*x)**3/(12*K**3),-d,d)[0]
Jy=quad(lambda x:x*x*(K*K-x*x)/K,-d,d)[0]
near('shape principal x',Jx/S,.21775200981598977)
near('shape principal y',Jy/S,.15857864376269049)
near('perpendicular axis theorem',(Jx+Jy)/S,.37633065357868026)

# Numerical force closure in the light-wedge limit and differentiated two-layer circuit.
th=np.pi/6;k=.5;as_=10*np.sin(th)/(k+np.sin(th)**2)
near('light wedge relative acceleration',as_,6.666666666666667)
near('light wedge normal',10*k*np.cos(th)/(k+np.sin(th)**2),5.773502691896258)
near('light wedge vertical acceleration',-as_*np.sin(th),-10/3)
w=.18028508756;R1=w;R2=1-w;eps=1e-5
for which in [1,2]:
 rr1=R1/(1+eps) if which==1 else R1;rr2=R2/(1+eps) if which==2 else R2
 dI=(1/(rr1+rr2)-1)/eps;dV=(rr2/(rr1+rr2)/R2-1)/eps
 near('conductivity current '+str(which),dI,w if which==1 else 1-w,2e-6)
 near('conductivity voltage '+str(which),dV,w if which==1 else -w,2e-6)

# Integrate the rectangular membrane's mode; equality is periodic average, not instantaneous.
near('square membrane mode energy',.25*(2*2*np.pi*np.pi),np.pi*np.pi)
out=Path(__file__).with_name('additional_math_verification.json')
out.write_text(json.dumps(dict(check_count=len(checks),checks=checks,focus_quadrature=focus),ensure_ascii=False,indent=2))
print(len(checks),'independent checks passed')
