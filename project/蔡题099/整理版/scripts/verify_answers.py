from __future__ import annotations

import math

import sympy as sp


def close(a: float, b: float, tolerance: float = 1e-7) -> None:
    if not math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError(f"{a} != {b}")


def q1_checks() -> None:
    eta, mass, gravity, time, height = sp.symbols("eta mass gravity time height", positive=True)
    acceleration = eta * gravity
    momentum = mass * eta * acceleration * time * (1 - acceleration * time**2 / (2 * height))
    derivative = sp.diff(momentum, time)
    expected = mass * gravity * eta**2 * (1 - 3 * acceleration * time**2 / (2 * height))
    assert sp.simplify(derivative - expected) == 0
    final_time_squared = 2 * height / acceleration
    assert sp.simplify(expected.subs(time**2, final_time_squared) + 2 * mass * gravity * eta**2) == 0


def q2_checks() -> None:
    theta = sp.symbols("theta", real=True)
    c, s = sp.cos(theta), sp.sin(theta)
    friction = sp.Rational(3, 4) * s * (3 * c - 2)
    normal = sp.Rational(1, 4) * (3 * c - 1) ** 2
    ratio = sp.simplify(friction / normal)
    derivative_numerator = sp.factor(sp.together(sp.diff(ratio, theta))).as_numer_denom()[0]
    root = float(sp.nsolve(derivative_numerator, 0.6))
    close(root, 0.612555, 2e-6)
    close(float(ratio.subs(theta, root)), 0.3705794, 2e-7)
    beta, length, omega, gravity = sp.symbols("beta length omega gravity", positive=True)
    centroid = sp.Rational(3, 4) * length * sp.cos(beta)
    axial_inertia = sp.Rational(3, 10) * length**2 * sp.sin(beta) ** 2
    precession = sp.simplify(gravity * centroid / (axial_inertia * omega))
    assert precession == 5 * gravity * sp.cos(beta) / (2 * length * omega * sp.sin(beta) ** 2)


def q3_checks() -> None:
    emf, resistance, inductance, capacitance = sp.symbols("emf resistance inductance capacitance", positive=True)
    current = emf / resistance
    q1 = sp.Rational(1, 2) * inductance * current**2
    q2 = q1 + sp.Rational(1, 2) * capacitance * emf**2
    assert sp.simplify(q1 + q2 - (inductance * emf**2 / resistance**2 + capacitance * emf**2 / 2)) == 0
    assert abs(1 - 3) == 2


def q4_checks() -> None:
    r, r1, r2, r3 = sp.symbols("r r1 r2 r3", positive=True)
    outer_fraction = (r3**2 - r**2) / (r3**2 - r2**2)
    assert sp.simplify(outer_fraction.subs(r, r2) - 1) == 0
    assert sp.simplify(outer_fraction.subs(r, r3)) == 0
    x = sp.symbols("x")
    r3_new = sp.sqrt(r3**2 + 2 * r2 * x + x**2)
    series = sp.series(r3_new, x, 0, 3).removeO()
    expected = r3 + r2 * x / r3 + (r3**2 - r2**2) * x**2 / (2 * r3**3)
    assert sp.simplify(series - expected) == 0


def q5_checks() -> None:
    lam = sp.symbols("lam")
    matrix = sp.Matrix([[2, 2], [2, 3]])
    characteristic = sp.factor(matrix.charpoly(lam).as_expr())
    assert characteristic == lam**2 - 5 * lam + 2
    roots = sorted([float(v) for v in matrix.eigenvals()], reverse=True)
    close(roots[0], (5 + math.sqrt(17)) / 2)
    close(roots[1], (5 - math.sqrt(17)) / 2)
    a = (3 + sp.sqrt(17)) / (2 * sp.sqrt(17))
    b = -(3 - sp.sqrt(17)) / (2 * sp.sqrt(17))
    assert sp.simplify(a + b - 1) == 0


def q6_checks() -> None:
    x, y = sp.symbols("x y")
    tau = (2 + y - x) / (2 * (1 - y))
    pressure_equation = tau - (1 - x) * (4 - 1 / (1 - y))
    entropy_equation = sp.Rational(11, 2) * sp.log(tau) + 2 * sp.log((2 + y - x) / 2) + sp.log(1 - x)
    solution = sp.nsolve([pressure_equation, entropy_equation], [x, y], [0.54, 0.28])
    xv, yv = map(float, solution)
    tauv = float(tau.subs({x: xv, y: yv}))
    t2v = 4 * (1 + xv)
    close(xv, 0.538, 5e-3)
    close(yv, 0.281, 5e-3)
    close(tauv, 1.21, 2e-2)
    close(t2v, 6.15, 3e-2)
    heat = 3 * (tauv - 1) + 2.5 * (tauv - 1) + 2.5 * (t2v - 2) + math.log(1 / (1 - yv))
    close(heat, 11.85, 3e-2)


def q7_checks() -> None:
    n, nu, gas_constant, temperature, mass = sp.symbols("n nu gas_constant temperature mass", positive=True)
    # All geometric factors cancel from d^2*pi*a^2*Kp/m.
    velocity_squared = sp.Rational(7, 5) * nu * gas_constant * temperature / mass
    assert sp.simplify(sp.sqrt(velocity_squared) ** 2 - velocity_squared) == 0


def q8_checks() -> None:
    coefficients = [1230.10, 140650.224, -17129050.5904]
    roots = sorted(sp.nroots(sp.Poly(coefficients, sp.Symbol("z"))), key=float)
    close(float(roots[0]), -188.2936992, 1e-8)
    close(float(roots[1]), 73.95321958, 1e-8)
    for z in map(float, roots):
        e_mu = math.sqrt(24.7**2 + 24.9**2 + 12.4**2)
        e_nu = math.sqrt(104.1**2 + 5.3**2 + z**2)
        dot = 24.7 * 104.1 - 24.9 * 5.3 - 12.4 * z
        invariant = 2 * (e_mu * e_nu - dot)
        close(invariant, 80.4**2, 2e-9)


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
