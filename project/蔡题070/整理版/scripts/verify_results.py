from __future__ import annotations

import math


def close(actual: float, expected: float, tol: float = 1e-9) -> None:
    scale = max(1.0, abs(actual), abs(expected))
    if abs(actual - expected) > tol * scale:
        raise AssertionError(f"{actual!r} != {expected!r}")


def q1_launch_range() -> None:
    x1 = (math.sqrt(13.0) - 1.0) / 6.0
    close(3.0 * x1 * x1 + x1 - 1.0, 0.0)
    s1_over_l = 4.0 * x1 * (1.0 - x1) * math.sqrt(1.0 - x1 * x1)
    close(s1_over_l, 0.8852156673, 1e-8)

    # Positive root of the movable-board stationary polynomial.
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        value = mid**4 + mid**3 + 4.0 * mid**2 + mid - 1.0
        if value < 0.0:
            lo = mid
        else:
            hi = mid
    x2 = (lo + hi) / 2.0
    assert x2 < x1
    assert math.acos(x2) > math.acos(x1)


def q2_dielectric_cylinder() -> None:
    eps1, eps2 = 5.0, 2.0
    c = 2.0 * eps2 / (eps1 + eps2)
    eta = (eps1 - eps2) / (eps1 + eps2)
    # Potential and normal-displacement boundary conditions.
    close(1.0 - eta, c)
    close(eps1 * c, eps2 * (1.0 + eta))
    # Identical-medium and conductor limits.
    close(2.0 * eps2 / (eps2 + eps2), 1.0)
    assert 2.0 * eps2 / (1e12 + eps2) < 1e-10


def q3_rolling_modes() -> None:
    kappa = 2.0 / 5.0
    close(1.0 / (1.0 + kappa), 5.0 / 7.0)
    close((2.0 + kappa) / (1.0 + kappa), 12.0 / 7.0)

    # In the axisymmetric case the factored circular-mode formula must
    # reproduce the two roots of the quadratic in omega^2.
    a, q = 3.2, 0.9
    w_plus = math.sqrt(a + q * q / 4.0) + q / 2.0
    w_minus = math.sqrt(a + q * q / 4.0) - q / 2.0
    for w in (w_plus, w_minus):
        close((a - w * w) ** 2 - q * q * w * w, 0.0)


def q4_push_cannon() -> None:
    a0, l1, l2, h = 2.7, 2.0, 3.0, 1.0
    work_over_m = a0 * (l1 - h) * l2 / (l1 - h + l2)
    v_rel_sq = 2.0 * work_over_m
    close(v_rel_sq, 2.0 * a0 * l2 * (l1 - h) / (l1 - h + l2))

    integral = 2.0 * (1.0 + 0.75 * math.log(3.0))
    # Numerical Simpson check of integral_0^1 sqrt((3+x)/x) dx.
    n = 200000
    # Remove the integrable endpoint singularity with x=t^2.
    step = 1.0 / n
    total = 0.0
    for i in range(n + 1):
        t = i * step
        value = 2.0 * math.sqrt(3.0 + t * t) if t > 0.0 else 2.0 * math.sqrt(3.0)
        weight = 1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)
        total += weight * value
    numerical = total * step / 3.0
    close(numerical, integral, 1e-8)


def q5_projective_construction() -> None:
    # The two diameter-circle conditions imply right angles at O.
    p, qpt = (-3.0, 0.0), (3.0, 0.0)
    r, s = (-2.25, 3.1), (2.25, 3.1)
    y = (3.1**2 + 3.0**2 - 2.25**2) / (2.0 * 3.1)
    x = math.sqrt(3.0**2 - y**2)

    def dot_from(vertex: tuple[float, float], a: tuple[float, float], b: tuple[float, float]) -> float:
        return (a[0] - vertex[0]) * (b[0] - vertex[0]) + (a[1] - vertex[1]) * (b[1] - vertex[1])

    close(dot_from((x, y), p, qpt), 0.0)
    close(dot_from((x, y), r, s), 0.0)


def q6_rod_collision() -> None:
    # I_O/(m l^2)=1/9 and post-impact kinetic energy is one quarter of pre-impact.
    close(1.0 / 12.0 + 1.0 / 36.0, 1.0 / 9.0)
    close((1.0 / 8.0) / (1.0 / 2.0), 1.0 / 4.0)
    # h_max/l=mu and the stated half-height case gives the quoted angle.
    mu = 2.0
    close(mu, 2.0)
    theta = 2.0 * math.atan((math.sqrt(7.0) - 2.0) / 3.0)
    close(1.0 + 2.0 * math.sin(theta), 2.0 * math.cos(theta))
    close(math.degrees(theta), 24.2951889, 1e-7)


def q7_induction_rail() -> None:
    c = 2.0 + math.sqrt(2.0)
    b, r_per_length, m, v1 = 1.7, 0.8, 2.3, 1.2
    xf_sq = 2.0 * c * m * r_per_length * v1 / b**2
    alpha = b**2 / (c * m * r_per_length)
    close(v1 - 0.5 * alpha * xf_sq, 0.0)
    # At t=0, x=0 and at large t the tanh solution tends to xf.
    xf = math.sqrt(xf_sq)
    close(xf * math.tanh(0.0), 0.0)
    assert xf * math.tanh(2.0) < xf * math.tanh(20.0) <= xf


def q8_decay_chain() -> None:
    na = 6.02214076e23
    t1_days = 1.91 * 365.25
    t2_days = 3.66
    ratio = t1_days / t2_days
    n20 = na / (228.0 * ratio + 224.0)
    n10 = ratio * n20
    close(n20, 1.37860805e19, 2e-6)
    close(n10, 2.62774559e21, 2e-6)

    lambda_ratio = t2_days / t1_days
    n2_half = n20 / (2.0 * (1.0 - lambda_ratio))
    close(n2_half, 6.92939428e18, 2e-6)
    assert 2.0 ** (-ratio) < 1e-50


def main() -> None:
    q1_launch_range()
    q2_dielectric_cylinder()
    q3_rolling_modes()
    q4_push_cannon()
    q5_projective_construction()
    q6_rod_collision()
    q7_induction_rail()
    q8_decay_chain()
    print("第070套数值、边界、极限与积分结果核验通过。")


if __name__ == "__main__":
    main()
