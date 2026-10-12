"""Independent numeric/symbolic checks of the 100 added variants; bind final drafts."""
from pathlib import Path
import math as m,json,hashlib
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
W=Path(__file__).resolve().parents[1]
records=[]
def C(n,q,v,method,actual,expected,tol=1e-8):
 a=np.asarray(actual,dtype=float);b=np.asarray(expected,dtype=float)
 err=float(np.max(np.abs(a-b)))
 assert err<=tol,(n,q,v,method,a,b,err)
 p=W/f'蔡题{n:03d}/整理版/drafts/question-{q:02d}.md'
 records.append(dict(set=n,question=q,variant=v,method=method,actual=a.tolist(),expected=b.tolist(),absolute_error=err,tolerance=tol,draft_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),passed=True))
def diff(f,x,h=1e-5):return (f(x+h)-f(x-h))/(2*h)
pi=m.pi
# 026: original force equations, direct field/area integration and dipole matrix integrals.
for mu,F,v,answer in [(0,.5,3,[.75,1/(2*m.sqrt(2)),1.25]),(.4,13/35,4,[0,5*m.sqrt(2)/7,2])]:
 c=1/m.sqrt(2);A=np.array([[1,-(c-mu*c),mu],[1,c+mu*c,0],[0,-(c+mu*c),1]])
 C(26,1,v,'solve three independent force equations',np.linalg.solve(A,[F,1,1]),answer)
C(26,2,3,'centripetal balance and quadrupole scaling',[m.sqrt((.5)**3),(.5)**2,1/m.sqrt(.5**3)],[1/(2*m.sqrt(2)),.25,2*m.sqrt(2)])
f=lambda t:-2-3*(3*m.cos(t)**2-1)
C(26,2,4,'integrate radial field and cosine coefficient',[quad(f,0,2*pi)[0]/(2*pi),-quad(lambda t:f(t)*m.cos(2*t),0,2*pi)[0]/pi],[-3.5,4.5])
C(26,3,3,'area and squared-radius change under dilation',[3**2,3**2*3**2,m.sqrt(3**4/3**2)],[9,81,3])
N=5;mass=sum(3**(-j) for j in range(N));inertia=17/36*sum(9**(-j) for j in range(N))
C(26,3,4,'finite layer sums without closed sum',inertia/mass,17/48*(1+3**(-N)))
Won=quad(lambda V:(8/V)**(5/3)/8,1,8)[0]-quad(lambda V:1/V,1,8)[0]
C(26,4,3,'integrate two pressure paths',[Won,1.5*(1-4)],[4.5-m.log(8),-4.5])
S=.7;gam=5/3;T=8**(gam-1)*m.exp(S/1.5)
C(26,4,4,'ideal gas entropy recovered from endpoint',1.5*m.log(T)-m.log(8),S)
phi=pi/3;H=np.outer([1,0],[1,0])+np.outer([m.cos(phi),m.sin(phi)],[m.cos(phi),m.sin(phi)])
C(26,5,3,'eigenvalues of curvature matrix',np.linalg.eigvalsh(H),[.5,1.5])
C(26,5,4,'reflection phase at center and first dark ring',[m.cos(2*pi*.5+pi),m.cos(2*pi*(.5+.5)+pi)],[1,-1])
C(26,6,3,'box eigenenergy and photon wavelength ratios',[1/1.01**2,1.01**2],[.9802960494069208,1.0201])
mat=lambda a,b:quad(lambda x:2*x*m.sin(a*pi*x)*m.sin(b*pi*x),0,1,epsabs=1e-12)[0]
C(26,6,4,'quadrature of wavefunctions',[mat(11,12),mat(11,13)],[-8*11*12/(pi**2*23**2),0])
flux=lambda R,b:quad(lambda x:2*pi*x*2*R/(x*x+R*R)**1.5,0,b)[0]
C(26,7,3,'integrate magnetic flux for moving radius',[flux(.5,1)-flux(1,2),(.5)**(-2)],[0,4])
C(26,7,4,'finite derivative of integrated moving flux',-.2*-diff(lambda R:flux(R,R*R),1),.2*m.sqrt(2)*pi,1e-7)
z=solve_ivp(lambda t,y:[y[1],2*y[1]-y[0]],(0,1),[0,.3],rtol=1e-11,atol=1e-13)
C(26,8,3,'integrate repeated-root circuit ODE',z.y[0,-1],.3*m.e)
k=m.log(2)/(2*pi);beta=k/m.sqrt(1+k*k)
C(26,8,4,'one-cycle growth from characteristic roots',m.exp(beta*2*pi/m.sqrt(1-beta*beta)),2)
# 027: geometry, contact/energy inequalities, circuit scaling, quartic quadratures.
x=lambda th:(2*m.cos(th)+1)/m.sin(th)
vp=-diff(x,pi/2);ap=(x(pi/2+1e-4)-2*x(pi/2)+x(pi/2-1e-4))/1e-8
C(27,1,2,'differentiate tangency geometry and rotation',[vp,ap,vp],[2,1,2],2e-7)
C(27,1,3,'chain-rule terms for changed angular rates',[2,2**2,4],[2,4,4])
C(27,1,4,'simultaneous ground/rod no-slip constraints',2*m.cos(pi/3),1)
s=.5;mu=.5
C(27,2,3,'vertical force from angular acceleration',(1-mu*(2*s-s*s))/(1-mu*s*s)**2,40/49)
C(27,2,4,'energy numerator at horizontal limiting field',2-2,0)
quarticT=lambda a:4*quad(lambda z:1/m.sqrt(1-z**4),0,1)[0]/a
C(27,3,3,'turning-point energy and period integral',[quarticT(3)/quarticT(1),3**2,3**4],[1/3,9,81])
C(27,3,4,'linearized tension stiffness and period',m.sqrt(1/4),.5)
C(27,4,3,'conductance matrix scaling with fixed endpoint voltages',[2*(7/10),(1/(2*(7/10)))/(1/(7/10))],[1.4,.5])
C(27,4,4,'parallel port conductances',[1/(10/7+1),(10/7)/1],[7/17,10/7])
d=.3;src=np.array([1+d/m.sqrt(2)]*2);img=np.array([1-src[1],1-src[0]])
C(27,5,3,'orthogonal reflection in plane x+y=1',np.linalg.norm(src-img),m.sqrt(2)+2*d)
C(27,5,4,'Snell invariance at n=1',m.asin(m.sin(.6)),.6)
C(27,6,3,'escape conductance controls equilibrium and decay',[1/2,1/2],[.5,.5])
ang=quad(lambda th:2*pi*m.sin(th)*m.cos(th),0,pi/2)[0]/(4*pi)
C(27,6,4,'isotropic hemisphere angular integral',[ang,(4/6)*m.sqrt(3*pi/8)],[.25,.7236012545582676])
remaining=lambda j:m.sqrt(1+(4/3/2**j)**2)-1
C(27,7,2,'mass-shell energy and integer threshold',[remaining(3)>1/150,remaining(4)<1/150],[1,1])
u=.0001;E=lambda u:m.sqrt(1+u*u)-1
C(27,7,3,'low-momentum mass-shell expansion',(E(u)-E(u/2))/(E(u/2)-E(u/4)),4,1e-5)
# Existing count is two for q7, so its new labels are 3 and 4; correct record labels.
records[-2]['variant']=3;records[-1]['variant']=4
C(27,8,3,'wire rho L/area similarity',3*.5,1.5)
C(27,8,4,'seven local linear iterations',.5**7<.01<.5**6,1)
# 028: ray matrices, impulses, rigid-body kinematics, thermodynamic line integrals.
xof=lambda u:(u*u+u-3)/(u*u-2.5)
C(28,1,2,'mirror position substitution and boundary times',[xof(2*.2),.5],[122/117,.5])
P=lambda d:np.array([[1.,d],[0,1.]])
Lf=np.array([[1,0],[-1,1.]]);Kf=np.array([[1,0],[2/3,1.]])
T=Lf@P(.5)@Kf@P(.5)@Lf
C(28,1,3,'zero image transfer upper-right element',(P(2)@T@P(1))[0,1],0)
C(28,1,4,'large-distance rational asymptotic',1e6*(xof(1e6)-1),1,1e-5)
u=1;jn=m.sqrt(3)/2;jt=1/6;w=.5+jt;omega=-1+2*jt
C(28,2,2,'collision impulse kinetic energies',(3/4-(w*w/2+omega*omega/4))/(3/4),5/9)
C(28,2,3,'separate impulse and sustained-friction cones',[1/3>1/(3*m.sqrt(3)),1/3<1/m.sqrt(3)],[1,1])
C(28,2,4,'geometric height vs radius scaling',[m.sqrt(3/9),(.5/.5)],[1/m.sqrt(3),1])
Phi=7*pi/2;ts=[m.log(7/5),m.log(7)];ph=[Phi*(1-m.exp(-t)) for t in ts]
C(28,3,2,'evaluate full upper-point velocity at two candidate times',[(1+m.cos(v))**2+m.sin(v)**2 for v in ph],[0,0])
C(28,3,3,'rigid-body damping energy at t=log 2',[m.exp(-2*m.log(2)),1-m.exp(-m.log(2))],[.25,.5])
C(28,3,4,'two distinct damping constants yield same final direction',[m.cos(2*pi),m.cos(4*pi)],[1,1])
C(28,4,2,'integrate upper and lower pressure branches',(1.2-.8)*(1.4/1.2-.6/.8),1/6)
C(28,4,3,'two-way reversible pressure integral',quad(lambda u:u,1/m.sqrt(2),m.sqrt(1.5))[0]+quad(lambda u:u,m.sqrt(1.5),1/m.sqrt(2))[0],0)
C(28,4,4,'friction work over round trip vs loop area',2*.1*.8,(1.1-.9)*.8)
z=solve_ivp(lambda t,y:[-y[1],y[0]],(0,pi/2),[1,0],rtol=1e-11,atol=1e-13)
C(28,5,2,'integrate undamped electromechanical exchange',z.y[:,-1],[0,1])
z=solve_ivp(lambda t,y:[-y[1],y[0]-2*y[1]],(0,2),[1,0],rtol=1e-11,atol=1e-13)
C(28,5,3,'integrate critical coupling ODE',z.y[0,-1],3*m.exp(-2))
z=solve_ivp(lambda t,y:[-y[1],y[0]-.7*y[1],y[1],.7*y[1]**2],(0,80),[1,0,0,0],rtol=1e-11,atol=1e-13)
C(28,5,4,'integrate signed current and Joule power',z.y[2:,-1],[1,.5])
C(28,6,3,'fixed-volume-flow momentum flux',1/(.5**2),4)
C(28,6,4,'telescoping cubic branch law',[1/(.5**3),8*.5**2,1/(8*.5**2)],[8,2,.5])
psi=.7;beta=.6;gam=1/m.sqrt(1-beta*beta)
C(28,7,2,'simultaneous rod endpoints with Lorentz contraction',m.hypot(m.cos(psi)/gam,m.sin(psi)),m.sqrt(1-beta*beta*m.cos(psi)**2))
C(28,7,3,'inverse transform on two stationary clock worldlines',beta*1-beta*0,.6)
C(28,7,4,'relative transverse velocity mass-shell clock rate',m.sqrt(1-(.6**2+.48**2)),16/25)
C(28,8,2,'exterior negative sphere and returned point source',(-.125+.125)/m.hypot(2,.5)**2,0)
C(28,8,3,'inversion of dipole and cavity vectors',[.5+(-.5),-.0625+.0625],[0,0])
r=100;potential=lambda z:1/abs(z)-.125/abs(z-.5)
C(28,8,4,'exact axial potentials vs leading odd multipole',potential(r)-potential(-r),-1/(8*r*r),1e-9)
# 029: direct quadratures, harmonic supports, mass-shell boosts and charge continuity.
C(29,1,3,'harmonic turning-point speed/support bounds',[.4<.5,.4*1<1],[1,1])
C(29,1,4,'support and velocity constraints scale differently',[m.sqrt(4),4,m.sqrt(4)],[2,4,2])
C(29,2,2,'rescale original radial force and energy',[m.sqrt(1/3),m.sqrt(3)],[1/m.sqrt(3),m.sqrt(3)])
t_half=quad(lambda s:m.sqrt(s/(2*(1-s))),.5,1)[0];t_all=quad(lambda s:m.sqrt(s/(2*(1-s))),0,1)[0]
C(29,2,3,'quadrature of infall dt/ds',t_half/t_all,.5+1/pi)
mass3=167/19;kappa=2-mass3*(1/4-1/9)
C(29,2,4,'relative acceleration from three direct attractions',[mass3,kappa,1/(8*kappa)],[167/19,533/684,171/1066])
C(29,3,3,'vector sum of two 60 degree unit tensions',np.linalg.norm([1+.5,m.sqrt(3)/2]),m.sqrt(3))
C(29,3,4,'homogeneous friction and tension constraints',(3**2*(4**2-2**2-1**2-2))/(4**2-2**2-1**2-2),9)
T=300;lamR=5000;h=.0001
C(29,4,3,'differentiate exact saturation log pressure',diff(lambda t:lamR*(1/T-1/t),T,h),lamR/T**2)
C(29,4,4,'Clapeyron temperature derivative with equal volumes',T*(1-1)/20,0)
C(29,5,2,'long RC intervals endpoints and discharge energy',[3*(1-m.exp(-100)),3*m.exp(-100),.002*3**2/2],[3,0,.009])
D=1/3;R=150e3;r=50e3;E0=4;U=D*E0*R/(r+D*R)
C(29,5,3,'averaged current balance and resistor heat',[D*(E0-U)/r-U/R,E0*D*(E0-U)/r,U*U/R],[0,53.333333333333e-6,26.666666666667e-6])
a=m.exp(-.1/75);b=m.exp(-.2/300)
C(29,5,4,'iterate affine maps for voltage perturbation',(a*b)**10,m.exp(-10*(.1/75+.2/300)))
xx=np.array([.5,1.,3]);yy=-2/xx
C(29,6,2,'Newton mapping removes constant object height',yy+2*(1/xx),[0,0,0])
h=2;r=m.sqrt(3)
C(29,6,3,'endpoint lateral magnifications product',(-1/(h-r))*(-1/(h+r)),1)
u=.4;xx=2
C(29,6,4,'differentiate focal-coordinate inverse position',[diff(lambda t:1/(xx+u*t),0),(1/(xx+u*1e-3)-2/xx+1/(xx-u*1e-3))/1e-6],[-u/xx**2,2*u*u/xx**3],1e-7)
v=.6
C(29,7,2,'Lorentz boost of inverse emitted child',[(v-v)/(1-v*v),2*v/(1+v*v)],[0,15/17])
u=.4
C(29,7,3,'perpendicular child velocity and gamma product',1-(v*v+u*u*(1-v*v)),(1-v*v)*(1-u*u))
C(29,7,4,'threshold mass-shell momentum',m.sqrt(1-4/2**2),0)
h=.8;L=2
Q=lambda h:quad(lambda r:-h*r/(r*r+h*h)**1.5,0,L)[0]
C(29,8,3,'differentiate integrated induced charge',diff(Q,h),L*L/(L*L+h*h)**1.5)
C(29,8,4,'integrate torque over chosen height history',quad(lambda h:-1/h,1,2)[0],-m.log(2))
# 030: orbital invariants, spherical diffusion integrals, harmonic forces and energy balances.
R1=1;R2=.4;tm=pi*m.sqrt((R1+R2)**3/8);nm=m.sqrt(1/R2**3);phi=pi-nm*tm
C(30,1,2,'target orbital phase at transfer endpoint',phi+nm*tm,pi)
C(30,1,3,'waterfall velocity-circle geometry',m.hypot(1,m.sqrt(5)/2),1.5)
C(30,1,4,'Kepler endpoint and half-orbit scaling',[m.sqrt(1/4),m.sqrt(4**3)],[.5,8])
C(30,2,2,'spherical diffusion integral geometry scaling',[quad(lambda r:r-r*r/2,0,2)[0]/quad(lambda r:r-r*r,0,1)[0],(1/.5-1/1)/(1/1-1/2)],[4,2])
xi=2**(-1/3);frac=quad(lambda r:r-r*r,xi,1)[0]/quad(lambda r:r-r*r,0,1)[0]
C(30,2,3,'integrate diffusion moving boundary dt/dr',[xi**3,frac],[.5,2-3*2**(-2/3)])
C(30,2,4,'reaction molar masses and matched solid volume',[44/56,(100/56)*.56],[11/14,1])
mass=np.array([2.,3.,5.]);pos=np.array([[1.,2.,0],[-1,0,2],[2,-3,1]]);center=np.sum(mass[:,None]*pos,axis=0)/sum(mass)
force=np.array([-sum(mass[j]*(pos[i]-pos[j]) for j in range(3)) for i in range(3)])
C(30,3,2,'sum all pair forces without center-force shortcut',force,-sum(mass)*(pos-center))
vel=np.array([[1.,0,0],[0,1,0],[0,0,1]]);shift=np.array([.3,-.4,.5])
C(30,3,3,'relative velocity unaffected by common inertial boost',(vel+shift)[0]-(vel+shift)[1],vel[0]-vel[1])
Om=2;r0=1;v0=3;t=.7
C(30,3,4,'ellipse trajectory and conserved angular momentum',(r0*m.cos(Om*t))*(v0*m.cos(Om*t))-(v0/Om*m.sin(Om*t))*(-r0*Om*m.sin(Om*t)),r0*v0)
C(30,4,2,'potential curvature at anti-aligned equilibrium',diff(lambda e:m.sin(pi+e),0),-1)
C(30,4,3,'trace and determinant of critical torque matrix',[np.trace([[0,1],[-1,-2]]),np.linalg.det([[0,1],[-1,-2]])],[-2,1])
C(30,4,4,'squared period ratio under doubled field',(1/(1/m.sqrt(2)))**2,2)
C(30,5,2,'flux conserved energy endpoints',[1/3,.5-.5/3,m.sqrt(2*(.5-.5/3))],[1/3,1/3,m.sqrt(2/3)])
C(30,5,3,'differentiate fixed-flux energy at endpoint',-diff(lambda x:1/(2*(1+2*x)),1)/(1),1/9)
C(30,5,4,'quadratic energy at doubled initial flux',[2**2,m.sqrt(2**2)],[4,2])
C(30,6,2,'aperture collection and diffraction-area flux ratio',[1/4,4,(4/(1/4))**.25],[.25,4,2])
C(30,6,3,'radiation power under area doubling',2*(2**(-.25))**4,1)
C(30,6,4,'specified quadrature blur budget',m.hypot(m.sqrt(5**2-3**2),3),5)
C(30,7,2,'spherical resistance integral under dilation',quad(lambda r:1/r**2,2,20)[0]/quad(lambda r:1/r**2,1,10)[0],.5)
C(30,7,3,'piecewise resistivity integral',quad(lambda r:(2 if r<3 else 5)/r**2,1,8,points=[3])[0],2*(1-1/3)+5*(1/3-1/8))
C(30,7,4,'integrate resistance to infinity',quad(lambda r:1/r**2,2,np.inf)[0],.5)
eta=m.asinh(.75)
C(30,8,2,'rapidity and mass ratio with rest endpoints',[m.tanh(eta),1-m.exp(-2*eta),.5*(1-m.exp(-2*eta))],[.6,.75,.375])
q=1e-4
C(30,8,3,'Taylor expansion against exact photon fuel fraction',1-m.exp(-2*m.asinh(q)),2*q-2*q*q,2e-12)
C(30,8,4,'linear incoming four-momentum flux under doubled area',[2*.3/.3,2*.3*1.25**3/(.3*1.25**3)],[2,2])
assert len(records)==100,len(records)
expected={(i['set'],i['question'],v) for i in json.loads((W/'核验/added_variants.json').read_text()) for v in range(i['first_variant'],5)}
assert {(r['set'],r['question'],r['variant']) for r in records}==expected
(W/'核验/added_math_verification.json').write_text(json.dumps(dict(all_passed=True,checks=len(records),scope='Numerical and symbolic checks for each added variant; conditional assumptions remain stated in prose. Not a general proof outside the stated model.',records=records),ensure_ascii=False,indent=2)+'\n')
print('100 added variants independently checked and bound to final draft hashes')
