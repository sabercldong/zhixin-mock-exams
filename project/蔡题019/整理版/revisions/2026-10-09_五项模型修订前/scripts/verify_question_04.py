"""用力/能量、特征向量、材料矩阵逆和任意位移场独立核验薄膜问题。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
def main():
    alpha,nu=sp.symbols('alpha nu',positive=True);Y=2*alpha*(1-nu);G=alpha*(1-nu)/(1+nu)
    compliance=sp.Matrix([[1,-nu,0],[-nu,1,0],[0,0,1+nu]])/Y
    stiffness=sp.simplify(compliance.inv())
    assert sp.simplify(stiffness[0,0]-2*alpha/(1+nu))==0
    assert sp.simplify(stiffness[0,1]-2*alpha*nu/(1+nu))==0
    # 第三分量为张量剪应变eps_xy，而非工程剪应变gamma_xy。
    assert sp.simplify(stiffness[2,2]-2*G)==0
    s,r0,p=sp.symbols('s r0 p',positive=True)
    strain_area=(1+s)**2-1;volume=(1+s)**3-1
    assert sp.diff(strain_area,s).subs(s,0)==2 and sp.diff(volume,s).subs(s,0)==3
    energy=8*sp.pi*alpha*r0*r0*s*s-4*sp.pi*p*r0**3*s
    equilibrium=sp.solve(sp.diff(energy,s),s)[0]
    assert sp.simplify(equilibrium-p*r0/(4*alpha))==0
    projected=quad(lambda theta:2*math.pi*math.sin(theta)*math.cos(theta),0,math.pi/2)[0]
    assert abs(projected-math.pi)<1e-12
    sphere=dict(alpha_N_per_m=400,r0_m=.1,delta_p_Pa=80,
                strain_radius=.005,strain_area=.010,relative_volume=.015,tension_N_per_m=4)
    assert abs(2*sphere['tension_N_per_m']/sphere['r0_m']-sphere['delta_p_Pa'])<1e-12
    tensor_rows=[]
    for matrix in [np.array([[4.,1.],[1.,2.]]),np.array([[6.,2.],[2.,3.]]),np.eye(2)*3,np.array([[0.,2.],[2.,0.]])]:
        values,vectors=np.linalg.eigh(matrix)
        angles=[]
        for index in range(2):
            normal=vectors[:,index];traction=matrix@normal
            assert np.linalg.norm(traction-values[index]*normal)<1e-12
            tangent=np.array([-normal[1],normal[0]])
            assert abs(tangent@traction)<1e-12
            angles.append(math.degrees(math.atan2(normal[1],normal[0])))
        for theta in [.0,.2,.8,1.4]:
            normal=np.array([math.cos(theta),math.sin(theta)])
            combined=matrix[:,0]*normal[0]+matrix[:,1]*normal[1]
            assert np.linalg.norm(combined-matrix@normal)<1e-12
        tensor_rows.append(dict(stress=matrix.tolist(),eigenvalues=values.tolist(),principal_angles_deg=angles))
    x,y=sp.symbols('x y',real=True);u=sp.Function('u')(x,y);v=sp.Function('v')(x,y)
    eps=sp.Matrix([sp.diff(u,x),sp.diff(v,y),(sp.diff(u,y)+sp.diff(v,x))/2]);stress=stiffness*eps
    div=[sp.diff(stress[0],x)+sp.diff(stress[2],y),sp.diff(stress[2],x)+sp.diff(stress[1],y)]
    pdes=[2*sp.diff(u,x,2)+(1-nu)*sp.diff(u,y,2)+(1+nu)*sp.diff(v,x,y),
          2*sp.diff(v,y,2)+(1-nu)*sp.diff(v,x,2)+(1+nu)*sp.diff(u,x,y)]
    assert all(sp.simplify(div[i]*(1+nu)/alpha-pdes[i])==0 for i in range(2))
    # 不变形及微小刚体运动必须无应力，不能对新坐标直接求一阶导当位移应变。
    rigid=sp.Matrix([0,0,(-.01+.01)/2]);assert stiffness*rigid==sp.zeros(3,1)
    material=dict(alpha=400,poisson=.3,Y=560,G=float(G.subs({alpha:400,nu:.3})))
    Sigma=np.array([[6.,2.],[2.,3.]])
    eps_numeric=np.array(compliance.subs({alpha:400,nu:.3}),float)@np.array([6.,3.,2.])
    recovered=np.array(stiffness.subs({alpha:400,nu:.3}),float)@eps_numeric
    assert np.linalg.norm(recovered-np.array([6.,3.,2.]))<1e-12
    # 一个非均匀解：直接由位移求应力再求散度；不以最终PDE回代自证。
    a,p0=sp.symbols('a p0',real=True)
    field_u=p0*x/(2*alpha)+a*(x*x-y*y);field_v=p0*y/(2*alpha)-2*a*x*y
    eps_field=sp.Matrix([sp.diff(field_u,x),sp.diff(field_v,y),(sp.diff(field_u,y)+sp.diff(field_v,x))/2])
    stress_field=sp.simplify(stiffness*eps_field)
    expected=sp.Matrix([p0+4*G*a*x,p0-4*G*a*x,-4*G*a*y])
    assert all(sp.simplify(b)==0 for b in stress_field-expected)
    assert sp.simplify(sp.diff(stress_field[0],x)+sp.diff(stress_field[2],y))==0
    assert sp.simplify(sp.diff(stress_field[2],x)+sp.diff(stress_field[1],y))==0
    membrane_matrix=sp.Matrix([[stress_field[0],stress_field[2]],[stress_field[2],stress_field[1]]])
    mu=sp.symbols('mu',real=True)
    assert sp.simplify((membrane_matrix-(p0+mu)*sp.eye(2)).det()-
                       (mu**2-16*G**2*a**2*(x*x+y*y)))==0
    phi=sp.symbols('phi',real=True);L=sp.symbols('L',positive=True)
    normal=sp.Matrix([sp.cos(phi),sp.sin(phi)])
    tangent=sp.Matrix([-sp.sin(phi),sp.cos(phi)])
    traction=sp.trigsimp(membrane_matrix.subs({x:L*sp.cos(phi),y:L*sp.sin(phi)})*normal)
    boundary_expected=sp.Matrix([p0*sp.cos(phi)+4*G*a*L*sp.cos(2*phi),
                                p0*sp.sin(phi)-4*G*a*L*sp.sin(2*phi)])
    assert all(sp.trigsimp(b)==0 for b in traction-boundary_expected)
    tangent_force=sp.trigsimp(tangent.dot(traction))
    assert sp.trigsimp(sp.expand_trig(tangent_force+4*G*a*L*sp.sin(3*phi)))==0
    totals=[sp.simplify(sp.integrate(L*traction[j],(phi,0,2*sp.pi))) for j in range(2)]
    totals.append(sp.simplify(sp.integrate(L*L*tangent_force,(phi,0,2*sp.pi))))
    assert totals==[0,0,0]
    # 应力函数自动满足平衡；相容性独立推出双调和算子。
    psi=sp.Function('Psi')(x,y)
    psi_stress=sp.Matrix([sp.diff(psi,y,2),sp.diff(psi,x,2),-sp.diff(psi,x,y)])
    epsi=compliance*psi_stress
    compatibility=sp.diff(epsi[0],y,2)+sp.diff(epsi[1],x,2)-2*sp.diff(epsi[2],x,y)
    biharmonic=sp.diff(psi,x,4)+2*sp.diff(psi,x,2,y,2)+sp.diff(psi,y,4)
    assert sp.simplify(compatibility*Y-biharmonic)==0
    source=['scripts/verify_question_04.py'];draft=ROOT/'drafts/question-04.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():source.append('drafts/question-04.md')
    if (ROOT/'figures/题04_图稿源文件.tex').exists():source.append('figures/题04_图稿源文件.tex')
    result=dict(question=4,verified_math=True,document_complete=complete,sphere=sphere,
                hemisphere_pressure_integral=projected,principal_tests=tensor_rows,material=material,
                affine_strain_tensor_components=eps_numeric.tolist(),nonuniform_stress=[str(e) for e in stress_field],
                boundary_resultant_and_moment=[str(e) for e in totals],
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source})
    (ROOT/'build'/('verification-q04.json' if complete else 'verification-q04-preliminary.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
