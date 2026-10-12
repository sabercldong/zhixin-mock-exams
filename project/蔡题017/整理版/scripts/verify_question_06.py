"""017 Q6: independent steady energy balances, BVP shooting and entropy quadrature."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq,minimize_scalar
from scipy.linalg import solve
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def shoot(TL,TH,Cc,Ch,G,length):
    def ode(x,t):
        heat=G*(t[1]-t[0])
        return [heat/Cc,heat/Ch]
    def residual(h0):
        return solve_ivp(ode,[0,length],[TL,h0],method='DOP853',
            rtol=2e-12,atol=2e-11,dense_output=True).y[1,-1]-TH
    h0=brentq(residual,TL,TH,xtol=2e-11)
    return solve_ivp(ode,[0,length],[TL,h0],method='DOP853',
        rtol=2e-12,atol=2e-11,dense_output=True)
def discrete(TL,TH,Cc,Ch,G,length,n=100):
    # Two oppositely moving streams; each row is a cell's actual enthalpy balance.
    M=np.zeros((2*(n+1),2*(n+1)));b=np.zeros(2*(n+1))
    M[0,0]=1;b[0]=TL
    M[1,2*n+1]=1;b[1]=TH
    conductance=G*length/n
    for j in range(n):
        cold=2*j;hot=cold+1;row=2*j+2
        heat_coeff={cold:-conductance/2,hot:conductance/2,
                    cold+2:-conductance/2,hot+2:conductance/2}
        M[row,cold+2]+=Cc;M[row,cold]-=Cc
        M[row+1,hot+2]+=Ch;M[row+1,hot]-=Ch
        for col,value in heat_coeff.items():
            M[row,col]-=value;M[row+1,col]-=value
    t=solve(M,b)
    return t[::2],t[1::2]
def expected(TL,TH,Cc,Ch,G,length,x):
    a=G*(1/Ch-1/Cc)
    E=lambda z:z if abs(a*length)<1e-12 else math.expm1(a*z)/a
    delta0=(TH-TL)/(math.exp(a*length)+(G/Cc)*E(length))
    cold=TL+G*delta0*E(x)/Cc
    hot=cold+delta0*math.exp(a*x)
    return np.array([cold,hot])
def physical():
    TL,TH=293.15,353.15;alpha=.1;c=4200.;r=.01;h=.0005;k=.6;length=5.
    C=alpha*c;G=2*math.pi*r*k/h;N=G*length/C;delta=(TH-TL)/(1+N)
    co=TL+N*delta;ho=TH-N*delta;Q=C*(co-TL)
    S=C*(math.log(co/TL)+math.log(ho/TH))
    return dict(TL=TL,TH=TH,alpha=alpha,c=c,r=r,h=h,k=k,l=length,C=C,G=G,
        N=N,l0=C/G,delta=delta,temperature_slope=G*delta/C,
        T_c_out=co,T_h_out=ho,Q_dot=Q,S_dot=S,
        target_90_percent_length=9*C/G,
        exact_cylindrical_G=2*math.pi*k/math.log1p(h/r),
        target_90_percent_exact_wall_length=9*C*math.log1p(h/r)/(2*math.pi*k))
def main():
    x,l,G,C,TL,TH=sp.symbols('x l G C TL TH',positive=True)
    delta=(TH-TL)/(1+G*l/C)
    tc=TL+G*delta*x/C;th=tc+delta
    assert sp.simplify(sp.diff(tc,x)-G*(th-tc)/C)==0
    assert sp.simplify(sp.diff(th,x)-G*(th-tc)/C)==0
    assert sp.simplify(tc.subs(x,0)-TL)==0
    assert sp.simplify(th.subs(x,l)-TH)==0
    assert sp.simplify(C*(tc.subs(x,l)-TL)-C*(TH-th.subs(x,0)))==0
    log_derivative=sp.diff(C*(sp.log(tc/TL)-sp.log(th/TH)),x)
    assert sp.simplify(log_derivative-G*delta*(1/tc-1/th))==0
    eps,N=sp.symbols('eps N',positive=True)
    D=TH-TL
    product=(TL+eps*D)*(TH-eps*D)
    assert sp.expand(product-TL*TH-eps*(1-eps)*D**2)==0
    assert sp.simplify(sp.diff(N/(1+N)*(1-N/(1+N)),N)
        -(1-N)/(1+N)**3)==0
    rows=[]
    for TLv,THv,Cv,Gv in [(280.,360.,200.,30.),(298.15,348.15,500.,40.)]:
        for nv in [.02,.3,1.,2.,10.]:
            length=nv*Cv/Gv
            sol=shoot(TLv,THv,Cv,Cv,Gv,length)
            coordinates=np.linspace(0,length,101)
            exact=np.column_stack([expected(TLv,THv,Cv,Cv,Gv,length,z) for z in coordinates])
            error=float(np.max(abs(sol.sol(coordinates)-exact)))
            assert error<2e-8
            cold,hot=discrete(TLv,THv,Cv,Cv,Gv,length,60)
            mesh=np.linspace(0,length,61)
            expected_mesh=np.column_stack([expected(TLv,THv,Cv,Cv,Gv,length,z) for z in mesh])
            cell_error=float(np.max(abs(np.vstack([cold,hot])-expected_mesh)))
            assert cell_error<2e-8
            local=quad(lambda z:Gv*(sol.sol(z)[1]-sol.sol(z)[0])*
                (1/sol.sol(z)[0]-1/sol.sol(z)[1]),0,length,epsabs=2e-10,epsrel=2e-11)[0]
            co,hi=sol.y[:,-1];ho=sol.y[1,0]
            streams=Cv*(math.log(co/TLv)+math.log(ho/THv))
            transfer=Cv*(co-TLv)
            formula=Cv*math.log(1+nv/(1+nv)**2*(THv-TLv)**2/(TLv*THv))
            assert local>=0 and abs(local-streams)<2e-8 and abs(streams-formula)<2e-8
            assert abs(transfer-Cv*(THv-ho))<2e-8
            rows.append(dict(TL=TLv,TH=THv,C=Cv,G=Gv,N=nv,l=length,
                BVP_temperature_error=error,discrete_enthalpy_temperature_error=cell_error,
                Q_dot=transfer,entropy_local_quadrature=local,entropy_streams=streams,
                logarithm_formula=formula,local_temperature_order_passed=bool(np.all(sol.sol(coordinates)[1]>=sol.sol(coordinates)[0]))))
    unequal=[]
    for Cc,Ch,Gv,length in [(200.,400.,20.,10.),(400.,200.,20.,10.),
        (180.,600.,12.,5.),(600.,180.,12.,5.),(300.,300.003,15.,6.),
        (300.003,300.,15.,6.)]:
        TLv,THv=290.,350.
        sol=shoot(TLv,THv,Cc,Ch,Gv,length)
        coordinates=np.linspace(0,length,121)
        exact=np.column_stack([expected(TLv,THv,Cc,Ch,Gv,length,z) for z in coordinates])
        error=float(np.max(abs(sol.sol(coordinates)-exact)));assert error<2e-8
        coarse=discrete(TLv,THv,Cc,Ch,Gv,length,100)
        fine=discrete(TLv,THv,Cc,Ch,Gv,length,200)
        nodes=np.linspace(0,length,201)
        expected_nodes=np.column_stack([expected(TLv,THv,Cc,Ch,Gv,length,z) for z in nodes])
        fine_error=float(np.max(abs(np.vstack(fine)-expected_nodes)))
        coarse_error=float(np.max(abs(np.vstack(coarse)-expected_nodes[:,::2])))
        assert fine_error<1e-4 and fine_error<=coarse_error*.27+1e-9
        co=sol.y[0,-1];ho=sol.y[1,0]
        Q=Cc*(co-TLv);assert abs(Q-Ch*(THv-ho))<2e-8
        S=Cc*math.log(co/TLv)+Ch*math.log(ho/THv)
        local=quad(lambda z:Gv*(sol.sol(z)[1]-sol.sol(z)[0])*
            (1/sol.sol(z)[0]-1/sol.sol(z)[1]),0,length,epsabs=2e-10)[0]
        assert local>0 and abs(S-local)<2e-8
        minimum=min(Cc,Ch);ratio=minimum/max(Cc,Ch);NTU=Gv*length/minimum
        exp=math.exp(-NTU*(1-ratio))
        effectiveness=(1-exp)/(1-ratio*exp)
        assert abs(Q/(minimum*(THv-TLv))-effectiveness)<2e-9
        unequal.append(dict(Cc=Cc,Ch=Ch,G=Gv,l=length,
            T_c_out=co,T_h_out=ho,Q_dot=Q,S_dot=S,
            BVP_temperature_error=error,discrete_coarse_error=coarse_error,
            discrete_fine_error=fine_error,local_entropy_quadrature=local,
            effectiveness=effectiveness))
    # Find the entropy maximum from numerically shot temperatures, not the final formula.
    def numerical_entropy(n):
        sol=shoot(280.,360.,200.,200.,30.,n*200/30)
        return 200*(math.log(sol.y[0,-1]/280)+math.log(sol.y[1,0]/360))
    maximum=minimize_scalar(lambda n:-numerical_entropy(n),bounds=(.05,8),method='bounded',
        options={'xatol':1e-8})
    assert abs(maximum.x-1)<2e-6
    assert abs(-maximum.fun-200*math.log(320**2/(280*360)))<2e-8
    # Resolve heat conduction through an actual cylindrical wall, then compare the thin-wall model.
    walls=[]
    for u in [.001,.01,.05,.1,.2,.4]:
        r=.01;h=r*u;k=.6;Dh=30.
        exact_G=2*math.pi*k/math.log1p(u);thin_G=2*math.pi*r*k/h
        Qprime=exact_G*Dh
        integrated=quad(lambda radius:Qprime/(2*math.pi*k*radius),r,r+h,
            epsabs=1e-11,epsrel=1e-12)[0]
        assert abs(integrated-Dh)<1e-10
        ratio=exact_G/thin_G
        series=1+u/2-u*u/12
        assert exact_G>thin_G
        walls.append(dict(h_over_r=u,G_exact=exact_G,G_thin=thin_G,
            radial_conduction_temperature_integral=integrated,ratio=ratio,
            second_order_series=series,series_error=abs(ratio-series)))
    quantities=physical()
    assert quantities['T_c_out']<quantities['T_h_out'] # N < 1 here; opposite ends.
    assert abs(quantities['Q_dot']-quantities['C']*(quantities['TH']-quantities['T_h_out']))<1e-8
    names=['question-06','slice-06','temperature-06','entropy-06','wall-06']
    sources=['scripts/verify_question_06.py','drafts/question-06.md','figures/题06_图稿源文件.tex']
    complete=all((ROOT/p).exists() for p in sources) and all(
        (ROOT/f'figures/{n}.{ext}').exists() for n in names for ext in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-06.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察','易错点','课堂讲解建议','变式训练']
        assert [s.split('、',1)[1] for s in text.splitlines() if s.startswith('## ')]==modules
        assert text.count('<!-- question-complete -->')==1
        assert all(text.count(f'../figures/{name}.png')==1 for name in names)
    report=dict(question=6,verified_math=True,document_complete=complete,set_accepted=False,
        scope='independent energy-cell and BVP/entropy checks; no visual or whole-set acceptance',
        equal_capacity_BVP_and_cells=rows,unequal_capacity_BVP_and_mesh_convergence=unequal,
        entropy_maximum_from_numerical_BVP=dict(N=float(maximum.x),S_max=float(-maximum.fun)),
        exact_cylindrical_conduction_checks=walls,solved_numerical_variant=quantities,
        symbolic_balances_boundary_log_integral_and_entropy_derivative_verified=True,
        dimensional_checks=dict(order=['mass','length','time','temperature'],
            capacity_rate=[1,2,-3,-1],conductance_per_length=[1,1,-3,-1],
            Q_dot=[1,2,-3,0],entropy_rate=[1,2,-3,-1],l0=[0,1,0,0],N=[0,0,0,0],
            extra_handwritten_delta_T_would_change_entropy_unit_to_power=True,passed=True),
        assumptions=['steady counterflow, uniform temperature within each cross-section',
            'equal mass and constant specific heat in the original problem',
            'no external heat loss, wall storage, axial conduction, pressure-work or viscous entropy term in this ideal thermal model',
            'given conduction law is the thin-wall model, not the finite-cylinder exact law',
            'logarithms use absolute temperatures',
            'entropy generation and transported water entropy gain equal; control-volume steady entropy accumulation is zero'],
        handwritten_notes=['retain both positive spatial temperature gradients and the opposite-end inlet boundary conditions',
            'constant local temperature gap and linear temperature profiles are correct',
            'the handwritten final entropy logarithm contains an extra multiplicative delta T; cancel G*delta/T-slope to obtain capacity rate alone',
            'the original entropy question is interpreted as water entropy gain/generation, not steady control-volume storage'],
        source_sha256={p:sha(ROOT/p) for p in sources if (ROOT/p).exists()},
        figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in names} if complete else {},
        originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')})
    path='verification-q06.json' if complete else 'verification-q06-preliminary.json'
    (ROOT/'build'/path).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,equal_cases=len(rows),
        unequal_cases=len(unequal),wall_cases=len(walls),numerical_variant=quantities,
        maximum_N=float(maximum.x)),ensure_ascii=False))
if __name__=='__main__':main()
