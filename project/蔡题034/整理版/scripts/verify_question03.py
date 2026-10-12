"""第034套第3题：从游泳者控制的航向出发直接最小化行程用时。"""
from pathlib import Path
import json
import math
ROOT=Path(__file__).resolve().parents[1]

def golden(f, lo, hi):
    ratio=(math.sqrt(5)-1)/2
    a=hi-ratio*(hi-lo); b=lo+ratio*(hi-lo)
    fa,fb=f(a),f(b)
    for _ in range(140):
        if fa<fb:
            hi,b,fb=b,a,fa
            a=hi-ratio*(hi-lo);fa=f(a)
        else:
            lo,a,fa=a,b,fb
            b=lo+ratio*(hi-lo);fb=f(b)
    x=(lo+hi)/2
    return x,f(x)

def run():
    report=[]
    # l=v=1，只用航向、匀速位移与跑步距离计算时间；未调用正文的 τ(x)。
    d=math.sqrt(3)/2;v=1.
    for u in [0., 1/3]:
        for h in [0.1,1.,2.,3.,4.,7*d/3,16*d/3,5.,8.,30.]:
            def route(theta):
                vy=v*math.cos(theta)
                vx=v*math.sin(theta)+u
                t=d/vy
                x=vx*t
                return 2*t+abs(h-2*x)/(2*v)
            theta,shore=golden(route,-math.pi/2+1e-6,math.pi/2-1e-6)
            direct=h/(v+u)
            actual=min(direct,shore)
            if u==0:
                expected=direct if h<=3 else (h+3)/2
            else:
                expected=direct if h<=16*d/3 else h/2+4*d/3
            assert abs(actual-expected)<1e-9,(u,h,actual,expected)
            report.append(dict(u_over_v=u,h_over_l=h,shore_time=shore,
                               direct_time=direct,minimum=actual,heading_rad=theta))
    # 航向不固定为本题的数值：检验教师变式的三组参数。
    for u,V,h in [(0.2,1.8,12),(0.6,2.7,9),(0.0,3.0,8)]:
        def variant(theta):
            t=d/(v*math.cos(theta))
            x=(u+v*math.sin(theta))*t
            return 2*t+abs(h-2*x)/V
        theta,shore=golden(variant,-math.pi/2+1e-6,math.pi/2-1e-6)
        D=math.sqrt((V-u)**2-v*v)
        threshold=2*d*(v+u)*D/(v*(V-v-u))
        expected=h/(v+u) if h<=threshold else h/V+2*d*D/(V*v)
        assert abs(min(h/(v+u),shore)-expected)<1e-9
        report.append(dict(variant=True,u=u,V=V,h=h,minimum=expected,heading_rad=theta))
    data=dict(status="passed",checks=len(report),method="相对水航向的一维数值极小化，显式计入向前或向后跑步",rows=report)
    (ROOT/"build/question03-verification.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    print("PASS",len(report),"cases")
if __name__=="__main__":run()

