"""费马点、受限距离和：独立坐标极小化、几何方程及端点核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.optimize import brentq,minimize_scalar,root,minimize
ROOT=Path(__file__).resolve().parents[1]
def main():
    s,p,h=sp.symbols('s p h',real=True);hpos=sp.symbols('hpos',positive=True)
    rr=sp.sqrt((s-p)**2+hpos**2)
    assert sp.simplify(sp.diff(rr,s,2)-hpos**2/rr**3)==0
    A=np.array([.5,math.sqrt(3)/2]);B=np.array([0.,0.]);C=np.array([1.,0.])
    t=math.radians(15);u=np.array([-math.sin(t),-math.cos(t)])
    L=A[1]/math.cos(t);D=A+L*u
    F=lambda s:s+np.linalg.norm(A+s*u-B)+np.linalg.norm(A+s*u-C)
    der=lambda s:1+sum(np.dot(A+s*u-X,u)/np.linalg.norm(A+s*u-X) for X in [B,C])
    hess=lambda s:sum((np.linalg.norm(A-X)**2-np.dot(A-X,u)**2)/np.linalg.norm(A+s*u-X)**3 for X in [B,C])
    sol=brentq(der,0,L,xtol=1e-14);O=A+sol*u
    direct=minimize_scalar(F,bounds=(0,L),method='bounded',options={'xatol':1e-14})
    assert abs(sol-direct.x)<2e-8 and abs(F(sol)-direct.fun)<1e-12
    assert der(0)<0 and abs(der(L)-1)<1e-14
    assert all(hess(v)>0 for v in np.linspace(0,L,200))
    cos_alpha=np.dot(B-O,u)/np.linalg.norm(B-O);cos_beta=np.dot(C-O,u)/np.linalg.norm(C-O)
    alpha=math.acos(cos_alpha);beta=math.acos(cos_beta)
    eq=lambda z:[math.cos(z[0])+math.cos(z[1])-1,
        math.sin(t)*math.sin(z[1])*math.sin(math.radians(75)-z[0])-
        math.sin(math.radians(45))*math.sin(z[0])*math.sin(math.radians(105)-z[1])]
    trig=root(eq,[math.radians(34),math.radians(80)],tol=1e-12)
    assert trig.success and np.linalg.norm(eq(trig.x))<1e-12
    assert np.linalg.norm(trig.x-[alpha,beta])<1e-12
    normal=np.array([-u[1],u[0]])
    vectors=(A-O)/np.linalg.norm(A-O)+(B-O)/np.linalg.norm(B-O)+(C-O)/np.linalg.norm(C-O)
    normal_coefficient=np.dot(vectors,normal)
    assert abs(np.dot(vectors,u))<1e-12
    assert abs(normal_coefficient-(math.sin(beta)-math.sin(alpha)))<1e-12
    # 坐标旋转路线独立检查，不先用120度作为优化器约束。
    Fxy=lambda xy:sum(np.linalg.norm(xy-X) for X in [A,B,C])
    unrestricted=minimize(Fxy,[.48,.27],method='BFGS',tol=1e-11)
    O0=np.array([.5,math.sqrt(3)/6]);assert abs(Fxy(unrestricted.x)-math.sqrt(3))<1e-12
    rot=np.array([[.5,math.sqrt(3)/2],[-math.sqrt(3)/2,.5]])
    Os=rot@O0;Cs=rot@C
    assert abs(np.linalg.norm(Os-O0)-np.linalg.norm(O0-B))<1e-14
    assert abs(np.linalg.norm(Cs-Os)-np.linalg.norm(C-O0))<1e-14
    assert abs(Fxy(O0)-np.linalg.norm(A-Cs))<1e-14
    generic=[]
    # 非正三角形独立最小化；旋转下界、角度与面积式交叉核验。
    for axy,bxy,cxy in [([.2,1.2],[0,0],[1.3,0]),([.7,.9],[0,0],[1.5,0]),([.1,.9],[-.6,0],[.8,0])]:
        AA,BB,CC=map(lambda z:np.array(z,float),[axy,bxy,cxy])
        ff=lambda xy:sum(np.linalg.norm(xy-X) for X in [AA,BB,CC])
        out=minimize(ff,(AA+BB+CC)/3,method='BFGS',options={'gtol':1e-10})
        oo=out.x;dirs=[(X-oo)/np.linalg.norm(X-oo) for X in [AA,BB,CC]]
        dots=[float(dirs[i]@dirs[j]) for i,j in [(0,1),(1,2),(2,0)]]
        assert max(abs(v+.5) for v in dots)<2e-7
        aa=np.linalg.norm(BB-CC);bb=np.linalg.norm(CC-AA);cc=np.linalg.norm(AA-BB)
        delta=abs(float(np.linalg.det(np.stack([BB-AA,CC-AA]))))/2
        expected=math.sqrt((aa*aa+bb*bb+cc*cc+4*math.sqrt(3)*delta)/2)
        assert abs(out.fun-expected)<1e-12
        generic.append(dict(vertices=[axy,bxy,cxy],point=oo.tolist(),minimum=out.fun,pairwise_cosines=dots))
    # 带解变式：中线、钝角顶点、加权顶点、约束于一条边。
    median_z=1/(2*math.sqrt(3));median_s=math.sqrt(3)/2-median_z
    fmed=lambda x:x+2*math.sqrt(.25+(math.sqrt(3)/2-x)**2)
    direct_med=minimize_scalar(fmed,bounds=(0,math.sqrt(3)/2),method='bounded')
    assert abs(direct_med.fun-math.sqrt(3))<1e-10
    endpoint_bound=1-2*math.cos(math.radians(65));assert endpoint_bound>0
    weighted_bound=2-math.sqrt(3);assert weighted_bound>0
    fedge=lambda x:1+math.sqrt((x-.5)**2+.75)
    direct_edge=minimize_scalar(fedge,bounds=(0,1),method='bounded')
    assert abs(direct_edge.x-.5)<1e-12 and abs(direct_edge.fun-(1+math.sqrt(3)/2))<1e-12
    row=dict(A=A.tolist(),B=B.tolist(),C=C.tolist(),D=D.tolist(),AD_over_a=L,AO_over_a=sol,O=O.tolist(),
             alpha_deg=math.degrees(alpha),beta_deg=math.degrees(beta),minimum_over_a=F(sol),
             derivative_A=der(0),derivative_D=der(L),endpoint_A=F(0),endpoint_D=F(L),
             reaction_over_mg=abs(normal_coefficient),OB_over_a=np.linalg.norm(O-B),OC_over_a=np.linalg.norm(O-C),
             bisection=[dict(s_over_a=v,derivative=der(v)) for v in [.58,.59,.583,.584,.5836,.5837,sol]])
    paths=['scripts/verify_question_08.py'];draft=ROOT/'drafts/question-08.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():paths.append('drafts/question-08.md')
    if (ROOT/'figures/题08_图稿源文件.tex').exists():paths.append('figures/题08_图稿源文件.tex')
    result=dict(question=8,verified_math=True,document_complete=complete,constrained=row,generic=generic,
                unrestricted=dict(minimum=Fxy(O0),point=O0.tolist(),rotated_O=Os.tolist(),rotated_C=Cs.tolist()),
                variants=dict(median_AO_over_a=median_s,median_minimum=math.sqrt(3),
                obtuse_endpoint_strict_bound=endpoint_bound,weighted_endpoint_strict_bound=weighted_bound,edge_minimum=direct_edge.fun),
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    dest=ROOT/'build'/('verification-q08.json' if complete else 'verification-q08-preliminary.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,constrained=row,variants=result['variants']),ensure_ascii=False))
if __name__=='__main__':main()
