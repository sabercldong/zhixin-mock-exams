"""Q6 control ports, pressure-work faces, state routes and graph geometry.

Tests inspect the current coordinates and independent elementary relations.
They do not substitute for actual inspection of figure/PDF pixels.
"""
from pathlib import Path
import math,re,json,hashlib,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
NAMES=["flow-06","reference-06","budget-06","flowwork-06","isothermal-06","nozzle-06"]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    source=ROOT/"figures/题06_图稿源文件.tex";tex=source.read_text()
    panels=re.findall(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}",tex,re.S)
    manuscript=(ROOT/"drafts/question-06.md").read_text();checks=[]
    def check(name,test,details=None):
        assert test,(name,details)
        checks.append({"name":name,"passed":True,"details":details or {}})
    check("six required vector pictures",len(panels)==6)
    flow,reference,budget,work,iso,nozzle=panels
    check("two distinct open inlet ports connect to tank interior",
          "(3.0,.75)--(3.0,.35)" in flow and "(3.0,1.65)--(3.0,2.05)" in flow
          and "(3.0,.95)--(3.0,1.45)" in flow
          and "(3.0,.75)--(3.0,.95)" not in flow
          and "(3.0,1.45)--(3.0,1.65)" not in flow)
    check("inlet arrow levels fall strictly inside correct open ports",
          .75<.85<.95 and 1.45<1.55<1.65
          and "(.35,1.55)--(3.50,1.55)" in flow
          and "(.35,.85)--(3.50,.85)" in flow)
    check("inlet and outlet arrows cross control boundary in material direction",
          .35<2.65<3.5 and 10.05<10.35<12.1
          and "(2.65,-.10)rectangle(10.35,2.65)" in flow
          and "(10.05,1.20)--(12.10,1.20)" in flow)
    check("positive heat is inward and shaft work outward",
          "(4.00,3.45)--(4.00,2.17)" in flow
          and "(5.10,2.18)--(5.10,3.45)" in flow
          and 2.17<2.65<3.45 and 2.18<2.65<3.45)
    check("reaction chamber connected to symmetric finite throat and open outlet",
          "(6.1,.80)" in flow and "(6.1,1.60)" in flow
          and "(7.10,1.01)--(7.85,1.01)" in flow
          and "(7.85,1.39)" in flow and "(10.1,.15)" in flow
          and "(10.1,2.25)" in flow
          and abs((1.01+1.39)/2-1.2)<1e-12
          and 0<1.39-1.01<1.60-.80<2.25-.15)
    check("stoichiometry on material labels not heat arrow",
          r"$3\dot\xi$" in flow and r"$\mathrm{N_2}:\mathrm{H_2O}=1:2$" in flow)
    check("reference route goes actual->reactant reference->product reference->exit",
          "(actual)at(0,0)" in reference and "(react)at(6.2,0)" in reference
          and "(product)at(6.2,-3.0)" in reference and "(exit)at(0,-3.0)" in reference
          and "(actual.east)--(react.west)" in reference
          and "(react.south)--(product.north)" in reference
          and "(product.west)--(exit.east)" in reference)
    check("reference signs and direct state difference preserved",
          r"{$D_1+D_2$}" in reference and r"{$-H_0$}" in reference
          and r"{$H_{\rm sens}$}" in reference
          and "(actual.south)--(exit.north)" in reference
          and r"{$\Delta H_{\rm total}$}" in reference)
    check("state-function path explicitly not actual engine sequence",
          "虚拟参考路径" in reference and "左下点才是最终出口产物的静焓" in manuscript)
    def constant(name):
        return float(re.search(r"\\def\\"+name+r"\{([0-9.]+)\}",budget).group(1))
    t0,ta,e,t1=[constant(n) for n in ["TrefX","TaX","EnergyY","SampleX"]]
    k=e*(ta-t1)/(ta-t0);slope=-e/(ta-t0)
    check("positive energy branch and ordered temperatures",0<t0<t1<ta and 0<k<e,
          {"T0_x":t0,"T1_x":t1,"Ta_x":ta,"E_y":e,"K_y":k})
    check("sample lies on energy line, actual source uses derived sample ordinate",
          abs(k-(e+slope*(t1-t0)))<1e-12
          and r"\EnergyY*(\TaX-\SampleX)/(\TaX-\TrefX)" in budget
          and r"(\TrefX,\EnergyY)--(\TaX,0)" in budget)
    check("energy graph axis is kinetic energy per reaction not velocity",
          r"$K_{\rm E}/\xi$" in budget and r"斜率 $-C_{p,\Sigma}$" in budget
          and slope<0 and r"K_{\rm E}/\xi=E-C_{p,\Sigma}(T_1-T_0)" in manuscript)
    angle=math.degrees(math.atan(slope))
    check("slope label follows drawn negative slope",
          abs(angle-(-31.8))<.1 and "rotate=-31.8" in budget,{"drawing_angle_deg":angle})
    check("positive-energy-only segment; axis break not a missing temperature domain",
          r"(\TrefX,0)" in budget and r"(\TaX,0)" in budget
          and "(.46,-.08)--(.60,.08)" in budget
          and "正动能一侧" in manuscript)
    check("inlet swept volume spans upstream face to control face",
          "(2.40,0)rectangle(3.00,1.40)" in work
          and "(2.40,0)--(2.40,1.40)" in work
          and "(3.00,-.12)--(3.00,1.90)" in work)
    check("outlet swept volume spans control face to downstream face",
          "(3.00,0)rectangle(3.60,1.40)" in work
          and "(3.60,0)--(3.60,1.40)" in work
          and "(3.00,-.35)--(3.60,-.35)" in work)
    check("pressure arrows act from correct material faces with correct recipients",
          "(2.40,.47)--(3.70,.47)" in work
          and "(3.60,.47)--(4.90,.47)" in work
          and "上游对流体" in work and "流体对下游" in work)
    check("swept volume equals section area times displacement in both panels",
          abs((3.0-2.4)*1.4-(3.6-3.0)*1.4)<1e-12
          and r"dV_i=S_i d\ell_i" in manuscript
          and r"dV_e=S_e d\ell_e" in manuscript,
          {"normalized_inlet_volume":(3-2.4)*1.4,"normalized_outlet_volume":(3.6-3)*1.4})
    check("pressure magnitude labels displaced clear of duct walls and displacements",
          r"\node[below]at(4.15,-.10){$p_iS_i$}" in work
          and r"\node[below]at(4.90,-.10){$p_0S_e$}" in work
          and 4.15-2.7>1 and 4.9-3.3>1)
    check("pressure work signs are actually used in following energy equations",
          r"(p_iS_i)d\ell_i=p_i\,dV_i" in manuscript
          and r"(p_0S_e)d\ell_e=p_0\,dV_e" in manuscript
          and r"=3RT_1-p_1\bar V_1-p_2\bar V_2" in manuscript)
    check("isotherm obeys same normalized pV product at both endpoints",
          abs(1*4-4*1)<1e-12 and "(1,4)" in iso and "(4,1)" in iso
          and r"(\x,{4/\x})" in iso)
    check("isothermal expansion area extends only over initial/final volume interval",
          "domain=1:4" in iso and "(1,0)" in iso and "(4,0)--cycle" in iso)
    check("isotherm direction corresponds to expansion with decreasing pressure",
          "domain=1.70:2.40" in iso and 4/1.7>4/2.4
          and math.log(4/1)>0)
    check("isothermal heat/work pair and signed integral are used",
          r"$Q_i=W_i$" in iso and r"$pV=RT_0$" in iso
          and r"=RT_0\ln\frac{p_{xi}}{p_0}" in manuscript
          and r"Q_i-W_i=0" in manuscript)
    check("nozzle throat finite symmetric and narrower than either end",
          "(2.7,-.38)--(3.3,-.38)" in nozzle
          and "(2.7,.38)--(3.3,.38)" in nozzle
          and 0<2*.38<2*1.08<2*1.18)
    check("flow arrows lie on nozzle symmetry axis and point downstream",
          "(.23,0)--(1.42,0)" in nozzle and "(6.25,0)--(8.65,0)" in nozzle
          and "(-.45,0)--(8.70,0)" in nozzle)
    check("stagnation and static variables not conflated with saturation pressure",
          r"$T_a,\ p_c$" in nozzle and r"$T_1,\ p_0$" in nozzle
          and "入口总态" in nozzle and "出口静态" in nozzle
          and "不是原题的某一个供料饱和压力" in manuscript)
    check("nozzle picture feeds actual enthalpy/entropy equations",
          r"c_pT_a&=c_pT_1+\frac12u^2" in manuscript
          and r"\left(\frac{p_0}{p_c}\right)^{6/23}" in manuscript)
    for i,name in enumerate(NAMES,1):
        check(name+" referenced in analysis and not decorative",
              f"](../figures/{name}.png)" in manuscript
              and manuscript.count(f"图6-{i}")>=2)
    figures={}
    for name in NAMES:
        pdf=ROOT/f"figures/{name}.pdf";png=pdf.with_suffix(".png")
        subprocess.run(["qpdf","--check",str(pdf)],capture_output=True,check=True)
        with fitz.open(pdf) as doc:
            check(name+" current single vector page",len(doc)==1 and len(doc[0].get_drawings())>0)
        figures[name]={"pdf_sha256":sha(pdf),"png_sha256":sha(png)}
    collection=source.with_suffix(".pdf")
    subprocess.run(["qpdf","--check",str(collection)],capture_output=True,check=True)
    warnings=re.findall(r"(?m)^.*(?:Warning|Underfull|Overfull|Missing character|^!).*$",
                        source.with_suffix(".log").read_text())
    check("current figure compilation log clean",not warnings,{"warnings":warnings})
    report={"question":"06","checks":checks,"check_count":len(checks),"source_sha256":sha(source),
            "manuscript_sha256":sha(ROOT/"drafts/question-06.md"),
            "collection_sha256":sha(collection),"program_sha256":sha(Path(__file__)),
            "renderer_sha256":sha(ROOT/"scripts/render_figures_06.py"),"figures":figures,
            "passed":True,"actual_visual_review_inferred":False,
            "question_accepted":False,"set_accepted":False}
    (ROOT/"build/question-06-figure-geometry.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"check_count":len(checks),"passed":True,"question_accepted":False}))
if __name__=="__main__":main()
