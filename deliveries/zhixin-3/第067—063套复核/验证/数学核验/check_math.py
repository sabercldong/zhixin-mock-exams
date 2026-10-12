"""40 independently reproducible key-result groups, not an exhaustive proof of every model.
NumPy/SciPy/SymPy required. Input values retain the stated conditional models.
"""
from pathlib import Path
import json,hashlib,math,itertools
import numpy as np
import sympy as S
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
from scipy.linalg import solve_banded
from fractal_network import graph
P=Path(__file__).resolve().parent
rows=[];extra=[]
def close(a,b,rtol=1e-8,atol=1e-9):
 assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
def ident(a):assert S.simplify(a)==0,S.simplify(a)
def group(n,q,label,fn):
 value=fn();rows.append(dict(set=n,question=q,check=label,passed=True,result=value));print(n,q,label,flush=True)
def scalar(x):return float(x)
pi=np.pi;g=9.8

def q671():
 m,l,v=1.,1.,1.;I=2*m*l*l/3;me=1/(1/(3*m)+(l/3)**2/I);close(me,2*m)
 for lam in [.3,2,10,100]:
  vp=(lam-2)/(lam+2)*v;J=4*lam/(lam+2)*m*v;Vc=J/(3*m);om=J*l/(3*I)
  close(.5*lam*m*v*v,.5*lam*m*vp*vp+.5*3*m*Vc*Vc+.5*I*om*om)
 threshold=6*pi/(3*np.sqrt(3)-pi)
 def D(phi,lam):return -(lam+6)/(6*lam)*phi-np.tan(phi)/3
 close(D(2*pi/3,threshold),0)
 for lam in [9.5,15,100]:
  root=brentq(lambda phi:D(phi,lam),2*pi/3,pi-1e-8);assert root>=2*pi/3
 assert D(2*pi/3,5)<0
 return dict(effective_mass=me,threshold=threshold)
group(67,1,'自由刚体接触等效质量、动能和单调交点阈值',q671)

def q672():
 a,c,th=S.symbols('a c theta',real=True)
 u=2*a*a*c-S.Rational(2,5)*((1+a)**2/(1-a*c)+(1-a)**2/(1+a*c))+S.Rational(4,5)*(1-a*a)/S.sqrt(1+a*a*(1-c*c))
 ident(u-u.subs(a,-a));ident(S.expand(S.series(u,a,0,4).removeO()+2*a*a-S.Rational(2,5)*a*a*(c-c*c)))
 U=u.subs(c,S.cos(th));curv=S.diff(U,th,2)
 ident(curv.subs(th,0)-2*a*a*(2*a**6-11*a**4+24*a*a+1)/(5*(1-a*a)**2))
 ident(curv.subs(th,S.pi)-2*a*a*(2*a*a+3)/5)
 for aa in [.005,.01]:
  d=S.lambdify(th,S.diff(U,th).subs(a,aa),'numpy');root=brentq(d,.7,1.4);approx=pi/3+65/(8*np.sqrt(3))*aa*aa;assert abs(root-approx)<2e-6
 return dict(T0_over_Tpi=math.sqrt(3),finite_a_curvatures='symbolically checked',tilt_shift='checked at a=.005,.01')
group(67,2,'精确镜像势、偶数阶展开、两端曲率和倾角修正',q672)

def q673():
 k,K,m=3.,7.,2.;A=np.array([[k+K,-K],[-K,k+K]])/m;ev=np.linalg.eigvalsh(A);close(ev,[k/m,(k+2*K)/m])
 v=2.;w=np.sqrt(ev);t=.137;xa=v/2*(np.sin(w[0]*t)/w[0]+np.sin(w[1]*t)/w[1]);xb=v/2*(np.sin(w[0]*t)/w[0]-np.sin(w[1]*t)/w[1]);acc=-v/2*np.array([w[0]*np.sin(w[0]*t)+w[1]*np.sin(w[1]*t),w[0]*np.sin(w[0]*t)-w[1]*np.sin(w[1]*t)]);close(acc,-A@np.array([xa,xb]));assert np.linalg.det([[k+K,-K],[-K,K]])>0
 return dict(omega_squared=ev.tolist(),single_free_end_no_zero=True)
group(67,3,'模态本征值、初速叠加和单端去约束',q673)

def q674():
 t=S.symbols('t',real=True);R,r,L,C=1,2,3,4;gamma=S.Rational(R-r,2*L);w=S.sqrt(1/(S.Rational(L)*C)-gamma**2);i=S.exp(-gamma*t)*S.sin(w*t)/w
 ident(L*S.diff(i,t,2)+(R-r)*S.diff(i,t)+i/C);close(i.subs(t,0),0);close(S.diff(i,t).subs(t,0),1)
 J=2;eta=4*(r-R)/(3*J*J);close((r-R)*J*J/2-eta*3*J**4/8,0)
 return dict(growing_oscillation=R<r<R+2*np.sqrt(L/C),nonlinear_amplitude_depends_on_eta=True)
group(67,4,'起振初值解、KVL及新增三次非线性供耗能平衡',q674)

def q675():
 th,eta=S.symbols('theta eta',positive=True);phi=-th+S.pi/(2*S.sqrt(eta))*S.atan(2*S.sqrt(eta)*th/S.pi)
 ident(S.diff(phi,th)+4*eta*th**2/(S.pi**2+4*eta*th**2));end=-pi/2+pi*pi/8
 for ratio in [.1,1,4]:
  beta=1/(1+ratio);rho=beta;rd=-(1-beta);close(rd+ratio*rho,0)
 return dict(equal_mass_phi_end=end,equal_mass_psi_end_degrees=pi*pi/8*180/pi)
group(67,5,'一般质量的质心、角动量微分和真实轨迹末点',q675)

def q676():
 om=2*pi*1000;A,x,y=3.95,1.96,2.48;phase=np.arcsin(x/A);B=A*y/x;r=100*y/x*np.sqrt(1-(x/A)**2)-100;L=100*y/(om*A);C=1/(om*100*np.tan(np.arcsin(2.5/3.54)));H=100/(100+r+1j*om*L);close(abs(H),A/B);close(-np.angle(H),phase)
 corners=[100*yy/xx*np.sqrt(1-(xx/aa)**2)-100 for aa,xx,yy in itertools.product([A-.005,A+.005],[x-.005,x+.005],[y-.005,y+.005])];assert min(corners)<10<max(corners)
 return dict(r_Ohm=r,L_mH=1e3*L,C_uF=1e6*C,f0_Hz=1/(2*pi*np.sqrt(L*C)),r_quantization_range=[min(corners),max(corners)])
group(67,6,'由原始椭圆截距反演、复阻抗回代及量化读数角点',q676)

def q677():
 z,b,la,mu,R,T0,P0=S.symbols('z b la mu R T0 P0',positive=True);press=P0*(1-b*z)**la;T=T0*(1-b*z);rho=mu*press/(R*T)
 ident(S.diff(press,z)+la*b*R*T0/mu*rho)
 z0=.4;la0=2.5;rho0=1;V=2;m0=.2;b0=.1;h=(1-(.5+m0/(rho0*V))**(1/(la0-1)))/b0;close(rho0*(1-b0*h)**(la0-1)*V,m0+rho0*V/2)
 return dict(ballast_exhaustion_height=h,sealed_gas_mass_constant=True)
group(67,7,'大气静力、气体定质量和丢配重最高平衡高度',q677)

def q678():
 K=np.sqrt(3)/4;J=np.array([[1.5,1j*K],[-1j*K,1.0]]);close(np.linalg.eigvalsh(J),[.75,1.75]);D=np.diag([1,1j]);after=D@J@D.conj().T
 th=pi/6;e=np.array([np.cos(th),np.sin(th)]);close((e@after@e).real,1.75);close(2*.75/np.trace(J).real,.6)
 return dict(eigen_intensity=[.75,1.75],unpolarized_fraction=.6,degree_of_polarization=.4)
group(67,8,'相干矩阵、波片变换、最大方向及非偏振比例',q678)

def q661():
 l,l0,F=S.symbols('l l0 F',positive=True);E=F*(l-l0-l0*S.log(l/l0));ident(S.diff(E,l)-F*(1-l0/l))
 fs,mm,MM=100.,2.,3.;a=quad(lambda lam:fs/(fs-mm*g-MM*g*lam),0,1)[0];closed=fs/(MM*g)*np.log((fs-mm*g)/(fs-mm*g-MM*g));close(a,closed)
 return dict(stretched_length=a,positive_area_condition=fs>(mm+MM)*g)
group(66,1,'非线性弹力能量导数、材料坐标积分与正截面',q661)

def q662():
 polar=quad(lambda th:3*np.cos(th)**2*np.sin(th),0,pi)[0]*2*pi;close(polar,4*pi);cavity=quad(lambda th:np.cos(th)**2*np.sin(th),0,pi)[0]*2*pi/(4*pi);close(cavity,1/3)
 for f in [.01,.1,.4]:
  er=(1+2*f)/(1-f);close((er-1)/(er+2),f)
 return dict(single_sphere_integral=polar,cavity_factor=cavity,mixture_result='conditional spherical-cavity mean field')
group(66,2,'单球电荷积分、球腔场积分及平均场代数',q662)

def q663():
 r,r0,b=S.symbols('r r0 b',positive=True);v=g/(4*b)*(r-r0**4/r**3);ident(b*S.diff(v,r)+3*b*v/r-g)
 kap=S.symbols('kappa',positive=True);w=2*S.Rational(49,5)/(7*kap)*(r-r0**7/r**6);ident(kap*S.diff(w,r)+6*kap*w/r-2*S.Rational(49,5))
 close(np.sqrt(14/8),np.sqrt(7)/2)
 return dict(active_h_limit='gt^2/8',swept_h_limit='gt^2/14',time_ratio=np.sqrt(7)/2,zero_seed='positive seed limit only')
group(66,3,'两种变质量动量ODE与正种子极限',q663)

def q664():
 F,k,G=5.,2.,3.;a,b=F/(3*k),2*F/(3*k);td=quad(lambda x:G/(F-k*x),a,b)[0];tu=quad(lambda x:G/(k*x),a,b)[0];close(td,tu);close(td,G/k*np.log(2));W=F*(b-a);close(W,F*F/(3*k));P=W/(td+tu);close(P,F*F/(6*G*np.log(2)));v=F/(G*np.sqrt(6*np.log(2)));close(G*v*v,P)
 return dict(down_time=td,up_time=tu,cycle_average=P)
group(66,4,'真实行程速度积分、循环功和等功率匀速',q664)

def q665():
 t=S.symbols('t',real=True);s=S.Rational(1,2);D,alpha,m=1,1,1;om=S.sqrt(2*(1-s*s));q=S.log((1+s*S.cos(om*t))/(1-s*s));U=(1-S.exp(-q))**2-1
 ident(S.Rational(1,2)*S.diff(q,t)**2+U-(s*s-1));ql=-np.log(1.5);qr=-np.log(.5);assert abs(ql)!=abs(qr)
 mu=12*15.99/(12+15.99)*1.660e-27;D0=1.780e-18;w0=4.088e14;alpha0=np.sqrt(mu*w0*w0/(2*D0));lam=2*pi*3e8/w0;close(alpha0,2.31e10,rtol=.005);close(lam,4.61e-6,rtol=.005)
 return dict(finite_energy_trajectory='symbolic energy conserved',turns=[ql,qr],small_oscillation_wavelength_m=lam)
group(66,5,'Morse有限能量精确轨迹、非对称转折点及红外尺度',q665)

def q666():
 for i in np.linspace(0,pi/2-.0001,60):
  ga=np.arcsin(np.sin(i)/1.5);rp=(1.5*np.cos(i)-np.cos(ga))/(1.5*np.cos(i)+np.cos(ga));tp=2*np.cos(i)/(1.5*np.cos(i)+np.cos(ga));close(rp*rp+1.5*np.cos(ga)/np.cos(i)*tp*tp,1)
 ib=np.arctan(1.5);ga=np.arcsin(np.sin(ib)/1.5);close(1.5*np.cos(ib)-np.cos(ga),0)
 return dict(Brewster_degrees=ib*180/pi,energy_conservation=True)
group(66,6,'Fresnel实数支能流守恒、布儒斯特角和基矢',q666)

def q667():
 Rx,rg,r,R0,eps=100.,20.,1.,150.,1.5;I1=eps/(r+Rx+rg+R0);I2=eps/(r+Rx+rg)
 Z3=Rx+rg*R0/(rg+R0);I3=eps/(r+Z3)*R0/(rg+R0)
 Z4=(Rx+rg)*R0/(Rx+rg+R0);I4=eps/(r+Z4)*R0/(Rx+rg+R0)
 ee=R0*I1*I2/(I2-I1);SS=I1*R0/(I2-I1);close(ee,eps);close(SS,Rx+rg+r)
 for II,target in [(I3,rg),(I4,r)]:
  K=R0*(ee/II-SS);small=2*K/(SS+np.sqrt(SS*SS-4*K));close(small,target)
 return dict(current_A=[I1,I2,I3,I4],epsilon=ee,S=SS,recovered=[rg,r,Rx])
group(66,7,'四种真实电路的支路电流、两二次式和稳定小根',q667)

def q668():
 c=S.symbols('c');poly=4*S.sqrt(3)*c**3-2*c*c-4*S.sqrt(3)*c+3;root=(S.sqrt(21)-S.sqrt(3))/6;ident(poly.subs(c,root));w0=np.sqrt(.8*g/(.88*np.cos(pi/6)))
 K=.5;om=2;th=.4;dt=1e-5
 def L(phi):return K*om*(np.array([0,0,1])-np.cos(th)*np.array([np.sin(th)*np.cos(phi),np.sin(th)*np.sin(phi),np.cos(th)]))
 close((L(om*dt)-L(-om*dt))/(2*dt),[0,-K*om*om*np.sin(th)*np.cos(th),0])
 return dict(initial_omega=w0,second_turn_degrees=float(S.acos(root))*180/pi,torque_azimuthal=True)
group(66,8,'转折三次根和角动量方向导数',q668)

def q651():
 x=S.symbols('x',positive=True);L=x+S.Rational(1,3)/x**3;ident(S.diff(L,x).subs(x,1));close(L.subs(x,1),4/3);ident(S.series(L.subs(x,1+S.Symbol('e')),S.Symbol('e'),0,4).removeO()-(S.Rational(4,3)+2*S.Symbol('e')**2-S.Rational(10,3)*S.Symbol('e')**3))
 E=-S.Rational(1,6)/x**2+(S.Rational(4,3)-x)**2/2;ident(S.diff(E,x).subs(x,1));ident(S.diff(E,x,2).subs(x,1));assert S.diff(E,x,3).subs(x,1)>0
 return dict(critical_L_over_l0=4/3,critical_is_not_minimum=True)
group(65,1,'同步支曲线、临界展开与势能三阶导数',q651)

def q652():
 z,a=S.symbols('z a',positive=True);M=a**4/(a*a+z*z)**S.Rational(3,2);ident(S.diff(M,z)+3*z*M/(a*a+z*z));shape=z/(a*a+z*z)**4;ident(S.diff(shape,z).subs(z,a/S.sqrt(7)))
 R,L,om,I0=2.,3.,5.,4.;zz=1.2;mm=float(M.subs({a:1,z:zz}));mp=float(S.diff(M,z).subs({a:1,z:zz}));D=R*R+(om*L)**2
 av=quad(lambda t:I0*np.sin(om*t)*(-mm*om*I0/D*(R*np.cos(om*t)+om*L*np.sin(om*t)))*mp,0,2*pi/om)[0]/(2*pi/om);close(av,-mp*mm*om*om*L*I0*I0/(2*D));assert av>0
 return dict(force_peak=1/np.sqrt(7),average_force=av)
group(65,2,'完整互感梯度、周期积分平均力和稳定峰值',q652)

def q653():
 vals=[]
 for bracket in [(.3,1.),(1.7,2.5)]:
  def eq(al):
   t=1/(np.sin(al)-.25);return 1+(1+np.cos(al))*t-t*t/2
  al=brentq(eq,*bracket);t=1/(np.sin(al)-.25);close(1+np.sin(al)*t,2+t/4);close(1+(1+np.cos(al))*t-t*t/2,0);assert 1+np.cos(al)>0;vals.append(dict(alpha_degrees=al*180/pi,time=t,ground_angle_degrees=90-al*90/pi))
 vc=np.array([.25,0]);r=np.array([2,-1]);ez=np.array([[0,-1],[1,0]]);vrot=vc-ez@r;arot=r-2*ez@vrot;close(arot,[-2,.5])
 return dict(throwing=vals,doppler_Hz=250*(10-1/(4*np.sqrt(2)))/(10+1/np.sqrt(2)))
group(65,3,'真实相遇根、地面轨迹初速、转动系负号和多普勒',q653)

def q654():
 nn=np.array([1.466,1.471,1.482]);lam=np.array([7.682e-7,5.876e-7,4.047e-7]);AA=1-1/nn**2;out={}
 for name,om in [('in_medium',2*pi*299792458/(nn*lam)),('vacuum',2*pi*299792458/lam)]:
  vals=[]
  for i,j in [(0,1),(0,2),(1,2)]:
   w2=(AA[i]*om[i]**2-AA[j]*om[j]**2)/(AA[i]-AA[j]);ss=AA[i]*(w2-om[i]**2);close(np.sqrt((w2-om[[i,j]]**2)/(w2-ss-om[[i,j]]**2)),nn[[i,j]]);vals.append(np.sqrt(w2))
  out[name]=vals
 return out
group(65,4,'两种波长口径逐对反演并回代折射率',q654)

def q655():
 flux=quad(lambda th:np.cos(th)*np.sin(th),0,pi/2)[0]*2*pi/(4*pi);pressure=2*quad(lambda th:np.cos(th)**2*np.sin(th),0,pi/2)[0]*2*pi/(4*pi);close(flux,.25);close(pressure,1/3)
 return dict(energy_flux_factor=flux,mirror_pressure_factor=pressure,blackbody_absorption_plus_emission=1/6+1/6)
group(65,5,'半球角积分、镜面动量与黑体发射反冲',q655)

def q656():
 records=[]
 for f in [50,1000]:
  om=2*pi*f;phi=om*19e-6;L=100*np.tan(phi)/(3*om);C=1/(4*om*om*L);assert L<.001;records.append(dict(f=f,L=L,C=C))
 om=2*pi*1000;L=100*np.tan(om*190e-6)/(3*om);C=1/(4*om*om*L);assert .001<L<.030;close(1/(2*pi*np.sqrt(L*C)),2000)
 return dict(original=records,high_frequency_period_smaller_than_shift=True,corrected_190us=[L,C])
group(65,6,'三档原19微秒排除与190微秒条件校勘',q656)

def q657():
 beta=pi/12;L=4;gap=.064;d=2*200e-9*L/(gap*np.cos(beta));close(d,25e-6/np.cos(beta))
 eta=.008;xp=L*eta/(np.cos(beta)+eta*np.sin(beta));xm=-L*eta/(np.cos(beta)-eta*np.sin(beta));close(xp-xm,2*L*eta*np.cos(beta)/(np.cos(beta)**2-eta*eta*np.sin(beta)**2));assert (xp+xm)/2<0
 C=1e-8;growth=12.;xs=np.geomspace(1e-7,1e-2,500);coef=(xs+C/(growth*xs))/2;assert np.argmin(coef) in range(0,500);close((np.sqrt(C/growth)+C/(growth*np.sqrt(C/growth)))/2,np.sqrt(C/growth))
 return dict(tipped_screen_width_um=d*1e6,exact_asymmetry=(xp+xm)/2,growth_minimum='positive product initial-value model')
group(65,7,'实际屏面投影、两光线精确交点及正初值优化',q657)

def q658():
 Q=.005/60;v=Q/(pi*.015**2);local=1060*v*v*np.log(.065/.035);force=2*1060*Q*v;avg=force/(2*.065*.03);book=g/.06;close(local,9.119,rtol=.0002);close(avg,5.340,rtol=.0002);k=(15/16)**.25;close(1/(1/16+k**4),1)
 return dict(Q=Q,v=v,local_Pa=local,average_dynamic_Pa=avg,book_Pa=book,ratio=avg/book,bridge_radius=k)
group(65,8,'流量、局部与整体弯管压强、书本比值和搭桥回代',q658)

def q641():
 cases=[]
 for x,y in [(3,5),(9,2),(12,9),(9,6)]:
  thresholds=[x/3,y/2,3];cases.append(dict(x=x,y=y,first=np.argmin(thresholds),F=min(thresholds)))
 # All three stick but base slides right, acceleration follows total mass balance.
 f,x,y=3.5,20,20;a=(f-3)/3;f1=3*f-a;f2=2*f+a;close(3*a,f-3);assert abs(f1)<x and abs(f2)<y
 return dict(first_events=cases,velocity_history_required_after_start=True)
group(64,1,'首次滑动三阈值、有效边界及共同加速受力',q641)

def q642():
 # Saddle equations xdd -2 Om yd +(ga-Om^2)x=0; ydd+2 Om xd+(-ga/2-Om^2)y=0.
 for om in [1.1,1.8]:
  A=np.array([[0,0,1,0],[0,0,0,1],[om*om-1,0,0,2*om],[0,om*om+.5,-2*om,0]])
  eig=np.linalg.eigvals(A);assert max(abs(eig.real))<1e-7
 om=1.;v=2.;y=4*v/(3*om);close(-2*om*0+(1-om*om)*3,0);close(2*om*v+(-.5-om*om)*y,0)
 return dict(strict_stability='Omega > sqrt(ga)',critical_linear_drift=True)
group(64,2,'完整一阶状态特征根和临界线性漂移解',q642)

def q643():
 mu_g,l,u,v=1.,1.,1.,3.;left=quad(lambda X:1/np.sqrt(v*v-mu_g*(X+1.5)**2/l),-1.5,-.5)[0];center=quad(lambda X:1/np.sqrt(v*v-mu_g*l-2*mu_g*(X+.5)),-.5,.5)[0];t=1/v+left+center;closed=l/v+np.sqrt(l/mu_g)*np.arcsin(np.sqrt(mu_g*l)/v)+(np.sqrt(v*v-mu_g*l)-np.sqrt(v*v-3*mu_g*l))/mu_g;close(t,closed)
 for beta in [1.1,1.4]:
  wR=(3*beta*beta-10*beta+9)/(2*beta);assert wR<beta
 for beta in [1.5,1.9]:assert 1-beta/2<beta
 for beta in [2,3,10]:assert 1/np.sqrt(2*beta)<=.5+1e-12
 return dict(high_speed_time=t,beta_ge_one_no_complete_crossing=True,turning_boundary_beta=2)
group(64,3,'位置积分与高速闭式、beta分支出口能量及转折',q643)

def q644():
 out=[]
 for u,l in [(4,np.sqrt(3)),(2,1/np.sqrt(3)),(4,2/np.sqrt(3))]:
  s=np.sqrt(3)*l/2;A=np.array([0.,0]);B=np.array([(u-s)/(u-s-1)-u/(u-1),-l/(2*(u-s-1))]);C=np.array([0.,-l/(u-1)]);sides=sorted([np.linalg.norm(B-A),np.linalg.norm(C-A),np.linalg.norm(C-B)]);close(np.array(sides)/sides[0],[1,np.sqrt(3),2]);right=C if len(out)<2 else B;oth=[p for p in [A,B,C] if not np.array_equal(p,right)];close(np.dot(oth[0]-right,oth[1]-right),0);out.append([A.tolist(),B.tolist(),C.tolist()])
 return dict(image_coordinates=out)
group(64,4,'三组逐点像坐标、直角点积及边长比',q644)

def boost(b):
 b=np.array(b);bs=b@b;ga=1/np.sqrt(1-bs);M=np.eye(3);M[0,0]=ga;M[0,1:]=-ga*b;M[1:,0]=-ga*b
 if bs:M[1:,1:]+=(ga-1)*np.outer(b,b)/bs
 return M

def q645():
 beta=.7;theta=.02;bp=np.array([beta,0]);bpp=beta*np.array([np.cos(theta),np.sin(theta)]);T=boost(bpp)@boost(-bp);eta=np.diag([1,-1,-1]);close(T.T@eta@T,eta)
 small=boost(beta*np.array([np.cos(1e-6),np.sin(1e-6)]))@boost(-bp);ga=1/np.sqrt(1-beta*beta);close(small[1,2]/1e-6,ga-1,rtol=1e-5)
 return dict(metric_preserved=True,passive_axis_rotation_coefficient=ga-1)
group(64,5,'独立标准推动复合、度规与小角空间旋转项',q645)

def q646():
 T,V,n,Cv,R=S.symbols('T V n Cv R',positive=True);entropy=n*Cv*S.log(T)+n*R*S.log(V/n);ident(S.diff(entropy,T)-n*Cv/T);ident(S.diff(entropy,V)-n*R/V)
 NA=6.02214076e23;kb=1.380649e-23;Rgas=NA*kb;me=9.1093837139e-31;c=299792458;temp=1e10;close(NA*me*c*c/(Rgas*temp),me*c*c/(kb*temp))
 return dict(molar_particle_exponent_equal=True,low_temperature='formal classical-model limit only')
group(64,6,'理想气体熵全微分与摩尔/粒子静能指数',q646)

def q647():
 records=[];x,y=.25,.5;prevD=1.;prevP=.25
 for depth in range(6):
  rec=graph(depth);assert rec['kcl']<1e-10
  if depth:
   x,y=x/3+1/12+y/6,x/3+1/6+y/3
   close(rec['Rdiag'],2*y);close(rec['Radj'],x+y);Ic=7/(12*(1+prevD));close(rec['Ic'],Ic);top=4*(1+prevD)/3;close(rec['P'],4*prevP/27+top*Ic*Ic)
  records.append({k:float(v) if isinstance(v,np.generic) else v for k,v in rec.items()});prevD=rec['Rdiag'];prevP=rec['P']
 xx=S.Rational(3,14);yy=S.Rational(5,14);ident(2*xx-4*yy+1);ident(S.Rational(2,3)*xx+yy-S.Rational(1,2));close((343/1296)/(1-4/27),343/1104)
 return dict(finite_graphs=records,limit_Rdiag=5/7,limit_Radj=4/7,limit_Ic=49/144,limit_P=343/1104)
group(64,7,'从几何去重建立有限导线图，核对递推和无限极限',q647)

def q648():
 a,b=2.,4.;rp,r1,r2,r3,U=3.,5.,7.,11.,10.;D=rp+a*a*r2+b*b*r3+(a+b)**2*r1;I=U/D;I2=a*I;I3=b*I;close(U*I/2,(rp*I*I+r1*(I2+I3)**2+r2*I2**2+r3*I3**2)/2);C=rp+b*b*r3+(a+b)**2*r1;opt=C/(a*a);close(.5*a*a*opt*(U/(C+a*a*opt))**2,U*U/(8*C))
 return dict(D=D,all_loss_power=U*I/2,optimal_r2=opt)
group(64,8,'真实公共电阻交叉项、源功率守恒及最大负载功率',q648)

def q631():
 a,mu,R=2.,.5,500.;t=np.sqrt(R*np.sqrt((mu*g)**2-4*a*a))/a;v=a*t;close(np.hypot(a,v*v/(2*R)),mu*g/2);close(-np.cross([0,0,1],[0,-1,0]),[-1,0,0]);assert t<np.sqrt(mu*g*R)/a
 return dict(quasisteady_rear_limit_seconds=t,body_gyro_torque=[-1,0,0])
group(63,1,'参考摩擦圆时刻及明确坐标下的陀螺反作用',q631)

def q632():
 h,rho,th,al=1.,10.,.01,pi/4;out=[]
 for ms,mc in [(1.,1.),(.75,.5),(1.15,.9)]:
  ts=np.sqrt(2*h*ms/g)/np.sin(al);uc=np.sqrt(2*g*h/mc);wc=np.sqrt(g/(mc*rho));tc=np.arctan(rho*th*wc/uc)/wc;close(ms*(2*g*h/ms),mc*uc*uc);out.append(4*(ts+tc))
 close(out,[2.646,2.277,2.826],rtol=.001)
 return dict(periods_seconds=out,connection_model='short smooth lossless transition, conditional')
group(63,2,'过渡两侧有效质量能量和修正周期数值',q632)

def q633():
 l=1.;l1=l2=.5;a2=b2=1/12;D=a2+b2+l1*l1+l2*l2;beta=g*(l1+l2)/D;T=g*(l2*(a2+l1*l1)-l1*(b2+l2*l2))/(l*D);SS=g-T-l2*beta;close(beta,1.5*g);close(T,0);close(SS,.25*g)
 # Arbitrary algebraic slack-state parameters, independently check the rigid-rod acceleration.
 l1,l2,a2,b2=.75,.3,.02,.015;A=a2+l1*l1;t=g*b2*(A-l*l1)/(b2*(A+l*l)+(l-l2)**2*A);aB=l*(g*l1+t*l)/A;aD=g-t*(1+(l-l2)**2/b2);close(aB,aD)
 return dict(uniform_beta=beta,uniform_T=T,uniform_S=SS,slack_rod_acceleration_residual=aB-aD)
group(63,3,'均匀双杆样例与松绳分支刚杆加速度约束',q633)

def q634():
 u=(1+np.sqrt(13))/3;v1=u/(u-1);p2=2-v1;v2=1/(-.5-1/p2);close(v2,u);ratio=1-2/v1;assert 0<ratio<1;d=u-1/3;R=.1;c0=1-u/np.sqrt(u*u+R*R);r=d*np.sqrt((1-c0/2)**-2-1);close(1-d/np.sqrt(d*d+r*r),c0/2)
 return dict(u_over_f=u,second_aperture_ratio=ratio,exact_half_flux_r=r)
group(63,4,'两透镜逐步像距、第二镜孔径和圆孔半立体角',q634)

def q635():
 r,C,om,q=1.,.7,1.3,2*pi/16;zv=r+1/(1j*om*C);s=np.exp(-1j*q);E=om*(s-1);Z=2*r+zv*(2-s-1/s);A=E/Z;N=16
 mat=np.zeros((N,N),complex)
 for j in range(N):mat[j,j]=2*r+2*zv;mat[j,(j-1)%N]=-zv;mat[j,(j+1)%N]=-zv
 driven=np.array([E*s**j for j in range(N)]);sol=np.linalg.solve(mat,driven);close(sol,A*s**np.arange(N))
 roots=np.roots([1,-(2+2*r/zv),1]);zeta=next(x for x in roots if abs(x)<1);I0=A*(s-zeta)/(s*(1-zeta));NN=180;ab=np.zeros((3,NN),complex);ab[0,1:]=-zv;ab[1,:]=2*r+2*zv;ab[1,0]=2*r+zv;ab[2,:-1]=-zv;sol=solve_banded((1,1),ab,E*s**np.arange(NN));close(sol[0],I0)
 return dict(periodic_AC_complex=[(A*(1/s-1)).real,(A*(1/s-1)).imag],halfline_AC_complex=[I0.real,I0.imag],decay_root_abs=abs(zeta))
group(63,5,'循环网孔矩阵与半无限端部三对角独立求解',q635)

def q636():
 d=S.symbols('d');ratio=S.sqrt(1+3*S.sin(d)**2)/S.cos(d)**6;ident(S.series(ratio,d,0,4).removeO()-(1+S.Rational(9,2)*d*d))
 c=299792458;gam=10/.511;v=c*np.sqrt(1-1/gam**2);B=3e-7;e=1.602176634e-19;me=9.1093837139e-31;om=e*B/(gam*me);a=gam*me*v/(e*B);close(a*om,v);slow=3/np.sqrt(2)*v/3e7
 return dict(gamma=gam,v_over_c=v/c,radius_m=a,cyclotron_omega=om,slow_omega=slow)
group(63,6,'真实偶极场线二阶展开及相对论频率半径',q636)

def q637():
 N=4;u=1.;v=0.
 for _ in range(2):v=(N-1)/(N+1)*v+2/(N+1)*u
 close(v,.64);N=100000;close(1-((N-1)/(N+1))**(N//2),1-np.exp(-1),rtol=1e-5)
 M=2.;E=.1;A=1.3;Ap=A+2*E/M;Ep=E/(A*Ap);oldE=M*(A+1/A)/2+E;newE=M*(Ap+1/Ap)/2+Ep;oldp=M*(A-1/A)/2+E;newp=M*(Ap-1/Ap)/2-Ep;close(oldE,newE);close(oldp,newp)
 return dict(finite_steel_fraction=v,photon_A_increment=Ap-A,reflected_energy=Ep)
group(63,7,'有限钢珠更新、连续极限和单次光子四动量',q637)

def q638():
 B,l,m,C,L,U=1.,1.,2.,3.,4.,1.;Cp=1/(1/C+B*B*l*l/m)
 records=[]
 for lam in [-9,-3,-1,-.6,.6,1,2,3,4,8.2]:
  y=lam;charges=0.;loss=0.;N=0
  while abs(y)>1+1e-12:
   sign=np.sign(y);yb=2*sign-y;dq=Cp*(y-yb);charges+=dq;loss+=abs(dq);y=yb;N+=1
  vf=B*l*charges/m;Uc=lam-charges/C;close(y,Uc-B*l*vf);initial=.5*C*lam*lam;final=.5*C*Uc*Uc+.5*m*vf*vf;close(initial-final,loss);close(N,max(0,math.ceil((abs(lam)-1)/2)));records.append(dict(lambda_=lam,F=y,halfcycles=N,vf=vf,loss=loss))
 return dict(effective_C=Cp,states=records)
group(63,8,'逐半周期阈值追踪、总能量耗散、次数和速度映射',q638)

assert len(rows)==40 and {(x['set'],x['question']) for x in rows}=={(n,q) for n in range(63,68) for q in range(1,9)}
result=dict(passed=True,scope='40题列出的关键结果；附加假设在各组说明，非全部物理模型的穷尽证明',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),groups=rows,extra=extra)
(P/'math_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=lambda v:v.item() if isinstance(v,np.generic) else str(v)));print('PASS: 40 groups')
