"""第1题：解析根与逐段反射射线追踪独立交叉核验。"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]
BETA=.2

def scalar_root(k, sigma, m=1):
    f=lambda t: t-2*k*math.sin((2*math.pi*m+sigma*BETA*t)/(2*k))
    if sigma==-1:
        lo=max(0., (2*math.pi*m-k*math.pi)/BETA)
        hi=min(2*k, 2*math.pi*m/BETA)
    else:
        lo=0.
        hi=min(2*k, (k*math.pi-2*math.pi*m)/BETA)
    assert hi>lo and f(lo)<0 and f(hi)>0, (k,sigma,m,lo,hi)
    return brentq(f,lo,hi,xtol=1e-13)

def trace(delta, sigma, k):
    # 单位半径。首段给出后，后续方向只按法向反射更新，
    # 不使用等圆心角公式生成后续端点。
    start=np.array([1.,0.])
    first=np.array([math.cos(sigma*delta),math.sin(sigma*delta)])
    direction=first-start
    direction=direction/np.linalg.norm(direction)
    current=start.copy()
    points=[current.copy()]
    lengths=[]
    vectors=[]
    for j in range(k):
        distance=-2*float(np.dot(current,direction))
        assert distance>0
        endpoint=current+distance*direction
        assert abs(np.dot(endpoint,endpoint)-1)<1e-12
        lengths.append(distance)
        vectors.append(direction.copy())
        points.append(endpoint.copy())
        normal=endpoint/np.linalg.norm(endpoint)
        direction=direction-2*np.dot(direction,normal)*normal
        current=endpoint
    total=sum(lengths)
    return total,points,vectors

def main():
    results=[]
    for sigma, ks in [(-1,range(2,9)),(1,range(3,9))]:
        previous=0.
        for k in ks:
            tau=scalar_root(k,sigma)
            delta=(2*math.pi+sigma*BETA*tau)/k
            assert 0<delta<=math.pi and tau>previous
            previous=tau
            total,points,vectors=trace(delta,sigma,k)
            runner=np.array([math.cos(BETA*total),math.sin(BETA*total)])
            position_error=float(np.linalg.norm(points[-1]-runner))
            assert abs(total-tau)<1e-10 and position_error<1e-10
            tangent=lambda p:np.array([-p[1],p[0]])
            emitter_projection=BETA*np.dot(tangent(points[0]),vectors[0])
            receiver_projection=BETA*np.dot(tangent(points[-1]),vectors[-1])
            ratio=(1-receiver_projection)/(1-emitter_projection)
            assert abs(ratio-1)<1e-12
            # 用射线追踪闭合误差独立求发射角，对照解析根。
            def shoot(d):
                length, ps, _=trace(d,sigma,k)
                expected=np.array([math.cos(BETA*length),math.sin(BETA*length)])
                cross=expected[0]*ps[-1][1]-expected[1]*ps[-1][0]
                return cross
            shot_delta=brentq(shoot,delta-.001,delta+.001,xtol=1e-13)
            shot_time,_,_=trace(shot_delta,sigma,k)
            assert abs(shot_time-tau)<1e-10
            results.append(dict(k=k,sigma=sigma,tau=tau,delta=delta,raytrace_tau=shot_time,endpoint_error=position_error,frequency_ratio=float(ratio)))
    ordered=sorted(results,key=lambda x:x['tau'])
    assert [(x['sigma'],x['k']) for x in ordered[:3]]==[(-1,2),(-1,3),(-1,4)]
    assert 8/(1+2*BETA/math.pi)>ordered[2]['tau']
    stationary=[2*k*math.sin(math.pi/k) for k in (2,3,4)]
    assert np.allclose(stationary,[4,3*math.sqrt(3),4*math.sqrt(2)])
    sources={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['drafts/question-01.md','figures/题01_图稿源文件.tex']}
    report=dict(question=1,pass_all=True,beta=BETA,first_three=ordered[:3],candidate_paths=results,m_ge_2_time_lower_bound=8/(1+2*BETA/math.pi),stationary=stationary,source_sha256=sources)
    dest=ROOT/'build'/'verification-q01.json'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':
    main()
