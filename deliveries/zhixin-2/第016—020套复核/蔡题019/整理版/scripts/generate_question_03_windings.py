"""投影真实环形磁芯上的连续螺旋绕线，按表面朝向区分可见和背侧。"""
from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parents[1]
def main():
    front=[];back=[];ends=[];record=[]
    for number,center in [(1,270),(2,180),(3,0)]:
        points=[]
        for i in range(961):
            t=2*math.pi*6*i/960;phi=math.radians(center-15+30*i/960)
            radius=1.34+.25*math.cos(t);z=.25*math.sin(t)
            x=radius*math.cos(phi);y=(radius*math.sin(phi)+z)/math.sqrt(2)
            facing=(-math.sin(phi)*math.cos(t)+math.sin(t))/math.sqrt(2)
            points.append((x,y,facing>=0))
        chunks=[];chunk=[points[0]]
        for previous,point in zip(points,points[1:]):
            if previous[2]!=point[2]:chunks.append((previous[2],chunk+[point]));chunk=[point]
            else:chunk.append(point)
        chunks.append((points[-1][2],chunk))
        for visible,chunk in chunks:
            command='\\draw['+('copper,thick' if visible else 'gray,dashed,thin')+'] plot coordinates {'+' '.join(f'({x:.6f},{y:.6f})' for x,y,_ in chunk)+'};'
            (front if visible else back).append(command)
        first,last=points[0],points[-1]
        ends.extend([f'\\coordinate(C{number}a)at({first[0]:.6f},{first[1]:.6f});',f'\\coordinate(C{number}b)at({last[0]:.6f},{last[1]:.6f});'])
        # 每一匝完整绕截面，六匝连成一条线；仅用示意匝数，不取代符号N_i。
        record.append(dict(winding=number,drawn_turns=6,center_deg=center,points=len(points),start=first[:2],end=last[:2]))
    text='\\newcommand{\\corebackwires}{\n'+'\n'.join(back)+'\n}\n'
    text+='\\newcommand{\\corefrontwires}{\n'+'\n'.join(front)+'\n}\n'+'\n'.join(ends)+'\n'
    (ROOT/'figures/core-03-coordinates.tex').write_text(text)
    (ROOT/'build/winding-q03.json').write_text(json.dumps(dict(projection='x=X,y=(Y+Z)/sqrt(2)',windings=record),indent=2)+'\n')
    print('three continuous six-turn schematic windings projected')
if __name__=='__main__':main()
