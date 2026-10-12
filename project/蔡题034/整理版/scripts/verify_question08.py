"""第034套第8题：变换实际光线事件、同时波面切向事件与一般相位事件。"""
from pathlib import Path
import json
import math
import random
ROOT=Path(__file__).resolve().parents[1]
def boost(event,beta):
    t,x,y,z=event
    gamma=1/math.sqrt(1-beta*beta)
    return gamma*(t-beta*x),gamma*(x-beta*t),y,z
def main():
    rng=random.Random(3408)
    worst=dict(speed=0.,normal=0.,phase=0.,simultaneity=0.)
    count=0
    for beta in [0,.1,.6,.9,.99]:
        angles=[0,math.pi/2,math.pi,math.acos(beta)]+[rng.uniform(-math.pi,math.pi) for _ in range(100)]
        gamma=1/math.sqrt(1-beta*beta)
        for theta in angles:
            nx,ny=math.cos(theta),math.sin(theta)
            # 两个光线事件，c=1；直接变换事件间隔得到新速度。
            event=boost((1.,nx,ny,0.),beta)
            velocity=(event[1]/event[0],event[2]/event[0],0.)
            speed=math.hypot(*velocity[:2])
            # 构造旧系中同相位、变换后同时的切向事件差。
            # n·dr=dt 且 dt'=0；不调用新波矢来挑选切向量。
            tangent=boost((beta*ny,ny,beta-nx,0.),beta)
            dot=velocity[0]*tangent[1]+velocity[1]*tangent[2]
            worst["speed"]=max(worst["speed"],abs(speed-1))
            worst["normal"]=max(worst["normal"],abs(dot))
            worst["simultaneity"]=max(worst["simultaneity"],abs(tangent[0]))
            # 一般事件的相位检验，含不在光线上及不在 phi=phi0 波面上的点。
            omega=2.3
            t,x,y,z=[rng.uniform(-3,3) for _ in range(4)]
            tp,xp,yp,zp=boost((t,x,y,z),beta)
            old=omega*(t-nx*x-ny*y)
            wp=gamma*omega*(1-beta*nx)
            kxp=gamma*omega*(nx-beta)
            kyp=omega*ny
            new=wp*tp-kxp*xp-kyp*yp
            worst["phase"]=max(worst["phase"],abs(new-old))
            count+=1
    assert max(worst.values())<1e-10,worst
    data=dict(status="passed",cases=count,c_normalization=1,
              method="事件洛伦兹变换：光线速度、同时波面切向量、一般相位",
              worst_absolute_residuals=worst)
    (ROOT/"build/question08-verification.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=="__main__":main()

