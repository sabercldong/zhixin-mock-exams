"""第031套：按研究对象独立积分、事件求根与光线追迹核验。

手写答案不是数值程序的输入；程序从受力、热量及速度关系重建结果。
第3题的滑动摩擦系数等于给定最大静摩擦系数属于明确模型约定。
第5题旋转圆环结论只验收缓慢翻转且相对运动不中断的分支。
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar
from check_rotating_ring import experiment

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'build'

def close(actual,expected,rtol=2e-8,atol=2e-9):
    assert np.isclose(actual,expected,rtol=rtol,atol=atol),(actual,expected)

def save(q,method,checks,limitations=None):
    record=dict(status='pass',method=method,checks=checks)
    if limitations:record['model_limitations']=limitations
    (DEST/f'question{q:02}-verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(f'第{q}题通过：{method}',flush=True)

def q1():
    rho,G,R=1.7,.83,2.3
    def mass(s):return quad(lambda r:4*np.pi*rho*r*r,0,s,epsabs=1e-11)[0]
    def pressure(s):return quad(lambda r:0 if r==0 else rho*G*mass(r)/r**2,s,R,epsabs=1e-11)[0]
    checks=[]
    for s in (0,.2*R,.7*R,R):
        value=pressure(s);close(value,2*np.pi*G*rho*rho*(R*R-s*s)/3)
        checks.append(dict(radius=s,pressure=value))
    ug=-quad(lambda r:0 if r==0 else G*mass(r)/r*4*np.pi*rho*r*r,0,R)[0]
    pv=quad(lambda r:4*np.pi*r*r*pressure(r),0,R)[0]
    close(3*pv,-ug)
    for n in (.3,2.,7.):
        m,h,A=1.2,.9,.7;degenerate=A*n/m*(h*n**(1/3))**2
        supported=brentq(lambda radius:2*np.pi*G*(n*m)**2*radius**2/3-degenerate,1e-8,10)
        predicted=np.sqrt(3*A*h*h/(2*np.pi*G*m**3*n**(1/3)))
        close(supported,predicted)
        checks.append(dict(number_density=n,support_radius=supported))
    save(1,'数值积分壳层质量、静力梯度及引力能，独立求支撑半径',checks,
         '均匀密度加给定压强只给粗略支撑尺度，不强加严格局部简并状态方程。')

def polygon_turn(radius,coefficient):
    vertices=np.array([[radius*np.cos(a),radius*np.sin(a)] for a in (np.pi/2,np.pi/2+2*np.pi/3,np.pi/2+4*np.pi/3,np.pi/2+2*np.pi)])
    total=0.
    for a,b in zip(vertices[:-1],vertices[1:]):
        velocity=b-a
        total+=quad(lambda t:-coefficient*((a+t*velocity)[0]*velocity[1]-(a+t*velocity)[1]*velocity[0]),0,1)[0]
    return total

def q2():
    checks=[]
    # m=M=r=1; 圆周角动量给 (I+mr²)theta'=-mr²psi'。
    circle=solve_ivp(lambda t,y:[-1/(.5+1)],(0,2*np.pi),[0.],rtol=1e-11,atol=1e-12).y[0,-1]
    close(circle,-4*np.pi/3)
    fixed=polygon_turn(1,1/.5);free=polygon_turn(.5,2/.5)
    close(fixed,-3*np.sqrt(3));close(free,-3*np.sqrt(3)/2)
    checks.append(dict(circle=circle,fixed_triangle=fixed,free_triangle=free))
    for M,m in ((2.,.7),(.5,1.3),(1.,1.)):
        I=M/2;mu=M*m/(M+m);cmradius=M/(M+m)
        # 相对向量 P-O=(M+m)/M * (P-C)，绕共同质心积分。
        angle=polygon_turn(cmradius,mu/I*((M+m)/M)**2)
        close(angle,-3*np.sqrt(3)*m/(M+m))
        checks.append(dict(disk_mass=M,person_mass=m,free_triangle_angle=angle))
    save(2,'对实际三角形各边积分角动量，圆周约束角速度积分及不等质量交叉核验',checks)

def cycle(eps):
    pl,ph=1-eps,1+eps;va=.5/pl;vc=2/ph
    states=[(va,pl),(va,ph),(vc,ph),(vc,pl)]
    heats=[];works=[]
    for i,(v,p) in enumerate(states):
        vn,pn=states[(i+1)%4]
        work=0 if vn==v else quad(lambda volume:p,v,vn)[0]
        du=2.5*(pn*vn-p*v)
        works.append(work);heats.append(du+work)
    return dict(states=states,works=works,heats=heats,work=sum(works),
                heat_in=sum(q for q in heats if q>0),heat_out=-sum(q for q in heats if q<0))

def q3():
    data=cycle(.25)
    for x,y in zip(data['heats'],(5/6,49/12,-2,-49/20)):close(x,y)
    close(data['work'],7/15);close(data['heat_in'],59/12);close(data['heat_out'],89/20)
    close(data['work']/data['heat_in'],28/295)
    optimum=minimize_scalar(lambda eps:-cycle(eps)['work']/cycle(eps)['heat_in'],bounds=(.001,.599),method='bounded',options={'xatol':1e-13})
    eps_star=(105-12*np.sqrt(35))/95
    close(optimum.x,eps_star,rtol=2e-7)
    # 稳态闭合回路压差乘体积变化等于摩擦耗散；外界p0的净功为零。
    dv=data['states'][2][0]-data['states'][0][0];close(data['work'],2*.25*dv)
    data['optimum_eps']=float(optimum.x);data['optimum_efficiency']=float(-optimum.fun)
    save(3,'四段过程分别积分边界功、由理想气体内能差重算吸放热并数值优化',data,
         '原题只给最大静摩擦力；稳定准静态回路采用动摩擦力等于该值，其他动摩擦规律不能由这些数据唯一确定。')

def q4():
    m,B,l,R,a,v0=.1,.5,.2,.5,2.,2.;k=B*B*l*l/R
    motion=solve_ivp(lambda t,y:[y[1],-a],(0,1),[0,v0],dense_output=True,rtol=1e-11,atol=1e-12)
    th=brentq(lambda t:B*l*motion.sol(t)[1]/R-.2,0,1)
    x,v=motion.sol(th);F=k*v-m*a
    close(th,.5);close(x,.75);close(F,-.18)
    checks=[dict(half_current_time=th,position=float(x),force=float(F))]
    for T in (.2,.5,1.):
        power=lambda t:(k*motion.sol(t)[1]-m*a)*motion.sol(t)[1]
        W=quad(power,0,T)[0];Q=quad(lambda t:(B*l*motion.sol(t)[1]/R)**2*R,0,T)[0]
        dK=m/2*(motion.sol(T)[1]**2-v0**2)
        close(W,Q+dK)
        close(W,k*(v0*v0*T-v0*a*T*T+a*a*T**3/3)-m*a*(v0*T-a*T*T/2))
        checks.append(dict(time=T,external_work=W,joule_heat=Q,kinetic_change=float(dK)))
    close(checks[-1]['external_work'],-13/75)
    natural=solve_ivp(lambda t,y:[y[1],-k/m*y[1]],(0,5*np.log(2)),[0,v0],rtol=1e-11,atol=1e-12)
    close(natural.y[1,-1],1.)
    save(4,'运动微分方程、实际外力功率积分及独立焦耳热积分，明确T的合法范围',checks)

def q5():
    fixed=[]
    for q in (1.,-.3):
        # B(t)=1-t/3，E_cw=-B'/2，切向动力学直接积分。
        sol=solve_ivp(lambda t,y:[q/6],(0,3),[.7],rtol=1e-11,atol=1e-12)
        close(sol.y[0,-1],.7+q/2)
        # 上式测试B从1到0。主稿用B从0增加到1，相反号。
        inc=solve_ivp(lambda t,y:[-q/6],(0,3),[.7],rtol=1e-11,atol=1e-12)
        close(inc.y[0,-1],.7-q/2)
        fixed.append(dict(q=q,field_decrease_speed=float(sol.y[0,-1]),field_increase_speed=float(inc.y[0,-1])))
    slow=[]
    for q in (1.,-.3):
        a=experiment(q,160);b=experiment(q,480)
        assert abs(b['final_signed_speed']-b['adiabatic_prediction'])<3e-7
        assert abs(b['final_signed_speed']-b['adiabatic_prediction'])<abs(a['final_signed_speed']-a['adiabatic_prediction'])
        slow.extend([a,b])
    crossing=experiment(-1.,160)
    save(5,'固定环感应场动力学与完整三维约束ODE、约束力功率积分和慢极限收敛',dict(fixed_ring=fixed,slow_flip=slow,outside_adiabatic_branch=crossing),
         '电荷为负且相对转速过零时不以绝热平均式判定答案；全ODE显示该支不同，正式解析已明确适用条件。')

def q6():
    c=330.;v=66.;T=24.;omega=2*np.pi/T;r=v/omega;f0=16/15
    def freq(t,b,azimuth):
        psi=omega*t-5*np.pi/12-azimuth
        D=np.sqrt(r*r+b*b-2*r*b*np.cos(psi))
        u=-v*b*np.sin(psi)/D
        return f0/(1-u/c)
    extrema=[]
    for label,b,az,peak_range,min_range,peak,minn in (
        ('B',np.sqrt(2)*r,0,(0,4),(6,10),2,8),
        ('A',r/np.sqrt(2),2*np.pi/3,(8,12),(14,18),10,16)):
        tp=minimize_scalar(lambda t:-freq(t,b,az),bounds=peak_range,method='bounded').x
        tm=minimize_scalar(lambda t:freq(t,b,az),bounds=min_range,method='bounded').x
        close(tp,peak,rtol=1e-6);close(tm,minn,rtol=1e-6)
        extrema.append(dict(receiver=label,maximum_time=float(tp),minimum_time=float(tm),maximum_khz=float(freq(tp,b,az)),minimum_khz=float(freq(tm,b,az))))
    fm,fn=extrema[0]['maximum_khz'],extrema[0]['minimum_khz']
    recovered_f0=2*fm*fn/(fm+fn);recovered_v=c*(fm-fn)/(fm+fn)
    close(recovered_f0,f0);close(recovered_v,v)
    bB=r/np.cos(np.pi*(8-2)/T);bA=r*np.cos(np.pi*(16-10)/T)
    A=np.array([bA*np.cos(2*np.pi/3),bA*np.sin(2*np.pi/3)]);B=np.array([bB,0.])
    dist=np.linalg.norm(A-B);close(dist,r*np.sqrt(3.5))
    # 若8s为真实接收时差，按各峰传播时长独立校正发射相位。
    dA=r/np.sqrt(2);dB=r;angle=omega*(8-(dA-dB)/c)
    corrected=np.linalg.norm(np.array([bA*np.cos(angle),bA*np.sin(angle)])-B)
    save(6,'按位置直接计算视线速度并数值寻极值，由极值频率独立反演参数',
         dict(extrema=extrema,radius=r,distance=dist,finite_delay_angle_deg=float(np.degrees(angle)),finite_delay_distance=float(corrected)),
         '主结果依题设忽略绝对传播延迟，不能把传播延迟修正分支与主读图结果混合。')

def q7():
    # 实际旋转透镜的面交点，再在其局部方向作薄透镜弯折；不预先代入解析s。
    def trace(s,d,f1,f2,theta=1e-7):
        e=np.array([np.cos(theta),np.sin(theta)]);n=np.array([-np.sin(theta),np.cos(theta)])
        center1=-s*e;point=np.array([-s/np.cos(theta),0.])
        y1=np.dot(point-center1,n)
        angle1=-theta-y1/f1
        y2=y1+d*np.tan(angle1)
        angle2=angle1-y2/f2
        return (angle2+theta)/theta,y1,y2
    checks=[]
    for d in (.4,.8,1.,1.5,2.8):
        f=1.;root=brentq(lambda s:trace(s,d,f,f)[0],-20,20)
        close(root,d/(2-d),rtol=2e-9)
        close(trace(root,d,f,f)[0],0,atol=2e-9)
        checks.append(dict(d=d,pivot_from_left_lens=root,right_focus_distance=abs(root-1),left_focus_distance=abs(root+1)))
    close(trace(0,2,1,1)[0],2,rtol=1e-9)
    close(trace(7,2,1,1)[0],2,rtol=2e-9)
    for f1,f2,d in ((1.,1.7,.8),(.7,1.2,1.8),(2.,.5,.2),(.2,.3,.1)):
        root=brentq(lambda s:trace(s,d,f1,f2)[0],-20,20)
        close(root,d*f1/(f1+f2-d),rtol=2e-9)
        checks.append(dict(f1=f1,f2=f2,d=d,pivot=root))
    save(7,'旋转透镜面的几何交点与两次独立光线弯折求根，验证正负位置和退化分支',checks,
         '先求镜心距离，再明确右侧、左侧轴上焦点；距离取绝对值，且平行出射不要求同线。')

def q8():
    # 无量纲c=a=1，以速度微分方程而不是双曲函数作为ODE输入。
    b=.6;expected=np.log((1+b)/(1-b))
    def rhs(tau,y):
        V,t,x=y;gamma=1/np.sqrt(1-V*V)
        return [1-V*V,gamma,V*gamma]
    sol=solve_ivp(rhs,(0,2),[0.,0.,0.],dense_output=True,rtol=2e-12,atol=2e-13,max_step=.008)
    hit=brentq(lambda tau:sol.sol(tau)[2]-b*sol.sol(tau)[1],.01,1.8,xtol=1e-12)
    V,t,x=sol.sol(hit);close(hit,expected,rtol=2e-9);close(t,15/8);close(x,9/8);close(V,15/17)
    catch_time=float(t)
    def local(tau):
        V,t,x=sol.sol(tau);gamma=1/np.sqrt(1-V*V)
        missile_time=(t-V*x)/(1-V*b)
        separation=gamma*((b*missile_time-x)-V*(missile_time-t))
        u=(b-V)/(1-b*V)
        return separation,u
    maximum=minimize_scalar(lambda tau:-local(tau)[0],bounds=(0,hit),method='bounded',options={'xatol':1e-12})
    close(maximum.x,np.arctanh(b),rtol=2e-7);close(-maximum.fun,.25)
    close(local(hit)[1],-b)
    for tau in (.2,.5,.9,1.2,1.6,1.8):
        step=1e-5;derivative=(local(tau+step)[0]-local(tau-step)[0])/(2*step)
        separation,u=local(tau);close(derivative,(1+separation)*u,rtol=2e-7)
    assert -1<local(1.8)[0]<0
    stop=1.;gap,u=local(stop);remaining=gap/(-u)
    V,t,x=sol.sol(stop)
    lab_after=(b*t-x)/(V-b)
    proper_after=lab_after*np.sqrt(1-V*V)
    close(remaining,proper_after)
    save(8,'从固有加速度速度ODE积分世界线、求相交事件；洛伦兹同时面重算距离和停止加速分支',
         dict(catch_proper_time=hit,catch_lab_time=catch_time,catch_position=9/8,
              maximum_separation_time=float(maximum.x),maximum_separation=float(-maximum.fun),
              coasting_remaining_proper_time=remaining),
         'a指固有加速度；加速系坐标距离对原点时钟的导数不是异地局部速度。')

def main():
    DEST.mkdir(exist_ok=True)
    for test in (q1,q2,q3,q4,q5,q6,q7,q8):test()

if __name__=='__main__':main()
