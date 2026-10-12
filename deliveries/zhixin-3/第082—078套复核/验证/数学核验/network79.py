import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from math import sqrt

def graph(depth):
 E=[]
 def edge(a,b):E.append((tuple(np.round(a,12)),tuple(np.round(b,12))))
 def tri(v,d):
  if d==0:
   for i in range(3):edge(v[i],v[(i+1)%3])
  else:
   child=[]
   for i in range(3):child.append([v[i],v[i]+(v[(i+1)%3]-v[i])/3,v[i]+(v[(i+2)%3]-v[i])/3])
   for i in range(3):
    tri(child[i],d-1);edge(child[i][1],child[(i+1)%3][2])
 tri(np.array([[.5,sqrt(3)/2],[0,0],[1,0]]),depth)
 nodes=sorted(set(a for a,b in E)|set(b for a,b in E));idx={a:i for i,a in enumerate(nodes)}
 return nodes,[(idx[a],idx[b]) for a,b in E]
def solve(depth):
 nodes,edges=graph(depth);N=len(nodes);lap=lil_matrix((N,N));b=np.zeros(N);rs=[];es=[]
 for i,j in edges:
  x,y=nodes[i];X,Y=nodes[j];r=np.hypot(x-X,y-Y);e=-.5*(x*Y-y*X);rs.append(r);es.append(e)
  lap[i,i]+=1/r;lap[j,j]+=1/r;lap[i,j]-=1/r;lap[j,i]-=1/r;b[i]-=e/r;b[j]+=e/r
 u=np.zeros(N);u[1:]=spsolve(lap.tocsr()[1:,1:],b[1:]);curr=np.array([(u[i]-u[j]+e)/r for (i,j),r,e in zip(edges,rs,es)])
 p=sum(curr*curr*np.array(rs));In=np.zeros(N);ia=min(range(N),key=lambda i:np.linalg.norm(np.array(nodes[i])-[.5,sqrt(3)/2]));ib=nodes.index((0.,0.));In[ia]=1;In[ib]=-1
 v=np.zeros(N);v[1:]=spsolve(lap.tocsr()[1:,1:],In[1:]);Req=v[ia]-v[ib]
 topcurr=[abs(c) for c,r in zip(curr,rs) if abs(r-1/3)<1e-8];return dict(depth=depth,nodes=N,R=Req,P_over_e0sq=p/(3/16),It_over_e0=topcurr[:3]/np.array([sqrt(3)/4]*min(3,len(topcurr))) if topcurr else [])
if __name__=='__main__':
 for d in range(6):print(solve(d))
