"""Check actual PDF vectors, face geometry, simultaneity slopes and curves."""
from pathlib import Path
import hashlib,json,math
import fitz
ROOT=Path(__file__).resolve().parents[1]
NAMES=['question-08','frames-08','pressure-08','events-08','fourforce-08','limits-08']
CM=72/2.54
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def colored(ds,ch):
    return [d for d in ds if d['color'] and d['color'][ch]>.4 and
            d['color'][ch]>max(d['color'][i] for i in range(3) if i!=ch)+.2]
def dots(ds):
    return [(d['rect'].tl+d['rect'].br)*.5 for d in ds if
        d['type']=='f' and len(d['items'])==4 and all(q[0]=='c' for q in d['items'])]
def line(d):
    assert len(d['items'])==1 and d['items'][0][0]=='l'
    return d['items'][0][1:]
def main():
    checks=[]
    with fitz.open(ROOT/'figures/frames-08.pdf') as doc:
        ds=doc[0].get_drawings()
        tops=[d for d in ds if d['type']=='fs' and len(d['items'])==4
            and d['fill'] and d['fill'][2]>.99 and .89<d['fill'][0]<.91]
        assert len(tops)==2
        lengths=[];errors=[]
        for top,expected in zip(sorted(tops,key=lambda d:d['rect'].x0),[4.,5.]):
            a,b=top['items'][0][1:];lengths.append((b.x-a.x)/CM)
            errors.append(abs(lengths[-1]-expected))
            # Last top edge runs from back-left to front-left.
            back,front=top['items'][-1][1:]
            errors += [abs((front.x-back.x)/CM-.45*1.5),
                       abs((front.y-back.y)/CM-.32*1.5)]
        # TeX coordinate rounding + pt-to-PDF-bp conversion is <0.001 mm.
        assert max(errors)<1e-4,errors
        assert abs(lengths[0]/lengths[1]-.8)<1e-5
        checks.append(dict(figure='frames-08',x_lengths=lengths,
            water_boat_length_ratio=lengths[0]/lengths[1],
            maximum_projection_error_cm=max(errors),actual_three_dimensional_faces=True))
    with fitz.open(ROOT/'figures/pressure-08.pdf') as doc:
        ds=doc[0].get_drawings();points=sorted(dots(ds),key=lambda p:p.y)
        assert len(points)==2
        top,bottom=points
        red=next(d for d in colored(ds,0) if d['type']=='s')
        blue=[d for d in colored(ds,2) if d['type']=='s']
        up=min(blue,key=lambda d:d['rect'].x0)
        R0,R1=line(red);B0,B1=line(up)
        error=max(abs(R0.x-top.x),abs(R0.y-top.y),abs(B0.x-bottom.x),abs(B0.y-bottom.y))
        assert error<2e-4
        assert R1.y>R0.y and B1.y<B0.y
        assert abs((bottom.y-top.y)/CM-1.5)<1e-4
        assert B1.y>R1.y  # opposite arrows do not overlap inside the body
        checks.append(dict(figure='pressure-08',force_application_point_error_pdf_pt=error,
            top_force_down=True,bottom_force_up=True,opposite_arrows_do_not_overlap=True))
    with fitz.open(ROOT/'figures/events-08.pdf') as doc:
        ds=doc[0].get_drawings();points=sorted(dots(ds),key=lambda p:p.y,reverse=True)
        assert len(points)==2
        P,Q=points
        slope=(Q.x-P.x)/(P.y-Q.y)
        assert abs(slope-.6)<1e-5
        red=next(d for d in colored(ds,0) if d['type']=='s')
        green=next(d for d in colored(ds,1) if d['type']=='s')
        ra,rb=line(red);ga,gb=line(green)
        assert abs(ra.y-rb.y)<1e-5
        assert abs((ga.y-gb.y)/(gb.x-ga.x)-.6)<1e-5
        checks.append(dict(figure='events-08',center_worldline_beta=slope,
            water_simultaneous_horizontal=True,boat_simultaneous_ct_over_x=.6))
    with fitz.open(ROOT/'figures/limits-08.pdf') as doc:
        ds=doc[0].get_drawings()
        axes=sorted([d for d in ds if d['type']=='s' and d['color']==(0.,0.,0.)
            and len(d['items'])==1 and d['rect'].width>100 and d['rect'].height<1e-4],
            key=lambda d:d['rect'].x0)
        assert len(axes)==2
        curves=[d for d in ds if d['type']=='s' and len(d['items'])==80]
        assert len(curves)==3
        errors=[]
        for curve in curves:
            ps=[curve['items'][0][1]]+[x[2] for x in curve['items']]
            axis=min(axes,key=lambda d:abs(d['rect'].x0-ps[0].x))
            ybase=axis['rect'].y0;yscale=ybase-ps[0].y
            xleft,xright=ps[0].x,ps[-1].x
            iswater=axis==axes[0];isblue=curve['color'][2]>.4
            for point in ps:
                beta=.9*(point.x-xleft)/(xright-xleft)
                val=(ybase-point.y)/yscale
                expected=math.sqrt(1-beta**2) if isblue else (
                    1/math.sqrt(1-beta**2) if iswater else 1/(1-beta**2))
                errors.append(abs(val-expected))
        assert max(errors)<8e-5,max(errors)
        checks.append(dict(figure='limits-08',samples=243,
            maximum_actual_force_curve_error=max(errors),finite_beta_max=.9))
    result=dict(question=8,passed=True,scope='actual vector geometry; actual human visual record required separately',
        checks=checks,figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in NAMES})
    (ROOT/'build/projected-geometry-q08.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
