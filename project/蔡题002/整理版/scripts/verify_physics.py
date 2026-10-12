"""独立符号、ODE及积分复核；各题先检查物理边界再比较闭式答案。"""
from pathlib import Path
import json, math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
reports={}
# 1 每半周逐段求ODE，并检查停止规则、能量收支及三角映射。
checks=[]
for u0 in [-8.4,-5,-4,-1.01,-1,0,.8,1,1.01,3,4,5,6,10.3]:
 u=u0; total=0.; k=0
 while abs(u)>1+1e-12:
  sign=math.copysign(1,u)
  sol=solve_ivp(lambda t,y:[y[1],-y[0]+sign],[0,np.pi],[u,0],rtol=2e-11,atol=2e-12,dense_output=True)
  old=u;u=float(sol.y[0,-1]);total+=quad(lambda t:abs(float(sol.sol(t)[1])),0,np.pi,epsabs=1e-10)[0];k+=1
  assert abs(u-(2*sign-old))<2e-9
 formula=2/np.pi*np.arcsin(np.sin(np.pi*u0/2))
 assert abs(u-formula)<2e-9 and abs(total-(u0*u0-u*u)/2)<2e-8
 checks.append(dict(u0=u0,u1=u,half_cycles=k,removed_energy=total))
reports['01']=dict(passed=True,checks=checks)
# 2 四种上升曲线，忽略自感极限的冲量均为K M I0^2/(2r)；有限自感先取阶跃给双倍。
vals=[]
for fun,dfun in [(lambda t:t,lambda t:1),(lambda t:t*t,lambda t:2*t),(lambda t:np.sin(np.pi*t/2),lambda t:np.pi/2*np.cos(np.pi*t/2)),(lambda t:3*t*t-2*t**3,lambda t:6*t-6*t*t)]:
 j=quad(lambda t:fun(t)*dfun(t),0,1,epsabs=1e-12)[0];assert abs(j-.5)<1e-12;vals.append(j)
# linear ramp, include post-ramp tail: normalized J=1/2+eta-eta^2(1-exp(-1/eta))
finite=[]
for eta in [.001,.01,.1,1,10]:
 # i'+i/eta=1/eta during ramp; after ramp i'+i/eta=0; F=I*i
 sol=solve_ivp(lambda t,y:[(1-y[0])/eta,t*y[0]],[0,1],[0,0],rtol=1e-10,atol=1e-12)
 j=sol.y[1,-1]+eta*sol.y[0,-1];pred=.5+eta-eta**2*(1-np.exp(-1/eta))
 assert abs(j-pred)<2e-9;finite.append(dict(eta=eta,j=j))
reports['02']=dict(passed=True,ramp_integrals=vals,finite_inductance=finite)
# 脉冲后局部运动感应阻尼的独立ODE、最高点事件及高度积分。
mt=1.;gt=9.8;vt=2.;bt=.3
def top(t,y):return y[1]
top.direction=-1;top.terminal=True
motion=solve_ivp(lambda t,y:[y[1],-gt-bt*y[1]/mt],[0,1],[0,vt],events=top,rtol=1e-11,atol=1e-12)
hpred=mt*vt/bt-mt*mt*gt/(bt*bt)*np.log1p(bt*vt/(mt*gt))
tpred=mt/bt*np.log1p(bt*vt/(mt*gt))
assert abs(motion.y[0,-1]-hpred)<1e-10 and abs(motion.t[-1]-tpred)<1e-10
reports['02']['motional_damping']=dict(height=hpred,time=tpred,ballistic_height=vt*vt/(2*gt),passed=True)
# 3 固定气体粒子数的电容导数与自由能广义力一致；符号线性刚度。
x,d,a,e,S,Q,p=sp.symbols('x d a e S Q p',positive=True)
y=d-x; cap=e*S*(1/x+a/x**2+1/y+a/y**2); U=Q/cap
fe=sp.diff(cap,x)*U**2/2; desired=e*S*U**2/2*((1+2*a/y)/y**2-(1+2*a/x)/x**2)
assert sp.simplify(fe-desired)==0
assert sp.simplify(-sp.diff(Q**2/(2*cap),x)-fe)==0
# at x=d/2, susceptibility chi=2a/d; electric destabilizing stiffness positive
ke=sp.simplify(sp.diff(fe,x).subs(x,d/2));kg=-4*p*S/d
samples=[]
for z in [.2,.3,.5,.7,.8]:
 fun=sp.lambdify(x,Q**2/(2*cap).subs({d:1,a:.15,e:1,S:1,Q:1}),'numpy') if False else None
 cs=lambda t:1/t+.15/t**2+1/(1-t)+.15/(1-t)**2
 h=1e-6;fd=-(1/(2*cs(z+h))-1/(2*cs(z-h)))/(2*h)
 expected=float(fe.subs({d:1,a:.15,e:1,S:1,Q:1,x:z}));assert abs(fd-expected)<1e-10
 samples.append(dict(x=z,force=expected))
reports['03']=dict(passed=True,electric_stiffness=str(ke),gas_stiffness=str(kg),samples=samples)
# 4 以原题给定公转周期校准G(M+m)，不混用另一组近似参数。
M=5.98e24;m=7.350e22;RE=6.37e6;rm=1.738e6;a0=3.84e8
CE=.4*M*RE**2;CM=.4*m*rm**2;mu=M*m/(M+m);n0=2*np.pi/(27.32*86400);omega=2*np.pi/86400
Gtot=n0*n0*a0**3;Lt=CE*omega+CM*n0+mu*a0*a0*n0
ls=lambda lam:(CE+CM)*n0*lam**(-1.5)+mu*a0*a0*n0*lam**.5-Lt
inner=brentq(ls,1e-4,.2);outer=brentq(ls,1,5);af=outer*a0;period=27.32*outer**1.5
solid=lambda distance:2*np.pi*(rm/distance)**2/(1+np.sqrt(1-(rm/distance)**2))
ratio=solid(af-RE)/solid(a0-RE);astar=np.sqrt(3*(CE+CM)/mu)
energy=lambda aa,om:.5*CE*om**2+.5*CM*(Gtot/aa**3)-.5*mu*Gtot/aa
energy_initial=energy(a0,omega);energy_final=energy(af,n0*outer**(-1.5))
assert inner*a0<astar<af and energy_final<energy_initial and abs(ls(outer)/Lt)<1e-12
reports['04']=dict(passed=True,inner_lambda=inner,outer_lambda=outer,final_period_days=period,solid_angle_ratio=ratio,far_ratio=outer**-2,critical_distance=astar,initial_L=Lt,initial_energy=energy_initial,final_energy=energy_final,CE=CE,CM=CM,mu=mu)
# 5 ODE积分阈值事件与解析半周期、R耗散积分。
U0=12.;UC=6.;C=1.;R=1.
up=solve_ivp(lambda t,y:[U0-y[0],(U0-y[0])**2],[0,np.log(3)],[-6,0],rtol=1e-11,atol=1e-12)
down=solve_ivp(lambda t,y:[-y[0],y[0]**2],[0,np.log(3)],[18,0],rtol=1e-11,atol=1e-12)
assert abs(up.y[0,-1]-UC)<1e-9 and abs(down.y[0,-1]-UC)<1e-9
assert abs(up.y[1,-1]+down.y[1,-1]-2*C*U0**2)<1e-8
reports['05']=dict(passed=True,half_period_over_RC=np.log(3),start_delay_over_RC=np.log(2),heat_cycle=up.y[1,-1]+down.y[1,-1])
# 6 Cartesian Lorentz ODE与三个积分；使用rho0=1m，事件探测径向速度再次归零。
a=.5;v0=1.;f=lambda z:1-np.exp(-2*z)-a*a*z*z
zmax=brentq(f,1,3);smax=np.exp(zmax)
def ode(t,y):
 xx,yy,zz,vx,vy,vz=y;r2=xx*xx+yy*yy
 # B=(-k*y/r2,k*x/r2,0), qk/m=a
 return [vx,vy,vz,-a*vz*xx/r2,-a*vz*yy/r2,a*(xx*vx+yy*vy)/r2]
def event(t,y):return (y[0]*y[3]+y[1]*y[4])/np.hypot(y[0],y[1])
event.direction=-1;event.terminal=True
sol=solve_ivp(ode,[0,100],[1,0,0,0,1,0],events=event,rtol=2e-11,atol=2e-12,max_step=.08)
Y=sol.y;r=np.hypot(Y[0],Y[1]);speed2=(Y[3:]**2).sum(axis=0);lz=Y[0]*Y[4]-Y[1]*Y[3]
assert abs(r[-1]-smax)<2e-8 and max(abs(speed2-1))<2e-9 and max(abs(lz-1))<2e-9 and max(abs(Y[5]-.5*np.log(r)))<2e-9
reports['06']=dict(passed=True,log_rmax=zmax,rmax_over_rho0=smax,turn_time=sol.t[-1],vz_max=.5*zmax,max_energy_error=float(max(abs(speed2-1))),max_L_error=float(max(abs(lz-1))))
# 7 按阀门分段压力直接积分，和闭式整周期功及气量比较。
checks=[]
for delta in [0,.02,.1,.2,.32]:
 pm=1-delta;pp=1+delta;vc=2*pm/pp;ve=pp/pm
 pc=lambda v:min(2*pm/v,pp);pe=lambda v:max(pp/v,pm)
 wc=quad(pc,1,2,points=[vc],epsabs=1e-12)[0]-quad(pe,1,2,points=[ve],epsabs=1e-12)[0]
 work=2*wc;pred=2*(1-3*delta)*np.log(pp/pm);N=2*pp*(vc-1)
 assert abs(work-pred)<1e-12 and abs(N-2*(1-3*delta))<1e-12
 checks.append(dict(delta=delta,work=work,moles_RT_over_P0V0=N,vc=vc,ve=ve))
dopt=brentq(lambda z:-3*np.log((1+z)/(1-z))+2*(1-3*z)/(1-z*z),.01,.32)
reports['07']=dict(passed=True,checks=checks,optimum_delta=dopt)
# 8 4力Lorentz变换、面电荷及E-B力的独立矩阵检查。
checks=[]
for beta in [0,.2,.6,.9]:
 gamma=1/np.sqrt(1-beta*beta);Ep=gamma;Bp=gamma*beta
 Fp=Ep-beta*Bp;area=1/gamma;pressure=.5*(Ep*Ep-Bp*Bp)
 # S' boost velocity -beta: (ct,x) -> gamma(ct+beta*x,x+beta*ct)
 Lambda=np.array([[gamma,gamma*beta,0,0],[gamma*beta,gamma,0,0],[0,0,1,0],[0,0,0,1]])
 K=Lambda@np.array([0,0,0,-1.]);u=Lambda@np.array([1.,0,0,0]);fz=K[3]/u[0]
 assert abs(Fp-1/gamma)<1e-14 and abs(pressure-.5)<1e-14 and abs(fz+Fp)<1e-14
 checks.append(dict(beta=beta,E_ratio=Ep,cB_over_E0=Bp,force_ratio=Fp,area_ratio=area,pressure_ratio=pressure/.5))
reports['08']=dict(passed=True,checks=checks)
(ROOT/'preview/verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(reports,ensure_ascii=False,indent=2))
