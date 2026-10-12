"""Check actual vector-PDF rope vertices against both projected cone outlines."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    path=ROOT/'figures/question-03.pdf'
    with fitz.open(path) as doc:
        page=doc[0];drawings=page.get_drawings()
        # The first four gray single-line paths are the two cone silhouettes.
        edges=[v['items'][0] for v in drawings if len(v['items'])==1
               and v['items'][0][0]=='l' and v['color']
               and abs(v['color'][0]-.65)<.01 and abs(v['color'][1]-.65)<.01][:4]
        assert len(edges)==4
        count=0;error=0.
        for v in drawings:
            color=v['color']
            if not color or not ((color[2]>.5 and color[0]<.1) or
                                  (color[0]>.5 and color[1]<.1 and color[2]<.1)):
                continue
            for item in v['items']:
                if item[0]!='l':continue
                for point in item[1:]:
                    pair=edges[:2] if point.x<190 else edges[2:]
                    apex=pair[0][1]
                    sides=[line[1].x+(point.y-line[1].y)*
                           (line[2].x-line[1].x)/(line[2].y-line[1].y) for line in pair]
                    error=max(error,min(sides)-point.x,point.x-max(sides),apex.y-point.y,0.)
                    count+=1
        assert count>900 and error<.025
    result=dict(passed=True,scope='actual vector rope centerlines, not automatic visual review',
                colored_projected_rope_vertices=count,
                maximum_outline_violation_pdf_points=error,
                pdf_sha256=sha(path),script_sha256=sha(Path(__file__)))
    (ROOT/'build/projected-geometry-q03.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
