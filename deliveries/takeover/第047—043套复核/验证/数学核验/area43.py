import numpy as np,itertools
from scipy.spatial import ConvexHull

def region(N,p):
 h=2*np.pi/N
 # active p consecutive legs centered on x-axis
 theta=(np.arange(N)-(p-1)/2)*h
 cs=np.cos(theta);sn=np.sin(theta);C=sum(cs[:p]);S=sum(sn[:p]);
 rows=np.column_stack((cs-C/p,sn-S/p)); vals=np.ones(N)/p
 # active f>=0, inactive f<=0; convert A v <= b
 signs=np.r_[-np.ones(p),np.ones(N-p)];A=rows*signs[:,None];b=-vals*signs
 pts=[]
 for i,j in itertools.combinations(range(N),2):
  mat=A[[i,j]]
  if abs(np.linalg.det(mat))<1e-11:continue
  v=np.linalg.solve(mat,b[[i,j]])
  if np.all(A@v<=b+1e-9):pts.append(v)
 pts=np.unique(np.round(pts,11),axis=0)
 hull=ConvexHull(pts);pts=pts[hull.vertices]
 # normalized load coordinates x=sumf_i cos_i, y=sumf_i sin_i
 pos=[]
 for v in pts:
  ff=vals[:p]+rows[:p]@v;pos.append([sum(ff*cs[:p]),sum(ff*sn[:p])])
 pos=np.array(pos);area=ConvexHull(pos).volume
 return theta,pts,pos,area
if __name__ == "__main__":
 for N,p in [(4,3),(5,3),(21,6),(7,4),(8,5),(10,8)]:
  th,b,pos,A=region(N,p);print(N,p,'verts',len(b),'fixedarea',A,'totalarea',N*A,'positions',pos.tolist())
