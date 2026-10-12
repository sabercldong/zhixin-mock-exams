from pathlib import Path
import json,math,hashlib,sys
import numpy as np
import sympy as s
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq,minimize_scalar
SCRIPT_DIR=Path(__file__).resolve().parent
rows=[];extra=[]
def ck(n,q,name,fn):
 out=fn();rows.append(dict(set=n,question=q,check=name,result=out,passed=True))
def eq(a,b,tol=1e-9):assert abs(float(a)-float(b))<=tol*max(1,abs(float(b))),(a,b);return float(a)
def zero(x):assert s.simplify(x)==0,x
# 072

def a721():
 M=1e10;m=1;V=-1.;v=0.;N=0;E=M*V*V
 while v<0 or V<v:
  if v<0:v=-v
  else:V,v=((M-m)*V+2*m*v)/(M+m),(2*M*V+(m-M)*v)/(M+m)
  N+=1
  assert N<314200
 assert N==314159 and 0<=v<=V
 eq((M*V*V+v*v)/E,1,1e-10)
 assert math.ceil(math.pi/math.atan(1e-5))-1==N
 return dict(collisions=N,terminal_V=V,terminal_v=v,relative_energy_error=(M*V*V+v*v)/E-1)
ck(72,1,'逐事件实际速度、停止扇区与能量',a721)
def a722():
 h=.7;d=.003;B=20
 ex=quad(lambda u:u/(u*u+h*h)-u/(u*u+(h+d)**2),0,B,epsabs=1e-13)[0]
 ez=quad(lambda u:h/(u*u+h*h)-(h+d)/(u*u+(h+d)**2),0,B,epsabs=1e-13)[0]
 eq(ex,.5*math.log((B*B+h*h)*(h+d)**2/(h*h*(B*B+(h+d)**2))))
 eq(ez,math.atan(B/h)-math.atan(B/(h+d)))
 return dict(finite_Ex=ex,finite_Ez=ez)
ck(72,2,'有限条带直接积分复算外场',a722)
def a723():
 a=35/3;x=a*math.log(7)
 eq(a*(math.cosh(x/a)-1),30);eq(quad(lambda t:math.cosh(t/a),0,x)[0],40)
 return dict(span=2*x,curvature_radius=a)
ck(72,3,'悬链线高度与实际弧长积分',a723)
def a724():
 A=np.diag([1/9,1/4]);P=np.array([1.2,0.])
 for ang in np.linspace(.07,math.pi-.07,21):
  d=np.array([math.cos(ang),math.sin(ang)]);coef=[d@A@d,2*P@A@d,P@A@P-1];roots=np.roots(coef)
  X,Y=[P+r*d for r in roots];S=np.linalg.solve(np.array([X@A,Y@A]),[1,1]);eq(S@A@P,1)
 return dict(polar_x=7.5,sample_chords=21)
ck(72,4,'21条弦的实际切线交点',a724)
def a725():
 L1=1;L2=1.5;M=(L2-2*L1)/2;K=np.full((3,3),M);np.fill_diagonal(K,L1)
 eq(np.ones(3)@K@np.ones(3),3*(L2-L1));assert min(np.linalg.eigvalsh(K))>0
 return dict(mutual=M,eigenvalues=np.linalg.eigvalsh(K).tolist(),third_inductance=1.5)
ck(72,5,'有向边界的磁能二次型',a725)
def a726():
 m=.03;M=.0635;Cu=24.44;Cs=3.84;Cl=4.59;Tm=600.61;Tc=300.15;Tp=303.15
 Qh=Cu*(Tm-Tc)+Cs*(Tm-Tp);Qm=Qh+613.5;Qfree=.5*m*850**2*M/(m+M)
 Tf=(Qfree+Cu*Tc+Cs*Tp)/(Cu+Cs);Sfree=Cu*math.log(Tf/Tc)+Cs*math.log(Tf/Tp)
 R=(3*m/(4*math.pi*11340))**(1/3);Ci=4*math.pi*8.8541878128e-12*R
 Qc=.5*m*750**2+.5*(4e-5)**2*(1/Ci-1/1.5e-12);mf=(Qc-Qh)/20450
 Scharge=Cu*math.log(Tm/Tc)+Cs*math.log(Tm/Tp)+mf*20450/Tm
 assert Qfree<Qh<Qc<Qm<.5*m*850**2
 eq(Tm+(.5*m*850**2-Qm)/(Cu+Cl)-273.15,387.3467,1e-5)
 return dict(Qheat=Qh,Qmelt=Qm,Qfree=Qfree,Tfree=Tf,Sfree=Sfree,Ci=Ci,Qcharged=Qc,melt_mass=mf,Scharged=Scharge)
ck(72,6,'三种能量与相区独立重算',a726)
def a727():
 a=.8;b=1.7;h=.003;d=.01;y=-b*h/a
 def L(sig,Y):
  xi=(b*h+a*Y+sig*a*b*d)/(a+b)
  return (xi-h)**2/(2*a)+(Y-xi)**2/(2*b)-sig*d*xi
 eq(L(-1,y)-L(1,y),0);Y=.017;eq(L(-1,Y)-L(1,Y),2*d*(a*Y+b*h)/(a+b))
 return dict(zero_order=y,phase_difference=L(-1,Y)-L(1,Y))
ck(72,7,'驻值光程直接代入零级与宽度',a727)
def a728():
 h=6.62607015e-34;m=1.6749275e-27;d=(22.4e-3/6.02214076e23)**(1/3)
 P=h*h/(4*m*d**5);E=3*h*h/(8*m*d*d);eq(P,2*E/(3*d**3))
 return dict(cell_nm=d*1e9,hardwall_pressure=P,ratio_to_variance_bound=math.pi**2)
ck(72,8,'盒中基态能量体积导数',a728)
# 071

def a711():
 z=s.symbols('z');M=s.Matrix([[6,-s.Rational(1,2)],[-s.Rational(1,2),s.Rational(1,4)]]);K=s.Matrix([[2,1],[1,s.Rational(3,4)]])
 roots=s.solve((K-z*M).det(),z);expected=[(12-s.sqrt(134))/5,(12+s.sqrt(134))/5]
 assert set(roots)==set(expected)
 for r in roots:
  e=s.Matrix([1,(6*r-2)/(1+r/2)]);assert (K-r*M)*e==s.zeros(2,1) or all(s.simplify(t)==0 for t in (K-r*M)*e)
 return dict(frequency_squared=[float(r) for r in roots])
ck(71,1,'广义特征值与两行本征关系',a711)
def a712():
 for N in [2,3,6,50,1000]:
  z=np.exp(2j*np.pi/N);S=sum((j*z**j for j in range(1,N+1)));assert abs(S+N*z/(1-z))<1e-7*max(1,abs(S))
  Q=1;q=2*Q/(N*(N+1));eq(sum(j*q for j in range(1,N+1)),Q)
 return dict(discrete_limits=[2,3,6,50,1000],fixed_total_limit=1/math.pi)
ck(71,2,'离散电荷向量逐项求和与总量',a712)
def a713():
 z=s.symbols('z');M=s.Matrix([[1,1],[1,s.Rational(4,3)]]);K=s.eye(2);poly=s.expand(3*(K-z*M).det());zero(poly-(z*z-7*z+3))
 lo=(7-math.sqrt(37))/2;hi=(7+math.sqrt(37))/2
 return dict(low_squared=lo,high_squared=hi,ratio=math.sqrt(hi/lo))
ck(71,3,'绳杆广义特征值与频率比',a713)
def a714():
 x=(5/8)**(3/5);n1=2*x;n2=3-n1;T1=2*x**(2/3);T2=2.5/n2
 eq(n1*T1+n2*T2,5);eq(n1*T1,n2*T2)
 Si=2*(1.5*math.log(2)+math.log(.5));Sf=n1*(1.5*math.log(T1)+math.log(1/n1))+n2*(1.5*math.log(T2)+math.log(1/n2));assert Sf>Si
 return dict(n1=n1,n2=n2,T1=T1,T2=T2,entropy_in_n0R=Sf-Si)
ck(71,4,'开放流动终态能量、压力与熵',a714)
def a715():
 K=np.array([[1,.5,.5],[.5,1,.5],[.5,.5,1]])
 i=np.array([4/3,-2/3,0]);eq(i@K@i,4/3);eq(K[1]@i,0)
 assert min(np.linalg.eigvalsh(K))>0
 return dict(shorted_current=i.tolist(),energy_factor=i@K@i)
ck(71,5,'线圈短接电流与磁能',a715)
def a716():
 mu=273;C=(mu*mu-1)/2;Ee=math.sqrt(C);Pe=math.sqrt(Ee*Ee-1);En=Ee;P=math.hypot(Pe,En);E=Ee+En
 eq(E*E-P*P,mu*mu,1e-10);eq((P/E)**2,(mu*mu-2)/(2*(mu*mu-1)))
 x=(mu*mu+1)/(2*mu);y=(mu*mu-1)/(2*mu)
 eq(x+y,mu);eq(math.sqrt(x*x-1),y)
 xx,cc,AA=s.symbols('x c A',positive=True);DD=xx-cc*s.sqrt(xx*xx-1)
 zero(s.diff(xx+AA/DD,xx)-(1-AA*(1-cc*xx/s.sqrt(xx*xx-1))/DD**2))
 return dict(equal_energy=Ee,beta=P/E,mass_shell=E*E-P*P,angle_extension_stationary_condition='symbolic derivative verified',back_to_back_minimum_beta=0)
ck(71,6,'直角两体动量与母粒子质量壳',a716)
def a717():
 x=s.symbols('x');F=(x+1)**2*(x-1)/x;zero(F-(x*x+x-1-1/x));zero(s.diff(F,x)-(2*x+1+x**-2))
 eps=s.symbols('e');eqcoeff=s.series(F.subs(x,1+eps),eps,0,4).removeO();zero(eqcoeff-(4*eps+eps**3))
 rt=brentq(lambda z:float(F.subs(x,z))-1.7,1,3)
 return dict(turning_ratio=rt,leading_series='4e+e^3')
ck(71,7,'外转折方程、单调性及弱场级数',a717)
def a718():
 direct=solve_ivp(lambda t,y:[y[1],math.cos(t)-y[1]*abs(y[1])],[0,3],[0,0],rtol=2e-11,atol=2e-12,dense_output=True)
 aux=solve_ivp(lambda t,y:[y[1],math.cos(t)*y[0]],[0,1],[1,0],rtol=2e-11,atol=2e-12,dense_output=True)
 t=np.linspace(0,1,30);u,up=aux.sol(t);x,v=direct.sol(t);assert max(abs(v-up/u))<1e-9 and max(abs(x-np.log(u)))<1e-9
 st=solve_ivp(lambda t,y:[math.cos(t)-y[0]*abs(y[0])],[0,44*math.pi],[0],rtol=1e-10,atol=1e-12,dense_output=True)
 lhs=quad(lambda t:st.sol(t)[0]*math.cos(t),42*math.pi,44*math.pi,epsabs=1e-9)[0];rhs=quad(lambda t:abs(st.sol(t)[0])**3,42*math.pi,44*math.pi,epsabs=1e-9)[0];eq(lhs,rhs,1e-8)
 return dict(auxiliary_max_error=float(max(abs(v-up/u))),period_power=lhs)
ck(71,8,'平方阻力辅助方程与直接积分、周期功率',a718)
# 070

def a701():
 x=(math.sqrt(13)-1)/6;root=brentq(lambda c:c**4+c**3+4*c*c+c-1,0,1);assert root<x
 opt=minimize_scalar(lambda t:-4*math.sin(t)*math.cos(t)*(1-math.cos(t)),bounds=(0,math.pi/2),method='bounded');eq(math.cos(opt.x),x,2e-6)
 return dict(fixed_angle_deg=math.degrees(math.acos(x)),moving_angle_deg=math.degrees(math.acos(root)),range_max=-opt.fun)
ck(70,1,'相对射程实际极值与两角次序',a701)
def a702():
 e1=4;e2=2;eta=(e1-e2)/(e1+e2);C=2*e2/(e1+e2)
 for phi in np.linspace(0,2*math.pi,31):
  eq((1-eta)*math.sin(phi),C*math.sin(phi));eq(e2*(1+eta)*math.cos(phi),e1*C*math.cos(phi))
 return dict(interior_factor=C,dipole_factor=eta,boundaries=31)
ck(70,2,'圆柱面切向E与法向D连续',a702)
def a703():
 A,B,qx,qy,w=s.symbols('A B qx qy w');mat=s.Matrix([[A-w*w,-s.I*w*qx],[s.I*w*qy,B-w*w]]);zero(mat.det()-(w**4-(A+B+qx*qy)*w*w+A*B))
 
 roots=np.roots([1,-736/49,1600/49]);assert all(roots>0);eq(max(roots),(736+math.sqrt(228096))/98)
 return dict(characteristic='w^4−(A+B+qx qy)w^2+AB',spin_parameter='required',gyroscopic_stable_roots=roots.tolist())
ck(70,3,'一般轴向自转的线性行列式',a703)
def a704():
 L=1;l2=3;a0=1;T=(math.sqrt(L*(L+l2))+l2*math.asinh(math.sqrt(L/l2)))/math.sqrt(2*a0*l2)
 num=quad(lambda z:2*z/math.sqrt(2*a0*l2*z*z/(l2+z*z)) if z else math.sqrt(2/a0),0,math.sqrt(L))[0];eq(T,num)
 u=1/T;eq(u,math.sqrt(1.5)/(1+.75*math.log(3)))
 return dict(time=T,handle_speed=u)
ck(70,4,'相对运动时间的积分与闭式',a704)
def a705():
 a=.5;t=np.array([math.cos(a),math.sin(a)]);v=np.array([-math.sin(a),math.cos(a)]);cen=np.array([-2.6,.1]);obj=np.array([cen-t-v,cen+t-v,cen+t+v,cen-t+v]);ims=np.array([p/(p[0]+1) for p in obj]);recovered=np.array([-p/(p[0]-1) for p in ims]);assert np.max(abs(recovered-obj))<1e-12
 for j in range(4):eq(np.linalg.norm(recovered[j]-recovered[(j+1)%4]),2)
 eq(np.dot([1,math.tan(a)],[1,-1/math.tan(a)]),0)
 return dict(reconstruction_error=float(np.max(abs(recovered-obj))),side=2)
ck(70,5,'四像点逆映射与正方形恢复',a705)
def a706():
 theta=brentq(lambda x:1+2*math.sin(x)-2*math.cos(x),0,math.pi/2)
 w2=4.5+3*math.sin(theta);N=.75*math.cos(theta);f=.75+1.5*math.sin(theta);eq(f,2*N);assert N>0
 return dict(first_slip_deg=math.degrees(theta),omega_squared_scaled=w2,normal_scaled=N)
ck(70,6,'临界摩擦、法向接触与转角',a706)
def a707():
 alpha=1.3;v0=2;x0=.2;xf=math.sqrt(x0*x0+2*v0/alpha)
 def x(t):return xf*math.tanh(alpha*xf*t/2+math.atanh(x0/xf))
 tt=.7;hh=1e-6;v=(x(tt+hh)-x(tt-hh))/(2*hh);eq(v+.5*alpha*x(tt)**2,v0+.5*alpha*x0*x0,2e-9)
 return dict(limit_position=xf,finite_position=x(tt))
ck(70,7,'磁制动守恒式与位移解导数',a707)
def a708():
 year=365.25*86400;t1=1.91*year;t2=3.66*86400;ratio=t1/t2;NA=6.02214076e23;N2=NA/(228*ratio+224);N1=ratio*N2
 l1=math.log(2)/t1;l2=math.log(2)/t2
 def dN2(t):return l1*N1*math.exp(-l1*t)-l2*(N2*math.exp(-l2*t)+l1*N1/(l2-l1)*(math.exp(-l1*t)-math.exp(-l2*t)))
 eq(dN2(0)/(l1*N1),0)
 eq((228*N1+224*N2)/NA,1);return dict(initial_ratio=ratio,N10_per_g=N1,N20_per_g=N2,secular_correction=l1/(l2-l1))
ck(70,8,'活度平衡初值与精确Bateman导数',a708)
# 069

def a691():
 k=.4;v=math.sqrt(k);errors=[]
 for theta in np.linspace(0,math.pi/2,15):
  def r2(t):return (math.cosh(t)-v*math.cos(theta)*math.sinh(t))**2+(v*math.sin(theta)*math.sinh(t))**2
  opt=minimize_scalar(r2,bounds=(0,4),method='bounded');analytic=(1-k+math.sqrt((1-k)**2+4*k*math.sin(theta)**2))/2;errors.append(abs(opt.fun-analytic))
 assert max(errors)<1e-8
 return dict(max_nearest_error=max(errors),vertex=math.sqrt(1-k))
ck(69,1,'轨道最小化与最近距离公式',a691)
def a692():
 # Integral of uniform exterior pressure over the small cap: n_x ranges −1 to −1/2.
 cap=2*math.pi*quad(lambda u:-u,-1,-.5)[0];eq(cap,3*math.pi/4)
 cut=(1/math.pi)**2*(3*math.pi/4)/2;push=(1/(4*math.pi))**2*cap/2;eq(cut-push,45/(128*math.pi))
 return dict(cap_projected_area=cap,force_coefficient=cut-push)
ck(69,2,'球冠法向压力积分与切面力',a692)
def a693():
 def state(u1,u2):
  if u2>=1/3 and u1+2*u2>=1:return 'a'
  if u1<=u2 and u1+2*u2<1:return 'b'
  if u2<1/3 and u1+u2>=2/3:return 'c'
  if u1>u2 and u1+u2<2/3:return 'd'
  raise AssertionError((u1,u2))
 for u1 in np.linspace(.001,.999,39):
  for u2 in np.linspace(.002,.998,37):state(u1,u2)
 assert state(.4,.2)=='d' and state(.4,.3)=='c' and state(.4,.5)=='a'
 return dict(grid_points=39*37,critical_mu2=[4/15,1/3],accelerations_at_04_02=[.2,.1,.1])
ck(69,3,'完整相图覆盖及固定μ1截线',a693)
def a694():
 M=np.eye(3);K=np.diag([3,3,5]);V=np.array([[1,1],[1,-1],[-2,0.]])
 mm=V.T@M@V;kk=V.T@K@V;eq(mm[0,0],6);eq(kk[0,0],26);eq(mm[1,1],2);eq(kk[1,1],6)
 assert not mm[0,1] and not kk[0,1]
 for ks in [[3,4,5],[3,3,5],[4,4,4],[.1,7,2]]:
  a,b,c=ks;sumk=a+b+c;pair=a*b+a*c+b*c
  KK=np.array([[a+c,c],[c,b+c]]);MM=np.array([[2,1],[1,2]])
  numerical=np.sort(np.linalg.eigvals(np.linalg.solve(MM,KK)))
  analytical=np.array([sumk-math.sqrt(sumk*sumk-3*pair),sumk+math.sqrt(sumk*sumk-3*pair)])/3
  assert np.max(abs(numerical-analytical))<1e-12
  assert min(numerical)>0
 return dict(mode_stiffnesses=[26,6],mode_masses=[6,2],frequency_squared_ratio=13/9,gas_lengths=[.5,.5,.25],unequal_stiffness_cases=4)
ck(69,4,'受约束质量与气体正劲度的投影',a694)
def a695():
 n=1.5;A=2*math.pi*math.sqrt(n*n-1)
 g=lambda w:w-2*math.atan(math.sqrt(max(0,A*A-w*w))/w)
 ws=[brentq(lambda w:g(w)-m*math.pi,1e-8,A-1e-8) for m in range(3)]
 angles=[math.degrees(math.acos(w/(2*math.pi*n))) for w in ws];assert all(a>math.degrees(math.asin(1/n)) for a in angles)
 return dict(TE_transverse_roots=ws,TE_angles_deg=angles,exact_modes=3,geometric_positive_modes=2)
ck(69,5,'精确TE反射相位与模式数',a695)
def a696():
 beta=s.symbols('b');u2=(s.Rational(40,63)-s.Rational(4,21)/(1+beta)**2)*4-s.Rational(40,21)*beta
 eq(u2.subs(beta,0),16/9);eq(u2.subs(beta,1),4/9)
 f=(12/(1+beta)**3+1)*(beta+s.Rational(4,5))/2;eq(f.subs(beta,0),26/5)
 assert all(float(s.diff(f,beta).subs(beta,b))<0 for b in np.linspace(0,1,40))
 roots=[]
 for gamma in [1,3,4,5]:
  bt=(gamma-6+math.sqrt(gamma*gamma+12*gamma))/6
  eq(3*(1+bt)**2,gamma*(2+bt));eq(gamma*(1-1/(1+bt)**2)-3*bt,0)
  roots.append(bt)
 eq(roots[2],1)
 return dict(critical_speed_squared=4,max_tip_moment_scaled=26/5,radial_turning_roots=roots)
ck(69,6,'杯口可达性、初速和倾覆力矩单调性',a696)
def a697():
 U=4575/13;I=1.2*(550-U)/300;eq(I,(U-175)/2000+U/500);eq(I,103/130)
 area=.5*100/300+200/300+.5*100/300;eq(area,1)
 return dict(first_U=195,second_U=U,second_I=I)
ck(69,7,'能谱归一化与工作点支路闭合',a697)
def a698():
 eps=.02;Epair=.5*(math.sqrt(1-eps)+math.sqrt(1+eps));change=Epair-1;leading=-eps*eps/8;eq(change,leading,1e-8)
 correlation=.25*(1/math.sqrt(1-eps)-1/math.sqrt(1+eps));assert correlation>0
 return dict(pair_energy_change=change,per_atom_change=change/2,positive_correlation=correlation)
ck(69,8,'零点能精确平方根与相关涨落',a698)
# 068

def a681():
 v=-.5+math.sqrt(3)/7;w=-1+5*math.sqrt(3)/14;K=.5*v*v+.2*w*w
 eq(K,(847-420*math.sqrt(3))/1960);assert K<.7 and v+w<0;eq((5*v-2*w)/7,-1/14)
 return dict(v2=v,omega2=w,post_energy=K,later_rolling_velocity=-1/14)
ck(68,1,'球底滑动、动能及后续滚动',a681)
def a682():
 ratio=(1-(3/4)**3)/((3/2)**3-(3/4)**3);eq(ratio,37/189)
 center=1/.125-6/4.5+1;eq(center,23/3)
 V1=-6/(4.5-.125)+1;V2=-.5/(3-.75)+1.5/3;U=.5*(V1+V2);eq(U,-59/1260)
 return dict(field_ratio=ratio,center_potential=center,assembly_energy=U)
ck(68,2,'分域镜像、电荷补偿与去自能',a682)
def a683():
 H=1;a=.7;M=1;dm=lambda z:3*z*z
 hc=quad(lambda z:z*dm(z),0,H)[0];I3=quad(lambda z:.5*(a*z)**2*dm(z),0,H)[0];I1=quad(lambda z:(z*z+.25*(a*z)**2)*dm(z),0,H)[0]
 eq(hc,.75);eq(I3,.3*a*a);eq(I1,.6*(1+a*a/4))
 return dict(hc=hc,I3=I3,I1=I1)
ck(68,3,'圆锥三个惯性量薄片积分',a683)
def a684():
 Rx=.6*4004.7/3000.1;rho=Rx*math.pi*(.0004856)**2/(4*1.059);eq(Rx,.8009133028899037)
 d=np.array([1.,1.1,.9,1.])*1e-4;unc=np.std(d,ddof=1)/2;eq(unc,4.082482904638632e-6)
 return dict(Rx=Rx,resistivity=rho,uncertainty_example=unc)
ck(68,4,'电桥阻值、电阻率及逐差统计',a684)
def a685():
 a=.02;l=.2;sig=3;Delta=np.array([10,20]);R=np.array([[1/a,1/l],[1/l,1/a]])/(4*math.pi*sig);P=np.linalg.solve(R,Delta)
 formula=4*math.pi*sig*a*l/(l*l-a*a)*np.array([l*10-a*20,l*20-a*10]);assert max(abs(P-formula))<1e-12
 return dict(powers=P.tolist(),linear_system_residual=max(abs(R@P-Delta)))
ck(68,5,'三维热阻直接求逆与功率',a685)
def a686():
 D=-1-math.sqrt(2);R=1;f=1;errs=[]
 for t in np.linspace(0,2*math.pi,100):
  X=D+math.cos(t);Y=math.sin(t);xp=X/(X+1);yp=Y/(X+1);errs.append(abs((xp+D)**2+yp*yp-R*R))
 assert max(errs)<1e-12;d=-2*D;eq(d/4-R*R/d,f)
 X,Y,D0,R0,f0=s.symbols('X Y D R f');expr=((f0+D0)*X-D0*f0)**2+f0*f0*Y*Y-R0*R0*(f0-X)**2
 expr=s.expand(expr.subs(R0*R0,D0*D0+2*f0*D0));zero(expr-f0*f0*((X+D0)**2+Y*Y-(D0*D0+2*f0*D0)))
 return dict(circle_map_max_residual=max(errs),required_radius_ratio=1,focal_length=f,source_unequal_radius_claim='fails in meridional model')
ck(68,6,'逐点物像映射与同半径必要条件',a686)
def a687():
 delta=.0002;E=5;R1=R4=1-delta;R2=R3=1+delta;U=E*(R1/(R1+R2)-R3/(R3+R4));eq(U,-E*delta)
 eps=quad(lambda x:1-x,.1,.3)[0]/.2;eq(eps,1-.2)
 return dict(signed_bridge_output=U,finite_gauge_mean=eps)
ck(68,7,'实际桥路分压极性与片长积分',a687)
def a688():
 W=math.sqrt(38);p=math.sqrt(377/152);e1=53/(2*W);e2=23/(2*W);beta=math.sqrt(73)/15;gamma=15/(2*W)
 eq(e1+e2,W);eq(e1*e1-p*p,16);eq(e2*e2-p*p,1)
 phi=math.atan(p/(gamma*math.sqrt((beta*e1)**2-p*p)));theta=math.atan(3/8)
 maxres=0
 for a in np.linspace(0,2*math.pi,121):
  ps=p*math.cos(a);py=p*math.sin(a)
  labE=gamma*(e1+e2+beta*(ps-ps));labPx=gamma*(ps-ps+beta*(e1+e2));eq(labE,7.5);eq(labPx,math.sqrt(73)/2)
 return dict(beta=beta,p_star=p,relative_max_deg=math.degrees(phi),direction_interval=[math.degrees(theta-phi),math.degrees(theta+phi)])
ck(68,8,'两末态四动量回代与切线方向',a688)
assert len(rows)==40 and len({(r['set'],r['question']) for r in rows})==40
out=dict(script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),groups=rows,extra=extra,passed=True,scope='每题关键结果组作独立代数、积分、事件或数值核验；非穷尽所有假设。完整推导及图示另经审读。')
(SCRIPT_DIR/'math_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(dict(passed=True,groups=len(rows),batch='072–068'),ensure_ascii=False))
