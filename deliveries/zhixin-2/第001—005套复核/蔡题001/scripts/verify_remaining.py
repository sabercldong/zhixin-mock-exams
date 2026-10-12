from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1];res={}
# Q4 centre field-energy integration, momentum, final energy and exterior barrier.
q4=[]
for q,Q,R,r,m,M,v in [(1,2,3,.2,2,4,2),(2,1,4,.3,3,5,2),(1,-2,3,.1,2,8,2)]:
 k=1.;mu=m*M/(m+M)
 Ui=k*q*q/(2*r)+k*Q*Q/(2*R)
 Uc=quad(lambda s:k*q*q/(2*s*s),r,R)[0]+quad(lambda s:k*(Q+q)**2/(2*s*s),R,np.inf)[0]
 assert abs(Uc-Ui-k*Q*q/R)<1e-11
 w=math.sqrt(v*v-2*k*Q*q/(R*mu));u=(m*v+M*w)/(m+M);V=(m*v-m*w)/(m+M)
 assert abs(m*u+M*V-m*v)<1e-12
 assert abs(.5*m*u*u+.5*M*V*V+Uc-(.5*m*v*v+Ui))<1e-11
 finalV=m*v/(m+M);Uf=k*(Q+q)**2/(2*R)
 H=.5*m*v*v+Ui-.5*(m+M)*finalV**2-Uf
 assert abs(H-(.5*mu*w*w+.5*k*q*q*(1/r-1/R)))<1e-11
 q4.append(dict(u=u,V=V,heat=H))
alpha=2.;star=brentq(lambda z:(2*z*z-1)/(z*(z*z-1)**2)-alpha,1.000001,100)
def U(z):return alpha/z-1/(2*z*z*(z*z-1))
assert U(star)<alpha and U(star)>max(U(star-.001),U(star+.001))
res['04']=dict(passed=True,centre_cases=q4,image_barrier_z=star,image_barrier_energy=U(star))
# Q5 work/Ohm checks independently from j, volume, force.
q5=[]
for a,b,c,rho,rhom,B,I,K in [(2,3,1,4,.2,2,1,2),(3,2,.5,1,.1,4,2,3),(1,2,1,2,.3,1,3,1.5)]:
 S1=b*c;S2=S1/K;p1=2.;p2=1.;H=p1-p2+I*B/b
 v1=math.sqrt(2*H/(rho*(K*K-1)));v2=K*v1
 j=I/(a*b);force=j*B*a*b*c;Rwater=rhom*c/(a*b);eps=rhom*j*c+v1*B*c
 P=eps*I;joule=rhom*j*j*a*b*c
 assert abs(P-joule-force*v1)<1e-12
 assert abs(.5*rho*v2*v2+p2-(.5*rho*v1*v1+p1+force/S1))<1e-12
 q5.append(dict(v1=v1,v2=v2,power=P))
res['05']=dict(passed=True,cases=q5)
# Q6 photon four-momentum and lightcone exact recoil.
q6=[]
for beta in [0,.01,.3,.7]:
 gam=1/math.sqrt(1-beta*beta);D=math.sqrt((1-beta)/(1+beta));Nenergy=1.
 pulseprime=D # whole source pulse energy
 dp_rest=2*pulseprime;dp_lab=gam*dp_rest
 assert abs(dp_lab-2/(1+beta))<1e-12
 eps=.00002;A=gam*(1+beta);Af=A+2*eps
 pi=.5*(A-1/A);pf=.5*(Af-1/Af)
 Ei=.5*(A+1/A);Ef=.5*(Af+1/Af);ref=eps/(A*Af)
 assert abs(Ei+eps-Ef-ref)<1e-12 and abs(pi+eps-pf+ref)<1e-12
 q6.append(dict(beta=beta,doppler=D,impulse_factor=dp_lab))
N=1*3e8**2/(2*1.6e10*300*1)*(math.sqrt(1.01/.99)-1)
res['06']=dict(passed=True,cases=q6,continuous_required_pulses=N,integer_required_pulses=math.ceil(N))
# Q7 full capacitance matrix ODE and independent quadrature.
C=R=E=1.;CM=np.array([[2,-1],[-1,2.]])
x0=np.linalg.solve(CM,[0,E]);assert np.max(abs(x0-[1/3,2/3]))<1e-14
sol=solve_ivp(lambda t,x:np.linalg.solve(CM,[E-x[0],-x[1]]),[0,80],x0,method='DOP853',rtol=1e-12,atol=1e-13,dense_output=True)
for t in np.linspace(0,25,90):assert max(abs(sol.sol(t)-[1-2/3*math.exp(-t/3),2/3*math.exp(-t/3)]))<1e-11
heat=quad(lambda t:2*sol.sol(t)[1]**2,0,80,epsabs=1e-10)[0]
assert abs(heat-4/3)<1e-10
th=1.5*math.log(2);xx=sol.sol(th);hh=quad(lambda t:2*sol.sol(t)[1]**2,0,th)[0]
assert abs(hh-2/3)<1e-11
assert max(abs(xx-[1-math.sqrt(2)/3,math.sqrt(2)/3]))<1e-11
res['07']=dict(passed=True,initial_nodes=x0.tolist(),heat=heat,half_heat_time=th,half_heat_capacitor_voltages=[float(xx[0]),float(1-xx[1]),float(xx[0]-xx[1])])
# Q8 all member and support forces, node equilibrium matrix independent of global moments.
q8=[]
for n in [1,2,4,8,16]:
 nodes=np.array([[j,y] for j in range(n+1) for y in [0,1]],float)
 edges=[]
 for j in range(n):edges.extend([(2*j,2*(j+1)),(2*j+1,2*(j+1)+1),(2*(j+1),2*(j+1)+1),(2*j,2*(j+1)+1)])
 A=np.zeros((len(nodes)*2,len(edges)+4));load=np.zeros(len(nodes)*2)
 for col,(a,b) in enumerate(edges):
  e=nodes[b]-nodes[a];e=e/np.linalg.norm(e);A[2*a:2*a+2,col]=e;A[2*b:2*b+2,col]=-e
 for k,row in enumerate([0,1,2,3]):A[row,len(edges)+k]=1
 for j in range(1,n+1):load[4*j+1]=-2.**(-(j-1))
 force=np.linalg.solve(A,-load);assert max(abs(A@force+load))<1e-10
 V=sum(2.**(-(j-1)) for j in range(1,n+1));H=sum(j*2.**(-(j-1)) for j in range(1,n+1))
 assert max(abs(force[-4:]-[H,V,-H,0]))<1e-10
 q8.append(dict(n=n,lower_support=force[-4:-2].tolist(),upper_support=force[-2:].tolist()))
res['08']=dict(passed=True,cases=q8,limit_lower=[4,2],limit_upper=[-4,0])
(ROOT/'preview/verify-remaining.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res,ensure_ascii=False))
