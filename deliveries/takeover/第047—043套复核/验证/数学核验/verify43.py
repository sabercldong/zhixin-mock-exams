from pathlib import Path
import json,math,numpy as np
from scipy.integrate import solve_ivp
from area43 import region
W=Path(__file__).parent;R=[]
for n in [47,46,45,44,43]:(W/str(n)).mkdir(exist_ok=True)
def record(q,name,got,want,tol=1e-8):
 err=float(np.max(np.abs(np.asarray(got)-np.asarray(want))))
 assert err<tol,(q,name,got,want,err)
 R.append(dict(set=43,question=q,check=name,max_error=err,tolerance=tol))
# car motions: direct piecewise integration
v=10.;a=1.;delay=math.sqrt(10)
s=lambda t: .5*a*t*t if 0<=t<10 else v*t-v*v/(2*a) if t>=10 else 0.
record(1,'time shifted displacement gives steady gap',2+s(50)-s(50-delay),2+v*delay)
for tau in [0,1,2,delay]:
 def brakepos(t,lag):
  z=max(0,min(10,t-lag));return v*min(t,lag)+v*z-.5*z*z
 times=np.linspace(0,10+tau,1001);gaps=np.array([2+v*delay+brakepos(t,0)-brakepos(t,tau) for t in times])
 record(1,f'minimum braking gap tau={tau:.4f}',min(gaps),2+v*delay-v*tau)
# 1D finite difference energy derivative
for L in [1.,2.,3.]:
 h=1e-5;energy=lambda x:9/(8*x*x)
 force=-(energy(L+h)-energy(L-h))/(2*h)
 record(2,f'wall force from independent finite difference L={L}',force,9/(4*L**3),1e-8)
for ell in [3,4,1000]:
 P=2*ell*math.sin(math.pi/ell);E=1/(2*P*P)
 want=1/54 if ell==3 else 1/64 if ell==4 else 1/(8*math.pi**2)
 record(2,f'polygon length ell={ell}',E,want,5e-8)
# dimensionless dust ODE da/dt=(2/3)/sqrt(a)
sol=solve_ivp(lambda t,z:[2/(3*math.sqrt(z[0]))],(1,5),[1],rtol=1e-11,atol=1e-12)
record(3,'dust scale from independent time integration',sol.y[0,-1],5**(2/3),1e-9)
H0=72000/(3.09e22);rho=3*H0*H0/(8*math.pi*6.67e-11)
R.append(dict(set=43,question=3,check='SI numerical age and critical density',H0=H0,t0_s=2/(3*H0),rho0=rho))
# black hole model limits
hb=1.054571817e-34;c=299792458;G=6.67430e-11;mp=1.67262192369e-27;kb=1.380649e-23
M=hb*c/(math.sqrt(2)*G*mp);r=hb*hb/(G*M*mp*mp);E=G*G*M*M*mp**3/(2*hb*hb)
record(4,'horizon crossing radius',r,2*G*M/(c*c),1e-25)
record(4,'formal boundary binding ratio',E/(mp*c*c),.25)
R.append(dict(set=43,question=4,check='Hawking scale and validity',M_limit=M,r_limit=r,E_J=E,T_toy=1e23/M,kT_over_E=kb*1e23/M/E,approximation='Newtonian limit fails at v=c/sqrt(2)'))
# radiation reversible entropy and power
for T,V in [(1,1),(2,3),(.7,1.4)]:
 h=1e-5;S=lambda T,V:4/3*V*T**3
 dSdT=(S(T+h,V)-S(T-h,V))/(2*h);dSdV=(S(T,V+h)-S(T,V-h))/(2*h)
 record(5,'entropy derivatives', [dSdT,dSdV],[4*V*T*T,4/3*T**3],1e-8)
alpha=72000/(3.26e6*c*365.25*86400)
R.append(dict(set=43,question=5,check='use supplied lightyear conversion',alpha_SI=alpha))
# unfolding segments: intersection on each positive mirror ray
rng=np.random.default_rng(43106)
for case in range(80):
 phi=rng.uniform(-35,35);theta=rng.uniform(36.01,323.99)
 if abs(theta-180-phi)<.01:continue
 unfolded=theta if theta<180+phi else theta-360
 k=math.floor((unfolded+36)/72);varphi=(-1)**k*(unfolded-72*k)
 assert -36<varphi<36
 o=rng.uniform(.2,2)*np.array([math.cos(math.radians(phi)),math.sin(math.radians(phi))]);i=rng.uniform(.2,2)*np.array([math.cos(math.radians(unfolded)),math.sin(math.radians(unfolded))]);di=i-o
 boundaries=[36+72*j for j in range(k)] if k>0 else [-36-72*j for j in range(-k)]
 ss=[]
 for angle in boundaries:
  ray=np.array([math.cos(math.radians(angle)),math.sin(math.radians(angle))]);s,rr=np.linalg.solve(np.column_stack((di,-ray)),-o)
  assert 0<s<1 and rr>0,(phi,theta,k,angle,s,rr)
  ss.append(s)
 assert np.all(np.diff(ss)>0)
R.append(dict(set=43,question=6,check='80 independent straight segment traces with random observer/image radii',pass_count=80,excluded='antipodal line through mirror vertex'))
# rods numerical time dynamics, including integrated displacement
for ms,rs in [([1,1],[.7,.7]),([.5,1],[.7,.35]),([.8,1.2],[.9,.4])]:
 m1,m2=ms;r1,r2=rs;b=1.3;C=.6;v1=2.1;v2=1.5;vf=(m1*v1+m2*v2)/(m1+m2+b*b*C)
 def rhs(t,z):
  p,q,V,S=z;I1=(b*p-V)/r1;I2=(b*q-V)/r2
  return [-b*I1/m1,-b*I2/m2,(I1+I2)/C,q-p]
 sol=solve_ivp(rhs,(0,40),[v1,v2,0,0],rtol=1e-11,atol=1e-12)
 S=(r2*m2*(v2-vf)-r1*m1*(v1-vf))/(b*b)
 record(7,f'rods ODE terminal velocities and displacement {ms}',sol.y[:,-1],[vf,vf,b*vf,S],1e-9)
 inv=m1*sol.y[0]+m2*sol.y[1]+b*C*sol.y[2]
 record(7,'conserved coupling combination',inv,np.full_like(inv,m1*v1+m2*v2),1e-10)
# all-inequality polygon area vs four-edge analytic formula
for N in range(4,24):
 for p in range(3,N):
  d=2*math.pi/N;A=(p-1)*d/2;B=(p+1)*d/2;C=math.sin(p*d/2)/math.sin(d/2)
  D=p/2+math.sin(p*d)/(2*math.sin(d))-C*C/p;E=p/2-math.sin(p*d)/(2*math.sin(d))
  ua=1/(C-p*math.cos(A));ub=1/(C-p*math.cos(B));ud=(math.sin(A)+math.sin(B))/(C*(math.sin(A)+math.sin(B))-p*math.sin(A+B));vd=(1+(p*math.cos(A)-C)*ud)/(p*math.sin(A))
  analytic=N*D*E*(ua-ub)*vd
  th,uv,pos,area=region(N,p)
  record(8,f'analytic vs all-leg inequalities N={N} p={p}',analytic,N*area,3e-8)
(W/'43/math_verification.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));print('PASS',len(R),'checks; alpha=',alpha)
