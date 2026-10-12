"""对收敛镜像能量逐点求和，机械生成图2-4；同时保存曲线数值。"""
from pathlib import Path
import json, math
ROOT=Path(__file__).resolve().parents[1]
def main():
    s3=1.051799790264645;h=.30
    rows=[];commands=[]
    for chi,color,style in [(.5,'blue!65!black','solid'),(1.,'orange!85!black','dashed'),(1.2,'red!65!black','densely dotted')]:
        points=[]
        for i in range(121):
            u=-.6+i*.01;x=h*u
            electric=sum(x*x/((2*j+1)*((2*j+1)**2-x*x)) for j in range(4000))
            gravitational=-math.expm1(.5*math.log1p(-u*u))
            value=gravitational-chi*electric/(2*h*h*s3)
            points.append(f'({u:.6f},{value:.10f})')
            rows.append(dict(u=u,x_over_l=x,chi=chi,U_over_mgh=value))
        commands.append('\\draw['+color+',very thick,'+style+'] plot coordinates {'+' '.join(points)+'};')
    (ROOT/'figures/effective-02-coordinates.tex').write_text('\n'.join(commands)+'\n')
    (ROOT/'build/curve-q02.json').write_text(json.dumps(dict(h_over_l=h,S3=s3,points=rows),indent=2)+'\n')
    print('potential range',min(r['U_over_mgh'] for r in rows),max(r['U_over_mgh'] for r in rows))
if __name__=='__main__':main()
