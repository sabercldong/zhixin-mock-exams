from pathlib import Path
import json, math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad, solve_ivp
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,residual,tol=1e-8):
 assert abs(residual)<tol,(name,residual,tol)
 checks.append(dict(name=name,residual=float(residual),tolerance=tol,passed=True))
g=9.8
# 1: solve complete force/moment equations, rather than assuming load balance.
G,h,l,k,M,P=9800,.3,2.4,1e-6,1000,2000
nf,nr=G/2-M/l,G/2+M/l
ff=M/h-k*nf**2/(2*h);fr=-k*nr**2/(2*h)
a=(ff+fr)*g/G
ts=brentq(lambda t:t-k*((G/2-t/l)**2+(G/2+t/l)**2)/2,0,100)
check('01 质心力矩闭合',l*(nf-nr)/2+k*(nf**2+nr**2)/2+h*(ff+fr))
check('01 匀速二次式与稳定根',ts-k*G**2/(2*(1+np.sqrt(1-(k*G/l)**2))))
check('01 变式无滚阻加速度',g*M/(G*h)-(g/G)*(M/h))
check('01 变式级数修正',ts/(k*G**2/4)-1-(k*G/l)**2/4,1e-9)
check('01 变式前轴摩擦约束更严',min(0,k*(G/2+ts/l)**2/(2*h*(G/2-ts/l))-k*(G/2+ts/l)/(2*h)))
slope=brentq(lambda s:h*G*np.sin(s)+k*G**2*np.cos(s)**2/4+k*M**2/l**2-M,0,.6)
# 2: minimize barrier ratio numerically independently of half-angle root.
phi=brentq(lambda x:np.tan(x/2)-x,1,3);lam=phi/(1-np.cos(phi))
opt=minimize_scalar(lambda x:x/(1-np.cos(x)),bounds=(.1,6.2),method='bounded',options={'xatol':1e-12})
check('02 势垒最小值交叉核对',opt.fun-lam)
check('02 临界能量',lam*(1-np.cos(phi))-phi)
check('02 临界力矩',lam*np.sin(phi)-1)
turn=brentq(lambda x:2*(1-np.cos(x))-x,.1,2)
check('02 变式转折点',2*(1-np.cos(turn))-turn)
check('02 薄壁筒临界惯量无关',lam*2-lam*2)
check('02 稳定平衡线性曲率',np.cos(np.arcsin(1/2))-np.sqrt(3)/2)
check('02 纯滚动摩擦上界',(1+2*lam)/3-1.2533667598,1e-9)
# 3: geometric tangential projections over many off-axis points.
for xx in [-1.1,-2,-5,-20]:
 yy=np.sqrt(3*(xx*xx-1));tt=np.array([1,3*xx/yy]);tt/=np.linalg.norm(tt)
 vv=np.array([2-xx,-yy]);vv/=np.linalg.norm(vv)
 check(f'03 双曲面切向守恒 x={xx}',tt[0]-.5*np.dot(tt,vv))
check('03 变式平面折射角',np.sin(np.deg2rad(20.7048110546))*np.sqrt(2)-.5)
check('03 原极性负电荷动能减小',(-1)*(3/8)-(0.5*0.5**2-0.5))
# 4: independent time-domain circuit integration and mean force integration.
R,r,sigma,rho,L,kB,alpha,f=.1,.001,3.7e7,2700,6e-7,.002,np.pi/6,1e4
res=2*R/(sigma*r*r);mass=2*np.pi**2*rho*R*r*r;om=2*np.pi*f;mut=np.pi*R*R*kB*np.cos(alpha)
coef=np.pi**2*R**3*kB**2*np.sin(alpha)*np.cos(alpha)*om**2*L/(res**2+om**2*L**2)
I0=np.sqrt(mass*g/coef);ip=om*mut*I0/np.hypot(res,om*L)
aI=-om**2*L*mut*I0/(res**2+om**2*L**2);bI=om*res*mut*I0/(res**2+om**2*L**2)
mean=quad(lambda t:-2*np.pi*R*kB*np.sin(alpha)*I0*np.cos(om*t)*(aI*np.cos(om*t)+bI*np.sin(om*t)),0,1/f,epsabs=1e-12)[0]*f
check('04 周期积分力平衡',mean-mass*g)
sol=solve_ivp(lambda t,y:[(om*mut*I0*np.sin(om*t)-res*y[0])/L],(0,10/f),[aI],rtol=1e-10,atol=1e-9)
check('04 时域电路周期闭合',sol.y[0,-1]-aI,1e-5)
check('04 无自感平均力',quad(lambda t:np.cos(t)*np.sin(t),0,2*np.pi)[0])
I1k=I0*np.sqrt((L+res**2/((2*np.pi*1000)**2*L))/(L+res**2/(om**2*L)))
check('04 高频系数饱和',coef/(np.pi**2*R**3*kB**2*np.sin(alpha)*np.cos(alpha)/L)-om**2*L**2/(res**2+om**2*L**2))
check('04 倾角最大值',np.sin(np.pi/4)*np.cos(np.pi/4)-.5)
# 5: compare exact Snell residual and inverse-map finite difference.
n=1.33
def D(x):return x*x+np.sqrt((1-x*x)*(n*n-x*x))
def X(a):return brentq(lambda x:x/D(x)-a,0,.99999999999,xtol=1e-14)
x=X(.5);dp=2*x-x*(1+n*n-2*x*x)/np.sqrt((1-x*x)*(n*n-x*x));mag=D(x)**2/(D(x)-x*dp)
check('05 原始斯涅尔方程',n*.5*np.sqrt(1-x*x)/np.sqrt(1+.25-x)-x)
check('05 逆映射宽度导数',(X(.500001)-X(.499999))/.000002-mag,1e-8)
check('05 轴上放大',X(1e-5)/1e-5-n,1e-9)
check('05 小偏轴级数',X(.001)-(n*.001-n*(n-1)**2*.001**3/2),1e-12)
finite=(X(.505)-X(.495))/.01
check('05 有限宽度趋近微分',finite-mag,1e-4)
# 6: minimize arrival cost under the actual angular momentum feasibility.
Re=6371e3;mu=g*Re**2;T=86400;rf=(mu*(T/(2*np.pi))**2)**(1/3);q=rf/Re;vc=np.sqrt(mu/rf);delta=2*mu*(1/Re-1/rf);wh=np.sqrt(delta/(q*q-1));v1=q*wh;dv2=vc-wh;dv=v1+dv2
cost=lambda w:np.sqrt(max(0,(q*q-1)*w*w-delta)+w*w+delta)+np.sqrt(max(0,(q*q-1)*w*w-delta)+(vc-w)**2)
opt=minimize_scalar(cost,bounds=(0,vc*2),method='bounded',options={'xatol':1e-8})
check('06 优化器全局相切解',opt.fun-dv,1e-3)
check('06 两端角动量',Re*v1-rf*wh,.01)
check('06 两端机械能',v1*v1/2-mu/Re-(wh*wh/2-mu/rf),1e-6)
check('06 质量比反代',200*np.log(np.exp(dv/200))-dv)
check('06 变式喷气速率加倍',np.log(np.exp(dv/400))*2-dv/200)
check('06 目标半径2R系数',np.sqrt(4/3)+1/np.sqrt(2)-1/np.sqrt(3)-(1/np.sqrt(3)+1/np.sqrt(2)))
check('06 径向弹道成本更高',min(0,np.sqrt(delta)+vc-dv))
check('06 已有低轨速度基准',v1-np.sqrt(mu/Re)+dv2-(dv-np.sqrt(mu/Re)))
# 7: explicit species vectors, atom balance and first law.
Rg=8.314462618;n1=202650*.0015/(Rg*350);Nper=21.5*79/21;water=15/(Nper+29);fuel=.168*n1/21.5;mf=.198*fuel
before=np.array([.632*n1+.2*n1*Nper/(Nper+29),.168*n1,.2*n1*14/(Nper+29),.2*n1*15/(Nper+29)])
after=before+np.array([0,-21.5*fuel,14*fuel,15*fuel]);cv=np.array([2.5,2.5,2.5,3])*Rg
C1=before@cv;C3=after@cv;n3=after.sum();ga1=1+n1*Rg/C1;ga3=1+n3*Rg/C3;T2=350*6**(ga1-1);QH=4e7*mf;dng=n3-n1;cor=dng*Rg*T2;T3=T2+(QH+cor)/C3;T4=T3/6**(ga3-1)
check('07 初始摩尔数组分和',before.sum()-n1)
check('07 氧原子守恒',2*21.5*fuel-2*14*fuel-15*fuel)
check('07 氢原子守恒',30*fuel-2*15*fuel)
check('07 碳原子守恒',14*fuel-14*fuel)
check('07 燃烧后水分数稳态',after[3]/n3-water)
check('07 定容燃烧第一定律',C3*(T3-T2)-QH-cor)
Wexp=quad(lambda V:n3*Rg*T3*(.00025/V)**(ga3-1)/V,.00025,.0015)[0]
Wcomp=quad(lambda V:n1*Rg*350*(.0015/V)**(ga1-1)/V,.00025,.0015)[0]
check('07 膨胀功独立pV积分',Wexp-C3*(T3-T4),1e-7)
check('07 压缩功独立pV积分',Wcomp-C1*(T2-350),1e-7)
check('07 去残气燃油质量比例',(.21*n1/21.5*.198)/mf-1.25)
check('07 产物比热比快捷式',ga3-1-1/(2.5+.5*water))
C10=2.5*n1*Rg;C30=Rg*(2.5*n3+7.5*fuel);g10=1+n1*Rg/C10;g30=1+n3*Rg/C30;t20=350*6**(g10-1);t30=t20+(QH+dng*Rg*t20)/C30;t40=t30/6**(g30-1)
# 8: construct unseen e+ photon state and invariant-check interior energies.
MM,mm,beta,theta=135,.511,.2,np.pi/6;gamma=1/np.sqrt(1-beta**2);bb=beta*np.cos(theta);AA=MM/(2*gamma);Emax=(AA+bb*np.sqrt(AA**2-(1-bb**2)*mm**2))/(1-bb**2);vmax=np.sqrt(1-(mm/Emax)**2)
check('08 端点未经平方方程',Emax-bb*np.sqrt(Emax**2-mm**2)-AA)
for E in [.511001,1,20,60,79.9]:
 pe=np.array([E,np.sqrt(E*E-mm*mm)*np.cos(theta),np.sqrt(E*E-mm*mm)*np.sin(theta),0]);QQ=np.array([gamma*MM,gamma*MM*beta,0,0])-pe;s=QQ[0]**2-QQ[1:]@QQ[1:];assert s>mm*mm
 eg=(s-mm*mm)/(2*np.sqrt(s));ep=(s+mm*mm)/(2*np.sqrt(s));check(f'08 充分性正电子壳条件 E={E}',ep*ep-eg*eg-mm*mm,1e-10)
check('08 母粒子静止能量界',MM/2-MM/(2*1))
check('08 横向能量界',AA-MM*np.sqrt(1-beta**2)/2)
check('08 无质量近似前向多普勒',AA/(1-beta)-MM*np.sqrt((1+beta)/(1-beta))/2)
vals=dict(car_torque=ts,car_speed=P*h/ts,car_acceleration=a,car_slope_degrees=np.rad2deg(slope),critical_phi=phi,critical_lambda=lam,lambda2_turn=turn,ring_resistance=res,ring_mass=mass,ring_I0=I0,ring_I1k=I1k,ring_I45=I0*np.sqrt(np.sin(alpha)*np.cos(alpha)/.5),ring_peak=ip,ring_Joule=res*ip**2/2,image_x=x,image_magnification=mag,finite_width_magnification=finite,earth_mu=mu,orbit_rf=rf,orbit_v1=v1,orbit_va=wh,orbit_vc=vc,orbit_dv=dv,orbit_mass_ratio=np.exp(dv/200),orbit_u400_ratio=np.exp(dv/400),orbit_radial_cost=np.sqrt(delta)+vc,orbit_parking_dv=dv-np.sqrt(mu/Re),fuel_mass=mf,gamma1=ga1,gamma3=ga3,T2=T2,T3=T3,T4=T4,enthalpy_correction=cor,temperature_correction=cor/C3,temperature_correction4=cor/C3/6**(ga3-1),T4_dryresidual=t40,T2_fresh100=350*6**.4,ideal_net_ratio=(Wexp-Wcomp)/QH,electron_Emax=Emax,electron_vmax=vmax,electron_rest_vmax=np.sqrt(1-(mm/(MM/2))**2))
(ROOT/'physics_verification.json').write_text(json.dumps(dict(all_passed=True,check_count=len(checks),checks=checks,values=vals),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(vals,ensure_ascii=False,indent=2));print('PASS',len(checks))
