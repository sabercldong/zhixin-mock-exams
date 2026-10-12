from __future__ import annotations

import math


def close(a: float, b: float, rel: float = 1e-8) -> None:
    assert math.isclose(a, b, rel_tol=rel, abs_tol=rel), (a, b)


def verify_problem_1() -> None:
    m, L, g, h = 2.3, 1.7, 9.8, 1.2
    u = math.sqrt(2 * g * h)
    inertia = m * L**2 / 12 + (m / 3) * (L / 4) ** 2
    omega = (m / 3) * u * (L / 4) / inertia
    close(omega, 4 * u / (5 * L))
    r30 = L / 4 + 25 * L**2 / (128 * h)
    close(r30, L / 4 + g * math.sin(math.pi / 6) / (2 * omega**2))
    h_critical = 25 * L / 16
    close(L / 4 + 25 * L**2 / (128 * h_critical), 3 * L / 8)
    v_huang = 5 * math.sqrt(6 * g * h_critical) / 9
    close(v_huang, 25 * math.sqrt(6 * g * L) / 36)


def verify_problem_2() -> None:
    G, M, mass = 6.67e-11, 6.0e24, 1.0e4
    mu, r, v = G * M, 1.30e7, 6.5e3
    eps = v**2 / 2 - mu / r
    hs = r * v * math.sin(math.pi / 3)
    a = -mu / (2 * eps)
    p = hs**2 / mu
    e = math.sqrt(1 - p / a)
    rp, ra = a * (1 - e), a * (1 + e)
    close(rp + ra, 2 * a)
    close(rp * ra, a * p)
    period_h = 2 * math.pi * math.sqrt(a**3 / mu) / 3600
    assert 8.1 < period_h < 8.4
    vesc = math.sqrt(2 * mu / r)
    fuel = mass * (1 - math.exp(-(vesc - v) / 2.0e3))
    assert 4.8e3 < fuel < 5.0e3


def verify_problem_3() -> None:
    rho_m, rho_M, R = 2.5, 5.2, 3.0
    roche = R * (2 * rho_M / rho_m) ** (1 / 3)
    self_g = 4 * math.pi * rho_m / 3
    tide = 2 * (4 * math.pi * rho_M * R**3 / 3) / roche**3
    close(self_g, tide)
    M, M0, r0 = 2.0, 8.0e5, 7.0
    hill = r0 * (M / (3 * M0)) ** (1 / 3)
    close(M / hill**2, 3 * M0 * hill / r0**3)


def verify_problem_4() -> None:
    q, l, B, m, E = 1.1, 1.4, 0.8, 2.2, 3.0
    A, K, inertia = q**2 * l**2 * B**2 / m, q * l * E, m * l**2 / 12
    omega_sq = (A + K) / inertia
    close(omega_sq, 12 * (q**2 * l**2 * B**2 + m * q * l * E) / (m**2 * l**2))


def verify_problem_5() -> None:
    B, r, v0 = 0.7, 0.4, 1.3
    V, omega = 1.5 * v0, v0 / (2 * r)
    u_a = V + r * omega
    u_d = V - 3 * r * omega
    close(V, 3 * r * omega)
    close(u_d, 0.0)
    close(2 * v0 - u_a - u_d, 0.0)
    emf = 2 * B * r * v0 + 0.5 * B * omega * ((3 * r) ** 2 - r**2) - 4 * B * r * V
    close(emf, -2 * B * r * v0)


def verify_problem_6() -> None:
    V, chi0, alpha, C = 1.7, 0.4, 0.03, 5.0
    E1, E2, T1, T2 = 4.0, 1.5, 320.0, 280.0
    q1 = 0.5 * V * (chi0 + alpha * T1) * (E2**2 - E1**2)
    q2 = (C + alpha * V * E2**2) * (T2 - T1)
    q3 = 0.5 * V * (chi0 + alpha * T2) * (E1**2 - E2**2)
    q4 = (C + alpha * V * E1**2) * (T1 - T2)
    expected = 0.5 * alpha * V * (T1 - T2) * (E1**2 - E2**2)
    close(q1 + q2 + q3 + q4, expected)
    eta = expected / (q3 + q4)
    assert 0 < eta < 1


def verify_problem_7() -> None:
    n = 1.5
    r = (1 - n) / (1 + n)
    t_min = 1 - 4 * r**2 / (1 + r**2) ** 2
    close(t_min, ((1 - r**2) / (1 + r**2)) ** 2)
    assert 0 < t_min < 1


def verify_problem_8() -> None:
    beta = 0.82
    c = math.sqrt(1 - beta**2)
    close(c**2 + beta**2, 1.0)
    # The apparent horizontal coordinate is a unit projection.
    theta = -math.asin(beta)
    apparent = c * math.cos(theta) - beta * math.sin(theta)
    close(apparent, 1.0)


if __name__ == "__main__":
    verify_problem_1()
    verify_problem_2()
    verify_problem_3()
    verify_problem_4()
    verify_problem_5()
    verify_problem_6()
    verify_problem_7()
    verify_problem_8()
    print("蔡题098：8题关键结论数值与代数核验全部通过。")
