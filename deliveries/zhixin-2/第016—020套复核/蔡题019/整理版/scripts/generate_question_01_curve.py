"""用模型正根生成曲线坐标；只机械绘制数值关系，不生成解答文字。"""
from pathlib import Path
import math
ROOT=Path(__file__).resolve().parents[1]
def main():
    points=[]
    for i in range(101):
        z=8*i/100;lo,hi=1,(1+z)**.25
        for _ in range(60):
            mid=(lo+hi)/2
            if mid**4+.4*(mid-1)<1+z:lo=mid
            else:hi=mid
        points.append(f'({z:.6f},{1/((lo+hi)/2):.9f})')
    (ROOT/'figures/radius-01-coordinates.tex').write_text('\\draw[orange!85!black,very thick] plot coordinates {'+' '.join(points)+'};\n')
if __name__=='__main__':main()
