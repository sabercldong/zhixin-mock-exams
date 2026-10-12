"""有限柔软载流导线：局部矢量平衡、独立ODE、端点闭合及长度数值核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
def main():
    beta=brentq(lambda q:math.sin(q)/q-.5,1e-6,math.pi,xtol=1e-14)
    R=1/(2*beta);T=R
    angle=math.pi-beta
    def planar_rhs(s,state):
        tx,ty,tz=state[3:]
        return [tx,ty,tz,-ty/T,tx/T,0]
    sol=solve_ivp(planar_rhs,[0,1],[0,0,0,math.cos(beta),-math.sin(beta),0],
                  method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True)
    assert np.linalg.norm(sol.y[:3,-1]-[.5,0,0])<1e-12
    s=np.linspace(0,1,40001);rows=sol.sol(s)
    length=np.linalg.norm(np.diff(rows[:3],axis=1),axis=0).sum()
    assert abs(length-1)<1e-9
    # 独立求解牛顿方程而非采样解析曲线；张力增量和总安培力相消。
    total_ampere=np.cross(np.array([.5,0,0]),[0,0,1])
    anchor_forces=-T*rows[3:,0]+T*rows[3:,-1]
    assert np.linalg.norm(total_ampere+anchor_forces)<1e-12
    center=np.array([.25,R*math.cos(beta),0])
    radii=np.linalg.norm(rows[:3]-center[:,None],axis=0)
    assert np.max(abs(radii-R))<1e-12
    assert 2*beta>math.pi and 2*beta<2*math.pi
    helices=[]
    for n in [1,2,3,7]:
        for delta in [0,.37,1.21]:
            tension=1/(2*math.pi*n);radius=math.sqrt(3)/(4*math.pi*n)
            initial=[0,0,0,.5,math.sqrt(3)/2*math.cos(delta),math.sqrt(3)/2*math.sin(delta)]
            def rhs(s,state):
                tx,ty,tz=state[3:]
                return [tx,ty,tz,0,-tz/tension,ty/tension]
            solution=solve_ivp(rhs,[0,1],initial,method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True)
            assert np.linalg.norm(solution.y[:3,-1]-[.5,0,0])<1e-11
            assert np.linalg.norm(solution.y[3:,-1]-initial[3:])<1e-10
            sample=solution.sol(np.linspace(0,1,40001))
            axis_y=-radius*math.sin(delta);axis_z=radius*math.cos(delta)
            distances=np.sqrt((sample[1]-axis_y)**2+(sample[2]-axis_z)**2)
            assert np.max(abs(distances-radius))<1e-11
            discrete=np.linalg.norm(np.diff(sample[:3],axis=1),axis=0).sum()
            assert abs(discrete-1)<5e-8
            force=np.cross(sample[3:].T,[1,0,0])/tension
            # t' + t×B/T=0；取B×t的ODE方向，勿反转右手螺旋。
            derivatives=np.column_stack([np.zeros(sample.shape[1]),-sample[5]/tension,sample[4]/tension])
            assert np.max(abs(force+derivatives))<1e-12
            helices.append(dict(n=n,phase=delta,tension=tension,radius=radius,pitch=.5/n,
                                endpoint_error=float(np.linalg.norm(solution.y[:3,-1]-[.5,0,0])),
                                discrete_length=discrete,axis_offset=[axis_y,axis_z]))
    # 完整带解变式：一般端点间距及近直线展开，不假设仅一种磁场方向。
    variants=[]
    for eta in [.5,.75,.99]:
        q=brentq(lambda z:math.sin(z)/z-eta,1e-7,math.pi,xtol=1e-14)
        variants.append(dict(chord_ratio=eta,planar_half_angle=q,planar_radius=1/(2*q),
                             helix_radius_n1=math.sqrt(1-eta*eta)/(2*math.pi),
                             helix_tension_n1=1/(2*math.pi),helix_pitch_n1=eta))
    sources=['scripts/verify_question_02.py']
    complete=False
    draft=ROOT/'drafts/question-02.md'
    if draft.exists():
        sources.append('drafts/question-02.md')
        complete='<!-- question-complete -->' in draft.read_text()
    fig=ROOT/'figures/题02_图稿源文件.tex'
    if fig.exists():sources.append('figures/题02_图稿源文件.tex')
    record=dict(question=2,verified_math=True,document_complete=complete,units='l=I=B0=1',
        planar=dict(beta=beta,central_angle=2*beta,complement_angle=angle,
                    complement_angle_degrees=math.degrees(angle),radius=R,tension=T,
                    endpoint_error=float(np.linalg.norm(sol.y[:3,-1]-[.5,0,0])),
                    discrete_length=length,center=center.tolist(),anchor_forces=anchor_forces.tolist()),
        helices=helices,variants=variants,source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources})
    (ROOT/'build').mkdir(exist_ok=True)
    path=ROOT/'build'/('verification-q02.json' if complete else 'verification-q02-preliminary.json')
    path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(record,ensure_ascii=False,indent=2))
if __name__=='__main__':main()

