from __future__ import annotations

import math

import sympy as sp


def close(a: float, b: float, tolerance: float = 1e-8) -> None:
    if not math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError(f"{a} != {b}")


def q1_checks() -> None:
    c = sp.symbols("c", positive=True)
    v2 = sp.simplify(sp.Rational(1, 2) * (1 + c) / c)
    assert sp.simplify(v2 - (1 + c) / (2 * c)) == 0
    assert sp.simplify(1 + c - 2 * c**2 + (c - 1) * (2 * c + 1)) == 0


def q2_checks() -> None:
    lam, x0, length, y0 = sp.symbols("lam x0 length y0", positive=True)
    expression = (x0**2 - 2 * length * y0) * (1 + lam**2) / (
        2 * x0 * lam - length * lam**2 - 2 * y0
    )
    numerator = sp.factor(sp.together(sp.diff(expression, lam))).as_numer_denom()[0]
    expected = 2 * (x0**2 - 2 * length * y0) * (
        x0 * lam**2 + (length - 2 * y0) * lam - x0
    )
    assert sp.simplify(numerator - expected) == 0


def q3_checks() -> None:
    l, radius = sp.symbols("l radius", positive=True)
    a = radius + sp.Rational(5, 4) * l
    s0 = radius + l / 4
    d0 = sp.expand(s0**2 - radius**2)
    assert sp.simplify(d0 - (l**2 / 16 + l * radius / 2)) == 0
    assert sp.expand(a * l) == l * radius + sp.Rational(5, 4) * l**2


def q4_checks() -> None:
    matrix = sp.Matrix([[12, -4, 0, -8], [-2, 6, -2, 0], [0, -1, 4, -1], [-4, 0, -2, 10]])
    vector = sp.Matrix([8, 0, 0, 4])
    solution = matrix.LUsolve(vector)
    assert solution == sp.Matrix([sp.Rational(150, 89), sp.Rational(64, 89), sp.Rational(42, 89), sp.Rational(104, 89)])
    assert 2 * solution[1] + 2 * solution[2] + 4 * solution[3] == sp.Rational(628, 89)


def q5_checks() -> None:
    b, l, inductance, mass = sp.symbols("b l inductance mass", positive=True)
    omega2 = b**2 * l**2 / (2 * mass * inductance)
    equilibrium = sp.simplify(-(b * l / mass) / omega2)
    assert equilibrium == -2 * inductance / (b * l)


def q6_checks() -> None:
    gravity = 6.7e-11
    mass = 2.0e30
    radius = 7.0e8
    sigma = 5.7e-8
    temperature = 6000.0
    heat_capacity = 1.0e3
    energy = 3 * gravity * mass**2 / (5 * radius)
    power = 4 * math.pi * radius**2 * sigma * temperature**4
    close(energy, 2.297142857142857e41, 1e-12)
    close(energy / power, 5.050125875515028e14, 1e-12)
    stellar_temperature = energy / (mass * heat_capacity)
    close(stellar_temperature, 1.1485714285714285e8, 1e-12)
    close((2.0e7 / stellar_temperature) ** 1.5, 0.07266210588694781, 1e-12)


def q7_checks() -> None:
    x, y, lagrange = sp.symbols("x y lagrange", positive=True)
    solutions = sp.nsolve(
        [4 * x * (x - 2) + 3 * (y - 2), (x - 2) ** 2 + (y - 2) ** 2 - 1],
        [x, y],
        [1.57, 2.90],
    )
    x_value, y_value = map(float, solutions)
    volume_ratio = math.exp(2 * (y_value - 1) - 1.5 * math.log(x_value))
    close(x_value, 1.568, 5e-4)
    close(y_value, 2.902, 5e-4)
    close(volume_ratio, 22.85, 5e-3)


def q8_checks() -> None:
    z, b = sp.symbols("z b", positive=True)
    integral = sp.integrate(1 / (b**2 + z**2) ** sp.Rational(3, 2), (z, -sp.oo, sp.oo))
    assert integral == 2 / b**2


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
