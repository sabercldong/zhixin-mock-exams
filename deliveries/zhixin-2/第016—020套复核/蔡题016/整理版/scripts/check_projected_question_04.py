"""Check the actual question-04 vector PDF's tangent and contact joins.

This is a geometric check, not a substitute for reading the rendered figures.
"""
from pathlib import Path
import hashlib,json
import fitz

ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def black(v):
    return v['color'] is not None and max(v['color'])<.02
def main():
    path=ROOT/'figures/question-04.pdf'
    with fitz.open(path) as doc:
        assert len(doc)==1
        paths=doc[0].get_drawings()
        circles=[v for v in paths if black(v) and v['type']=='s'
                 and len(v['items'])==4 and all(t[0]=='c' for t in v['items'])
                 and v['rect'].width>25]
        assert len(circles)==4
        ropes=sorted([v for v in paths if v['color'] is not None
                      and v['color'][2]>.5 and max(v['color'][:2])<.02
                      and len(v['items'])==1 and v['items'][0][0]=='l'
                      and v['rect'].width<.01],key=lambda v:v['rect'].x0)
        assert len(ropes)==2
        boxes=[v for v in paths if black(v) and v['type']=='fs'
               and v['rect'].width>5 and v['rect'].height>5]
        floor=[v for v in paths if black(v) and v['type']=='s'
               and len(v['items'])==1 and v['items'][0][0]=='l'
               and v['rect'].height<.01 and v['rect'].width>20]
        checks=[]
        for rope in ropes:
            rr=rope['rect']
            pair=[v['rect'] for v in circles if v['rect'].x0<rr.x0<v['rect'].x1+.01]
            assert len(pair)==2
            inner,outer=sorted(pair,key=lambda r:r.width)
            cy=(outer.y0+outer.y1)/2
            mass=[v['rect'] for v in boxes if abs(v['rect'].y0-rr.y1)<.02
                  and v['rect'].x0<rr.x0<v['rect'].x1]
            assert len(mass)==1
            relevant_floor=[v['rect'] for v in floor if abs(v['rect'].y0-outer.y1)<.02]
            left=[r.x1 for r in relevant_floor if r.x1<rr.x0]
            right=[r.x0 for r in relevant_floor if r.x0>rr.x0]
            assert left and right
            gap=(max(left),min(right))
            error=max(abs(rr.x0-inner.x1),abs(rr.y0-cy),abs(rr.y1-mass[0].y0),
                      abs((mass[0].x0+mass[0].x1)/2-rr.x0))
            assert error<.025
            assert gap[0]<rr.x0<gap[1] and gap[1]-gap[0]<outer.width*.1
            checks.append(dict(inner_hub_tangent=True,rope_reaches_mass_top=True,
                               floor_has_slot=True,slot_pdf_points=list(gap),
                               maximum_join_error_pdf_points=error,
                               r_over_R=inner.width/outer.width))
            assert abs(inner.width/outer.width-.4)<1e-4
        right_outer=max([v['rect'] for v in circles],key=lambda r:r.x1)
        block=[v['rect'] for v in boxes if v['rect'].height>60
               and abs(v['rect'].x0-right_outer.x1)<.025]
        assert len(block)==1
        block=block[0]
        assert abs(block.y1-right_outer.y1)<.025
        cy=(right_outer.y0+right_outer.y1)/2
        contact=[v['rect'] for v in paths if v['fill'] is not None
                 and max(v['fill'])<.02 and v['type'] in ['f','fs']
                 and v['rect'].width<4 and v['rect'].height<4
                 and abs((v['rect'].x0+v['rect'].x1)/2-block.x0)<.025
                 and abs((v['rect'].y0+v['rect'].y1)/2-cy)<.025]
        assert len(contact)==1
    result=dict(passed=True,scope='actual vector geometry, not automatic visual review',
                rope_tangent_slot_and_mass_connections=checks,
                block_left_face_at_outer_tangent=True,
                block_floor_contact_at_same_height=True,
                C_contact_at_spool_center_height=True,
                pdf_sha256=sha(path),script_sha256=sha(Path(__file__)))
    output=ROOT/'build/projected-geometry-q04.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
