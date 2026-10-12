"""对本批修正重新建立数值模型；不依赖草稿中的结果文件。"""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import minimize_scalar

ROOT=Path(__file__).resolve().parents[1]
results=[]
def check(name,residual,tol=1e-8):
    residual=float(residual)
    assert abs(residual)<tol,(name,residual,tol)
    results.append(dict(name=name,residual=residual,tolerance=tol,passed=True))

# 004-02: 直接积分辅助中心力方程，比较完整回返，而不是重代周期恒等式。
for alpha in [math.pi/6,math.pi/4,math.pi/3]:
    for a in [0.7,2.8]:
        r0=1.3;n0=math.sqrt(a/r0);wz=n0*math.sin(alpha)
        period=math.pi*r0**1.5/(math.sqrt(a)*math.sin(alpha)**3)
        def rhs(t,u):
            x,y,z,vx,vy,vz,optical=u;r=math.hypot(x,y)
            return [vx,vy,vz,-a*x/(2*r**3),-a*y/(2*r**3),0,a/r]
        sol=solve_ivp(rhs,[0,period],[r0,0,0,0,n0*math.cos(alpha),wz,0],method='DOP853',rtol=2e-12,atol=2e-13)
        u=sol.y[:,-1]
        check(f'004-02 回返点 a={a},alpha={alpha}',np.linalg.norm(u[:2]-[r0,0]),2e-8)
        check(f'004-02 高度独立于a a={a},alpha={alpha}',u[2]-math.pi*r0/math.sin(alpha)**2,2e-8)
        check(f'004-02 光程 a={a},alpha={alpha}',u[6]-2*math.pi*math.sqrt(a*r0)/math.sin(alpha),2e-8)

# 005-03: 固定原题极性，以带符号q由能量求速度，再验证有限孔径的局部透射。
for eccentricity in [1.2,2,3.5]:
    A=1.1;B=A*math.sqrt(eccentricity**2-1);c=A*eccentricity
    q=-0.7;m=1.4;v0=2.1
    potential_drop=0.5*m*v0*v0*(1-1/eccentricity**2)/abs(q)
    v1=math.sqrt(v0*v0+2*q*potential_drop/m)
    check(f'005-03 负粒子原极性速率 e={eccentricity}',v1-v0/eccentricity)
    for y in [0.1,1.2,5.0]:
        x=-A*math.sqrt(1+y*y/(B*B));D=math.hypot(c-x,y)
        tangent=np.array([-A*y/(B*B*math.sqrt(1+y*y/(B*B))),1.]);tangent/=np.linalg.norm(tangent)
        outgoing=np.array([c-x,-y])/D
        check(f'005-03 切向守恒 e={eccentricity},y={y}',v0*tangent[0]-v1*np.dot(outgoing,tangent))
        assert v1*v1-(v0*tangent[0])**2>0
        check(f'005-03 非轴上距离 e={eccentricity},y={y}',D-(A-eccentricity*x))
    assert math.sqrt(v0*v0+2*abs(q)*potential_drop/m)>v0>v1

# 004-05: 临界等号时到中心的时间积分发散；略高于阈值时有限。
Omega=1.7;L=1.3
for cutoff in [0.1,0.01,0.001]:
    travel=quad(lambda x:1/(Omega*x),cutoff,L)[0]
    check(f'004-05 临界时间积分 cutoff={cutoff}',travel-math.log(L/cutoff)/Omega)
for excess in [0.01,0.2,1.0]:
    travel=quad(lambda x:1/math.sqrt(excess+Omega**2*x*x),0,L)[0]
    check(f'004-05 超临界有限时间 excess={excess}',travel-math.asinh(Omega*L/math.sqrt(excess))/Omega)

# 004-08: 锥面位移直接差分，检查初始加速度及其切向方向。
v=2.;L=3.;alpha=math.pi/6;theta=0.4
def curve(t):
    rho=L-v*math.cos(theta)*t
    phi=-math.tan(theta)/math.sin(alpha)*math.log(rho/L)
    return np.array([rho*math.sin(alpha)*math.cos(phi),rho*math.sin(alpha)*math.sin(phi),rho*math.cos(alpha)])
dt=1e-4;acc=(curve(dt)-2*curve(0)+curve(-dt))/(dt*dt)
expected=np.array([-v*v*math.sin(theta)**2/(L*math.sin(alpha)),-v*v*math.sin(theta)*math.cos(theta)/L,0.])
check('004-08 几何轨迹二阶差分',np.linalg.norm(acc-expected),2e-7)
tangent_acc=np.array([-math.sin(alpha)*math.sin(theta),-math.cos(theta),-math.cos(alpha)*math.sin(theta)])
initial_velocity=np.array([-math.sin(alpha)*math.cos(theta),math.sin(theta),-math.cos(alpha)*math.cos(theta)])
check('004-08 切向加速度正交速度',np.dot(tangent_acc,initial_velocity))

# 005-07: 图稿的两个绝热曲线与已计算状态坐标在同一坐标系闭合。
beta=.6;gamma=1/math.sqrt(1-beta*beta);Q=gamma**3-2*gamma*gamma+2
clock=np.array([(gamma-2)*(gamma*gamma-1),1+gamma-gamma*gamma])/Q
vy=beta*gamma*(gamma-1)/Q
check('003-06 精确方向向量与净速度长度收缩',np.linalg.norm(clock)-math.sqrt(1-vy*vy))
g1=1.3978276798413862;g3=1.389369331364691
check('005-07 压缩曲线端点 P2/P1',6**g1-24.476614/2,
      3e-5)
check('005-07 膨胀曲线端点 P4/P1',62.91765*6**(-g3)-10.43908/2,3e-5)

out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(dict(all_passed=True,check_count=len(results),checks=results),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(all_passed=True,check_count=len(results)),ensure_ascii=False))
