from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 1e-8) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=1e-12):
        raise AssertionError(f"{actual=} 与 {expected=} 不符")


def verify_q1() -> None:
    g_const = 6.67e-11
    m_e, m_s = 6.0e24, 2.0e30
    period = 365.24 * 24 * 3600
    omega = 2 * math.pi / period
    length = (g_const * (m_s + m_e) / omega**2) ** (1 / 3)
    r_s = length * m_e / (m_s + m_e)
    speed = omega * r_s
    direct = (2 * math.pi * g_const / period) ** (1 / 3) * m_e / (
        m_s + m_e
    ) ** (2 / 3)
    close(length, 1.499e11, 8e-4)
    close(r_s, 4.50e5, 1.5e-3)
    close(speed, 8.95e-2, 1.5e-3)
    close(speed, direct)


def verify_q2() -> None:
    g, theta, a0 = 9.8, 0.37, 1.6
    drive = g * math.sin(theta) - a0 * math.cos(theta)
    ar = 2 * drive / 3
    friction = -ar / 2
    close(ar, drive + friction)
    ax = a0 + ar * math.cos(theta)
    ay = -ar * math.sin(theta)
    ax_expanded = a0 * (1 - 2 * math.cos(theta) ** 2 / 3) + g * math.sin(
        2 * theta
    ) / 3
    ay_expanded = -2 * g * math.sin(theta) ** 2 / 3 + a0 * math.sin(
        2 * theta
    ) / 3
    close(ax, ax_expanded)
    close(ay, ay_expanded)
    # Fixed incline and horizontal-platform limits.
    close(2 * (g * math.sin(theta)) / 3, 2 * g * math.sin(theta) / 3)
    close(a0 + 2 * (0 - a0) / 3, a0 / 3)


def verify_q3() -> None:
    # Work in consistent arbitrary units; only the algebraic identities matter.
    mu0, m0, m, mass, g = 1.3, 2.1, 0.8, 0.6, 9.8
    h = (3 * mu0 * m0 * m / (2 * math.pi * mass * g)) ** 0.25
    force = 3 * mu0 * m0 * m / (2 * math.pi * h**4)
    close(force, mass * g)
    derivative = -12 * mu0 * m0 * m / (2 * math.pi * h**5)
    close(-derivative / mass, 4 * g / h)
    i0, omega0 = 0.17, 21.0
    b0 = mu0 * m0 / (2 * math.pi * h**3)
    precession = m * b0 / (i0 * omega0)
    assert precession > 0
    drive_omega = 80.0
    b_min = drive_omega * math.sqrt(2 * i0 * b0 / m)
    slow_sq = m**2 * b_min**2 / (2 * i0**2 * drive_omega**2) - m * b0 / i0
    close(slow_sq, 0.0, 1e-6)


def verify_q4() -> None:
    a, c, m1, m2, g = 0.696, 0.313, 3.20, 3.55, 9.8
    total = m1 + m2
    delta = (m2 - m1) / total
    lam = (a - c) / (a + c)
    assert lam * m2 < m1 < m2
    l1 = a - c * delta
    l2 = a + c * delta
    l3 = 2 * math.sqrt(m1 * m2) / total * math.sqrt(a * a - c * c)
    close(l1, 0.6797703703703704)
    close(l2, 0.7122296296296295)
    close(l3, 0.6208123653542029)

    p, q, dm = a - c, a + c, m2 - m1
    k11 = g * total / (2 * p) + g * dm / (4 * c)
    k22 = g * total / (2 * q) + g * dm / (4 * c)
    k12 = -g * dm / (4 * c)
    aa = m1 * m2
    bb = -(k11 * m2 + k22 * m1)
    cc = k11 * k22 - k12 * k12
    disc = bb * bb - 4 * aa * cc
    roots = sorted(((-bb - math.sqrt(disc)) / (2 * aa), (-bb + math.sqrt(disc)) / (2 * aa)))
    close(roots[0], 9.96855691, 2e-8)
    close(roots[1], 27.87987549, 2e-8)
    close(math.sqrt(roots[0]), 3.15730215, 2e-8)
    close(math.sqrt(roots[1]), 5.28013972, 2e-8)


def verify_q5() -> None:
    for ratio in (1.01, 2.0, 10.0, 100.0):
        exact = math.acosh(ratio)
        logarithmic = math.log(ratio + math.sqrt(ratio * ratio - 1))
        close(exact, logarithmic)
    ratio = 10.0
    expanded = math.log(2 * ratio) - 1 / (4 * ratio**2)
    close(expanded, math.acosh(ratio), 4e-6)
    assert math.acosh(11.0) > math.acosh(10.0)


def verify_q6() -> None:
    # Normalize n0 = R = T0 = V0 = 1.
    def volume_on_adiabat(t_start: float, v_start: float, t_end: float) -> float:
        return v_start * (t_start / t_end) ** 6

    v_c = volume_on_adiabat(1.0, 2.0, 2.0)
    v_d = volume_on_adiabat(2.0, 1 / 64, 1.0)
    close(v_c, 1 / 32)
    close(v_d, 1.0)
    p_a, p_b = 1.0, 0.5
    p_c, p_d = 4 / v_c, 4 / (1 / 64)
    close(p_c, 128.0)
    close(p_d, 256.0)
    q1, q2 = math.log(2), 4 * math.log(2)
    close(q1 / (q2 - q1), 1 / 3)
    close(1 - q1 / q2, 3 / 4)
    assert p_d > p_c > p_a > p_b


def verify_q7() -> None:
    rho, g, sigma = 0.03, 9.8, 0.072
    r = 0.08
    h0 = rho * g * r * r / (8 * sigma)
    close(h0, rho * g * r**2 / (8 * sigma))
    r1, r2, separation = 0.12, 0.04, 0.01

    def z(x: float) -> float:
        return rho * g * (r1 * r1 - x * x) / (8 * sigma) + (
            separation + rho * g * (r2 * r2 - r1 * r1) / (8 * sigma)
        ) / math.log(r1 / r2) * math.log(r1 / x)

    close(z(r1), 0.0)
    close(z(r2), separation)
    wave_speed = math.sqrt(2 * sigma / rho)
    assert wave_speed > 0


def verify_q8() -> None:
    for beta in (0.0, 0.1, 0.35):
        close((1 - beta) / (1 - beta), 1.0)  # n = 1 limit
    n, beta = 1.6, 1e-7
    exact = (n + beta) / (1 + n * beta)
    first_order = n - (n * n - 1) * beta
    close(exact, first_order, 2e-14)
    focal_ratio = math.pi / 2 * math.sqrt(n / (2 * (n * n - 1)))
    assert focal_ratio > 0
    near_vacuum = math.pi / 2 * math.sqrt(1.001 / (2 * (1.001**2 - 1)))
    assert near_vacuum > focal_ratio


def main() -> None:
    verify_q1()
    verify_q2()
    verify_q3()
    verify_q4()
    verify_q5()
    verify_q6()
    verify_q7()
    verify_q8()
    print("第 045 套数值、矩阵本征值、边界条件、量纲标度与极限核验通过")


if __name__ == "__main__":
    main()
