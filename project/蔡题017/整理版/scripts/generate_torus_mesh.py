"""Generate deterministic TikZ vector tiles from the actual torus embedding.

Construction artifact only, not visual acceptance. Orthographic camera is
(0,-sqrt(3)/2,1/2); screen axes are x and (0,1/2,sqrt(3)/2).
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
def main():
    major,minor=2.4,.8
    np_,nt=64,32
    camera=np.array([0,-math.sqrt(3)/2,.5])
    up=np.array([0,.5,math.sqrt(3)/2])
    light=np.array([-.3,-.45,.84]);light/=np.linalg.norm(light)
    def point(t,a):
        s=major-minor*math.cos(t)
        return np.array([s*math.cos(a),s*math.sin(a),minor*math.sin(t)])
    polygons=[]
    for j in range(nt):
        low=j*2*math.pi/nt;high=(j+1)*2*math.pi/nt
        for i in range(np_):
            left=i*2*math.pi/np_;right=(i+1)*2*math.pi/np_
            vertices=[point(low,left),point(high,left),point(high,right),point(low,right)]
            middle=(low+high)/2;az=(left+right)/2
            n=np.array([-math.cos(middle)*math.cos(az),-math.cos(middle)*math.sin(az),math.sin(middle)])
            tone=round(12+30*(1-float(n@light))/2)
            depth=float(np.mean(vertices,axis=0)@camera)
            path='--'.join(f'({v[0]:.6f},{float(v@up):.6f})' for v in vertices)+'--cycle'
            polygons.append((depth,math.degrees(middle),tone,path))
            for v in vertices:
                assert abs((math.hypot(v[0],v[1])-major)**2+v[2]**2-minor**2)<1e-13
    polygons.sort(key=lambda a:a[0])
    assert len(polygons)==2048
    outputs={}
    for name,band in [('torus-base-03.tex',False),('torus-cap-03.tex',True)]:
        rows=['% Automatically generated vector mesh; parameters and camera in build/torus-mesh-q03.json.']
        for _,theta,tone,path in polygons:
            color='green!65!black' if band and 45<theta<90 else 'blue'
            percentage=max(20,tone+15) if band and 45<theta<90 else tone
            rows.append(r'\path[fill='+color+f'!{percentage}!white,draw='+color+f'!{percentage}!white,line width=.12pt] '+path+';')
        out=ROOT/'figures'/name;out.write_text('\n'.join(rows)+'\n')
        outputs[name]=hashlib.sha256(out.read_bytes()).hexdigest()
    data=dict(major_radius=major,minor_radius=minor,ratio=major/minor,
              phi_intervals=np_,theta_intervals=nt,vector_tiles=len(polygons),
              camera=camera.tolist(),screen_vertical=up.tolist(),
              inner_upper_band_theta_degrees=[45,90],
              generated_mesh_sha256=outputs,
              generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              actual_visual_reviewed=False)
    (ROOT/'build/torus-mesh-q03.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))
if __name__=='__main__':main()
