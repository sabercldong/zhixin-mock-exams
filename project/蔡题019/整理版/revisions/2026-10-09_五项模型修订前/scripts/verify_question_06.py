"""薄板四端测量：边界、实际电流通量、保角映射与独立电阻网格。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.fft import dctn,idctn
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]

def quarter_v_grad(point):
    point=np.array(point,dtype=float)
    result=0.;gradient=np.zeros(2)
    for center,sign in [([0.,1.],1),([0.,-1.],1),([1.,0.],-1),([-1.,0.],-1)]:
        vector=point-np.array(center);distance=np.linalg.norm(vector)
        result+=sign*math.log(distance)/math.pi
        gradient+=sign*vector/(math.pi*distance**2)
    return result,gradient

def network_voltage(lam,m,L):
    # 均匀方格每条相邻支路电导为1。全部边界无电流；
    # A与D从边界分别注入/抽出1，解图拉普拉斯，不使用解析势。
    h=1/(m+.5);n=int(round(L/h))
    rhs=np.zeros((n,n));rhs[m,0]=1;rhs[0,m]=-1
    modes=dctn(rhs,type=2,norm='ortho')
    eigen=4*np.sin(np.pi*np.arange(n)/(2*n))**2
    denominator=eigen[:,None]+eigen[None,:]
    denominator[0,0]=1;modes[0,0]=0
    voltage=idctn(modes/denominator,type=2,norm='ortho')
    coordinate=(np.arange(n)+.5)*h
    # 非接触点的绝缘边界，二阶外推到板边。
    vb=np.interp(lam,coordinate,(9*voltage[:,0]-voltage[:,1])/8)
    vc=np.interp(lam,coordinate,(9*voltage[0,:]-voltage[1,:])/8)
    # 独立检查节点总电流及互易对称性。
    residual=np.zeros_like(voltage)
    residual[:-1,:]+=voltage[:-1,:]-voltage[1:,:]
    residual[1:,:]+=voltage[1:,:]-voltage[:-1,:]
    residual[:,:-1]+=voltage[:,:-1]-voltage[:,1:]
    residual[:,1:]+=voltage[:,1:]-voltage[:,:-1]
    assert np.max(np.abs(residual-rhs))<2e-12
    assert abs(vb+vc)<2e-12
    return dict(grid=n,spacing=h,outer_extent=n*h,U_over_I=vb-vc,
                node_current_residual=float(np.max(np.abs(residual-rhs))))

def disk_v_grad(point):
    point=np.array(point,dtype=float);a=point-np.array([1.,0.]);d=point-np.array([-1.,0.])
    return math.log(np.linalg.norm(d)/np.linalg.norm(a))/math.pi,(
        d/(d@d)-a/(a@a))/math.pi

def main():
    lam=sp.symbols('lambda',positive=True)
    vb=sp.log((1+lam**2)/(1-lam**2))/sp.pi
    assert sp.simplify(sp.diff(vb,lam)-4*lam/(sp.pi*(1-lam**4)))==0
    boundary=[]
    for coordinate in [.13,.41,.76,1.37,2.6]:
        bottom=quarter_v_grad([coordinate,0.])[1][1]
        left=quarter_v_grad([0.,coordinate])[1][0]
        assert abs(bottom)<1e-13 and abs(left)<1e-13
        boundary.append(dict(coordinate=coordinate,bottom_normal_gradient=bottom,left_normal_gradient=left))
    flux=[]
    for rho in [1e-2,1e-3]:
        def outward(angle):
            unit=np.array([math.cos(angle),math.sin(angle)])
            return -quarter_v_grad(np.array([1.,0.])+rho*unit)[1]@unit*rho
        value=quad(outward,0,math.pi,epsabs=1e-11)[0]
        assert abs(value-1)<1e-11
        flux.append(dict(model='quarter',radius=rho,normalized_source_current=value))
    samples=[]
    for value in [.1,.3,.5,.8,.95]:
        u=quarter_v_grad([value,0.])[0]-quarter_v_grad([0.,value])[0]
        expected=2/math.pi*math.log((1+value*value)/(1-value*value))
        # 独立保角映射w=(z/l)^2后，半平面单源单汇势差。
        zB=complex(value,0.);zC=complex(0.,value)
        half=lambda w:math.log(abs(w+1)/abs(w-1))/math.pi
        mapped=half(zB**2)-half(zC**2)
        assert abs(u-expected)<2e-14 and abs(mapped-u)<2e-14
        samples.append(dict(lam=value,U_over_I=u,half_plane_result=mapped))
    general=[]
    for omega in [math.pi/3,math.pi/2,3*math.pi/4,math.pi]:
        p=math.pi/omega;s=.5**p
        mapped=2/math.pi*math.log((1+s)/(1-s))
        general.append(dict(angle=omega,power=p,lambda_value=.5,U_over_I=mapped))
    exact=2/math.pi*math.log(5/3)
    grids=[network_voltage(.5,m,16) for m in [16,32,64]]
    for row in grids:row['relative_error']=abs(row['U_over_I']/exact-1)
    assert grids[-1]['relative_error']<.003
    assert grids[-1]['relative_error']<grids[0]['relative_error']
    extents=[network_voltage(.5,64,L) for L in [4,8,16]]
    for row in extents:row['relative_error']=abs(row['U_over_I']/exact-1)
    assert extents[-1]['relative_error']<extents[0]['relative_error']
    disk_boundary=[]
    for angle in np.linspace(.1,2*math.pi-.1,30):
        point=np.array([math.cos(angle),math.sin(angle)])
        normal=float(disk_v_grad(point)[1]@point)
        assert abs(normal)<1e-12;disk_boundary.append(normal)
    for rho in [1e-2,1e-3]:
        lo=math.acos(-rho/2)
        def inward_arc(angle):
            unit=np.array([math.cos(angle),math.sin(angle)])
            return -disk_v_grad(np.array([1.,0.])+rho*unit)[1]@unit*rho
        value=quad(inward_arc,lo,2*math.pi-lo,epsabs=1e-11)[0]
        assert abs(value-1)<1e-11
        flux.append(dict(model='disk',radius=rho,normalized_source_current=value))
    B=[.5,math.sqrt(3)/2];C=[-.5,math.sqrt(3)/2]
    u_disk=disk_v_grad(B)[0]-disk_v_grad(C)[0]
    assert abs(u_disk-math.log(3)/math.pi)<1e-14
    # 积分电场沿板内折线路径，而非仅回代测得电压公式。
    def line_integral(f,start,end):
        start=np.array(start);delta=np.array(end)-start
        return quad(lambda s:float(-f(start+s*delta)[1]@delta),0,1,epsabs=1e-11)[0]
    integral_q=line_integral(quarter_v_grad,[.5,0.],[.5,.5])+line_integral(quarter_v_grad,[.5,.5],[0.,.5])
    integral_d=line_integral(disk_v_grad,B,C)
    assert abs(integral_q-exact)<1e-12 and abs(integral_d-u_disk)<1e-12
    examples=dict(I_A=.01,t_m=1e-4,U_V=.001,
                  quarter_sigma_S_per_m=2*.01/(math.pi*1e-4*.001)*math.log(5/3),
                  disk_sigma_S_per_m=.01*math.log(3)/(math.pi*1e-4*.001),
                  original_linear_sigma_S_per_m=2*.01/(math.pi*1e-4*.001)*math.log(3),
                  quarter_U_V_if_sigma_1e6=.01/(1e6*1e-4)*exact,
                  disk_U_V_if_sigma_1e6=.01/(1e6*1e-4)*u_disk)
    assert examples['quarter_sigma_S_per_m']>0
    variants=dict(same_material_voltage_ratio=exact/u_disk,
                  corner_microV_if_disk_70=70*exact/u_disk,
                  inferred_angle_rad=math.pi/3,
                  voltage_V_for_sixty_deg=.02/math.pi*math.log(9/7),
                  ninety_degree_disk_geometry=math.log(2)/math.pi,
                  lambda_error_relative=(2/(15/16)/math.log(5/3))*.005)
    # 一般角部反算幂、圆周等角弦长与差分灵敏度另行核验。
    s=(9/7-1)/(9/7+1)
    inferred_power=math.log(s)/math.log(.5)
    assert abs(inferred_power-3)<1e-12
    for angle in [math.pi/6,math.pi/3,math.pi/2]:
        points=[np.array([math.cos(j*angle),math.sin(j*angle)]) for j in range(4)]
        a,b,c,d=points
        cross_ratio=np.linalg.norm(b-d)*np.linalg.norm(c-a)/(np.linalg.norm(b-a)*np.linalg.norm(c-d))
        assert abs(cross_ratio-4*math.cos(angle/2)**2)<1e-13
    f=lambda l:math.log((1+l*l)/(1-l*l))
    eps=1e-6
    numerical_derivative=(f(.5+eps)-f(.5-eps))/(2*eps)
    assert abs(numerical_derivative-2/(15/16))<2e-9
    paths=['scripts/verify_question_06.py'];draft=ROOT/'drafts/question-06.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():paths.append('drafts/question-06.md')
    if (ROOT/'figures/题06_图稿源文件.tex').exists():paths.append('figures/题06_图稿源文件.tex')
    result=dict(question=6,verified_math=True,document_complete=complete,
                model_note='角部夹角尚未确认；直角及一般夹角分别处理，不把模型未决当作整套完成',
                boundary=boundary,source_flux=flux,quarter_samples=samples,wedge_examples=general,
                grid_refinement=grids,grid_extent=extents,disk_boundary_max=max(map(abs,disk_boundary)),
                field_line_integrals=dict(quarter=integral_q,disk=integral_d),examples=examples,variants=variants,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    path=ROOT/'build'/('verification-q06.json' if complete else 'verification-q06-preliminary.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=6,passed=True,grid_refinement=grids,grid_extent=extents,examples=examples,variants=variants),ensure_ascii=False))

if __name__=='__main__':main()
