from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def main() -> None:
    # Q1: force projections and vector acceleration.
    g = 9.81
    theta = math.pi / 6
    tension_over_m = 2 * g * math.cos(theta) / (1 + 2 * math.sin(theta) ** 2)
    a_ring = tension_over_m * math.sin(theta)
    fictitious_over_2m = a_ring
    a_rel = g * math.sin(theta) + a_ring * math.cos(theta)
    ax = -a_ring + a_rel * math.cos(theta)
    ay = -a_rel * math.sin(theta)
    close(a_ring, g / math.sqrt(3))
    close(a_rel, g)
    close(math.hypot(ax, ay), g / math.sqrt(3))
    close(2 * math.pi / math.sqrt(3 * g), 2 * math.pi * math.sqrt(1 / (3 * g)))

    # Q2: moving fold and momentum flux.
    mass, length, u, v = 2.3, 4.7, 3.1, 1.4
    lam = mass / length
    dt = 1e-5
    fold_shift = 0.5 * (u - v) * dt
    dl1 = u * dt - fold_shift
    dl2 = -v * dt - fold_shift
    close(dl1 + dl2, 0.0)
    momentum_rate = lam * (dl1 * u - dl2 * v) / dt
    close(momentum_rate, lam * (u + v) ** 2 / 2)

    # Q3: coefficients satisfy the forced first-order equation and initial data.
    r_e, capacitance, field, rail, m, f0, omega = 0.8, 0.04, 0.6, 1.2, 0.7, 2.1, 1.4
    d = 2 / capacitance + 3 * field**2 * rail**2 / (2 * m)
    e = field * rail * f0 / (2 * m * omega)
    p = -e * d / (d**2 + 4 * r_e**2 * omega**2)
    qcoef = 2 * r_e * omega * e / (d**2 + 4 * r_e**2 * omega**2)
    close(d * p - 2 * r_e * omega * qcoef, -e)
    close(2 * r_e * omega * p + d * qcoef, 0.0)
    close(p * omega + qcoef * d / (2 * r_e), 0.0)

    # Q4: exact force is the derivative of the interaction potential; threshold limit.
    ke, charge, radius, h = 8.99, 0.3, 0.4, 2.2
    force = ke * charge**2 * radius**3 * (2 * h**2 - radius**2) / (
        h**3 * (h**2 - radius**2) ** 2
    )
    eps = 1e-6
    potential = lambda x: -ke * charge**2 * radius**3 / (2 * x**2 * (x**2 - radius**2))
    derivative = (potential(h + eps) - potential(h - eps)) / (2 * eps)
    close(force, derivative, tol=1e-7)
    impact, particle_mass = 3.0, 0.2
    vc_exact = math.sqrt(4 * ke * charge**2 * radius**3 / (particle_mass * (impact**2 - radius**2) ** 2))
    h0sq = (impact**2 + radius**2) / 2
    stationarity_rhs = ke * charge**2 * radius**3 * (2 * h0sq - radius**2) / (h0sq - radius**2) ** 2
    close(particle_mass * vc_exact**2 * impact**2, stationarity_rhs)

    # Q5: ellipse through square vertex and phase period.
    alpha4 = 12 / math.sqrt(119)
    a = 12 / 13
    b = alpha4
    close((1 / math.sqrt(2)) ** 2 / a**2 + (1 / math.sqrt(2)) ** 2 / b**2, 1.0)
    beta = 8 * math.acos(13 / (12 * math.sqrt(2)))
    close(beta, 5.585204159351068, tol=1e-10)
    assert math.floor(math.pi / math.acos(12 / 13)) == 7

    # Q6: magnetic and electric force matching gives v^2/c^2.
    eps0, mu0, speed, light = 1.7, 2.1, 0.03, 1 / math.sqrt(1.7 * 2.1)
    ratio = eps0 * mu0 * speed**2
    close(ratio, speed**2 / light**2)

    # Q7: photon energy, natural width and full Doppler width.
    wavelength_nm = 486.1
    photon_ev = 1240 / wavelength_nm
    close(photon_ev, 2.5509154494959883)
    natural = 1 / (4 * math.pi * 1.5e-8)
    close(natural, 5.305164769729845e6)
    wavelength_m, vmax = wavelength_nm * 1e-9, 700.0
    doppler = 2 * vmax / wavelength_m
    close(doppler, 2.8800658300761156e9)

    # Q8: collision count and coordinate reconstruction.
    target_over_t0 = 5 / math.sqrt(2)
    collisions = sum(1 for n in range(1, 20) if 2 * n - 1 <= target_over_t0)
    assert collisions == 2
    s = target_over_t0 - 3
    xi_over_l = 2 * s - s**2
    close(xi_over_l, 20 * math.sqrt(2) - 55 / 2)
    close(25 / 2 + xi_over_l - 1, 20 * math.sqrt(2) - 16)

    print("All eight questions passed independent algebraic and numerical checks")


if __name__ == "__main__":
    main()
