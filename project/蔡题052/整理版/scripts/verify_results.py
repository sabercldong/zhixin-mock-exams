#!/usr/bin/env python3
"""第052套八题关键方程、数值与边界条件的独立核验。"""

from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-8) -> None:
    if abs(a - b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError(f"{a} != {b}")


def bisect(fn, lo: float, hi: float, iterations: int = 100) -> float:
    flo = fn(lo)
    for _ in range(iterations):
        mid = (lo + hi) / 2
        fm = fn(mid)
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def q1() -> None:
    rho1, rho2, rho3, h, area, g = 1.20, 0.90, 0.60, 0.70, 0.40, 9.8
    x3 = h * (rho1 - rho2) / (rho1 - rho3)
    x1 = h - x3
    close(rho1 * x1 + rho3 * x3, rho2 * h)
    k = (rho1 - rho3) * area * g
    mass = rho2 * area * h
    period = 2 * math.pi * math.sqrt(mass / k)
    close(period, 2 * math.pi * math.sqrt(rho2 * h / (g * (rho1 - rho3))))
    if not 0 < x3 < h:
        raise AssertionError("第1题平衡位置超出圆柱")


def q2() -> None:
    mu, eb, mpi, hbarc, lam = 469.0, 2.22, 138.0, 197.3269804, 1.42991
    q = 2 * mu * eb / (mpi * mpi)
    fn = lambda x: q * x**3 + q * x**2 + x - 1
    x = bisect(fn, 0.0, 1.0)
    close(x, 0.852702, 2e-6)
    r = lam * x
    close(r, 1.21928, 2e-5)
    g2 = hbarc * hbarc * math.exp(x) / (mu * r * (1 + x))
    close(g2, 86.22, 3e-4)
    close(g2 / hbarc, 0.4369, 3e-4)
    energy = hbarc**2 / (2 * mu * r**2) - g2 * math.exp(-x) / r
    close(energy, -eb, 3e-5)


def q3() -> None:
    g, ta = 9.8, 3.1
    radius = g * ta**2 / (16 * math.pi**2)
    phi = 1.37
    x = radius * (phi + math.sin(phi))
    y = radius * (1 - math.cos(phi))
    arc = (ta / math.pi) * math.sqrt(g * y / 2)
    close(arc, 4 * radius * math.sin(phi / 2))
    close(arc * arc, 8 * radius * y)
    radius_c = g * ta**2 / (24 * math.pi**2)
    close(radius_c / radius, 2 / 3)
    r = 0.07
    x_track = radius_c * (phi + math.sin(phi)) + r * math.sin(phi / 2)
    y_track = radius_c * (1 - math.cos(phi)) + r * (1 - math.cos(phi / 2))
    if not x_track > x * 2 / 3 or not y_track > y * 2 / 3:
        raise AssertionError("第3题等时轨道偏置方向异常")


def q4() -> None:
    mass, radius, current, field = 0.8, 0.3, 1.7, 0.9
    inertia = mass * radius**2 / 2
    omega0 = math.sqrt(current * math.pi * radius**2 * field / inertia)
    period = 2 * math.pi / omega0
    close(period, math.sqrt(2 * math.pi * mass / (current * field)))
    theta, inductance = 0.6, 0.75
    dphi = math.pi * radius**2 * field * (1 - math.cos(theta))
    kinetic = current * dphi - dphi**2 / (2 * inductance)
    omega = math.sqrt(2 * kinetic / inertia)
    close(omega**2, 4 * (current * dphi - dphi**2 / (2 * inductance)) / (mass * radius**2))
    if not 0 < dphi < 2 * inductance * current:
        raise AssertionError("第4题隔离后的可达转角条件异常")


def q5() -> None:
    g, omega, radius, ell = 10.0, 10.0, 0.05, 0.10
    fn = lambda theta: g * math.tan(theta) - omega**2 * (1.5 * ell + radius * math.sin(theta) / 4)
    theta = bisect(fn, 0.01, 1.45)
    close(math.degrees(theta), 58.0927, 2e-5)
    wx = -omega * (ell / radius + math.sin(theta)) * math.cos(theta)
    wy = omega * (math.cos(theta) ** 2 - (ell / radius) * math.sin(theta))
    close(wx, -15.06, 3e-3)
    close(wy, -14.18, 3e-3)
    close(omega**2 * ell / g, 1.0)


def q6() -> None:
    spacing, alpha, wavelength = 1e-3, math.radians(35), 550e-9
    delta_approx = wavelength / (spacing * math.sin(alpha))
    beta = math.acos(math.cos(alpha) + wavelength / spacing)
    delta_exact = abs(beta - alpha)
    if abs(delta_exact / delta_approx - 1) > 2e-3:
        raise AssertionError("第6题小角近似与精确光栅方程不相符")
    close(spacing, 1e-3)


def q7() -> None:
    year, au, msun = 365.25 * 86400, 1.495978707e11, 1.98847e30
    period = 3.44 * year
    v1, v2 = 2.998e8 * 5.20e-6, 2.998e8 * 6.24e-5
    vrel = v1 + v2
    close(vrel, 20266.5, 5e-6)
    rs = vrel * 8.5 * 3600 / 2
    rb = vrel * (25.08 - 8.50) * 3600 / 2
    close(rs / rb, math.sqrt(0.04 / 0.153), 3e-3)
    a = vrel * period / (2 * math.pi)
    total_mass = 4 * math.pi**2 * a**3 / (6.67430e-11 * period**2)
    close(a / au, 2.341, 8e-4)
    close(total_mass / msun, 1.084, 2e-3)
    close(total_mass * v2 / vrel / msun, 1.001, 2e-3)
    close(total_mass * v1 / vrel / msun, 0.0834, 2e-3)
    luminosity = 4.1829e28
    sigma = 5.670374419e-8
    ts = (0.847 * luminosity / (4 * math.pi * rs**2 * sigma)) ** 0.25
    tb = (0.153 * luminosity / (4 * math.pi * rb**2 * sigma)) ** 0.25
    close(ts, 2.68e4, 4e-3)
    close(tb, 1.25e4, 5e-3)
    rdust = math.sqrt(luminosity / (16 * math.pi * sigma * 300**4))
    close(rdust / au, 8.998, 8e-4)


def q8() -> None:
    n, ell, alpha = 5.0, 3.0, 1 / 137.035999084
    eccentricity = math.sqrt(1 - ell**2 / n**2)
    a = n**2
    rmin, rmax = a * (1 - eccentricity), a * (1 + eccentricity)
    close(rmin + rmax, 2 * a)
    close(rmin * rmax, n**2 * ell**2)
    close(a * a * (1 - eccentricity**2), n**2 * ell**2)
    close(1 / alpha**2, 1.8779e4, 2e-4)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 052 套八题的关键方程、数值与边界条件验证通过")


if __name__ == "__main__":
    main()
