"""椭圆接触几何、牛顿矩阵、ODE到达事件及焦点轨迹独立核验。"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp,quad
from scipy.optimize import minimize_scalar
ROOT=Path(__file__).resolve().parents[1]

def main():
    t=sp.symbols('theta',real=True)
    h=sp.sqrt(sp.cos(t)**2+sp.Rational(2,3)*sp.sin(t)**2)
    hp=sp.diff(h,t);hpp=sp.diff(hp,t);j=sp.Rational(5,12);c=1/sp.sqrt(3)
    q=sp.pi/3
    geom=[sp.simplify(v.subs(t,q)) for v in [h,hp,hpp,h+hpp]]
    assert geom==[sp.sqrt(3)/2,-sp.Rational(1,6),5*sp.sqrt(3)/54,16*sp.sqrt(3)/27]
    assert sp.trigsimp(h+hpp-sp.Rational(2,3)/h**3)==0
    expressions={};values={}
    f_h=sp.lambdify(t,[h,hp,hpp],'numpy')
    for kind in ['smooth','rolling']:
        D=j+hp**2+(h**2 if kind=='rolling' else 0)
        w2=2*(1-h)/D
        alpha=-(hp+sp.diff(D,t)*w2/2)/D
        vx=(c*sp.cos(t)+(h if kind=='rolling' else 0))
        vy=hp-c*sp.sin(t)
        ax=sp.diff(vx,t)*w2+vx*alpha
        ay=sp.diff(vy,t)*w2+vy*alpha
        agx=(hp*w2+h*alpha) if kind=='rolling' else sp.Integer(0)
        agy=hpp*w2+hp*alpha
        fr=agx;normal=1+agy
        row={k:sp.simplify(v.subs(t,q)) for k,v in dict(w2=w2,alpha=alpha,
                 vx_over_w=vx,vy_over_w=vy,ax=ax,ay=ay,agx=agx,agy=agy,friction=fr,normal=normal).items()}
        expressions[kind]={k:str(v) for k,v in row.items()}
        values[kind]={k:float(v) for k,v in row.items()}
        assert sp.simplify(row['normal']-1-row['agy'])==0
        assert sp.simplify(j*row['alpha']+geom[1]*row['normal']+geom[0]*row['friction'])==0
        # 动力学另解alpha、质心加速度、接触力，不调用能量求导的alpha。
        def newton(theta,w):
            height,dh,ddh=map(float,f_h(theta))
            if kind=='smooth':
                mat=np.array([[-dh,1,0],[0,-1,1],[float(j),0,dh]],float)
                out=np.linalg.solve(mat,[ddh*w*w,1,0])
                return out[0]
            mat=np.array([[-height,1,0,0,0],[-dh,0,1,0,0],
                          [0,-1,0,1,0],[0,0,-1,0,1],[float(j),0,0,height,dh]],float)
            return np.linalg.solve(mat,[dh*w*w,ddh*w*w,0,1,0])[0]
        assert abs(newton(float(q),math.sqrt(values[kind]['w2']))-values[kind]['alpha'])<1e-12
        def ode(time,state):return [state[1],newton(state[0],state[1])]
        def stop(time,state):return state[0]-float(q)
        stop.terminal=True;stop.direction=1
        solution=solve_ivp(ode,[0,80],[1e-5,0],events=stop,method='DOP853',rtol=2e-12,atol=2e-13,max_step=.15)
        assert len(solution.t_events[0])==1
        reached=solution.y_events[0][0];numerical_w2=reached[1]**2
        assert abs(numerical_w2-values[kind]['w2'])<1e-9
        values[kind]['ode_w2']=numerical_w2
        values[kind]['ode_relative_error']=abs(numerical_w2-values[kind]['w2'])/values[kind]['w2']
        # 另一条几何路线：直接在旋转后的参数椭圆上寻找最低材料点。
        def support(theta):
            y=lambda psi: math.cos(psi)*math.cos(theta)-math.sqrt(2/3)*math.sin(psi)*math.sin(theta)
            opt=minimize_scalar(y,bounds=[math.pi/2,3*math.pi/2],method='bounded',options={'xatol':1e-14})
            psi=opt.x
            px=math.sqrt(2/3)*math.sin(psi)*math.cos(theta)+math.cos(psi)*math.sin(theta)
            return -opt.fun,px
        height,px=support(float(q))
        assert abs(height-float(geom[0]))<1e-12 and abs(px-float(geom[1]))<2e-8
        def focus(theta):
            height=support(theta)[0]
            X=quad(lambda z:support(z)[0],0,theta,epsabs=1e-11)[0] if kind=='rolling' else 0.
            return np.array([X+float(c)*math.sin(theta),height+float(c)*math.cos(theta)])
        w=math.sqrt(values[kind]['w2']);acc=values[kind]['alpha'];dt=2e-4
        theta=float(q)
        p0=focus(theta);pm=focus(theta-w*dt+.5*acc*dt*dt);pp=focus(theta+w*dt+.5*acc*dt*dt)
        numerical_v=(pp-pm)/(2*dt);numerical_a=(pp-2*p0+pm)/(dt*dt)
        wanted_v=np.array([values[kind]['vx_over_w'],values[kind]['vy_over_w']])*w
        wanted_a=np.array([values[kind]['ax'],values[kind]['ay']])
        assert np.linalg.norm(numerical_v-wanted_v)<2e-7
        assert np.linalg.norm(numerical_a-wanted_a)<3e-6
        values[kind]['cartesian_focus_v']=numerical_v.tolist();values[kind]['cartesian_focus_a']=numerical_a.tolist()
        if kind=='rolling':
            ff=sp.lambdify(t,fr,'numpy');nn=sp.lambdify(t,normal,'numpy')
            ratio=lambda z:abs(float(ff(z)))/float(nn(z))
            result=minimize_scalar(lambda z:-ratio(z),bounds=[1e-6,float(q)],method='bounded',options={'xatol':1e-12})
            theta_max=result.x;mu=max(-result.fun,ratio(float(q)))
            table=[dict(theta_deg=d,mu_required=ratio(math.radians(d)),normal_over_mg=float(nn(math.radians(d)))) for d in [0,15,30,45,60]]
            values[kind]['mu_at_60']=ratio(float(q));values[kind]['mu_max_0_to_60']=mu
            values[kind]['mu_max_theta_deg']=math.degrees(theta_max);values[kind]['friction_table']=table
            assert all(row['normal_over_mg']>0 for row in table)
    # 任意均匀椭圆的惯量由面积坐标积分核验，并检查圆形退化。
    r,p=sp.symbols('r phi',real=True);A,B=sp.symbols('a b',positive=True)
    area_moment=sp.integrate(sp.integrate((A*A*sp.cos(p)**2+B*B*sp.sin(p)**2)*r**3,(r,0,1)),(p,0,2*sp.pi))/sp.pi
    assert sp.simplify(area_moment-(A*A+B*B)/4)==0
    for beta in [.4,.6,.8,.99,1.]:
        height=math.sqrt(math.cos(float(q))**2+beta*beta*math.sin(float(q))**2)
        assert height<=1+1e-14
    initial_omega_critical=math.sqrt(3.)
    assert abs(1+(2/3-1)*initial_omega_critical**2)<1e-12
    paths=['scripts/verify_question_01.py'];draft=ROOT/'drafts/question-01.md'
    complete=draft.exists() and '<!-- question-complete -->' in draft.read_text()
    if draft.exists():paths.append('drafts/question-01.md')
    if (ROOT/'figures/题01_图稿源文件.tex').exists():paths.append('figures/题01_图稿源文件.tex')
    result=dict(question=1,verified_math=True,document_complete=complete,
                normalized_units='a=g=m=1; theta clockwise; x right and y up',geometry=list(map(str,geom)),
                expressions=expressions,values=values,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths})
    (ROOT/'build').mkdir(exist_ok=True)
    out=ROOT/'build'/('verification-q01.json' if complete else 'verification-q01-preliminary.json')
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
