from __future__ import annotations

import math

import sympy as sp


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def q1_checks() -> None:
    x = sp.symbols("x", positive=True)
    tangent = 3 / (1 / x + 4 * x)
    critical = sp.solve(sp.diff(tangent, x), x)
    assert critical == [sp.Rational(1, 2)]
    assert sp.simplify(tangent.subs(x, critical[0])) == sp.Rational(3, 4)
    close(math.sin(math.asin(1 / 5)), 1 / 5)


def q2_checks() -> None:
    c = sp.symbols("c", real=True)
    s2 = 1 - c**2
    d = 9 - 2 * c**2
    w2 = 12 * (1 - c) / d
    dd = 6 * sp.sqrt(s2) * (9 + 2 * c**2 - 4 * c) / d**2
    a = sp.simplify((c * dd - sp.sqrt(s2) * w2) / 3)
    expected_a = -2 * sp.sqrt(s2) * (2 * c**3 - 27 * c + 18) / d**2
    assert sp.simplify(a - expected_a) == 0

    normal = sp.simplify(c - w2 - a * sp.sqrt(s2))
    expected_n = (-2 * c**3 - 12 * c**2 + 135 * c - 72) / d**2
    assert sp.simplify(normal - expected_n) == 0
    roots = [complex(root) for root in sp.nroots(2 * c**3 + 12 * c**2 - 135 * c + 72)]
    physical = [root.real for root in roots if abs(root.imag) < 1e-12 and 0 < root.real < 1]
    assert len(physical) == 1
    close(physical[0], 0.564300828511741, 1e-12)

    friction = sp.simplify(sp.sqrt(s2) + a * c - dd)
    expected_f = 3 * sp.sqrt(s2) * (2 * c**2 - 4 * c + 9) / d**2
    assert sp.simplify(friction - expected_f) == 0


def q3_checks() -> None:
    x, y, z, r, lam, eps = sp.symbols("x y z r lam eps", nonzero=True)
    phi = lam / eps * (
        sp.Rational(1, 4)
        - y / (4 * sp.pi * r)
        + (sp.pi * (x**2 + y**2 - 2 * z**2) - 3 * x * y)
        / (16 * sp.pi * r**2)
    )
    field = [-sp.diff(phi, variable) for variable in (x, y, z)]
    assert sp.simplify(field[0] - lam / eps * (3 * y - 2 * sp.pi * x) / (16 * sp.pi * r**2)) == 0
    assert sp.simplify(field[1] - lam / eps * (1 / (4 * sp.pi * r) + (3 * x - 2 * sp.pi * y) / (16 * sp.pi * r**2))) == 0
    assert sp.simplify(field[2] - lam / eps * z / (4 * r**2)) == 0


def q4_checks() -> None:
    theta = sp.symbols("theta", real=True)
    assert sp.integrate(sp.sin(theta) ** 3, (theta, 0, sp.pi)) == sp.Rational(4, 3)
    c = sp.symbols("c", positive=True)
    assert sp.simplify(1 / (sp.Symbol("mu0") * sp.Symbol("eps0")) - c**2) != 0


def q5_checks() -> None:
    theta = sp.symbols("theta", real=True)
    x = 3 * sp.cos(theta) + sp.cos(3 * theta)
    y = 3 * sp.sin(theta) + sp.sin(3 * theta)
    arg_derivative = sp.simplify((x * sp.diff(y, theta) - y * sp.diff(x, theta)) / (x**2 + y**2))
    expected = 6 * (1 + sp.cos(2 * theta)) / (5 + 3 * sp.cos(2 * theta))
    assert sp.trigsimp(arg_derivative - expected) == 0

    omega_sq = sp.Symbol("a", positive=True) * (theta + sp.sin(theta))
    assert sp.simplify(omega_sq.subs(theta, sp.pi) - sp.pi * sp.Symbol("a", positive=True)) == 0


def q6_checks() -> None:
    gas_constant = 8.31
    temperature = 373.0
    pressure = 1.01e5
    v1 = gas_constant * temperature / pressure
    close(v1, 0.030681, 1e-4)
    gamma = 15 / 11
    partial = 0.5 * pressure * (0.5**gamma)
    close(partial, 1.9636e4, 2e-3)
    heat = 1.5 * gas_constant * temperature * math.log(2) + 0.0045 * 2.26e5
    close(heat, 4.239e3, 2e-3)


def q7_checks() -> None:
    beta, time, radius, c = sp.symbols("beta time radius c", positive=True)
    psi = beta * c * time / radius
    gamma = 1 / sp.sqrt(1 - beta**2)
    tb = (time - beta * radius * sp.sin(psi) / c) / (gamma * (1 - beta**2 * sp.cos(psi)))
    assert sp.simplify(tb.subs(time, 0)) == 0
    assert sp.limit(tb, beta, 0) == time


def q8_checks() -> None:
    photon = 100.0
    nucleus = 3932.0
    electron = 0.51
    total = nucleus + photon
    beta_c = photon / total
    gamma_c = 1 / math.sqrt(1 - beta_c**2)
    s = total**2 - photon**2
    root_s = math.sqrt(s)
    p_star = math.sqrt(
        (s - (nucleus + 2 * electron) ** 2)
        * (s - (nucleus - 2 * electron) ** 2)
    ) / (2 * root_s)
    energy_n_star = math.sqrt(nucleus**2 + p_star**2)
    beta_star = p_star / energy_n_star
    beta_min = (beta_c - beta_star) / (1 - beta_c * beta_star)
    p_min = nucleus * beta_min / math.sqrt(1 - beta_min**2)
    close(p_min, 0.005202138752552412, 1e-10)

    cos_star = -p_star / (beta_c * energy_n_star)
    sin_star = math.sqrt(1 - cos_star**2)
    px = gamma_c * (p_star * cos_star + beta_c * energy_n_star)
    py = p_star * sin_star
    theta_max = math.degrees(math.atan2(py, px))
    close(theta_max, 89.40818764125258, 1e-10)


def main() -> None:
    q1_checks()
    q2_checks()
    q3_checks()
    q4_checks()
    q5_checks()
    q6_checks()
    q7_checks()
    q8_checks()
    print("Q1-Q8 symbolic and numerical checks passed")


if __name__ == "__main__":
    main()
