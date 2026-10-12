from pathlib import Path
import math,json
import numpy as np
import sympy as s
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
W=Path(__file__).parent;R=[]
for n in [47,46,45,44,43]:(W/str(n)).mkdir(exist_ok=True)
def ck(n,q,name,got,want,tol=1e-8):
 err=float(np.max(np.abs(np.asarray(got)-np.asarray(want))))
 assert err<tol,(n,q,name,got,want,err,tol)
 R.append(dict(set=n,question=q,check=name,max_error=err,tolerance=tol))
def ident(n,q,name,a,b):
 assert s.simplify(a-b)==0,(n,q,name,s.simplify(a-b))
 R.append(dict(set=n,question=q,check=name,symbolic='pass'))
x=s.symbols('x',positive=True);t=s.symbols('t',positive=True)
# 047: all eight questions, with independent equations or integrals.
z=brentq(lambda z:1/math.sqrt(1+9*z*z)+1/math.sqrt(1+z*z)-1.6,0,3)
ck(47,1,'rod equal lengths and fixed span',1/math.sqrt(1+9*z*z)+1/math.sqrt(1+z*z),1.6)
ck(47,1,'height from original 1.6-m span',.5*(3*z/math.sqrt(1+9*z*z)+z/math.sqrt(1+z*z)),.549720317628)
th=math.radians(35);v=40;h=15;g=10;al=math.pi/6
A=v*(math.sin(th)+math.cos(th)*math.tan(al));tt=(A-math.sqrt(A*A-2*g*h))/g
xx=v*math.cos(th)*tt;yy=v*math.sin(th)*tt-g*tt*tt/2
ck(47,2,'ballistic intersection',[yy,xx],[h-xx*math.tan(al),12.291935],1e-6)
ck(47,2,'energy independent of roof intercept',(v*math.cos(th))**2+(v*math.sin(th)-g*tt)**2,v*v-2*g*yy)
for ni,rad in [(1.5,.1),(1.7,.03),(1.9,.2)]:
 phi=(1-ni)/rad;y=.001;angle=-phi*y
 ck(47,3,'virtual focus ray intercept',-y/angle,1/phi)
for aa,rr in [(.2,1),(1,1),(8,1)]:
 bg=-quad(lambda q:aa*q/(aa*aa+q*q)**1.5,0,rr)[0]
 ba=quad(lambda zz:.5*rr*rr/(rr*rr+zz*zz)**1.5,-aa,aa)[0]
 ck(47,4,'finite disk and current-ring integration',[bg,ba],[aa/math.sqrt(aa*aa+rr*rr)-1,aa/math.sqrt(aa*aa+rr*rr)])
 ck(47,4,'microscopic centre field difference',ba-bg,1)
Rgas=8.31;T0=373.;L=40800.;Cv=3*Rgas;Cl=75.8
dn=(L/(Rgas*T0)-1)/T0;Q=Cl+Cv+dn*(L-Rgas*T0)
ck(47,5,'one-K differential phase calculation',[dn,Q],[.0326082074364,1330.071485389],1e-8)
y=s.symbols('y');series=s.series(s.log(1+2*s.cosh(y)),y,0,6).removeO()
ident(47,6,'spin-1 log partition expansion',series,s.log(3)+y*y/3-y**4/36)
for lam in [1,4/3,2]:
 cc=np.linspace(0,1,100001);N=1-(1+2*cc-3*cc*cc)/lam
 ck(47,7,'support quadratic minimum',np.min(N),1-4/(3*lam),1e-9)
for lam in [4,5,12,100]:
 c=(lam+3-math.sqrt(lam*lam-3*lam))/(lam+1)
 ck(47,8,'physical nonzero relative-rest root',lam*(2-c)*c,(3-c)**2)
for c in [.01,.3,.540302305868,1]:
 om=1;gr=10;w=math.sqrt((6*gr*c-om*om*c*c)/(3-c*c))
 for ww in [-w,w]:
  u=c*(ww+om)/3
  ck(47,8,'paired ring energy and magnetic impulse',[1.5*u*u-u*ww*c+.5*ww*ww,3*u-c*ww],[gr*c,om*c])
# 046
G=6.67430e-11;rho=5500;RE=6.4e6;ME=4/3*math.pi*RE**3*rho;MM=7.35e22;period=27.3*86400
rr=(G*(ME+MM)*period**2/(4*math.pi**2))**(1/3)
ck(46,1,'two-body relative acceleration',4*math.pi**2*rr/period**2,G*(ME+MM)/rr**2)
for eta,kap in [(.2,.4),(.5,.5),(.8,.15)]:
 m=2;a=3;r=1;d=r*(1-eta);I=kap*m*r*r;f=-m*a*I/(I+m*d*d);alpha=d*f/I
 ck(46,2,'left detached initial rolling equations',f+m*a,-m*d*alpha)
ck(46,3,'small-electrode boundary voltage ratio',.5*math.log(2000)/math.log(1000),.5501716659439969)
for mu in [.2,.5,.8]:
 # Finite-difference check that all four logarithmic sources give zero radial derivative.
 def pot(rad,th):
  z=rad*complex(math.cos(th),math.sin(th))
  return sum(sign*math.log(abs(z-a)) for a,sign in [(-mu,-1),(mu,1),(-1/mu,-1),(1/mu,1)])
 for th in [.3,1,2]:
  ee=1e-5;der=(pot(1+ee,th)-pot(1-ee,th))/(2*ee)
  ck(46,3,'same-sign image insulated boundary',der,0,2e-8)
I0,I1,J,xxs=s.symbols('I0 I1 J x',positive=True)
ident(46,4,'rotating free tube extra stiffness',s.diff(J**2/(2*(I0+I1*xxs)),xxs,2).subs(xxs,0),J**2*I1**2/I0**3)
ident(46,5,'parabolic area derivative',s.diff(s.Rational(4,3)*t**s.Rational(3,2),t),2*s.sqrt(t))
for angle in [.1,.5,1.3]:
 ii=math.asin(math.sin(angle)/2)
 doutdi=2*math.cos(ii)/math.cos(angle)
 dO_ratio=math.sin(angle)*doutdi/math.sin(ii)
 ck(46,6,'radiance angular Jacobian',math.cos(angle)*dO_ratio,4*math.cos(ii))
for nn,N in [(4/3,1),(4/3,2),(2.03,2)]:
 aa=math.asin(math.sqrt(((N+1)**2-nn*nn)/(N*(N+2))));ii=math.asin(math.sin(aa)/nn)
 ck(46,7,'rainbow stationary derivative',2-2*(N+1)*math.cos(aa)/(nn*math.cos(ii)),0)
mp=1.672622e-27;mhe=6.644657e-27;me=9.109384e-31;c=299792458
Q=(4*mp-mhe-2*me)*c*c;Ehe=mhe*c*c+Q;p=math.sqrt(Q*(Q+2*mhe*c*c))/c;ue=p/(4*mp)
ck(46,8,'reaction invariant helium momentum',Ehe*Ehe-p*p*c*c,(mhe*c*c)**2,1e-28)
R.append(dict(set=46,question=8,check='consistent exhaust energy bookkeeping',u_he=p*c*c/Ehe,u_eff=ue,F=1e-3*ue,fuel_ratio=math.exp(c/ue*math.atanh(.2))-1,S_ly=15*math.sinh(ue/(2*c)*math.log(101))))
# 045
ck(45,1,'barycentric stellar amplitude',(2*math.pi*6.67e-11/(365.25*86400))**(1/3)*6e24/(2e30+6e24)**(2/3),.08952,1e-4)
for th,a in [(math.pi/6,0),(math.pi/6,8),(math.pi/4,3)]:
 ar=(9.8*math.sin(th)-a*math.cos(th))/1.5;f=-.5*ar
 ck(45,2,'rolling accelerated slope tangential equation',ar,9.8*math.sin(th)-a*math.cos(th)+f)
for om in [3,5,10]:
 wm=.7;roots=[(om-math.sqrt(om*om-4*wm))/2,(om+math.sqrt(om*om-4*wm))/2]
 ck(45,3,'both gyro roots',[sum(roots),math.prod(roots)],[om,wm])
for m1,m2 in [(3.2,3.55),(.2,3.55)]:
 a=.696;c0=.313;pp=a-c0;qq=a+c0;M=m1+m2;D=m2-m1
 KI=9.8*np.diag([M/(2*qq),M/(2*pp)])-9.8*D/(4*c0)*np.array([[1,-1],[-1,1]])
 ck(45,4,'first vertical stiffness determinant',np.linalg.det(KI),9.8**2*M/(4*pp*qq)*(M-a*D/c0),1e-9)
 eig=np.linalg.eigvalsh(np.diag([1/math.sqrt(m1),1/math.sqrt(m2)])@KI@np.diag([1/math.sqrt(m1),1/math.sqrt(m2)]))
 assert (eig[0]>0)==(D/M<c0/a)
 if m1==3.2:
  KII=9.8*np.diag([M/(2*pp),M/(2*qq)])+9.8*D/(4*c0)*np.array([[1,-1],[-1,1]])
  ev=np.linalg.eigvalsh(np.diag([1/math.sqrt(m1),1/math.sqrt(m2)])@KII@np.diag([1/math.sqrt(m1),1/math.sqrt(m2)]))
  ck(45,4,'second vertical numeric normal frequencies',np.sqrt(ev),[3.1573,5.28014],.0002)
for ll,rad in [(2,1),(5,.3),(1.1,1)]:
 d=math.sqrt(ll*ll-rad*rad)
 ck(45,5,'cylinder right-end distance ratio',(ll+rad+d)/(ll+rad-d),(ll+d)/rad)
 # Circumference must be equipotential.
 vals=[]
 for th in np.linspace(0,2*math.pi,31):
  z=ll+rad*complex(math.cos(th),math.sin(th))
  vals.append(math.log(abs(z+d)/abs(z-d)))
 ck(45,5,'entire metal circumference equipotential',vals,np.full(len(vals),math.acosh(ll/rad)),1e-12)
TT,V=s.symbols('T V',positive=True);p0=TT*TT/V;u0=3*TT*TT
ident(45,6,'thermodynamic consistency failure is p',TT*s.diff(p0,TT)-p0-s.diff(u0,V),p0)
r1,r2,h0,rg,sg=s.symbols('r1 r2 h0 rho_g sigma',positive=True)
z=rg*(x*x-r1*r1)/(8*sg)+(h0-rg*(r2*r2-r1*r1)/(8*sg))*s.log(x/r1)/s.log(r2/r1)
ident(45,7,'annular membrane static PDE',s.diff(z,x,2)+s.diff(z,x)/x,rg/(2*sg))
ident(45,7,'outer and inner membrane boundaries',z.subs(x,r1),0);ident(45,7,'inner membrane boundary',z.subs(x,r2),h0)
n,b,py=s.symbols('n beta p_y',positive=True);eps=s.symbols('e');px=n-eps*py**2/(2*n)-eps*(n*n-1)*b
disp=n*n*(1-eps*b*px)**2-(px-eps*b)**2-(1-eps**2*b*b)*eps*py**2
ident(45,8,'moving medium paraxial dispersion order',s.expand(disp).coeff(eps,1),0)
# 044 independent integrals / ODE / stationary conditions.
u=s.symbols('u',positive=True)
tfun=(s.log(u)+(1-u**-2)/2)/2
xfun=(s.Rational(4,3)-1/u-1/(3*u**3))/2
yfun=(s.log(u)+(u**-4-1)/4)/4
ident(44,1,'parametric trajectory vx',s.diff(xfun,u)/s.diff(tfun,u),1/u)
ident(44,1,'parametric trajectory vy',s.diff(yfun,u)/s.diff(tfun,u),(1-u**-2)/2)
for aa in [.1,.5,2]:
 rr=2;v=3;N=1/(rr*math.sqrt(1+aa*aa))
 ck(44,2,'log spiral curvature',rr*rr*(1+aa*aa)/(rr**3*(1+aa*aa)**1.5),N)
ck(44,3,'monopole damping integral',quad(lambda xx:1/(1+xx*xx)**3,-np.inf,np.inf)[0],3*math.pi/8)
ff=u/(4*(1+u*u)**2)+3*u/(8*(1+u*u))+3*s.atan(u)/8
ident(44,3,'finite damping primitive',s.diff(ff,u),1/(1+u*u)**3)
Tl=300;Tr=332;L0=10
den=quad(lambda xx:1/(Tl+(Tr-Tl)*xx/L0),0,L0)[0]
cg=quad(lambda xx:xx/(Tl+(Tr-Tl)*xx/L0),0,L0)[0]/den
ck(44,4,'temperature weighted centre',cg,L0*(1/math.log(Tr/Tl)-1/(Tr/Tl-1)),1e-10)
kk=1+math.sqrt(2)
area=quad(lambda xx:(kk*kk-xx*xx)/kk,-1,1)[0]
ck(44,5,'cap area independent integral',area,(8+4*math.sqrt(2))/3)
m=3.18;M=6.4;th=math.radians(40.7);kap=.5;gg=9.8;D=(1+kap)*M+m*(kap+math.sin(th)**2)
arel=(M+m)*gg*math.sin(th)/D;Xdd=-m*math.cos(th)*arel/(M+m);NN=m*(gg*math.cos(th)+Xdd*math.sin(th));mu=kap*m*arel/NN
ck(44,6,'moving rolling slope quantitative values',[arel,Xdd,mu],[4.881234,-1.228393,.368190],1e-6)
Mpr=938;MK=494;ML=1116;Mpi=140;pf=200
threshold=((MK+ML)**2-Mpr*Mpr)/(2*Mpr);thresholdF=((MK+ML)**2-Mpr*Mpr)/(2*(math.sqrt(Mpr*Mpr+pf*pf)+pf))
estar=(ML*ML+Mpi*Mpi-Mpr*Mpr)/(2*ML);pstar=math.sqrt(estar*estar-Mpi*Mpi);beta=.773;gam=1/math.sqrt(1-beta*beta)
ck(44,7,'photon thresholds',[threshold,thresholdF],[912.716418,738.624013],1e-6)
for zz in [-1,-.5,.3,1]:
 E=gam*(estar+beta*pstar*zz);px=gam*(pstar*zz+beta*estar);pyp=pstar*math.sqrt(1-zz*zz)
 ck(44,7,'decay Lorentz invariant',E*E-px*px-pyp*pyp,Mpi*Mpi,1e-8)
radii=[.724,.491,.216];sig=[5.08,4.42]
res=[quad(lambda xx:1/(4*math.pi*sig[j]*xx*xx),radii[j+1],radii[j])[0] for j in range(2)]
I=6.19/sum(res);eps0=8.85e-12
ck(44,8,'spherical resistance integrations',[res[0],res[1],I],[.01026744,.046683705,108.689644],1e-6)
ck(44,8,'free plus bound interface charge',eps0*2.98*I/5.08-eps0*1.98*I/5.08,eps0*I/5.08,1e-22)
for n in [47,46,45,44]:
 rows=[r for r in R if r['set']==n]
 assert sorted({r['question'] for r in rows})==list(range(1,9))
 (W/str(n)/'math_verification.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('PASS',len(R),'checks across 32 questions')
