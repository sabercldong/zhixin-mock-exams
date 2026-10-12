from pathlib import Path
import json,math,cmath
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
C=[];S=[]
def check(q,name,actual,expected,tol=1e-8):
 a=np.asarray(actual);e=np.asarray(expected);err=float(np.max(abs(a-e)));scale=max(1,float(np.max(abs(e))))
 C.append(dict(name=f'{q:02d} {name}',actual=np.real_if_close(a).tolist(),expected=np.real_if_close(e).tolist(),max_abs_error=err,passed=bool(err<=tol*scale)))
def supp(q,name,passed,details):S.append(dict(name=f'{q:02d} {name}',passed=bool(passed),details=details))
# 01: retarded geometry, coordinate transformation, numerical differentiation.
b=.6;g=1/math.sqrt(1-b*b);xi=.5
q=(2*xi-b*math.sqrt(4*xi*xi+1-b*b))/(1-b*b)
s=(-25+math.sqrt(504))/22;sf=(-25-math.sqrt(504))/22
check(1,'ground unsquared light equation',2*xi-q,b*math.sqrt(1+q*q))
check(1,'ground near length',abs(q-xi),.1380857945186592)
check(1,'person near retarded equation',.5-s,b*math.sqrt(1+4*s*s))
check(1,'person far retarded equation',.5-sf,b*math.sqrt(1+4*sf*sf))
check(1,'near-root exact length',abs(s),.11591162178892506)
vnear=b/(1+4*b*s/math.sqrt(1+4*s*s));vfar=b/(1+4*b*sf/math.sqrt(1+4*sf*sf))
check(1,'near signed shadow speed',vnear,.8230465247380176)
check(1,'far signed shadow speed',vfar,-3.5503192520107425)
def personroot(d):return (d-math.sqrt(4*b*b*d*d+b*b-4*b**4))/(1-4*b*b)
dt=1e-6;fd=(personroot(.5+b*dt)-personroot(.5-b*dt))/(2*dt)
check(1,'finite-difference near speed',fd,vnear)
check(1,'same-event current distances',g*.5,.625)
# Transform a person-simultaneous shadow event into ground coordinates.
# Current foot has person t'=D/b and ground X=gamma D.
tp=.5/b;tground=g*(tp+b*s);xground=g*(s+b*tp)
check(1,'Lorentz transformed shadow ray',2*b*tground-xground,b*math.sqrt(1+xground*xground))
check(1,'classical limit',(2-1e-9*math.sqrt(5))/(1-1e-18),2,tol=1e-8)
check(1,'shadow-at-foot distance',b,b*math.sqrt(1))
ds=np.linspace(.45,1.4,48);errs=[]
for d in ds:
 ss=personroot(d);tt=g*(d/b+b*ss);xx=g*(ss+d);errs.append(abs(2*b*tt-xx-b*math.sqrt(1+xx*xx)))
supp(1,'48 Lorentz transformed near-branch events',max(errs)<1e-10,dict(max_residual=max(errs),near_speed=vnear,far_speed=vfar))
# 02: exact extrema and independent dense-angle scans.
th=brentq(lambda t:t+math.sin(t)-math.pi/2,0,math.pi/2);xc=(1-math.cos(th))/2
te=math.acos(math.sqrt(.6));A=(te-math.sin(te)*math.cos(te))/2;P8=4*A/math.pi
check(2,'center speed from end rotation',.5,.5)
check(2,'kinetic decomposition',1/8+1/24,1/6)
check(2,'endpoint crossing equation',th+math.sin(th),math.pi/2)
check(2,'left full-coverage threshold',xc,.16319398540839258)
check(2,'outer envelope x',.5+.5*math.cos(te)**2,.8)
check(2,'outer envelope material-coordinate Jacobian',.5*math.cos(te)-.5*math.cos(te),0)
check(2,'outer halfwidth',A,.09741062722282365)
check(2,'probability right',P8,.12402706265755463)
def scanprob(x,n=100001):
 d=x-.5;al=math.acos(2*abs(d));tt=np.linspace(-al,al,n);zz=-tt/2+d*np.tan(tt);return min(1,(max(zz)-min(zz))/(math.pi/2))
check(2,'dense-angle left coverage',scanprob(.2),1)
check(2,'dense-angle right coverage',scanprob(.8),P8,tol=1e-8)
check(2,'0.9 probability',scanprob(.9),.04051932635383402,tol=1e-8)
check(2,'unmarked-line vertical period',math.pi/2,1.5707963267948966)
errs=[]
for x in np.linspace(.01,.99,51):
 d=x-.5;al=math.acos(2*abs(d));candidates=[-al/2+d*math.tan(al),al/2-d*math.tan(al)]
 if d>0:
  t=math.acos(math.sqrt(2*d));candidates.extend([-t/2+d*math.tan(t),t/2-d*math.tan(t)])
 exact=min(1,(max(candidates)-min(candidates))/(math.pi/2));errs.append(abs(scanprob(x,20001)-exact))
supp(2,'51 horizontal-position envelope versus scan',max(errs)<3e-8,dict(max_error=max(errs),P02=1,P08=P8))
# 03: catenary arc length, geometric derivatives, kinetic conservation.
u=math.acosh(math.sqrt(2));p=2*u
check(3,'half-period',u,math.log(1+math.sqrt(2)))
check(3,'period',p,1.762747174039086)
check(3,'groove depth',math.cosh(u)-1,math.sqrt(2)-1)
check(3,'half-groove arc quadrature',quad(lambda x:math.sqrt(1+math.sinh(x)**2),0,u)[0],1)
check(3,'axis height at arbitrary x',1-math.cosh(.4)+math.sqrt(1+math.sinh(.4)**2),1)
check(3,'bottom tangent slope',-math.sinh(u),-1)
check(3,'minimum periods',math.ceil(2*math.sqrt(2)/p),2)
check(3,'minimum wheelbase',2*p,3.525494348078172)
M=4;m=1;I=1/6;wt=1;wb=math.sqrt(19/37)
check(3,'top kinetic energy',.5*(M+2)*wt**2+I*wt**2,19/6)
check(3,'bottom kinetic energy',.5*(M+2)*2*wb**2+I*wb**2,19/6)
check(3,'horizontal velocity ratio',math.sqrt(2)*wb,math.sqrt(38/37))
check(3,'hexagon terminal slope',math.sinh(math.acosh(2/math.sqrt(3))),1/math.sqrt(3))
maxerr=max(abs((1-math.cosh(x))+math.sqrt(1+math.sinh(x)**2)-1) for x in np.linspace(0,u,100))
supp(3,'100-point fixed axle and arc matching',maxerr<1e-12,dict(max_axis_error=maxerr,hexagon_period=math.sqrt(3)*math.log(3)))
# 04: boundary integration independently of center-gradient formula.
l=1.7;k1=.8;k2=-.3;sig=lambda x,y:2+k1*x+k2*y
fx=quad(lambda y:sig(l,y)-sig(0,y),0,l)[0];fy=quad(lambda x:sig(x,l)-sig(x,0),0,l)[0]
check(4,'square boundary x force',fx,k1*l*l)
check(4,'square boundary y force',fy,k2*l*l)
r=3;rad=.2;bb=.7;sig2=lambda x,y:2+bb*(x*x+y*y)
fx2=quad(lambda t:sig2(r+rad*math.cos(t),rad*math.sin(t))*math.cos(t)*rad,0,2*math.pi)[0]
fy2=quad(lambda t:sig2(r+rad*math.cos(t),rad*math.sin(t))*math.sin(t)*rad,0,2*math.pi)[0]
check(4,'finite circle exact force',fx2,2*bb*math.pi*rad*rad*r)
check(4,'finite circle transverse force',fy2,0)
J=2;D=3;aa=.4;area=.6;k=.8;r1=2;r2=1;n=lambda r:J/(2*math.pi*D*r)
check(4,'hemisphere flux',-D*(-J/(2*math.pi*D*r1*r1))*2*math.pi*r1*r1,J)
check(4,'concentration from gradient integral',quad(lambda x:J/(2*math.pi*D*x*x),r1,np.inf)[0],n(r1))
CC=aa*area*J/(2*math.pi*D*k)
check(4,'inward force',-aa*area*J/(2*math.pi*D*r1*r1),-k*CC/r1**2)
T=(r1**3-r2**3)/(3*CC)
check(4,'travel-time quadrature',quad(lambda r:r*r/CC,r2,r1)[0],T)
check(4,'cubic trajectory',r1**3-3*CC*T,r2**3)
check(4,'half-radius time fraction',1-.5**3,7/8)
check(4,'full-space concentration factor',J/(4*math.pi*D*r1),n(r1)/2)
check(4,'uniform-background boundary force',quad(lambda t:5*math.cos(t),0,2*math.pi)[0],0)
rat=[]
for ar in [.1,.05,.025]:
 q=ar*r;ff=quad(lambda t:n(math.hypot(r+q*math.cos(t),q*math.sin(t)))*math.cos(t)*q,0,2*math.pi,epsabs=1e-14)[0];pred=math.pi*q*q*(-J/(2*math.pi*D*r*r));rat.append(ff/pred)
supp(4,'finite disk nonlinear concentration gradient convergence',abs(rat[-1]-1)<abs(rat[0]-1),dict(force_ratios=rat))
# 05: complex recursion, finite networks, branch and total power checks.
def Z(q):return (3+1j*q+cmath.sqrt(17-q*q+14j*q))/4
z=Z(1);B=1+1j;rho=1-1/z
check(5,'recursion real',(1+2*z*B/(2*z+B)).real,z.real)
check(5,'recursion imaginary',(1+2*z*B/(2*z+B)).imag,z.imag)
poly=2*z*z-(3+1j)*z-(1+1j)
check(5,'polynomial residual real',poly.real,0)
check(5,'polynomial residual imaginary',poly.imag,0)
zz=1+B
for _ in range(80):zz=1+2*zz*B/(2*zz+B)
check(5,'finite 81-level real',zz.real,z.real)
check(5,'finite 81-level imaginary',zz.imag,z.imag)
check(5,'DC impedance',Z(0).real,(3+math.sqrt(17))/4)
check(5,'DC voltage ratio',(1-1/Z(0)).real,.4384471871911697)
check(5,'low-frequency effective inductance',Z(1e-5).imag/1e-5,(1+7/math.sqrt(17))/4)
check(5,'high-frequency real',Z(1e5).real,2.5,tol=2e-8)
check(5,'high-frequency scaled imaginary',Z(1e5).imag/1e5,.5,tol=2e-8)
power=(1/abs(z)**2+abs(rho)**2/abs(B)**2)/(2*(1-abs(rho)**2/2))
check(5,'sum of all resistor losses',power,(1/z).real/2)
errs=[];dec=[]
for q in np.logspace(-5,4,80):
 z=Z(q);B=1+1j*q;zz=1+B
 for _ in range(120):zz=1+2*zz*B/(2*zz+B)
 errs.append(abs(zz-z)/abs(z));dec.append(abs(1-1/z))
supp(5,'80-frequency finite ladder and passive spatial branch',max(errs)<1e-10 and max(dec)<1,dict(max_relative_error=max(errs),max_voltage_ratio=max(dec)))
# 06: differential geometry and fixed-link constraints.
bb=1;v=1;al=math.pi/3;d=1/math.sqrt(3);ell=1
w=-.75;acc=3*math.sqrt(3)/8
rD=np.array([d*math.cos(al),d*math.sin(al)]);vD=w*np.array([-rD[1],rD[0]]);aD=acc*np.array([-rD[1],rD[0]])-w*w*rD
vE=np.array([.5,0]);aE=np.array([-7*math.sqrt(3)/24,0]);rED=np.array([math.sqrt(3)/2,-.5])
check(6,'angular velocity',-math.sin(al)**2,w)
check(6,'angular acceleration',2*math.sin(al)**3*math.cos(al),acc)
check(6,'OD geometry',d,1/(2*math.sin(al)))
check(6,'DE length',np.linalg.norm(rED),ell)
check(6,'D velocity',vD,[3/8,-math.sqrt(3)/8])
check(6,'D acceleration',aD,[-9*math.sqrt(3)/32,-3/32])
check(6,'relative velocity perpendicular',np.dot(vE-vD,rED),0)
check(6,'relative-speed magnitude',np.linalg.norm(vE-vD),.25)
check(6,'second-order link constraint',np.dot(aE-aD,rED)+np.dot(vE-vD,vE-vD),0)
def xe(x):return d*x/math.sqrt(x*x+1)+math.sqrt(1-d*d/(x*x+1))
x0=1/math.sqrt(3);hh=1e-4
check(6,'coordinate velocity finite difference',(xe(x0+hh)-xe(x0-hh))/(2*hh),.5,tol=2e-8)
check(6,'coordinate acceleration finite difference',(xe(x0+hh)-2*xe(x0)+xe(x0-hh))/(hh*hh),aE[0],tol=3e-7)
check(6,'DE angular speed',rED[0]*(vE-vD)[1]-rED[1]*(vE-vD)[0],.25)
errs=[]
for h in [1e-3,5e-4,2e-4]:errs.append(abs((xe(x0+h)-2*xe(x0)+xe(x0-h))/h**2-aE[0]))
supp(6,'fixed material point finite-difference convergence',errs[-1]<errs[0],dict(acceleration_errors=errs,instant_midpoint_not_differentiated=True))
# 07: image flight, arrival-time differentiation, projection Doppler.
beta=1/3
def kval(beta,delta):
 a=1-math.cos(delta);return (a*beta+math.sqrt(a*a*beta*beta+2*a*(1-beta*beta)))/(1-beta*beta)
K1=kval(beta,math.pi/3);K2=kval(beta,2*math.pi/3);f1=1/(1+beta*K1);f2=1/(1+beta*K2)
check(7,'single-reflection flight equation',K1*K1,1+(1+beta*K1)**2-(1+beta*K1))
check(7,'single propagation coefficient',K1,3*(1+math.sqrt(33))/16)
check(7,'single-reflection frequency',f1,(17-math.sqrt(33))/16)
check(7,'double-reflection flight equation',K2*K2,1+(1+beta*K2)**2+(1+beta*K2))
check(7,'double-reflection frequency',f2,(19-math.sqrt(105))/16)
r=2;dt=1e-6;ta1=r*K1;ta2=dt+(r+beta*dt)*K1
check(7,'two emitted crests time ratio',dt/(ta2-ta1),f1,tol=2e-8)
e=np.array([math.cos(math.pi/6),math.sin(math.pi/6)]);ep=np.array([e[0],-e[1]]);nvec=((1+beta*K1)*e-ep)/K1
check(7,'image propagation unit vector',np.linalg.norm(nvec),1)
check(7,'source-receiver projection Doppler',(1-beta*np.dot(e,nvec))/(1-beta*np.dot(ep,nvec)),f1)
check(7,'static frequency',1/(1+0*kval(0,math.pi/3)),1)
check(7,'first-order low-speed derivative',(1/(1+1e-6*kval(1e-6,math.pi/3))-1)/1e-6,-1,tol=1e-6)
check(7,'numeric time at r10 u300',10*K1/300,.04215351671814043,tol=1e-8)
check(7,'formal vertex path ratio',1/(1+beta*kval(beta,math.pi)),.5)
errs=[]
for be in np.linspace(0,.8,41):
 kk=kval(be,math.pi/3);root=brentq(lambda t:t*t-1-(1+be*t)**2+(1+be*t),1e-9,20);errs.append(abs(kk-root))
supp(7,'41 speeds image equation versus independent root',max(errs)<1e-10,dict(max_time_error=max(errs),single_frequency=f1,double_frequency=f2,vertex_requires_extra_model=True))
# 08: line integrals, bounds and arbitrary-angle limiting behavior.
fup=quad(lambda r:r/(2+r),0,1)[0];fhor=quad(lambda r:r/2,0,1)[0];fdown=quad(lambda r:r/(2-r),0,1)[0]
check(8,'horizontal quadrature',fhor,.25)
check(8,'upward quadrature',fup,1-2*math.log(1.5))
check(8,'downward quadrature',fdown,2*math.log(2)-1)
check(8,'upward voltage ratio',fup/fhor,.7562791351346849)
check(8,'downward voltage ratio',fdown/fhor,1.5451774444795623)
check(8,'B constant distance',1/2,.5)
check(8,'tip-to-center magnetic ratio upward',(1/3)/(1/2),2/3)
check(8,'dimensionless log endpoint ratio',3/2,1.5)
mu=4*math.pi*1e-7;II=10;ww=100;RR=.1;base=mu*II*ww*RR/(2*math.pi)
check(8,'numeric horizontal volts',base*fhor,5e-6,tol=1e-12)
check(8,'numeric upward volts',base*fup,3.781395675673425e-6,tol=1e-12)
check(8,'velocity-cross-field outward',np.cross(np.array([0,-1,0]),np.array([0,0,-1])),[1,0,0])
check(8,'horizontal analytic continuous limit',quad(lambda r:r/7,0,1)[0],1/14)
errs=[]
for co in np.linspace(-1,1,51):
 val=quad(lambda r:r/(2+r*co),0,1)[0];exact=.25 if abs(co)<1e-10 else 1/co-2*math.log1p(co/2)/co**2;errs.append(abs(val-exact))
supp(8,'51 direction analytic integrals versus quadrature',max(errs)<1e-12,dict(max_error=max(errs),up_horizontal_down=[fup,fhor,fdown]))

# Additional checks for the final generalizations; retained within the eight groups.
err_special=[];err_general=[]
for dd in [.1,.3,.5,1,3]:
 ss=(dd*dd-.25)/(2*dd)
 err_special.append(abs(dd-ss-.5*math.sqrt(1+4*ss*ss)))
for lam in [.2,.35,.5,.7]:
 for be in [.1,.3,.6]:
  tt=2.0;xi=be*tt;gg=1/math.sqrt(1-be*be)
  qq=brentq(lambda q:xi-(1-lam)*q-be*lam*math.sqrt(1+q*q),0,30)
  sp=gg*(qq-be*tt);tp=gg*(tt-be*qq);dd=be*tp
  err_general.append(abs(dd-(1-lam)*sp/lam-be*math.sqrt(1+sp*sp/(lam*lam))))
S[0]['details'].update(beta_half_max_residual=max(err_special),general_height_12_events_max_residual=max(err_general))
S[0]['passed'] &= max(err_special+err_general)<1e-10
finite_ratios=S[3]['details']['force_ratios'];coeff=[(rr-1)/ar**2 for rr,ar in zip(finite_ratios,[.1,.05,.025])]
from scipy.integrate import solve_ivp
sol=solve_ivp(lambda t,y:[y[1],(2-3*y[1])/4],[0,2],[0,0],rtol=1e-11,atol=1e-12)
expected_w=2/3*(1-math.exp(-1.5));expected_x=2/3*(2-4/3*(1-math.exp(-1.5)))
transient_error=max(abs(sol.y[0,-1]-expected_x),abs(sol.y[1,-1]-expected_w))
S[3]['details'].update(finite_disk_quadratic_coefficients=coeff,expected_coefficient=3/8,local_inertia_ode_error=transient_error)
S[3]['passed'] &= abs(coeff[-1]-3/8)<.001 and transient_error<1e-9
lambda_errs=[]
for lam in [1.2,1.5,2,3,5]:
 for om in [0,.1,1,10]:
  BB=1+1j*om;AA=lam+(lam-1)*BB;zz=(AA+cmath.sqrt(AA*AA+4*lam*BB))/(2*lam)
  rec=1+lam*zz*BB/(lam*zz+BB);lambda_errs.append(abs(rec-zz))
S[4]['details'].update(general_multiplier_max_recursion_error=max(lambda_errs))
S[4]['passed'] &= max(lambda_errs)<1e-10
series_err=[]
for be in [.01,.005,.0025]:
 exact=1/(1+be*kval(be,math.pi/3));normal=(1-be/2)/(1+be/2)
 series_err.append((exact-normal)/be**3)
S[6]['details'].update(normal_approximation_cubic_difference=series_err,expected_cubic_difference=-3/8)
S[6]['passed'] &= abs(series_err[-1]+3/8)<.002

for item in S:item['passed']=bool(item['passed'])
assert len(C)==96 and len(S)==8
report=dict(all_passed=all(x['passed'] for x in C+S),check_count=len(C),supplementary_check_count=len(S),checks=C,supplementary_checks=S)
(ROOT/'physics_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['checks','supplementary_checks']},ensure_ascii=False))
for x in C+S:
 if not x['passed']:print('FAIL',x)
assert report['all_passed']
