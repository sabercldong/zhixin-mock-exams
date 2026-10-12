"""第033套第1题：用椭圆支承函数与有限差分独立核验焦点轨迹。"""
from pathlib import Path
import json
import math
import random

ROOT = Path(__file__).resolve().parents[1]


def support(alpha, a, b):
    c2 = a * a - b * b
    return math.sqrt(b * b + c2 * math.cos(alpha) ** 2)


def y_focus(alpha, a, b):
    c = math.sqrt(a * a - b * b)
    return support(alpha, a, b) + c * math.cos(alpha)


def y_point(alpha, a, b, d):
    return support(alpha, a, b) + d * math.cos(alpha)


def derivatives(alpha, a, b, step=2e-4):
    """五点差分求y'、y''；滚动几何还给出x'=y、x''=y'。"""
    f = lambda z: y_focus(z, a, b)
    fm2, fm1, f0, fp1, fp2 = [f(alpha + k * step) for k in (-2, -1, 0, 1, 2)]
    yp = (fm2 - 8 * fm1 + 8 * fp1 - fp2) / (12 * step)
    ypp = (-fm2 + 16 * fm1 - 30 * f0 + 16 * fp1 - fp2) / (12 * step * step)
    return f0, yp, ypp


def derivatives_point(alpha, a, b, d, step=2e-4):
    f = lambda z: y_point(z, a, b, d)
    fm2, fm1, f0, fp1, fp2 = [f(alpha + k * step) for k in (-2, -1, 0, 1, 2)]
    yp = (fm2 - 8 * fm1 + 8 * fp1 - fp2) / (12 * step)
    ypp = (-fm2 + 16 * fm1 - 30 * f0 + 16 * fp1 - fp2) / (12 * step * step)
    return f0, yp, ypp


def generic_offset_case(a, b, d, g):
    c2 = a * a - b * b
    y3, yp3, ypp3 = derivatives_point(math.pi, a, b, d)
    rho_num = math.hypot(y3, yp3) ** 3 / abs(y3 * ypp3 - yp3 * yp3)
    rho_formula = a * (a - d) ** 2 / (a * d - c2)
    y2, yp2, ypp2 = derivatives_point(math.pi / 2, a, b, d)
    det2 = y2 * ypp2 - yp2 * yp2
    q = math.sqrt(b * b + d * d)
    v2sq = 2 * g * (a + d - b)
    ax = g * b * d / q ** 2 + v2sq * (c2 - d * d) * d / q ** 4
    ay = -g * d * d / q ** 2 + v2sq * (c2 - d * d) * b / q ** 4
    # 直接由有限差分轨迹的切、法分量重构加速度。
    speed_shape = math.hypot(y2, yp2)
    tx, ty = y2 / speed_shape, yp2 / speed_shape
    nx, ny = -ty, tx
    curvature = det2 / speed_shape ** 3
    at = -g * ty
    ax_num = at * tx + v2sq * curvature * nx
    ay_num = at * ty + v2sq * curvature * ny
    return {
        "rho_relative": abs(rho_num / rho_formula - 1),
        "det_absolute": abs(det2 - (c2 - d * d)),
        "acceleration_absolute": max(abs(ax_num - ax), abs(ay_num - ay)),
    }


def one_case(a, b, g):
    c = math.sqrt(a * a - b * b)
    # 状态III，alpha=pi。
    y3, yp3, ypp3 = derivatives(math.pi, a, b)
    speed_shape3 = math.hypot(y3, yp3)
    det3 = y3 * ypp3 - yp3 * yp3
    rho_num = speed_shape3 ** 3 / abs(det3)
    rho_formula = a * (a - c) / c
    v3sq = 4 * g * c
    ac_num = v3sq / rho_num
    ac_formula = 4 * g * c * c / (a * (a - c))

    # 状态II，alpha=pi/2；曲率行列式应为零。
    y2, yp2, ypp2 = derivatives(math.pi / 2, a, b)
    speed_shape2 = math.hypot(y2, yp2)
    det2 = y2 * ypp2 - yp2 * yp2
    tx, ty = y2 / speed_shape2, yp2 / speed_shape2
    at = -g * ty
    ax, ay = at * tx, at * ty
    ax_formula = g * b * c / (a * a)
    ay_formula = -g * c * c / (a * a)
    normal = g + ay
    normal_formula = g * b * b / (a * a)
    friction_formula = ax_formula
    # 取m=1，直接检查牛顿方程残差。
    fx_residual = friction_formula - ax
    fy_residual = normal_formula - g - ay

    return {
        "a": a,
        "b": b,
        "c": c,
        "state_III": {
            "rho_numeric": rho_num,
            "rho_formula": rho_formula,
            "a_numeric": ac_num,
            "a_formula": ac_formula,
        },
        "state_II": {
            "path_curvature_determinant": det2,
            "shape_speed": speed_shape2,
            "ax_numeric": ax,
            "ax_formula": ax_formula,
            "ay_numeric": ay,
            "ay_formula": ay_formula,
            "normal_per_mass": normal,
            "normal_formula_per_mass": normal_formula,
            "newton_residual": max(abs(fx_residual), abs(fy_residual)),
        },
        "errors": {
            "rho_relative": abs(rho_num / rho_formula - 1),
            "aIII_relative": abs(ac_num / ac_formula - 1),
            "aII_absolute": max(abs(ax - ax_formula), abs(ay - ay_formula)),
            "detII_absolute": abs(det2),
        },
    }


def main():
    rng = random.Random(3301)
    cases = []
    for _ in range(160):
        a = rng.uniform(1.0, 6.0)
        b = a * rng.uniform(0.28, 0.94)
        g = rng.uniform(4.0, 15.0)
        cases.append(one_case(a, b, g))
    generic = []
    for _ in range(80):
        a = rng.uniform(1.0, 6.0)
        b = a * rng.uniform(0.35, 0.93)
        c2 = a * a - b * b
        threshold = c2 / a
        d = threshold + rng.uniform(0.08, 0.92) * (a - threshold)
        g = rng.uniform(4.0, 15.0)
        generic.append(generic_offset_case(a, b, d, g))
    maxima = {
        key: max(case["errors"][key] for case in cases)
        for key in cases[0]["errors"]
    }
    # 五点差分误差阈值；与正文闭式公式无共同代数化简。
    assert maxima["rho_relative"] < 2.0e-6, maxima
    assert maxima["aIII_relative"] < 2.0e-6, maxima
    assert maxima["aII_absolute"] < 2.0e-5, maxima
    assert maxima["detII_absolute"] < 2.0e-5, maxima
    assert max(case["state_II"]["newton_residual"] for case in cases) < 2.0e-5
    generic_maxima = {
        key: max(case[key] for case in generic)
        for key in generic[0]
    }
    assert generic_maxima["rho_relative"] < 2.0e-6, generic_maxima
    assert generic_maxima["det_absolute"] < 2.0e-5, generic_maxima
    assert generic_maxima["acceleration_absolute"] < 2.0e-5, generic_maxima
    report = {
        "status": "pass",
        "method": "ellipse support function plus five-point finite differences",
        "case_count": len(cases),
        "max_errors": maxima,
        "generic_offset_case_count": len(generic),
        "generic_offset_max_errors": generic_maxima,
        "representative_cases": cases[:4],
    }
    target = ROOT / "build/question01-verification.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
