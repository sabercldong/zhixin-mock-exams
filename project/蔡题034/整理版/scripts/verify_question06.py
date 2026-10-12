"""第034套第6题：直接积分静力/绝热微分方程，再用浮力零点求高。
未调用解析 p(T) 幂律或解析高度式来生成独立参考根。
"""
from pathlib import Path
import json
import math
ROOT=Path(__file__).resolve().parents[1]
mu=.029;g=9.81;R=8.314462618;Cp=3.5*R
T0=288.;p0=101325.;r=6.;kappa=3.;power=40000.
V=4*math.pi*r**3/3
delta=power/(4*math.pi*r*r*kappa)
def deriv(p,T):
    dp=-mu*p*g/(R*T)
    dT=R*T/(Cp*p)*dp
    return dp,dT
def environment(z):
    p,T=p0,T0
    dz=z/500
    for _ in range(500):
        a=deriv(p,T)
        b=deriv(p+dz*a[0]/2,T+dz*a[1]/2)
        c=deriv(p+dz*b[0]/2,T+dz*b[1]/2)
        d=deriv(p+dz*c[0],T+dz*c[1])
        p+=dz*(a[0]+2*b[0]+2*c[0]+d[0])/6
        T+=dz*(a[1]+2*b[1]+2*c[1]+d[1])/6
    return p,T
def capacity(z):
    p,T=environment(z)
    outside=mu*p/(R*T)
    inside=mu*p/(R*(T+delta))
    return V*(outside-inside)
def root(m0,upper):
    lo,hi=0.,upper
    assert capacity(hi)<m0<capacity(lo)
    for _ in range(55):
        mid=(lo+hi)/2
        if capacity(mid)>m0:lo=mid
        else:hi=mid
    return (lo+hi)/2
def main():
    M0=capacity(0)
    D=mu*g*(3*T0+5*delta)/(7*R*T0*(T0+delta))
    # 0.1 m 对称差分兼顾 O(h^2) 截断误差与逐步积分后的相消误差。
    numericD=-(capacity(.1)-capacity(-.1))/(.2*M0)
    assert abs(numericD/D-1)<1e-7
    rows=[]
    for eps in [.001,.005,.01,.02]:
        m0=(1-eps)*M0
        linear=eps/D
        exact=root(m0,2*linear)
        relative=abs(exact-linear)/exact
        assert relative<eps
        assert abs(capacity(exact)-m0)<1e-9
        rows.append(dict(ground_capacity_margin=eps,self_mass_kg=m0,
                         linear_height_m=linear,ode_root_height_m=exact,
                         relative_first_order_error=relative))
    assert rows[0]["relative_first_order_error"]<rows[-1]["relative_first_order_error"]
    # 变式功率：不代入高度公式，由当地两种密度直接检验力平衡。
    p,T=environment(100)
    outside=mu*p/(R*T)
    for q in [.1,.2,.5]:
        dT=q*T/(1-q)
        heat=4*math.pi*r*r*kappa*dT
        inside=mu*p/(R*(T+dT))
        mass=q*outside*V
        assert abs((outside-inside)*V-mass)<1e-9
        rows.append(dict(variant=True,load_ratio=q,required_power_W=heat))
    data=dict(status="passed",method="RK4积分静力与绝热微分方程 + 浮力零点二分",
              ground_capacity_kg=M0,delta_K=delta,
              D_analytical_per_m=D,D_finite_difference_per_m=numericD,rows=rows)
    (ROOT/"build/question06-verification.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
