from __future__ import annotations

import math


def close(a: float, b: float, rel: float = 1e-8) -> None:
    assert math.isclose(a, b, rel_tol=rel, abs_tol=rel), (a, b)


def verify_q1() -> None:
    inertia, a = 2.3, 4.1
    l0 = (3 * inertia * a**3) ** 0.25
    capital_l0 = 4 * l0 / 3
    close(inertia * a**3 / l0**3, l0 / 3)
    close(capital_l0, l0 + inertia * a**3 / l0**3)
    close(1 / inertia - 3 * a**3 / (1.1 * l0) ** 4 > 0, True)


def verify_q2() -> None:
    mu, n_turns, a, z = 1.7, 230, 0.02, 0.35
    mutual = mu * n_turns * math.pi * a**4 / (2 * z**3)
    close(mutual * 2 * z**3, mu * n_turns * math.pi * a**4)
    resistance, inductance, omega = 4.0, 0.02, 80.0
    phase = math.atan2(resistance, omega * inductance)
    close(math.sin(phase), resistance / math.hypot(resistance, omega * inductance))


def verify_q3() -> None:
    roots = [math.radians(63.919), math.radians(14.570)]
    expected = [1.85, 4.22]
    for theta, target in zip(roots, expected):
        d = math.sin(2 * theta) - 0.25
        tau = 1 / d
        residual = 1 + 2 * tau * math.cos(theta) ** 2 - 0.5 * tau**2
        assert abs(residual) < 2e-3
        close(tau, target, 3e-3)
    doppler = 250 * (10 - 1 / (4 * math.sqrt(2))) / (10 + 1 / math.sqrt(2))
    close(doppler, 229.0, 2e-3)


def omega0_pair(lam_i: float, n_i: float, lam_j: float, n_j: float,
                medium_wavelength: bool) -> float:
    c = 3.0e8
    wi = 2 * math.pi * c / (lam_i * (n_i if medium_wavelength else 1))
    wj = 2 * math.pi * c / (lam_j * (n_j if medium_wavelength else 1))
    ai = (n_i**2 - 1) / n_i**2
    aj = (n_j**2 - 1) / n_j**2
    return math.sqrt((ai * wi**2 - aj * wj**2) / (ai - aj))


def verify_q4() -> None:
    lam = [7.682e-7, 5.876e-7, 4.047e-7]
    n = [1.466, 1.471, 1.482]
    medium = [
        omega0_pair(lam[0], n[0], lam[1], n[1], True),
        omega0_pair(lam[0], n[0], lam[2], n[2], True),
        omega0_pair(lam[1], n[1], lam[2], n[2], True),
    ]
    vacuum = [
        omega0_pair(lam[0], n[0], lam[1], n[1], False),
        omega0_pair(lam[0], n[0], lam[2], n[2], False),
        omega0_pair(lam[1], n[1], lam[2], n[2], False),
    ]
    for value, target in zip(medium, [1.83e16, 1.97e16, 2.03e16]):
        close(value, target, 4e-3)
    for value, target in zip(vacuum, [2.71e16, 2.93e16, 3.03e16]):
        close(value, target, 4e-3)


def verify_q5() -> None:
    # Half-space angular integral: integral cos(theta)dOmega = pi.
    angular = 2 * math.pi * 0.5
    close(angular / (4 * math.pi), 0.25)
    # Isotropy gives <p_x^2>/p^2 = 1/3.
    close(sum([1 / 3, 1 / 3, 1 / 3]), 1)


def lc_parameters(dt: float) -> tuple[float, float]:
    f = 1000.0
    omega = 2 * math.pi * f
    inductance = 100 * math.tan(omega * dt) / (3 * omega)
    capacitance = 1 / (4 * omega**2 * inductance)
    return inductance, capacitance


def verify_q6() -> None:
    l_printed, c_printed = lc_parameters(19e-6)
    close(l_printed, 0.636359e-3, 2e-6)
    close(c_printed, 9.95126e-6, 2e-6)
    assert l_printed < 1e-3
    l_intended, c_intended = lc_parameters(190e-6)
    close(l_intended, 13.3993e-3, 2e-6)
    close(c_intended, 0.472604e-6, 2e-6)
    close(1 / (2 * math.pi * math.sqrt(l_intended * c_intended)), 2000)


def verify_q7() -> None:
    hbar, mass, length, g = 1.054e-34, 0.01, 0.1, 9.8
    growth = math.sqrt(3 * g / (2 * length))
    tmax = math.log(math.sqrt(mass * length**2 * growth / hbar)) / growth
    close(tmax, 2.94, 2e-2)
    width = 2 * 200e-9 * 4.00 / 0.064
    close(width, 25e-6)
    close(width * math.cos(math.radians(15)), 24.148e-6, 2e-4)


def verify_q8() -> None:
    flow = 5e-3 / 60
    speed = flow / (math.pi * (0.015)**2)
    close(flow, 8.333333333e-5)
    close(speed, 0.11789, 2e-4)
    rho, rc, ra = 1.06e3, 0.05, 0.015
    bend = rho * speed**2 * math.log((rc + ra) / (rc - ra))
    close(bend, 9.10, 4e-3)
    close((3 / 18), 1 / 6)
    k = (15 / 16) ** 0.25
    close(k, 0.984, 2e-4)
    close(1 / 16 + k**4, 1)
    close(1.25, 1 + 0.25)


def main() -> None:
    verify_q1()
    verify_q2()
    verify_q3()
    verify_q4()
    verify_q5()
    verify_q6()
    verify_q7()
    verify_q8()
    print("蔡题065：八题的代数、数值、量纲与双口径数据核验通过。")


if __name__ == "__main__":
    main()
