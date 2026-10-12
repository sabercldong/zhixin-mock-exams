from pathlib import Path
import math,json
import numpy as np
from scipy.optimize import minimize_scalar
ROOT=Path(__file__).resolve().parents[1]
n=1.58;R=.1;lam=550e-9;f=R/(n-1)
def geometric_angle(r):
 theta=math.asin(r/R);gamma=math.asin(n*math.sin(theta))-theta
 return (f+R*(1-math.cos(theta)))*math.tan(gamma)-r
# Independent vector Snell law: incident u=(1,0), outward normal is (cos(theta),sin(theta)).
def ray_trace(r):
 normal=np.array([math.sqrt(1-(r/R)**2),r/R]);u=np.array([1.,0.])
 tangent=u-np.dot(u,normal)*normal
 transmitted=n*tangent+math.sqrt(1-n*n*np.dot(tangent,tangent))*normal
 point=np.array([R*normal[0],r]);distance=(R+f-point[0])/transmitted[0]
 y=(point+distance*transmitted)[1]
 return abs(float(y))
for r in np.geomspace(.00005,.05,50):assert abs(geometric_angle(r)-ray_trace(r))<1e-13
D=.61*lam*f
approx_r=(2*D*R*R/(3*n*n))**.25
approx_geom=n*n*approx_r**3/(2*R*R)
opt=minimize_scalar(lambda r:ray_trace(r)+D/r,bounds=(.0001,.015),method='bounded',options={'xatol':1e-14})
assert opt.success
# Independent finite-grid comparison and cubic small-aperture convergence.
for h in [.001,.0005,.00025]:
 assert abs(ray_trace(h)/(n*n*h**3/(2*R*R))-1)<.003
assert abs(opt.x-approx_r)/approx_r<.004
report=dict(passed=True,method='vector Snell ray trace + angle geometry + small-aperture convergence + exact scalar minimization',focal_length_m=f,full_aperture_radius_m=.05,geometric_spot_radius_m=ray_trace(.05),approx_optimal_lens_radius_m=approx_r,approx_minimum_spot_radius_m=4*approx_geom,exact_optimal_lens_radius_m=float(opt.x),exact_minimum_spot_radius_m=float(opt.fun),total_internal_reflection_threshold_radius_m=R/n)
(ROOT/'preview/verify-question-03.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
