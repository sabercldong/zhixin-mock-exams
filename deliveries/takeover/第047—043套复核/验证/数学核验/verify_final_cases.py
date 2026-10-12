from pathlib import Path
import json,numpy as np,sympy as s
from scipy.optimize import brentq
from scipy.integrate import quad,solve_ivp
rows=[]
def ck(name,a,b,tol=1e-8):
 assert abs(a-b)<tol,(name,a,b)
 rows.append(dict(name=name,actual=float(a),expected=float(b),passed=True))
y,w=s.symbols('y w',positive=True)
G=2*w*s.sinh(y)/(1+2*w*s.cosh(y))
coef=s.expand(s.series(G,y,0,5).removeO()).coeff(y,3)
assert s.simplify(coef-w*(1-4*w)/(3*(1+2*w)**2))==0
rows.append(dict(name='anisotropy cubic coefficient',passed=True))
series=s.series(G.subs(w,s.Rational(1,4)),y,0,7).removeO()
assert s.simplify(series-y/3+y**5/540)==0
rows.append(dict(name='tricritical quintic stabilization',passed=True))
Tc=brentq(lambda T:T-2/(np.exp(.1/T)+2),.3,.7)
ck('anisotropic critical temperature',Tc,.6305446632894578)
ck('original Tc limit',2/(np.exp(0)+2),2/3)
ck('tricritical linear condition',2*.25/(1+2*.25),1/3)

def Z(q):return 2*(5-10*(1-.5*np.cos(q))-3*(q-.5*np.sin(q)))/(1.75-np.cos(q))
def force(q,z):
 dd=-(3*(1-.5*np.cos(q))+5*np.sin(q)+.5*np.sin(q)*z)/(1.75-np.cos(q))
 return dd,-3-(1-.5*np.cos(q))*dd-.5*np.sin(q)*z,10+.5*np.sin(q)*dd+.5*np.cos(q)*z
qs=brentq(lambda q:abs(force(q,Z(q))[1])/force(q,Z(q))[2]-.25,-.3,-1e-6)
ts=quad(lambda u:2*u/np.sqrt(Z(-u*u)),0,np.sqrt(-qs))[0]
ck('first slip angle',qs,-.18366098946440101)
ck('first slip time',ts,.4548230571645221)
ck('first slip speed squared',Z(qs),.5032379388448904)
def event(t,y):return abs(force(y[0],y[1]**2)[1])/force(y[0],y[1]**2)[2]-.25
event.terminal=True
dyn=solve_ivp(lambda t,y:[y[1],force(y[0],y[1]**2)[0]],(0,1),[0,0],events=event,rtol=1e-11,atol=1e-12)
ck('independent slip ODE time',dyn.t_events[0][0],ts,1e-8)
ck('independent slip ODE angle',dyn.y_events[0][0][0],qs,1e-8)
Path(__file__).with_name('final_math_verification.json').write_text(json.dumps(dict(count=len(rows),checks=rows),indent=2))
print(len(rows),'final model checks passed')
