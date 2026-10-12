from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 1e-9, abs_tol: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol):
        raise AssertionError(f"{actual=} differs from {expected=}")


def q1() -> None:
    g = 9.8
    l = 2.4
    v02 = 3.0 * g * l
    v2 = 0.5 * v02 - g * l
    tension = 4.0 * v2 / l - g
    normal_per_mass = g - tension
    close(normal_per_mass, 0.0, abs_tol=1e-12)
    rho = v2 / (4.0 * v2 / l)
    close(rho, l / 4.0)

    beta = 4.0
    s = (beta - math.sqrt(beta * beta - 8.0)) / 2.0
    close(s * s - beta * s + 2.0, 0.0, abs_tol=1e-12)
    wc2 = 2.0 * g * l / s
    assert wc2 > 0.0


def q2() -> None:
    d = 15.0 * math.sqrt(3.0) - 2.0 * math.pi
    area = d / 9.0
    close(area, 2.1886196451503968)
    r0, resistance = 2.3, 1.7
    emf = area
    current = 2.0 * emf / (3.0 * (2.0 * r0 + resistance))
    lhs = emf
    rhs = 2.0 * r0 * current + 0.5 * current * (3.0 * resistance + 2.0 * r0)
    close(lhs, rhs)
    close(-2.0 * current * r0, -2.0 * (current * r0))


def q3() -> None:
    r = 7.0
    close(2.0 * r / 4.0, r / 2.0)
    close(2.0 * r * (1.0 / 4.0 + 1.0 / 12.0), 2.0 * r / 3.0)


def q4() -> None:
    magnetic, speed, lam, k, time = 1.3, 2.2, 0.8, 0.7, 1.6
    length = 2.0 * math.sqrt(speed * time / k)
    emf = magnetic * length * speed
    resistance = lam * length
    current = emf / resistance
    close(current, magnetic * speed / lam)
    power_force = magnetic * current * length * speed
    power_joule = current * current * resistance
    close(power_force, power_joule)


def q5() -> None:
    v0, g, h0 = 2.0, 9.8, 0.192
    alpha = math.acos(math.sqrt((v0 * v0 + 2.0 * g * h0) / (2.0 * v0 * v0 + 2.0 * g * h0)))
    close(math.degrees(alpha), 35.67116975793707)
    range_max = v0 * math.sqrt(v0 * v0 + 2.0 * g * h0) / g
    close(range_max, 0.5686228495434448)

    rho, h, eta, length, radius = 922.0, 0.18, 4.04e-3, 0.20, 1.0e-3
    p1 = 0.5 * rho * v0 * v0 - rho * g * h
    p2 = 4.0 * eta * length * v0 / radius**2 - rho * g * h
    close(p1, 217.5920000000001)
    close(p2, 4837.592000000001)
    flow = 0.5 * math.pi * radius**2 * v0
    close(flow, math.pi * 1.0e-6)

    volume_ratio, n = 129.0, 0.587
    delta = n ** (-0.4) - (n + 1.0 / (2.0 * volume_ratio)) ** (-0.4)
    coefficient = math.sqrt(10.0 * volume_ratio * delta - 2.0)
    close(coefficient, 1.4822158863179284)


def q6() -> None:
    steps = 20000
    start, end = 0.0, math.pi / 2.0
    width = (end - start) / steps

    def integrand(u: float) -> float:
        return 2.0 / (1.0 + 3.0 * math.sin(u) ** 2)

    total = integrand(start) + integrand(end)
    for index in range(1, steps):
        total += (4.0 if index % 2 else 2.0) * integrand(start + index * width)
    total *= width / 3.0
    close(total, math.pi / 2.0, rel=1e-11)


def q7() -> None:
    gravitational = 6.67e-11
    m1 = 1.29e22
    r1 = 2.30e6
    period = 6.387 * 86400.0
    separation = 1.974e7
    r2 = 6.03e5
    omega = 2.0 * math.pi / period
    m2_exact = omega**2 * separation**3 / gravitational - m1
    close(m2_exact, 2.0504419327123705e21, rel=1e-12)

    m2 = 2.1e21
    moved = 1.0e10
    total_mass = m1 + m2
    reduced = m1 * m2 / total_mass
    energy_change = moved * (
        gravitational * m1 / r1
        - gravitational * m1 / separation
        - gravitational * m2 / r2
        + gravitational * m2 / separation
        + 0.5 * omega**2 * separation**2 * m2 / total_mass
        - 0.5 * omega**2 * separation**2 * m1 / total_mass
    )
    energy = -gravitational * total_mass * reduced / (2.0 * separation)
    dmu = moved * (1.0 / m2 - 1.0 / m1)
    da = -energy_change / energy + dmu
    dperiod = 1.5 * period * da
    db = -0.5 * (dmu + energy_change / energy)
    dmean = separation * db
    close(dperiod, 1.9058979098115564e-5, rel=1e-12)
    close(dmean, 1.485580694274027e-4, rel=1e-12)


def q8() -> None:
    for reflectivity in (0.0, 0.2, 0.8, 1.0):
        momentum_factor = 2.0 * reflectivity / (3.0 * (2.0 - reflectivity))
        kinetic_factor = momentum_factor**2 / 2.0
        expected = 2.0 * reflectivity**2 / (9.0 * (2.0 - reflectivity) ** 2)
        close(kinetic_factor, expected)
    close(2.0 * 0.0**2 / (9.0 * 2.0**2), 0.0)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("蔡题087：8题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
