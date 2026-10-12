"""初步核验：圆截面环形磁通积分与实际闭合螺旋曲线的Neumann互感。"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from scipy.integrate import quad, solve_ivp

ROOT=Path(__file__).resolve().parents[1]

def helix(n,minor,coil,handedness=1,points=1024):
    t=np.arange(points)*2*math.pi/points
    rho=1+minor*np.cos(n*t);dr=-minor*n*np.sin(n*t)
    if coil==1:
        xyz=np.column_stack((rho*np.cos(t),rho*np.sin(t),minor*np.sin(n*t)))
        tangent=np.column_stack((dr*np.cos(t)-rho*np.sin(t),dr*np.sin(t)+rho*np.cos(t),minor*n*np.cos(n*t)))
    else:
        # major circle in xz, centre (1,0,0); sign of y sets minor winding chirality.
        xyz=np.column_stack((1+rho*np.cos(t),handedness*minor*np.sin(n*t),rho*np.sin(t)))
        tangent=np.column_stack((dr*np.cos(t)-rho*np.sin(t),handedness*minor*n*np.cos(n*t),dr*np.sin(t)+rho*np.cos(t)))
    return xyz,tangent

def neumann(n1,n2,minor,handedness=-1,points=1024):
    x,dx=helix(n1,minor,1,points=points)
    y,dy=helix(n2,minor,2,handedness=handedness,points=points)
    return neumann_paths(x,dx,y,dy)

def neumann_paths(x,dx,y,dy):
    points=len(x)
    total=0.
    for start in range(0,points,64):
        displacement=x[start:start+64,None,:]-y[None,:,:]
        distances=np.linalg.norm(displacement,axis=2)
        dot=dx[start:start+64]@dy.T
        total+=float(np.sum(dot/distances))
    return total*(2*math.pi/points)**2/(4*math.pi)

def main():
    flux=[]
    for minor in [.02,.05,.1,.2,.4]:
        integral=quad(lambda t:2*minor**2*math.sin(t)**2/(1+minor*math.cos(t)),0,math.pi,epsabs=1e-13,epsrel=1e-12)[0]/(2*math.pi)
        exact=minor**2/(1+math.sqrt(1-minor**2))
        assert abs(integral-exact)<1e-12
        flux.append(dict(r_over_R=minor,integrated_flux_per_NI=integral,exact_flux_per_NI=exact,thin_flux_per_NI=minor**2/2))
    helical=[]
    for n1,n2 in [(12,16),(24,32)]:
        minor=.08
        coefficient=minor**2/(1+math.sqrt(1-minor**2))
        for handedness,sign in [(-1,1),(1,-1)]:
            low=neumann(n1,n2,minor,handedness=handedness,points=1024)
            high=neumann(n1,n2,minor,handedness=handedness,points=2048)
            prediction=coefficient*(n1+sign*n2)
            helical.append(dict(N1=n1,N2=n2,minor_winding_sign=handedness,
                                coarse_neumann=low,fine_neumann=high,continuous_sheet_prediction=prediction,
                                relative_difference_to_sheet=(high-prediction)/prediction,
                                quadrature_refinement_absolute_change=abs(high-low)))
            assert abs(high-low)<1e-9
            assert abs((high-prediction)/prediction)<.01
    x,dx=helix(24,.08,1,points=1024)
    y,dy=helix(32,.08,2,handedness=-1,points=1024)
    forward=neumann_paths(x,dx,y,dy);reverse=neumann_paths(y,dy,x,dx)
    assert abs(forward-reverse)<1e-12
    major_major=neumann(1,1,0.,points=1024)
    assert abs(major_major)<1e-13
    # 独立极坐标体积积分：直接用磁场能量密度，不重复条带磁通积分。
    energy=[]
    for minor in [.05,.2,.4]:
        n=7.;current=.3
        def shell(s):
            return quad(lambda theta:(n*current/(2*math.pi*(1+s*math.cos(theta))))**2
                        *math.pi*(1+s*math.cos(theta))*s,0,2*math.pi,epsabs=1e-12)[0]
        integrated=quad(shell,0,minor,epsabs=1e-12)[0]
        expected=.5*n*n*current*current*(1-math.sqrt(1-minor*minor))
        assert abs(integrated-expected)<1e-12
        energy.append(dict(r_over_R=minor,volume_integrated_energy=integrated,energy_from_inductance=expected))
    # 带电阻初级的时域ODE与直接有效值积分，独立核验相量结果。
    mu0=4*math.pi*1e-7;R=.1;r=.01;n1=1000;n2=1500;U=12.;f=1000.;rw=2.
    coefficient=mu0*r*r/(R+math.sqrt(R*R-r*r));L=n1*n1*coefficient;M=(n1+n2)*coefficient
    omega=2*math.pi*f
    solution=solve_ivp(lambda t,y:[(math.sqrt(2)*U*math.cos(omega*t)-rw*y[0])/L],
                       [0,20/f],[0.],rtol=1e-10,atol=1e-11,dense_output=True,max_step=1/(f*100))
    times=np.linspace(10/f,20/f,20001);current=solution.sol(times)[0]
    secondary=M*(math.sqrt(2)*U*np.cos(omega*times)-rw*current)/L
    rms=math.sqrt(float(np.trapezoid(secondary**2,times)/(times[-1]-times[0])))
    prediction=U*omega*abs(M)/math.hypot(rw,omega*L)
    assert abs(rms-prediction)/prediction<1e-8
    circuit=dict(C=coefficient,L1=L,Mplus=M,Mminus_abs=abs(n1-n2)*coefficient,
                 reactance=omega*L,current_rms=U/math.hypot(rw,omega*L),phase_lag=math.atan2(omega*L,rw),
                 ideal_secondary=U*M/L,ode_secondary_rms=rms,phasor_secondary_rms=prediction,
                 thin_relative_underestimate=1-(mu0*r*r/(2*R))/coefficient)
    files=['scripts/verify_question_05.py','scripts/generate_question_05_mesh.py','drafts/question-05.md',
           'figures/题05_图稿源文件.tex','figures/question-05-mesh.tex']
    draft=(ROOT/'drafts/question-05.md').read_text()
    assert len([line for line in draft.splitlines() if line.startswith('## ')])==9
    assert 'DRAFT' not in draft
    report=dict(question=5,verified_math=True,document_complete=True,model_conditions_required=True,
                normalization='mu0=R=1 for field and Neumann checks',cross_section_flux=flux,actual_helix_neumann=helical,
                reciprocal_integrals=[forward,reverse],symmetric_major_major=major_major,volume_energy=energy,circuit=circuit,
                source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    (ROOT/'build'/'verification-q05.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
