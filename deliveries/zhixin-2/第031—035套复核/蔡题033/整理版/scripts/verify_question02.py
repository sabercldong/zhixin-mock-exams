"""第033套第2题：直接积分共同运动方程并核验三种摩擦区间。"""
from pathlib import Path
import json
import math
import random
import re

ROOT = Path(__file__).resolve().parents[1]


def verify_pulley_geometry():
    """从实际TikZ源读取轮缘和绳路，避免只检查另一组自定义坐标。"""
    source=(ROOT/'figures/题02_图稿源文件.tex').read_text()
    number=r'(-?(?:\d+(?:\.\d*)?|\.\d+))'
    point=r'\('+number+','+number+r'\)'
    rim=re.search(r'\\draw\[body,fill=white\]\s*'+point+r'\s*circle\('+number+r'\)',source)
    rope=re.search(r'\\draw\[rope\]\s*'+point+r'--'+point+
                   r'\s*arc\[start angle=90,end angle=0,radius='+number+r'\]--'+point,source)
    assert rim and rope,'未识别实际轮缘或绳路'
    cx,cy,radius=map(float,rim.groups())
    sx,sy,tx,ty,arc_radius,ex,ey=map(float,rope.groups())
    residuals=[abs(radius-arc_radius),abs(tx-cx),abs(ty-cy-radius),
               abs(sy-ty),abs(ex-cx-radius)]
    assert max(residuals)<1e-12 and sx<tx and ey<cy,'轮缘相切或绳路连续性错误'
    return dict(status='pass',rim_radius=radius,rope_radius=arc_radius,
                max_tangency_residual=max(residuals))


def rk4_step(x, v, dt, mass, spring, drive):
    def acc(position):
        return (drive - spring * position) / mass
    k1x, k1v = v, acc(x)
    k2x, k2v = v + .5 * dt * k1v, acc(x + .5 * dt * k1x)
    k3x, k3v = v + .5 * dt * k2v, acc(x + .5 * dt * k2x)
    k4x, k4v = v + dt * k3v, acc(x + dt * k3x)
    return (x + dt * (k1x + 2*k2x + 2*k3x + k4x) / 6,
            v + dt * (k1v + 2*k2v + 2*k3v + k4v) / 6)


def one_case(m1, m2, M, k, g, fraction):
    total = m1 + m2 + M
    mu0 = M / total
    mu1 = M * (2*m1 + m2 + 2*M) / (m2 * total)
    mu = mu0 + fraction * (mu1 - mu0)
    L = m2 * g * (mu * total - M) / (k * (M + m1))
    amplitude = M * g / k
    omega = math.sqrt(k / total)
    time_formula = math.acos(1 - L / amplitude) / omega

    # 不调用闭式轨迹，直接积分T*x''=Mg-kx，寻找第一次到达L。
    turn_time = math.pi / omega
    dt = turn_time / 20000
    x = v = t = 0.0
    previous = (t, x)
    max_energy_error = 0.0
    while x < L and t < turn_time:
        previous = (t, x)
        x, v = rk4_step(x, v, dt, total, k, M*g)
        t += dt
        energy = .5 * total * v*v + .5 * k*x*x - M*g*x
        max_energy_error = max(max_energy_error, abs(energy))
    t0, x0 = previous
    time_numeric = t0 + (L-x0) * (t-t0) / (x-x0)

    a = (M*g-k*L)/total
    friction_direct = m2*a+k*L
    friction_formula = (m2*M*g + (M+m1)*k*L)/total
    return {
        "mu0": mu0,
        "mu1": mu1,
        "mu": mu,
        "L": L,
        "turning_displacement": 2*amplitude,
        "time_formula": time_formula,
        "time_numeric": time_numeric,
        "time_absolute_error": abs(time_numeric-time_formula),
        "friction_relative_error": abs(friction_direct/friction_formula-1),
        "threshold_residual": abs(friction_formula/(m2*g)-mu),
        "max_energy_absolute_error": max_energy_error,
    }


def main():
    rng = random.Random(3302)
    cases = []
    for _ in range(60):
        values = [rng.uniform(.3, 7.0) for _ in range(3)]
        m1, m2, M = values
        k = rng.uniform(2.0, 25.0)
        g = rng.uniform(7.0, 13.0)
        fraction = rng.uniform(.04, .96)
        cases.append(one_case(m1, m2, M, k, g, fraction))
    maxima = {
        "time_absolute_error": max(c["time_absolute_error"] for c in cases),
        "friction_relative_error": max(c["friction_relative_error"] for c in cases),
        "threshold_residual": max(c["threshold_residual"] for c in cases),
        "energy_absolute_error": max(c["max_energy_absolute_error"] for c in cases),
    }
    assert maxima["time_absolute_error"] < 2e-7, maxima
    assert maxima["friction_relative_error"] < 2e-14, maxima
    assert maxima["threshold_residual"] < 2e-14, maxima
    assert all(0 < c["L"] < c["turning_displacement"] for c in cases)

    # 直接检查临界端点：mu0对应L=0；mu1对应最大伸长2Mg/k。
    endpoint_errors = []
    for _ in range(60):
        m1, m2, M = [rng.uniform(.3, 7.0) for _ in range(3)]
        k, g = rng.uniform(2.0, 25.0), rng.uniform(7.0, 13.0)
        total = m1+m2+M
        mu0 = M/total
        mu1 = M*(2*m1+m2+2*M)/(m2*total)
        def crossing(mu):
            return m2*g*(mu*total-M)/(k*(M+m1))
        endpoint_errors.append(max(abs(crossing(mu0)),
                                   abs(crossing(mu1)-2*M*g/k)))
    assert max(endpoint_errors) < 2e-13
    report = {
        "status": "pass",
        "method": "RK4 integration of the common-motion ODE plus direct force balance",
        "intermediate_case_count": len(cases),
        "endpoint_case_count": len(endpoint_errors),
        "max_errors": maxima,
        "max_endpoint_error": max(endpoint_errors),
        "pulley_geometry": verify_pulley_geometry(),
        "representative_cases": cases[:4],
    }
    (ROOT/"build/question02-verification.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
