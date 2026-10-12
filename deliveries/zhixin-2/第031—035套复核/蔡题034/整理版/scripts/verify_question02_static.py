"""第034套第2题内部复核：完整三接触摩擦锥的静态承载上界。
这是资料疑点诊断，尚不等价于给出唯一的摩擦动力学过程。
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import minimize
ROOT=Path(__file__).resolve().parents[1]
r=-np.eye(3)
t=np.array([0,1,-1])/math.sqrt(2)
external=np.ones(3)/math.sqrt(3)
def torque(z):
    return np.cross(r,z.reshape(3,3)).sum(axis=0)
def objective(z):
    return np.dot(t,torque(z))
def equality(z):
    f=z.reshape(3,3)
    tau=torque(z)
    return np.r_[f.sum(axis=0)-external,tau[0],tau[1]+tau[2]]
def cones(z,mu):
    f=z.reshape(3,3)
    return np.array([mu*f[i,i]-np.linalg.norm(np.delete(f[i],i)) for i in range(3)])
def analytical(mu):
    if mu<1/math.sqrt(5):
        s=math.sqrt(1-mu*mu)
        return mu*(s+math.sqrt(2)-mu)/(math.sqrt(3)*(s+math.sqrt(2)*mu*mu))
    if mu<=1/math.sqrt(2):
        return 1/math.sqrt(6)
    return None
def main():
    rows=[]
    initial=(np.eye(3)/math.sqrt(3)).ravel()
    for mu in [.1,.2,.3,.4,1/math.sqrt(5),.46,.5,.6,.7,.71]:
        # 法向反力非负；高摩擦情形加有限上界只用于发现“任意滚起”推论的反例。
        bounds=[(0,50) if i==j else (-100,100) for i in range(3) for j in range(3)]
        result=minimize(objective,initial,method="SLSQP",bounds=bounds,
                        constraints=[{"type":"eq","fun":equality},
                                     {"type":"ineq","fun":lambda z:cones(z,mu)}],
                        options={"ftol":1e-12,"maxiter":2000})
        feasible=max(abs(equality(result.x)))<1e-7 and min(cones(result.x,mu))>-1e-7
        actual=-result.fun
        expected=analytical(mu)
        assert feasible,(mu,result.message)
        if expected is not None:
            assert abs(actual-expected)<1e-7,(mu,actual,expected)
        kd=mu*(1+math.sqrt(2)-mu)/(math.sqrt(3)*(1+math.sqrt(2)*mu*mu))
        rows.append(dict(mu=mu,static_limit_numerical=actual,static_limit_analytical=expected,
                         fixed_spin_friction_torque=kd,reactions=result.x.reshape(3,3).tolist(),
                         equality_residual=max(abs(equality(result.x))),
                         cone_min=float(min(cones(result.x,mu)))))
    # Additional direct counterexample: two admissible instantaneous motions
    # at the same force under a rigid Coulomb model. A homogeneous sphere is
    # used only as an allowed example, not silently added to the problem.
    mu,lam,G,mass,radius,inertia=.46,.6,1.,1.,1.,.4
    fcrit=G/(math.sqrt(6)*lam-1)
    applied=1.01*fcrit
    W=G+applied; w=W/math.sqrt(3)
    acc=(math.sqrt(2)*lam*applied-w)/(mass+2*inertia/radius**2)
    f=(w+mass*acc)/2
    s=f*f/w
    normal=w+s
    rolling=np.array([[0.,0.,0.],[f,normal,-s],[f,-s,normal]])
    alpha_roll=np.array([0.,acc/radius,-acc/radius])
    applied_torque=lam*radius*applied*t
    force_error_roll=rolling.sum(axis=0)-W*external-mass*np.array([acc,0,0])
    torque_error_roll=np.cross(radius*r,rolling).sum(axis=0)+applied_torque-inertia*alpha_roll
    needed=math.hypot(f,s)/normal
    pnormal=W*(1-2*mu)/(math.sqrt(3)*(1+math.sqrt(2)*mu*mu))
    nnormal=W*(math.sqrt(2)+mu)/(math.sqrt(6)*(1+math.sqrt(2)*mu*mu))
    p=mu*pnormal; fslide=mu*nnormal
    spinning=np.array([[pnormal,-p/math.sqrt(2),-p/math.sqrt(2)],
                       [fslide,nnormal,0],[fslide,0,nnormal]])
    net_torque=np.cross(radius*r,spinning).sum(axis=0)+applied_torque
    alpha_spin=np.dot(net_torque,t)/inertia
    force_error_spin=spinning.sum(axis=0)-W*external
    torque_error_spin=net_torque-inertia*alpha_spin*t
    assert acc>0 and needed<mu and alpha_spin>0 and pnormal>0
    assert np.max(abs(force_error_roll))<1e-12 and np.max(abs(torque_error_roll))<1e-12
    assert np.max(abs(force_error_spin))<1e-12 and np.max(abs(torque_error_spin))<1e-12
    both=dict(mu=mu,lam=lam,G=G,mass=mass,radius=radius,inertia=inertia,
              force=applied,geometric_unload_force=fcrit,
              rolling_acceleration=acc,rolling_friction_ratio=needed,
              rolling_reactions=rolling.tolist(),spin_angular_acceleration=alpha_spin,
              spin_reactions=spinning.tolist(),
              max_force_residual=float(max(np.max(abs(force_error_roll)),np.max(abs(force_error_spin)))),
              max_torque_residual=float(max(np.max(abs(torque_error_roll)),np.max(abs(torque_error_spin)))))
    data=dict(status="diagnostic_verified_not_final_answer",
              model="各接触点静摩擦矢量独立满足圆锥约束；不将静摩擦预设为固定轴滑动方向",
              rows=rows,instantaneous_two_mode_counterexample=both)
    (ROOT/"build/question02-static-diagnostic.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
