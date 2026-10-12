"""从等棱长三维坐标生成网络，以有理数结点方程独立核验三问。"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import math
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def geometry():
    points = [np.array([0., 0., 1.])]
    for z, start in ((1/math.sqrt(5), 234), (-1/math.sqrt(5), 270)):
        for i in range(5):
            angle = math.radians(start + 72*i)
            points.append(np.array([2/math.sqrt(5)*math.cos(angle),
                                    2/math.sqrt(5)*math.sin(angle), z]))
    points.append(np.array([0., 0., -1.]))
    distances = {(i,j): float(np.linalg.norm(points[i]-points[j]))
                 for i,j in combinations(range(12),2)}
    edge_length = min(distances.values())
    edges = [e for e,d in distances.items() if abs(d-edge_length)<1e-10]
    faces = [face for face in combinations(range(12),3)
             if all(tuple(sorted(e)) in edges for e in combinations(face,2))]
    assert len(edges)==30 and len(faces)==20
    assert all(sum(v in e for e in edges)==5 for v in range(12))
    return points,edges,faces


def eliminate(matrix, rhs):
    a = [row[:] + [b] for row,b in zip(matrix,rhs)]
    for col in range(len(a)):
        pivot = next(row for row in range(col,len(a)) if a[row][col])
        a[col],a[pivot] = a[pivot],a[col]
        factor=a[col][col]
        a[col]=[v/factor for v in a[col]]
        for row in range(len(a)):
            if row != col:
                factor=a[row][col]
                a[row]=[x-factor*y for x,y in zip(a[row],a[col])]
    return [row[-1] for row in a]


def solve(edges, a=0, c=6, ab_resistance=F(1)):
    idx=[i for i in range(12) if i!=c]
    g=[[F(0) for _ in range(12)] for _ in range(12)]
    conductances={}
    for i,j in edges:
        conductance=1/ab_resistance if (i,j)==(0,1) else F(1)
        conductances[(i,j)]=conductance
        g[i][i]+=conductance;g[j][j]+=conductance
        g[i][j]-=conductance;g[j][i]-=conductance
    rhs=[F(i==a) for i in idx]
    sol=eliminate([[g[i][j] for j in idx] for i in idx],rhs)
    v=[F(0) for _ in range(12)]
    for i,x in zip(idx,sol):v[i]=x
    for i in range(12):
        assert sum(g[i][j]*v[j] for j in range(12))==F(1 if i==a else -1 if i==c else 0)
    dissipated=sum(gij*(v[i]-v[j])**2 for (i,j),gij in conductances.items())
    assert dissipated==v[a]-v[c]
    return v[a]-v[c],v


def main():
    points,edges,faces=geometry()
    deleted=[set(),{(0,1),(1,6),(1,2)},{(0,1)}]
    expected=[F(7,15),F(14,23),F(21,38)]
    results=[]
    for removed,target in zip(deleted,expected):
        value,v=solve([e for e in edges if e not in removed])
        assert value==target,(value,target)
        results.append(dict(removed=sorted(removed),resistance=str(value),
                            potentials=[str(x) for x in v],kcl="exact_pass",power="exact_pass"))
    adjacent,_=solve(edges,a=0,c=1)
    assert adjacent==F(11,30)
    r,v=solve(edges)
    assert v[1]==v[2]==r/2
    no_ab_bc=[e for e in edges if e not in {(0,1),(1,6)}]
    r2,v2=solve(no_ab_bc)
    assert r2==F(14,23) and v2[1]==v2[2]
    for n in range(1,101):
        lam=F(n,7)
        direct,_=solve(edges,ab_resistance=lam)
        derived=7*(3*lam+1)/(2*(19*lam+11))
        assert direct==derived
    report=dict(status="pass",vertices=12,edges=30,faces=20,
                independent_geometry="equal_edge_3d_coordinates",
                adjacent_resistance=str(adjacent),cases=results,parameter_cases=100)
    (ROOT/"build/question07-verification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=="__main__":main()
