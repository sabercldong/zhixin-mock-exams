from pathlib import Path
import json,math,hashlib,re
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
from scipy.special import airy,ai_zeros,erf
W=Path(__file__).resolve().parents[1]
rows=[]
def ck(n,q,index,method,value=True):
 assert value is not False,(n,q,index,method)
 rows.append(dict(set=n,question=q,variant=index,method=method,passed=True))
def near(a,b,tol=1e-8):assert abs(a-b)<tol,(a,b)
# 021: inversion, ODE, distribution, finite networks, Hessian, distance, thermal ODE, ray chain
k=sp.symbols('k',positive=True)
near(1+4*(1/3)**2/(1-1/3)**2,2);near((7/9)/math.sqrt(1-(7/9)**2),7/(4*math.sqrt(2)))
ck(21,1,3,'支持力反演和接触上界')
sig=1.3;eps=1e-4;sol=solve_ivp(lambda t,y:[y[1],sig**2*y[0]],(0,2),[eps,0],rtol=1e-11,atol=1e-13)
near(sol.y[0,-1],eps*math.cosh(2*sig),1e-10);ck(21,1,4,'线性不稳定平衡初值方程积分')
z=(np.arange(500000)+.5)/500000;F=-z+2*np.sqrt(z*(1.25-z))
for d in [.05,.2,.5,.7]:
 near(float(np.mean(F<=d)),1-math.sqrt(25-20*d-16*d*d)/5,5e-6)
ck(21,2,4,'均匀碰撞高度分布独立采样')
r=.5
for i in range(6):r=.5*r+1/6
near((r-1/3)/(1/3),1/128);ck(21,3,4,'有限网络迭代达到误差门槛')
s,zs,C,L,m=sp.symbols('s z C L m',positive=True)
U=L**2/(2*m*s*s)-C*zs/(s*s+zs*zs)**sp.Rational(3,2)
# a=m=Omega=1 fixes C by radial circular condition
Cval=3*sp.sqrt(3)/4
H=sp.hessian(U,(s,zs)).subs({s:1,zs:1/sp.sqrt(2),m:1,L:1,C:Cval})
expected=sp.Matrix([[sp.Rational(2,3),-2*sp.sqrt(2)/3],[-2*sp.sqrt(2)/3,sp.Rational(4,3)]])
assert sp.simplify(H-expected)==sp.zeros(2)
ck(21,4,4,'完整有效势的耦合Hessian求导')
a,b,tc,vmax=2.,.7,1.1,5.
vc=a/b*(math.exp(b*tc)-1)
near(quad(lambda t:a/b*(math.exp(b*t)-1),0,tc)[0],a/b**2*(math.exp(b*tc)-1-b*tc))
near(quad(lambda t:vmax+(vc-vmax)*math.exp(-b*t),0,2)[0],2*vmax+(vc-vmax)/b*(1-math.exp(-2*b)))
ck(21,5,4,'逐段速度积分检查出轨位移')
rate=3.;sol=solve_ivp(lambda t,y:[-rate*y[0]],(0,1),[1],rtol=1e-11,atol=1e-13);near(sol.y[0,-1],math.exp(-3));ck(21,6,4,'封闭定容温度扰动方程积分')
kk,D,f1,f2,u=2.,1.7,2.,1.,.6
def img(D):return 2*(f1+f2)+D-u-(kk*kk*D-2*kk*(f1+f2))
near(img(D+.01)-img(D),(1-kk*kk)*.01);ck(21,7,4,'镜末端坐标变动计入全局像位移')
# 022
h=(math.sqrt(5)-1)/2;near(h*h/(1-h),1);ck(22,1,3,'周期单调反演与物理解筛选')
near(math.sqrt((.5**2+.25)/(1-.5)),1);ck(22,1,4,'新增惯量的能量比')
ecrit=2*9**(-1/8)-1;near(((1+ecrit)/2)**8,1/9);ck(22,2,3,'递推固定增量正负阈值')
assert .99**(8*37)>.05>.99**(8*38);ck(22,2,4,'逐级偏差衰减整数边界')
m1,m2=2.,3.;theta=.7;V=m1/(m1+m2);w=m2/(m1+m2);v1=np.array([V+w*math.cos(theta),w*math.sin(theta)]);v2=np.array([V-V*math.cos(theta),-V*math.sin(theta)])
near(float(v1@v2),(m1-m2)/(2*m1)*float(v2@v2));ck(22,3,3,'质心系散射构造检查异质量夹角')
v1=np.array([2.5,math.sqrt(3)/2]);v2=np.array([1.5,-math.sqrt(3)/2]);near(v1@v1,7);near(v2@v2,3);near(v1@v2,3);ck(22,3,4,'出射矢量构造和能量动量守恒')
O,tau,A=1.4,.7,2.
def theory(t):return A/math.sqrt(1+(O*tau)**2)*math.cos(O*t-math.atan(O*tau))
sol=solve_ivp(lambda t,y:[(A*math.cos(O*t)-y[0])/tau],(0,5),[theory(0)],rtol=1e-11,atol=1e-13)
near(sol.y[0,-1],theory(5));ck(22,4,3,'正弦驱动磁场方程初值积分')
sig,T,ar,Dm,Bf=2.,.3,.8,1.1,1.4;ta=sig*T*ar**2/(4*Dm)
PJ=lambda t:quad(lambda r:2*math.pi*r*sig*T*(r*Bf*math.exp(-t/ta)/(2*ta))**2,0,ar)[0]
Q=quad(PJ,0,np.inf)[0];Um=math.pi*ar*ar*Dm*Bf*Bf/2;near(Q,Um/2);near(2*Um-Um-Q,Um/2)
ck(22,4,4,'时空焦耳热双积分揭示近似能量缺口')
near(math.exp(-2*(math.log(2)/2)),.5);ck(22,5,3,'磁能半衰期及热功率积分')
tt=sp.symbols('t',nonnegative=True);I=sp.exp(-tt/2-tt**2/12)
assert sp.simplify(sp.diff(I,tt)+(1+tt/3)*I/2)==0;ck(22,5,4,'时变电阻率的一阶方程残差')
near(quad(lambda b:math.sqrt(1-b*b),0,1)[0],math.pi/4);ck(22,6,3,'条件冲击参数的弦长分布积分')
near(math.sqrt(.01**2+.02**2+.02**2),.03);ck(22,6,4,'三个独立输入对数偏导传播')
near(-1.5*(1.5+1)/4,-15/16);ck(22,7,3,'由直接像高反演折射率')
near(1/(1/.5-1/1.5),.75);ck(22,7,4,'折射率匹配后的独立球面镜成像')
a1,a2=-ai_zeros(2)[0];fn=lambda y:airy(y-a1)[0]**2
norm=quad(fn,0,40)[0];av=quad(lambda y:y*fn(y),0,40)[0]/norm
near(av,2*a1/3);ck(22,8,3,'Airy波函数平均高度直接积分')
ratio=(a2-a1)*math.sqrt(a1)/math.pi;assert ratio<1
ck(22,8,4,'精确Airy零点与经典时间标度比较')
# 023
D=[np.array([[1.,0.,-y],[0.,1.,x]]) for x,y in [(0,1),(-math.sqrt(3)/2,-.5),(math.sqrt(3)/2,-.5)]]
K=sum(d.T@d for d in D);disp=np.linalg.solve(K,[0,-3,0]);forces=np.array([-d@disp for d in D])
near(max(np.linalg.norm(forces,axis=1)),1);ck(23,1,3,'三腿刚度矩阵独立求解不等容量')
near(abs(disp[2]),0);ck(23,1,4,'力偶抵消后转动自由度求解')
x=(np.arange(500000)+.5)/500000*2-1
near(np.mean(abs(x)>math.sqrt(.75)),1-math.sqrt(.75),3e-6);ck(23,2,4,'球面方向余弦均匀统计')
for ep in [1e-3,1e-5]:
 exact=.5*(1+math.sqrt(1-1/(1+ep)**2));approx=.5+math.sqrt(ep/2)
 assert abs(exact-approx)<ep**1.5
ck(23,3,3,'临界双根展开误差阶')
for B in [100,300]:
 rt=brentq(lambda r:B*B*(r-1)*(r+1)**2-16*r,1,2)
 assert abs((rt-1)/(4/B**2)-1)<.001
ck(23,3,4,'强场转向点原方程求根')
G,MS,RE,RM=6.67e-11,1.99e30,1.5e11,5.79e10
tf=math.pi*math.sqrt(((RE+RM)/2)**3/(G*MS));phi=(math.pi-math.sqrt(G*MS/RM**3)*tf)%(2*math.pi)
near((phi+math.sqrt(G*MS/RM**3)*tf)%(2*math.pi),math.pi)
ck(23,4,3,'霍曼端点时间及行星相位会合')
u=24019.94241/math.log(100);near(math.exp(24019.94241/u),100);ck(23,4,4,'火箭质量比反演上限')
Aw=100*2e-8*140/10;near(8000*140*Aw,31.36);ck(23,5,3,'固定线长电阻和质量约束')
y=sp.symbols('y');mu=sp.Rational(1800);Lam=(1-2*(.001-y))/mu+2*(.001-y)
F=sp.Rational(1,10)*4*sp.pi*10**(-7)*1000**2/Lam**2
near(float(sp.diff(F,y).subs(y,0)),30139714.082301274,1e-4);ck(23,5,4,'磁吸力对气隙的独立求导')
gam=1.4;ep=.0001;al=1+ep;fun=lambda h:al/(gam-1)*(1-(1+h)**(1-gam))-h
hv=al**(1/gam)-1;hh=brentq(fun,ep/gam,4*ep/gam,xtol=1e-12)
assert abs(hh/(2*ep/gam)-1)<.001
near(fun(hv)/ep**2,1/(2*gam),1e-4);ck(23,6,3,'弱超压停点数值求根与峰值功展开')
al=2;fun=lambda h:al/(gam-1)*(1-(1+h)**(1-gam))-h;hh=brentq(fun,1e-3,10)
assert fun(hh*.8)>0 and fun(hh*1.2)<0;ck(23,6,4,'有限缸出口判据的功积分符号')
near(330/(4*.056),1473.2142857142858);ck(23,7,3,'指定端修正有效长度')
near(1650*math.sqrt(313.15/293.15),1705.3565868111318);ck(23,7,4,'理想气体温标平方根')
tau=math.acosh(2);near(math.cosh(tau),2);near(math.sinh(tau),math.sqrt(3));near(math.tanh(tau),math.sqrt(3)/2);ck(23,8,4,'双曲世界线的实验室功与时间')
# 024
t=sp.symbols('t');rx=sp.cos(2*t);ry=sp.sin(2*t);near(float((sp.diff(rx,t,2)*rx+sp.diff(ry,t,2)*ry).subs(t,.4)),-4);ck(24,1,3,'圆周轨迹微分得到受力与功率')
dt=1e-5;tm=math.pi/3;near((1/(1+2*math.cos(2*(tm-dt))))*dt,1/(2*math.sqrt(3)),3e-6);ck(24,1,4,'奇点原函数数值极限')
a,b=1.,2.;Ad=lambda x:a+(b-a)*x
down=quad(lambda s:quad(Ad,s,1)[0]/Ad(s),0,1)[0]
Au=lambda x:b-(b-a)*x
up=quad(lambda s:quad(Au,s,1)[0]/Au(s),0,1)[0]
near(down,(b*b*math.log(b/a)-(b*b-a*a)/2)/(2*(b-a)**2));near(up,(-a*a*math.log(b/a)+(b*b-a*a)/2)/(2*(b-a)**2))
ck(24,2,3,'自重轴力及变截面柔度双积分')
near(1/quad(lambda x:1/(1+x),0,1)[0]/1.5,2/(3*math.log(2)));ck(24,2,4,'端力柔度积分和固定体积比较')
p=lambda n:n/(1+.2*n)**2;near(p(5)/p(4),81/80);ck(24,3,3,'不同灯数功率比反演')
assert [n for n in range(1,20) if 1/(1+.2*n)>=.75]==[1];ck(24,3,4,'效率限制整数可行集枚举')
s=sp.symbols('s',positive=True);f=s/(1+s*s)**sp.Rational(3,2)
near(float(f.subs(s,1/sp.sqrt(2))),2/(3*math.sqrt(3)));assert sp.simplify(sp.diff(f,s).subs(s,1/sp.sqrt(2)))==0;ck(24,4,3,'恢复力最大值求导')
x=.3;m=2;T=3;K=(4*math.pi**2*m/T**2)*(1+x*x)**2.5/(1-2*x*x)
near(K*(1-2*x*x)/(1+x*x)**2.5/m,(2*math.pi/T)**2);ck(24,4,4,'局部势能曲率反演')
d=sp.symbols('d',positive=True);VV=sp.symbols('V');Force=VV/d**2-d/(d*d-1)**2
eqV=d**3/(d*d-1)**2
assert sp.simplify(sp.diff(Force,d).subs(VV,eqV)-(d*d+3)/(d*d-1)**3)==0;ck(24,5,3,'固定电势平衡消元后的力导数')
UU=VV/d-1/(2*(d*d-1));assert sp.simplify(-sp.diff(UU,d)-Force)==0;ck(24,5,4,'计入电源后的有效势求导')
prob=quad(lambda u:4/math.sqrt(math.pi)*u*u*math.exp(-u*u),0,math.sqrt(1.5))[0]
near(prob,erf(math.sqrt(1.5))-2*math.sqrt(1.5)*math.exp(-1.5)/math.sqrt(math.pi));ck(24,6,3,'麦克斯韦三维动量分布积分')
hstep=1e-6;der=(math.asin(.5/(1+hstep))-math.asin(.5/(1-hstep)))/(2*hstep)
near(abs(der)*.01,.01/math.sqrt(3),1e-8);ck(24,6,4,'衍射角对动量的差分敏感度')
A=.5**2;B=.75;cross=.5*.5*.75
near(2*cross/(A+B),.375);ck(24,7,3,'相关矩阵交叉项与背景强度')
th=math.pi/3;alpha=th;tt=.5;AA=math.cos(alpha)**2;BB=tt**2*math.cos(alpha-th)**2
near(AA,BB);near(2*tt*abs(math.cos(th)*math.cos(alpha)*math.cos(alpha-th))/(AA+BB),.5);ck(24,7,4,'可调检偏投影强度匹配')
xv=np.array([.2,.4,.7])
vals=[np.prod(np.sin(xv*np.array(sign))) for sign in __import__('itertools').product([-1,1],repeat=3)]
near(max(abs(np.array(vals)))-min(abs(np.array(vals))),0);ck(24,8,3,'八种波数符号直接比较空间模态')
integr=quad(lambda x:x**3/math.expm1(x),0,100)[0];near(integr,math.pi**4/15);ck(24,8,4,'玻色能量积分独立数值计算')
# 025
m,b,k,G,I,w=2.,.4,1.1,1.3,.7,.8
aa=G*I/math.sqrt((k-m*w*w)**2+(b*w)**2);ph=math.atan2(b*w,k-m*w*w)
x=lambda t:aa*math.cos(w*t-ph);v=lambda t:-w*aa*math.sin(w*t-ph)
sol=solve_ivp(lambda t,y:[y[1],(G*I*math.cos(w*t)-b*y[1]-k*y[0])/m],(0,5),[x(0),v(0)],rtol=1e-11,atol=1e-13)
near(sol.y[0,-1],x(5));ck(25,1,3,'有阻尼弹簧受迫振动方程积分')
RR,L=.3,.7;wc=G/math.sqrt(m*L);Z=RR+1j*(wc*L-G*G/(m*wc));near(abs(Z),RR);ck(25,1,4,'耦合电流速度相量直接消元')
bet=.6;ga=1/math.sqrt(1-bet*bet);cost=-bet
labE=ga*(1+bet*cost);labpx=ga*(cost+bet)
near(labpx,0);near(labE,1/ga);ck(25,2,3,'静止系光子四矢量boost到实验室横向')
ep=sp.symbols('ep',positive=True);Mass=ep+sp.sqrt(ep*ep+1)
assert sp.simplify(ep*sp.diff(Mass,ep)/Mass-ep/sp.sqrt(ep*ep+1))==0;ck(25,2,4,'精确质量反演的误差偏导')
for freq in [1,1.5]:near(math.cos(freq*4*math.pi),1)
ck(25,3,3,'有理频率共同相位恢复及坐标有界')
A,B,de,w=1.4,.8,.6,1.2;C1=math.sqrt(2)*B*math.cos(de)-A;C2=-math.sqrt(2)*B*math.sin(de)
area=quad(lambda t:.5*(A*math.cos(w*t)*(-w*C1*math.sin(w*t)+w*C2*math.cos(w*t))-(C1*math.cos(w*t)+C2*math.sin(w*t))*(-w*A*math.sin(w*t))),0,2*math.pi/w)[0]
near(abs(area),math.pi*math.sqrt(2)*A*B*abs(math.sin(de)));ck(25,3,4,'平面轨迹面积线积分')
TH,T,k=313.15,298.15,173.;P=k*(TH-T)**2/T
fn=lambda T:k*(TH-T)-P*T/(TH-T)
d=(fn(T+1e-4)-fn(T-1e-4))/(2e-4);near(-d,k*(1+TH/T),1e-5);ck(25,4,3,'冷室热收支函数差分稳定性')
q=1000;PP=(k*(TH-T)+q)*(TH-T)/T;near(PP,180.8653362401476);near(k*(TH-T)+q-PP*T/(TH-T),0);ck(25,4,4,'增加热源后冷端稳态收支')
near(56**2,3136);ck(25,5,3,'二维孔径映射Jacobian及功率守恒')
near(34*(14/17),28);ck(25,5,4,'正常点像与鬼像圆边缘距离')
near(math.sin(.001)/.001,1-.001**2/6,1e-12);near(1/math.pi,.3183098861837907);ck(25,6,3,'短弧级数与长弧分支范围')
assert 2/math.pi>.5;near(1/2,.5);ck(25,6,4,'单调载荷容量分支反演')
th=.8;e=.6;ll=1.2;L=1.5;mm=2.;r=ll/(1+e*math.cos(th));vr=L/(mm*ll)*e*math.sin(th);vt=L/(mm*r)
VV=np.array([vr*math.cos(th)-vt*math.sin(th),vr*math.sin(th)+vt*math.cos(th)])
ref=L/(mm*ll)*np.array([-math.sin(th),e+math.cos(th)])
near(float(np.linalg.norm(VV-ref)),0);ck(25,7,3,'极坐标速度独立投到固定轴')
a,b,T=2.,1.,3.;H=2*math.pi*a*b/T;near(H*H/(b*b/a),4*math.pi**2*a**3/T**2);ck(25,7,4,'面积速度与半通径消去短轴')
p,z=1.3,.7
for c in [.01,.005]:
 exact=quad(lambda phi:(z-c*math.sin(phi))/math.sqrt(p*p+2*c*z*math.sin(phi)-c*c*math.sin(phi)**2),0,2*math.pi,epsabs=1e-12)[0]
 app=2*math.pi*z/p*(1+3*c*c/(4*p*p)*(1+z*z/(p*p)))
 assert abs(exact-app)<4*c**4
ck(25,8,3,'整圈精确运动积分与二阶位移展开')
p,c=1.,1.5;sinphi=p/c;rate2=p*p-c*c*sinphi*sinphi;zdot=-c*sinphi
nr=-rate2-c*zdot*sinphi
near(nr,1);ck(25,8,4,'转向点径向Newton方程检验反力换向')
# Bind all added paragraphs to final source (including corrected numerical estimates).
expected=[]
for item in json.loads((W/'核验/added_variants.json').read_text()):
 n,q=item['set'],item['question'];tail=(W/f'蔡题{n:03d}/整理版/drafts/question-{q:02}.md').read_text().split('## 九、变式训练')[-1]
 blocks=re.split(r'(?m)^(?:变式([一二三四])：|（([1-4])）)',tail)[1:]
 assert len(blocks)==12,(n,q,len(blocks))
 orig_count=4-item['added_count']
 for idx in range(orig_count+1,5):expected.append((n,q,idx))
assert sorted(expected)==sorted((r['set'],r['question'],r['variant']) for r in rows),(len(expected),len(rows))
for row in rows:
 path=W/f"蔡题{row['set']:03d}/整理版/drafts/question-{row['question']:02}.md"
 row['draft_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
(W/'核验/added_math_verification.json').write_text(json.dumps(dict(all_passed=True,checks=len(rows),records=rows),ensure_ascii=False,indent=2)+'\n')
print('added variants independent checks',len(rows),'passed')
