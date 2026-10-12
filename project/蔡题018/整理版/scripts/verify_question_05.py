"""薄泡膜、均匀等熵气体近似：从压强合力、能量Hessian和非线性ODE独立核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
ROOT=Path(__file__).resolve().parents[1]

def main():
    r,b,C,sigma,m=sp.symbols('r b C sigma m',positive=True)
    pg=C/r**5;pe=b/r**4;ps=4*sigma/r
    force=4*sp.pi*r**2*(pg+pe-ps)
    energy=2*sp.pi*C/r**2+8*sp.pi*sigma*r**2+4*sp.pi*b/r
    assert sp.simplify(force+sp.diff(energy,r))==0
    # 在平衡点使用C=4 sigma r^4-b r，直接由力对r求导，而非代回周期公式。
    fprime=sp.simplify(sp.diff(force,r).subs(C,4*sigma*r**4-b*r))
    expected=4*sp.pi*r*(pe-4*ps)
    assert sp.simplify(fprime-expected)==0
    x,y=sp.symbols('x y',real=True)
    R,Pg,Pe,Ps=sp.symbols('R Pg Pe Ps',positive=True)
    total_volume_ratio=((1+x)**3+(1+y)**3)/2
    gas=Pg*total_volume_ratio**(-sp.Rational(5,3))
    rel_acc=[]
    for z in [x,y]:
        rel_acc.append(4*sp.pi*R/m*(1+z)**2*
                       (gas+Pe/(1+z)**4-Ps/(1+z)))
    J=sp.Matrix(rel_acc).jacobian([x,y]).subs({x:0,y:0,Pg:Ps-Pe})
    J=sp.simplify(J)
    sum_eigen=sp.simplify((J*sp.Matrix([1,1]))[0])
    diff_eigen=sp.simplify((J*sp.Matrix([1,-1]))[0])
    assert sp.simplify(sum_eigen-4*sp.pi*R/m*(Pe-4*Ps))==0
    assert sp.simplify(diff_eigen-4*sp.pi*R/m*(Ps-4*Pe))==0
    # 独立总能量：2泡初态r0=1、sigma=1、p0=4、m=1。
    ra,rb,bb=sp.symbols('ra rb bb',positive=True)
    vv=(ra**3+rb**3)/2
    pair_energy=16*sp.pi*vv**(-sp.Rational(2,3))
    pair_energy+=8*sp.pi*(ra**2+rb**2)+4*sp.pi*bb*(1/ra+1/rb)
    pair_gas=4*vv**(-sp.Rational(5,3))
    pair_force=sp.Matrix([4*sp.pi*z**2*(pair_gas+bb/z**4-4/z) for z in [ra,rb]])
    gradient=sp.Matrix([sp.diff(pair_energy,z) for z in [ra,rb]])
    assert all(sp.simplify(item)==0 for item in pair_force+gradient)
    hessian=sp.lambdify((ra,rb,bb),sp.hessian(pair_energy,(ra,rb)),'numpy')
    critical_r=(4/3)**.25;critical_b=(4/3)**.75
    assert abs(4*critical_r**4-critical_b*critical_r-4)<1e-13
    rows=[]
    for bv in [0,.5,critical_b*(1-.001),critical_b*(1+.001),2,8,100]:
        radius=brentq(lambda z:4*z**4-bv*z-4,1,1+bv,xtol=5e-15) if bv else 1.
        q=bv/(4*radius**3)
        pgas=4/radius**5;pfield=bv/radius**4;psurface=4/radius
        assert abs(pgas+pfield-psurface)<2e-12
        assert abs(q-(1-radius**-4))<1e-12
        wsum2=4*math.pi*radius*(4*psurface-pfield)
        wdiff2=4*math.pi*radius*(4*pfield-psurface)
        wsingle2=wsum2
        assert wsingle2>0 and q<1
        # 直接有限差分两泡非线性合力，检验所有矩阵元素。
        def accelerations(pos):
            a1,a2=pos;gas=4*((a1**3+a2**3)/2)**(-5/3)
            return np.array([4*math.pi*z*z*(gas+bv/z**4-4/z) for z in pos])
        step=1e-5*radius
        numerical=np.column_stack([(accelerations(np.array([radius,radius])+np.eye(2)[k]*step)-
                                    accelerations(np.array([radius,radius])-np.eye(2)[k]*step))/(2*step)
                                   for k in range(2)])
        analytical=-np.asarray(hessian(radius,radius,bv),dtype=float)
        assert np.max(abs(numerical-analytical))<1e-6
        assert abs(np.linalg.eigvalsh(analytical)[0]+max(wsum2,wdiff2))<1e-9
        assert abs(np.linalg.eigvalsh(analytical)[1]+min(wsum2,wdiff2))<1e-9
        # 单泡微小振幅的完整非线性轨迹，过平衡点事件验证四分之一周期。
        period=2*math.pi/math.sqrt(wsingle2)
        def ode(t,z):return [z[1],4*math.pi*z[0]**2*(4/z[0]**5+bv/z[0]**4-4/z[0])]
        def crossing(t,z):return z[0]-radius
        crossing.direction=-1;crossing.terminal=True
        sol=solve_ivp(ode,(0,period),[radius*(1+1e-5),0],events=crossing,
                      method='DOP853',rtol=1e-12,atol=1e-13,max_step=period/100)
        assert len(sol.t_events[0])==1
        measured=4*sol.t_events[0][0]
        assert abs(measured/period-1)<1e-4
        rows.append(dict(b_dimensionless=bv,r_over_r0=radius,electric_to_surface_pressure=q,
                         w_single_squared=wsingle2,w_symmetric_squared=wsum2,
                         w_antisymmetric_squared=wdiff2,radial_pair_stable=wdiff2>0,
                         independent_force_jacobian_max_error=float(np.max(abs(numerical-analytical))),
                         nonlinear_single_period_relative_error=measured/period-1))
    # 总质量与有效径向惯性不能未经条件等同：均匀气体仿射径向流的直接体积分。
    rho,Rg,rdot=sp.symbols('rho Rg rdot',positive=True)
    u=sp.symbols('u',nonnegative=True)
    gas_K=sp.integrate(sp.Rational(1,2)*rho*(rdot*u/Rg)**2*4*sp.pi*u**2,(u,0,Rg))
    gas_mass=4*sp.pi*rho*Rg**3/3
    assert sp.simplify(gas_K/(sp.Rational(1,2)*gas_mass*rdot**2)-sp.Rational(3,5))==0
    # 任意热容比从完整压强方程重推，不只检查最终gamma=5/3公式。
    gamma=sp.symbols('gamma',positive=True)
    general_gas=Pg*total_volume_ratio**(-gamma)
    general_acc=sp.Matrix([4*sp.pi*R/m*(1+z)**2*
                          (general_gas+Pe/(1+z)**4-Ps/(1+z)) for z in [x,y]])
    Jg=sp.simplify(general_acc.jacobian([x,y]).subs({x:0,y:0,Pg:Ps-Pe}))
    assert sp.simplify((Jg*sp.Matrix([1,1]))[0]+4*sp.pi*R/m*
                      ((3*gamma-1)*Ps+(4-3*gamma)*Pe))==0
    assert sp.simplify((Jg*sp.Matrix([1,-1]))[0]-4*sp.pi*R/m*(Ps-4*Pe))==0
    phi_acc=4*sp.pi*R/m*(1+x)**2*(Pg/(1+x)**5+Pe/(1+x)**2-Ps/(1+x))
    phi_derivative=sp.diff(phi_acc,x).subs({x:0,Pg:Ps-Pe})
    assert sp.simplify(phi_derivative-4*sp.pi*R/m*(3*Pe-4*Ps))==0
    # 带解变式的实际数值和gamma=7/5阈值：独立求根、频率及代回。
    variant_period=math.sqrt(math.pi*1e-6/(16*.025))
    assert abs(variant_period-0.002802495608198964)<1e-16
    z=brentq(lambda z:4*z**4-2*z-4,1,2,xtol=1e-14)
    q=1-z**-4
    zp=1.12;newton=[]
    for _ in range(3):
        value=4*zp**4-2*zp-4;slope=16*zp**3-2
        znext=zp-value/slope
        newton.append(dict(z=zp,residual=value,derivative=slope,next=znext));zp=znext
    assert abs(zp-z)<1e-13
    g=sp.Rational(7,5);zc=(sp.Rational(4,3))**(1/(3*g-1))
    assert sp.simplify(zc**(3*g-1)-sp.Rational(4,3))==0
    assert sp.simplify(zc**3-sp.Rational(4,3)**sp.Rational(15,16))==0
    draft=ROOT/'drafts/question-05.md'
    doc_complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    files=['scripts/verify_question_05.py','drafts/question-05-核验备忘.md',
           'drafts/question-05.md','figures/题05_图稿源文件.tex']
    present=[p for p in files if (ROOT/p).exists()]
    figures=['question-05','interfaces-05','element-05','modes-05','stability-05']
    report=dict(question=5,verified_math=True,document_complete=doc_complete,
                set_accepted=False,
                scope='薄膜集总径向惯性、均匀等熵气体与球壳自场模型；分题核验不代表整套交付',
                assumptions=['m作泡膜有效径向惯性质量，气体惯性忽略',
                             '加电后的比较状态沿相同等熵气体常数，若存在额外加热需改写常数',
                             '连通管质量、体积、流动惯性及阻尼忽略；连通气体压强和温度均匀',
                             '只保留均匀带电独立球壳自场，忽略泡间静电相互作用',
                             '本核验只针对保持球形的径向微扰，不用其代替完整非球形稳定性证明'],
                symbolic_single_force_derivative=str(fprime),symbolic_pair_jacobian=str(J),
                symmetric_acceleration_eigenvalue=str(sum_eigen),
                antisymmetric_acceleration_eigenvalue=str(diff_eigen),
                charge_threshold_squared='32*pi^2*epsilon0*sigma*r0^3*(4/3)^(3/4)',
                critical_r_over_r0=critical_r,critical_b_dimensionless=critical_b,
                numerical_checks=rows,gas_inertia_fraction_of_mass='3/5 for homogeneous affine radial flow',
                general_gamma_pair_jacobian=str(Jg),fixed_potential_acceleration_derivative=str(phi_derivative),
                solved_variants=dict(period_seconds=variant_period,quadruple_mass_period_seconds=2*variant_period,
                                     beta2_z=z,beta2_q=q,newton_steps=newton,
                                     omega_plus_over_unit=2*math.sqrt(4-q),
                                     omega_minus_over_unit=2*math.sqrt(4*q-1),
                                     mode_frequency_ratio=math.sqrt((4*q-1)/(4-q)),
                                     gamma7_over5_threshold_exponent='15/16'),
                figures_sha256={name:hashlib.sha256((ROOT/f'figures/{name}.pdf').read_bytes()).hexdigest()
                                for name in figures if (ROOT/f'figures/{name}.pdf').exists()},
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in present})
    target='verification-q05.json' if doc_complete else 'verification-q05-preliminary.json'
    (ROOT/'build'/target).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
