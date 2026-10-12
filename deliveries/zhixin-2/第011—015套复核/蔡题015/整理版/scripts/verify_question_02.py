"""Independent q02 pre-verification. This does not mark a manuscript or set complete."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as sp
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

ROOT=Path(__file__).resolve().parents[1]
symbolic=[];numerical=[]
def exact(label,value):
 if isinstance(value,sp.MatrixBase):
  for entry in value:exact(label+" component",entry)
  return
 value=sp.trigsimp(sp.simplify(value))
 if value!=0:value=sp.simplify(value.rewrite(sp.exp))
 assert value==0,(label,value)
 symbolic.append({"check":label,"residual":str(value)})
def numeric(label,actual,expected,atol=3e-8):
 actual=np.asarray(actual,dtype=float);expected=np.asarray(expected,dtype=float)
 error=float(np.max(np.abs(actual-expected)))
 assert error<atol,(label,actual,expected,error,atol)
 numerical.append({"check":label,"max_absolute_error":error,"actual":actual.tolist(),"expected":expected.tolist()})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def network():
 golden=(1+np.sqrt(5))/2
 vertices=np.array([(0,u,v*golden) for u in [-1,1] for v in [-1,1]]+
                   [(u,v*golden,0) for u in [-1,1] for v in [-1,1]]+
                   [(u*golden,0,v) for u in [-1,1] for v in [-1,1]])
 edges=[(i,j) for i in range(12) for j in range(i+1,12) if abs(np.linalg.norm(vertices[i]-vertices[j])-2)<1e-12]
 assert len(edges)==30
 lap=np.zeros((12,12))
 for i,j in edges:lap[i,i]+=1;lap[j,j]+=1;lap[i,j]-=1;lap[j,i]-=1
 assert np.all(np.diag(lap)==5)
 pinv=np.linalg.pinv(lap)
 nodepairs=[];fieldmax=0;resmax=0
 t,w=leggauss(32);t=(t+1)/2;w=w/2
 for a in range(12):
  for b in range(a+1,12):
   source=np.zeros(12);source[a]=1;source[b]=-1
   potential=pinv@source
   numeric(f"Kirchhoff pair {a}-{b}",lap@potential,source,2e-14)
   field=np.zeros(3)
   for i,j in edges:
    current=potential[i]-potential[j]
    wire=vertices[i]+t[:,None]*(vertices[j]-vertices[i])
    element=vertices[j]-vertices[i]
    field+=current*np.sum(w[:,None]*np.cross(element,-wire)/np.linalg.norm(wire,axis=1)[:,None]**3,axis=0)
   fieldmax=max(fieldmax,float(np.linalg.norm(field)))
   numeric(f"actual 30-wire Biot-Savart center pair {a}-{b}",field,np.zeros(3),2e-14)
   nodepairs.append({"source":a,"sink":b,"normalized_field":field.tolist()})
 for i,j in edges:
  delta=np.eye(12)[i]-np.eye(12)[j]
  resistance=float(delta@pinv@delta)
  resmax=max(resmax,abs(resistance-11/30))
 numeric("all thirty adjacent effective resistances",resmax,0,2e-14)
 for i in range(12):
  near=[j for j in range(12) if (min(i,j),max(i,j)) in edges]
  numeric(f"five-neighbor vector sum at vertex {i}",np.sum(vertices[near],axis=0),np.sqrt(5)*vertices[i],3e-14)
 a,b=edges[0]
 matrix=sp.Matrix(lap.astype(int).tolist())
 q=sp.zeros(12,1);q[a]=1;q[b]=-1
 ids=[i for i in range(12) if i!=b]
 solution=matrix.extract(ids,ids).inv()*q.extract(ids,[0])
 potentials={str(i):str(solution[ids.index(i)]) if i!=b else "0" for i in range(12)}
 exact("exact adjacent effective resistance",solution[ids.index(a)]-sp.Rational(11,30))
 return {"vertices":vertices.tolist(),"edges":edges,"adjacent_source":a,"adjacent_sink":b,
         "exact_grounded_potentials_per_IR":potentials,"all_pairs_max_field_error":fieldmax,
         "adjacent_resistance_max_error":resmax,"lead_field_scope":"30-edge network only; radial external leads add zero at O, unspecified nonradial leads are not included"}

def plane():
 nodes,weights=leggauss(360)
 t=(nodes+1)/2;weights=weights/2
 radii=t/(1-t);dr=1/(1-t)**2
 phi=2*np.pi*(np.arange(512)+.5)/512
 for rho,z in [(1,.6),(1,1.3),(1,2.6),(1,-.6),(1,-1.3),(1,-2.6),(.7,.7),(.7,-.7)]:
  dist=(rho*rho+radii[:,None]**2-2*rho*radii[:,None]*np.cos(phi)+z*z)**1.5
  sheet=np.sum(weights*dr*np.mean(-z*np.cos(phi)[None,:]/dist,axis=1))
  wire=quad(lambda s:-rho/(rho*rho+(z-s)**2)**1.5,0,np.inf,epsabs=1e-11,epsrel=1e-11)[0]
  numeric(f"plane actual sheet+semiwire rho={rho},z={z}",sheet+wire,(-2/rho if z>0 else 0),4e-10)
  numeric(f"plane sheet alone rho={rho},z={z}",sheet,-(np.sign(z)-z/np.hypot(rho,z))/rho,4e-10)
 return {"integration":"Direct radial surface-current Biot-Savart quadrature and independent semi-infinite straight-wire integral; normalized by mu0*I/(4*pi)","points":8}

def axes(a):
 a=np.asarray(a,dtype=float);a=a/np.linalg.norm(a)
 seed=np.array([0.,0.,1.]) if abs(a[2])<.8 else np.array([1.,0.,0.])
 u=np.cross(seed,a);u/=np.linalg.norm(u);v=np.cross(a,u)
 return u,v,a
def sheet_source(point,a,order):
 u,v,a=axes(a)
 t,w=leggauss(order);gamma=(t+1)*np.pi/2;w=w*np.pi/2
 phi=2*np.pi*(np.arange(2*order)+.5)/(2*order)
 radial=np.sin(gamma)[:,None,None]*(np.cos(phi)[None,:,None]*u+np.sin(phi)[None,:,None]*v)+np.cos(gamma)[:,None,None]*a
 tangent=np.cos(gamma)[:,None,None]*(np.cos(phi)[None,:,None]*u+np.sin(phi)[None,:,None]*v)-np.sin(gamma)[:,None,None]*a
 offset=point-radial
 density=np.cross(tangent,offset)/np.linalg.norm(offset,axis=2)[:,:,None]**3
 weighted=density*(1+np.cos(gamma))[:,None,None]*w[:,None,None]/(4*np.pi)
 return np.sum(weighted,axis=(0,1))*(2*np.pi/(2*order))
def wire_source(point,a):
 _,_,a=axes(a);cross=np.cross(-a,point)
 integral=quad(lambda s:1/np.linalg.norm(point-s*a)**3,1,np.inf,epsabs=5e-12,epsrel=5e-12)[0]
 return cross*integral
def k_surface(n,a,b):
 ca=n@a;cb=n@b
 return ((ca*n-a)/(1-ca)-(cb*n-b)/(1-cb))/(4*np.pi)
def sphere():
 a=np.array([0.,0.,1.]);checks=[]
 cases=[]
 for theta0 in [.45,1.1,2.3]:
  b=np.array([-np.sin(theta0),0.,np.cos(theta0)])
  for radius,theta,phi in [(.35,.8,.4),(.7,1.5,1.0),(.65,2.1,2.2),(1.55,.9,.5),(1.8,1.8,1.4),(2.7,2.0,2.8)]:
   n=np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])
   point=radius*n
   low=sheet_source(point,a,64)-sheet_source(point,b,64)+wire_source(point,a)-wire_source(point,b)
   high=sheet_source(point,a,128)-sheet_source(point,b,128)+wire_source(point,a)-wire_source(point,b)
   expected=np.zeros(3) if radius<1 else (np.cross(b,n)/(1-b@n)-np.cross(a,n)/(1-a@n))/radius
   numeric(f"all-source sphere theta0={theta0},R={radius},theta={theta},phi={phi}",high,expected,4e-9)
   numeric(f"sphere quadrature convergence theta0={theta0},R={radius}",low,high,4e-8)
   numeric(f"sphere B radial component theta0={theta0},R={radius}",high@n,0,4e-9)
   cases.append({"theta0":theta0,"R":radius,"theta":theta,"phi":phi,"field":high.tolist(),"expected":expected.tolist()})
  for theta,phi in [(.6,.0),(1.4,.7),(2.2,1.3)]:
   n=np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])
   et=np.array([np.cos(theta)*np.cos(phi),np.cos(theta)*np.sin(phi),-np.sin(theta)])
   ep=np.array([-np.sin(phi),np.cos(phi),0.])
   def voltage(unit):
    return np.log(np.sqrt((1-unit@b)/(1-unit@a)))/(2*np.pi)
   numerical_k=[]
   for direction in [et,ep]:
    eps=2e-6
    np1=n*np.cos(eps)+direction*np.sin(eps);nm1=n*np.cos(eps)-direction*np.sin(eps)
    numerical_k.append(-(voltage(np1)-voltage(nm1))/(2*eps))
   numeric(f"independent potential gradient theta0={theta0},theta={theta},phi={phi}",numerical_k,[k_surface(n,a,b)@et,k_surface(n,a,b)@ep],3e-10)
  for sign,center in [(1,a),(-1,b)]:
   for angle in [.08,.18]:
    u,v,c=axes(center);phi=2*np.pi*(np.arange(1000)+.5)/1000
    n=np.sin(angle)*(np.cos(phi)[:,None]*u+np.sin(phi)[:,None]*v)+np.cos(angle)*c
    out=np.cos(angle)*(np.cos(phi)[:,None]*u+np.sin(phi)[:,None]*v)-np.sin(angle)*c
    flux=sum(k_surface(nn,a,b)@oo for nn,oo in zip(n,out))*2*np.pi*np.sin(angle)/len(phi)
    numeric(f"actual source/sink cap flux theta0={theta0},angle={angle},sign={sign}",flux,sign,4e-12)
 return {"integration":"Actual spherical-film current plus both semi-infinite radial leads; uniform auxiliary radial currents cancel by spherical symmetry. Direct Gauss/trapezoidal Biot-Savart quadrature at 64 and 128 orders.","cases":cases}

def symbolic_checks():
 from sympy.physics.units import ampere,meter,newton,tesla,volt,ohm,siemens,watt,convert_to
 exact("SI sheet current unit",convert_to(ampere/meter,[ampere,meter])/(ampere/meter)-1)
 exact("SI magnetic field unit",convert_to(newton/(ampere*meter),tesla)/tesla-1)
 exact("SI sheet conductance unit",convert_to(meter/(ohm*meter),siemens)/siemens-1)
 exact("SI sheet voltage unit",convert_to((ampere/meter)/siemens*meter,volt)/volt-1)
 exact("SI sheet dissipation unit",convert_to((ampere/meter)**2/siemens*meter**2,watt)/watt-1)
 g=(1+sp.sqrt(5))/2
 exact("golden-ratio squared",g*g-g-1)
 exact("exact neighboring chord squared",1+(1-g)**2+g*g-4)
 exact("exact neighboring polar cosine",g/(g+2)-1/sp.sqrt(5))
 theta,R=sp.symbols("theta R",positive=True)
 exact("auxiliary cap conservation",sp.cot(theta/2)*sp.sin(theta)-(1+sp.cos(theta)))
 exact("auxiliary sheet divergence",sp.diff(sp.sin(theta)*sp.cot(theta/2),theta)/sp.sin(theta)+1)
 exact("auxiliary surface log Laplacian",sp.diff(sp.sin(theta)*sp.diff(sp.log(sp.sin(theta/2)),theta),theta)/sp.sin(theta)+sp.Rational(1,2))
 bp=-sp.cot(theta/2)/R
 exact("auxiliary external radial curl",sp.diff(sp.sin(theta)*bp,theta)/(R*sp.sin(theta))-1/R**2)
 exact("auxiliary external polar curl",-sp.diff(R*bp,R)/R)
 ca,cb,d=sp.symbols("ca cb d",real=True)
 squared=(1+ca)/(1-ca)+(1+cb)/(1-cb)-2*(d-ca*cb)/((1-ca)*(1-cb))
 exact("full tangent-difference magnitude",squared-2*(1-d)/((1-ca)*(1-cb)))
 x,y,z=sp.symbols("x y z",real=True)
 exact("cross-product jump identity",sp.Matrix([0,0,1]).cross(sp.Matrix([x,y,0]).cross(sp.Matrix([0,0,1])))-sp.Matrix([x,y,0]))
 alpha=sp.symbols("alpha",positive=True)
 exact("opposite-cap integral primitive",sp.diff(sp.log(sp.tan(theta/2)),theta)-1/sp.sin(theta))
 exact("finite-cap endpoint tangent reciprocity",sp.tan((sp.pi-alpha)/2)*sp.tan(alpha/2)-1)
 return {"normalizations":"Network I=R_edge=1; fields divided by mu0*I/(4*pi). Sphere radius=1. Geometry and scaling are checked separately."}


def variants():
 mu=4*np.pi*1e-7
 nodes,weights=leggauss(360);t=(nodes+1)/2;weights=weights/2
 s=t/(1-t);ds=1/(1-t)**2
 phi=2*np.pi*(np.arange(512)+.5)/512
 for z in [.75,-.75]:
  wire=quad(lambda v:-1/(1+(z-v)**2)**1.5,0,np.inf,epsabs=1e-12)[0]
  kernel=(1+s[:,None]**2-2*s[:,None]*np.cos(phi)+z*z)**1.5
  sheet=np.sum(weights*ds*np.mean(-z*np.cos(phi)[None,:]/kernel,axis=1))
  scale=mu*2/(4*np.pi*.02)
  expected=[-1.6e-5,-.4e-5,-2e-5] if z>0 else [-.4e-5,.4e-5,0]
  numeric(f"variant1 actual semi-wire/sheet/total at signed height {z}",scale*np.array([wire,sheet,wire+sheet]),expected,3e-14)
 a=np.array([0.,0.,1.]);b=np.array([0.,0.,-1.])
 theta=np.pi/3;n=np.array([np.sin(theta),0.,np.cos(theta)])
 x=.5/.2*n
 actual=(sheet_source(x,a,128)-sheet_source(x,b,128)+wire_source(x,a)-wire_source(x,b))*mu*.8/(4*np.pi*.2)
 numeric("variant2 actual source integrals",actual,[0,-6.4e-7/np.sqrt(3),0],3e-15)
 numeric("variant2 surface current by independent potential derivative",
         k_surface(n,a,b)@np.array([np.cos(theta),0.,-np.sin(theta)])*.8/.2,4/(np.pi*np.sqrt(3)),3e-14)
 b=np.array([-1.,0.,0.]);n=np.array([-1.,0.,1.])/np.sqrt(2);x=3*n
 actual=(sheet_source(x,a,128)-sheet_source(x,b,128)+wire_source(x,a)-wire_source(x,b))*mu*2/(4*np.pi*.1)
 numeric("variant3 actual two leads and film",actual,[0,(4/3)*(1+np.sqrt(2))*1e-6,0],3e-14)
 numeric("variant3 actual current vector magnitude",np.linalg.norm(k_surface(n,a,b))*2/.1,10*(1+np.sqrt(2))/np.pi,3e-13)
 alpha=np.deg2rad(10);sigma=.05
 integrated=quad(lambda angle:1/(2*np.pi*sigma*np.sin(angle)),alpha,np.pi-alpha,epsabs=1e-12)[0]
 resistance=np.log(1/np.tan(alpha/2))/(np.pi*sigma)
 numeric("variant4 direct voltage integral per unit current",integrated,resistance,3e-13)
 chain=[]
 for count in [8000,16000]:
  step=(np.pi-2*alpha)/count
  angles=alpha+(np.arange(count)+.5)*step
  resistors=step/(2*np.pi*sigma*np.sin(angles))
  chain.append(float(np.sum(resistors)))
 numeric("variant4 independent band-resistor chain",chain[1],resistance,6e-7)
 assert abs(chain[1]-resistance)<abs(chain[0]-resistance)
 return {"variant2_K_A_per_m":4/(np.pi*np.sqrt(3)),
         "variant2_B_T":6.4e-7/np.sqrt(3),
         "variant3_K_A_per_m":10*(1+np.sqrt(2))/np.pi,
         "variant3_B_T":(4/3)*(1+np.sqrt(2))*1e-6,
         "variant4_R_ohm":resistance,"variant4_voltage_V":.12*resistance,
         "variant4_band_chain_ohm":chain}

def main():
 meta=symbolic_checks()
 net=network();pl=plane();sh=sphere();vr=variants()
 report={"paper":"015","question":"02","scope":"independent preliminary physics/math verification; manuscript and figures not yet complete",
         "verified_math":True,"document_complete":False,"question_accepted":False,"set_accepted":False,
         "original_question1_vertices":"adjacent, not opposite",
         "angle_convention":"b=(-sin(theta0),0,cos(theta0)); handwritten source/sink geometry uses negative-x half-plane, so phi=0 contains theta+theta0. It is not a sign error.",
         "surface_field_convention":"inside/outside limits distinguished; ideal current sheet has no unique same-point tangential B",
         "symbolic_checks":symbolic,"independent_numerical_checks":numerical,"normalization":meta,
         "network":net,"plane":pl,"sphere":sh,"variants":vr,
         "manuscript_sha256":sha(ROOT/"drafts/question-02.md"),
         "manuscript_written":True,"figure_count_expected":7,"figures_rendered":False,
         "source_sha256":{name:sha(ROOT.parent/name) for name in ["试卷.pdf","答案.pdf"]},
         "script_sha256":sha(Path(__file__)),"source_detail_manifest_sha256":sha(ROOT/"preview/originals/question-02-detail-manifest.json")}
 (ROOT/"build/question-02-preverification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"verified_math":True,"symbolic_checks":len(symbolic),"independent_numerical_checks":len(numerical),"max_network_center_field":net["all_pairs_max_field_error"],"exact_potentials":net["exact_grounded_potentials_per_IR"],"document_complete":False},ensure_ascii=False))
if __name__=="__main__":main()
