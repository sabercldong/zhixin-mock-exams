"""按接线约束直接解瞬时电路，积分功率并核对原边能量及等效阻抗。"""
from pathlib import Path
import hashlib,json,math
import sympy as sp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
def main():
    U,N1,N2,N3,r=sp.symbols('U N1 N2 N3 r',positive=True)
    e2=N2*U/N1;e3=N3*U/N1
    a2,b2,a3,b3,I=sp.symbols('a2 b2 a3 b3 I',real=True)
    # 串联相助：b2=a3，r+r从a2回到b3；串联相消：b2=b3，负载从a2回到a3。
    plus=sp.solve([a2-b2-e2,a3-b3-e3,b2-a3,b3,a2-b3-2*r*I],[a2,b2,a3,b3,I],dict=True)[0]
    minus=sp.solve([a2-b2-e2,a3-b3-e3,b2-b3,b3,a2-a3-2*r*I],[a2,b2,a3,b3,I],dict=True)[0]
    assert sp.simplify(plus[I]-(e2+e3)/(2*r))==0
    assert sp.simplify(minus[I]-(e2-e3)/(2*r))==0
    formula={'independent':(N2**2+N3**2)*U**2/(2*r*N1**2),
             'aiding':(N2+N3)**2*U**2/(4*r*N1**2),
             'opposing':(N2-N3)**2*U**2/(4*r*N1**2)}
    assert sp.simplify(formula['independent']-formula['aiding']-formula['opposing'])==0
    rows=[]
    for n1,n2,n3,rv,u0 in [(200,100,60,10,12*math.sqrt(2)),(150,70,70,8,20),(150,50,90,8,20)]:
        omega=2*math.pi*50;period=2*math.pi/omega
        for case in formula:
            def currents(t):
                uu=u0*math.sin(omega*t);v2=n2*uu/n1;v3=n3*uu/n1
                if case=='independent':i2,i3=v2/rv,v3/rv;return uu,i2,i3,(n2*i2+n3*i3)/n1
                loop=(v2+v3)/(2*rv) if case=='aiding' else (v2-v3)/(2*rv)
                i3=loop if case=='aiding' else -loop
                return uu,loop,i3,(n2*loop+n3*i3)/n1
            actual=quad(lambda t:rv*(currents(t)[1]**2+currents(t)[2]**2),0,period,epsabs=1e-12)[0]/period
            expected=float(formula[case].subs({N1:n1,N2:n2,N3:n3,r:rv,U:u0}))
            assert abs(actual-expected)<1e-10
            original=quad(lambda t:currents(t)[0]*currents(t)[3],0,period,epsabs=1e-12)[0]/period
            assert abs(actual-original)<1e-10
            winding_power=[]
            for ns,idx in [(n2,1),(n3,2)]:
                value=quad(lambda t:ns/n1*currents(t)[0]*currents(t)[idx],0,period,epsabs=1e-12)[0]/period
                winding_power.append(value)
            assert abs(sum(winding_power)-actual)<1e-10
            rows.append(dict(N1=n1,N2=n2,N3=n3,r=rv,U0=u0,case=case,numerical_average_heat=actual,
                             formula_heat=expected,primary_average_power=original,secondary_delivered_power=winding_power))
    # 带解变式：匝数不等/极性切换；不等负载电阻；反推两次测量。
    v2,v3,r2,r3=6,3.6,10,20
    unequal=dict(independent=v2*v2/r2+v3*v3/r3,aiding=(v2+v3)**2/(r2+r3),opposing=(v2-v3)**2/(r2+r3))
    assert abs(unequal['aiding']-3.072)<1e-12
    assert abs(unequal['opposing']-.192)<1e-12
    vplus=math.sqrt(2*10*4.608);vminus=math.sqrt(2*10*.288)
    recovered=((vplus+vminus)/2,(vplus-vminus)/2)
    assert abs(recovered[0]-6)<1e-12 and abs(recovered[1]-3.6)<1e-12
    extrema=[]
    for total in range(2,25):
        cases=[(a,total-a,(a-(total-a))**2) for a in range(1,total)]
        minimum=min(v[2] for v in cases);maximum=max(v[2] for v in cases)
        assert minimum==total%2 and maximum==(total-2)**2
        extrema.append(dict(total_turns=total,min_difference_squared=minimum,max_difference_squared=maximum))
    # 同一sin波形的平均平方及相反匝数序情况均由积分核对，不仅回代最终式。
    source=['scripts/verify_question_03.py'];draft=ROOT/'drafts/question-03.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():source.append('drafts/question-03.md')
    for p in ['figures/题03_图稿源文件.tex','scripts/generate_question_03_windings.py','figures/core-03-coordinates.tex']:
        if (ROOT/p).exists():source.append(p)
    result=dict(question=3,verified_math=True,document_complete=complete,circuit_solutions={k:str(s) for k,s in [('aiding',plus),('opposing',minus)]},
                numerical_integrals=rows,unequal_resistors=unequal,recovered_secondary_voltages=recovered,integer_extrema=extrema,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source})
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build'/('verification-q03.json' if complete else 'verification-q03-preliminary.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
