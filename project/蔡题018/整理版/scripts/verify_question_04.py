"""按模7规则独立建立21条二极管支路；全5节点与对称2节点分别求解。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import root,minimize
ROOT=Path(__file__).resolve().parents[1]
EDGES=[(i,j) for i in range(7) for j in range(7) if (i-j)%7 in {3,5,6}]
assert len(EDGES)==21
assert {tuple(sorted(e)) for e in EDGES}=={(i,j) for i in range(7) for j in range(i+1,7)}
assert all(sum(a==i for a,b in EDGES)==sum(b==i for a,b in EDGES)==3 for i in range(7))
def circuit(voltage):
    def all_potentials(floating):return np.r_[voltage/2,-voltage/2,floating]
    def residues(allv):
        net=np.zeros(7)
        for a,b in EDGES:
            current=math.expm1(allv[a]-allv[b])
            net[a]+=current;net[b]-=current
        return net
    def jacobian(allv):
        jac=np.zeros((7,7))
        for a,b in EDGES:
            conductance=math.exp(allv[a]-allv[b])
            jac[a,a]+=conductance;jac[b,b]+=conductance
            jac[a,b]-=conductance;jac[b,a]-=conductance
        return jac
    sol=root(lambda v:residues(all_potentials(v))[2:],np.zeros(5),
             jac=lambda v:jacobian(all_potentials(v))[2:,2:],tol=1e-12)
    allv=all_potentials(sol.x);res=residues(allv)
    assert np.max(abs(res[2:]))<2e-12
    assert abs(res[0]+res[1])<2e-12
    assert np.max(abs(allv+allv[[1,0,6,5,4,3,2]]))<2e-12
    assert max(allv[2:])<abs(voltage/2)+1e-12
    assert min(allv[2:])>-abs(voltage/2)-1e-12
    branch_powers=[(allv[a]-allv[b])*math.expm1(allv[a]-allv[b]) for a,b in EDGES]
    assert min(branch_powers)>=0
    power=sum(branch_powers)
    assert abs(power-voltage*res[0])<2e-12
    assert power>=0
    jac=jacobian(allv)
    min_eigenvalue=float(np.min(np.linalg.eigvalsh(jac[2:,2:])))
    assert min_eigenvalue>0
    if voltage==1:
        def energy(v):
            phi=all_potentials(v)
            return sum(math.expm1(phi[a]-phi[b])-(phi[a]-phi[b]) for a,b in EDGES)
        alternate=minimize(energy,np.linspace(-.2,.2,5),jac=lambda v:residues(all_potentials(v))[2:],
                           method='BFGS',options={'gtol':1e-12,'maxiter':1000})
        assert np.max(abs(alternate.x-sol.x))<5e-8
        alt_error=float(np.max(abs(alternate.x-sol.x)))
    else:alt_error=None
    return dict(voltage_dimensionless=voltage,potentials_dimensionless=allv.tolist(),
                residuals_I0=res.tolist(),source_current_I0=float(res[0]),total_diode_power_I0_per_alpha=power,
                minimum_float_jacobian_eigenvalue=min_eigenvalue,independent_energy_minimizer_error=alt_error,
                individual_branch_powers_I0_per_alpha=branch_powers)
def main():
    mp.mp.dps=60
    a=mp.exp(mp.mpf('.5'))
    def first(x,y):return x/y+x/a+x*y-1/(a*x)-1/(x*x)-1/x
    def second(x,y):return y/a+a*y+x*y-1/(y*y)-1/y-x/y
    xx,yy=mp.findroot((first,second),(.99,.96),tol=mp.mpf('1e-55'))
    u1,u2=mp.log(xx),mp.log(yy)
    current=(mp.e+a*yy+a-1/(a*xx)-xx/a-yy/a)
    rows=[circuit(v) for v in [1,.5,2,-1,.001,-.001]]
    assert abs(rows[0]['source_current_I0']-float(current))<1e-12
    assert abs(rows[0]['potentials_dimensionless'][5]-float(u1))<1e-12
    assert abs(rows[0]['potentials_dimensionless'][6]-float(u2))<1e-12
    x,y,aa=sp.symbols('x y a',positive=True)
    F=x/y+x/aa+x*y-1/(aa*x)-1/x**2-1/x
    G=y/aa+aa*y+x*y-1/y**2-1/y-x/y
    derivative=sp.Matrix([F,G]).jacobian([x,y])
    # 小信号极限来自所有21支路独立线性化K7网络，不采用指数解直接宣称。
    incidence=np.zeros((7,21))
    for k,(i,j) in enumerate(EDGES):incidence[i,k]=1;incidence[j,k]=-1
    lap=incidence@incidence.T
    assert np.max(abs(lap-(7*np.eye(7)-np.ones((7,7)))))==0
    small_solution=np.linalg.solve(lap[2:,2:],-lap[2:,:2]@np.array([.5,-.5]))
    small_current=(lap@np.r_[.5,-.5,small_solution])[0]
    assert abs(small_current-3.5)<1e-14
    assert abs(rows[-2]['source_current_I0']/.001-3.5)<.001
    records=[]
    # 报告牛顿迭代中间值，使正文计算可重现而非只公布最终根。
    p=np.array([1.,1.]);aval=math.exp(.5)
    fun=sp.lambdify((x,y,aa),sp.Matrix([F,G]),'numpy')
    jac=sp.lambdify((x,y,aa),derivative,'numpy')
    for k in range(5):
        value=np.asarray(fun(*p,aval),dtype=float).reshape(2)
        J=np.asarray(jac(*p,aval),dtype=float)
        delta=np.linalg.solve(J,-value)
        records.append(dict(k=k,x=float(p[0]),y=float(p[1]),F=float(value[0]),G=float(value[1]),
                            J=J.tolist(),delta=delta.tolist()))
        p+=delta
    assert max(abs(p-[float(xx),float(yy)]))<1e-13
    sources=['scripts/verify_question_04.py']
    complete=False
    for name in ['drafts/question-04.md','drafts/question-04-核验备忘.md','figures/题04_图稿源文件.tex']:
        path=ROOT/name
        if path.exists():
            sources.append(name)
            if name.endswith('question-04.md'):complete='<!-- question-complete -->' in path.read_text()
    figures={path.name:hashlib.sha256(path.read_bytes()).hexdigest()
             for path in sorted((ROOT/'figures').glob('*-04.pdf'))}
    result=dict(question=4,verified_math=True,document_complete=complete,
                edges_anode_to_cathode=EDGES,source_current_mA=mp.nstr(current,45),
                symmetry_variables=dict(x=mp.nstr(xx,45),y=mp.nstr(yy,45),
                    u1_V=mp.nstr(u1,45),u2_V=mp.nstr(u2,45)),
                newton_jacobian=str(derivative),newton_iterations=records,
                full_five_node_checks=rows,small_signal_source_conductance_I0_alpha=small_current,
                figure_pdf_sha256=figures,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources})
    dest=ROOT/'build'/('verification-q04.json' if complete else 'verification-q04-preliminary.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
