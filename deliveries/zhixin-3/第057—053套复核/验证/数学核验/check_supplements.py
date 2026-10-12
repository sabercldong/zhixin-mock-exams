"""Independent replay for the extra proofs, examples and numerical branch conditions."""
from pathlib import Path
import hashlib,json
import sympy as s
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
P=Path(__file__).parent;checks=[]
def check(name,condition):
 assert bool(condition),name
 checks.append(dict(name=name,passed=True))
def zero(v):return s.simplify(v)==0
def near(a,b,tol=1e-8):return np.allclose(a,b,atol=tol,rtol=tol)
x,z,a,b,J,m,r,u,L=s.symbols('x z a b J m r u L',positive=True)
# Equal-mass pulley fourth-order correction, with mass transformation done independently.
vp=-s.sqrt((1+x)**2-s.Rational(1,4));vm=vp.subs(x,-x)
pot=s.series(vp+vm+s.sqrt(3),x,0,6).removeO()
mass=s.series(s.diff(vp,x)**2+s.diff(vm,x)**2,x,0,4).removeO()
coord=x+s.Rational(13,54)*x**3
newpot=s.series(pot.subs(x,z-s.Rational(13,54)*z**3),z,0,6).removeO()
check('057Q2_常质量四次势能',zero(newpot.coeff(z,4)-76/(81*s.sqrt(3))))
check('057Q2_首阶频移',zero(3*newpot.coeff(z,4)/(4*newpot.coeff(z,2))-s.Rational(19,18)))
root=brentq(lambda v:2-3*v-v**3,0,1)
check('057Q1_不等质量极值',near(root,.5960716379833215))
check('057Q3_冲击耗散符号',all(-(1-e*e)*v*v/(2*(1+rr*rr))<=0 for e in [0,.4,1] for v in [-2,1] for rr in [.2,1]))
check('057Q5_平衡线性增长率',zero(s.diff(1-1/x**2,x).subs(x,1)-2))
check('057Q7_奇异等温球',zero((3*(2/r)/r+s.diff(2/r,r))-4/r**2))
tt=s.symbols('tt',positive=True);ww=tt+1-x-tt/x
check('056Q2_最大功及效率',zero(ww.subs({tt:4,x:2})-1) and zero((1-1/x).subs(x,2)-s.Rational(1,2)))
check('056Q2_TS面积',zero(s.integrate(s.exp(z),(z,0,s.log(2)))-1))
check('056Q3_不等长停止条件',zero(1-3*x+2*(1-s.Rational(7,2)*x)-(3-10*x)))
check('056Q3_变长停止位移',near((1-3*.32)/(3.5*.32-1),1/3))
times=np.array([2/np.sqrt(.13),2/(np.sqrt(.13)+np.sqrt(.115)),2*np.sqrt(.115)/(77/300)])
check('056Q3_停止时间逐段位移',near(.5*np.sqrt(.13)*times[0],1) and near(.5*(np.sqrt(.13)+np.sqrt(.115))*times[1],1) and near(.5*np.sqrt(.115)*times[2],69/154))
check('056Q1_平衡势能与小振动',zero((-s.Rational(3,2)*a*a+a*b).subs(b,3*a/2)) and zero((b/6)/(b*b/9)-3/(2*b)))
check('056Q4_一般中心二阶张量',all(near(sum(np.outer([np.cos(th),np.sin(th)],[np.cos(th),np.sin(th)])for th in 2*np.pi*np.arange(n)/n),np.eye(2)*n/2) for n in [3,4,5,2020]))
check('056Q5_双回路正定性',np.linalg.eigvalsh([[1,.5],[.5,1]]).min()>0)
check('056Q6_负boost数值',near((.4+.2)/(1+.08),5/9))
D1=1-s.sqrt(3);D2=1-s.sqrt(3)/2
B12=(-s.sqrt(3)/D1)/(1-s.sqrt(3)/(2*D1))
B21=(-s.sqrt(3)/D2)/(1-s.sqrt(3)/D2)
check('056Q7_B两种次序',zero(B12-B21) and zero(B12-(18+4*s.sqrt(3))/23))
F=(s.sqrt(3)*x+2)/(s.sqrt(3)*x+3)
check('056Q8_递推误差不反号',zero(s.diff(F,x)-s.sqrt(3)/(s.sqrt(3)*x+3)**2))
check('055Q2_精确波长差',zero((2/(s.sqrt(x*x+1)+x))**2/4+x*2/(s.sqrt(x*x+1)+x)-1))
check('055Q3_平行投影极限',zero(s.limit((1-s.cos(z))/s.sin(z),z,0)))
LP=s.Matrix([[1,0],[1,1]])*s.Matrix([[1,x],[0,1]])*s.Matrix([[1,0],[-1,1]])
check('055Q5_双镜间距矩阵',LP==s.Matrix([[1-x,x],[-x,1+x]]))
check('055Q6_球内简谐时间',near(quad(lambda v:1/np.sqrt(1-v*v),0,1)[0],np.pi/2))
zg=1/x**2+(1-1/x**2)*s.cos(x*z)
check('055Q6_含重力轨迹与中心速度',zero(s.diff(zg,z,2)-(1-x*x*zg)) and zero(zg.subs(z,0)-1) and zero(s.diff(zg,z).subs(z,0)) and zero(x*x*(1-1/x**2)**2-1/x**2-(x*x-2)) and zero((x*x-2).subs(x,s.sqrt(2))))
check('055Q7_冲击中心',zero((3*x/2-1).subs(x,s.Rational(2,3))))
check('055Q8_同时事件钟读数',all(near((1/(1-v*v))/np.sqrt(1/(1-v*v)),1/np.sqrt(1-v*v))for v in [.2,.6,.8]))
sa=s.sqrt(3)/2;ca=s.Rational(1,2);mom=s.symbols('mom',real=True)
omega=(mom-m*r*sa*u)/(J+m*r*r);vr=ca*u;vtheta=sa*u+omega*r
E=s.simplify(m*(vr*vr+vtheta*vtheta)/2+J*omega*omega/2)
check('054Q1_带非零角动量有效动能',zero(E-(mom*mom/(2*(J+m*r*r))+m*u*u*(ca*ca+J*sa*sa/(J+m*r*r))/2)))
mods=json.loads((P/'collision_models.json').read_text())
check('054Q2_三模型无提前车身接触',all(q['body_min_clearance']>1.67 and q['front_min_clearance']>0 for q in mods.values()))
check('054Q3_小循环展开',zero(s.limit((x-s.log(1+x))/(x*x),x,0)-s.Rational(1,2)))
check('054Q4_格点二阶惯量',near(np.mean(np.array([-3,-1,1,3],float)**2)/64,5/64))
check('054Q6_圆轨道平均修正',zero((-s.Rational(1,2)*(1-s.Rational(3,4)))+s.Rational(1,8)))
check('054Q8_转矩峰值例',zero(((a*a-b*b)/(2*a*b)).subs(b,a/2)-s.Rational(3,4)))
ev=2/5;A=5/14;C=1/7;B=np.sqrt(21)/14
for angle in [.2,1,2.8]:
 X=C+A*np.cos(angle);Y=-B*np.sin(angle)
 assert near(np.hypot(X,Y),A*(1+ev*np.cos(angle)))
check('053Q1_时间参数与径向距离',True)
check('053Q2_黏性稳态耗散',zero(s.integrate((1-s.Rational(3,2)*x)**2,(x,0,1))-s.Rational(1,4)))
power=x**3/(2*(x*x+1)**2)
check('053Q4_外电阻功率最大值',zero(s.diff(power,x).subs(x,s.sqrt(3))))
f=1+2*x-3*x*x
check('053Q5_区间与通量抽样',zero(s.integrate(f,(x,s.Rational(1,4),s.Rational(3,4)))-s.Rational(19,32)) and zero(s.Rational(12,5)*s.integrate(x*x*f,(x,0,1))-s.Rational(14,25)))
be=s.symbols('be',positive=True);q=(1+be)/(1-be)
check('053Q6_反射时间几何和',zero(2/(1+be)/(1-1/q)-1/be))
check('053Q6_半距台阶',near((11/9)**3,1.8257887517) and near((1.01/.99)**34,1.973922476,1e-7))
check('053Q7_两种放置视深极限',zero(s.limit((3*x/(3*x-4))/x,x,0)+s.Rational(3,4)) and zero(s.limit((3*x/(x-4))/x,x,0)+s.Rational(3,4)))
fB=1-s.Rational(5,6)*x+x*x/2-x**3/6
check('053Q8_半时半速',zero(fB.subs(x,1)-s.Rational(1,2)) and zero(-s.diff(fB,x).subs(x,1)-s.Rational(1,3)))
result=dict(passed=True,groups=checks,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'supplement_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('PASS',len(checks),'supplement groups')
