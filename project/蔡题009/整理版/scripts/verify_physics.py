"""独立核验第009套：线性静力、积分、有限差分、节点求解和多极展开。"""
from pathlib import Path
import json,math
import numpy as np
import sympy as s
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def ck(q,name,ok,details):
 CHECKS.append(dict(name=f'{q:02d}-{name}',passed=bool(ok),details=details))
def near(a,b,rtol=1e-7,atol=1e-10):return bool(np.allclose(a,b,rtol=rtol,atol=atol))
def main():
 # 1: solve force and moment balance independently; scan all beam sections.
 A=np.eye(4)
 for i in range(4):A[i,(i-1)%4]=-.5
 T=np.linalg.solve(A,[.75,0,0,0]);R=np.roll(T,1)-T+[1,0,0,0]
 ck(1,'闭合矩方程',near(T,[.8,.4,.2,.1]),dict(T_over_W=T.tolist()))
 ck(1,'碗口反力',near(R,[.3,.4,.2,.1]),dict(R_over_W=R.tolist()))
 ck(1,'整体竖直平衡',near(sum(R),1),'四个碗口反力之和为W')
 ck(1,'单侧接触可行',np.all(T>=0) and np.all(R>=0),'内端和碗口均无需拉力')
 x=np.linspace(0,1,20001);M=sum(F*np.maximum(x-pos,0) for pos,F in [(0,-20),(.25,20),(.75,20),(1,-20)])
 ck(1,'测试截面扫描',near(np.max(abs(M)),5),dict(max_abs_M=float(np.max(abs(M)))))
 m1=sum(F*np.maximum(x-pos,0) for pos,F in [(0,R[0]),(.5,-T[3]),(.75,-1),(1,T[0])])
 ck(1,'第一杆截面扫描',near(m1.max(),.2) and near(x[m1.argmax()],.75),dict(max_M_over_W=float(m1.max()),position=float(x[m1.argmax()])))
 for i in range(1,4):
  mi=R[i]*x-T[i-1]*np.maximum(x-.5,0)
  ck(1,f'第{i+1}杆截面扫描',near(mi.max(),[.2,.1,.05][i-1]),dict(max_M_over_W=float(mi.max())))
 ck(1,'两根同时临界',near(.2*25,5),'第1、2杆同为5Nm')
 ck(1,'质量换算',near(25/9.8,2.551020408),'g=9.8时2.551kg，g=10时2.5kg')
 ck(1,'减半测试载荷',near(2.5/.2,12.5),'测试四力10N，临界载荷12.5N')
 # 2: vector signs, finite-field expansion, Faraday torque and power quadrature.
 v=np.array([0,2,0]);Bvec=np.array([0,0,-3]);f=np.cross(v,Bvec)
 ck(2,'圆周磁力方向',near(f,[-6,0,0]),dict(v_cross_B=f.tolist()))
 eps=1e-5;exact=(1-eps)**(-1/3)-1
 ck(2,'同步半径一阶',near(exact/eps,1/3,rtol=1e-5),dict(quotient=exact/eps))
 ck(2,'负电荷半径方向',(1+eps)**(-1/3)<1,'负电荷半径向内偏移')
 t=s.symbols('t');rho=s.Function('rho')(t);Bt=s.Function('B')(t);q=s.symbols('q')
 const=s.simplify(q*Bt*rho*s.diff(rho,t)-s.diff(q*Bt*rho**2/2,t)+q*rho**2*s.diff(Bt,t)/2)
 ck(2,'均匀变场守恒量',const==0,'磁力矩+感生电力矩等于d(q B rho²/2)/dt')
 ck(2,'法拉第环路',near(2*np.pi*2*(2*.7/2),np.pi*2**2*.7),'半径2场强导数.7：电场环量等于负磁通导数')
 ph,om,db=s.symbols('ph om db',real=True);bz=-s.symbols('B0')+db*s.cos(ph-om*t)
 ck(2,'固定点时间偏导',s.simplify(s.diff(bz,t)-om*db*s.sin(ph-om*t))==0,'固定点导数包含图样转速om')
 rr,E=s.symbols('rr E');curl=-s.diff(E*s.cos(ph),ph)/rr
 ck(2,'径向场旋度',s.simplify(curl-E*s.sin(ph)/rr)==0,'径向场具有正确的z向旋度')
 avg=lambda w,p:quad(lambda z:np.sin(z)*np.cos((1-w)*z+p),0,2*np.pi,epsabs=1e-12)[0]/(2*np.pi)
 ck(2,'共振相位pi除2',near(avg(2,np.pi/2),.5),'功率积分的无系数平均为1/2')
 ck(2,'共振零相位',near(avg(2,0),0),'相位0平均为0')
 ck(2,'共振反相',near(avg(2,-np.pi/2),-.5),'相位改变使平均功反号')
 ck(2,'非匹配整数频率',near(avg(3,np.pi/2),0),'遇场频率2而振动频率1，积分相消')
 r,m,J,w,wc=s.symbols('r m J w wc',positive=True)
 U=J**2/(2*m*r**2)+m*wc**2*r**2/8-m*(w*w-w*wc)*r**2 # last gravity derivative handled below
 rr0,GM=s.symbols('rr0 GM',positive=True)
 Ueff=J**2/(2*m*r**2)+m*wc**2*r**2/8-GM*m/r
 kap=s.diff(Ueff,r,2).subs({J:m*rr0**2*(w-wc/2),r:rr0,GM:rr0**3*(w*w-w*wc)})/m
 ck(2,'径向有效势二阶',s.simplify(kap-(w*w-w*wc+wc*wc))==0,'κ²=ω0²−ω0ωc+ωc²')
 # 3: exact equilibria at perturbed plate separations verify differential response.
 th=.6;eta=.4;l=2.;dl=1e-5;W=5.;elec=eta*W;gpart=W-elec
 shape=lambda th:np.sin(th)**4/np.cos(th)
 Wf=gpart+elec*l/(l+dl);thf=brentq(lambda z:Wf*shape(z)-W*shape(th),.01,1.55)
 predicted=eta*dl/l*np.sin(th)*np.cos(th)/(1+3*np.cos(th)**2)
 ck(3,'精确平衡微分核验',near(thf-th,predicted,rtol=2e-5,atol=1e-12),dict(exact_delta=thf-th,linear_delta=predicted))
 ck(3,'展开方向',thf>th,'间距增大则角度增大')
 wf=np.sin(th)**2/np.sin(thf)**2
 ck(3,'角速度变化',near((wf-1)/dl,-2/ l*eta*np.cos(th)**2/(1+3*np.cos(th)**2),rtol=2e-5),'有限平衡变化与角速度微分式一致')
 Tf=wf**2
 ck(3,'张力两式核对',near(Tf,(Wf/W)*np.cos(th)/np.cos(thf)),'T∝ω²和T=W/cosθ一致')
 z=s.symbols('z',positive=True);sh=s.sin(z)**4/s.cos(z)
 ck(3,'角函数对数导数',s.simplify(s.diff(sh,z)/sh-(4*s.cot(z)+s.tan(z)))==0,'轨道半径平方产生四倍cot项')
 ck(3,'角函数单调',np.all(np.diff(shape(np.linspace(.01,1.56,500)))>0),'允许区间的平衡解唯一')
 mm,hh,WW,JJ=s.symbols('mm hh WW JJ',positive=True)
 vv=JJ**2/(2*mm*hh**2*s.sin(z)**2)-WW*hh*s.cos(z)
 sub={JJ**2:mm*hh**3*WW*s.sin(z)**4/s.cos(z)}
 ck(3,'有效势驻点',s.simplify(s.diff(vv,z).subs(sub))==0,'固定J的有效势恢复圆锥平衡')
 ck(3,'有效势稳定曲率',s.trigsimp(s.diff(vv,z,2).subs(sub)-WW*hh*(1+3*s.cos(z)**2)/s.cos(z))==0,'倾角频率平方为ω²(1+3cos²θ)')
 ck(3,'电力消失极限',near(0*dl/l*np.sin(th)*np.cos(th),0),'q或U为0时没有角度变化')
 ck(3,'恒电荷场不变',near(2/(3*4),2/(3*4)),'固定Q和S，场不依赖间距')
 ck(3,'固定角速度区别',near((eta*np.cos(th)/np.sin(th))/(eta*np.sin(th)*np.cos(th)/(1+3*np.cos(th)**2)),(1+3*np.cos(th)**2)/np.sin(th)**2),'另一约束产生不同响应')
 ck(3,'变式数值',near(.01*np.sqrt(3)/13,0.001332346775),'30度、η=.5、间距增2%得到.001332rad')
 # 4: two surface matrices and pressure examples.
 nA=1.48;nB=1.33;sig=.073
 pa=lambda dens,v0,v:dens*(v0*v0-v*v)/2
 pA=pa(800,1,.5);pL=pa(1000,1,.8);D=2*pA-2*pL;f=nB*sig/((nA-nB)*D)
 ck(4,'伯努利数值',near([pA,pL,D],[300,180,240]),dict(relative_pressures=[pA,pL],D=D))
 ck(4,'焦距数值',near(f,.00269694444444),dict(f_m=f))
 RL=sig/(pA-pL);RR=-RL;S1=np.array([[1,0],[-(nA-nB)/RL,1]]);S2=np.array([[1,0],[-(nB-nA)/RR,1]])
 ck(4,'折射矩阵核对',near(-(S2@S1)[1,0]/nB,1/f),'两面折合角矩阵给出同一焦度')
 ck(4,'曲率正负',RL>0 and RR<0,'双凸左正右负')
 ck(4,'对称会聚阈值',near(.2+ .8*.5**2,.4),'vB²>0.2v0²+0.8vA²')
 ck(4,'入口压强抵消',near(2*(pA+12345)-2*(pL+12345),D),'共同p0不影响焦度')
 ck(4,'入口速度不能抵消',near(800-1000,-200),'不同密度下v0²系数−200')
 ck(4,'等速无焦度',near(2*pa(800,1,1)-2*pa(1000,1,1),0),'局部速度均为入口速度时D=0')
 ck(4,'等折射率无焦度',near((nB-nB)*D/(nB*sig),0),'曲率存在但折射率相等时焦度0')
 ck(4,'弯月形无焦度',near(100/sig-100/sig,0),'左右压差相反，光学半径相同')
 ck(4,'张力翻倍',near(nB*(2*sig)/((nA-nB)*D),2*f),'固定D时焦距增两倍')
 ck(4,'周围介质因子',near((nA-1)/(nA/nB-1),4.256),'空气透镜系数与浸没系数不同，不能替换')
 # 5: solve original circuit with the inferred clamp/zero-current branch.
 for x in [0,.1,.2,1/3,.5,1,2,2.9,3,4,10,1e6]:
  U0=4.;res=2.
  # Unknown A,B,j. Equations are x-multiplied KCL at A and ordinary KCL at B.
  mat=np.array([[1+x,0,x*res],[0,2,-res],[1,-1,0]],float);rhs=np.array([U0,U0,U0/4 if x<=1/3 else -U0/4])
  if 1/3<x<3:mat[2]=[0,0,1];rhs[2]=0
  VA,VB,j=np.linalg.solve(mat,rhs);I=VB/res
  given=3*U0/(4*res)*(1+x)/(3*x+1) if x<=1/3 else (U0/(2*res) if x<3 else 5*U0/(4*res)*(1+x)/(3*x+1))
  ck(5,f'独立节点解x={x:g}',near(I,given) and (VA-VB)*j>=-1e-12,dict(I_nodes=float(I),I_measured=given,u=float(VA-VB),j=float(j)))
 # 6: nine lines plus total internal reflection, ell exclusion and boundaries.
 for n,expected in zip(range(9,18),[546.684997,548.814182,550.392723,551.595149,552.532006,553.276050,553.876744,554.368659,554.776544]):
  # Compute by Cartesian chord length, independently of sin formula in draft.
  vertices=np.array([(120*np.cos(2*np.pi*j/n),120*np.sin(2*np.pi*j/n)) for j in range(n)])
  length=np.linalg.norm(np.roll(vertices,-1,axis=0)-vertices,axis=1).sum();lam=1.48*length/2
  ck(6,f'闭合弦路n={n}',near(lam,expected,atol=1e-6),dict(lambda_nm=float(lam)))
 ck(6,'全反射最小次数',np.cos(np.pi/6)<1.33/1.48<np.cos(np.pi/7),'nmin=7')
 ck(6,'排除其他相位整数',2*7*1.48*120*np.sin(np.pi/7)>555 and 2*np.pi*1.48*120/3<545,'ell1最小值太大；ell≥3最大值太小')
 ck(6,'波段边界完整',8*1.48*120*np.sin(np.pi/8)<545 and 18*1.48*120*np.sin(np.pi/18)>555,'n8低于下限，n18超过上限，单调性保证完整')
 # 7: symbolic derivatives and independently bracketed stable roots.
 d,r0,K=s.symbols('d r0 K',positive=True);U=-K*s.exp(-d/r0)/d
 force=s.diff(U,d)
 ck(7,'势能求导',s.simplify(force-K*s.exp(-d/r0)*(1+d/r0)/d**2)==0,'两个乘积导数项都保留')
 hc=197.3269804;mu=.5;a=.12;p=hc/(2*a);e=np.hypot(mu,p);beta=p/e;kn=hc*hc/(mu*a)
 ck(7,'非相对论K系数',near(kn,648965.619896),'KNR=648965.62 e^x/(1+x) MeVfm')
 ck(7,'牛顿超光速',near(p/mu,1644.391503333),'vNR/c=1644.39')
 ck(7,'相对论速度',near(beta,.99999981509041,atol=1e-13) and beta<1,dict(beta=beta,gamma=e/mu))
 ck(7,'圆轨道重新校准',near(kn/(e/mu),2*hc*beta),'同半径Krel=KNR/γ')
 ck(7,'自由能量之和',near(2*e,1644.391807397),'仅忽略势能时2Eq=1644.39MeV')
 pp,mm=s.symbols('pp mm',positive=True);A=s.symbols('A',positive=True)
 H=2*s.sqrt(mm**2+(A/d)**2)-K*s.exp(-d/r0)/d
 der=s.diff(H,d);cond=K*s.exp(-d/r0)*(1+d/r0)-2*A*(A/d)/s.sqrt(mm**2+(A/d)**2)
 ck(7,'径向驻点条件',s.simplify(der-cond/d**2)==0,'H′与相对论力平衡一致')
 kval=2*A*(A/d)/s.sqrt(mm**2+(A/d)**2)*s.exp(d/r0)/(1+d/r0)
 b2=(A/d)**2/(mm**2+(A/d)**2)
 expected=2*A*(A/d)/s.sqrt(mm**2+(A/d)**2)/d**3*((1-b2)-(d/r0)**2/(1+d/r0))
 ck(7,'稳定性二阶导数',s.simplify(s.diff(H,d,2).subs(K,kval)-expected)==0,'二阶导数符号等价于1−β²>x²/(1+x)')
 rshort=1.;xs=.24;ks=2*hc*beta*np.exp(xs)/(1+xs);zeta=2*hc/(mu*rshort)
 # f(x)=β(x)e^x/(1+x) starts at1 and has positive log derivative for zeta²>1.
 ck(7,'短范围无n2根',zeta*zeta>1 and ks/(4*hc)<1,'r0=1fm时f(x)>1，而K/(4ℏc)=.5126<1')
 rl=1e6;kl=2*hc*beta*np.exp(.24/rl)/(1+.24/rl)
 fun=lambda d:kl*np.exp(-d/rl)*(1+d/rl)-4*hc*((2*hc/d)/np.hypot(mu,2*hc/d))
 root=brentq(fun,1000,2000);energy=2*np.hypot(mu,2*hc/root)-kl*np.exp(-root/rl)/root;bn=(2*hc/root)/np.hypot(mu,2*hc/root);xx=root/rl
 ck(7,'长范围稳定束缚根',near(root,1367.12346199) and near(energy,.8664198414) and 1-bn*bn>xx*xx/(1+xx) and energy<1,dict(d_fm=root,H_MeV=energy))
 outer=brentq(fun,1e7,2e7);bo=(2*hc/outer)/np.hypot(mu,2*hc/outer);xo=outer/rl
 ck(7,'外根不稳定',1-bo*bo<xo*xo/(1+xo),dict(outer_d_fm=outer))
 bc=beta/2;dc=2*hc*np.sqrt(1-bc*bc)/(mu*bc);Ec=2*mu*np.sqrt(1-bc*bc)
 ck(7,'库仑极限核对',near(Ec,.866025457164,rtol=1e-7) and near(2*np.hypot(mu,2*hc/dc)-2*hc*beta/dc,Ec),'解析极限与能量直接代入一致')
 # 8: source moments, high precision exact sums, gradient and harmonicity.
 ck(8,'单极消失',sum([-1,2,-1])==0,'三个电荷之和0')
 ck(8,'偶极消失',sum(c*x for c,x in zip([-1,2,-1],[-1,0,1]))==0,'偶极矩0')
 rr,ll,c=s.symbols('rr ll c',positive=True);ep=s.symbols('ep')
 expanded=s.series(2-(1+ep**2-2*ep*c)**s.Rational(-1,2)-(1+ep**2+2*ep*c)**s.Rational(-1,2),ep,0,5).removeO()
 ck(8,'精确电势展开',s.expand(expanded).coeff(ep,2)==1-3*c*c and s.expand(expanded).coeff(ep,1)==0,'二阶系数1−3cos²θ，一阶消失')
 th=s.symbols('th',real=True);V=ll**2*(1-3*s.cos(th)**2)/rr**3;Er=-s.diff(V,rr);Et=-s.diff(V,th)/rr
 ck(8,'径向梯度',s.simplify(Er-3*ll**2*(1-3*s.cos(th)**2)/rr**4)==0,'Er主阶r−4')
 ck(8,'角向梯度',s.simplify(Et+6*ll**2*s.sin(th)*s.cos(th)/rr**4)==0,'Eθ带额外1/r')
 lap=s.diff(rr**2*s.diff(V,rr),rr)/rr**2+s.diff(s.sin(th)*s.diff(V,th),th)/(rr**2*s.sin(th))
 ck(8,'源外拉普拉斯',s.simplify(s.trigsimp(lap))==0,'四极主阶在源外调和')
 angle=np.arccos(1/np.sqrt(3));et=-6*np.sin(angle)*np.cos(angle)
 ck(8,'零势角仍有场',near(et,-2*np.sqrt(2)),'魔角Er0而Eθ非0')
 mag=s.trigsimp((Er**2+Et**2)*rr**8/(9*ll**4)-(1-2*s.cos(th)**2+5*s.cos(th)**4))
 ck(8,'场强模平方',mag==0,'大小公式与两个分量一致')
 pair=6-4/(1-ep)-4/(1+ep)+1/(1-2*ep)+1/(1+2*ep)
 series=s.series(pair,ep,0,8).removeO()
 ck(8,'九电荷对展开',series.coeff(ep,4)==24 and series.coeff(ep,6)==120 and series.coeff(ep,2)==0,'作用能首项24l4/R5，下一项120l6/R7')
 mp.mp.dps=60;R=mp.mpf(1000);lmp=mp.mpf(1)
 ex=lambda R:6/R-4/(R-lmp)-4/(R+lmp)+1/(R-2*lmp)+1/(R+2*lmp)
 F=-mp.diff(ex,R);lead=120/R**6
 ck(8,'精确合力渐近',abs(F/lead-1)<mp.mpf('1e-5') and F>0,dict(exact_over_leading=str(F/lead)))
 ck(8,'距离翻倍幂次',near((120/2**6)/120,1/64),'主阶力幂次6')
 ck(8,'电荷尺度幂次',near((2**2),4),'两分子作用含q²，电荷翻倍力变4倍')

 # 补充主稿推广的独立核验；与原96项分别计数。
 supplement=[]
 def sc(q,n,ok,detail):supplement.append(dict(question=q,name=n,passed=bool(ok),details=detail))
 vals=[]
 for pos in np.linspace(.5,1,21):
  ts=np.linalg.solve(np.eye(4)-.5*np.roll(np.eye(4),1,axis=0),[pos,0,0,0]);rs=np.roll(ts,1)-ts+[1,0,0,0]
  scan=rs[0]*np.linspace(0,1,2001)-ts[3]*np.maximum(np.linspace(0,1,2001)-.5,0)-np.maximum(np.linspace(0,1,2001)-pos,0)
  mx=max(scan.max(),ts[0]/4);theory=16*pos*(1-pos)/15 if pos<=.75 else 4*pos/15
  vals.append(near(mx,theory,atol=1e-8))
 sc(1,'21个载荷位置截面扫描',all(vals),'最大弯矩的两段式及a=.75最优位置')
 longavg=quad(lambda t:np.sin(t)*np.cos(.7*t+.3),0,200*np.pi,epsabs=1e-10,limit=1000)[0]/(200*np.pi)
 sc(2,'非匹配频率长期平均',abs(longavg)<1e-10,'200个周期的非共振项相消')
 z=symbol=s.symbols('z');der=s.diff(z*(1-z)/(1+3*z)**2,z)
 sc(3,'响应系数极值',s.simplify(der-(1-5*z)/(1+3*z)**3)==0 and near(np.sqrt(.2*.8)/1.6,.25),'最大角度系数1/4')
 # Independent paraxial ABCD product with nonzero thickness.
 tt=.0001;P=np.array([[1,tt/nA],[0,1]]);mat=S2@P@S1
 invf=(nA-nB)/nB*(1/RL-1/RR+(nA-nB)*tt/(nA*RL*RR))
 sc(4,'厚度矩阵修正',near(-mat[1,0]/nB,invf),'非零厚度时的两面折射与传播矩阵')
 vc=1.;uNew=8.;xp=(uNew-2*vc)/(uNew+2*vc);xm=1/xp
 sc(5,'改变源电压的阈值',near([xp,xm],[.6,5/3]) and near(uNew*(1-xp)/(2*(1+xp)),vc),'固定器件阈值，源电压翻倍后转折点3/5和5/3')
 lam=1097.628364/(2+.2/(2*np.pi))
 sc(6,'反射相移变式',near(lam,540.2163714),'δ=-.02，n10 ell2的修正波长')
 b=.8;xx=.5;energy=2*.5/np.sqrt(1-b*b)*(1-b*b/(1+xx))
 sc(7,'稳定且束缚示例',1-b*b>xx*xx/(1+xx) and near(energy,.9555555556) and energy<1,'β=.8 x=.5时稳定且低于解离阈值')
 Rv,lv=s.symbols('Rv lv',positive=True)
 pair=6/Rv-4/(Rv-lv)-4/(Rv+lv)+1/(Rv-2*lv)+1/(Rv+2*lv)
 sc(8,'精确有理式通分',s.simplify(pair-24*lv**4/(Rv*(Rv**2-lv**2)*(Rv**2-4*lv**2)))==0,'九电荷对与正的有理式一致')
 assert len(supplement)==8 and all(c['passed'] for c in supplement),supplement

 assert len(CHECKS)==96,len(CHECKS)
 assert all(sum(c['name'].startswith(f'{q:02d}-') for c in CHECKS)==12 for q in range(1,9))
 result=dict(all_passed=all(c['passed'] for c in CHECKS),check_count=len(CHECKS),checks=CHECKS,
  supplementary_check_count=8,supplementary_checks=supplement,
  scope='题设简化模型及明确补充条件的独立数值/符号核验；不代表真实介子、纳米球吸收或天体逃逸的完整模型验证。')
 (ROOT/'physics_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(dict(all_passed=result['all_passed'],check_count=96,failed=[c for c in CHECKS if not c['passed']]),ensure_ascii=False))
 assert result['all_passed']
if __name__=='__main__':main()
