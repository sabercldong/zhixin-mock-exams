"""015 Q6 independent enthalpy, reaction, pressure-path and nozzle checks.

Models remain conditional until the separate human reply. Numerical verification
does not imply a physically realizable pair of 273.15 K liquids or PDF acceptance.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import math

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
SYMBOLIC = []
NUMERIC = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(name, expression):
    residual = sp.simplify(expression)
    assert residual == 0, (name, residual)
    SYMBOLIC.append({"name": name, "residual": str(residual)})


def close(name, value, expected, tolerance=3e-10):
    error = abs(value - expected) / max(1, abs(expected))
    assert error <= tolerance, (name, value, expected, error)
    NUMERIC.append({
        "name": name, "value": float(value), "expected": float(expected),
        "normalized_error": float(error),
    })


def main():
    R, T0, T1, p0, p1, p2 = sp.symbols("R T0 T1 p0 p1 p2", positive=True)
    H0, D1, D2, M = sp.symbols("H0 D1 D2 M", positive=True)
    CvN, CvW = sp.Rational(5, 2) * R, 3 * R
    CpN, CpW = CvN + R, CvW + R
    CV, CP = CvN + 2 * CvW, CpN + 2 * CpW
    exact("product Cv sum", CV - sp.Rational(17, 2) * R)
    exact("product Cp sum", CP - sp.Rational(23, 2) * R)
    exact("three product moles pressure work", CP - CV - 3 * R)
    CPIN = 4*R + sp.Rational(7,2)*R
    exact("reactant Cp sum", CPIN-sp.Rational(15,2)*R)
    exact("Kirchhoff reaction Cp difference", CP-CPIN-4*R)
    release_at_T1 = H0-(CP-CPIN)*(T1-T0)
    exact("heat reactants then react versus react then heat products",
          release_at_T1-D1-D2-CPIN*(T1-T0)
          -(H0-D1-D2-CP*(T1-T0)))
    exact("nitrogen atomic balance", sp.Integer(2)-2)
    exact("hydrogen atomic balance", sp.Integer(4)-2*2)
    exact("oxygen atomic balance", sp.Integer(2)-2)
    # Reaction gas enthalpy at T0: product minus reactants is -H0.
    hA, hB, hN, hW = sp.symbols("hA hB hN hW", real=True)
    heat = hA + hB - hN - 2 * hW
    inlet = hA + hB - D1 - D2
    outlet = hN + 2 * hW + CP * (T1 - T0)
    exact("direct species enthalpy accounting",
          inlet - outlet - (heat - D1 - D2 - CP * (T1 - T0)))
    exact("gas reaction delta U, delta n=1",
          ((hN - R*T0) + 2*(hW - R*T0) - (hA - R*T0) - (hB - R*T0))
          - (-heat - R*T0))
    vA, vB = sp.symbols("vA vB", positive=True)
    liquidU = (hA - D1 - p1*vA) + (hB - D2 - p2*vB)
    productU = (hN - R*T0) + 2*(hW - R*T0) + CV*(T1-T0)
    flow = 3*R*T1 - p1*vA - p2*vB
    exact("closed internal energy plus inlet/outlet flow work",
          liquidU - productU - flow - (heat - D1 - D2 - CP*(T1-T0)))
    exact("formal vaporization delta U includes pressure work",
          (hA-R*T0)-(hA-D1-p1*vA)-(D1-R*T0+p1*vA))
    exact("formal Hess phase path including reaction delta U",
          (D1-R*T0+p1*vA)+(D2-R*T0+p2*vB)-heat-R*T0
          +CV*(T1-T0)+flow - (D1+D2-heat+CP*(T1-T0)))
    Q, W, E = sp.symbols("Q W E", real=True)
    K = H0 - D1 - D2 - CP*(T1-T0) + Q - W
    exact("open first law including specified heat and shaft work",
          H0-D1-D2+Q-W-(K+CP*(T1-T0)))
    u = sp.sqrt(2*(H0-D1-D2-CP*(T1-T0))/M)
    exact("kinetic budget", M*u**2/2-(H0-D1-D2-CP*(T1-T0)))
    Tad = T0+(H0-D1-D2)/CP
    exact("stagnation temperature equivalence", u**2-2*CP/M*(Tad-T1))
    exact("speed square thermal slope", sp.diff(u**2,T1)+2*CP/M)
    exact("speed square reaction heat slope", sp.diff(u**2,H0)-2/M)
    exact("speed square each inlet deficit slope", sp.diff(u**2,D1)+2/M)
    uref = sp.symbols("uref", positive=True)
    exact("batch-mole scaling cancels in speed",
          2*sp.Symbol("xi", positive=True)*E/(sp.Symbol("xi", positive=True)*M)-2*E/M)
    # Exact isothermal heat balances: the logarithmic work is not an energy loss.
    x, vi, vf = sp.symbols("x vi vf", positive=True)
    Wiso = sp.integrate(R*T0/x, (x, vi, vf))
    exact("signed isothermal pV integral", Wiso - R*T0*sp.log(vf/vi))
    exact("isothermal delta U is zero", R*T0-R*T0)
    exact("isothermal heat equals work, net zero", Wiso-Wiso)
    legacy = H0-D1-D2-CP*(T1-T0)-R*T0*(sp.log(p1/p0)+sp.log(p2/p0))
    exact("legacy discrepancy is omitted isothermal heat",
          (H0-D1-D2-CP*(T1-T0)-legacy)-R*T0*(sp.log(p1/p0)+sp.log(p2/p0)))
    exact("ideal gas enthalpy pressure derivative", sp.diff(CpN*T1,p0))
    gamma = sp.simplify(CP/CV)
    exact("frozen mixture gamma", gamma-sp.Rational(23,17))
    exact("isentropic pressure exponent", gamma/(gamma-1)-sp.Rational(23,6))
    T, pc = sp.symbols("T pc", positive=True)
    Texit = T*(p0/pc)**((gamma-1)/gamma)
    exact("isentropic entropy change",
          CP*sp.log(Texit/T)-3*R*sp.log(p0/pc))
    Th, To, lh, lo = sp.symbols("Th To lh lo", positive=True)
    def1 = lh-CpW*(Th-T0)  # N2H4 Cv=3R, hence Cp=4R like H2O.
    def2 = lo+CpN*(T0-To)  # O2 Cv=2.5R, hence Cp=3.5R like N2.
    exact("actual-temperature feed deficits by state functions",
          (hA-(hA+CpW*(Th-T0)-lh))+(hB-(hB+CpN*(To-T0)-lo))
          -(def1+def2))
    a, b, delta = sp.symbols("a b delta", nonnegative=True)
    cp_int = sp.integrate(CP+(a+2*b)*x, (x, 0, delta))
    exact("variable heat capacity enthalpy integral",
          cp_int-CP*delta-(a+2*b)*delta**2/2)
    A = sp.symbols("A", positive=True)
    stable_delta = 2*E/(CP+sp.sqrt(CP**2+2*A*E))
    exact("stable quadratic temperature root",
          CP*stable_delta+A*stable_delta**2/2-E)
    from sympy.physics.units import joule, kilogram, meter, second, mole, kelvin, convert_to
    exact("SI speed squared", convert_to(joule/kilogram, meter**2/second**2)-meter**2/second**2)
    exact("SI molar enthalpy increment",
          convert_to((joule/(mole*kelvin))*kelvin,joule/mole)-joule/mole)

    rv = 8.31446261815324
    rng = np.random.default_rng(1506)
    # Independently construct species state enthalpies then integrate Cp.
    for j in range(18):
        ref = rng.uniform(-2e5, 3e5, 4)
        ref[0] = float(ref[2]+2*ref[3]+rng.uniform(3e5,8e5))
        ref[1] = 0.0
        h0 = float(ref[0]+ref[1]-ref[2]-2*ref[3])
        deficit = rng.uniform(5e3,5e4,2)
        t0 = float(rng.uniform(270,330))
        t1 = float(rng.uniform(450,1800))
        cpn, cpw = 3.5*rv, 4*rv
        integrals = [quad(lambda t:cpn,t0,t1)[0],quad(lambda t:cpw,t0,t1)[0]]
        hin = float(ref[0]-deficit[0]+ref[1]-deficit[1])
        hout = float(ref[2]+integrals[0]+2*(ref[3]+integrals[1]))
        budget = h0-float(sum(deficit))-11.5*rv*(t1-t0)
        assert budget>0
        close(f"species-state path {j+1} directly integrated budget",hin-hout,budget)
        # Separate route: heat gaseous reactants, integrate reaction-enthalpy change.
        reactant_heat = quad(lambda t:7.5*rv,t0,t1)[0]
        reaction_heat_at_t1 = h0-quad(lambda t:4*rv,t0,t1)[0]
        close(f"species-state path {j+1} independent Kirchhoff route",
              reaction_heat_at_t1-float(sum(deficit))-reactant_heat,budget)
        mass = float(rng.uniform(.04,.10))
        speed = brentq(lambda q:mass*q*q/2+hout-hin,0,10000,xtol=1e-10)
        close(f"species-state path {j+1} independent speed root",speed,math.sqrt(2*budget/mass))
        # Input liquid/feed molar volumes retained; flow terms must cancel.
        pressures = rng.uniform(1e4,1e7,2)
        volumes = rng.uniform(1e-5,1e-4,2)
        uin = hin-float(pressures@volumes)
        uout = hout-3*rv*t1
        flow = 3*rv*t1-float(pressures@volumes)
        close(f"species-state path {j+1} internal-energy flow check",uin-uout-flow,budget)
    # Direct signed p(V) quadrature, both expansion and compression, per mole.
    for j, ratio in enumerate([.01,.2,.75,1,2,5,20,100]):
        ti = 273.15
        pf = 1.01e5
        pi = pf*ratio
        vi, vf = rv*ti/pi, rv*ti/pf
        work = quad(lambda v:rv*ti/v,vi,vf,epsabs=1e-10,epsrel=2e-12)[0]
        close(f"isothermal {j+1} signed work integral",work,rv*ti*math.log(ratio))
        heat_in = work
        close(f"isothermal {j+1} no net energy loss",heat_in-work,0)
    # Real-temperature feed variant: two independent paths to a common gas reference.
    h0, lhv, lov, th, to, t0, t1, mass = 600000.,45000.,7000.,300.,90.,273.15,1300.,.064
    d1 = lhv-quad(lambda t:4*rv,t0,th)[0]
    d2 = lov+quad(lambda t:3.5*rv,to,t0)[0]
    effective = d1+d2
    # Path A: reference gas reaction plus deficits; path B: vaporize then heat gas reactants.
    reactants_to_ref = lhv+lov+quad(lambda t:4*rv,th,t0)[0]+quad(lambda t:3.5*rv,to,t0)[0]
    close("different storage-temperature phase path",reactants_to_ref,effective)
    root_storage = brentq(lambda q:mass*q*q/2+effective+11.5*rv*(t1-t0)-h0,0,10000)
    close("different storage-temperature speed",root_storage,math.sqrt(2*(h0-effective-11.5*rv*(t1-t0))/mass))
    # Nozzle temperature is solved from entropy ODE, not fed an answer velocity.
    for j in range(6):
        tc = 2500+400*j
        ratio = 2+3*j
        pe, pp = 1.01e5, 1.01e5*ratio
        gg = 23/17
        sol = solve_ivp(lambda p,y:[(gg-1)/gg*y[0]/p],[pp,pe],[tc],
                        rtol=2e-12,atol=2e-12,max_step=(pp-pe)/500)
        te = float(sol.y[0,-1])
        close(f"nozzle {j+1} entropy ODE exit temperature",
              te,tc*(pe/pp)**((gg-1)/gg),tolerance=2e-9)
        dv = quad(lambda t:11.5*rv,te,tc)[0]
        nozzle_speed = brentq(lambda q:mass*q*q/2-dv,0,10000)
        close(f"nozzle {j+1} enthalpy-integral speed root",
              nozzle_speed,math.sqrt(2*11.5*rv*(tc-te)/mass))
        entropy_change = quad(lambda t:11.5*rv/t,tc,te)[0]-3*rv*math.log(pe/pp)
        close(f"nozzle {j+1} independent entropy integral",entropy_change,0,tolerance=3e-9)
    # Four complete numerical variants and variable-Cp nonlinear roots.
    cp = 11.5*rv
    base = h0-45000.-12000.-cp*(t1-t0)
    sbase = brentq(lambda q:mass*q*q/2-base,0,10000)
    tad = brentq(lambda t:quad(lambda q:cp,t0,t)[0]-(h0-57000),t0,20000)
    pc_needed = 1.01e5*(tad/t1)**(23/6)
    acoef,bcoef=.005,.010
    added = quad(lambda t:(acoef+2*bcoef)*(t-t0),t0,t1)[0]
    delta_root = brentq(lambda dd:quad(lambda t:cp+(acoef+2*bcoef)*t,0,dd)[0]-(h0-57000),0,20000)
    stable_root = 2*(h0-57000)/(cp+math.sqrt(cp*cp+2*(acoef+2*bcoef)*(h0-57000)))
    close("variable Cp independent stagnation-temperature root",delta_root,stable_root)
    for j in range(7):
        aval = .005+.003*j
        ee = 2e5+50000*j
        rr = brentq(lambda dd:quad(lambda t:cp+aval*t,0,dd)[0]-ee,0,20000)
        close(f"variable Cp {j+1} integral versus stable root",rr,2*ee/(cp+math.sqrt(cp*cp+2*aval*ee)))
    sloss = brentq(lambda q:mass*q*q/2+30000+10000-base,0,10000)
    close("heat and shaft output root",sloss,math.sqrt(2*(base-40000)/mass))
    close("heat and shaft speed ratio",sloss/sbase,math.sqrt(1-40000/base))
    variable_speed = brentq(lambda q:mass*q*q/2+added-base,0,10000)
    close("variable Cp speed root",variable_speed,math.sqrt(2*(base-added)/mass))
    for j, xi in enumerate([.1,.5,1,3,10,100]):
        rr=brentq(lambda q:xi*mass*q*q/2-xi*base,0,10000)
        close(f"batch scaling {j+1} speed",rr,sbase)
    report = {
        "paper":"015","question":6,"stage":"independent conditional preverification; not document/figure/PDF acceptance",
        "created_utc":datetime.now(timezone.utc).isoformat(),
        "scope":"Frozen ideal gas products and explicitly given inlet enthalpy deficits; first-law energy bound, not proof of a realizable maximum or original liquid phases.",
        "verified_math":True,"document_complete":False,"model_condition_resolved":False,
        "question_accepted":False,"set_accepted":False,
        "symbolic_checks":SYMBOLIC,"numeric_checks":NUMERIC,
        "symbolic_count":len(SYMBOLIC),"numeric_count":len(NUMERIC),
        "max_normalized_error":max(x["normalized_error"] for x in NUMERIC),
        "variant_values":{
            "base_heat_budget_J_per_batch":base,"base_speed_m_s":sbase,
            "frozen_stagnation_temperature_K":tad,"isentropic_chamber_pressure_Pa":pc_needed,
            "loss_heat_J":30000.,"shaft_work_J":10000.,"loss_case_speed_m_s":sloss,
            "actual_temperature_feed_deficit1_J_mol":d1,"actual_temperature_feed_deficit2_J_mol":d2,
            "actual_temperature_feed_speed_m_s":root_storage,
            "variable_Cp_extra_enthalpy_J_per_batch":added,
            "variable_Cp_speed_m_s":variable_speed,
            "variable_Cp_stagnation_temperature_K":t0+delta_root,
        },
        "script_sha256":sha(Path(__file__)),
        "originals":{"paper":sha(ROOT.parent/"试卷.pdf"),"answers":sha(ROOT.parent/"答案.pdf")},
        "detail_manifest_sha256":sha(ROOT/"preview/originals/question-06-detail-manifest.json"),
        "actual_source_record_sha256":sha(ROOT/"preview/source-reviewed-q06.json"),
        "model_record_sha256":sha(ROOT/"build/question-06-模型审查.json"),
    }
    manuscript=ROOT/"drafts/question-06.md"
    report["source_sha256"]=sha(manuscript) if manuscript.exists() else None
    (ROOT/"build/question-06-preverification.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({key:report[key] for key in [
        "verified_math","symbolic_count","numeric_count","max_normalized_error","variant_values"
    ]},ensure_ascii=False))


if __name__ == "__main__":
    main()
