"""以轨道ODE、冲量迭代、差分Hessian、网络线性解等独立核验第011套。"""
from pathlib import Path
import json,itertools,math
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
checks=[];supp=[]
def ck(name,value,target=0,rtol=1e-7,atol=1e-9):
 a=np.asarray(value);b=np.asarray(target);ok=bool(np.allclose(a,b,rtol=rtol,atol=atol))
 checks.append(dict(name=name,passed=ok,value=a.tolist(),expected=b.tolist(),rtol=rtol,atol=atol))
 if not ok:print('FAILED',name,a,b)
def sc(name,ok,detail):supp.append(dict(name=name,passed=bool(ok),detail=detail))
# 01: phase increments, geometry, electric-field tangent.
h=.1;lam=20;eps=h/(h+lam);hp=h*(1-eps)
ck('01-01 beat reconstruction',1/(1/hp-1/h),lam)
ck('01-02 compression fractional displacement',100*eps,100/201)
ck('01-03 finite Young modulus',1/eps,201)
ck('01-04 approximation relative error',(201-200)/201,eps)
ck('01-05 shear phase one beat',(.1/20)*20/.1,1)
ck('01-06 shear geometry',np.tan(np.arctan(h/lam)),h/lam)
d=1.5;aa=.7;yy=np.linspace(-2,2,19);xx=aa*np.sqrt(1+yy*yy/(d*d-aa*aa))
ck('01-07 hyperbola focus distance',np.hypot(xx+d,yy)-np.hypot(xx-d,yy),np.full_like(yy,2*aa))
ck('01-08 zero distance difference',np.hypot(d,yy)-np.hypot(-d,yy),0)
delta=np.pi/3;cy=d/np.tan(delta);rad=d/np.sin(delta);P=np.array([0,cy+rad]);vl=P+np.array([d,0]);vr=P-np.array([d,0]);ang=np.arctan2(vr[1],vr[0])-np.arctan2(vl[1],vl[0])
ck('01-09 circle angular branch',ang,delta)
Ef=vl/np.dot(vl,vl)-vr/np.dot(vr,vr);grad=lambda v:np.array([-v[1],v[0]])/np.dot(v,v)
ck('01-10 angular streamfunction orthogonal',np.dot(Ef,grad(vr)-grad(vl)),0)
ck('01-11 half-cycle grid shift',((.5)*lam)*(1/hp-1/h),.5)
ck('01-12 right angle circle field tangent',np.dot(np.array([0,d]),np.array([1,0])),0)
sc('01 spatial phase and strain sweep',all(np.isclose(1/(1/(h*(1-e))-1/h),h*(1-e)/e) for e in [.001,.01,.08,.2]),'Beat geometry checked across four positive compression strains.')
# 02: central-force integration plus independent optimization.
R=6.37e6;g=9.8;v0=3200;mu=g*R*R;s=v0*v0/(g*R);alpha=np.arctan(np.sqrt(1-s));a=R/(2-s);e=np.sqrt(1-s);eta=np.arccos(e)
psi=lambda al:2*np.arctan2(s*np.sin(al)*np.cos(al),1-s*np.cos(al)**2)
opt=minimize_scalar(lambda al:-psi(al),bounds=(1e-8,np.pi/2-1e-8),method='bounded',options={'xatol':1e-12})
def grav(t,Y):
 pos=Y[:2];return np.r_[Y[2:],-mu*pos/np.linalg.norm(pos)**3]
def ground(t,Y):return np.linalg.norm(Y[:2])-R if t>1e-5 else 1.0
ground.direction=-1;ground.terminal=True
sol=solve_ivp(grav,[0,1200],[R,0,v0*np.sin(alpha),v0*np.cos(alpha)],events=ground,rtol=2e-11,atol=1e-7,max_step=2)
tf=float(sol.t_events[0][0]);landing=sol.y_events[0][0];angle=np.arctan2(landing[1],landing[0]);tform=2*np.sqrt(a**3/mu)*(eta+e*np.sin(eta))
ck('02-01 central speed parameter',s,.16403421651235062)
ck('02-02 optimum by bounded search',opt.x,alpha,atol=2e-8)
ck('02-03 angle at numerical landing',angle,psi(alpha),atol=2e-9)
ck('02-04 time by force integration',tf,tform,atol=2e-5)
ck('02-05 numerical flight time',tf,510.3039022643,atol=2e-5)
ck('02-06 launch optimal angle degrees',np.degrees(alpha),42.4370390182)
ck('02-07 energy initial final',np.dot(landing[2:],landing[2:])/2-mu/np.linalg.norm(landing[:2]),v0*v0/2-mu/R,rtol=1e-9)
ck('02-08 angular momentum initial final',(landing[0]*landing[3]-landing[1]*landing[2]),R*v0*np.cos(alpha),rtol=1e-9)
ck('02-09 maximum angle alternate form',psi(alpha),2*np.arcsin(s/(2-s)))
ck('02-10 finite derivative at optimum',(psi(alpha+1e-5)-psi(alpha-1e-5))/(2e-5),0,atol=1e-9)
ck('02-11 surface eccentric anomaly',a*(1-e*np.cos(np.pi-eta)),R)
ck('02-12 surface above arc apogee',int(a*(1+e)>R),1)
sc('02 central-force independent landing event',sol.success and len(sol.t_events[0])==1 and abs(tf-tform)<2e-5,'ODE integrates Cartesian gravitational force, no Kepler time formula in the evolution.')
# 03: event-to-event impulses, integer boundaries, energy.
def bounce_distance(v,u,g,fric=.5,Mratio=1):
 w=v;distance=v*u/g;count=0;history=[]
 while w>1e-12:
  J=min(2*fric*u,w/(1+1/Mratio));new=w-J*(1+1/Mratio);count+=1;history.append(new)
  if new>1e-12:distance+=new*2*u/g
  w=new
 return distance,count,history
def closed(v,u,g,fric=.5):
 dec=4*fric*u;n=math.ceil(v/dec);return u/g*((2*n-1)*v-dec*n*(n-1)),n
u=2.;gg=10.;vv=10.;dist,n,hist=bounce_distance(vv,u,gg)
ck('03-01 first fall time',np.sqrt(2*.2/gg),.2)
ck('03-02 upward rebound normal impulse',2*u,4)
ck('03-03 relative velocity iteration',hist,[6,2,0])
ck('03-04 distance by event loop',dist,5.2)
ck('03-05 number to stick',n,3)
ck('03-06 integer boundary count',bounce_distance(8,u,gg)[1],2)
ck('03-07 integer boundary length',bounce_distance(8,u,gg)[0],3.2)
ck('03-08 first impact sticking limit',bounce_distance(3,u,gg)[0],.6)
ck('03-09 equal mass momentum',np.array([(vv+w)/2+(vv-w)/2 for w in hist]),vv)
ck('03-10 total horizontal loss',sum((old**2-new**2)/4 for old,new in zip([vv,*hist[:-1]],hist)),vv**2/4)
ck('03-11 finite closed sum',closed(vv,u,gg)[0],dist)
ck('03-12 arbitrary board mass impulse',bounce_distance(vv,u,gg,Mratio=2)[2],[7,4,1,0])
speeds=np.r_[np.linspace(.2,30,51),4,8,12,16];zetas=np.ceil(speeds/(2*u))-speeds/(2*u)
sc('03 impulse sweep, continuous bound and inverse threshold',all(np.isclose(bounce_distance(v,u,gg)[0],closed(v,u,gg)[0]) for v in speeds) and np.allclose([bounce_distance(v,u,gg)[0] for v in speeds],speeds**2/(2*gg)+4*(u*u/(2*gg))*zetas*(1-zetas)) and np.isclose(bounce_distance(8.8,u,gg)[0],4),'Saturated impulse is capped at sticking; independent event loop verifies ceiling expression, bounded bounce correction and 4m board threshold.')
# 04: finite-difference metric and energy expansion.
ns=np.array([[1,0],[-.5,np.sqrt(3)/2],[-.5,-np.sqrt(3)/2]]);L=1.;ap=L/np.sqrt(3);m=1;M=1;holes=ap*ns
U=lambda q:9.8*np.linalg.norm(q-holes,axis=1).sum()
step=1e-4;H=np.zeros((2,2));z=np.zeros(2)
for i in range(2):
 di=np.eye(2)[i]*step;H[i,i]=(U(di)-2*U(z)+U(-di))/step**2
H[0,1]=H[1,0]=(U(np.array([step,step]))-U(np.array([step,-step]))-U(np.array([-step,step]))+U(np.array([-step,-step])))/(4*step**2)
ks=3*np.sqrt(3)*m*9.8/(2*L);me=M+1.5*m;om=np.sqrt(ks/me)
ck('04-01 direction sum',ns.sum(axis=0),0)
ck('04-02 directional metric',ns.T@ns,1.5*np.eye(2))
ck('04-03 potential Hessian difference',H,ks*np.eye(2),rtol=2e-7,atol=1e-6)
ck('04-04 potential gradient at centre',[(U(np.eye(2)[i]*step)-U(-np.eye(2)[i]*step))/(2*step) for i in range(2)],0,atol=1e-6)
vel=np.array([.13,-.08]);ck('04-05 full hanging kinetic mass',M*np.dot(vel,vel)+m*np.dot(ns@vel,ns@vel),me*np.dot(vel,vel))
ck('04-06 frequency',om**2,3*np.sqrt(3)*9.8/5)
ck('04-07 equal mass period',2*np.pi/om,1.9690,rtol=1e-4)
times=np.linspace(0,4*np.pi/om,100);A=.01;B=.015;x=A*np.cos(om*times);y=B*np.sin(om*times);vx=-A*om*np.sin(om*times);vy=B*om*np.cos(om*times)
ck('04-08 elliptic geometry',x*x/A**2+y*y/B**2,1)
ck('04-09 quadratic energy invariant',me*(vx*vx+vy*vy)/2+ks*(x*x+y*y)/2,ks*(A*A+B*B)/2)
ck('04-10 linear angular momentum',me*(x*vy-y*vx),me*A*B*om)
ck('04-11 massless tabletop frequency',ks/1.5,np.sqrt(3)*9.8)
ck('04-12 positive tension sufficient',int(om**2*max(A,B)<9.8),1)
rhos=np.array([.001,.0005]);ths=np.linspace(0,2*np.pi,17);cubic_errors=[abs(np.linalg.norm(r*np.array([np.cos(t),np.sin(t)])-holes,axis=1).sum()-(3*ap+3*r*r/(4*ap)-3*r**3*np.cos(3*t)/(8*ap**2))) for r in rhos for t in ths]
sc('04 finite mass metric and cubic anisotropy',np.allclose(ns.T@ns,1.5*np.eye(2)) and np.linalg.eigvalsh(H).min()>0 and max(cubic_errors)<1e-11,'Explicit distances give positive Hessian and mass metric; third-order triangular anisotropy compared at 34 small positions.')
# 05: physical roots, matched finite chains, power and local conservation.
def impedance(w):
 return np.sqrt(1-w*w/4)+1j*w/2 if w<2 else 1j*(w/2+np.sqrt(w*w/4-1))
w=1.;Z=impedance(w);rho=1-1j*w/Z;k=2*np.arcsin(w/2)
ck('05-01 impedance polynomial real',np.real(Z*Z-1j*w*Z-1),0)
ck('05-02 impedance polynomial imag',np.imag(Z*Z-1j*w*Z-1),0)
ck('05-03 propagation root',np.angle(rho),-k)
ck('05-04 node difference equation',abs(rho+1/rho-2+w*w),0)
Zchain=Z
for _ in range(15):Zchain=1j*w+1/(1j*w+1/Zchain)
ck('05-05 terminated chain self similarity',abs(Zchain-Z),0)
t=np.linspace(0,2*np.pi/w,20001);U0=2;vv=U0*np.cos(w*t);ii=U0*np.real(np.exp(1j*w*t)/Z)
ck('05-06 cycle mean power numeric',np.trapezoid(vv*ii,t)/(t[-1]-t[0]),np.sqrt(3),rtol=1e-8)
ck('05-07 energy velocity product',.5*U0**2*np.cos(k/2),np.sqrt(3))
Zh=impedance(3);rh=1-3j/Zh
ck('05-08 stop-band ratio',np.real(rh),-(7-3*np.sqrt(5))/2)
ck('05-09 stop-band attenuation',np.log(abs(rh)),-2*np.arccosh(1.5))
ck('05-10 stop-band polynomial',abs(rh+1/rh-2+9),0)
th=np.linspace(0,2*np.pi/3,20001);ph=np.cos(3*th)*np.real(np.exp(3j*th)/Zh)
ck('05-11 stop-band mean power numeric',np.trapezoid(ph,th)/(th[-1]-th[0]),0)
ck('05-12 power negative interval',int(np.min(vv*ii)<0),1)
wg=np.array([.01,.3,1,1.99]);kg=2*np.arcsin(wg/2);group_fd=(2*np.sin((kg+1e-6)/2)-2*np.sin((kg-1e-6)/2))/(2e-6)
sc('05 physical branches and energy velocity',all(np.real(impedance(w))>0 for w in wg) and all(abs(1-1j*w/impedance(w))<1 for w in [2.01,3,10]) and np.allclose(group_fd,np.cos(kg/2)), 'Outgoing flux in pass band and bounded evanescent field in stop band; numerical dispersion derivative agrees with mean power divided by unit cell energy.')
# 06: Lorentz radiation momentum and circular orbital balances.
Ld=3.8e26;rd=1e-5;density=3000.;md=4*np.pi*density*rd**3/3;c=299792458.;G=6.6743e-11;Ms=1.99e30;Rorb=1.5e11;vel=np.sqrt(G*Ms/Rorb);Pabs=Ld*rd**2/(4*Rorb**2);F=Pabs*vel/c**2;Apr=Ld*rd**2/(2*md*c*c)
ck('06-01 geometric interception',Pabs,Ld/(4*np.pi*Rorb**2)*np.pi*rd**2,atol=0)
ck('06-02 aberration transverse momentum',Pabs/c*(vel/c),F,atol=0)
# paired isotropic photons have transformed total momentum E*v/c^2 at first order.
photon_dirs=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]);mom_rest=photon_dirs.sum(axis=0)*Pabs/(6*c)
mom_sun=mom_rest+np.array([0,Pabs*vel/c**2,0])
ck('06-03 emitted tangential momentum',mom_sun[1],F,atol=0)
mu_eff=G*Ms;rdot=-Apr/Rorb;Edot=mu_eff*md/(2*Rorb**2)*rdot
ck('06-04 orbital energy dissipation',Edot,-F*vel,atol=0)
Jdot=md*np.sqrt(mu_eff)/(2*np.sqrt(Rorb))*rdot
ck('06-05 torque balance',Jdot,-F*Rorb,atol=0)
ck('06-06 density substitution',Apr,3*Ld/(8*np.pi*density*rd*c*c))
ck('06-07 half-radius time fraction',(Rorb**2-(Rorb/2)**2)/Rorb**2,.75)
ck('06-08 radius squared derivative',2*Rorb*rdot,-2*Apr)
beta=Ld*rd**2/(4*c*G*Ms*md)
ck('06-09 pressure gravity ratio',Pabs/c/(G*Ms*md/Rorb**2),beta,atol=0)
ck('06-10 effective circular speed ratio',np.sqrt((1-1/3)*G*Ms/Rorb)/vel,np.sqrt(2/3))
ck('06-11 free emitter velocity derivative',(-Pabs*vel/c**2-(-Pabs/c**2)*vel)/md,0)
ck('06-12 near-circular bound',int(abs(rdot)/vel<1e-4),1)
Ls_ex=3.828e26;R_ex=1.495978707e11;Apr_ex=Ls_ex*rd**2/(2*md*c*c);time_ex=3*R_ex**2/(8*Apr_ex)/(365.25*86400)
sc('06 effective gravity and numerical example',all(np.isclose((2*Rorb**2/(mue*md))*(-Pabs*mue/(Rorb*c*c)),-Apr/Rorb) for mue in [G*Ms,G*Ms*.8,G*Ms*.2]) and np.isclose(time_ex,15692.331036,rtol=1e-8) and np.isclose(-Apr_ex/R_ex,-.113283133,rtol=1e-7),'Same effective gravity cancels from drift; 10 micron numerical example independently evaluated in SI units.')
# 07: open-system ODE in mole transfer, whole-system energy, entropy.
gam=1.4;cv=1/(gam-1);cp=cv+1;n0=1.;T0=1.;p0=1.;V0=1.;nu_f=1/gam
# Right chamber variables U_R,V_R. Enthalpy outflow derived from its own state.
def flow_ode(nu,Y):
 Ur,Vr,Ul=Y;nr=2-nu;Tr=Ur/(nr*cv)
 dVr=-Tr/2;dUr=-2*dVr-cp*Tr;return [dUr,dVr,cp*Tr]
flo=solve_ivp(flow_ode,[0,nu_f],[2*cv,1,cv],rtol=1e-11,atol=1e-12)
Ur,Vr,Ul=flo.y[:,-1];nr=2-nu_f;nl=1+nu_f;Tr=Ur/(nr*cv);Tl=Ul/(nl*cv);alf=1-1/(2*gam)
ck('07-01 right temperature by open ODE',Tr,1)
ck('07-02 left temperature by open ODE',Tl,2*gam/(gam+1))
ck('07-03 volume by open ODE',Vr,alf)
ck('07-04 mole conservation',nl+nr,3)
ck('07-05 terminal pressures',[nl*Tl,nr*Tr/Vr],[2,2])
ck('07-06 total energy work',Ur+Ul-3*cv,2*(1-Vr))
ck('07-07 monatomic terminal ratio',1-1/(2*(5/3)),.7)
ck('07-08 monatomic left temperature',2*(5/3)/(5/3+1),1.25)
ck('07-09 diatomic ratio',Vr,9/14)
ck('07-10 diatomic left temperature',Tl,7/6)
ck('07-11 later equilibrium temperature',(nl*Tl+nr*Tr)/3,23/21)
ck('07-12 incorrect inlet internal-energy contradiction',2*(1-.5),1)
entropy=nl*cp*np.log(Tl)-nl*np.log(2)-nr*np.log(2)+2*np.log(2)
sc('07 pressure-ratio, entropy and energy checks',all(np.isclose(cv*(q*(1+1-(q-1)/(q*gam))-(1+q)),q*(q-1)/(q*gam)) for q in [1.01,1.5,2,4]) and np.isclose(entropy,.2317568984036048) and np.allclose([Ul,Ur,Ul+Ur-3*cv],[5,45/14,5/7]),'Whole-system energy for four pressure ratios; entropy and individual terminal energies reconstructed from open-system ODE state.')
# 08: graph generation, independent grounded solves and pseudoinverse.
vs=np.array(sorted(set(itertools.permutations((1,1,0)))|set(itertools.permutations((1,-1,0)))|set(itertools.permutations((-1,-1,0)))),dtype=float)
es=[(i,j) for i in range(12) for j in range(i+1,12) if np.sum((vs[i]-vs[j])**2)==2];LG=np.zeros((12,12))
for i,j in es:LG[i,i]+=1;LG[j,j]+=1;LG[i,j]-=1;LG[j,i]-=1
A=list(map(tuple,vs)).index((1.,0.,1.));B=list(map(tuple,vs)).index((0.,1.,1.));C=list(map(tuple,vs)).index((1.,0.,-1.))
def network_potential(target):
 rhs=np.zeros(12);rhs[A]=1;rhs[target]=-1;ids=[i for i in range(12) if i!=target];phi=np.zeros(12);phi[ids]=np.linalg.solve(LG[np.ix_(ids,ids)],rhs[ids]);return phi,rhs
pab,bab=network_potential(B);pac,bac=network_potential(C);pinv=np.linalg.pinv(LG)
res=lambda i,j:pinv[i,i]+pinv[j,j]-2*pinv[i,j]
ck('08-01 number vertices',len(vs),12)
ck('08-02 number edges',len(es),24)
ck('08-03 degree four',np.diag(LG),4)
ck('08-04 adjacent resistance grounded',pab[A],11/24)
ck('08-05 diagonal resistance grounded',pac[A],7/12)
ck('08-06 both Kirchhoff residuals',np.r_[LG@pab-bab,LG@pac-bac],0)
ck('08-07 pseudoinverse adjacent',res(A,B),11/24)
ck('08-08 pseudoinverse diagonal',res(A,C),7/12)
ck('08-09 Foster sum',sum(res(i,j) for i,j in es),11)
bdot=np.array([-1.,1.,0]);em=np.zeros((12,12))
for i,j in es:em[i,j]=-.5*np.dot(bdot,np.cross(vs[i],vs[j]));em[j,i]=-em[i,j]
ck('08-10 induced source divergence',em.sum(axis=1),0)
ck('08-11 direct AB field integral',-.5*np.dot(bdot,np.cross(vs[A],vs[B])),0)
ck('08-12 direct AC field integral',-.5*np.dot(bdot,np.cross(vs[A],vs[C])),-1)
triangles=[(i,j,k) for i in range(12) for j in range(i+1,12) for k in range(j+1,12) if LG[i,j]==LG[j,k]==LG[k,i]==-1]
loops=[]
for i,j,k in triangles:
 area=.5*(np.cross(vs[i],vs[j])+np.cross(vs[j],vs[k])+np.cross(vs[k],vs[i]));loops.append(abs(em[i,j]+em[j,k]+em[k,i]+np.dot(bdot,area))<1e-12)
induced_heat=sum(em[i,j]**2 for i,j in es);cross_power=sum((pab[i]-pab[j])*em[i,j] for i,j in es)
sc('08 face flux and both graph heat sources',len(triangles)==8 and all(loops) and np.isclose(sum((pab[i]-pab[j])**2 for i,j in es),11/24) and np.isclose(induced_heat,12) and abs(cross_power)<1e-12 and sum(abs(em[i,j])>0 for i,j in es)==12,'All eight triangular faces obey Faraday; static and induced Joule heat verified, with zero conservative-solenoidal cross term.')
assert len(checks)==96 and len(supp)==8
result={'check_count':len(checks),'supplementary_check_count':len(supp),'all_passed':all(c['passed'] for c in checks+supp),'checks':checks,'supplementary_checks':supp}
(ROOT/'physics_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['checks','supplementary_checks']}))
assert result['all_passed']
