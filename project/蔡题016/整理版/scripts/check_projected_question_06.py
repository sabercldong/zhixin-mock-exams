"""Read actual Q6 vector PDFs; check joins, arrow signs and equation-drawn curves."""
from pathlib import Path
import hashlib
import json
import math
import fitz

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['question-06','exchange-06','impulse-06','energy-06','count-06','crossings-06']

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def points(path):
    items = path['items']
    assert all(item[0]=='l' for item in items)
    return [items[0][1]]+[item[2] for item in items]

def color_paths(drawings, channel):
    return [d for d in drawings if d['color'] and d['color'][channel]>.4
            and d['color'][channel]>max(d['color'][i] for i in range(3) if i!=channel)+.2]

def main():
    results = []
    with fitz.open(ROOT/'figures/question-06.pdf') as doc:
        p = doc[0]; drawings = p.get_drawings()
        blocks = [d['rect'] for d in drawings if d['type']=='fs' and len(d['items'])==4
                  and all(q[0]=='l' and (abs(q[1].x-q[2].x)<.001 or
                                        abs(q[1].y-q[2].y)<.001) for q in d['items'])]
        assert len(blocks)==3
        blocks.sort(key=lambda r:r.x0)
        table = drawings[0]['items'][0]
        assert table[0]=='l'
        ground_y = table[1].y
        maximum_join = max(abs(b.y1-ground_y) for b in blocks)
        assert maximum_join<.001
        assert blocks[0].x1<blocks[1].x0<blocks[1].x1<blocks[2].x0
        wall_x = table[2].x
        assert blocks[2].x1<wall_x
        for channel in [0,2]:
            line = next(d for d in color_paths(drawings,channel) if d['type']=='s')
            a,b = line['items'][0][1:]
            assert b.x>a.x and abs(b.y-a.y)<.001
        results.append(dict(figure='question-06',table_joins_max_pdf_points=maximum_join,
                            order='A<B<C<wall',initial_arrows='both right'))
    with fitz.open(ROOT/'figures/energy-06.pdf') as doc:
        drawings = doc[0].get_drawings()
        blue = next(d for d in color_paths(drawings,2) if len(d['items'])>50)
        red = next(d for d in color_paths(drawings,0) if len(d['items'])>50)
        bp,rp = points(blue),points(red)
        x0,y0 = rp[0]
        sx = bp[-1].x-bp[0].x
        sy = y0-bp[0].y
        errors=[]
        for curve,formula in [(bp,lambda X:1/X**2),(rp,lambda X:1-1/X**2)]:
            for px,py in curve:
                X=1+(px-x0)/sx
                value=(y0-py)/sy
                errors.append(abs(value-formula(X)))
        assert max(errors)<3e-5
        results.append(dict(figure='energy-06',actual_vector_curve_samples=len(errors),
                            maximum_normalized_equation_error=max(errors),
                            final_light_energy_fraction=(y0-bp[-1].y)/sy,
                            final_A_energy_fraction=(y0-rp[-1].y)/sy))
    with fitz.open(ROOT/'figures/crossings-06.pdf') as doc:
        drawings=doc[0].get_drawings()
        blue=next(d for d in color_paths(drawings,2) if len(d['items'])==3)
        red=next(d for d in color_paths(drawings,0) if len(d['items'])==5)
        bp,rp=points(blue),points(red)
        sx=(bp[-1].x-bp[0].x)/2
        ybase=max(q.y for q in bp+rp)
        sy=ybase-min(q.y for q in bp+rp)
        xbase=bp[0].x
        def fold(q):return 1-abs(1-q%2)
        errors=[]
        for path,speed,phase in [(bp,1,.173),(rp,2,.617)]:
            for px,py in path:
                s=(px-xbase)/sx;y=(ybase-py)/sy
                errors.append(abs(y-fold(speed*s+phase)))
        assert max(errors)<3e-5
        solid=[];hollow=[]
        for d in drawings:
            if len(d['items'])==4 and all(q[0]=='c' for q in d['items']):
                c=d['rect'].tl+(d['rect'].br-d['rect'].tl)*.5
                if d['type']=='f':solid.append(c)
                elif d['type']=='fs':hollow.append(c)
        assert len(solid)==4 and len(hollow)==6,(len(solid),len(hollow))
        interior=[]
        for c in solid:
            s=(c.x-xbase)/sx;y=(ybase-c.y)/sy
            error=max(abs(y-fold(s+.173)),abs(y-fold(2*s+.617)))
            assert error<3e-5 and 0<s<2 and 0<y<1
            interior.append(dict(s=s,y=y,equation_error=error))
        endpoint=[(ybase-c.y)/sy for c in hollow]
        assert sum(abs(y)<1e-5 for y in endpoint)==3
        assert sum(abs(y-1)<1e-5 for y in endpoint)==3
        results.append(dict(figure='crossings-06',maximum_folded_path_error=max(errors),
                            actual_interior_crossings=interior,
                            A_endpoint_events=3,wall_endpoint_events=3))
    report=dict(question=6,passed=True,scope='actual vector geometry only; visual review separately required',
                checks=results,figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in NAMES})
    (ROOT/'build/projected-geometry-q06.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
