"""三体衰变：直接实验室能量求根、三维洛伦兹变换与全区间极值交叉核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.optimize import brentq,minimize_scalar

ROOT=Path(__file__).resolve().parents[1]

def state(p,M=5.,mpi=1.,mu=1.):
    Epi=math.hypot(mpi,p);E=M-Epi;Q2=E*E-p*p
    assert Q2>=4*mu*mu-1e-10
    Q=math.sqrt(Q2);delta=Q2/4-mu*mu
    if abs(delta)<1e-14*max(1.,mu*mu):delta=0.
    b=math.sqrt(max(0.,delta));g=E/Q
    A=p/2;a=g*b;C=a*a-b*b;D=A*A-a*a
    return dict(p=p,Epi=Epi,E=E,Q=Q,b=b,a=a,A=A,C=C,D=D,gamma=g,beta=p/E)

def cos_direct(s,u,phi=0.):
    v=math.sqrt(max(0.,1-u*u));trans=s['b']*v
    plus=np.array([s['A']+s['a']*u,trans*math.cos(phi),trans*math.sin(phi)])
    minus=np.array([s['A']-s['a']*u,-plus[1],-plus[2]])
    n=np.linalg.norm(plus)*np.linalg.norm(minus)
    return None if n<1e-11 else float(np.clip(plus@minus/n,-1.,1.))

def prediction(s):
    A,a,b,C,D=[s[k] for k in ['A','a','b','C','D']]
    if b<1e-12:return dict(kind='degenerate',cos=1.,v=0.)
    if abs(D)<1e-10:return dict(kind='supremum',cos=0.,v=0.)
    if D<0:return dict(kind='antiparallel',cos=-1.,v=0.)
    if D>=C:return dict(kind='symmetric',cos=(A*A-b*b)/(A*A+b*b),v=1.)
    return dict(kind='asymmetric',cos=math.sqrt(D*C/(D*C+A*A*b*b)),v=math.sqrt(D/C))

def main():
    M,mpi,mu=5.,1.,1.
    pmax=math.sqrt((M*M-(mpi+2*mu)**2)*(M*M-(mpi-2*mu)**2))/(2*M)
    # 不预设共速条件：在固定p下直接最小化两粒子的总实验室能量。
    minimal_energy=[]
    for p in [0.,.7,1.4,pmax]:
        def energy(px):return math.hypot(mu,px)+math.hypot(mu,p-px)
        opt=minimize_scalar(energy,bracket=(p/2-.5,p/2,p/2+.5),tol=1e-12)
        assert abs(opt.x-p/2)<1e-6 and abs(opt.fun-2*math.hypot(mu,p/2))<1e-10
        minimal_energy.append(dict(p=p,px=opt.x,E_mu_pair=opt.fun))
    root=brentq(lambda p:math.hypot(mpi,p)+2*math.hypot(mu,p/2)-M,0.,M)
    assert abs(root-pmax)<1e-11
    # 在随机方向上进行真实四动量变换，逐项核验壳条件、守恒及椭球。
    rng=np.random.default_rng(20261008);max_energy=0.;max_surface=0.;max_direct_root=0.
    for p in np.linspace(.05,pmax*.999,23):
        s=state(float(p));E=s['E'];Q=s['Q'];g=s['gamma'];beta=s['beta'];b=s['b']
        for _ in range(51):
            n=rng.normal(size=3);n/=np.linalg.norm(n)
            star=b*n;plus=np.array([g*(star[0]+beta*Q/2),star[1],star[2]])
            minus=np.array([g*(-star[0]+beta*Q/2),-star[1],-star[2]])
            ep=math.sqrt(float(plus@plus)+mu*mu);em=math.sqrt(float(minus@minus)+mu*mu)
            max_energy=max(max_energy,abs(ep+em-E));assert np.linalg.norm(plus+minus-np.array([p,0,0]))<1e-12
            ell=(plus[0]-p/2)**2/s['a']**2+(plus[1]**2+plus[2]**2)/b**2
            max_surface=max(max_surface,abs(ell-1))
        # 从实验室能量方程直接求每个px的横向动量，不使用椭球公式求根。
        for u in np.linspace(-.97,.97,17):
            px=s['A']+s['a']*float(u)
            f=lambda r:math.sqrt(px*px+r*r+mu*mu)+math.sqrt((p-px)**2+r*r+mu*mu)-E
            r=brentq(f,0.,E)
            max_direct_root=max(max_direct_root,abs(r-b*math.sqrt(1-u*u)))
    assert max_energy<1e-11 and max_surface<1e-11 and max_direct_root<1e-9
    # 全区间直接计算两向量夹角；包含对称、非对称、反向、退化及上确界。
    threshold0=brentq(lambda p:state(p)['D'],1.5,1.9,xtol=5e-15)
    threshold1=brentq(lambda p:state(p)['D']-state(p)['C'],threshold0+1e-7,pmax-1e-7,xtol=5e-15)
    rows=[]
    for p in [0.,1.,1.7,1.75,1.8,1.9,pmax]:
        s=state(p);pred=prediction(s)
        grid=np.linspace(0.,1.,20001)
        vals=[cos_direct(s,float(u)) for u in grid];valid=[v for v in vals if v is not None]
        if pred['kind']=='degenerate':optcos=min(valid);uopt=0.
        else:
            idx=int(np.nanargmin([v if v is not None else np.nan for v in vals]));lo=grid[max(0,idx-2)];hi=grid[min(len(grid)-1,idx+2)]
            opt=minimize_scalar(lambda u:cos_direct(s,float(u)),bounds=(lo,hi),method='bounded',options={'xatol':1e-14})
            optcos=min(min(valid),opt.fun);uopt=math.sqrt(max(0.,1-pred['v']**2))
        assert abs(optcos-pred['cos'])<1e-8,(p,optcos,pred)
        # 方位角不影响夹角，仍用非零pz独立验证三维向量。
        if s['b']>1e-12:
            for phi in [.2,1.1,2.3]:assert abs(cos_direct(s,uopt,phi)-pred['cos'])<1e-8
        rows.append(dict(p=p,regime=pred['kind'],Q=s['Q'],A=s['A'],a=s['a'],b=s['b'],D=s['D'],C=s['C'],
                         cosine=pred['cos'],angle_degrees=math.degrees(math.acos(pred['cos'])),v=pred['v'],
                         symmetric_cosine=(s['A']**2-s['b']**2)/(s['A']**2+s['b']**2) if s['A']**2+s['b']**2>0 else None))
    s0=state(threshold0);assert abs(s0['D'])<1e-10 and cos_direct(s0,1.) is None
    approach=[]
    for v in [1e-2,1e-3,1e-4]:
        value=cos_direct(s0,math.sqrt(1-v*v));assert value>0
        approach.append(dict(v=v,cosine=value,angle_degrees=math.degrees(math.acos(value))))
    # 符号验证两次平方后的椭球及极值导数；所有单位保留c。
    A,b,C,D,v=sp.symbols('A b C D v',positive=True)
    tan=2*A*b*v/(D+C*v*v)
    derivative=sp.factor(sp.diff(tan,v));assert sp.simplify(derivative-2*A*b*(D-C*v*v)/(D+C*v*v)**2)==0
    w=math.sqrt(1+threshold1**2)
    assert abs(5*w**3-59*w**2+235*w-277)<1e-10
    threshold_variants=[]
    for delta in [.001,.0001,.00001]:
        mother=3+delta
        direct=brentq(lambda p:math.hypot(1.,p)+2*math.hypot(1.,p/2)-mother,0.,1.,xtol=1e-14)
        leading=math.sqrt(4*delta/3)
        assert abs(direct/leading-1)<delta
        threshold_variants.append(dict(delta=delta,direct_energy_root=direct,threshold_leading=leading,relative_error=direct/leading-1))
    c,E,Q,p,t,r,m=sp.symbols('c E Q p t r m',positive=True)
    ep=E/2+p*c*c*t/E
    residual=sp.expand(ep**2-c*c*((p/2+t)**2+r*r)-m*m*c**4)
    assert sp.simplify(residual-(E**2-p*p*c*c)/4-c*c*t*t*(p*p*c*c/E**2-1)+c*c*r*r+m*m*c**4)==0
    files=['scripts/verify_question_08.py']+[f for f in ['drafts/question-08.md','figures/题08_图稿源文件.tex','scripts/generate_question_08_space.py','figures/momentum-08-space.tex'] if (ROOT/f).exists()]
    complete=(ROOT/'drafts/question-08.md').exists() and sum(line.startswith('## ') for line in (ROOT/'drafts/question-08.md').read_text().splitlines())==9 and '<!-- question-complete -->' in (ROOT/'drafts/question-08.md').read_text()
    report=dict(question=8,verified_math=True,document_complete=complete,numerical_units='c=1, toy masses 5:1:1, not measured particle masses',pion_pmax=pmax,
                direct_energy_minimization=minimal_energy,energy_conservation_max_error=max_energy,ellipsoid_max_residual=max_surface,
                direct_lab_energy_root_max_error=max_direct_root,angle_regimes=rows,threshold_A_equals_a=threshold0,threshold_D_equals_C=threshold1,
                supremum_approach=approach,symbolic_angle_derivative=str(derivative),threshold_variants=threshold_variants,source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    dest=ROOT/'build'/('verification-q08.json' if complete else 'verification-q08-preliminary.json')
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
