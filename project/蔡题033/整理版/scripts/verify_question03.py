"""第033套第3题：扫描摆角并直接构造两接触处的摩擦锥反力。"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]


def loads(theta):
    """取m*g=1；返回所需接触合力的水平/轴向量H与竖直量V。"""
    c, s = math.cos(theta), math.sin(theta)
    tension = 3*c
    return tension*s, 1.5+tension*c


def planar_required(theta):
    H, V = loads(theta)
    delta = math.atan2(H, V)
    return math.tan(delta/2)


def spatial_required(theta):
    H, V = loads(theta)
    A, B = V/math.sqrt(2), H/2
    normal = (A*A+B*B)/A
    fs = A-normal
    fz = B
    mu = math.hypot(fs, fz)/normal
    # 对称的两接触反力：x分量相反，y、z分量各承担一半。
    per_y = (normal+fs)/math.sqrt(2)
    residual = max(abs(2*per_y-V), abs(2*fz-H))
    return mu, normal, fs, fz, residual


def golden_max(function, left=0.0, right=math.pi/2, iterations=100):
    ratio = (math.sqrt(5)-1)/2
    x1 = right-ratio*(right-left)
    x2 = left+ratio*(right-left)
    f1, f2 = function(x1), function(x2)
    for _ in range(iterations):
        if f1 < f2:
            left, x1, f1 = x1, x2, f2
            x2 = left+ratio*(right-left)
            f2 = function(x2)
        else:
            right, x2, f2 = x2, x1, f1
            x1 = right-ratio*(right-left)
            f1 = function(x1)
    x = (left+right)/2
    return x, function(x)


def main():
    sample_count = 200001
    max_planar = (-1.0, None)
    max_spatial = (-1.0, None)
    max_residual = 0.0
    for i in range(sample_count):
        theta = (math.pi/2)*i/(sample_count-1)
        p = planar_required(theta)
        s, _, _, _, residual = spatial_required(theta)
        if p > max_planar[0]: max_planar = (p, theta)
        if s > max_spatial[0]: max_spatial = (s, theta)
        max_residual = max(max_residual, residual)
    theta_p, mu_p = golden_max(planar_required)
    theta_s, mu_s = golden_max(lambda z: spatial_required(z)[0])
    exact_p = 2-math.sqrt(3)  # tan 15 degrees
    exact_s = 1/math.sqrt(7)
    assert abs(theta_p-math.pi/3) < 2e-8
    assert abs(theta_s-math.pi/3) < 2e-8
    assert abs(mu_p-exact_p) < 2e-14
    assert abs(mu_s-exact_s) < 2e-14
    assert max_residual < 2e-15

    # 直接检查平面情形的两接触力构造。
    construction_residual = 0.0
    for i in range(1, 1000):
        theta=(math.pi/2)*i/1000
        H,V=loads(theta)
        phi=.5*math.atan2(H,V)
        y=V/2
        xa=y*math.tan(math.pi/4+phi)
        xb=y*math.tan(-math.pi/4+phi)
        construction_residual=max(construction_residual,abs(xa+xb-H))
    assert construction_residual < 3e-14
    report = {
        "status": "pass",
        "method": "dense angle scan, golden-section maximization, and explicit friction-cone force construction",
        "sample_count": sample_count,
        "planar": {
            "theta_max_numeric": theta_p,
            "theta_max_degrees": math.degrees(theta_p),
            "mu_numeric": mu_p,
            "mu_exact": exact_p,
            "dense_scan_mu": max_planar[0],
        },
        "spatial": {
            "theta_max_numeric": theta_s,
            "theta_max_degrees": math.degrees(theta_s),
            "mu_numeric": mu_s,
            "mu_exact": exact_s,
            "dense_scan_mu": max_spatial[0],
        },
        "max_force_balance_residual": max_residual,
        "max_planar_construction_residual": construction_residual,
    }
    (ROOT/"build/question03-verification.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    )
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
