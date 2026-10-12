from pathlib import Path
import json,math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp,quad
from scipy.linalg import eigh
out=[]
def ck(name,a,b=None,tol=1e-8):
 ok=bool(a) if b is None else abs(a-b)<tol
 assert ok,(name,a,b)
 out.append(dict(name=name,passed=bool(ok),actual=float(a) if b is not None else bool(a),expected=None if b is None else float(b)))
T=.8*2/3
def G(m):return 2*np.sinh(m/T)/(1+2*np.cosh(m/T))
m=brentq(lambda m:G(m)-m,.001,.99)
P=np.array([np.exp(m/T),1,np.exp(-m/T)]);P/=P.sum()
ck('mean field root',m,.6776583220391559)
ck('probability normalization',P.sum(),1);ck('probability magnetization',P[0]-P[2],m)
df=.5*m*m-T*np.log((1+2*np.cosh(m/T))/3)
ck('free energy difference',df,-.025889980655678824)
ck('infinite line relative error',1-1/np.sqrt(1+.1**2),.004962809790010847)
for ratio in [.01,.1,10]:
 exact=quad(lambda z:ratio/(ratio**2+z*z)**1.5,-1,1)[0]
 ck('finite line integral '+str(ratio),exact,2/(ratio*np.sqrt(1+ratio**2)),1e-7)

H=1.672622e-27;He=6.644657e-27;e=9.109384e-31;delta=4*H-He-2*e
for f,eta in [(1,4.874862367888829),(.5,11.258165509623641),(.1,271.523686704784)]:
 gam=1+f*delta/He;aa=He*np.sqrt(gam*gam-1)/(4*H)
 ck('fuel ratio '+str(f),np.expm1(np.arctanh(.2)/aa),eta,1e-8)

m1=3.2;m2=3.55;a=.696;c=.313;g=9.8;M=np.diag([m1,m2]);off=g*(m2-m1)/(4*c)
K=np.array([[g*(m1+m2)/(2*(a-c))+off,-off],[-off,g*(m1+m2)/(2*(a+c))+off]])
z,V=eigh(K,M);v1=V[:,0]/V[1,0];v2=V[:,1]/V[0,1];co=np.linalg.solve(np.column_stack([v1,v2]),[1,0])
ck('mode orthogonality',v1@M@v2,0)
ck('mode initial A',np.column_stack([v1,v2])[0]@co,1)
ck('mode initial B',np.column_stack([v1,v2])[1]@co,0)
ck('mode energy',sum(.5*co[i]**2*z[i]*(vv@M@vv) for i,vv in enumerate([v1,v2])),.5*K[0,0])

# Direct one-period Floquet integration for the supplied high-frequency example.
eps=.0001;b=.02
def rhs(t,y):
 P=y.reshape((2,2));return (np.array([[0,1],[eps+b*np.cos(t),0]])@P).ravel()
sol=solve_ivp(rhs,[0,2*np.pi],np.eye(2).ravel(),rtol=1e-11,atol=1e-12)
Floq=sol.y[:,-1].reshape((2,2));ck('Floquet determinant',np.linalg.det(Floq),1,1e-9)
ck('Floquet stable trace',abs(np.trace(Floq))<2)
Omega=np.arccos(np.trace(Floq)/2)/(2*np.pi)
ck('Floquet slow rate',Omega,.01,2e-5)

pm=1116;dm=140;om=938;beta=.773;gam=1/np.sqrt(1-beta*beta)
Es=(pm*pm+dm*dm-om*om)/(2*pm);ps=np.sqrt(Es*Es-dm*dm);B=beta*Es/ps
thmax=np.arctan(1/(gam*np.sqrt(B*B-1)));th0=thmax/2;D=gam*gam*np.tan(th0)**2
zm=(-D*B-np.sqrt(1+D-D*B*B))/(1+D);zp=(-D*B+np.sqrt(1+D-D*B*B))/(1+D)
prob=1-(zp-zm)/2;ck('decay cone probability',prob,.29349414527022843)
for zz in [zm,zp]:
 ck('decay cone boundary '+str(zz),np.arctan(np.sqrt(1-zz*zz)/(gam*(zz+B))),th0)
grid=np.linspace(-1,1,200001);theta=np.arctan(np.sqrt(1-grid*grid)/(gam*(grid+B)))
ck('decay cone direct angular sample',np.mean(theta<=th0),prob,2e-5)
ck('decay lower energy',gam*(Es-beta*ps),149.06966522203516)
ck('decay upper energy',gam*(Es+beta*ps),395.01729385841725)
ck('uniform energy density normalization',(gam*(Es+beta*ps)-gam*(Es-beta*ps))/(2*gam*beta*ps),1)
Path(__file__).with_name('case_math_verification.json').write_text(json.dumps(dict(count=len(out),checks=out,Floquet=Floq.tolist(),Floquet_slow_rate=Omega),ensure_ascii=False,indent=2))
print(len(out),'case checks passed; Floquet trace',np.trace(Floq))
