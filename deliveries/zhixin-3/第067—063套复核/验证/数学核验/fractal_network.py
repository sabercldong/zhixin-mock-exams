"""Independent finite resistor graph: overlapping wire is counted only once."""
import numpy as np
from collections import defaultdict
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def graph(depth):
 N=3**depth;h=defaultdict(list);v=defaultdict(list)
 def square(x,y,l,d):
  for yy in [y,y+l]:h[yy].append((x,x+l))
  for xx in [x,x+l]:v[xx].append((y,y+l))
  if d:
   for dx,dy in [(0,0),(2*l//3,0),(0,2*l//3),(2*l//3,2*l//3)]:square(x+dx,y+dy,l//3,d-1)
 square(0,0,N,depth)
 def covered(z,intervals):return any(a<=z<=b for a,b in intervals)
 edges=[]
 for y,intervals in h.items():
  xs=sorted(set([x for a,b in intervals for x in [a,b]]+[x for x,iv in v.items() if covered(x,intervals) and covered(y,iv)]))
  for a,b in zip(xs,xs[1:]):
   if covered((a+b)/2,intervals):edges.append(((a,y),(b,y),(b-a)/N))
 for x,intervals in v.items():
  ys=sorted(set([y for a,b in intervals for y in [a,b]]+[y for y,iv in h.items() if covered(y,intervals) and covered(x,iv)]))
  for a,b in zip(ys,ys[1:]):
   if covered((a+b)/2,intervals):edges.append(((x,a),(x,b),(b-a)/N))
 points=sorted({p for a,b,r in edges for p in [a,b]});index={p:i for i,p in enumerate(points)}
 a=np.array([index[e[0]] for e in edges]);b=np.array([index[e[1]] for e in edges]);R=np.array([e[2] for e in edges]);x=np.array(points)/N
 G=1/R;K=coo_matrix((np.r_[G,G,-G,-G],(np.r_[a,b,a,b],np.r_[a,b,b,a])),shape=(len(points),)*2).tocsr()
 def solve(rhs):
  out=np.zeros(len(points));out[1:]=spsolve(K[1:,1:],rhs[1:]);return out
 def resistance(t,s):
  rhs=np.zeros(len(points));rhs[index[t]]=1;rhs[index[s]]=-1;V=solve(rhs);return V[index[t]]-V[index[s]]
 # E=(k/2)(-y,x), k=r=l=1. Exact segment line integral.
 emf=(x[a,0]*x[b,1]-x[a,1]*x[b,0])/2
 rhs=np.bincount(a,weights=-emf*G,minlength=len(points))+np.bincount(b,weights=emf*G,minlength=len(points))
 V=solve(rhs);I=(V[a]-V[b]+emf)*G
 Ic=[I[j] for j,(aa,bb,_) in enumerate(edges) if aa[1]==bb[1]==0 and aa[0]==N//3 and bb[0]==2*N//3]
 if depth==0:Ic=[I[j] for j,(aa,bb,_) in enumerate(edges) if aa[1]==bb[1]==0]
 return dict(depth=depth,nodes=len(points),edges=len(edges),Rdiag=resistance((0,0),(N,N)),Radj=resistance((0,0),(N,0)),Ic=Ic[0],P=float(np.sum(R*I*I)),kcl=float(np.max(np.abs(np.bincount(a,weights=I,minlength=len(points))-np.bincount(b,weights=I,minlength=len(points))))))
if __name__=='__main__':
 for d in range(6):print(graph(d))
