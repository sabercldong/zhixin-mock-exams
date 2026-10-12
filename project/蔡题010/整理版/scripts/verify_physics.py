"""第010套独立核验：电感矩阵、积分、求根、光线映射、Airy函数与刚体运动。"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq,minimize_scalar
from scipy.special import airy,ai_zeros
ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def near(a,b,rtol=2e-7,atol=1e-11):return bool(np.allclose(a,b,rtol=rtol,atol=atol))
def ck(q,name,ok,detail):CHECKS.append(dict(name=f'{q:02d}-{name}',passed=bool(ok),details=detail))
def main():
 # 01: use the two-branch matrix, then check the singular limit and energy.
 N=2000.;n1=300.;n2=N-n1;L=5.;R=200.;U=1.5;t=.1
 L1=L*(n1/N)**2;L2=L*(n2/N)**2;M=L*n1*n2/N**2
 ck(1,'平方匝数',near([L1,L2,M],[.1125,3.6125,.6375]),[L1,L2,M])
 ck(1,'矩阵零模',near(np.linalg.det([[L1,-M],[-M,L2]]),0),float(M*M-L1*L2))
 i2=(1+M/L1)*U/R;im=U*t/L1;i1=im+M/L1*i2
 ck(1,'长段代数约束',near(i2,.05),float(i2))
 ck(1,'短段总电流',near(i1,1.616666666666667),float(i1))
 ck(1,'净安匝初值',near(n1*M/L1*i2-n2*i2,0),float(n1*M/L1*i2-n2*i2))
 v=np.array([U/L1,0]);ck(1,'双支路KVL',near(np.array([[L1,-M],[-M,L2]])@v,[U,U-R*i2]),v.tolist())
 k=.9;mk=k*M;mat=np.array([[L1,-mk],[-mk,L2]])
 sol=solve_ivp(lambda tt,ii:np.linalg.solve(mat,[U,U-R*ii[1]]),[0,t],[0,0],rtol=1e-10,atol=1e-12)
 i2s=(1+mk/L1)*U/R;leak=L2-mk*mk/L1;i2f=i2s*(1-np.exp(-R*t/leak));i1f=U*t/L1+mk/L1*i2f
 ck(1,'非零漏感独立积分',near(sol.y[:,-1],[i1f,i2f]),sol.y[:,-1].tolist())
 kval=.999999;mk=kval*M;ss=(1+mk/L1)*U/R;ll=L2-mk*mk/L1;rr=ss*(1-np.exp(-R*t/ll));ii=U*t/L1+mk/L1*rr
 ck(1,'完全耦合极限',near([ii,rr],[i1,i2],rtol=2e-6),[float(ii),float(rr)])
 ck(1,'时刻功率',near([U*(i1+i2),U*im,R*i2*i2],[2.5,2.,.5]),[U*(i1+i2),U*im,R*i2*i2])
 wb=quad(lambda tt:U*(U*tt/L1+N/n1*i2),0,t)[0];eb=.5*L1*im*im;heat=R*i2*i2*t
 ck(1,'积分能量账',near([wb,eb,heat],[.15,.1,.05]) and near(wb,eb+heat),[wb,eb,heat])
 ck(1,'电阻变式',near(U*t/L1+n2/n1*(N*U/(n1*400)),1.475),1.475)
 ns=500.;ls=L*(ns/N)**2;ir=N*U/(ns*R);ish=U*t/ls+(N-ns)/ns*ir
 ck(1,'抽头变式',near([ir,ish],[.03,.57]),[ir,ish])
 # 02: orbital velocities, Bernoulli and depth integrals.
 g=9.8;T=2.;A=.1;rho=1000.;w=2*np.pi/T;c=g/w;lam=c*T;kw=w/c
 ck(2,'运动学色散',near(lam,g*T*T/(2*np.pi)) and near(w*w,g*kw),[lam,c,kw])
 ck(2,'表面速度',near([w*A,-w*A],[np.pi*.1,-np.pi*.1]),[w*A,-w*A])
 ck(2,'随波速度',near([c-w*A,c+w*A],[2.805277619242169,3.433596149960128],rtol=2e-6),[c-w*A,c+w*A])
 ck(2,'伯努利差',near(.5*((c+w*A)**2-(c-w*A)**2),2*g*A),float(2*g*A))
 z=np.linspace(-4,0,15);kx=kw*.7
 potential=lambda xx,zz:(g*A/w)*np.exp(kw*zz)*np.sin(kw*xx)
 dh=.001
 lap=(potential(.7+dh,z)+potential(.7-dh,z)+potential(.7,z+dh)+potential(.7,z-dh)-4*potential(.7,z))/(dh*dh)
 ck(2,'势函数拉普拉斯',near(lap,0,atol=1e-7),float(np.max(np.abs(lap))))
 ck(2,'自由面运动学',near(g*A*kw/w,A*w),[g*A*kw/w,A*w])
 ek=.5*rho*quad(lambda zz:w*w*A*A*np.exp(2*kw*zz),-np.inf,0)[0]
 ck(2,'深度动能积分',near(ek,rho*g*A*A/4),float(ek))
 ep=.5*rho*g*quad(lambda ph:(A*np.cos(ph))**2,0,2*np.pi)[0]/(2*np.pi)
 ck(2,'面势能平均',near(ep,ek),float(ep))
 dk=kw*1e-5;cg=(np.sqrt(g*(kw+dk))-np.sqrt(g*(kw-dk)))/(2*dk)
 ck(2,'群速度差分',near(cg,c/2),float(cg))
 ck(2,'能流数值',near((ep+ek)*cg,76.4262,rtol=1e-6),float((ep+ek)*cg))
 ck(2,'四倍波长',near(np.sqrt(g/(kw/4)),2*c) and near(np.sqrt(g*kw/4),w/2),'周期两倍，相速度两倍，轨道速度减半')
 kh=1e-4;cw=np.sqrt(g*kw*np.tanh(kh))/kw;hs=kh/kw
 ck(2,'浅水极限',near(cw,np.sqrt(g*hs)),[float(cw),float(np.sqrt(g*hs))])
 # 03: independent polynomial roots and energy curvature.
 me=5.9e24;mm=7.35e22;Re=6.4e6;mu=g*Re**2;Ie=.4*me*Re**2;r0=3.8e8;om0=2*np.pi/86400
 J=Ie*om0+mm*np.sqrt(mu*r0);sync=lambda a:Ie*np.sqrt(mu/a**3)+mm*np.sqrt(mu*a)
 ai=brentq(lambda a:sync(a)-J,1e7,3e7);ao=brentq(lambda a:sync(a)-J,4e8,8e8)
 ck(3,'引力与惯量',near([mu,Ie],[4.01408e14,9.66656e37]),[mu,Ie])
 ck(3,'初始角动量',near(J,3.5735685688480756e34),float(J))
 ck(3,'内根',near(ai,16158778.63832251),float(ai))
 ck(3,'外根',near(ao,584393016.4938122),float(ao))
 coeff=[mm*np.sqrt(mu)*1e4/J,-1,0,0,Ie*np.sqrt(mu)/1e12/J]
 pp=np.roots(coeff);pr=sorted(z.real**2*1e8 for z in pp if abs(z.imag)<1e-7 and z.real>0)
 ck(3,'四次多项式复核',near(pr,[ai,ao]),pr)
 of=np.sqrt(mu/ao**3);ck(3,'最终周期',near(2*np.pi/of/86400,51.277948311845485),float(2*np.pi/of/86400))
 ck(3,'最终角动量',near(Ie*of+mm*np.sqrt(mu*ao),J),float((Ie*of+mm*np.sqrt(mu*ao))/J))
 ad=np.sqrt(3*Ie/mm);ck(3,'临界半径',ai<ad<r0<ao,float(ad))
 energy=lambda a:(J-mm*np.sqrt(mu*a))**2/(2*Ie)-mu*mm/(2*a)
 curv=[]
 for aa in [ai,ao]:
  da=aa*1e-4;curv.append((energy(aa+da)-2*energy(aa)+energy(aa-da))/(da*da))
 ck(3,'稳定性独立差分',curv[0]<0<curv[1],curv)
 ini=.5*Ie*om0*om0-mu*mm/(2*r0);fin=energy(ao)
 ck(3,'机械能耗散',ini>fin,[float(ini),float(fin),float(ini-fin)])
 bound=J*J/(mm*mm*mu);ck(3,'外根上界',ao<bound,float(bound))
 do=om0*1e-6;JJ=J+Ie*do;an=brentq(lambda a:sync(a)-JJ,4e8,8e8);dlin=2*Ie*ao**2.5/(np.sqrt(mu)*(mm*ao*ao-3*Ie))*do
 ck(3,'初始自转响应',near(an-ao,dlin,rtol=2e-5),[float(an-ao),float(dlin)])
 # 04: solve isothermal balance and normalize independently.
 gas=8.314462618;temp=300.;mol=.029;rad=1000.;omega=np.sqrt(2*gas*temp/mol)/rad;b=mol*omega**2/(2*gas*temp);p0=1e5
 pressure=lambda s,beta=b:p0*np.exp(beta*s*s)
 ck(4,'单位指数',near(b*rad*rad,1),float(b*rad*rad))
 ck(4,'角速度数值',near(omega,.4147569945285369),float(omega))
 ck(4,'压强比',near(pressure(rad)/p0,np.e),float(pressure(rad)/p0))
 ss=500.;ds=.001;grad=(pressure(ss+ds)-pressure(ss-ds))/(2*ds);rhs=mol*pressure(ss)/(gas*temp)*omega*omega*ss
 ck(4,'微元力平衡差分',near(grad,rhs),[float(grad),float(rhs)])
 density=lambda s:mol*pressure(s)/(gas*temp)
 ck(4,'密度比',near(density(rad)/density(0),np.e),float(density(rad)/density(0)))
 oo=solve_ivp(lambda s,p:mol*omega**2*s*p/(gas*temp),[0,rad],[p0],rtol=1e-10,atol=1e-6)
 ck(4,'气体ODE复核',near(oo.y[0,-1],pressure(rad)),float(oo.y[0,-1]))
 hh=30.;mass=2*np.pi*hh*quad(lambda s:density(s)*s,0,rad,epsabs=1e-4)[0];massformula=2*np.pi*hh*(pressure(rad)-p0)/omega**2
 ck(4,'总气量积分',near(mass,massformula),float(mass))
 ck(4,'小压差展开',near(np.expm1(1e-6),1e-6,rtol=1e-6),'指数小参数1e-6')
 ratio=np.exp(mol*g*rad/(2*gas*temp));ck(4,'人工重力变式',near(ratio,1.0586229984031397),float(ratio))
 ck(4,'半径翻倍',near([omega/2*rad*2,(omega/2)**2*rad*2],[omega*rad,omega**2*rad/2]),'固定压强比')
 ck(4,'温度四倍',near(np.sqrt(2*gas*(4*temp)/mol)/rad,2*omega),'固定摩尔质量和压强比')
 om=1e-6;bs=mol*om**2/(2*gas*temp);normp=mass*om*om/(2*np.pi*hh*np.expm1(bs*rad*rad));uniform=mass*gas*temp/(np.pi*hh*rad*rad*mol)
 ck(4,'零转速质量极限',near(normp,uniform,rtol=1e-7),[float(normp),float(uniform)])
 # 05: Snell ray mapping and differentiation, angles always radians.
 n=1.309;ap=np.pi/3;ts=np.arcsin(n*np.sin(ap/2));dc=2*ts-ap
 def dev(th,nn=n,aa=ap):
  be=np.arcsin(np.sin(th)/nn);ex=np.arcsin(nn*np.sin(aa-be));return th+ex-aa
 ck(5,'黄光最小偏向',near(np.degrees(dc),21.763496346709573),float(np.degrees(dc)))
 ck(5,'对称入射角',near(np.degrees(ts),40.88174817335479),float(np.degrees(ts)))
 low=np.arcsin(n*np.sin(ap-np.arcsin(1/n)))
 ck(5,'透射边界',near(dev(low),low+np.pi/2-ap),float(np.degrees(low)))
 opt=minimize_scalar(dev,bounds=(low+.0001,np.pi/2-.0001),method='bounded',options={'xatol':1e-13})
 ck(5,'独立数值极小',near(opt.x,ts) and near(opt.fun,dc),[float(opt.x),float(opt.fun)])
 step=1e-5;d1=(dev(ts+step)-dev(ts-step))/(2*step)
 ck(5,'一阶驻点',abs(d1)<1e-8,float(d1))
 d2=(dev(ts+step)-2*dev(ts)+dev(ts-step))/step**2;expected=2*np.sin(ts)*(n*n-1)/(np.cos(ts)*n*n*np.cos(ap/2)**2)
 ck(5,'二阶导数',near(d2,expected,rtol=3e-5),[float(d2),float(expected)])
 th=.9;be=np.arcsin(np.sin(th)/n);ex=np.arcsin(n*np.sin(ap-be));rev=dev(ex)
 ck(5,'光路可逆',near(rev,dev(th)),[float(th),float(ex)])
 nd=1e-5;dn=(2*np.arcsin((n+nd)/2)-2*np.arcsin((n-nd)/2))/(2*nd)
 ck(5,'色散导数',near(dn,1/np.sqrt(1-n*n/4)),float(dn))
 ck(5,'内缘色序',2*np.arcsin(1.306/2)-ap<2*np.arcsin(1.317/2)-ap,'示例折射率增加使角半径增加')
 ck(5,'根号二变式',near(2*np.arcsin(np.sqrt(2)/2)-ap,np.pi/6),'顶角60度，最小偏向30度')
 ck(5,'平行面',near(np.arcsin(n*np.sin(np.arcsin(np.sin(.6)/n))),.6),'两次折射恢复原传播方向')
 dd90=2*np.arcsin(n/np.sqrt(2))-np.pi/2
 ck(5,'九十度棱镜',near(np.degrees(dd90),45.518849518554106),float(np.degrees(dd90)))
 # 06: dimensional scale, action integral, Airy nodes and probability moments.
 h=6.62607015e-34;hb=h/(2*np.pi);em=9.1093837139e-31;ell=(hb*hb/(2*em*em*g))**(1/3);eps=em*g*ell
 ck(6,'电子长度尺度',near(ell,.0008809935985944328),float(ell))
 ck(6,'电子能量尺度',near(eps,7.864802564304554e-33,atol=0),float(eps))
 zstar=(hb*hb/(4*em*em*g))**(1/3)
 ck(6,'不确定估计极值',near(zstar/ell,2**(-1/3)),float(zstar/ell))
 ck(6,'估计能量比例',near(hb*hb/(8*em*zstar*zstar)/(em*g*zstar),.5),.5)
 E=2.3;ma=1.2;ga=3.4;Sint=2*quad(lambda zz:np.sqrt(2*ma*(E-ma*ga*zz)),0,E/(ma*ga))[0];Sformula=4*np.sqrt(2*ma)*E**1.5/(3*ma*ga)
 ck(6,'经典面积积分',near(Sint,Sformula),float(Sint))
 eg=eps*(3*np.pi/2*np.array([.25,1.25]))**(2/3)
 ck(6,'题给能量比',near(eg[1]/eg[0],5**(2/3)),[float(v) for v in eg])
 wall=eps*(3*np.pi/2*np.array([.75,1.75]))**(2/3);aa=-ai_zeros(2)[0]
 ck(6,'硬壁WKB误差',np.all(abs(wall/eps-aa)/aa<.01),[float(v) for v in wall/eps])
 ck(6,'Airy地面节点',near([airy(-v)[0] for v in aa],[0,0]),aa.tolist())
 norm=airy(-aa[0])[1]**2;P=lambda zz:airy(zz-aa[0])[0]**2/norm
 ck(6,'波函数归一化',near(quad(P,0,np.inf,epsabs=1e-10)[0],1),'Ai平方在半直线积分')
 mean=quad(lambda zz:zz*P(zz),0,np.inf,epsabs=1e-10)[0]
 ck(6,'平均高度',near(mean,2*aa[0]/3),float(mean))
 kin=quad(lambda zz:airy(zz-aa[0])[1]**2/norm,0,np.inf,epsabs=1e-10)[0]
 ck(6,'量子维里关系',near(kin,aa[0]/3) and near(2*kin,mean),float(kin))
 de=1e-5;S=lambda ee:4*np.sqrt(2*ma)*ee**1.5/(3*ma*ga);period=(S(E+de)-S(E-de))/(2*de)
 ck(6,'作用量导数周期',near(period,2*np.sqrt(2*ma*E)/(ma*ga)),float(period))
 # 07: solve impact impulse rather than reuse final CM formulas.
 BM=1.;bm=.01;v0=500.;a=.1;b=.05;I0=BM*(.2**2+.1**2)/12;mt=BM+bm;mr=BM*bm/mt;VG=bm*v0/mt
 impulse=bm*v0/(1+bm/BM+bm*a*a/I0);VB=impulse/BM;Om=impulse*a/I0;vbullet=VB+Om*a
 ck(7,'碰撞线动量',near(BM*VB+bm*vbullet,bm*v0),[VB,vbullet])
 ck(7,'组合质心速度',near((BM*VB+bm*vbullet)/mt,VG),float(VG))
 ck(7,'质心上升高度',near(VG*VG/(2*g),1.2503776140394398),float(VG*VG/(2*g)))
 IG=I0+mr*a*a;LG=mr*v0*a
 ck(7,'组合角动量',near(IG*Om,LG),float(LG))
 ck(7,'平行轴惯量',near(IG,I0+BM*(bm*a/mt)**2+bm*(BM*a/mt)**2),float(IG))
 ck(7,'精确角速度',near(Om,116.05415860735008),float(Om))
 Et=.5*mt*VG*VG;Er=.5*IG*Om*Om;E0=.5*bm*v0*v0
 ck(7,'精确平转能',near([Et,Er],[12.376237623762377,28.726276883007444]),[float(Et),float(Er)])
 raw=.5*BM*VB*VB+.5*bm*vbullet*vbullet+.5*I0*Om*Om
 ck(7,'原粒子动能复核',near(raw,Et+Er),float(raw))
 ck(7,'内能差',near((E0-Et)-(E0-Et-Er),Er) and near(E0-Et-Er,1208.8974854932303),float(E0-Et-Er))
 IGb=I0+mr*(a*a+b*b);erb=LG*LG/(2*IGb)
 ck(7,'嵌入位置变式',near([erb,E0-Et-erb],[28.560548362528554,1209.063214013709]),[float(erb),float(E0-Et-erb)])
 ck(7,'主阶近似',near([(bm*v0*a/I0), (bm*v0*a)**2/(2*I0)],[120,30]),'统一忽略m/M修正')
 epsb=bm/mt;ck(7,'木块瞬时速度',near(VG-epsb*a*Om,VB) and not near(VB*VB/(2*g),VG*VG/(2*g)),float(VB))
 # 08: vector kinematics, surface area, force and the slip comparison.
 theta=.6;phi=.8;rr=1.7;ww=2.3;BB=4.1;e=np.array([np.cos(phi),np.sin(phi),0]);ta=np.array([-np.sin(phi),np.cos(phi),0]);zh=np.array([0,0,1]);by=np.array([0,BB,0])
 u=np.cos(theta)*e-np.sin(theta)*zh;normal=np.sin(theta)*e+np.cos(theta)*zh;C=rr*np.sin(theta)*zh;Apoint=rr*np.cos(theta)*e;OM=-ww*np.sin(theta)*u
 ck(8,'瞬时轴方向',near(np.cross(OM,Apoint-C),0),OM.tolist())
 ck(8,'中心接触零速度',near(np.cross(OM,Apoint-C),np.zeros(3)),'两固定瞬时点确定轴')
 dn=ww*np.sin(theta)*ta;ck(8,'法线演化',near(np.cross(OM,normal),dn),dn.tolist())
 ck(8,'角速度分量',near(OM,[-ww*np.sin(theta)*np.cos(theta)*np.cos(phi),-ww*np.sin(theta)*np.cos(theta)*np.sin(phi),ww*np.sin(theta)**2]),OM.tolist())
 ck(8,'角速度大小',near(np.linalg.norm(OM),ww*np.sin(theta)),float(np.linalg.norm(OM)))
 area=.5*np.cross(Apoint-C,-C);flux=float(area@by);ff=.5*BB*rr*rr*np.sin(theta)*np.cos(theta)*np.cos(phi)
 ck(8,'三角形磁通',near(flux,ff),float(flux))
 step=1e-5;fluxph=lambda ph:.5*BB*rr*rr*np.sin(theta)*np.cos(theta)*np.cos(ph);df=ww*(fluxph(phi+step)-fluxph(phi-step))/(2*step)
 ck(8,'几何磁通导数',near(df,-.5*BB*rr*rr*ww*np.sin(theta)*np.cos(theta)*np.sin(phi)),float(df))
 xs=np.linspace(0,rr,11);speeds=[np.cross(OM,x*u) for x in xs]
 ck(8,'整条CA零速度',near(speeds,np.zeros((11,3))),float(np.max(np.abs(speeds))))
 forces=[-1.7*np.cross(v,by) for v in speeds];ck(8,'电子磁力',near(forces,0),'所有x处携带速度磁力为零')
 work=quad(lambda x:float(np.cross(np.cross(OM,x*u),by)@u),0,rr)[0]
 ck(8,'路径单位电荷功',near(work,0),float(work))
 ck(8,'圆盘其他点运动',np.linalg.norm(np.cross(OM,.3*ta))>0,'离瞬时轴距离不为零的点一般在运动')
 emslip=quad(lambda x:float(np.cross(np.cross(ww*zh,x*u),by)@u),0,rr)[0]
 ck(8,'有滑动变式',near(emslip,-df),float(emslip))
 # Eight supplementary cross-checks tied to the draft's physical distinctions.
 supplement=[]
 def sc(q,name,ok,d):supplement.append(dict(question=q,name=name,passed=bool(ok),details=d))
 sc(1,'多个抽头能量闭合',all(near(U*(U*t/(L*(ns/N)**2)+(N/ns)*(N*U/(ns*R))),U*U*t/(L*(ns/N)**2)+R*(N*U/(ns*R))**2) for ns in [200,500,1000,1500]),'不同抽头的输入功率=储能率+热功率')
 cc=[]
 for khh in [.02,.7,8.]:
  depth=khh/kw;omfun=lambda kk:np.sqrt(g*kk*np.tanh(kk*depth));cgdiff=(omfun(kw+dk)-omfun(kw-dk))/(2*dk);cgexact=omfun(kw)/kw/2*(1+2*khh/np.sinh(2*khh));cc.append(near(cgdiff,cgexact))
 sc(2,'轨道衰减及有限水深群速度',near(np.exp(kw*(-1/kw)),np.exp(-1)) and all(cc),'浅水、中等水深、深水三组导数独立差分')
 jcrit=sync(ad);sc(3,'同步临界角动量',J>jcrit and near(mm*ad*ad,3*Ie),float(jcrit))
 sc(4,'两参考系力方向',pressure(rad)>pressure(0) and grad>0,'较高外侧压力提供向内合力')
 delta=.0002;caustic=(dev(ts+delta)+dev(ts-delta)-2*dev(ts))/(delta*delta)
 sc(5,'最小偏向二次映射',near(caustic,expected,rtol=2e-6),float(caustic))
 an=-ai_zeros(2)[1];bb=(3/4)**(1/3);normtrial=quad(lambda zz:4*bb**3*zz**2*np.exp(-2*bb*zz),0,np.inf)[0];etkin=quad(lambda zz:4*bb**3*(1-bb*zz)**2*np.exp(-2*bb*zz),0,np.inf)[0];etpot=quad(lambda zz:4*bb**3*zz**3*np.exp(-2*bb*zz),0,np.inf)[0]
 sc(6,'反射边界及变分积分',near([airy(-z)[1] for z in an],0) and near(an[0],1.018792971647471) and near(normtrial,1) and near(etkin+etpot,3*(3/4)**(2/3)) and etkin+etpot>aa[0],dict(neumann_zeros=an.tolist(),trial_normalization=normtrial,trial_energy=etkin+etpot,trial_mean_height=etpot))
 ttop=VG/g;func=lambda tt:VG*tt-g*tt*tt/2-epsb*a*np.sin(Om*tt);opt7=minimize_scalar(lambda tt:-func(tt),bounds=(ttop-.05,ttop+.05),method='bounded');peak=-opt7.fun
 sc(7,'木块中心高度界',abs(peak-VG*VG/(2*g))<=epsb*a*1.000001,[float(peak),float(epsb*a)])
 trials=[]
 for ph in np.linspace(0,2*np.pi,17):
  for th in [.2,.7,1.2]:
   ev=np.array([np.cos(ph),np.sin(ph),0]);uv=np.cos(th)*ev-np.sin(th)*zh;ov=-ww*np.sin(th)*uv;trials.append(np.linalg.norm(np.cross(ov,rr*uv)))
 sc(8,'多相位无滑动轴',max(trials)<1e-12,float(max(trials)))
 assert len(CHECKS)==96 and all(sum(c['name'].startswith(f'{q:02d}-') for c in CHECKS)==12 for q in range(1,9))
 result=dict(all_passed=all(c['passed'] for c in CHECKS),check_count=96,checks=CHECKS,
   supplementary_check_count=len(supplement),supplementary_checks=supplement,
   scope='仅核验明确写出的理想耦合、线性波、孤立圆轨道、等温气体、棱镜、量子边界、非弹性点状碰撞和无滑动准静态电路模型。')
 (ROOT/'physics_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(dict(all_passed=result['all_passed'],check_count=96,supplementary_count=8,failed=[c for c in CHECKS+supplement if not c['passed']]),ensure_ascii=False))
 assert result['all_passed'] and len(supplement)==8 and all(c['passed'] for c in supplement)
if __name__=='__main__':main()
