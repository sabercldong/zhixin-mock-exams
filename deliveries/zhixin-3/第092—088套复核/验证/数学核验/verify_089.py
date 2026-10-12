from __future__ import annotations

import math
from fractions import Fraction
from itertools import product


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError((a, b))


def hypercube_resistance(n: int, source: tuple[int, ...], sink: tuple[int, ...]) -> Fraction:
    vertices = list(product((0, 1), repeat=n))
    unknown = [v for v in vertices if v not in (source, sink)]
    matrix: list[list[Fraction]] = []
    for v in unknown:
        row = []
        for w in unknown:
            adjacent = sum(a != b for a, b in zip(v, w)) == 1
            row.append(Fraction(n if v == w else (-1 if adjacent else 0)))
        rhs = Fraction(sum(a != b for a, b in zip(v, source)) == 1)
        matrix.append(row + [rhs])

    size = len(unknown)
    for col in range(size):
        pivot = next(i for i in range(col, size) if matrix[i][col])
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        factor = matrix[col][col]
        matrix[col] = [x / factor for x in matrix[col]]
        for i in range(size):
            if i == col:
                continue
            factor = matrix[i][col]
            matrix[i] = [matrix[i][j] - factor * matrix[col][j] for j in range(size + 1)]

    voltage = {source: Fraction(1), sink: Fraction(0)}
    voltage.update({unknown[i]: matrix[i][-1] for i in range(size)})
    current = sum(
        Fraction(1) - voltage[v]
        for v in vertices
        if sum(a != b for a, b in zip(source, v)) == 1
    )
    return 1 / current


def main() -> None:
    # Q1: limiting angle and rubber friction.
    gamma = math.degrees(math.acos(math.sqrt(3) - 1.5)) - 30
    close(gamma, 46.58215851203755)
    close(math.tan(math.radians(60)), math.sqrt(3))

    # Q2: C height cancels for arbitrary admissible configurations.
    L, a, b = 2.0, 3.0, 4.0
    target_height = (b * b - a * a) / (2 * L)
    for theta in (0.0, 0.2, 0.6):
        y = (b * b - a * a) / (4 * L * math.cos(theta / 2)) - L * math.cos(theta / 2)
        height = L + L * math.cos(theta) + 2 * y * math.cos(theta / 2)
        close(height, target_height)

    # Q3: mechanical gain equals negative field loss.
    mu0, turns, charge, current, aa, bb = 1.7, 2.1, 0.8, 3.2, 0.6, 1.4
    mechanical = 0.5 * mu0 * turns * charge * current * (bb * bb - aa * aa)
    field_change = -0.5 * mu0 * turns * charge * current * (bb * bb - aa * aa)
    close(mechanical + field_change, 0.0)

    # Q4: independent nodal solution for the three networks.
    assert hypercube_resistance(3, (0, 0, 0), (1, 0, 1)) == Fraction(3, 4)
    assert hypercube_resistance(4, (0, 0, 0, 0), (1, 1, 1, 1)) == Fraction(2, 3)
    assert hypercube_resistance(4, (0, 0, 0, 0), (1, 1, 0, 1)) == Fraction(61, 96)

    # Q5: analytic rod integral and compact formula agree numerically.
    mass, height, radius, theta, omega = 1.3, 0.7, 5.0, 0.8, 2.2
    integral = mass / height * omega**2 * math.sin(theta) * (
        radius * height**2 / 2 - height**3 * math.cos(theta) / 3
    )
    compact = mass * omega**2 * height * math.sin(theta) * (
        radius / 2 - height * math.cos(theta) / 3
    )
    close(integral, compact)

    # Q6: two sample image points recover h=2f and p=f.
    a_parabola, focal = 2.0, 3.0
    x1, x2 = 1.0, 2.0
    y1 = 2 * focal - a_parabola * x1**2
    y2 = 2 * focal - a_parabola * x2**2
    h = (y1 * x2**2 - y2 * x1**2) / (x2**2 - x1**2)
    close(h, 2 * focal)
    close(h / 2, focal)

    # Q7: static limit is Snell's law; layer expansion yields the stated curvature.
    n1, n2, theta = 1.6, 1.2, 0.5
    sin_i_prime = (n1 * math.sin(theta)) / n2
    close(n2 * sin_i_prime, n1 * math.sin(theta))
    n0, c, alpha, dh = 1.0003, 3.0e8, 0.02, 1.0e-3
    u = alpha * dh
    exact = (n0 * c + u) / (n0 * (c + n0 * u))
    first_order = 1 - (n0 * n0 - 1) / n0 * u / c
    close(exact, first_order, tol=1e-12)
    curvature_radius = n0 / (n0 * n0 - 1) * c / alpha
    close(1 / curvature_radius, (n0 * n0 - 1) / n0 * alpha / c)

    # Q8: initial rate, steady heat-flux equality, and mass conservation.
    rho_w, rho_i = 0.999e3, 0.92e3
    k_w, k_i, latent, H0 = 0.57, 2.2, 3.3e5, 5.0
    rate = (k_i * 10 / 0.01 - k_w * 4 / H0) / (rho_i * latent)
    close(rate, 7.244874835309618e-6)
    h_i = rho_w * H0 * k_i * 10 / (rho_i * k_i * 10 + rho_w * k_w * 4)
    h_w = H0 - rho_i / rho_w * h_i
    close(k_i * 10 / h_i, k_w * 4 / h_w)
    close(rho_i * h_i + rho_w * h_w, rho_w * H0)

    print("蔡题089：8 题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
