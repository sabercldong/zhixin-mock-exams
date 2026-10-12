"""由原二阶Lorentz方程生成TikZ轨迹，独立核对第一积分。"""
from pathlib import Path
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk
ROOT=Path(__file__).resolve().parents[1]
def orbit(wc,wz,end,name):
    def ode(t,Y):
        phi,rate,z,vz=Y
        return [rate,wc*vz*math.cos(phi),vz,-wc*rate*math.cos(phi)]
    sol=solve_ivp(ode,(0,end),[0,1,0,wz],t_eval=np.linspace(0,end,501),
                  rtol=1e-11,atol=1e-12,max_step=.02)
    phi,rate,z,vz=sol.y
    assert np.max(abs(vz-(wz-wc*np.sin(phi))))<1e-8
    X=np.cos(phi);Y=np.sin(phi)
    dest=ROOT/'figures/data';dest.mkdir(parents=True,exist_ok=True)
    for suffix,ab in [('space',(.95*X+.45*Y,.18*X-.32*Y+.60*z)),('unwrapped',(phi,z))]:
        np.savetxt(dest/f'{name}-{suffix}.dat',np.array(ab).T,fmt='%.10f')
    projected=np.array([.95*X+.45*Y,.18*X-.32*Y+.60*z]).T
    front=np.sin(phi-math.atan2(.45,.95))>=0
    switches=np.r_[0,np.nonzero(front[1:]!=front[:-1])[0]+1,len(phi)]
    color={'winding':'blue','weak':'blue','strong':'green','critical':'red'}[name]
    lines=[]
    for a,b in zip(switches[:-1],switches[1:]):
        points=projected[max(a-1,0):b]
        style=color+',very thick'+('' if front[a] else ',densely dashed')
        lines.append(r'\draw['+style+'] plot coordinates {'+
                     ' '.join(f'({x:.8f},{y:.8f})' for x,y in points)+'};')
    (dest/f'{name}-path.tex').write_text('\n'.join(lines)+'\n')
    return sol
def main():
    orbit(.3,.6,13.3,'winding')
    orbit(.5,0,4*ellipk(.25),'weak')
    orbit(1.5,0,4/1.5*ellipk(4/9),'strong')
    orbit(1,0,5,'critical')
    print('四条轨迹已由二阶运动方程生成；保留空间投影与展开数据。')
if __name__=='__main__':main()
