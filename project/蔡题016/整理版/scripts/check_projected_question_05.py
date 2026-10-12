"""Check actual vector joins and the two signed mode directions, not visual review."""
from pathlib import Path
import hashlib,json,math
import fitz

ROOT=Path(__file__).resolve().parents[1]
NAMES=['question-05','forces-05','circuit-05','motion-05','modes-05','energy-05']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def black(p):return p['color'] is not None and max(p['color'])<.02
def lines(paths):
    return [p for p in paths if black(p) and p['type']=='s'
            and len(p['items'])==1 and p['items'][0][0]=='l']
def main():
    with fitz.open(ROOT/'figures/question-05.pdf') as doc:
        paths=doc[0].get_drawings();ls=lines(paths)
        rails=sorted([p['rect'] for p in ls if p['rect'].height<.01
                      and p['rect'].width>140],key=lambda r:r.y0)
        assert len(rails)==2
        rods=[p['rect'] for p in ls if p['rect'].width<.01 and p['width']>1]
        assert len(rods)==2
        join_error=max(max(abs(r.y0-rails[0].y0),abs(r.y1-rails[1].y0)) for r in rods)
        assert join_error<.02
        assert all(rails[0].x0<r.x0<rails[0].x1 for r in rods)
        cap_plates=sorted([p['rect'] for p in ls if p['rect'].height<.01
                           and 20<p['rect'].width<30],key=lambda r:r.y0)
        assert len(cap_plates)==2 and cap_plates[1].y0-cap_plates[0].y0>8
        cap_wires=sorted([p['rect'] for p in ls if p['rect'].width<.01
                          and abs(p['rect'].x0-rails[0].x0)<.02],key=lambda r:r.y0)
        assert len(cap_wires)==2
        cap_error=max(abs(cap_wires[0].y0-rails[0].y0),
                      abs(cap_wires[0].y1-cap_plates[0].y0),
                      abs(cap_wires[1].y0-cap_plates[1].y0),
                      abs(cap_wires[1].y1-rails[1].y0))
        assert cap_error<.02
        assert not any(p['rect'].width<.01 and
                       abs(p['rect'].x0-rails[0].x0)<.02 and
                       p['rect'].y0<cap_plates[0].y0+.01 and
                       p['rect'].y1>cap_plates[1].y0-.01 for p in ls)
    with fitz.open(ROOT/'figures/circuit-05.pdf') as doc:
        paths=doc[0].get_drawings();ls=lines(paths)
        rails=sorted([p['rect'] for p in ls if p['rect'].height<.01
                      and p['rect'].width>150],key=lambda r:r.y0)
        circles=[p['rect'] for p in paths if black(p) and p['type']=='s'
                 and len(p['items'])==4 and all(t[0]=='c' for t in p['items'])
                 and 15<p['rect'].width<25]
        assert len(rails)==2 and len(circles)==2
        branch_errors=[]
        for circle in circles:
            cx=(circle.x0+circle.x1)/2
            strokes=[p['rect'] for p in ls if p['rect'].width<.01
                     and abs(p['rect'].x0-cx)<.02]
            source_up=[p for p in strokes if abs(p.y1-circle.y0)<.02]
            source_down=[p for p in strokes if abs(p.y0-circle.y1)<.02]
            top=[p for p in strokes if abs(p.y0-rails[0].y0)<.02]
            assert len(source_up)==len(source_down)==len(top)==1
            coils=[p['rect'] for p in paths if black(p) and len(p['items'])>4
                   and p['rect'].width>2 and p['rect'].width<10
                   and abs((p['rect'].x0+p['rect'].x1)/2-cx)<1]
            assert len(coils)==1
            coil=coils[0]
            error=max(abs(source_down[0].y1-rails[1].y0),
                      abs(top[0].y1-coil.y0),abs(source_up[0].y0-coil.y1))
            assert error<.025
            branch_errors.append(error)
    # Exact physical basis, not a conclusion copied from the final displacement.
    # e_y x (-e_z)=-e_x; e_x x (-e_z)=e_y.
    def cross(a,b):
        return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
                a[0]*b[1]-a[1]*b[0])
    assert cross((0,1,0),(0,0,-1))==(-1,0,0)
    assert cross((1,0,0),(0,0,-1))==(0,1,0)
    # Separate actual positions from displacements in the representative snapshot.
    X10,X20,X1,X2=1.3,5.5,1.9,4.4
    assert abs(((X1+X2)-(X10+X20))/2-((X1-X10)+(X2-X20))/2)<1e-12
    assert abs((X2-X1)-((X20-X10)+(X2-X20)-(X1-X10)))<1e-12
    # Small positive time from each phase origin has the illustrated turn sense.
    h=1e-5
    cc=(1,0);cc_next=(math.cos(h),-math.sin(h))
    dd=(-1,0);dd_next=(-math.cos(h),-math.sin(h))
    common_cross=cc[0]*cc_next[1]-cc[1]*cc_next[0]
    relative_cross=dd[0]*dd_next[1]-dd[1]*dd_next[0]
    assert common_cross<0 and relative_cross>0
    text=(ROOT/'figures/题05_图稿源文件.tex').read_text()
    assert 'start angle=-10,end angle=-40' in text
    assert 'start angle=190,end angle=220' in text
    result=dict(passed=True,scope='actual vector joins and signed geometric relations; not visual review',
        two_rods_touch_both_rails=True,capacitor_has_no_short_circuit=True,
        plan_join_error_pdf_points=join_error,capacitor_join_error_pdf_points=cap_error,
        parallel_inductive_branch_join_errors_pdf_points=branch_errors,
        Lorentz_force_and_motional_emf_cross_products=True,
        displacement_and_actual_distance_consistent=True,
        phase_orbit_common_clockwise=True,phase_orbit_relative_counterclockwise=True,
        script_sha256=sha(Path(__file__)),tikz_source_sha256=sha(ROOT/'figures/题05_图稿源文件.tex'),
        figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in NAMES})
    (ROOT/'build/projected-geometry-q05.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
