"""第034套第4题独立求场：内部离散线电荷的边界配点法。
不使用解析 sigma(theta)，先强制整圆电势为零，再计算外侧场与 Maxwell 压力。
无量纲 R=epsilon0=E0=L=1；检验逐级加密收敛。
"""
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def solve(a,b):
    a=[row[:]+[val] for row,val in zip(a,b)]
    n=len(b)
    for j in range(n):
        p=max(range(j,n),key=lambda i:abs(a[i][j]))
        a[j],a[p]=a[p],a[j]
        assert abs(a[j][j])>1e-14
        z=a[j][j]
        a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i==j:continue
            c=a[i][j]
            a[i]=[x-c*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]

def check(n):
    src=[(.55*math.cos(2*math.pi*j/n),.55*math.sin(2*math.pi*j/n)) for j in range(n)]
    pts=[(math.cos(2*math.pi*(j+.23)/n),math.sin(2*math.pi*(j+.23)/n)) for j in range(n)]
    # 未知线电荷 + 常数电势；附加总线电荷=0，符合横向匀强场的中性整圆柱。
    matrix=[[-math.log(math.dist(p,s))/(2*math.pi) for s in src]+[1.] for p in pts]
    matrix.append([1.]*n+[0.])
    charges=solve(matrix,[p[1] for p in pts]+[0.])
    def field(p):
        ex,ey=0.,1.
        for q,s in zip(charges[:-1],src):
            dx,dy=p[0]-s[0],p[1]-s[1]
            rr=dx*dx+dy*dy
            ex+=q*dx/(2*math.pi*rr)
            ey+=q*dy/(2*math.pi*rr)
        return ex,ey
    count=1600
    step=math.pi/count
    integral=0.
    residual=0.
    for j in range(count+1):
        a=j*step
        p=(math.cos(a),math.sin(a))
        ex,ey=field(p)
        normal=ex*p[0]+ey*p[1]
        tangent=-ex*p[1]+ey*p[0]
        residual=max(residual,abs(tangent))
        integrand=.5*normal*normal*p[1]
        weight=1 if j in (0,count) else (4 if j%2 else 2)
        integral+=weight*integrand
    integral*=step/3
    return dict(sources=n,force_per_length=integral,
                error=abs(integral-8/3),maximum_tangential_residual=residual)
def main():
    rows=[check(n) for n in (16,24,32)]
    assert rows[-1]["error"]<1e-5
    assert rows[-1]["maximum_tangential_residual"]<1e-5
    assert rows[-1]["error"]<rows[0]["error"]
    data=dict(status="passed",method="边界配点线电荷求场 + 表面压力数值积分",rows=rows)
    (ROOT/"build/question04-verification.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=="__main__":main()

