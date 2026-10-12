"""从原始方程交叉核验第032套；不用最终答案重复自证。"""
from pathlib import Path
from fractions import Fraction as F
import json
import math
import numpy as np
from scipy.optimize import minimize, brentq
from scipy.integrate import solve_ivp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

ROOT=Path(__file__).resolve().parents[1]


def q1():
    volume=lambda h:h*(1-h*h)/(4*math.pi)
    optimum=minimize(lambda x:-volume(x[0]),[.6],bounds=[(1e-8,1-1e-8)],tol=1e-13)
    hm=float(optimum.x[0]);vm=volume(hm)
    expected=1/(6*math.sqrt(3)*math.pi)
    assert abs(vm-expected)<1e-12
    roots=[brentq(lambda x:volume(x)-.38*vm,*interval) for interval in [(0,hm),(hm,1)]]
    for h in roots:
        radius=math.sqrt(.38*vm/(math.pi*h))
        assert abs(math.hypot(h,2*math.pi*radius)-1)<1e-10
    return dict(status='pass',max_height_over_L=hm,max_volume_over_L3=vm,
                limiting_heights_over_L=roots,theta_deg=math.degrees(math.acos(math.sqrt(2/3))))


def q2():
    outcomes=[]
    for mu in [.02,.1,.3,.7,1,1.4,3,10]:
        # Ground impulse=(x,y); wall impulse=(-x,d). Both magnitude <=1.
        con=[{'type':'ineq','fun':lambda a:1-a[0]**2-a[1]**2},
             {'type':'ineq','fun':lambda a:1-a[0]**2-a[2]**2},
             {'type':'ineq','fun':lambda a,mu=mu:mu*a[1]-a[0]},
             {'type':'ineq','fun':lambda a,mu=mu:mu*a[0]-a[2]}]
        result=minimize(lambda a:-a[1]-a[2],[.03,.6,.001],bounds=[(0,1)]*3,
                        constraints=con,method='SLSQP',options={'ftol':1e-12,'maxiter':2000})
        value=-result.fun
        theory=math.sqrt(1+mu*mu) if mu<=1 else 2*mu/math.sqrt(1+mu*mu)
        assert abs(value-theory)<2e-8,(mu,result)
        # Optimize steady wall impulse directly; X=u*cos(18), Z=vertical launch speed.
        result2=minimize(lambda a:-a[0]*a[1],[.25,.1],bounds=[(0,.5)]*2,
                         constraints=[{'type':'ineq','fun':lambda a:.25-a[0]**2-a[1]**2},
                                      {'type':'ineq','fun':lambda a,mu=mu:mu*a[0]-a[1]}],
                         method='SLSQP',options={'ftol':1e-13,'maxiter':1000})
        product=-result2.fun
        expected=.25*mu/(1+mu*mu) if mu<=1 else .125
        assert abs(product-expected)<2e-9
        X,Z=result2.x;u=X/math.cos(math.pi/10);t=2*Z
        radius=u*t/(2*math.cos(math.pi/10))
        # Reconstruct all five flights in 3D; endpoints have equal height.
        points=[np.array([radius*math.cos(4*j*math.pi/5),radius*math.sin(4*j*math.pi/5),0]) for j in range(6)]
        for j in range(5):
            v=(points[j+1]-points[j])/t+np.array([0,0,Z])
            end=points[j]+v*t-np.array([0,0,t*t/2])
            assert np.linalg.norm(end-points[j+1])<1e-9
        outcomes.append(dict(mu=mu,two_kick_final_speed_over_v0=value,
                             maximum_radius_over_v0sq_g=radius))
    return dict(status='pass',cases=outcomes)


def exact_network(edges,source,sink,nodes):
    keep=[x for x in nodes if x!=sink]
    m=[[F(0) for _ in keep] for _ in keep];b=[F(int(x==source)) for x in keep]
    for a,c,resistance in edges:
        g=1/F(resistance)
        for x,y in [(a,c),(c,a)]:
            if x==sink:continue
            i=keep.index(x);m[i][i]+=g
            if y!=sink:m[i][keep.index(y)]-=g
    for i in range(len(keep)):
        pivot=m[i][i];assert pivot
        m[i]=[x/pivot for x in m[i]];b[i]/=pivot
        for j in range(len(keep)):
            if j==i:continue
            factor=m[j][i]
            m[j]=[x-factor*y for x,y in zip(m[j],m[i])];b[j]-=factor*b[i]
    return b[keep.index(source)]


def lattice_resistance(size,changes,source,sink):
    total=2*size*size
    index=lambda i,j,s:2*((i%size)*size+(j%size))+s
    A=index(0,0,0);B=index(0,0,1);C=index(-1,0,1);D=index(0,-1,1)
    ids={'A':A,'B':B,'C':C,'D':D}
    matrix=lil_matrix((total,total),dtype=float)
    for i in range(size):
        for j in range(size):
            a=index(i,j,0)
            for c in [index(i,j,1),index(i-1,j,1),index(i,j-1,1)]:
                r=changes.get(tuple(sorted((a,c))),1)
                if r is None:continue
                g=1/r
                matrix[a,a]+=g;matrix[c,c]+=g;matrix[a,c]-=g;matrix[c,a]-=g
    src,ground=ids[source],ids[sink]
    keep=np.array([i for i in range(total) if i!=ground])
    rhs=np.zeros(total);rhs[src]=1
    potential=spsolve(matrix.tocsr()[keep][:,keep],rhs[keep])
    return float(potential[np.where(keep==src)[0][0]])


def q3():
    rest=[('B','C',3),('C','D',3),('D','B',3)]
    modified=rest+[('A','B',2),('A','C',3),('A','D',4)]
    RBC=exact_network(modified,'B','C',['A','B','C','D'])
    RAB=exact_network(modified,'A','B',['A','B','C','D'])
    assert RBC==F(67,47) and RAB==F(58,47)
    tests=[]
    for size in [12,24,48]:
        index=lambda i,j,s:2*((i%size)*size+(j%size))+s
        A=index(0,0,0);B=index(0,0,1);C=index(-1,0,1);D=index(0,-1,1)
        edge=lambda a,b:tuple(sorted((a,b)))
        rows=[('intact',{},'B','C',1),('removed',{edge(A,B):None,edge(A,C):None},'B','C',2),
              ('modified_BC',{edge(A,B):2,edge(A,C):3,edge(A,D):4},'B','C',float(RBC)),
              ('modified_AB',{edge(A,B):2,edge(A,C):3,edge(A,D):4},'A','B',float(RAB))]
        for name,changes,src,sink,expected in rows:
            result=lattice_resistance(size,changes,src,sink)
            assert abs(result-expected)<4/size**2,(name,size,result,expected)
            tests.append(dict(size=size,case=name,resistance_over_r=result,target=expected))
    return dict(status='pass',R1_over_r=1,R2_over_r=2,R3_over_r=str(RBC),RAB_over_r=str(RAB),
                finite_periodic_lattice_checks=tests)


def q4():
    results=[]
    for delta,label in [(1,'题给准静态绝热流出模型'),(.5,'自由分子逸出能量模型对照')]:
        def rhs(t,y):
            N,O,T=y;dN=-N*math.sqrt(T/28);dO=-O*math.sqrt(T/32)
            return [dN,dO,delta*T*(dN+dO)/(2.5*(N+O))]
        def half(t,y):return (y[0]+y[1])*y[2]-.5
        half.terminal=True;half.direction=-1
        solution=solve_ivp(rhs,(0,100),[.78,.22,1],events=half,rtol=2e-11,atol=1e-13)
        N,O,T=solution.y[:,-1];n=N+O
        expected=.5**(1/(1+delta/2.5))
        assert abs(n-expected)<2e-10
        assert abs(math.log(N/.78)-math.sqrt(32/28)*math.log(O/.22))<2e-10
        results.append(dict(model=label,total_fraction=n,temperature_fraction=T,N2_fraction=N/n,
                            O2_fraction=O/n,mole_ratio_N2_O2=N/O))
    return dict(status='pass',models=results)


def q5():
    # Node potentials include bond emf from a fixed uniform-field gauge.
    # x=0,1,2,3; upper/lower; omit capacitor bond at x=1.
    positions=[(x,y) for x in range(4) for y in [0,1]]
    edges=[]
    for x in range(3):
        for y in [0,1]:edges.append(((x,y),(x+1,y)))
    for x in [0,2,3]:edges.append(((x,0),(x,1)))
    matrix=np.zeros((8,8));rhs=np.zeros(8)
    emf=lambda a,b:.5*((a[1]+b[1])/2*(b[0]-a[0])-(a[0]+b[0])/2*(b[1]-a[1]))
    for a,b in edges:
        i,j=positions.index(a),positions.index(b);e=emf(a,b)
        matrix[i,i]+=1;matrix[j,j]+=1;matrix[i,j]-=1;matrix[j,i]-=1
        rhs[i]-=e;rhs[j]+=e
    potential=np.zeros(8);potential[1:]=np.linalg.solve(matrix[1:,1:],rhs[1:])
    current=lambda a,b:potential[positions.index(a)]-potential[positions.index(b)]+emf(a,b)
    IAB=current((0,0),(0,1))
    Ucap=potential[positions.index((1,1))]-potential[positions.index((1,0))]+emf((1,1),(1,0))
    heat=sum(current(a,b)**2 for a,b in edges)
    assert abs(IAB-9/23)<1e-12 and abs(Ucap+4/23)<1e-12 and abs(heat-26/23)<1e-12
    noemf=[(str(a),str(b),1) for a,b in edges]
    Rth=exact_network(noemf,str((1,1)),str((1,0)),[str(x) for x in positions])
    assert Rth==F(33,23)
    for U in [-.6,-4/23,0,.5]:
        currents=np.linalg.solve(np.array([[4,-1,0],[-1,4,-1],[0,-1,4]],float),[1-U,1+U,1])
        assert abs(currents[0]-currents[1]-(-4-23*U)/56)<1e-12
    return dict(status='pass',AB_up_current_over_e_r=IAB,capacitor_top_minus_bottom_over_e=Ucap,
                heat_power_over_e2_r=heat,removed_edge_port_Rth_over_r=str(Rth),
                capacitor_plate_port_Rth_over_r=str(Rth+1))


def q6():
    b=.8;z=.6;alpha=math.pi/6;gamma=1/math.sqrt(1-b*b)
    cosine=(math.cos(alpha)-b)/(1-b*math.cos(alpha))
    theta=math.acos(cosine)
    n=np.array([math.cos(alpha),-math.sin(alpha)])
    # Construct emission and interception events and reverse the null path.
    emission=[0,gamma];events=[]
    for t0 in emission:
        x0=np.array([b*t0,0.]);hit=(100+(1-b*n[0])*t0)/(1+z)
        position=x0+(hit-t0)*n
        assert abs(np.dot(n,position)-(100-z*hit))<1e-11
        travel=-position[1]/(-n[1]);ret=hit+travel;point=position-travel*n
        assert abs(point[1])<1e-11 and abs(point[0]-b*t0)<1e-11
        events.append(dict(emission=t0,hit=hit,hit_point=position.tolist(),return_time=ret,return_point=point.tolist()))
    dt_hit=events[1]['hit']-events[0]['hit'];proper=dt_hit*math.sqrt(1-z*z)
    signed=events[1]['return_time']-events[0]['return_time']
    assert abs(proper-(5-2*math.sqrt(3))/6)<1e-11
    assert abs(signed-5*(1-2*math.sqrt(3))/12)<1e-11
    dx=events[1]['return_point'][0]-events[0]['return_point'][0]
    assert dx*dx-signed*signed>0
    delta_hit=np.array(events[1]['hit_point'])-np.array(events[0]['hit_point'])
    frame_interval=(dt_hit+z*np.dot(n,delta_hit))/math.sqrt(1-z*z)
    assert abs(frame_interval-proper)<1e-12
    return dict(status='pass',theta_deg=math.degrees(theta),received_zombie_frame_coordinate_interval_s=frame_interval,
                signed_x_axis_arrival_interval_s=signed,absolute_arrival_interval_s=abs(signed),
                return_events_spacelike=True,events=events)


def q7():
    n0,n1,n2=1.,1.52,1.72
    a=(n0-n1)/(n0+n1);b=(n1-n2)/(n1+n2)
    t01=2*n0/(n0+n1);t10=2*n1/(n0+n1);r10=-a
    errors=[]
    for phase in np.linspace(0,2*math.pi,101):
        q=r10*b*np.exp(1j*phase)
        series=a+sum(t01*t10*b*np.exp(1j*phase)*q**j for j in range(60))
        closed=(a+b*np.exp(1j*phase))/(1+a*b*np.exp(1j*phase))
        errors.append(abs(series-closed))
        transmitted=t01*2*n1/(n1+n2)*np.exp(.5j*phase)/(1+a*b*np.exp(1j*phase))
        assert abs(abs(series)**2+n2/n0*abs(transmitted)**2-1)<1e-12
    assert max(errors)<1e-12
    return dict(status='pass',complex_series_checks=101,max_amplitude_error=max(errors),
                R1=a*a,R2=b*b,Rmax=((a+b)/(1+a*b))**2,Rmin=((a-b)/(1-a*b))**2,
                optimal_film_index=math.sqrt(n0*n2))


def q8():
    G=.12;g=9.8;K=G*G/(8*math.pi**2*g);R=.8
    # Integrate pressure-gradient surface equation, not the claimed closed form.
    rhs=lambda r,y:[(G/(2*math.pi*r))**2/(g*r)]
    solution=solve_ivp(rhs,(R,.03),[0],dense_output=True,rtol=1e-11,atol=1e-13)
    errors=[]
    for r in np.linspace(.03,R,70):
        z=float(solution.sol(r)[0]);closed=K*(1/R**2-1/r**2)
        errors.append(abs(z-closed));assert abs(z-closed)<1e-10
        v=G/(2*math.pi*r)
        assert abs(g*z+.5*v*v-.5*(G/(2*math.pi*R))**2)<1e-9
    return dict(status='pass',radial_integration_checks=70,max_height_error=max(errors),
                model='弱径向入流、自由涡、忽略径向和竖直速度对自由表面主阶的贡献；只用于非零半径外区。')


def main():
    build=ROOT/'build';build.mkdir(exist_ok=True)
    for i,function in enumerate([q1,q2,q3,q4,q5,q6,q7,q8],1):
        result=function()
        (build/f'question{i:02}-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(i,result,flush=True)


if __name__=='__main__':main()
