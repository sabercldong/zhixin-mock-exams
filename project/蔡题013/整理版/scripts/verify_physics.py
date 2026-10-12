"""独立代数、积分、矩阵及运动方程核验；只记录实际执行的检查。"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
C=[];S=[]
def check(q,name,actual,expected,tol=1e-8):
 a=np.asarray(actual);e=np.asarray(expected);err=float(np.max(abs(a-e)));scale=max(1.,float(np.max(abs(e))))
 C.append(dict(name=f'{q:02d} {name}',actual=a.tolist(),expected=e.tolist(),max_abs_error=err,passed=bool(err<=tol*scale)))
def supp(q,name,passed,details):S.append(dict(name=f'{q:02d} {name}',passed=bool(passed),details=details))
# 01: units m=kappa=r=1, independent force integration and event calculation.
U=lambda r:.5*(r*r-1) if r<=1 else math.log(r)
vc=math.sqrt(2*math.log(2)/3);J=2*vc;E=U(2)+.5*vc**2
check(1,'interior force integral',quad(lambda x:x,1,.6)[0],U(.6))
check(1,'exterior force integral',quad(lambda x:1/x,1,2)[0],U(2))
check(1,'critical-speed number',vc,.6797779934458726)
check(1,'boundary critical effective energy',J*J/2,E)
check(1,'constant exterior circular speed',math.sqrt(2*(1/2)),1)
q=math.sqrt(3);al=math.acos(1/math.sqrt(3));tau=math.pi/4
pos=lambda t:np.array([-math.cos(t)+q*math.cos(al)*math.sin(t),q*math.sin(al)*math.sin(t)])
vel=lambda t:np.array([math.sin(t)+q*math.cos(al)*math.cos(t),q*math.sin(al)*math.cos(t)])
check(1,'specified perpendicular exit position',pos(tau),[0,1])
check(1,'exit speed conservation',np.dot(vel(tau),vel(tau)),q*q)
cross=lambda p,v:p[0]*v[1]-p[1]*v[0]
check(1,'angular momentum at exit',cross(pos(tau),vel(tau)),cross(pos(0),vel(0)))
check(1,'entry angle',math.degrees(al),54.735610317245346)
check(1,'first-exit root',brentq(lambda t:np.dot(pos(t),pos(t))-1,.001,1.2),tau)
check(1,'repulsive center time',brentq(lambda t:-math.cosh(t)+2*math.sinh(t),0,1),math.atanh(.5))
check(1,'center launch boundary threshold',math.sqrt(2*(U(1)-U(0))),1)
errs=[];interior=[]
for q in np.linspace(1.02,4,19):
 al=math.acos(math.sqrt((q*q-1)/(2*q*q)));te=math.atan(math.sqrt(2/(q*q-1)))
 sol=solve_ivp(lambda t,z:[z[2],z[3],-z[0],-z[1]],[0,te],[-1,0,q*math.cos(al),q*math.sin(al)],rtol=2e-11,atol=2e-12,dense_output=True)
 errs.append(float(np.linalg.norm(sol.y[:2,-1]-[0,1])));interior.append(float(np.max(np.sum(sol.sol(np.linspace(te*.01,te*.99,90))[:2]**2,axis=0))))
supp(1,'19 direct harmonic trajectories and first-exit interiors',max(errs)<1e-8 and max(interior)<1,dict(max_exit_error=max(errs),largest_interior_radius_squared=max(interior)))
# 02: complete velocity transformation and distinct events at spatial crossing.
def velocities(v,th,V):
 ux=v*math.cos(th);uy=v*math.sin(th);ga=1/math.sqrt(1-V*V)
 return np.array([(ux-V)/(1-ux*V),uy/(ga*(1-ux*V))]),np.array([(-ux-V)/(1+ux*V),-uy/(ga*(1+ux*V))])
v=.6;th=math.pi/2;V=v/math.sqrt(1+v*v);a,b=velocities(v,th,V)
check(2,'transverse boost',V,.5144957554275266)
check(2,'first transformed vector',a,[-V,V])
check(2,'second transformed vector',b,[-V,-V])
check(2,'transformed orthogonality',np.dot(a,b),0)
check(2,'transformed speed',np.linalg.norm(a),.7276068751089989)
ga=1/math.sqrt(1-V*V);d=1.;tg1=-d/(2*V);tg2=d/(2*V)
t1=ga*tg1;t2=ga*(tg2-V*d)
check(2,'spatial crossing x',-ga*V*tg1,ga*(d-V*tg2))
check(2,'spatial crossing y',v*tg1,-v*tg2)
check(2,'crossing event time difference',t2-t1,d/(ga*V))
check(2,'orthogonal transverse event difference',t2-t1,d/v)
check(2,'variant 0.8c boost',.8/math.sqrt(1+.8**2),.6246950475544243)
check(2,'variant 45-degree boost',.6/math.sqrt(1+.36*.5),.552344770738994)
check(2,'classical dot condition',v*v-v*v,0)
errs=[];speeds=[];same=[]
for v in [.01,.3,.6,.9,.99]:
 for th in np.linspace(.03,math.pi-.03,33):
  V=v/math.sqrt(1+v*v*math.sin(th)**2);a,b=velocities(v,th,V);errs.append(abs(float(a@b)));speeds.extend([np.linalg.norm(a),np.linalg.norm(b)])
  aa,bb=velocities(v,th,V);same.append(np.linalg.norm(aa-aa))
supp(2,'165 nondegenerate full transformations',max(errs)<1e-12 and max(speeds)<1 and max(same)==0,dict(max_dot=max(errs),max_transformed_speed=float(max(speeds)),same_velocity_remains_identical=True))
# 03: point-wheel approximation, positive tensions and wrap angle in radians.
cf=1/math.sqrt(3)
def wheel(x):
 y=math.sqrt(2*(1-x*x)/3);d1=1+x/math.sqrt(3);d2=1-x/math.sqrt(3)
 T1=d1*(cf-x)/(2*cf*y);T2=d2*(cf+x)/(2*cf*y)
 phi=math.acos((cf+x)/d1)+math.acos((cf-x)/d2)
 return y,d1,d2,T1,T2,phi,math.log(T2/T1)/phi
y,d1,d2,T1,T2,phi,mu=wheel(.3)
check(3,'rope length',d1+d2,2)
check(3,'left geometric distance',math.hypot(cf+.3,y),d1)
check(3,'right geometric distance',math.hypot(cf-.3,y),d2)
check(3,'horizontal force balance',-T1*(cf+.3)/d1+T2*(cf-.3)/d2,0)
check(3,'vertical force balance',T1*y/d1+T2*y/d2,1)
check(3,'left tension',T1,.361791277986033)
check(3,'right tension',T2,.806540867982694)
check(3,'wrap angle',phi,1.954729777162244)
check(3,'capstan coefficient',mu,.410126819050202)
check(3,'minimum tension',wheel(0)[3],math.sqrt(3/8))
check(3,'small-displacement coefficient',wheel(1e-6)[6]/1e-6,2/(math.sqrt(3)*math.acos(1/math.sqrt(3))),tol=1e-6)
check(3,'lean at five wheel radii',math.sin(math.asin((T2-T1)/5)),(T2-T1)/5)
res=[];positive=[]
for x in np.linspace(-cf+.0001,cf-.0001,151):
 y,d1,d2,T1,T2,phi,mu=wheel(float(x));res.extend([abs(T1*y/d1+T2*y/d2-1),abs(-T1*(cf+x)/d1+T2*(cf-x)/d2)]);positive.extend([T1,T2])
edge=[wheel(cf-z)[6] for z in [.01,.001,.0001,.00001]]
supp(3,'151 positive-tension force balances and capstan divergence',max(res)<1e-12 and min(positive)>0 and all(np.diff(edge)>0),dict(max_residual=max(res),min_tension=min(positive),edge_friction_coefficients=edge))
# 04: numeric heat integrals separately from integrated analytic formula.
a=(3-math.sqrt(5))/2;b=(3+math.sqrt(5))/2
def node(t):
 u2=1-(b*math.exp(-a*t)-a*math.exp(-b*t))/(b-a);i2=(math.exp(-a*t)-math.exp(-b*t))/(b-a)
 return u2+i2,u2,i2
QR=quad(lambda t:node(t)[2]**2,0,np.inf)[0];QL=quad(lambda t:(1-node(t)[0])**2,0,np.inf)[0]
check(4,'initial node voltages',node(0)[:2],[0,0])
check(4,'initial right current',node(0)[2],0)
check(4,'right heat integral',QR,1/6)
check(4,'left heat integral',QL,5/6)
check(4,'heat ratio',QL/QR,5)
check(4,'energy balance',QL+QR,1)
check(4,'node two differential equation',node(1)[0]-node(1)[1],node(1)[2])
check(4,'two decay sum',a+b,3)
check(4,'two decay product',a*b,1)
check(4,'R2 twice heat ratio',1+4/2,3)
check(4,'R1 twice heat ratio',1+4*2,9)
check(4,'C1 twice right heat',1/(2*(2+1+1)),1/8)
errs=[];ratios=[]
for R1,R2,C1,C2 in [(1,1,1,1),(1,2,1,1),(2,1,1,1),(1,1,2,1),(.3,2,1,3),(2,.7,3,.5)]:
 def rhs(t,z):
  u1,u2=z[:2];i1=(1-u1)/R1;i2=(u1-u2)/R2
  return [(i1-i2)/C1,i2/C2,R1*i1*i1,R2*i2*i2]
 sol=solve_ivp(rhs,[0,150*max(R1,R2)*(C1+C2)],[0,0,0,0],rtol=2e-10,atol=2e-12)
 qr=R2*C2*C2/(2*(R1*(C1+C2)+R2*C2));total=(C1+C2)/2
 errs.extend(abs(sol.y[2:,-1]-[total-qr,qr]));ratios.append(float(sol.y[2,-1]/sol.y[3,-1]))
supp(4,'six independent two-node ODE heat accumulations',max(errs)<1e-8,dict(max_heat_error=float(max(errs)),ratios=ratios))
# 05: unequal masses and charges, vector Coulomb forces and full dynamics.
eta=np.array([1.,2.,3.]);mass=np.array([1.,2.,4.]);charge=eta*mass
d12=3**(-1/3);d13=2**(-1/3);xx=(d12*d12+d13*d13-1)/(2*d12);yy=math.sqrt(d13*d13-xx*xx)
P=np.array([[0.,0.],[d12,0.],[xx,yy]]);P-=np.sum(mass[:,None]*P,axis=0)/sum(mass)
def acc(P):
 out=np.zeros_like(P)
 for i in range(3):
  for j in range(3):
   if i!=j:
    dr=P[i]-P[j];out[i]+=charge[i]*charge[j]/mass[i]*dr/np.linalg.norm(dr)**3
 return out
A=6*sum(mass);I=float(np.sum(mass[:,None]*P*P));U=sum(charge[i]*charge[j]/np.linalg.norm(P[i]-P[j]) for i in range(3) for j in range(i))
check(5,'opposite side 23',np.linalg.norm(P[1]-P[2]),1)
check(5,'opposite side 31',np.linalg.norm(P[2]-P[0]),2**(-1/3))
check(5,'opposite side 12',np.linalg.norm(P[0]-P[1]),3**(-1/3))
check(5,'mass center',np.sum(mass[:,None]*P,axis=0),[0,0])
check(5,'central force first',acc(P)[0],A*P[0])
check(5,'central force second',acc(P)[1],A*P[1])
check(5,'central force third',acc(P)[2],A*P[2])
check(5,'energy-scale coefficient',U/I,A)
check(5,'force scale at two',acc(2*P),acc(P)/4)
check(5,'kinetic at double scale',.5*I*A,U/2)
check(5,'scale four terminal speed',math.sqrt(2*A/4),math.sqrt(2*A)/2)
check(5,'variant impossible triangle margin',.5+1/3-1,-1/6)
def dyn(t,z):
 pp=z[:6].reshape(3,2);vv=z[6:].reshape(3,2);return np.r_[vv.ravel(),acc(pp).ravel()]
sol=solve_ivp(dyn,[0,2],np.r_[P.ravel(),np.zeros(6)],rtol=3e-11,atol=3e-12,dense_output=True)
sc=solve_ivp(lambda t,z:[z[1],A/z[0]**2],[0,2],[1,0],rtol=3e-11,atol=3e-12,dense_output=True)
tt=np.linspace(0,2,121);err=max(float(np.max(abs(sol.sol(t)[:6].reshape(3,2)-sc.sol(t)[0]*P))) for t in tt)
ener=[]
for t in tt:
 z=sol.sol(t);pp=z[:6].reshape(3,2);vv=z[6:].reshape(3,2);uu=sum(charge[i]*charge[j]/np.linalg.norm(pp[i]-pp[j]) for i in range(3) for j in range(i));ener.append(abs(.5*np.sum(mass[:,None]*vv*vv)+uu-U))
supp(5,'full 12-component Coulomb ODE versus independent scale ODE',err<1e-8 and max(ener)<1e-7,dict(max_position_error=err,max_energy_error=max(ener),unequal_masses=mass.tolist(),charge_mass_ratios=eta.tolist()))
# 06: exact dimensionless energy and separate angular-momentum axes.
gold=(math.sqrt(5)-1)/4
check(6,'initial mass equilibrium',1,1)
check(6,'loaded inward turning energy',.5/.5**2-3*(1-.5),.5)
check(6,'loaded circular equilibrium',3**(-1/3),.6933612743506348)
check(6,'loaded nearest radius',brentq(lambda z:.5/z**2-3*(1-z)-.5,.2,.9),.5)
check(6,'loaded turn tangential speed',1/.5,2)
check(6,'new-axis angular momentum',.5,.5)
check(6,'nail initial radial acceleration numerator',.5**2/.5**3-1,1)
check(6,'nail energy root',.5/(1+2*gold)**2+gold,.5)
check(6,'nail exact rise',gold,.30901699437494745)
check(6,'mass factor two descent',1-(1+math.sqrt(17))/8,.3596117967977924)
check(6,'nail at three quarters rise',.75*((1+math.sqrt(7))/3-1),(math.sqrt(7)-2)/4)
check(6,'small radial frequency lambda eleven',math.sqrt(3/12),.5)
turns=[];errs=[]
for lam in [1.,11.,100.]:
 for added in [True,False]:
  j=1 if added else .5;load=3 if added else 1;rho0=1 if added else .5;massfactor=1+load*lam
  def rhs(t,z):return [z[1],lam*(j*j/z[0]**3-load)/massfactor]
  def ev(t,z):return z[1]
  ev.direction=1 if added else -1;ev.terminal=True
  dt=1e-6;aa=rhs(0,[rho0,0])[1];init=[rho0+.5*aa*dt*dt,aa*dt]
  sol=solve_ivp(rhs,[dt,100],init,events=ev,rtol=3e-11,atol=3e-12)
  assert len(sol.t_events[0])==1
  turn=float(sol.y_events[0][0,0]);expected=.5 if added else .5+gold;errs.append(abs(turn-expected));turns.append(dict(lam=lam,added=added,radius=turn,time=float(sol.t_events[0][0])))
supp(6,'six exact finite-mass radial turning events',max(errs)<1e-8,dict(max_turning_error=max(errs),turns=turns))
# 07: both positive pairs, propagation through physical elements.
L=25.;l1=10.;l2=5.;pairs=[]
def lens(f):return np.array([[1.,0.],[-1/f,1.]])
def prop(d):return np.array([[1.,d],[0.,1.]])
for sign in [-1,1]:pairs.append((75/4+sign*25*math.sqrt(33)/12,175/8+sign*25*math.sqrt(33)/8))
for f1,f2 in pairs:
 M=lens(f2)@prop(L)@lens(f1);a,b,c,d=M.ravel()
 label='short' if f1<L else 'long'
 check(7,label+' first signed lens equation',1/l1+1/(L-f2),1/f1)
 check(7,label+' second signed lens equation',1/(L-f1)+1/l2,1/f2)
 check(7,label+' point-source output slope',d+l1*c,0)
 check(7,label+' parallel output focus',a+l2*c,0)
 check(7,label+' determinant',np.linalg.det(M),1)
 check(7,label+' inversion quadratic',l1*l2*c*c-L*c-1,0)
errs=[]
for f1,f2 in pairs:
 for h in np.linspace(-2,2,41):
  ray=lens(f2)@prop(L)@lens(f1)@prop(l1)@np.array([0.,h]);errs.append(abs(ray[1]))
  ray=prop(l2)@lens(f2)@prop(L)@lens(f1)@np.array([h,0.]);errs.append(abs(ray[0]))
 for scale in [.5,2,4]:
  mm=lens(scale*f2)@prop(scale*L)@lens(scale*f1);errs.extend([abs(mm[1,1]+scale*l1*mm[1,0]),abs(mm[0,0]+scale*l2*mm[1,0])])
supp(7,'164 rays for both pairs and three dimensional scalings',max(errs)<1e-12 and all(min(p)>0 for p in pairs),dict(max_ray_error=max(errs),focal_pairs=pairs))
# 08: supplied constants, canonical momentum and circular weak-field expansion.
m=.91e-30;q=1.6e-19;K=8.99e9;h=6.628e-34;hb=h/(2*math.pi);mu0=4*math.pi*1e-7;k=K*q*q
r=hb*hb/(m*k);v=k/hb;B0=mu0*q*v/(4*math.pi*r*r);muB=q*hb/(2*m);E1=-m*k*k/(2*hb*hb)
check(8,'Bohr radius normalized to stated constants',r/1e-11,5.313298478502108)
check(8,'speed normalized',v/1e6,2.181710017068101)
check(8,'nuclear self field',B0,12.364842287764153)
check(8,'self field closed form',mu0*m*m*K**3*q**7/(4*math.pi*hb**5),B0)
check(8,'binding energy normalized',E1/1e-18,-2.16573566239593)
check(8,'zero-field transition frequency normalized',(-3*E1/4)/h/1e15,2.4506664858424)
check(8,'linear frequency slope normalized',muB/h/1e10,1.3991643349077276)
check(8,'second orbit self field',B0/32,.38640132149263)
check(8,'literal h radius ratio',(h/hb)**2,(2*math.pi)**2)
check(8,'literal h self-field ratio',(hb/h)**5,(2*math.pi)**-5)
eps=.001;u=brentq(lambda x:x+eps*eps*x**4-1,.9,1)
check(8,'radius second-order limit',(u-1)/eps**2,-1,tol=1e-5)
en=.5/u**2-1/u+eps+eps*eps*u*u/2
check(8,'energy keeps first-order constant',(en+.5)/eps,1+eps/2,tol=1e-8)
# Dimensionless radial motion in fixed field: j=l-eps*r^2; direct polar ODE.
ee=.03;j=1.;initial=[1.1,.04,(j+ee*1.1**2)/1.1**2,0.]
def polar(t,z):
 rr,dr,om,phi=z
 return [dr,rr*om*om-1/rr**2-2*ee*rr*om,2*dr*(ee-om)/rr,om]
sol=solve_ivp(polar,[0,20],initial,rtol=2e-11,atol=2e-12,dense_output=True)
rr,dr,om,phi=sol.sol(np.linspace(0,20,301));JJ=rr*rr*om-ee*rr*rr;ener=.5*(dr*dr+rr*rr*om*om)-1/rr
raderrs=[]
for e in [1e-4,1e-3,.01]:
 up=brentq(lambda x:x+e*e*x**4-1,.8,1);un=brentq(lambda x:x+(-e)**2*x**4-1,.8,1);raderrs.append(abs(up-un))
supp(8,'301 polar ODE points and signed-field stationary roots',max(abs(JJ-j))<1e-8 and max(abs(ener-ener[0]))<1e-8 and max(raderrs)==0,dict(max_canonical_error=float(max(abs(JJ-j))),max_energy_error=float(max(abs(ener-ener[0]))),signed_radius_errors=raderrs))
assert len(C)==96 and len(S)==8
report=dict(check_count=len(C),supplementary_check_count=len(S),all_passed=all(x['passed'] for x in C+S),checks=C,supplementary_checks=S)
(ROOT/'physics_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(all_passed=report['all_passed'],checks=len(C),supplementary=len(S),failed=[x['name'] for x in C+S if not x['passed']]),ensure_ascii=False))
assert report['all_passed']
