from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


def verify_q1() -> None:
    a0y, l0, l1 = 200.0, 2.0, 3.1
    force = a0y * (1.0 - l0 / l1)
    energy = a0y * ((l1 - l0) - l0 * math.log(l1 / l0))
    step = 1e-6
    ep = a0y * (((l1 + step) - l0) - l0 * math.log((l1 + step) / l0))
    em = a0y * (((l1 - step) - l0) - l0 * math.log((l1 - step) / l0))
    close((ep - em) / (2 * step), force, 1e-8)
    m, rope_mass, g = 2.0, 1.3, 9.8
    l2 = a0y * l0 / (rope_mass * g) * math.log(
        (a0y - m * g) / (a0y - (m + rope_mass) * g)
    )
    assert l2 > l0


def verify_q2() -> None:
    f = 0.27
    eps2 = (1 + 2 * f) / (1 - f)
    close((eps2 - 1) / (eps2 + 2), f)


def verify_q3() -> None:
    # r0 -> 0: old h=gt^2/8, swept-mass mode h=gt^2/14.
    ratio = math.sqrt((1 / 8) / (1 / 14))
    close(ratio, math.sqrt(7) / 2)


def verify_q4() -> None:
    f0, k, c, resistance = 5.0, 12.0, 0.8, 3.0
    gamma = c * c / resistance
    down = gamma / k * math.log(2)
    up = gamma / k * math.log(2)
    work = f0 * (f0 / (3 * k))
    p0 = work / (down + up)
    close(p0, f0 * f0 / (6 * gamma * math.log(2)))
    v0 = math.sqrt(p0 * resistance) / c
    close(v0, f0 * resistance / (math.sqrt(6 * math.log(2)) * c * c))


def verify_q5() -> None:
    atomic_u = 1.660e-27
    mu = 12.00 * 15.99 / (12.00 + 15.99) * atomic_u
    omega, depth, light_speed = 4.088e14, 1.780e-18, 2.998e8
    alpha = omega * math.sqrt(mu / (2 * depth))
    wavelength = 2 * math.pi * light_speed / omega
    close(alpha, 2.31e10, 3e-3)
    close(wavelength, 4.61e-6, 3e-3)


def verify_q6() -> None:
    n1, n2, incidence = 1.0, 1.5, math.radians(35)
    refraction = math.asin(n1 / n2 * math.sin(incidence))
    rp_angle = math.tan(incidence - refraction) / math.tan(incidence + refraction)
    rp_index = (
        n2 * math.cos(incidence) - n1 * math.cos(refraction)
    ) / (
        n2 * math.cos(incidence) + n1 * math.cos(refraction)
    )
    close(rp_angle, rp_index)


def currents(epsilon: float, r: float, rg: float, rx: float, r0: float):
    i1 = epsilon / (rx + rg + r + r0)
    i2 = epsilon / (rx + rg + r)
    parallel_c = rg * r0 / (rg + r0)
    total_c = epsilon / (rx + r + parallel_c)
    i3 = total_c * r0 / (rg + r0)
    x = rx + rg
    parallel_d = x * r0 / (x + r0)
    total_d = epsilon / (r + parallel_d)
    i4 = total_d * r0 / (x + r0)
    return i1, i2, i3, i4


def verify_q7() -> None:
    epsilon, r, rg, rx, r0 = 1.5, 1.0, 20.0, 100.0, 20.0
    i1, i2, i3, i4 = currents(epsilon, r, rg, rx, r0)
    total_s = i1 * r0 / (i2 - i1)
    recovered_e = r0 * i1 * i2 / (i2 - i1)
    close(total_s, rx + rg + r)
    close(recovered_e, epsilon)
    close(rg * rg - total_s * rg + r0 * (epsilon / i3 - total_s), 0)
    close(r * r - total_s * r + r0 * (epsilon / i4 - total_s), 0)


def verify_q8() -> None:
    m1, m2, r1, r2, g = 1.0, 2.0, 0.4, 0.6, 9.8
    theta0 = math.radians(30)
    inertia = m1 * r1 * r1 + m2 * r2 * r2
    omega0 = math.sqrt((m2 * r2 - m1 * r1) * g / (inertia * math.cos(theta0)))
    close(omega0, 3.21, 2e-3)
    theta_max = math.radians(61.6)
    lhs = 2 * math.sin(theta0) ** 4 / math.sin(theta_max) ** 2
    lhs -= math.cos(theta0) * math.cos(theta_max)
    rhs = 2 * math.sin(theta0) ** 2 - math.cos(theta0) ** 2
    close(lhs, rhs, 2e-3)


def main() -> None:
    verify_q1()
    verify_q2()
    verify_q3()
    verify_q4()
    verify_q5()
    verify_q6()
    verify_q7()
    verify_q8()
    print("蔡题066：八题的代数、数值、极限与等价式核验通过。")


if __name__ == "__main__":
    main()
