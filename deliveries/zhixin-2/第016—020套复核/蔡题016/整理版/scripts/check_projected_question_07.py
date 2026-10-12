"""Actual Q7 vector figures: perpendiculars, reflected rays and finite-sum curve."""
from pathlib import Path
import hashlib, json, math
import fitz

ROOT=Path(__file__).resolve().parents[1]
NAMES=['question-07','geometry-07','angles-07','path-07','phasors-07','peak-07']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def line(draw):assert len(draw['items'])==1 and draw['items'][0][0]=='l';return draw['items'][0][1:]
def colored(ds,ch):
    return [d for d in ds if d['color'] and d['color'][ch]>.4
        and d['color'][ch]>max(d['color'][i] for i in range(3) if i!=ch)+.2]
def dots(ds):
    return [(d['rect'].tl+d['rect'].br)*.5 for d in ds
        if d['type']=='f' and len(d['items'])==4 and all(q[0]=='c' for q in d['items'])]
def unit(a,b):
    x,y=b.x-a.x,a.y-b.y;L=math.hypot(x,y);return x/L,y/L
def main():
    checks=[]
    with fitz.open(ROOT/'figures/geometry-07.pdf') as doc:
        ds=doc[0].get_drawings();cs=dots(ds);assert len(cs)==3
        top=sorted(cs,key=lambda p:p.y)[:2];P,Q=sorted(top,key=lambda p:p.x)
        H=max(cs,key=lambda p:p.y)
        scale=(Q.x-P.x)/4
        hx=(H.x-P.x)/scale;hz=(P.y-H.y)/scale
        expected=(4*math.cos(math.radians(25))**2,
                  -4*math.sin(math.radians(25))*math.cos(math.radians(25)))
        err=max(abs(hx-expected[0]),abs(hz-expected[1]))
        assert err<3e-5
        dot=((H.x-P.x)*(Q.x-H.x)+(H.y-P.y)*(Q.y-H.y))/scale**2
        assert abs(dot)<7e-5
        assert abs(math.hypot(Q.x-H.x,Q.y-H.y)/scale-4*math.sin(math.radians(25)))<3e-5
        checks.append(dict(figure='geometry-07',orthogonal_foot_error_normalized=err,
            perpendicular_dot_normalized=dot,layer_normal_spacing=math.hypot(Q.x-H.x,Q.y-H.y)/scale))
    with fitz.open(ROOT/'figures/angles-07.pdf') as doc:
        ds=doc[0].get_drawings();greens=[d for d in colored(ds,1) if d['type']=='s']
        assert len(greens)==2
        incoming=unit(*line(greens[0]));outgoing=unit(*line(greens[1]))
        mirror=next(d for d in colored(ds,2) if d['type']=='s')
        tangent=unit(*line(mirror));normal=(-tangent[1],tangent[0])
        projection=sum(incoming[i]*normal[i] for i in range(2))
        expected=tuple(incoming[i]-2*projection*normal[i] for i in range(2))
        err=math.hypot(*(outgoing[i]-expected[i] for i in range(2)))
        assert err<2e-5
        angle=math.degrees(math.atan2(outgoing[0],outgoing[1]))
        assert abs(angle-50)<.002
        checks.append(dict(figure='angles-07',actual_vector_reflection_error=err,
                           outgoing_angle_to_cut_normal_deg=angle))
    with fitz.open(ROOT/'figures/path-07.pdf') as doc:
        ds=doc[0].get_drawings();cs=dots(ds);assert len(cs)==3
        P,Q=sorted(sorted(cs,key=lambda p:p.y,reverse=True)[:2],key=lambda p:p.x)
        K=min(cs,key=lambda p:p.y)
        greens=[d for d in colored(ds,1) if d['type']=='s']
        diagonals=[d for d in greens if abs(line(d)[1].x-line(d)[0].x)>1]
        ray=max(diagonals,key=lambda d:math.hypot(line(d)[1].x-line(d)[0].x,line(d)[1].y-line(d)[0].y))
        outgoing=unit(*line(ray))
        scale=(Q.x-P.x)/5
        pk=((K.x-P.x)/scale,(P.y-K.y)/scale)
        expected=(5*outgoing[0]**2,5*outgoing[0]*outgoing[1])
        err=math.hypot(pk[0]-expected[0],pk[1]-expected[1])
        dot=(Q.x-K.x)*(K.x-P.x)+(Q.y-K.y)*(K.y-P.y)
        assert err<5e-5 and abs(dot/scale**2)<2e-4
        checks.append(dict(figure='path-07',actual_wavefront_projection_error_normalized=err,
            outgoing_perpendicular_dot_normalized=dot/scale**2,
            actual_PK_over_period=math.hypot(*pk)/5))
    with fitz.open(ROOT/'figures/peak-07.pdf') as doc:
        ds=doc[0].get_drawings()
        curve=next(d for d in colored(ds,2) if len(d['items'])==200)
        points=[curve['items'][0][1]]+[item[2] for item in curve['items']]
        left,right=points[0].x,points[-1].x
        baseline=max(p.y for p in points);peak=min(p.y for p in points)
        errors=[];zero_values=[]
        for j,p in enumerate(points):
            u=-.25+.5*(p.x-left)/(right-left)
            intensity=(baseline-p.y)/(baseline-peak)
            re=sum(math.cos(2*math.pi*u*k) for k in range(8))
            im=sum(math.sin(2*math.pi*u*k) for k in range(8))
            expected=(re*re+im*im)/64
            errors.append(abs(intensity-expected))
            if j in [0,50,150,200]:zero_values.append(intensity)
        assert max(errors)<3e-5 and max(map(abs,zero_values))<1e-7
        assert abs((baseline-points[100].y)/(baseline-peak)-1)<1e-8
        checks.append(dict(figure='peak-07',samples=201,
            maximum_actual_vector_intensity_error=max(errors),zeros=zero_values,center_peak=1))
    report=dict(question=7,passed=True,scope='actual vector geometry; visual review separately required',
        checks=checks,figures_sha256={name:sha(ROOT/f'figures/{name}.pdf') for name in NAMES})
    (ROOT/'build/projected-geometry-q07.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
