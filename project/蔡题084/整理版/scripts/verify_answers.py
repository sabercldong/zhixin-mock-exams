from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 1e-9, abs_tol: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol):
        raise AssertionError(f"{actual=} differs from {expected=}")


def solve_linear(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Small Gaussian elimination routine used to keep the audit self-contained."""
    n = len(vector)
    aug = [row[:] + [rhs] for row, rhs in zip(matrix, vector)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(aug[i][col]))
        if abs(aug[pivot][col]) < 1e-14:
            raise AssertionError("singular audit matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def q1() -> None:
    rho0, rho, alpha, length, gravity = 1000.0, 900.0, 0.5, 0.12, 9.8
    volume = length**3
    volume0 = volume * (2 * rho - 3 * alpha * rho0) / rho0
    assert volume0 > 0 and rho > alpha * rho0

    inertia = 2 * rho * volume + 0.5 * rho0 * volume0
    stiffness = 4.5 * rho0 * length**2 * gravity
    omega2_direct = stiffness / inertia
    omega2_closed = 3 * rho0 * gravity / ((2 * rho - alpha * rho0) * length)
    close(omega2_direct, omega2_closed)
    period = 2 * math.pi / math.sqrt(omega2_direct)
    close(period, 2 * math.pi * math.sqrt((2 * rho - alpha * rho0) * length / (3 * rho0 * gravity)))


def octahedron_edges() -> list[tuple[int, int]]:
    opposite = {frozenset((0, 1)), frozenset((2, 3)), frozenset((4, 5))}
    return [
        (i, j)
        for i in range(6)
        for j in range(i + 1, 6)
        if frozenset((i, j)) not in opposite
    ]


def network_voltage(injection: list[float], resistance: float = 1.0, ground: int = 1) -> list[float]:
    edges = octahedron_edges()
    unknown = [i for i in range(6) if i != ground]
    index = {node: k for k, node in enumerate(unknown)}
    matrix = [[0.0] * len(unknown) for _ in unknown]
    rhs = [injection[node] for node in unknown]
    conductance = 1.0 / resistance
    for i, j in edges:
        if i != ground:
            matrix[index[i]][index[i]] += conductance
        if j != ground:
            matrix[index[j]][index[j]] += conductance
        if i != ground and j != ground:
            matrix[index[i]][index[j]] -= conductance
            matrix[index[j]][index[i]] -= conductance
    values = solve_linear(matrix, rhs)
    voltage = [0.0] * 6
    for node, value in zip(unknown, values):
        voltage[node] = value
    return voltage


def q2() -> None:
    assert len(octahedron_edges()) == 12
    resistance = 3.7
    vab = network_voltage([1, -1, 0, 0, 0, 0], resistance)
    close(vab[0] - vab[1], resistance / 2)

    vac = network_voltage([1, 0, -1, 0, 0, 0], resistance, ground=2)
    close(vac[0] - vac[2], 5 * resistance / 12)

    current = 2.3
    three_terminal = network_voltage([current, -3 * current, 2 * current, 0, 0, 0], resistance)
    close(three_terminal[0] - three_terminal[3], 5 * current * resistance / 12)


def first_order_derivative(function, step: float = 1e-6) -> float:
    return (function(step) - function(-step)) / (2 * step)


def q3() -> None:
    # Check the 90-degree result against the unexpanded spherical-refraction recurrence.
    n = 1.61

    def exact_h(eps: float) -> float:
        # l is used as the length unit and R/l=1/eps.
        oc = 1 / math.sqrt(2) + eps / 4
        sc = math.sqrt(2) - oc
        v1 = n / ((n - 1) * eps - 1 / sc)
        u4 = 2 * oc - v1
        v4 = 1 / ((n - 1) * eps - n / u4)
        return oc + v4

    h0 = -math.sqrt(2) / n
    h1 = -(n - 1) * (2 * n**2 + 3 * n + 4) / (2 * n**2)
    close(exact_h(0.0), h0)
    close(first_order_derivative(exact_h), h1, rel=2e-7)

    # Check all compact coefficients used for the 120-degree answer.
    a = math.sqrt(2) - 0.5
    q = (n - 1) * a - 3 / (8 * a)
    b0, b1 = 0.5 + n * a, 3 / 8 + n * a * q
    u0, u1 = 0.75 + n * a / 2, 9 / 16 + n * a * q / 2
    y0, y1 = math.sqrt(3) * b0 / 2, math.sqrt(3) * b1 / 2
    assert all(math.isfinite(x) for x in (q, b0, b1, u0, u1, y0, y1))

    def exact_120(eps: float) -> tuple[float, float]:
        oc = 0.5 + 3 * eps / 8
        sc = math.sqrt(2) - oc
        v1 = n / ((n - 1) * eps - 1 / sc)
        os2 = oc - v1
        u3 = oc + os2 / 2
        y3 = math.sqrt(3) * os2 / 2
        v3 = 1 / ((n - 1) * eps - n / u3)
        beta = -n * v3 / u3
        return oc + v3, beta * y3

    h0_120 = 0.5 - u0 / n
    h1_120 = 3 / 8 - u0**2 * (n - 1) / n**2 - u1 / n
    y0_120 = y0
    y1_120 = y1 + y0 * u0 * (n - 1) / n
    close(exact_120(0.0)[0], h0_120)
    close(exact_120(0.0)[1], y0_120)
    close(first_order_derivative(lambda e: exact_120(e)[0]), h1_120, rel=3e-7)
    close(first_order_derivative(lambda e: exact_120(e)[1]), y1_120, rel=3e-7)


def q4() -> None:
    alpha, mass, radius, gravity = 7.0, 2.0, 0.36, 9.8
    disk_mass = alpha * mass
    tension = 2 * alpha * mass * gravity / (alpha + 3)
    a = (3 - alpha) * gravity / (alpha + 3)
    angular = 4 * gravity / ((alpha + 3) * radius)
    a_disk = (alpha + 1) * gravity / (alpha + 3)
    close(mass * gravity - tension, mass * a)
    close(disk_mass * gravity - tension, disk_mass * a_disk)
    close(tension * radius, 0.5 * disk_mass * radius**2 * angular)
    close(a_disk, angular * radius - a)
    assert a < 0 < a_disk

    height = 1.8
    t_right = math.sqrt(2 * (alpha + 3) * height / ((alpha + 1) * gravity))
    t_left = math.sqrt(2 * (alpha + 3) * height / ((alpha - 3) * gravity))
    assert t_right < t_left

    mu = 0.21
    critical = 3 * math.exp(math.pi * mu)
    t1 = mass * gravity
    t2 = critical * mass * gravity / 3
    close(t2 / t1, math.exp(math.pi * mu))


def q5() -> None:
    lam, eps0, radius, a = 1.7e-8, 8.8541878128e-12, 0.8, 1.7
    z = 0.006
    axial = lam * radius * z / (2 * eps0 * (radius**2 + z**2) ** 1.5)
    linear = lam * z / (2 * eps0 * radius**2)
    close(axial, linear, rel=9e-5)

    # Independent midpoint quadrature for the ring force.
    def integrate_force(offset: float, count: int = 300_000) -> tuple[float, float]:
        fx = fy = 0.0
        dphi = 2 * math.pi / count
        prefactor = lam**2 * radius / (2 * math.pi * eps0)
        for k in range(count):
            phi = (k + 0.5) * dphi
            dx = radius * math.cos(phi) - offset
            dy = radius * math.sin(phi)
            denominator = dx * dx + dy * dy
            fx += prefactor * dx / denominator * dphi
            fy += prefactor * dy / denominator * dphi
        return fx, fy

    fx_out, fy_out = integrate_force(a)
    close(fx_out, -lam**2 * radius / (eps0 * a), rel=3e-8)
    close(fy_out, 0.0, abs_tol=1e-16)
    fx_in, fy_in = integrate_force(0.35)
    close(fx_in, 0.0, abs_tol=2e-16)
    close(fy_in, 0.0, abs_tol=2e-16)


def q6() -> None:
    mass, charge, magnetic, radius = 9.11e-31, 1.60e-19, 0.10, 1.0
    v_parallel, v_perp = 2.4e5, 1.7e5
    curvature = -mass * v_parallel**2 / (charge * magnetic * radius)
    gradient = -mass * v_perp**2 / (2 * charge * magnetic * radius)
    total = -mass * (2 * v_parallel**2 + v_perp**2) / (2 * charge * magnetic * radius)
    close(curvature + gradient, total)

    thermal_energy = charge * 1.0  # 1 eV
    thermal_drift = -2 * thermal_energy / (charge * magnetic * radius)
    close(thermal_drift, -20.0)


def q7() -> None:
    height, h0 = 3.51, 2.82
    h1 = height / 2
    close(h1, 1.755)

    h2 = (
        -7 * height
        - 2 * h0
        + math.sqrt(81 * height**2 + 44 * height * h0 + 4 * h0**2)
    ) / 4
    x = (height - h2) / 5
    pressure_equation = h0 * height / (height - x) + height - h2
    close(pressure_equation, h0 + height / 2)
    close(h2, 2.01717377970639)

    x_open = height / 4
    h_a = 5 * height / 16 + x_open / 4
    h_b = height - x_open
    close(h_a, h_b / 2)
    close(h_b - h_a, 3 * height / 8)

    discriminant = 441 * height**2 + 432 * height * h0 + 64 * h0**2
    x_closed = 2 * height + 2 * h0 / 3 - math.sqrt(discriminant) / 12
    gas_height = 15 * height / 16 - x_closed / 4
    h_a_closed = 5 * height / 16 + x_closed / 4
    h_b_closed = height - x_closed
    close(h0 * height / gas_height + h_a_closed, h0 + h_b_closed / 2)
    h4 = h_b_closed - h_a_closed
    close(h4, 1.8177933715882073)
    assert 0 < x_closed < height and gas_height > 0


def q8() -> None:
    mass, radius, inertia, initial = 1.8, 2.4, 3.1, 5.7
    final = mass * radius**2 * initial / (inertia + mass * radius**2)
    omega = final / radius
    close(mass * initial * radius, mass * final * radius + inertia * omega)
    before = 0.5 * mass * initial**2
    after = 0.5 * mass * final**2 + 0.5 * inertia * omega**2
    close(after / before, mass * radius**2 / (inertia + mass * radius**2))
    assert 0 < final < initial and after < before


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("蔡题084：8题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
