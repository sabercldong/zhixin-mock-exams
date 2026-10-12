"""Geometry audit of the CURRENT vector PDFs; not a substitute for reading."""
from pathlib import Path
import hashlib, json, math
import fitz

ROOT=Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def blue(d):
    c=d.get("color")
    return c is not None and c[0]<.02 and c[1]<.02 and abs(c[2]-.7)<.02
def vertices(d):
    lines=[v for v in d["items"] if v[0]=="l"]
    return [tuple(lines[0][1])]+[tuple(v[2]) for v in lines]
report={}
doc=fitz.open(ROOT/"figures/mirror-01.pdf")
paths=doc[0].get_drawings()
wall=next(d for d in paths if d["type"]=="s" and d.get("color") is not None and
          abs(d["color"][0]-.25)<.01 and len(d["items"])==1 and d["rect"].width>240)
origin=((wall["rect"].x0+wall["rect"].x1)/2,wall["rect"].y0)
scale=wall["rect"].width/10.6
curves=[d for d in paths if blue(d) and len(d["items"])>=70]
assert len(curves)==10
rows=[]
for i,d in enumerate(curves):
    aa=[-2,-.8,0,.8,2][i//2]
    pts=[((xx-origin[0])/scale,(origin[1]-yy)/scale) for xx,yy in vertices(d)]
    # Complete curves meet the boundary; arrow marks are placed in the interior.
    samples=pts
    residual=max(abs((xx-aa)**2+yy*yy-(aa*aa+4)) for xx,yy in samples)
    assert residual<.002,(i,residual)
    start=math.hypot(samples[0][0],samples[0][1]-2)
    assert start<.0002
    tangent_dot=[]
    for a,b in zip(samples[2:-2],samples[3:-1]):
        xx,yy=(a[0]+b[0])/2,(a[1]+b[1])/2
        denominator_p=xx*xx+(yy-2)**2
        denominator_m=xx*xx+(yy+2)**2
        jx=(xx/denominator_p-xx/denominator_m)/(2*math.pi)
        jy=((yy-2)/denominator_p-(yy+2)/denominator_m)/(2*math.pi)
        value=jx*(b[0]-a[0])+jy*(b[1]-a[1])
        tangent_dot.append(value)
        assert value>0,(i,value)
    # The painted shaft/head footprint meets the thick horizontal boundary.
    painted_bottom=d["rect"].y1+d["width"]/2
    wall_top=wall["rect"].y0-wall["width"]/2
    contact=max(0,wall_top-painted_bottom)
    assert contact<.001,(i,contact)
    assert abs(samples[-1][1])<.0002,(i,samples[-1])
    rows.append(dict(curve=i+1,center_a=aa,source_error=start,circle_residual=residual,
                     min_flow_direction_dot=min(tangent_dot),painted_boundary_gap_pdf_points=contact))
report["mirror"]=dict(curves=rows,wall_origin_pdf_points=origin,
                      check="true circle streamlines; arrow directions follow image-source cumulative flux; painted paths meet boundary")
doc=fitz.open(ROOT/"figures/density-01.pdf")
paths=doc[0].get_drawings()
curve=next(d for d in paths if blue(d) and len(d["items"])>=200)
horizontal=next(d for d in paths if d.get("color")== (0.,0.,0.) and len(d["items"])==1 and d["rect"].width>250)
vertical=next(d for d in paths if d.get("color")== (0.,0.,0.) and len(d["items"])==1 and d["rect"].height>40)
origin=(vertical["rect"].x0,horizontal["rect"].y0)
scale=28.3468
points=vertices(curve)
residuals=[]
for xx,yy in points:
    u=(xx-origin[0])/scale
    density=(origin[1]-yy)/(4.5*scale)
    residuals.append(abs(density-1/(math.pi*(1+u*u))))
assert max(residuals)<2e-5,max(residuals)
report["density"]=dict(vertices=len(points),max_dimensionless_density_error=max(residuals),
                       check="actual plotted vector vertices vs normalized Cauchy function")

source=(ROOT/"figures/题01_图稿源文件.tex").read_text()
assert r"node[right]{$\Delta x$}" in source and r"node[above]{$\Delta y$}" in source
assert r"\draw[->](0,-2.7)--(0,3.25)" in source
assert r"\draw[aux](2.5,0)arc(0:180:2.5);" in source
assert r"\draw[aux](0,0)circle(2.5);" not in source
assert r"(\x,2.3)--(\x,2.9416667)" in source
report["analytic_constructions"]=dict(
    local_step=dict(a=1.8,angle_degrees=34,x_component=1.8*math.cos(math.radians(34)),
                    y_component=1.8*math.sin(math.radians(34)),axes="local displacements, not global coordinates"),
    strip_arrows=dict(l=1.4,h=3.8,lower_arrow_length=1.1,upper_arrow_length=.6416667,
                      Eb_over_Et_expected=(3.8-1.4)/1.4),
    mapping=dict(strip_l_over_h=.4,start_angle_degrees=72,
                 lower_boundary="positive real axis",upper_boundary="negative real axis",
                 diagram_circle="upper auxiliary semicircle only",unit_modulus=1))
names=["geometry-01","averaging-01","mirror-01","density-01","strip-01","mapping-01"]
report.update(passed=True,question="01",set_accepted=False,
              figure_source_sha256=sha(ROOT/"figures/题01_图稿源文件.tex"),
              script_sha256=sha(__file__),
              current_figures={n:dict(pdf_sha256=sha(ROOT/f"figures/{n}.pdf"),
                                    png_sha256=sha(ROOT/f"figures/{n}.png")) for n in names})
dest=ROOT/"build/question-01-figure-geometry.json"
dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(dict(passed=True,mirror_streamlines=10,
                    plotted_density_vertices=len(points),max_density_error=max(residuals),
                    output=str(dest)),ensure_ascii=False))
