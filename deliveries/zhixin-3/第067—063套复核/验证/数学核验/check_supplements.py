"""Cross-check selected newly expanded variants and limits; not a physical-assumption proof."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
from scipy.optimize import brentq
from scipy.integrate import quad
out=[]
def ident(x):assert s.simplify(x)==0,s.simplify(x)
def close(x,y):assert np.allclose(x,y,rtol=1e-8,atol=1e-9),(x,y)
def record(n,q,label,v):out.append(dict(set=n,question=q,check=label,result=v,passed=True))
x=s.symbols('x',positive=True);ident(s.diff(x/(1+x*x)**4,x)-(1-7*x*x)/(1+x*x)**5);close((1/np.sqrt(7))/(1+1/7)**4,7**3.5/8**4)
record(65,2,'无量纲平均力导数与峰值',{'peak_x':1/np.sqrt(7)})
t,om,w,q,E,m=s.symbols('t om w q E m',positive=True);xp=q*E/(m*(w*w-om*om))*(s.cos(om*t)-s.cos(w*t));ident(s.diff(xp,t,2)+w*w*xp-q*E/m*s.cos(om*t));ident(xp.subs(t,0));ident(s.diff(xp,t).subs(t,0));lim=q*E*t*s.sin(w*t)/(2*m*w);ident(s.diff(lim,t,2)+w*w*lim-q*E/m*s.cos(w*t))
record(65,4,'无阻尼突然接通的全初值解与共振解',{'zero_initial_values':True})
T,Ti,V,S,c,a,C0=s.symbols('T Ti V S c a C0',positive=True);tc=16*V/(S*c)*s.log(Ti/T)+4*C0/(3*S*a*c)*(T**-3-Ti**-3);ident(s.diff(tc,T)+(4*a*V*T**3+C0)/(S*a*c*T**4/4))
record(65,5,'含常壁热容的冷却积分',{'energy_balance_derivative':True})
l,l0,F,P=s.symbols('l l0 F P',positive=True);Pi=F*(l-l0-l0*s.log(l/l0))-P*(l-l0);ident(s.diff(Pi,l).subs(l,l0*F/(F-P)));ident(s.diff(Pi,l,2)-F*l0/l**2);val=quad(lambda z:1/(.8-.3*z),0,1)[0];close(val,np.log(.8/.5)/.3)
record(66,1,'恒载势能曲率与悬绳积分样例',{'length_ratio':val})
eta,d,tau=s.symbols('eta d tau',nonnegative=True);FF=(eta+d/tau)**2+(tau/2-1-1/tau)**2;expanded=tau*tau/4-tau+eta*eta+(2*eta*d+2)/tau+(d*d+1)/tau**2;ident(FF-expanded);ident(s.diff(FF,tau,2)-(s.Rational(1,2)+2*(2*eta*d+2)/tau**3+6*(d*d+1)/tau**4));fn=s.lambdify(tau,FF.subs({eta:.25,d:1}),'numpy');df=s.lambdify(tau,s.diff(FF,tau).subs({eta:.25,d:1}),'numpy');minimum=brentq(df,.1,10);roots=[brentq(lambda z:fn(z)-1,.01,minimum),brentq(lambda z:fn(z)-1,minimum,10)];angles=[]
for tt in roots:
 sa=.25+1/tt;ca=tt/2-1-1/tt;close(sa*sa+ca*ca,1);angles.append(float(np.degrees(np.arctan2(sa,ca))))
assert all(abs(x-y)<.003 for x,y in zip(sorted(angles),[29.140,127.838]))
record(65,3,'一般抛速四次方程、严格凸性和两支原题根',{'tau':roots,'relative_angles_degrees':angles,'critical_k':float(np.sqrt(fn(minimum)))})
la=2.5;theta=.03;vv=.04;AA=(theta+vv/la)/2;DD=(theta-vv/la)/2;tt=np.log((1+np.sqrt(1-4*AA*DD))/(2*AA))/la;close(AA*np.exp(la*tt)+DD*np.exp(-la*tt),1)
record(65,7,'保留衰减模的到达时间',{'sample_time':tt})
for eta0 in [.2,1,2,4]:
 kk=(15*eta0/16)**.25;close(1/16+kk**4/eta0,1);kk2=(15*eta0/17)**.25;close(2/17+kk2**4/eta0,1)
record(65,8,'桥管长度推广、半段狭窄并联回代',{'four_lengths_checked':True})
g=9.8;acc=2;mu=.5;R=500;tfour=np.sqrt(R*np.sqrt((mu*g)**2-acc**2))/acc;trear=np.sqrt(R*np.sqrt((mu*g)**2-(2*acc)**2))/acc;close(np.hypot(acc,(acc*tfour)**2/R),mu*g);assert tfour>trear
record(63,1,'四轮与后轴单独驱动的摩擦圆样例',{'four_wheel_seconds':tfour,'rear_seconds':trear})
mm,MM,J,rr,xprime,sdot,Xdot=s.symbols('m M J r xp sd Xd',positive=True);kin=(MM+mm)*Xdot**2/2+mm*Xdot*xprime*sdot+(mm+J/rr**2)*sdot**2/2;reduced=kin.subs(Xdot,-mm*xprime*sdot/(MM+mm));ident(reduced-(mm-mm**2*xprime**2/(MM+mm)+J/rr**2)*sdot**2/2);close(float((mm-mm**2*xprime**2/(MM+mm)+J/rr**2).subs({mm:1,MM:1,J:s.Rational(2,5),rr:1,xprime:1/s.sqrt(2)})),1.15)
record(63,2,'移动山体沿任意轨道的惯性消元',{'rolling_slope_effective_mass_over_m':1.15})
M=1.;e=.1;A=1.;Ap=A+2*e/M;Ep=e/(A*Ap);Eold=M*(A+1/A)/2+e;Enew=M*(Ap+1/Ap)/2+Ep;close(Eold,Enew);close((Ap*Ap-1)/(Ap*Ap+1),11/61)
record(63,7,'静止镜面单光子反射的数值能量回代',{'A_final':Ap,'reflected_energy_fraction':Ep/e})
Cp,U0=3.,2.;ya=4*U0;yb=-2*U0;yc=0;dq1=Cp*(ya-yb);dq2=Cp*(yb-yc);close(dq1+dq2,4*Cp*U0);close(U0*(abs(dq1)+abs(dq2)),8*Cp*U0**2)
record(63,8,'lambda=4两半周期净电荷与总耗能',{'net_charge':dq1+dq2,'dissipated_energy':U0*(abs(dq1)+abs(dq2))})
p=Path(__file__);result=dict(passed=True,script_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scope='新增变式中列出的关系、初值和极限，共11组',groups=out);assert len(out)==11
p.with_name('supplement_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('PASS',len(out),'supplement groups')
