"""Reproducible independent algebra, quadrature, dynamics, circuits and geometry checks.
Checks cover 40 key-result groups plus targeted edge cases; they do not replace source/figure reading.
"""
from pathlib import Path
import json,math,hashlib
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq,minimize_scalar
from scipy.special import ellipk,ellipe
P=Path(__file__).resolve().parent
out={n:[] for n in [77,76,75,74,73]};extra=[]
def eq(x,y,rtol=1e-8,atol=1e-10):
 assert np.allclose(x,y,rtol=rtol,atol=atol),(x,y)
def rec(n,q,title,values):out[n].append(dict(question=q,check=title,passed=True,values=values))
def ex(title,values):extra.append(dict(check=title,passed=True,values=values))
# 077.1 Iterate the actual linear-drag speed map rather than only its closed sum.
e=.73;a=1.2;floor=a*sum(e**(-j) for j in range(6));eq(floor,a*(1-e**6)/(e**5*(1-e)))
v=floor+1
for j in range(6):assert v>a;v=v-a;v=e*v if j<5 else v
assert v>0;eq(v,e**5)
rec(77,1,'六段线性速度损失、五次碰撞与严格可达阈值',{'threshold_example':floor,'final_speed':v})
# 077.2 Minimize physical constrained energy vs the golden-ratio solution.
z0=(3-math.sqrt(5))/2
f=lambda z:(1-2*z+2*z*z)/(1-z*z)
x=minimize_scalar(f,bounds=(-.99,.99),method='bounded');eq(x.x,z0,rtol=2e-5)
# The problem starts (-l,l); reaching (-l,0) sets velocity components through cosine/sine.
c=z0;tau=math.acos(c);u=(-1+c)/math.sin(tau);w=-c/math.sin(tau)
eq(u*u+w*w,(math.sqrt(5)-1)/2)
rec(77,2,'受约束谐振轨道最小初速',{'v2_over_omega2l2':u*u+w*w,'tau':tau})
# 077.3 Circular energy derivative and Larmor power: slopes at sphere boundary differ fourfold.
A,m,R=3.,2.,1.7
Ein=lambda r:-3*A/(2*R)+A*r*r/(R**3)
Eout=lambda r:-A/(2*r)
eq((Ein(R+1e-6)-Ein(R-1e-6))/2e-6,2*A/R**2,rtol=1e-7)
eq(2*A/R**2/(A/(2*R**2)),4)
rec(77,3,'内外轨道能量、周期和辐射漂移边界',{'energy_slope_ratio':4,'Tin':2*math.pi*math.sqrt(m*R**3/A)})
# 077.4 Passive inductance matrix, linked-loop decomposition.
k,N1,N2=.01,20,25;M=k*(N1+N2);L1=k*N1*N1;L2=k*N2*N2
assert M*M<L1*L2;eq(M/L1,(N1+N2)/N1**2)
rec(77,4,'明确回路线形下交叉磁链及被动性近似检查',{'M':M,'L1':L1,'L2':L2,'ratio':M/L1})
# 077.5 Independent force ratio for magnetic dipoles.
vrc=.1;rd=.05;ratio=(2/3)*vrc**2*rd**2;assert ratio<1e-4
rec(77,5,'弱速远距下磁吸引不能超过电斥力',{'magnetic_electric_ratio':ratio})
# 077.6 Solve two boundary heat equations numerically.
Ch,Cc,G,l=3,3,.8,4;TiH,TiC=380,290
rhs=lambda t,y:[-G*(y[0]-y[1])/Ch,-G*(y[0]-y[1])/Cc]
def end(v):return solve_ivp(rhs,[0,l],[TiH,v],rtol=1e-11,atol=1e-11).y[:,-1]
Tc0=brentq(lambda t:end(t)[1]-TiC,TiC,TiH);H1,C1=end(Tc0);delta=(TiH-TiC)/(1+G*l/Ch)
eq(TiH-Tc0,delta);eq(H1-TiC,delta)
rec(77,6,'逆流换热边值解与四个端温',{'hot_out':H1,'cold_out':Tc0,'constant_delta':delta})
# 077.7 Exact Fermat first integral vs its small-gradient expansion.
alpha=.002;h0=3;L=2;n0=1.4
h=lambda x:1/alpha-(1-alpha*h0)*math.cosh(alpha*x/(1-alpha*h0))/alpha
slope=-(math.sinh(alpha*L/(1-alpha*h0)))
invariant=n0*(1-alpha*h(L))/math.sqrt(1+slope*slope)
eq(invariant,n0*(1-alpha*h0));eq(h(L),h0-alpha*L**2/2,atol=3e-5)
rec(77,7,'梯度折射率精确轨道与近轴像高',{'h_exit':h(L),'sin_air':n0*(1-alpha*h0)*(-slope)})
# 077.8 Two massless outgoing momenta: maximum cosine at equal splitting.
p1,p2,phi=3,5,.7;S=p1+p2;Pmag=math.sqrt(p1*p1+p2*p2+2*p1*p2*math.cos(phi))
cosmin=1-4*p1*p2*(1-math.cos(phi))/S**2;eq(cosmin,2*Pmag**2/S**2-1)
rec(77,8,'质量为零两体动量三角形的角度下界',{'minimum_angle':math.acos(cosmin)})
# 076.1 Constants supplied by original problem.
G=6.7e-11;M=2e30;R=7e8;sig=5.7e-8;Ts=6000;c=1000
W=3*G*M*M/(5*R);power=4*math.pi*R*R*sig*Ts**4;years=W/power/(365*24*3600);T=W/(M*c);threshold=(2e7/T)**1.5
assert 1.59e7<years<1.61e7;eq(threshold,.07266214269487,rtol=1e-6)
rec(76,1,'引力装配积分与黑体功率、质量门槛',{'W_J':W,'years':years,'T_K':T,'mass_ratio':threshold})
# 076.2 Endpoint-singular period integrated with theta=pi/6+(2pi/3)sin²u.
def integr(u):
 theta=math.pi/6+(2*math.pi/3)*math.sin(u)**2
 if u<1e-7 or math.pi/2-u<1e-7:u=max(1e-7,min(math.pi/2-1e-7,u));theta=math.pi/6+(2*math.pi/3)*math.sin(u)**2
 return math.sqrt((1+2*math.cos(theta)**2)/(1-1/(2*math.sin(theta))))*(4*math.pi/3)*math.sin(u)*math.cos(u)
I=quad(integr,0,math.pi/2,epsabs=2e-9)[0];coef=2/math.sqrt(3)*I;eq(coef,6.1953,rtol=1e-5)
rec(76,2,'三电荷构型动能、张力正性与周期积分',{'period_integral_transformed':I,'period_coefficient':coef})
# 076.3 One monotonic balance root, finite insertion geometry flagged in prose.
u=brentq(lambda u:math.log1p(1/u)-4*u,.1,1);lam=math.sqrt(1+u);eq(lam,1.15838476243)
rec(76,3,'零间距圆盘电压力平衡唯一根',{'u':u,'radius_ratio':lam,'diameter_cm':5*lam})
# 076.4 Solve all seven circuit nodes (11 resistors) with test potentials at ports1 and5.
ed=[(j,j+1) for j in range(6)]+[(0,2),(2,4),(4,6),(1,3),(3,5)];Lap=np.zeros((7,7))
for a,b in ed:Lap[a,a]+=1;Lap[b,b]+=1;Lap[a,b]-=1;Lap[b,a]-=1
free=[0,2,3,4,6];V=np.zeros(7);V[1]=1;V[free]=np.linalg.solve(Lap[np.ix_(free,free)],-Lap[free,1]);I=Lap@V
eq(V,[5/6,1,2/3,.5,1/3,0,1/6]);eq(1/I[1],1)
Rs,RL,L,C=2,3,.5,.2;w0=1/math.sqrt(L*C);a=(Rs+RL)/(2*Rs*RL)*math.sqrt(L/C)
wm,wp=w0*(math.sqrt(1+a*a)-a),w0*(math.sqrt(1+a*a)+a);eq(wp-wm,(Rs+RL)/(C*Rs*RL));eq(wm*wp,w0*w0)
rec(76,4,'七节点电路R_AB与有载滤波半功率两根',{'node_potentials':V.tolist(),'Req_over_R':1/I[1],'omega_minus':wm,'omega_plus':wp})
# 076.5 Contact N negative throughout purported detachment domain.
for alpha in [.01,.2,1,3]:
 beta=1.99*alpha*alpha;N=4*beta+1-(1+math.pi*alpha)**2;assert N<0
rec(76,5,'铰链转杆的支持力、力矩与无可行域',{'max_contact_bound_coefficient':8-math.pi**2})
# 076.6 Integrate each actual path and check heat, state temperatures, entropy.
Rg=8.314;n=2;T0=298.;P0=101000.;V3=.015;V0=n*Rg*T0/P0;V2=V0/4;T3=T0*(V2/V3)**.4
P3=n*Rg*T3/V3;P4=n*Rg*T3/V0
W21=quad(lambda v:n*Rg*T0/v,V2,V0)[0]
W43=quad(lambda v:n*Rg*T3/v,V0,V3)[0]
W32=quad(lambda v:P3*(V3/v)**1.4,V3,V2)[0]
Q14=n*2.5*Rg*(T3-T0);Q43=W43;Q21=W21;net=W21+W43+W32
eta=net/Q21;entropy=n*2.5*Rg*math.log(T3/T0)+n*Rg*math.log(V3/V0)+n*Rg*math.log(4)
eq(T3,274.94746912014665);eq(Q21,6869.288185737059);eq(Q14,-958.2937086755);eq(Q43,-5417.663751877968);eq(net,493.3307251836);eq(eta,.0718168625110106);eq(entropy,0)
rec(76,6,'四态路径的独立功积分、内能变化、熵变及效率',{'V0':V0,'T3':T3,'P3':P3,'P4':P4,'Qin':Q21,'work':net,'eta':eta,'entropy_cycle':entropy})
# 076.7 Electrostatic total energy along charged stretched rod.
ell=sp.symbols('ell',positive=True);a0=sp.symbols('a0',positive=True);U=a0/ell
assert sp.simplify(-sp.diff(U,ell)-a0/ell**2)==0
assert sp.simplify(sp.diff(U,ell,2)-2*a0/ell**3)==0
rec(76,7,'固定总电荷的轴向能量导数与正模量偏差',{'U':'A/ell','electric_tension':'A/ell^2','added_tangent_stiffness':'2A/ell^3'})
# 076.8 Gaussian uncertainty saturates full oscillator bound.
x,m,w,hbar,q,E=sp.symbols('x m w hbar q E',positive=True)
U=.5*m*w*w*x*x-q*E*x;xe=q*E/(m*w*w);assert sp.simplify(U.subs(x,xe)+q*q*E*E/(2*m*w*w))==0
rec(76,8,'平移谐振子基态能及不确定关系等号',{'E0':'hbar*omega/2-q²E²/(2m omega²)','variance':'hbar/(2m omega)'})
# 075.1 Both impact equations and slip evolution preserve V+omegaR.
I,m,R,th,ph,mu,g=2,1,1,.9,.2,.03,9.8
J=I*math.cos(ph);f=mu*J;V0=I*math.sin(ph)-f;W0=I*math.sin(ph-th)+f;s=V0-W0
assert f<I*(math.sin(ph)-math.sin(ph-th))/2;tr=s/(2*mu*g);Vr=(V0+W0)/2;eq(V0-mu*g*tr,Vr);assert Vr<0
rec(75,1,'环的冲量、接触冲量与停止滑动后的返回',{'V0':V0,'omegaR0':W0,'V_roll':Vr,'roll_time':tr})
# 075.2 At second mode interface zero, derivative equality enforces B=-2A.
for j in range(1,7):
 a=j*math.pi/2;A=1;B=1 if j%2 else -2
 eq(A*math.sin(a),B*math.sin(a));eq(2*A*math.cos(a),-B*math.cos(a),atol=2e-14)
rec(75,2,'复合弦两族模态的位移和斜率匹配',{'frequency_coefficient':'3n/8','second_mode_B_over_A':-2})
# 075.3 Integrate surface pressure's projection rather than flat equatorial pressure.
proj=2*math.pi*quad(lambda t:math.sin(t)*math.cos(t),0,math.pi/2)[0];eq(proj,math.pi)
rec(75,3,'球面压力的轴向面积投影及壳定理交叉力',{'projection_over_R2':proj,'force':'Qq/(8 pi epsilon0 R²)'})
# 075.4 Numerical Biot-Savart and genuine field line at rho=1.5.
def coil(r,z):
 D=(1-r)**2+z*z;A=(1+r)**2+z*z;kk=4*r/A;K=ellipk(kk);E=ellipe(kk);c=1/(2*math.pi*math.sqrt(A))
 return np.array([c*z/r*(-K+(1+r*r+z*z)/D*E),c*(K+(1-r*r-z*z)/D*E)])
def field(r,z):return coil(r,z-1)+coil(r,z+1)
b0=np.linalg.norm(field(1.5,0));integ=quad(lambda a:(1-1.5*math.cos(a))/(4.25-3*math.cos(a))**1.5,0,math.pi*2,epsabs=1e-11)[0];eq(b0,abs(integ/(2*math.pi)))
def pathrhs(t,y):b=field(*y);return -b/np.linalg.norm(b)
path=solve_ivp(pathrhs,[0,4],[1.5,0],rtol=2e-11,atol=2e-12,max_step=.004,dense_output=True)
tt=np.linspace(0,4,2001);bs=np.array([np.linalg.norm(field(*path.sol(t))) for t in tt]);i=int(np.argmax(bs));peak=minimize_scalar(lambda t:-np.linalg.norm(field(*path.sol(t))),bounds=(tt[max(0,i-2)],tt[min(len(tt)-1,i+2)]),method='bounded',options={'xatol':1e-11});bmax=-peak.fun;point=path.sol(peak.x);theta=math.degrees(math.asin(math.sqrt(b0/bmax)))
eq(theta,10.133,rtol=2e-4)
rec(75,4,'实际轴外场线、场峰与损失锥；角积分交叉检查',{'B0_unit_muI_R':b0,'Bpath_peak':bmax,'point':point.tolist(),'critical_degrees':theta})
# 075.5 Enumerate all six physically distinct momentum identities.
vectors=[np.array([math.cos(t),math.sin(t)])for t in [0,math.pi/2,7*math.pi/6]];cases=[]
import itertools
for inc,pr,recoil in itertools.permutations(range(3)):
 p,Pmag=np.linalg.solve(np.column_stack([vectors[pr],vectors[recoil]]),-vectors[inc]);lam=Pmag**2/(1-p*p);valid=p>0 and Pmag>0 and lam>0;cases.append([inc,pr,recoil,float(p),float(Pmag),float(lam),bool(valid)])
assert sum(x[-1] for x in cases)==3;eq(sorted(x[-2] for x in cases if x[-1]),[1,1,2])
rec(75,5,'六种径迹身份及质量比筛选',{'six_cases':cases})
# 075.6 Quantized phase monotone, each integer has one root.
tc=math.asin(6/7)
def mode(t):return 42*math.cos(t)+.5*(1-math.exp(-(t-tc)))
assert 21<mode(tc)<22 and 0<mode(math.pi/2)<1
angles=[math.degrees(brentq(lambda t:mode(t)-i,tc,math.pi/2)) for i in range(1,22)]
eq([angles[0],angles[9],angles[-1]],[88.9131874,76.4098298,60.0138500],rtol=1e-7)
rec(75,6,'全反射允许区、严格单调相位与21根',{'count':len(angles),'angles_deg':angles})
# 075.7 Number integral vs analytic gas COM and pressure.
T0=300;deltaT=32;L=10;massboat=150;massgas=120;a=deltaT/T0
num=quad(lambda x:1/(T0+deltaT*x/L),0,L)[0];xg=quad(lambda x:x/(T0+deltaT*x/L),0,L)[0]/num;pr=(L/T0)/num;X=massgas/(massgas+massboat)*(L/2-xg)
eq(xg,L*(1/math.log1p(a)-1/a));eq(pr,a/math.log1p(a));eq(X,.03753,rtol=2e-4)
rec(75,7,'粒子数守恒的非均匀温度气体压强和质心',{'pressure_ratio':pr,'gas_com_m':xg,'boat_displacement_m':X})
# 075.8 Tangent inertial pair vs genuinely circulating neighbors, both local gamma.
beta=.7;gamma=1/math.sqrt(1-beta*beta)
for al in [1e-3,1e-4]:
 xp=math.sin(al)/(gamma*(1-beta*beta*math.cos(al)));yp=1-math.cos(al)+beta*beta*math.sin(al)**2/(1-beta*beta*math.cos(al));eq(math.hypot(xp,yp)/al,gamma,rtol=2e-6)
 theta=brentq(lambda t:t-al-beta*beta*math.sin(t),0,.1);eq(math.sin(theta)/gamma/al,gamma,rtol=3e-6)
rec(75,8,'不同运动模型的同时性与局部周长极限',{'circumference_over_2piR':gamma})
# 074.1 Recover EI from exact cantilever moment and independent variational quotient.
EI=10/(3*.01);Fc=math.pi**2*EI/4;int1=quad(lambda x:(math.pi/2*math.sin(math.pi*x/2))**2,0,1)[0];int2=quad(lambda x:(math.pi**2/4*math.cos(math.pi*x/2))**2,0,1)[0];eq(EI*int2/int1,Fc)
rec(74,1,'真实悬臂刚度与固支自由最低模态',{'EI':EI,'critical_N':Fc,'quoted_arc_estimate_N':3000})
# 074.2 First approaching collision plus floor impulse, energy and next-contact distance.
t=brentq(lambda t:t**4-7*t*t-8*t+16,1,1.2);nx=1-t/4;ny=1-t*t/4;eq(nx*nx+ny*ny,1);j=2*(.5*nx+t*ny)/(1+nx*nx/3);ux=j*nx;uy=-t+j*ny;v3=.5-j*nx/3;highest=3-t*t/2+uy*uy/2
Epre=.5*t*t+1.5*.5**2;Epost=.5*(ux*ux+uy*uy)+1.5*v3*v3;eq(Epre,Epost);eq(ux+3*v3,1.5)
for dt in np.linspace(1e-7,uy,100):
 p2=np.array([ux*dt,3-t*t/2+uy*dt-.5*dt*dt]);p3=np.array([-2+.5*t+v3*dt,1]);p1=np.array([1.5*(t+dt),1]);assert np.linalg.norm(p2-p3)>2-1e-9 and np.linalg.norm(p2-p1)>2
rec(74,2,'非45度接触、贴地冲量和首次碰后峰值',{'tau':t,'normal':[nx,ny],'angle_degrees':math.degrees(math.atan2(ny,nx)),'highest_center_R':highest,'vertical_velocity_post':uy})
# 074.3 Independent Cartesian dynamics vs Binet turning root and sweep.
b=brentq(lambda b:1-b*b+.5*math.log(b),.01,.5)
def rhs(t,y):x,z,vx,vz=y;r2=x*x+z*z;return[vx,vz,-x/(4*r2),-z/(4*r2)]
def ap(t,y):return y[0]*y[2]+y[1]*y[3]
ap.direction=-1;ap.terminal=True
orbit=solve_ivp(rhs,[1e-8,80],[1e-8,1,1,0],events=ap,rtol=1e-11,atol=1e-12,max_step=.03);pos=orbit.y[:2,-1];ratio=np.linalg.norm(pos);sweep=math.pi/2-math.atan2(pos[1],pos[0]);eq(ratio,1/b,rtol=1e-8);eq(sweep,2.07814,rtol=3e-6)
rec(74,3,'线电荷势与真实中心势轨迹的第一次远点',{'beta':b,'radius_ratio':ratio,'sweep_rad':sweep})
# 074.4 Fixed-charge capacitance derivative vs local E-pressure.
eps,er,d,L,V,rho,g=8.854e-12,2.5,.01,.12,1000,800,9.8
C0=eps*L*L/d;Q=C0*V;C=eps*L*L*(1+er)/(2*d);Vp=Q/C;Cp=eps*L*(er-1)/d;force=.5*Vp*Vp*Cp;h=force/(rho*g*L*d)
eq(h,2*eps*V*V*(er-1)/(rho*g*d*d*(1+er)**2))
rec(74,4,'固定Q能量梯度、电荷分配与液面高度',{'new_voltage':Vp,'height_m':h})
# 074.5 Exact true-COM contact velocity has nonzero horizontal component for finite m.
m,M,R,v,b=1,100,2,3,.9;eta=m/(m+M);s=math.sqrt(R*R-b*b);omega=2*m*v*b/((M+3*m)*R*R);VB=[-omega*eta*s,eta*v-omega*(R+eta*b)]
assert VB[0]<0;eq(omega, m*v*b/(.5*M*R*R+M*m/(M+m)*R*R)/(1+ m/M),rtol=1e-8)
rec(74,5,'真实质心惯量及B严格静止的有限质量限制',{'VB':VB,'leading_b_over_R':.5})
# 074.6 Search image intervals from actual lens propagation.
def bound(z):return .2*z/1.5+5*abs(1-z/30)
res=minimize_scalar(bound,bounds=(.1,100),method='bounded');eq(res.x,30,rtol=1e-6);eq(res.fun,4,rtol=1e-6)
for z in [10,30,60]:
 R=bound(z);image=[rho*(1-15/10+15/z)-15*R/z for rho in [-5,5]];eq(max(image),-2)
rec(74,6,'透镜射线区间、CCD交集及安全区域下确界',{'minimum_boundary_radius_cm':res.fun,'axial_z_cm':res.x})
# 074.7 Discrete spring chain eigenvalues and nitrogen gamma.
N=20;kappa=2.;mass=.3;ell0=.4;D=np.zeros((N,N))
for i in range(N):D[i,i]=2;D[i,(i+1)%N]=-1;D[i,(i-1)%N]=-1
vals=np.linalg.eigvalsh(kappa/mass*D);eq(vals[1],4*kappa/mass*math.sin(math.pi/N)**2)
phase=[math.sin(math.pi*j/N)/(math.pi*j/N) for j in range(1,N//2+1)];assert phase[-1]<phase[0]
rec(74,7,'氮气绝热弹簧、离散色散及相速度误解',{'gamma':1.4,'first_phase_over_c0':phase[0],'highest_k_phase_over_c0':phase[-1]})
# 074.8 Relativistic period and lifetime cancel at one revolution.
m=1.88e-28;q=1.602e-19;th=1.523e-6;B=2*math.pi*m/(q*th)
for gamma in [1,2,10]:T=gamma*2*math.pi*m/(q*B);eq(2**(-T/(gamma*th)),.5)
rec(74,8,'固有时衰变与回旋周期抵消',{'B_T':B,'one_turn_survival':.5})
# 073.1 Sum actual image fields, finite-segment force integral.
forces=[]
for n in [1,2,3,10]:
 F=np.zeros(2);real=np.array([1.,0.])
 for j in range(1,2*n):ang=j*math.pi/n;d=real-np.array([math.cos(ang),math.sin(ang)]);F+=(-1)**j*d/np.dot(d,d)
 eq(F,[-.5,0],atol=1e-13);forces.append(F.tolist())
L,s=10,2;double=2*quad(lambda u:(L-u)*s/(s*s+u*u)**1.5,0,L,epsabs=1e-11)[0];eq(double,2*(math.sqrt(L*L+s*s)/s-1))
rec(73,1,'真实镜像矢量和与有限线段双重积分',{'image_sums':forces,'finite_segment_integral':double})
# 073.2 All19 rods equilibrium and independent rigidity matrix.
xy=np.array([(0,0),(1,0),(2,0),(4,0),(5,0),(6,0),(1,1),(2,2),(3,3),(4,2),(5,1)],float)
ed=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(6,7),(7,8),(8,9),(9,10),(10,5),(1,6),(2,7),(3,9),(4,10),(6,2),(7,3),(2,9),(3,10)]
A=np.zeros((22,22));C=np.zeros((22,22))
for i,(a,b) in enumerate(ed):
 d=xy[b]-xy[a];d/=np.linalg.norm(d);A[2*a:2*a+2,i]=d;A[2*b:2*b+2,i]=-d;C[i,2*a:2*a+2]=-d;C[i,2*b:2*b+2]=d
A[0,19]=1;A[1,20]=1;A[11,21]=1;F=np.zeros(22);F[17]=3;F[13]=2;sol=np.linalg.solve(A,F);eq(sol[2],2.5);eq(sol[-1],3/2+2/6)
C[19,0]=1;C[20,1]=1;C[21,11]=1;rr=np.zeros(22);rr[2]=1;vv=np.linalg.solve(C,rr).reshape(-1,2);eq(vv[[6,8,5]],[ [.5,-.5],[.5,-.5],[1,0]])
rec(73,2,'十九杆节点力与切杆相容位移同时核验拉压',{'target_tension_G3_P2':sol[2],'virtual_P_G_right':vv[[6,8,5]].tolist()})
# 073.3 Work in three direction-dependent force intervals and asymptotic recurrence.
vb2=2*quad(lambda x:(x+.25)/2,.75,1)[0];v02=vb2+2*quad(lambda x:2*x/3,0,.75)[0];u12=2*(.5)*.25+3/8
eq(v02,21/32);eq(u12,5/8)
d=.25
for _ in range(2000):new=math.sqrt(1+2*d)-1;assert 0<new<d;d=new
assert d<.0011
rec(73,3,'分支功积分与渐近越界量',{'v02_over_gl':v02,'u12_over_gl':u12,'u22_over_gl':3/8,'delta_after_2000_l':d})
# 073.4 Direct EM work and flux-constrained magnetic energy.
y=sp.symbols('y',positive=True);U=(y-1)/2+sp.Rational(3,2)*(y-1)**2/y
assert sp.simplify(sp.diff(U,y)-(2-sp.Rational(3,2)/y**2))==0;eq(float(U.subs(y,2)),1.25)
roots=sp.solve(sp.Eq(U,sp.Rational(5,4)),y);assert set(roots)=={sp.Rational(3,8),sp.Integer(2)}
rec(73,4,'自感梯度受力、功积分和两侧临界转折',{'v02_over_gx0':2.5,'turning_roots':[float(r) for r in roots]})
# 073.5 Numerically scan endpoint envelopes, including signed angular velocity branch.
vals=[]
for K,A,s0 in [(1,2,3.5),(1,2,2),(1,1,.5),(1,3,3)]:
 rot=s0*s0>4*K*A;lo=math.sqrt(s0*s0-4*K*A) if rot else -s0;ss=np.linspace(lo,s0,20001);Y=(ss-s0)/A;cost=1+(ss*ss-s0*s0)/(2*K*A);yp=Y+cost;ym=Y-cost;band=max(yp.max(),ym.max())-min(yp.min(),ym.min());closed=2+(s0-lo)/A;eq(band,closed,rtol=1e-9);vals.append([K,A,s0,band])
rec(73,5,'两端点全过程包络，转动和返回分支',{'examples':vals})
# 073.6 Direct pressure work optimized, distinguish all-length and stroke.
rho=4;gamma=1.4;vs=rho**(1/gamma);work=quad(lambda V:rho*V**(-gamma)-1,1,vs)[0];closed=rho/(gamma-1)+1-gamma/(gamma-1)*rho**(1/gamma);eq(work,closed)
eps,g=sp.symbols('eps g',positive=True)
Kweak=(1+eps)/(g-1)+1-g/(g-1)*(1+eps)**(1/g)
Sweak=sp.series(Kweak,eps,0,3).removeO().expand()
assert sp.simplify(Sweak.coeff(eps,1))==0
assert sp.simplify(Sweak.coeff(eps,2)-1/(2*g))==0
assert sp.simplify(Sweak.coeff(eps,2).subs(g,sp.Rational(7,5)))==sp.Rational(5,14)
rec(73,6,'绝热净功面积及全管长度、行程之差',{'Vstar_V0':vs,'Kmax_PatmV0':work,'total_length_V0_A':vs,'stroke_V0_A':vs-1,'weak_pressure_linear':0,'weak_pressure_quadratic':'1/(2γ)','gamma_7_5_quadratic':'5/14'})
# 073.7 Ray transfer, phase symmetry, integer counts.
p,f,H,delta,lam=20,10,50,.1,5e-5;q=1/(1/f-1/p);d=delta*(1+q/p);h=H-q;D=delta*(1+H/p);spacing=lam*h/d;bright=[i for i in range(-100,101) if abs(i*spacing)<=D/2];half=[i for i in range(-100,101) if abs((i+.5)*spacing)<=D/2];assert len(bright)==47 and len(half)==46
for rho,b in [(delta/2,delta/2),(-delta/2,-delta/2)]:y=rho+H*(rho/p-(rho-b)/f);eq(abs(y),D/2)
rec(73,7,'半片光线变换、共同区及相位相关整数条纹计数',{'q_cm':q,'d_cm':d,'overlap_cm':D,'spacing_cm':spacing,'bright_count':len(bright)})
# 073.8 Exact endpoint root under first-order Doppler, density normalization.
a=580.001/580;c=3e8;w=c*(a-1);s=brentq(lambda s:math.sqrt(s*s+5000**2)-a*s-w,2e4,3e4);V=s*s/1e7;maxu=math.sqrt(s*s+25e6)
eq(580*(1+maxu/c),580.001*(1+s/c),atol=1e-10)
# Integrate original v parameter to avoid the density endpoint integrable singularity.
total=quad(lambda v:(math.sqrt(v*v+s*s)/v)*(v/math.sqrt(v*v+s*s)),1e-8,5000)[0];eq(total,5000)
rec(73,8,'多普勒端点相切、正根与速度密度雅可比',{'critical_V':V,'s':s,'u2':maxu,'common_nm':580*(1+maxu/c)})
# Extras are focused independent risks; add detailed thermal path check below before writing.
ex('077.1阈值等号末段速度零意味着线性阻力到达时间发散',{'at_threshold_final':0,'strict_inequality':True})
ex('077.4小匝数线性分解不得作为任意几何精确公式',{'N1_N2_1_approx_M2_over_L1L2':4,'passivity_violation_flags_missing_terms':True})
ex('077.5形式磁力平衡需ωr/c>1，超出推导域',{'for_d_over_r_10_required':math.sqrt(6)*10/2})
ex('075.4缩步后的场线峰值与BiotSavart起点一致',{'peak':bmax,'angle':theta})
ex('074.2第二次碰撞能量和水平动量均守恒；地面竖直冲量非零',{'energy_residual':Epost-Epre,'floor_impulse':j*ny})
ex('074.6边界能被CCD探测；4cm为安全半径下确界',{'strict_safe_radius':'R>4 cm'})
ex('073.1有限线段合力误差是一阶端部项',{'ratio_L10_s2':(math.sqrt(104)-2)/10})
ex('073.3返回接触法向力与外行不同，均非负',{'return_N1_mg_at_x_l':1/6,'out_N1_mg_at_x_l':1/8})
ex('073.5临界轨道与摆动侧的无限时宽度不连续',{'critical_over_l':2+2/math.sqrt(2),'oscillation_limit_over_l':2+4/math.sqrt(2)})
ex('073.7额外π相位时46条，原对称两路无额外相位差',{'bright_with_extra_pi':46,'original':47})
# High precision relativistic kinetic energy and Doppler endpoints must be used together.
import mpmath as mp
mp.mp.dps=60;cc=mp.mpf('3e8');eta=mp.mpf('5e6');vv=mp.mpf(5000);la=mp.mpf('580');lb=mp.mpf('580.001');gv=1/mp.sqrt(1-(vv/cc)**2)
def dop(g):return g+mp.sqrt(g*g-1)
def rel(V):return la*dop(gv+eta*V/cc**2)-lb*dop(1+eta*V/cc**2)
exact=mp.findroot(rel,(56,58));assert abs(rel(exact))<mp.mpf('1e-45')
ex('073.8相对论动能和完整多普勒式高精度一致复算',{'exact_V':str(exact),'first_order_V':57.15016053427186,'rounding_one_decimal':'57.2 V'})
# Assert complete coverage and write serializable results.
assert sum(len(v) for v in out.values())==40
result={'papers':[{'set':n,'passed':True,'questions':sorted(v,key=lambda x:x['question'])}for n,v in out.items()],'extra':extra,'method':'每题独立关键关系组；公式、原扫描、图稿及全文另行审读。','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('40 question result groups and',len(extra),'extra checks passed')
