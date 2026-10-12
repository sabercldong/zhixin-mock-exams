"""Independent checks of the fifteen new solved variants, with draft binding."""
from pathlib import Path
import hashlib,json,math,re
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
SET=int(re.search(r'蔡题(\d+)',str(ROOT)).group(1))
rows=[]
def record(q,v,method,values):
 p=ROOT/f'drafts/question-{q:02}.md'
 rows.append(dict(question=q,variant=v,passed=True,method=method,values=values,
                  draft_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
def close(x,y,tol=1e-8):
 assert abs(x-y)<tol*max(1,abs(y)),(x,y,tol)
if SET==19:
 # Solve the full implicit shape, then compare finite differences to its
 # sensitivity over a grid, rather than only substituting the example.
 errors=[]
 for z in [.1,1,15,50]:
  for e in [0,.1,1,10]:
   root=lambda eta:brentq(lambda w:w**4+eta*(w-1)-1-z,1,1+(1+z)**.25,xtol=1e-14)
   w=root(e);h=1e-5
   deriv=(1/root(e+h)-1/root(e-h))/(2*h)
   exact=(w-1)/(w*w*(4*w**3+e));close(deriv,exact)
   errors.append(abs(deriv-exact));assert exact>0
 record(1,4,'Implicit roots and central finite differences at sixteen parameter pairs',dict(max_error=max(errors),zero_tension_sensitivity=1/128))
 # Construct image charges directly and numerically differentiate their force.
 l=h=m=g=1.;K=1.;S=float(sp.zeta(3)*sp.Rational(7,8));q=math.sqrt(1.2/S);ks=.3
 def force(x):
  j=np.arange(-10000,10001,dtype=float);pos=(4*j+2)*l-x
  return float(np.sum(-K*q*q*(x-pos)/np.abs(x-pos)**3))
 dx=1e-5;electric_slope=(force(dx)-force(-dx))/(2*dx)
 close(electric_slope,1.2,1e-7)
 stiffness=m*g/h+ks-electric_slope;close(stiffness,.1,1e-7)
 record(2,4,'Direct 20,001-image Coulomb force derivative plus gravity and spring',dict(electric_slope=electric_slope,stiffness=stiffness,period_ratio=math.sqrt(10)))
 # Integrate each instantaneous resistor power and reconstruct source power.
 n1,n2,n3,r=200,100,60,10
 u=lambda t:12*math.sin(t)+4*math.sin(3*t)
 avg=lambda f:quad(f,0,2*math.pi,epsabs=1e-10)[0]/(2*math.pi)
 ind=avg(lambda t:(n2*n2+n3*n3)*u(t)**2/(n1*n1*r))
 plus=avg(lambda t:(n2+n3)**2*u(t)**2/(n1*n1*2*r))
 minus=avg(lambda t:(n2-n3)**2*u(t)**2/(n1*n1*2*r))
 for a,b in zip([ind,plus,minus],[2.72,2.56,.16]):close(a,b)
 source=avg(lambda t:u(t)*((n2/n1)*(n2/n1)*u(t)/r+(n3/n1)*(n3/n1)*u(t)/r));close(source,ind)
 record(3,4,'Time integration of non-sinusoidal resistor power and input power',dict(independent=ind,series_plus=plus,series_minus=minus,input_power=source))
 G=400*.7/1.3;s=.01;eps=np.array([[0,s/2],[s/2,0]])
 stress=2*G*eps;ev=np.linalg.eigvalsh(stress);close(ev[1],G*s);close(ev[0],-G*s)
 energy=float(np.sum(stress*eps)/2);work=quad(lambda t:G*t,0,s)[0];close(energy,work)
 grad=np.array([[0,-.01],[.01,0]]);assert np.max(np.abs(grad+grad.T))==0
 record(4,4,'Stress eigenvalues, boundary loading work and zero rigid-rotation strain',dict(shear_modulus=G,principal_stresses=ev.tolist(),energy_density=energy))
 integrals=[]
 for beta in [0,.3,.6,.9,.99]:
  integral=quad(lambda t:(1-beta*beta)*math.sin(t)/(1-beta*beta*math.sin(t)**2)**1.5,0,math.pi,epsabs=1e-11)[0]
  close(integral,2);integrals.append(dict(beta=beta,flux_over_2pi_kq=integral))
 record(5,4,'Numerical solid-angle flux integral over five speeds',dict(integrals=integrals))
elif SET==20:
 def echo(k,b):return brentq(lambda t:t-2*k*math.sin((2*math.pi-b*t)/(2*k)),0,2*k)
 slopes=[]
 for beta in [.001,.003,.01]:
  t2=echo(2,beta);assert abs(t2-(4-2*beta*beta))<3*beta**4
  t3=echo(3,beta);close(t3,3*math.sqrt(3)-3*math.sqrt(3)*beta/2,1e-4)
  slopes.append(dict(beta=beta,two=t2,three=t3))
 record(1,3,'Direct implicit arrival roots and small-speed asymptotics',dict(samples=slopes))
 beta=.2;tau=echo(2,beta);delta=(2*math.pi-beta*tau)/2
 # Build both chord vectors and project on receiver tangent, independent of
 # the trigonometric j expression used in the solution.
 pts=[np.array([math.cos(-i*delta),math.sin(-i*delta)]) for i in range(3)]
 ray=(pts[2]-pts[1]);ray/=np.linalg.norm(ray)
 tangent=np.array([-math.sin(beta*tau),math.cos(beta*tau)])
 j=float(ray@tangent);close(j,-math.sin(beta*tau/4))
 ratio=1-beta*j;close(ratio,1.038982,1e-6)
 record(1,4,'Reflected chord direction projected onto moving receiver tangent',dict(tau=tau,j=j,frequency_ratio=ratio))
 r=sp.symbols('r',positive=True);W=r*r/(r*r+1)**3;rb=sp.sqrt(2)/2
 k2=sp.simplify(-sp.diff(W,r,2).subs(r,rb)/2);assert k2==sp.Rational(32,81)
 k=math.sqrt(float(k2));d=.002;times=[]
 for extra in [1e-7,1e-8,1e-9]:
  full=quad(lambda x:1/math.sqrt(4/27+extra-x*x/(x*x+1)**3),float(rb)-d,float(rb)+d,epsabs=1e-9)[0]
  local=2/k*math.asinh(k*d/math.sqrt(extra));close(full,local,1e-4)
  times.append(dict(excess_speed_squared=extra,full_time=full,local_time=local))
 record(2,3,'Symbolic barrier curvature and exact/local transit-time integration',dict(kappa_squared=float(k2),samples=times))
 # Direct Cartesian Lorentz ODE in the equatorial plane for original and
 # rescaled dipoles. Units q/m=1, mu0*m0/(2pi)=C.
 def path(h,C,T):
  def rhs(t,z):
   x,y,vx,vy=z;r2=x*x+y*y;B=C*(2*h*h-r2)/(r2+h*h)**2.5
   return [vx,vy,vy*B,-vx*B]
  return solve_ivp(rhs,[0,T],[0,0,.8,0],rtol=1e-10,atol=1e-12,dense_output=True)
 a=path(1,1,4);b=path(2,4,8);ts=np.linspace(0,4,41)
 error=float(np.max(np.abs(b.sol(2*ts)[:2]-2*a.sol(ts)[:2])));assert error<1e-8
 record(2,4,'Two full Cartesian Lorentz integrations under the proposed similarity scaling',dict(max_position_error=error,original_vc=2/(3*math.sqrt(3)),scaled_vc=2*4/(3*math.sqrt(3)*4)))
 # Vary input data and use finite differences of the nonlinear inverse.
 inv=lambda R,D:(27*math.sqrt(3)/5*D*R**5)**(1/6)
 R=100.;L=1.;D=5*L**6/(27*math.sqrt(3)*R**5);close(inv(R,D),L)
 e=1e-5;dR=(math.log(inv(R*(1+e),D))-math.log(inv(R*(1-e),D)))/(2*e)
 dD=(math.log(inv(R,D*(1+e)))-math.log(inv(R,D*(1-e))))/(2*e)
 close(dR,5/6);close(dD,1/6)
 record(3,3,'Nonlinear inverse and finite-difference logarithmic error sensitivities',dict(recovered_l=inv(R,D),sensitivity_R=dR,sensitivity_range=dD))
 omega0=1.;Omega=.003;phase=.73;T0=2*math.pi;n=np.arange(100)
 real=np.cos(3*(omega0-Omega)*n*T0+phase);aliased=np.cos(phase-6*math.pi*n*Omega)
 err=float(np.max(np.abs(real-aliased)));assert err<1e-11
 samples=np.cos(phase+np.array([0,math.pi/2,math.pi]));close((samples[0]-samples[2])/2,math.cos(phase));close(-samples[1],math.sin(phase))
 record(3,4,'Explicit fast-signal sampling and phase reconstruction',dict(max_alias_identity_error=err,three_samples=samples.tolist()))
 # Integrate exact radial energy with x=A*sin(theta), which removes the
 # turning-point singularity. A closed difference avoids cancellation.
 def potential(x):return .5*((1+x)**-2+(1-x)**-2)
 T0=2*math.pi/math.sqrt(3);periods=[]
 for A in [.005,.01,.02]:
  def integrand(theta):
   x=A*math.sin(theta)
   # U(A)-U(x) factored analytically in x^2 to avoid catastrophic cancellation.
   z=A*A;w=x*x
   diff=(z-w)*(3-z-w-z*w)/((1-z)**2*(1-w)**2)
   return 4*A*math.cos(theta)/math.sqrt(diff)
  T=quad(integrand,0,math.pi/2,epsabs=1e-9)[0]
  prediction=T0*(1-1.25*A*A);close(T,prediction,1e-6);periods.append(dict(amplitude=A,exact_period=T,asymptotic_period=prediction))
 record(4,3,'Exact nonlinear period by energy quadrature, compared with amplitude correction',dict(samples=periods))
 ratio=2**(2/3);r1=2*ratio/(1+ratio);r2=2/(1+ratio)
 close(4/r1**3,1/r2**3)
 f=lambda x:(4/(r1+x)**3-1/(r2-x)**3)/2
 dx=1e-5;k2=1.5*(4/r1**4+1/r2**4);close(-(f(dx)-f(-dx))/(2*dx),k2)
 record(4,4,'Equal-tension equilibrium and direct force linearization after unequal impulses',dict(r1=r1,r2=r2,frequency_squared=k2))
 def imaging(x):
  f=1.6;u1=8+x;v1=f*u1/(u1-f);u2=10-v1;v2=f*u2/(u2-f)
  return v2,f*f/((u1-f)*(u2-f))
 x=1.;h=1e-4;X,M=imaging(x);deriv=(imaging(x+h)[0]-imaging(x-h)[0])/(2*h);close(deriv,-M*M)
 linear=1e-5/(M*M);exact=brentq(lambda z:imaging(z)[0]-(X-1e-5),1,1.1)-1
 close(exact,linear,3e-6)
 record(7,4,'Sequential mirror imaging, finite-difference axial derivative and inverse displacement',dict(M=M,derivative=deriv,estimated_dx=linear,exact_dx=exact))
 pmax=math.sqrt(96)/5;pstar=math.sqrt(3)
 energies_rest=[1,math.sqrt(1+pstar*pstar),math.sqrt(1+pstar*pstar)]
 energies_end=[math.sqrt(1+pmax*pmax),math.sqrt(1+pmax*pmax/4),math.sqrt(1+pmax*pmax/4)]
 close(sum(energies_rest),5);close(sum(energies_end),5)
 directions=np.random.default_rng(1).normal(size=(20,3));directions/=np.linalg.norm(directions,axis=1)[:,None]
 for p in pstar*directions:close(np.dot(p,-p)/(np.linalg.norm(p)**2),-1)
 record(8,4,'Endpoint energy conservation and opposite nonzero momenta on the rest-frame sphere',dict(pstar=pstar,pmax=pmax,energies_at_rest=energies_rest,energies_at_endpoint=energies_end))
else:raise AssertionError(SET)
assert len(rows)==(5 if SET==19 else 10)
(ROOT/'build/added-variant-math.json').write_text(json.dumps(dict(set=SET,all_passed=True,checks=rows),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(set=SET,all_passed=True,variant_checks=len(rows)),ensure_ascii=False))
