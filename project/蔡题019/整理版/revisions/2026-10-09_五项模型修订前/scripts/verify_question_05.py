"""同一事件坐标、延迟场独立求根、磁场与不变量及球面通量核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
C=299792458.0;K=8.9875517923e9

def fields(q,beta,position,time):
    u=beta*C;g=1/math.sqrt(1-beta*beta)
    r=np.array(position,float)+np.array([u*time,0.,0.])
    rest=np.array([g*r[0],r[1],r[2]])
    E_rest=K*q*rest/np.linalg.norm(rest)**3
    E=np.array([E_rest[0],g*E_rest[1],g*E_rest[2]])
    velocity=np.array([-u,0.,0.]);B=np.cross(velocity,E)/C**2
    # 不用最终闭式回代：由迟滞光锥数值求发射时间，再使用速度场。
    equation=lambda tau:C*tau-np.linalg.norm(r+velocity*tau)
    upper=np.linalg.norm(r)/(C-abs(u))*1.01
    age=brentq(equation,0.,upper,xtol=1e-24,rtol=1e-14)
    retarded=r+velocity*age;distance=np.linalg.norm(retarded);n=retarded/distance
    betavec=velocity/C
    E_delay=K*q*(1-beta*beta)*(n-betavec)/((1-n@betavec)**3*distance**2)
    B_delay=np.cross(n,E_delay)/C
    assert np.linalg.norm(E_delay-E)/np.linalg.norm(E)<2e-11
    scale=max(np.linalg.norm(B),np.linalg.norm(E)/C*1e-9)
    assert np.linalg.norm(B_delay-B)/scale<2e-7
    invariant=E@E-C*C*(B@B);expected=E_rest@E_rest
    assert abs(invariant-expected)/expected<2e-11
    assert abs(E@B)<np.linalg.norm(E)*max(np.linalg.norm(B),1e-30)*1e-12+1e-25
    return dict(E_V_per_m=E.tolist(),B_T=B.tolist(),rest_coordinates_m=rest.tolist(),
                emission_age_s=age,relative_delay_error=float(np.linalg.norm(E_delay-E)/np.linalg.norm(E)))

def main():
    b,x,y,z=sp.symbols('beta x y z',real=True);g=1/sp.sqrt(1-b*b)
    D=g*g*x*x+y*y+z*z
    E=sp.Matrix([g*x,g*y,g*z])/D**sp.Rational(3,2)
    cB=sp.Matrix([0,b*E[2],-b*E[1]])
    assert sp.simplify(E.dot(E)-cB.dot(cB)-1/D**2)==0
    # 在横轴/纵轴分别约化；不把负坐标的方向遗漏。
    xp,yp=sp.symbols('xp yp',positive=True)
    assert sp.simplify(E.subs({x:0,y:yp,z:0})[1]-g/yp**2)==0
    subluminal=sp.symbols('one_minus_beta_squared',positive=True)
    axis_residual=E.subs({x:xp,y:0,z:0})[0]-(1-b*b)/xp**2
    assert sp.simplify(axis_residual.subs(b*b,1-subluminal))==0
    cases=[]
    for beta in [0.,.2,.6,.95,-.6]:
        for q,position,time in [(1e-9,[0.,.2,0.],0.),(1e-9,[.2,0.,0.],0.),
                               (-2e-9,[-.12,.16,.05],2e-10),(1e-9,[.12,.16,0.],0.)]:
            row=fields(q,beta,position,time);row.update(beta=beta,q_C=q,position_m=position,time_s=time)
            cases.append(row)
    flux=[]
    for beta in [0.,.2,.6,.95,.99]:
        # 比库仑通量4*pi*k*q的比值，应为1。
        ratio=(1-beta*beta)*quad(lambda mu:(1-beta*beta+beta*beta*mu*mu)**(-1.5),-1,1,
                                 epsabs=1e-11,epsrel=1e-11)[0]/2
        assert abs(ratio-1)<1e-10;flux.append(dict(beta=beta,normalized_flux=ratio))
    examples=dict(axis_A=fields(1e-9,.6,[0.,.2,0.],0.),axis_B=fields(1e-9,.6,[.2,0.,0.],0.),
                  oblique=fields(1e-9,.6,[.12,.16,0.],0.))
    negative_A=fields(-1e-9,-.6,[0.,-.2,0.],0.)
    negative_B=fields(-1e-9,-.6,[-.2,0.,0.],0.)
    assert negative_A['E_V_per_m'][1]>0 and negative_A['B_T'][2]>0
    assert negative_B['E_V_per_m'][0]>0
    ratio_A=fields(2e-9,math.sqrt(3)/2,[0.,.1,0.],0.)
    ratio_B=fields(2e-9,math.sqrt(3)/2,[.1,0.,0.],0.)
    assert abs(ratio_A['E_V_per_m'][1]/ratio_B['E_V_per_m'][0]-8)<1e-12
    examples.update(negative_A=negative_A,negative_B=negative_B,inverse_ratio_A=ratio_A,inverse_ratio_B=ratio_B)
    paths=['scripts/verify_question_05.py'];draft=ROOT/'drafts/question-05.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():paths.append('drafts/question-05.md')
    if (ROOT/'figures/题05_图稿源文件.tex').exists():paths.append('figures/题05_图稿源文件.tex')
    result=dict(question=5,verified_math=True,document_complete=complete,examples=examples,cases=cases,
                sphere_flux=flux,source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    dest=ROOT/'build'/('verification-q05.json' if complete else 'verification-q05-preliminary.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=5,passed=True,cases=len(cases),examples=examples,sphere_flux=flux),ensure_ascii=False))

if __name__=='__main__':main()
