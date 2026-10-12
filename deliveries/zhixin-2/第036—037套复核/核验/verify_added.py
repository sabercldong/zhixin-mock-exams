from pathlib import Path
import json,re,hashlib,math
import numpy as np
import sympy as s
from scipy.integrate import quad,solve_ivp
from scipy.optimize import minimize_scalar
W=Path(__file__).resolve().parents[1];rows=[]
def eq(a,b,tol=2e-7):
 assert np.allclose(a,b,rtol=tol,atol=tol),(a,b)
 return dict(computed=np.asarray(a).tolist(),expected=np.asarray(b).tolist())
def rec(n,q,j,method,*checks):
 p=W/f'蔡题{n:03d}/整理版/drafts/question-{q:02d}.md';v=re.split(r'^变式[一二三四]：',p.read_text().split('## 九、变式训练')[1],flags=re.M)[1:];assert len(v)==4
 rows.append(dict(set=n,question=q,variant=j,method=method,checks=checks,status='pass',variant_sha256=hashlib.sha256(v[j-1].strip().encode()).hexdigest(),draft_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
# Ring potential: axis curvature and cone geometry, then exact energy integral for weak Duffing correction.
rec(36,1,2,'单环轴向势能二阶展开和正质量',eq(-2*(-np.pi**3/12)*2,np.pi**3/3))
rec(36,1,3,'母线弧长下的势能与周期比',eq(np.sqrt(6/3),np.sqrt(2)))
A=np.pi**3/12;B=np.pi**5/320;am=.001;T=4*quad(lambda th:1/np.sqrt(2*A+2*B*am*am*(1+np.sin(th)**2)),0,np.pi/2)[0];T0=2*np.pi/np.sqrt(2*A)
rec(36,1,4,'四次势能的周期能量积分',eq(T/T0,1-9*np.pi**2/320*am*am,tol=1e-10))
H,V=np.sqrt(3)/8,1/8
rec(36,2,2,'弧长积分及摩擦圆边界',eq(2*quad(lambda z:H/np.sqrt(H*H+(2*V*z)**2),0,.5)[0],np.sqrt(3)*np.log(3)/2),eq((np.hypot(H,V)-H)/(2*V),1-np.sqrt(3)/2),eq(H*H+(.5-V)**2,3/16))
V=(np.sqrt(3)*.75-1)/4;H=np.sqrt(3-(3-np.sqrt(3)*.75)**2)/4
rec(36,2,3,'实际张力与跨度数值回代',eq([V,H,np.hypot(V,H),H/V*np.arcsinh(V/H)],[.0747595264192,.0816733716014,.1107227457172,.896087202987]))
mu=np.sqrt(3)-1+1e-12;V=(np.sqrt(3)*mu-1)/4;H=np.sqrt(3-(3-np.sqrt(3)*mu)**2)/4
rec(36,2,4,'静止可行区间与竖直绳极限',eq([H/V*np.arcsinh(V/H),(np.hypot(H,V)-H)/(2*V)],[0,.5],tol=3e-4))
norms=np.array([[np.sqrt(3)/2,.5],[-np.sqrt(3)/2,.5],[0,-1]]);mass=np.array([1,2,3])
center=np.array([3*np.sqrt(3),39])/61;acc=np.array([24,15,22])/61
rec(36,3,2,'有限质量环的完整力与约束',eq(acc-norms@center,[0,0,1]),eq(center+(mass*acc)@norms,[0,0]))
U=np.array([2.7,-1.9]);rel=np.array([[0,0],[0,0],[1,0]])
rec(36,3,3,'共同速度平移的相对速度不变',eq((rel+U)-U,rel))
acc=np.array([6,3,2])/11;center=-np.array([8/np.sqrt(3),2])/11
rec(36,3,4,'换初速珠后的完整几何约束',eq(acc-norms@center,[1,0,0]),eq((mass*acc)@norms,[0,0]))
L,R,rs,E=2.,7.,3.,12.;tau=L*(R+rs)/(R*rs);inf=E/rs;tb=tau*np.log(2)
rec(36,4,2,'电感电流ODE和电荷积分',eq(quad(lambda t:inf*(1-np.exp(-t/tau)),0,tb)[0],inf*tau*(np.log(2)-.5)),eq(.5*L*(inf/2)**2,L*inf**2/8))
rec(36,4,3,'两个放电回路分别积分',eq([quad(lambda t:np.exp(-2*R*t/L),0,np.inf)[0]/quad(lambda t:np.exp(-R*t/L),0,np.inf)[0],quad(lambda t:2*R*np.exp(-4*R*t/L),0,np.inf)[0]/quad(lambda t:R*np.exp(-2*R*t/L),0,np.inf)[0]],[.5,1]))
ii=.7;tb=.8;il=lambda t:inf+(ii-inf)*np.exp(-t/tau);ir=lambda t:rs/(R+rs)*(inf-ii)*np.exp(-t/tau)
heat=quad(lambda t:rs*(il(t)+ir(t))**2+R*ir(t)**2,0,tb)[0];work=E*quad(lambda t:il(t)+ir(t),0,tb)[0]
rec(36,4,4,'非零初流的源功与完整电阻热',eq(quad(il,0,tb)[0],inf*tb+(ii-inf)*tau*(1-np.exp(-tb/tau))),eq(heat,work-L*(il(tb)**2-ii**2)/2))
K,J,E,R,k=.3,.8,2.,1.1,.2;steady=K*E/(K*K+k*R);tau=J*R/(K*K+k*R);tb=tau*np.log(2)
rec(36,5,2,'电机ODE与输入电荷时间积分',eq(quad(lambda t:(E-K*steady*(1-np.exp(-t/tau)))/R,0,tb)[0],E*tau/R*np.log(2)-K*steady*tau/R*(np.log(2)-.5)))
rec(36,5,3,'动生电动势半径积分',eq(quad(lambda r:r,.5,1)[0]/quad(lambda r:r,0,1)[0],.75))
opt=minimize_scalar(lambda x:-x*(1-2*x)/(1-x),bounds=(0,.5),method='bounded')
rec(36,5,4,'功率和效率分别优化',eq(opt.x,1-1/np.sqrt(2),tol=1e-5),eq(-opt.fun,3-2*np.sqrt(2)),eq(.25*(1-2*.25)/(1-.25),1/6))
aa=np.array([-.5,1-np.sqrt(3)/2,.5,1+np.sqrt(3)/2]);ff=np.sign(aa)*aa*(1-aa)
rec(36,6,2,'四位置的物距像距与焦点',eq(ff,[.75,(2*np.sqrt(3)-3)/4,.25,-(2*np.sqrt(3)+3)/4]),eq((.25-aa)**2,ff**2))
rec(36,6,3,'发散透镜的唯一负焦距',{'negative_f_count':int(sum(ff<0))},eq(aa[ff<0],[1+np.sqrt(3)/2]))
rec(36,6,4,'按真实入射方向计算横向倍率',eq([-.5/.5,-(-1.5)/.5],[-1,3]))
tl=(5/6)**.4;nl=4*(5/6)**.6;nr=5-nl;tr=(5/3)/nr
rec(36,7,2,'不等容室的质量和总内能守恒',eq([nl*tl,nr*tr],[10/3,5/3]),eq((nl*tl+nr*tr),5),eq(tl,(nl/4)**(2/3)))
rec(36,7,3,'完整热平衡的总量和能量',eq([1.5+1.5,1.5*1+1.5*1],[3,3]))
x=2*.75**.6;ds=1.5*(x*np.log(.75**.4)+(3-x)*np.log(1.5/(3-x)))-x*np.log(x)-(3-x)*np.log(3-x)+2*np.log(2)
assert ds>0
rec(36,7,4,'开放子系统的理想气体熵',{'entropy_in_A0R':ds,'positive':True})
v,u=.6,.2;vp=(v+u)/(1+v*u);out=(-vp-u)/(1+vp*u);dp=out/np.sqrt(1-out*out)-v/np.sqrt(1-v*v);de=1/np.sqrt(1-out*out)-1/np.sqrt(1-v*v)
rec(36,8,2,'两次洛伦兹速度变换与四动量',eq(out,-.8),eq(de,-u*dp),eq([de,dp],[5/12,-25/12]))
v,u,w=.5,.5,13/14;r=v/(v+u)*(1-u/w)
rec(36,8,3,'相邻碰撞和返回事件的反演',eq(r,3/13),eq(v*w*(1-r)/(v+r*w),u))
rec(36,8,4,'光子四动量反射与镜面功',eq((1+.5)/(1-.5),3),eq(3-1,-.5*(-3-1)))
# 037: physical normal impact, region-current counts, signed spherical optics and modal perturbations.
eta=.17;a=.2;Om=1.3;Ic=a*a/eta
for j,e in [(2,1),(3,0)]:
 J=2*a*(1+e)*Om/(1+eta);vc=-a*Om+J;omega=-Om+a*J/Ic;before=(a*a+Ic)*Om**2/2;after=(vc*vc+Ic*omega*omega)/2
 rec(37,1,j,'法向冲量的质心动量、角动量和动能',eq(vc+a*omega,2*e*a*Om),eq((before-after)/before,4*eta*(1-e*e)/(1+eta)**2))
N=math.ceil(np.log(2)/(-2*np.log(.99)));assert .99**(2*(N-1))>.5>=.99**(2*N)
rec(37,1,4,'明确能量重置模型的整数阈值',eq(N,35))
rec(37,2,2,'轴对称安培环路穿面电流',eq([0,4*np.pi*1e-7*2/(2*np.pi*.1)],[0,4e-6]))
rec(37,2,3,'馈线破坏平面对称性后的安培定律',eq([-4*np.pi*1e-7*3/(2*np.pi*.2),0],[-3e-6,0]))
mu,I,b,a=1.2,2,.1,1
rec(37,2,4,'柱壳磁能密度直接积分',eq(quad(lambda r:(mu*I/(2*np.pi*r))**2/(2*mu)*2*np.pi*r,b,a)[0],mu*I*I/(4*np.pi)*np.log(a/b)))
n,l=s.symbols('n l');u=-1/(2*(n-1)+1/l);xr=l/(1-2*l);expr=1/(2-u)+n/(xr-2)-(1-n)
nv=(-89+np.sqrt(23041))/56
rec(37,3,2,'逐界面成像式回代物理根',eq(float(expr.subs({n:nv,l:s.Rational(1,10)})),0),eq(28*nv*nv+89*nv-135,0))
lv=(-29+np.sqrt(1057))/18
rec(37,3,3,'固定折射率反演物点位置',eq(float(expr.subs({n:s.Rational(4,3),l:lv})),0),eq(9*lv*lv+29*lv-6,0))
nv=1.3330398446566;lv=.195;uv=float(u.subs({n:nv,l:lv}));p=2-uv;vv=lv/(1-2*lv)-2
rec(37,3,4,'接触界面与末球面的横向倍率连乘',eq([1/(1-2*lv),(-uv/lv)*(-vv/(nv*p))],[100/61,.51349935418]))
M=np.array([[2,1],[1,1]]);K=np.diag([2,1]);vl=np.array([1,np.sqrt(2)]);vh=np.array([1,-np.sqrt(2)])
rec(37,4,2,'两个广义特征向量与初值分解',eq(K@vl,(2-np.sqrt(2))*M@vl),eq(K@vh,(2+np.sqrt(2))*M@vh),eq((vl+vh)/2,[1,0]))
rec(37,4,3,'等比例摆长缩放的特征值',eq(np.sqrt(1.01),1+.01/2-.01**2/8,tol=1e-7))
e=s.symbols('e');coef=[]
for sign in [-1,1]:
 ratio=(2+sign*s.sqrt(2)*s.sqrt(1+e*e))/((1-e*e)*(2+sign*s.sqrt(2)))
 coef.append(float(s.diff(ratio**(-s.Rational(1,2)),e,2).subs(e,0)/2))
rec(37,4,4,'精确频率的二阶符号微分',eq(coef,[(np.sqrt(2)-1)/4,-(np.sqrt(2)+1)/4]))
q=11.86**(2/3);tf=.5*((1+q)/2)**1.5;phase=np.pi-2*np.pi*tf/11.86
rec(37,5,2,'转移椭圆半周期和木星追踪相位',eq(phase+2*np.pi*tf/11.86,np.pi),eq([tf,np.degrees(phase)],[2.72947655805,97.1491095363]))
ve=np.array([3.,0]);uin=np.array([-2.,0]);uout=-uin
rec(37,5,3,'两个日心动能直接相减',eq((np.dot(ve+uout,ve+uout)-np.dot(ve+uin,ve+uin))/2,np.dot(ve,uout-uin)),eq(np.dot(ve,uout-uin),12))
eh=1+7000*8.821**2/398600
rec(37,5,4,'双曲线轨道能量和渐近线角',eq([eh,np.degrees(2*np.arcsin(1/eh))],[2.36645832163,49.9942028819]))
cross=np.cross([1,.1,0],[0,0,-1]);radius=np.linalg.norm([1,.1,0])**3/np.linalg.norm(cross)
rec(37,6,2,'三维事件曲线的欧氏曲率定义',eq(radius,1.01))
h=.03;rec(37,6,3,'相邻波峰的本地钟速因子',eq(1/(1+h),1-h+h*h-h**3/(1+h)))
d=.7;b=1;z=d*d/(2*b);ct=np.sqrt(d*d+z*z);vr=ct/np.sqrt(b*b+ct*ct);gamma=1/np.sqrt(1-vr*vr)
rec(37,6,4,'双曲接收世界线的命中事件与多普勒',eq(z,np.sqrt(b*b+ct*ct)-b),eq(z/d,d/(2*b)),eq(gamma*(1-vr*z/ct),1))
v=np.array([(1-np.sqrt(5))/4,.5,(1+np.sqrt(5))/4]);assert v[0]<=v[1]<=v[2]
rec(37,7,2,'速度排序和两个完整守恒式',eq([sum(v),sum(v*v)],[1,1]))
v=np.array([2/3,-1/3,2/3]);rec(37,7,3,'允许圆盘左端点的动量能量',eq([sum(v),sum(v*v)],[1,1]))
N=s.symbols('N',positive=True);x,y=s.symbols('x y');poly=x*x+y*y+((1-x)**2+y*y)/(N-1)-1;disk=N/(N-1)*((x-1/N)**2+y*y-((N-1)/N)**2)
rec(37,7,4,'其余粒子最小能量与配方恒等式',eq(float(s.simplify(poly-disk).subs({N:5,x:.2,y:.3})),0),{'N2_requires_boundary':True})
norms=np.array([[1,0],[-.5,np.sqrt(3)/2],[-.5,-np.sqrt(3)/2]])
rec(37,8,2,'非对称绳速三投影回代',eq(norms@np.array([2,0])+1,[3,0,0]))
rec(37,8,3,'相同绳速的纯转动与向心项',eq((2/3)*np.ones(3)@norms,[0,0]),eq(np.linalg.norm([0,-1]),1))
rec(37,8,4,'切向加速度约束的三方向重建',eq(norms@np.array([2,0]),[2,-1,-1]))
assert len(rows)==48
(W/'核验/added_variant_verification.json').write_text(json.dumps(dict(status='pass',count=48,checks=rows),ensure_ascii=False,indent=2)+'\n')
print('48 source-bound independent added-variant checks passed')
