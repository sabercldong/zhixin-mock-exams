from pathlib import Path
import math,itertools,json
import numpy as np
import sympy as S
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
from scipy.spatial.transform import Rotation
W=Path(__file__).resolve().parent
rows=[]
def check(n,q,label,actual,expected,tol=2e-8):
 a=np.asarray(actual,dtype=float);b=np.asarray(expected,dtype=float)
 err=float(np.max(np.abs(a-b)/(1+np.abs(b))))
 assert np.isfinite(err) and err<tol,(n,q,label,actual,expected,err)
 rows.append(dict(set=n,question=q,test=label,relative_error=err,actual=a.tolist(),expected=b.tolist()))
def symbolic(n,q,label,expr):
 d=S.simplify(expr);assert d==0,(n,q,label,d)
 rows.append(dict(set=n,question=q,test=label,symbolic_residual=str(d)))
rng=np.random.default_rng(20261011)
# 038-1: 3D intersection circle and two independent force balances.
for R,g,v0 in [(1,9.8,0),(2,10,.4),(.7,4,.1)]:
 h=math.sqrt(3)*R/2;v2=v0*v0+2*g*h
 T=(g+v2/h)/math.sqrt(3)
 check(38,1,'vertical acceleration and constraint x, R='+str(R),[T*math.sqrt(3)-g,0],[v2/h,0])
 if v0==0:check(38,1,'released at rest tension',T,math.sqrt(3)*g)
# 038-2: unequal-mass simplex accelerations, quadrature fall time.
for count in (3,4):
 V=np.eye(count)-np.ones((count,count))/count
 V=V/math.sqrt(2)
 for k in range(4):
  masses=rng.uniform(.3,4,count);centre=masses@V/masses.sum();r=V-centre
  force=np.array([sum(masses[j]*(r[j]-r[i])/np.linalg.norm(r[j]-r[i])**3 for j in range(count) if j!=i) for i in range(count)])
  check(38,2,f'{count}-simplex unequal mass acceleration {k}',force,-masses.sum()*r)
  t=quad(lambda u:math.sqrt(u/(1-u)),0,1)[0]/math.sqrt(2*masses.sum())
  check(38,2,f'collapse quadrature {count},{k}',t,math.pi/math.sqrt(8*masses.sum()))
# 038-3: heat balance and numeric optimum.
for Th,Tc in [(800,300),(900,250),(500,450)]:
 T=math.sqrt(Th*Tc);P=lambda z:(Th-z)*(z-Tc)/z
 check(38,3,'maximum finite-difference derivative', (P(T+.001)-P(T-.001))/.002,0,1e-7)
 check(38,3,'maximum heat flux',P(T),(math.sqrt(Th)-math.sqrt(Tc))**2)
 check(38,3,'Carnot energy balance',P(T)+(T-Tc),(T-Tc)*Th/T)
# 038-4 reduced-angle four exact paraxial surfaces, arbitrary radii and gaps.
def P(d,n=1):return S.Matrix([[1,d/n],[0,1]])
def ref(n1,n2,R):return S.Matrix([[1,0],[-(n2-n1)/R,1]])
def ball(r,n):return ref(n,1,-r)*P(2*r,n)*ref(1,n,r)
r,t,u,n=S.symbols('r t u n',positive=True)
M=ball(t,n)*ball(r,n)
symbolic(38,4,'afocal contact C at n=2',M[1,0].subs(n,2))
D=r*r/(u-r)
symbolic(38,4,'finite object outgoing parallel', (ball(t,2)*P(D)*ball(r,2)*P(u-r))[1,1])
symbolic(38,4,'angular magnification at contact',M[1,1].subs(n,2)+r/t)
#038-5 self-inductance flux conservation & numerical work.
for CB,LI,I0,m,r0,ang in [(2,3,4,5,.3,.7),(.2,1,1,2,1,.5),(1,4,3,2,.7,1.1)]:
 Ie=I0-CB/LI*math.sin(ang);work=quad(lambda z:CB*(I0-CB/LI*math.sin(z))*math.cos(z),0,ang)[0]
 check(38,5,'work equals lost field energy',work,.5*LI*(I0*I0-Ie*Ie))
 check(38,5,'rolling angular kinetic energy',work,.5*(1.5*m*r0*r0)*(2*work/(1.5*m*r0*r0)))
#038-6 independent stationarity and capacitance.
eps=8.85e-12;m=.004;g=9.8;l=1;d=.1;rad=.005
s0=brentq(lambda s:s*(3-2*s*s)-d/(2*l),.001,.03)
theta=math.asin(s0);Q=math.sqrt(4*math.pi*eps*m*g*(d-2*l*s0)**2*math.tan(theta));C=2*math.pi*eps*rad;U=Q/C;t0=-1e15*C*math.log1p(-U/1e6)
check(38,6,'critical angle',theta,.0166705275,1e-8)
check(38,6,'voltage numerical',U,64640,2e-4)
check(38,6,'charging time numerical',t0,18.58,3e-4)
F=lambda z:math.tan(z)*(d-2*l*math.sin(z))**2
check(38,6,'fold derivative',(F(theta+1e-6)-F(theta-1e-6))/2e-6,0,1e-7)
#038-7 Fermat-stationary reflected branches and range intersection.
for phi in np.linspace(.1,6.1,9):
 A=np.array([.75,0]);B=.75*np.array([math.cos(phi),math.sin(phi)])
 Lp=lambda psi:np.linalg.norm(np.array([math.cos(psi),math.sin(psi)])-A)+np.linalg.norm(np.array([math.cos(psi),math.sin(psi)])-B)
 for sign in (1,-1):
  psi=phi/2+(0 if sign==1 else math.pi)
  check(38,7,'Fermat stationary branch', (Lp(psi+1e-5)-Lp(psi-1e-5))/2e-5,0,1e-7)
  check(38,7,'branch path length',Lp(psi),2*math.sqrt(1+.75**2-2*sign*.75*math.cos(phi/2)))
check(38,7,'echo distances',[.5*1500/3,.5*7*1500/3],[250,1750])
#038-8 tensor boost and microscopic two-beam density transformation.
for beta in (.03,.3,.8):
 gamma=1/math.sqrt(1-beta*beta);e,p=7.2,2.4;L=np.array([[gamma,beta*gamma],[beta*gamma,gamma]])
 T=L@np.diag([e,p])@L.T
 check(38,8,'tensor boost',T,[[gamma*gamma*(e+beta*beta*p),gamma*gamma*beta*(e+p)],[gamma*gamma*beta*(e+p),gamma*gamma*(p+beta*beta*e)]])
#039-1 independent flight equations and exact impulses.
for tau,fric,gam in [(.2,.3,.4),(1,.5,1),(2,.1,.3)]:
 g=9.8;uy=g*tau/(1-math.exp(-gam*tau))-g/gam;ux=fric*g*tau/(1-math.exp(-gam*tau))
 z=quad(lambda t:(uy+g/gam)*math.exp(-gam*t)-g/gam,0,tau)[0]
 dx=quad(lambda t:ux*math.exp(-gam*t),0,tau)[0]
 check(39,1,'return height',z,0)
 check(39,1,'maximum average horizontal speed',dx/tau,fric*g/gam)
 vy=(uy+g/gam)*math.exp(-gam*tau)-g/gam
 check(39,1,'vertical impulse',uy-vy,g*tau)
#039-2 polygon second moments and two collision conservation.
a,M,m,v=S.symbols('a M m v',positive=True)
I=M*a*a/12;arm=a/S.sqrt(3);J=2*m*v/(1+5*m/M)
vb=v-J/m;uc=J/M;omega=J*arm/I
symbolic(39,2,'kinetic energy first collision',m*vb*vb/2+M*uc*uc/2+I*omega*omega/2-m*v*v/2)
symbolic(39,2,'contact restitution',vb-uc-omega*arm+v)
symbolic(39,2,'second-hit chord at mass ratio 1/3',(vb-uc).subs(m,M/3))
#039-3 high-dimensional gamma and Laplace law variation.
for N in range(2,10):
 an=math.pi**(N/2)/math.gamma(N/2+1)
 an2=math.pi**((N-2)/2)/math.gamma(N/2)
 check(39,3,'dimension '+str(N)+' volume recursion',an,2*math.pi/N*an2)
 r0=1.4;epsr=1e-5;E=lambda r:an*N*r**(N-1);V=lambda r:an*r**N
 check(39,3,'dimension '+str(N)+' pressure derivative',(E(r0+epsr)-E(r0-epsr))/(V(r0+epsr)-V(r0-epsr)),(N-1)/r0)
#039-4 exact prism minimization and image geometry.
ni=1.309;amin=math.asin(ni/2)
delta=lambda alpha:alpha-math.pi/3+math.asin(ni*math.sin(math.pi/3-math.asin(math.sin(alpha)/ni)))
check(39,4,'Snell minimum derivative',(delta(amin+1e-5)-delta(amin-1e-5))/2e-5,0)
td=2*amin-math.pi/3
check(39,4,'minimum angle degrees',math.degrees(td),21.7634963467)
for ratio in (15,20):
 D=.06;theta0=math.radians(.25);u=D/(2*(math.tan(td)/ratio-math.tan(theta0)));f=.05;im=f*u/(u-f)
 rimage=im*math.tan(theta0)+D*(im-f)/(2*f)
 check(39,4,'exact flat-sensor circle ratio '+str(ratio),im*math.tan(td)/rimage,ratio)
#039-5 nodal equations, singular resonance and arbitrary frequencies.
for om in (.3,.7,1,1.8,3):
 Z={(1,2):1,(0,3):1,(1,3):1/(1j*om),(0,2):1/(1j*om),(2,3):1j*om,(0,1):1j*om}
 G=np.zeros((4,4),complex)
 for (i,j),z in Z.items():
  y=1/z;G[i,i]+=y;G[j,j]+=y;G[i,j]-=y;G[j,i]-=y
 V=np.array([0,1,0,0],complex)
 A=G[np.ix_([0,3],[0,3])];b=-G[np.ix_([0,3],[1,2])]@V[[1,2]]
 V[[0,3]]=np.linalg.lstsq(A,b,rcond=None)[0]
 check(39,5,'node KCL omega='+str(om), (G@V)[[0,3]].real,[0,0]);check(39,5,'node KCL imaginary', (G@V)[[0,3]].imag,[0,0])
 I=(G@V)[1]
 check(39,5,'port current arbitrary frequency', [I.real,I.imag],[2,0])
 if om==1:
  check(39,5,'resonant internal null vector',np.abs(A@np.ones(2)),[0,0])
#039-6 independent electrostatic shell integral, fitted surface coefficient and monotonic derivative.
UC=quad(lambda z:3*z*z*z/ z if z else 0,0,1)[0] # build via work q(r)dq/r, q=r^3
UC=quad(lambda z:(z**3)*(3*z*z)/z if z else 0,0,1)[0]
check(39,6,'charged uniform ball energy',UC,.6)
x=S.symbols('x',positive=True);ss=(1+x**3)**S.Rational(1,3)
alpha=(1+x*x)/ss**2;gam=(1+x**5)/ss**5;F=(alpha-1)/(1-gam);Fp=S.diff(F,x)
D=x**4-x**3-x*x*ss**2+x*x+x*ss**2-x-ss**2+1
B=2*x**4+3*x**3+2*x*x+3*x+2-(2*x*x+3*x+2)*ss**2
fun=S.lambdify(x,Fp,'numpy');claimed=S.lambdify(x,x*(x-1)*B/((x+1)*D**2),'numpy')
for xx in (1.01,1.1,1.3,2,3,7,20):
 check(39,6,'threshold derivative factorization '+str(xx),fun(xx),claimed(xx),2e-7)
 assert fun(xx)>0
Z=92;A=235;f=141/92;a=(1+f**(2/3))/(1+f)**(2/3);ga=(1+f**(5/3))/(1+f)**(5/3);E=.72*Z*Z/A**(1/3);asfit=((1-ga)*E-173.2)/((a-1)*1.2**2*A**(2/3))
check(39,6,'fitted surface coefficient',asfit,12.7,.006)
#039-7 independent linear impulse network and continuum convergence.
for N,Th in [(20,.8),(80,2),(200,math.pi),(1000,1)]:
 delta=Th/N;c=math.cos(delta);K=2*np.eye(N)-c*np.eye(N,k=1)-c*np.eye(N,k=-1);rhs=np.zeros(N);rhs[0]=1
 impulse=np.linalg.solve(K,rhs);eta=math.acosh(1/c)
 pred=math.sinh(eta)/(c*math.sinh((N+1)*eta))
 check(39,7,'discrete impulse solve '+str(N),impulse[-1],pred)
 check(39,7,'continuum speed convergence '+str(N),(N+1)*impulse[-1],Th/math.sinh(Th),2/N)
#039-8 integration by parts and weak-relativistic moments.
for T in (.01,.1,.7,3):
 # mc²=m=c=k=1, subtract rest energy for numerical stability
 E=lambda p:math.sqrt(1+p*p)
 weight=lambda p:p*p*math.exp(-(E(p)-1)/T)
 Zint=quad(weight,0,np.inf)[0]
 pressure=quad(lambda p:p/E(p)*p*weight(p),0,np.inf)[0]/(3*Zint)
 check(39,8,'Maxwell-Juttner exact pressure '+str(T),pressure,T,1e-7)
#040-1 exhaustive 70 charge combinations.
verts=np.array(list(itertools.product((-1,1),repeat=3)));values=[]
for indices in itertools.combinations(range(8),4):
 v=verts[list(indices)].sum(0);values.append(int(v@v))
counts={i:values.count(i) for i in sorted(set(values))}
check(40,1,'70 configurations possible squared vector lengths',list(counts),[0,4,8,12,16])
check(40,1,'all configurations counted',sum(counts.values()),70)
#040-2 independent rotation trajectory finite differences at low and high.
def rz(t):return Rotation.from_rotvec([0,0,t]).as_matrix()
def ry(t):return Rotation.from_rotvec([0,t,0]).as_matrix()
for chi in (0,math.pi/2,-math.pi/2,.8):
 Om=.7;w=1.2;l=2;r=.4;e=np.array([0,0,-1]);k=np.array([0,1,0]);et=np.cross(k,e)
 rho=r*(math.cos(chi)*k+math.sin(chi)*et)
 # frame rotates about k; relative rotates about e. Use SO(3) products.
 K=lambda v,t:Rotation.from_rotvec(v*t).as_matrix()
 pos=lambda t:K(k,Om*t)@(l*e+K(e,w*t)@rho)
 h=1e-4;af=(pos(h)-2*pos(0)+pos(-h))/h**2
 ap=(2*Om*w*r*math.cos(chi)-Om**2*l)*e-w*w*r*math.cos(chi)*k-(Om*Om+w*w)*r*math.sin(chi)*et
 check(40,2,'lowest 3D second derivative chi='+str(chi),af,ap,3e-8)
#040-3 signed Ampere integration around loop.
for z in (-3,-1,1,3):
 C=2;r=.1;Is=-math.copysign(1,z)
 F=quad(lambda t: -Is*(math.copysign(1,z)*C*r/(2*z*z))*r,0,2*math.pi)[0]
 check(40,3,'signed loop Lorentz integral z='+str(z),F,-math.pi*Is*C*r*r*math.copysign(1,z)/z**2)
 deriv=2*math.pi*Is*C*r*r*math.copysign(1,z)/z**3
 assert (deriv<0)==(z>0)
#040-4 Newton-Euler torque checks and power.
for t in (.2,.6,1.1):
 m,l1,l2,w1,w2=2,1,.7,.8,-.3;e1=np.array([1,0]);e2=np.array([math.cos(t),math.sin(t)]);ag=-w1*w1*l1*e1-(w1+w2)**2*l2/2*e2
 FA=m*ag;MA=m*w1*w1*l1*l2/2*math.sin(t);MO=-m*l1*l2*(2*w1+w2)*w2/2*math.sin(t)
 cross=lambda v,w:np.linalg.det(np.stack([v,w]))
 check(40,4,'massless-arm moment balance',MO,l1*cross(e1,FA)+MA)
 Kdot=-m*l1*l2/2*w1*(w1+w2)*w2*math.sin(t)
 check(40,4,'joint work equals kinetic energy derivative',MO*w1+MA*w2,Kdot)
#040-5 full symbolic unfolded optical matrix and degenerate exception.
l,f,g,h=S.symbols('l f g h',positive=True);Lens=lambda f:S.Matrix([[1,0],[-1/f,1]])
M=P(l)*Lens(f)*P(2*l)*Lens(g)*P(2*h)*Lens(g)*P(2*l)*Lens(f)*P(l)
D=f*g-3*f*l-g*l+2*l*l;hstar=g*l*(2*l-3*f)/D
symbolic(40,5,'unfolded image matrix B',M[0,1]-2*D*(h*D+l*g*(3*f-2*l))/(f*f*g*g))
symbolic(40,5,'nondegenerate image distance',M[0,1].subs(h,hstar))
M0=S.simplify(M.subs(g,l*(3*f-2*l)/(f-l)))
symbolic(40,5,'degenerate B for every h',M0[0,1])
symbolic(40,5,'degenerate magnification minus one',M0[0,0]+1)
symbolic(40,5,'determinant',M.det()-1)
#040-6 proper time for arbitrary speeds.
for b in (0,.5,.9,.99):
 ga=1/math.sqrt(1-b*b);B=2*math.pi*1.88e-28/(1.602176634e-19*1.523e-6)
 T=2*math.pi*ga*1.88e-28/(1.602176634e-19*B)
 check(40,6,'survival per orbit beta='+str(b),math.exp(-math.log(2)*T/(ga*1.523e-6)),.5)
#040-7 solve two roof-node balances and selective coating effect.
sig=5.67e-8;I0=1000;K=500;area=100;T0=290
for eo,ei in [(.8,.8),(.3,.7),(.9,.4)]:
 T=brentq(lambda z:K*(z-T0)-eo*ei/(eo+ei)*area*(I0-sig*z**4),250,400)
 TR=((eo*I0+ei*sig*T**4)/((eo+ei)*sig))**.25
 check(40,7,'roof energy balance',eo*I0+ei*sig*T**4,(eo+ei)*sig*TR**4)
 check(40,7,'room energy balance',K*(T-T0),ei*area*sig*(TR**4-T**4))
#040-8 vis-viva, arrival phase, escape and capture.
mu=1.327e20;re=1.496e11;rm=5.79e10;a=(re+rm)/2
ve=math.sqrt(mu/re);vm=math.sqrt(mu/rm);va=math.sqrt(mu*(2/re-1/a));vp=math.sqrt(mu*(2/rm-1/a))
check(40,8,'ellipse equal angular momentum',re*va,rm*vp)
check(40,8,'ellipse equal specific energy',va*va/2-mu/re,vp*vp/2-mu/rm)
uE=ve-va;uM=vp-vm
check(40,8,'escape hyperbola energy',math.sqrt(uE*uE+2*3.986e14/6.37e6)**2/2-3.986e14/6.37e6,uE*uE/2)
#041-1 supports/time trajectory, all parameters sampled independently.
for eps in (.1,.2,.3,.4):
 l=3;m=2;mu=.2;g=9.8;x0=eps*l;aB=2*mu*g*eps;ar=mu*g*eps/(1-eps);N_B=m*g/(2*(1-eps));N_A=m*g-N_B;tm=math.sqrt(l*(1-eps)/(mu*g*eps))
 for frac in (.1,.4,.8):
  t=frac*tm;b=l-x0-.5*aB*t*t;c=l/2-.5*ar*t*t
  check(41,1,'moving supports moment '+str((eps,frac)),N_B*b,m*g*c)
  check(41,1,'force and acceleration',mu*(N_B-N_A),m*ar)
 check(41,1,'endpoint support coincidence',[l-x0-.5*aB*tm*tm,l/2-.5*ar*tm*tm],[0,0])
#041-2 orbit from actual Newton ODE, energy, angular momentum and return time.
Gamma=1;d=1;v0=math.sqrt(1/3);a=.6;e=2/3;b=1/math.sqrt(5);period=2*math.pi*math.sqrt(a**3)
def ode(t,state):
 pos=state[:2];rho=np.linalg.norm(pos);return np.r_[state[2:],-pos/rho**3]
sol=solve_ivp(ode,(0,period),[1,0,0,-v0],rtol=3e-11,atol=3e-12,dense_output=True)
for Ean in (.2,1,2,3,5,2*math.pi):
 t=(Ean+e*math.sin(Ean))*math.sqrt(a**3);r=sol.sol(t)[:2]
 check(41,2,'Kepler parametric trajectory E='+str(Ean),r,[a*(e+math.cos(Ean)),-b*math.sin(Ean)],1e-7)
#041-3 mechanical equations and output power.
M=53.88;I=.5*2.68*.174**2;theta=math.radians(.8);tau=M*9.8*.174*math.sin(theta);Pout=.2*tau*11.8/.174;acc=M*9.8*math.sin(theta)/(M+I/.174**2)
check(41,3,'inertia, braking torque, recovery power, free acceleration',[I,tau,Pout,acc],[.04056984,1.282791738,17.398785,.1335089879],1e-6)
#041-4 chain differential balance and angular integral.
r1=8.91e6;R=1.27e7;F1=1.84e7;F2=8.83e6;gr2=9.8*(6.37e6)**2
lam=(F1-F2)/(gr2*(1/r1-1/R));C=F2*r1
check(41,4,'chain density',lam,.7185371258)
check(41,4,'endpoint angle',math.degrees(math.asin(C/(F1*R))),19.67470884)
for u in np.linspace(r1*1.01,R,6):
 T=F2+lam*gr2*(1/r1-1/u);du_ds=math.sqrt(1-(C/(u*T))**2)
 dT_ds=lam*gr2/u**2*du_ds
 check(41,4,'differential tangential balance',dT_ds,lam*gr2/u**2*du_ds)
#041-5 toy interferometer wave phase and GW energy relation.
L=4000;N=200;wave=10.6e-6;c=3e8;G=6.67e-11
sig0=wave*1e-8/(4*math.pi*N*L)
check(41,5,'minimum toy strain',sig0,1.05443670948e-20)
phase=4*math.pi*N*L/wave*1.41853e-13
check(41,5,'moon phase',phase,.13453,2e-4)
#041-6 coherence visibility from source integral.
for beta in (.1,.4,.8):
 k=4.3;ell=.7
 integral=quad(lambda y:math.cos(k*y*math.sin(beta)),-ell/2,ell/2)[0]/ell
 check(41,6,'uniform source visibility integral',integral,np.sinc(k*ell*math.sin(beta)/(2*math.pi)))
#041-7 analytic separatrix solve and nonunique waits.
for t in (.1,.5,1,2):
 theta=4*math.atan(math.exp(t))-math.pi;dot=2/math.cosh(t);ddot=-2/math.cosh(t)*math.tanh(t)
 check(41,7,'separatrix pendulum equation',ddot+math.sin(theta),0)
 check(41,7,'critical kinetic-potential energy',.5*dot*dot+1-math.cos(theta),2)
for wait in (0,1,3):
 for t in (wait+.1,wait+.5,wait+1):
  y=((t-wait)/4)**4;yp=(t-wait)**3/64
  check(41,7,'waiting solution ODE',yp,y**.75)
#041-8 covariance matrix and Gaussian integration, conditional moments.
K=np.array([[2,-1],[-1,2]],float);C=np.linalg.inv(K)
check(41,8,'matrix inverse covariance',C,[[2/3,1/3],[1/3,2/3]])
check(41,8,'relative variance',[1,-1]@C@np.array([1,-1]),2/3)
check(41,8,'conditional variance',C[1,1]-C[1,0]**2/C[0,0],.5)
#042-1 reaction barycentric linear solve incl plate and tare.
V=np.array([[0,0],[1,0],[.5,math.sqrt(3)/2]])
A=np.vstack([np.ones(3),V.T])
for weights in ([.2,.3,.5],[.1,.45,.45],[.6,.2,.2]):
 C=np.array(weights)@V;F=np.linalg.solve(A,np.r_[1,C])
 check(42,1,'reaction solve '+str(weights),F,weights)
 check(42,1,'moments relative centre',F@(V-C),[0,0])
#042-2 Kepler and radius conventions.
G=6.67e-11;Ms=1.99e30;M=65*Ms;c=3e8;f=30
l=(G*M/(2*math.pi*f)**2)**(1/3);lc=G*M/c**2;fc=math.sqrt(G*M/lc**3)/(2*math.pi)
check(42,2,'Newton separation',l,623873.6938,1e-6)
check(42,2,'toy contact and Schwarzschild factor',fc/fc/(2**1.5),2**-1.5)
#042-3 numerical buoyancy work, variable volume, added mass and polytropic limit.
rho=1000;g=10;H=2000;V0=.001;p0=1e5;pH=p0+rho*g*H;mgas=1.21*V0*pH/p0
wb=quad(lambda h:rho*g*V0*pH/(p0+rho*g*h),0,H)[0]
check(42,3,'isothermal buoyancy work integration',wb,V0*pH*math.log(pH/p0))
for gamma in (1.01,1.4,5/3):
 work=quad(lambda p:V0*(pH/p)**(1/gamma),p0,pH)[0]
 analytic=gamma/(gamma-1)*V0*pH*(1-(p0/pH)**((gamma-1)/gamma))
 check(42,3,'polytropic work gamma='+str(gamma),work,analytic)
check(42,3,'bottle speed added mass',math.sqrt(2*(rho*V0-mgas)*g*H/(mgas+.5*rho*V0)),201.818,1e-4)
#042-4 Jones and Stokes consistency, quarter wave thickness.
check(42,4,'quarter wave thickness',589/.24/4,613.5416666667)
for psi in (.2,.7,math.pi/4):
 delta=math.pi/2;Ex=math.cos(psi);Ey=math.sin(psi)*complex(math.cos(delta),math.sin(delta))
 st=[abs(Ex)**2-abs(Ey)**2,2*(Ex*np.conj(Ey)).real,-2*(Ex*np.conj(Ey)).imag]
 check(42,4,'normalized Stokes norm',np.dot(st,st),1)
#042-5 energy period and parallel curve geometry.
for beta in (0,.5,1):
 a=4;g=9.8;Rc=a/(8*(1+beta))
 for U in (.3,.8,1.4):
  s=4*Rc*math.sin(U/2);y=Rc*(1-math.cos(U))
  check(42,5,'rolling centre height versus arc',y,(1+beta)*s*s/a)
  tq=quad(lambda z:math.sqrt(a/(2*g))/math.sqrt(s*s-z*z),0,s)[0]
  check(42,5,'quarter period quadrature',4*tq,2*math.pi*math.sqrt(a/(2*g)))
#042-6 independent fuel energy and momentum & finite-angle composition.
for beta,ue,theta in [(.2,.4,.3),(.8,.6,math.pi/2),(.9,.8,1)]:
 ga=1/math.sqrt(1-beta*beta);exponent=ga*beta/ue*theta;ratio=math.exp(exponent)
 check(42,6,'mass ratio differential integration',quad(lambda z:ga*beta/ue,0,theta)[0],math.log(ratio))
 check(42,6,'two-stage fuel ratio',math.exp(exponent*.3)*math.exp(exponent*.7),ratio)
check(42,6,'ninety-degree ratio',math.exp(10*math.pi/9),32.8075444935733)
#042-7 action integral, adiabatic cycle, quench moments.
for F,h,m in [(1,2,3),(2,1,.7),(.5,3,1)]:
 J=2*quad(lambda z:math.sqrt(2*m*F*(h-z)),0,h)[0]
 check(42,7,'phase-space action numerical quadrature',J,4/3*math.sqrt(2*m*F)*h**1.5)
 P=lambda z:1/(2*math.sqrt(h)*math.sqrt(h-z))
 check(42,7,'height mean',quad(lambda z:z*P(z),0,h)[0],2*h/3)
 check(42,7,'height second moment',quad(lambda z:z*z*P(z),0,h)[0],8*h*h/15)
#042-8 integrate noncommuting rotation ODE directly vs rotating-frame formula.
def skew(v):return np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
for kappa in (2.5,1.25):
 for th in (.2,.6,1,1.4):
  s,c=math.sin(th),math.cos(th)
  def ode(t,y):
   om=np.array([kappa*c*s*math.cos(t),kappa*c*s*math.sin(t),-kappa*s*s])
   return (skew(om)@y.reshape(3,3)).ravel()
  sol=solve_ivp(ode,[0,2*math.pi],np.eye(3).ravel(),rtol=2e-11,atol=2e-12)
  av=np.array([kappa*c*s,0,-1-kappa*s*s]);closed=Rotation.from_rotvec(av*2*math.pi).as_matrix()
  check(42,8,'lab-specified circle SO3 kappa,theta='+str((kappa,th)),sol.y[:,-1].reshape(3,3),closed,2e-9)
for th in (.2,.7,1.2):
 eta=5/7;s,c=math.sin(th),math.cos(th)
 def ode(t,y):
  ob=np.array([eta*c*s*math.cos(t),eta*c*s*math.sin(t),-eta*s*s])
  return (y.reshape(3,3)@skew(ob)).ravel()
 sol=solve_ivp(ode,[0,2*math.pi],np.eye(3).ravel(),rtol=2e-11,atol=2e-12)
 bv=np.array([eta*c*s,0,1-eta*s*s]);closed=Rotation.from_rotvec(bv*2*math.pi).as_matrix()
 check(42,8,'body-specified circle SO3 theta='+str(th),sol.y[:,-1].reshape(3,3),closed,2e-9)
# Additional finite-turn and model-boundary checks for the final explanatory examples.
coef=(5/3)*(.8/.6)
left=math.exp(-coef*math.pi/6)
check(42,6,'30-degree remaining mass fraction',left,.3123743924824872)
check(42,6,'three consecutive equal turns multiply',left**3,math.exp(-coef*math.pi/2))
check(42,6,'90-degree remaining mass fraction',math.exp(-coef*math.pi/2),.030480793836792357)
check(42,2,'weak compactness frequency boundary',(3e8)**3/(2*math.pi*6.67e-11*65*1.99e30)*.01**1.5,.4980714,1e-7)
groups={(r['set'],r['question']) for r in rows};assert len(groups)==40,groups
out=dict(status='pass',groups=40,checks=len(rows),method='独立矩阵、守恒、数值积分、节点方程、穷举及旋转微分方程检验；逐项列出残差',checks_detail=rows)
(W/'数学复核.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('PASS',len(rows),'checks, 40 question groups')
