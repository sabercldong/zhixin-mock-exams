"""两腔换气以开系统焓流独立积分；与集中参数等容及理想回热分开。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
R=8.31446261815324

def actual_transfer(n,Tc,Th,Cv,volume,reverse=False):
    delta=Th-Tc;Cp=Cv+R
    def state(f):
        nh=n*(1-f) if reverse else n*f
        dnh=-n if reverse else n
        nc=n-nh;dnc=-dnh
        p=R*(nh*Th+nc*Tc)/volume
        dp=R*(dnh*Th+dnc*Tc)/volume
        vh=nh*R*Th/p;vc=volume-vh
        dvh=R*Th*(dnh*p-nh*dp)/p**2;dvc=-dvh
        h_flow=Cp*(Th if reverse else Tc)
        qh=Cv*Th*dnh+p*dvh-h_flow*dnh
        qc=Cv*Tc*dnc+p*dvc-h_flow*dnc
        assert abs(p*vh-nh*R*Th)<1e-9
        assert abs(p*vc-nc*R*Tc)<1e-9
        assert abs(p*(dvh+dvc))<1e-9
        assert abs(qh+qc-Cv*delta*dnh)<1e-9
        return qh,qc,p*dvh,p*dvc
    values=[quad(lambda f:state(f)[j],0,1,epsabs=1e-9)[0] for j in range(4)]
    B=n*R*Tc*Th/delta*math.log(Th/Tc)
    expected=[n*Cv*delta-n*R*Tc+B,n*R*Tc-B,B,-B] if not reverse else [
        n*R*Th-B,-n*Cv*delta-n*R*Th+B,-B,B]
    for val,exp in zip(values,expected):assert abs(val-exp)<1e-8
    return dict(Q_hot_J=values[0],Q_cold_J=values[1],W_hot_J=values[2],W_cold_J=values[3],
                net_heat_J=values[0]+values[1])

def main():
    f,tc,th,N,gV,rr=sp.symbols('f Tc Th n0 V R',positive=True)
    p=N*rr*(tc+(th-tc)*f)/gV
    vh=N*f*rr*th/p;vc=N*(1-f)*rr*tc/p
    assert sp.simplify(vh+vc-gV)==0
    assert sp.simplify(p*sp.diff(vh,f)-N*rr*tc*th/(tc+(th-tc)*f))==0
    cases=[]
    for n,Tc,Th,ratio,V2 in [(1.,300.,600.,2.,.012),(.04,250.,500.,3.,.001),
                             (.1,300.,450.,1.5,.002),(2.,290.,300.,1.1,.02)]:
        Cv=2.5*R;Cp=3.5*R;V1=V2*ratio;delta=Th-Tc
        forward=actual_transfer(n,Tc,Th,Cv,V2)
        backward=actual_transfer(n,Tc,Th,Cv,V1,True)
        work_cold=quad(lambda v:n*R*Tc/v,V1,V2,epsabs=1e-9)[0]
        work_hot=quad(lambda v:n*R*Th/v,V2,V1,epsabs=1e-9)[0]
        work=work_cold+work_hot
        assert abs(work-n*R*delta*math.log(ratio))<1e-8
        qh=work_hot+forward['Q_hot_J']+backward['Q_hot_J']
        qc=work_cold+forward['Q_cold_J']+backward['Q_cold_J']
        assert abs(qh-(work_hot+n*Cp*delta))<1e-8
        assert abs(qh+qc-work)<1e-8
        sgen=-qh/Th-qc/Tc
        assert abs(sgen-n*Cp*delta**2/(Tc*Th))<1e-8 and sgen>0
        concentrated_qh=work_hot+n*Cv*delta
        eta_two=work/qh;eta_single=work/concentrated_qh;eta_regen=work/work_hot
        assert 0<eta_two<eta_single<eta_regen<1
        assert abs(eta_regen-(1-Tc/Th))<1e-14
        rows=dict(n0_mol=n,Tc_K=Tc,Th_K=Th,volume_ratio=ratio,V2_m3=V2,
                  transfer_to_hot=forward,transfer_to_cold=backward,
                  W_compression_J=work_cold,W_expansion_J=work_hot,W_cycle_J=work,
                  Q_hot_two_chamber_J=qh,Q_cold_two_chamber_J=qc,
                  entropy_generation_J_per_K=sgen,
                  efficiency_two_chamber=eta_two,efficiency_concentrated=eta_single,
                  efficiency_perfect_regen=eta_regen,
                  state_pressures_Pa=[n*R*Tc/V1,n*R*Tc/V2,n*R*Th/V2,n*R*Th/V1])
        cases.append(rows)
    base=cases[0]
    # 完全回热时流入端焓等于接收腔温度的Cp*T，
    # 各腔仍有热交换，但往返净量为零，而非每一阶段均为零。
    n=1.;Tc=300.;Th=600.;Cv=2.5*R;Cp=3.5*R;delta=Th-Tc
    B=n*R*Tc*Th/delta*math.log(Th/Tc)
    qh2_regen=base['transfer_to_hot']['Q_hot_J']-n*Cp*delta
    qc4_regen=base['transfer_to_cold']['Q_cold_J']+n*Cp*delta
    assert abs(qh2_regen+base['transfer_to_cold']['Q_hot_J'])<1e-9
    assert abs(qc4_regen+base['transfer_to_hot']['Q_cold_J'])<1e-9
    variants=dict(partial_regen_eta_half=base['W_cycle_J']/(base['W_expansion_J']+.5*n*Cp*delta),
                  minimum_eps_for_eta_0_3=1-(base['W_cycle_J']/.3-base['W_expansion_J'])/(n*Cp*delta),
                  mass_half_hot_volume_fraction=Th/(Tc+Th),
                  mass_half_pressure_Pa=n*R*(Tc+Th)/(2*.012))
    eps=variants['minimum_eps_for_eta_0_3']
    assert 0<eps<1
    assert abs(base['W_cycle_J']/(base['W_expansion_J']+(1-eps)*n*Cp*delta)-.3)<1e-14
    paths=['scripts/verify_question_07.py'];draft=ROOT/'drafts/question-07.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():paths.append('drafts/question-07.md')
    if (ROOT/'figures/题07_图稿源文件.tex').exists():paths.append('figures/题07_图稿源文件.tex')
    result=dict(question=7,verified_math=True,document_complete=complete,cases=cases,variants=variants,
                model_note='两腔无储热、集中参数等容、完全回热三种模型不得混用',
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    dest=ROOT/'build'/('verification-q07.json' if complete else 'verification-q07-preliminary.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=7,passed=True,base_case=base,variants=variants),ensure_ascii=False))

if __name__=='__main__':main()
