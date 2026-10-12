"""独立积分射流Euler方程、直接表面面积求根、曲率及微扰核验。"""
from pathlib import Path
import hashlib,json,math,re
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
def main():
    r0,v0,rho,sigma,g=.0015,.8,1000.,.072,9.8
    eta=2*sigma/(rho*v0*v0*r0)
    def root(y,e=eta):
        z=2*g*y/v0**2;upper=(1+z)**.25
        return 1. if y==0 else brentq(lambda w:w**4+e*(w-1)-1-z,1,upper)
    # 速度ODE来自局部动量平衡和连续性，不调用闭式y(r)。
    def ode(y,state):
        v=state[0];r=r0*math.sqrt(v0/v)
        return [g/(v+sigma/(2*rho*v*r))]
    sol=solve_ivp(ode,[0,3],[v0],rtol=2e-11,atol=2e-12,dense_output=True)
    rows=[]
    for y in [0,.01,.1,.5,1,2.7]:
        w=root(y);r=r0/w;v=v0*w*w;v_num=float(sol.sol(y)[0])
        assert abs(v_num-v)<2e-9
        assert r0/(1+2*g*y/v0**2)**.25<=r+1e-15<=r0+1e-15
        residual=(sigma/r+.5*rho*v*v-rho*g*y)-(sigma/r0+.5*rho*v0*v0)
        assert abs(residual)<2e-6
        rows.append(dict(y=y,r=r,v=v,ode_error=v_num-v,bernoulli_residual=residual))
    a=.0015;rc=2*a/3
    def area_difference(y):
        r=r0/root(y);L=4*a**3/(3*r*r)
        return 4*math.pi*a*a-2*math.pi*r*L
    yc=brentq(area_difference,0,.5,xtol=1e-14)
    formula=v0*v0/(2*g)*((3*r0/(2*a))**4-1)+sigma/(rho*g)*(3/(2*a)-1/r0)
    assert abs(yc-formula)<1e-12
    vc=v0*(r0/rc)**2;Lc=4*a**3/(3*rc*rc)
    slope=-g*rc/(2*vc**2+sigma/(rho*rc))
    assert abs(Lc-3*a)<1e-14
    inverse=math.sqrt((2*g*yc-2*sigma/(rho*r0)*(r0/rc-1))/((r0/rc)**4-1))
    assert abs(inverse-v0)<1e-12
    a2=.00075;yc2=v0*v0/(2*g)*((3*r0/(2*a2))**4-1)+sigma/(rho*g)*(3/(2*a2)-1/r0)
    assert abs(yc2-2.622040816326531)<1e-12
    f=3*r0*r0*v0/(4*a**3);assert abs(f-400)<1e-10 and abs(vc/f-Lc)<1e-14
    # 微扰误差应为二阶；独立正根求解比较。
    small=[];z=3.;wstar=(1+z)**.25
    for e in [.02,.01,.005]:
        w=brentq(lambda w:w**4+e*(w-1)-1-z,1,wstar)
        approx=1/wstar*(1+e*(wstar-1)/(4*wstar**4))
        small.append(dict(eta=e,absolute_error=abs(approx-1/w)))
    ratios=[small[i]['absolute_error']/small[i+1]['absolute_error'] for i in range(2)]
    assert all(3.8<x<4.2 for x in ratios)
    # 有限周期波纹：独立数值积分表面积，体积保持到二阶。
    surface=[]
    for kr in [.7,1.4]:
        wavelength=2*math.pi/kr
        errors=[]
        for eps in [.03,.015,.0075]:
            R=lambda s:1+eps*math.cos(kr*s)-eps*eps/4
            Rp=lambda s:-eps*kr*math.sin(kr*s)
            volume=quad(lambda s:math.pi*R(s)**2,0,wavelength,epsabs=1e-12)[0]
            area=quad(lambda s:2*math.pi*R(s)*math.sqrt(1+Rp(s)**2),0,wavelength,epsabs=1e-12)[0]
            coefficient=(area/(2*math.pi*wavelength)-1)/eps**2
            # 主文只取二阶；有限eps的四阶面积修正明确保留后再核验六阶余项。
            fourth=-(kr*kr/16+3*kr**4/64)*eps**2
            assert abs(coefficient-(kr*kr-1)/4-fourth)<.5*eps**4
            assert (area-2*math.pi*wavelength)*(kr*kr-1)>0
            assert abs(volume/(math.pi*wavelength)-1)<=eps**4/16+1e-12
            errors.append(dict(epsilon=eps,area_quadratic_coefficient=coefficient,volume_relative_error=volume/(math.pi*wavelength)-1))
        surface.append(dict(kr=kr,predicted=(kr*kr-1)/4,integrals=errors))
    r,sg,rr,vv,gg=sp.symbols('r sigma r0 v0 g',positive=True);dens=sp.symbols('rho',positive=True)
    yr=vv**2/(2*gg)*((rr/r)**4-1)+sg/(dens*gg)*(1/r-1/rr)
    expected=-gg*r/(2*vv**2*rr**4/r**4+sg/(dens*r))
    assert sp.simplify(1/sp.diff(yr,r)-expected)==0
    draft=(ROOT/'drafts/question-01.md').read_text();assert '<!-- question-complete -->' in draft
    # 同时核对正文给出的数值，不能只验脚本自身。
    assert '2.62204' in draft and '0.135102' in draft and '400' in draft
    plotted=re.findall(r'\((\d+\.\d+),(\d+\.\d+)\)',(ROOT/'figures/radius-01-coordinates.tex').read_text())
    assert len(plotted)==101
    plot_residual=max(abs((1/float(r))**4+.4*(1/float(r)-1)-1-float(z)) for z,r in plotted)
    assert plot_residual<4e-8
    source=['drafts/question-01.md','figures/题01_图稿源文件.tex','scripts/verify_question_01.py',
            'scripts/generate_question_01_curve.py','figures/radius-01-coordinates.tex']
    result=dict(question=1,verified_math=True,document_complete=True,eta=eta,velocity_ode=rows,
                direct_area_root_y=yc,closed_model_y=formula,critical_radius=rc,critical_speed=vc,
                critical_segment=Lc,local_segment_relative_change=abs(Lc*slope/rc),
                inferred_v0=inverse,inverse_without_capillarity=math.sqrt(2*g*yc/((r0/rc)**4-1)),
                smaller_drop_y=yc2,uniform_drop_frequency=f,perturbation_errors=small,
                perturbation_error_ratios=ratios,surface_integrals=surface,plot_model_max_residual=plot_residual,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source},
                limitations=['能量阈值非动态断裂高度','小扰动稳定性不等于有限球滴终态比较'])
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build/verification-q01.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
