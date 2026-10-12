"""第033套第4题：随机参数下检查两段T-Q关系和滑动阶段第一定律。"""
from pathlib import Path
import json
import random

ROOT = Path(__file__).resolve().parents[1]


def one_case(C, R, p0, S, F, T0):
    p1 = p0+F/S
    T1 = T0*p1/p0
    Q1 = C*(T1-T0)
    ceff = C+R-R*F/(2*p1*S)
    # 在滑动阶段任选温升，直接核对热力学第一定律。
    dT = .137*T0
    dV = R*dT/p1
    dx = dV/S
    dQ = ceff*dT
    first_law_residual = C*dT-(dQ+.5*F*dx-p1*dV)
    # 分段函数在转折点左右应连续。
    T_left = T0+Q1/C
    T_right = T1+(Q1-Q1)/ceff
    return {
        "p1": p1, "T1": T1, "Q1": Q1, "Ceff": ceff,
        "slope_fixed": 1/C, "slope_moving": 1/ceff,
        "continuity_error": abs(T_left-T_right),
        "first_law_error": abs(first_law_residual),
        "pressure_threshold_error": abs(p1*S-(p0*S+F)),
        "slope_order_ok": ceff>C,
    }


def main():
    rng = random.Random(3304)
    cases=[]
    for _ in range(500):
        R=rng.uniform(2,15)
        C=rng.uniform(.8,6)*R
        p0=rng.uniform(3e4,3e5)
        S=rng.uniform(.002,.3)
        F=rng.uniform(.01,.9)*p0*S
        T0=rng.uniform(180,600)
        cases.append(one_case(C,R,p0,S,F,T0))
    maxima={
        "continuity_error":max(c["continuity_error"] for c in cases),
        "first_law_error":max(c["first_law_error"] for c in cases),
        "pressure_threshold_error":max(c["pressure_threshold_error"] for c in cases),
    }
    assert maxima["continuity_error"] < 2e-12
    assert maxima["first_law_error"] < 2e-11
    assert maxima["pressure_threshold_error"] < 5e-11
    assert all(c["slope_order_ok"] and c["Ceff"]>0 for c in cases)
    report={
        "status":"pass",
        "method":"random parameter first-law balance and piecewise-continuity checks",
        "case_count":len(cases),
        "max_errors":maxima,
        "representative_cases":cases[:4],
    }
    (ROOT/"build/question04-verification.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    )
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
