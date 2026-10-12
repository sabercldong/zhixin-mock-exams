from __future__ import annotations

import cmath
import math
import random


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def bisect_root(function, left: float, right: float, tol: float = 1e-13) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left * f_right > 0:
        raise AssertionError("root is not bracketed")
    while right - left > tol:
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return (left + right) / 2


def solve_linear(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    """Gaussian elimination with partial pivoting, avoiding external packages."""
    size = len(rhs)
    augmented = [row[:] + [value] for row, value in zip(matrix, rhs)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-14:
            raise AssertionError("singular linear system")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * reference
                for value, reference in zip(augmented[row], augmented[column])
            ]
    return [augmented[row][-1] for row in range(size)]


def simpson(function, left: float, right: float, panels: int = 20000) -> float:
    if panels % 2:
        panels += 1
    step = (right - left) / panels
    total = function(left) + function(right)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(left + index * step)
    return total * step / 3


def q1_projectile_and_collision_checks() -> None:
    h, g, vertical_speed, horizontal_speed = 1.0, 9.8, 4.0, 10.0
    mu, wall_distance = 0.05, 6.0
    fall_time = math.sqrt(2 * h / g)
    impact_speed = math.sqrt(2 * g * h)
    close(impact_speed, g * fall_time)
    horizontal_after_floor = horizontal_speed - 2 * mu * impact_speed
    flight_to_wall = (wall_distance - horizontal_speed * fall_time) / horizontal_after_floor
    assert horizontal_after_floor > 0 and flight_to_wall > 0
    wall_height = vertical_speed * flight_to_wall - g * flight_to_wall**2 / 2
    vertical_after_wall = vertical_speed - g * flight_to_wall + 2 * mu * horizontal_after_floor
    return_time = wall_distance / horizontal_after_floor
    final_height = wall_height + vertical_after_wall * return_time - g * return_time**2 / 2
    formula = (
        vertical_speed * flight_to_wall
        - g * flight_to_wall**2 / 2
        + (vertical_speed - g * flight_to_wall + 2 * mu * horizontal_after_floor)
        * wall_distance
        / horizontal_after_floor
        - g * (wall_distance / horizontal_after_floor) ** 2 / 2
    )
    close(final_height, formula)


def q2_collision_checks() -> float:
    y = 0.36
    denominator = 51 + 200 * y * y
    v = (45 + 200 * y * y) / denominator
    vc = 96 / denominator
    omega = 400 * y / denominator
    inertia = 6 / 5
    close(80.0, 80 * v + 5 * vc)
    close(80 * y, 80 * v * y + inertia * omega)
    close(40.0, 40 * v * v + 2.5 * vc * vc + 0.5 * inertia * omega * omega)

    def endpoint_equation(value: float) -> float:
        theta = math.acos(-5 * value / 3)
        k = (51 - 200 * value * value) / (400 * value * value)
        return k * theta + math.tan(theta)

    critical = bisect_root(endpoint_equation, 0.30, 0.35)
    close(critical, 0.3204287981053907, 1e-10)
    return critical


def effective_ring(nodes: int, special_opposite: bool = False) -> float:
    # r=1. Node 0 is fixed at one volt; the central node is ground.
    unknown = list(range(1, nodes))
    matrix = [[0.0 for _ in unknown] for _ in unknown]
    rhs = [0.0 for _ in unknown]

    def radial_resistance(i: int) -> float:
        if special_opposite and i in (0, nodes // 2):
            return 1.0
        return 4.0

    for row, i in enumerate(unknown):
        conductance_sum = 1 / radial_resistance(i)
        for j in ((i - 1) % nodes, (i + 1) % nodes):
            g = 1 / 2.0
            conductance_sum += g
            if j == 0:
                rhs[row] += g
            else:
                matrix[row][j - 1] -= g
        matrix[row][row] += conductance_sum

    voltages = [0.0] * nodes
    voltages[0] = 1.0
    voltages[1:] = solve_linear(matrix, rhs)
    current = 1 / radial_resistance(0)
    current += (1 - voltages[1]) / 2
    current += (1 - voltages[-1]) / 2
    return 1 / current


def q3_network_checks() -> None:
    close(effective_ring(3), 12 / 7)
    for n in range(3, 9):
        close(effective_ring(2 * n, special_opposite=True), 2 / 3)
    for n in range(3, 10):
        expected = 4 * (2**n + 1) / (3 * (2**n - 1))
        close(effective_ring(n), expected)


def q5_circuit_checks() -> None:
    r = 3.2
    l0 = 0.8
    c0 = 0.5
    c1 = 0.7
    u = 11.0
    omega = 1 / math.sqrt(l0 * c0)
    l1 = l0 * c0 / c1
    z1 = r + 1j * omega * l1
    z2 = r - 1j / (omega * c1)
    zp = z1 * z2 / (z1 + z2)
    ztotal = r + zp + 1j * (omega * l0 - 1 / (omega * c0))
    assert abs(ztotal.imag) < 1e-12
    i0 = u / ztotal
    i1 = i0 * zp / z1
    i2 = i0 * zp / z2
    close((i1 + i2).real, i0.real)
    close((i1 + i2).imag, i0.imag)
    assert cmath.phase(i1) < 0 < cmath.phase(i2)
    average_power = 0.5 * u * i0.real
    resistor_power = 0.5 * r * (abs(i0) ** 2 + abs(i1) ** 2 + abs(i2) ** 2)
    close(average_power, resistor_power)


def q6_view_factor_checks() -> None:
    l = 1.0
    common = math.pi / 2

    def q1(x: float) -> float:
        return common * (1 - x / math.sqrt(x * x + l * l))

    def q3(x: float) -> float:
        d = l - x
        return common * (1 - d / math.sqrt(d * d + l * l))

    def q2(x: float) -> float:
        return common * (
            x / math.sqrt(x * x + l * l)
            + (l - x) / math.sqrt((l - x) ** 2 + l * l)
        )

    for index in range(21):
        x = index / 20
        close(q1(x) + q2(x) + q3(x), math.pi)
    q1_total = simpson(q1, 0, l)
    q2_total = simpson(q2, 0, l)
    q3_total = simpson(q3, 0, l)
    total = q1_total + q2_total + q3_total
    close(q1_total / total, 1 - 1 / math.sqrt(2))
    close(q2_total / total, math.sqrt(2) - 1)
    close(q3_total / total, 1 - 1 / math.sqrt(2))


def q7_contrast_check() -> None:
    phase = math.radians(10)
    a = 1 / 4
    b = phase / 2
    contrast = ((a + b) ** 2 - (a - b) ** 2) / ((a + b) ** 2 + (a - b) ** 2)
    close(contrast, 0.6223056448558543)


def q4_ion_wind_checks() -> None:
    elementary_charge = 1.6e-19
    ion_mass = 4.65e-26
    field, mean_free_path, length = 2.0e5, 8.0e-7, 0.12
    current, groups = 2.0e-4, 6
    collision_speed = math.sqrt(
        2 * elementary_charge * field * mean_free_path / ion_mass
    )
    momentum_per_collision = ion_mass * collision_speed
    collision_rate = current / elementary_charge * length / mean_free_path
    direct_force = groups * momentum_per_collision * collision_rate
    closed_form = groups * current * length * math.sqrt(
        2 * ion_mass * field / (elementary_charge * mean_free_path)
    )
    close(direct_force, closed_form)


def q8_h_theorem_checks() -> None:
    rng = random.Random(101)
    for _ in range(100):
        p = [rng.random() for _ in range(8)]
        normalization = sum(p)
        p = [value / normalization for value in p]
        rates = [[0.0] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(i + 1, 8):
                value = rng.random()
                rates[i][j] = rates[j][i] = value
        dp = [
            sum(rates[i][j] * p[j] for j in range(8))
            - sum(rates[i]) * p[i]
            for i in range(8)
        ]
        d_h = sum((1 + math.log(value)) * derivative for value, derivative in zip(p, dp))
        if d_h > 1e-11:
            raise AssertionError(f"dH/dt must be nonpositive, got {d_h}")


def main() -> None:
    q1_projectile_and_collision_checks()
    critical = q2_collision_checks()
    q3_network_checks()
    q4_ion_wind_checks()
    q5_circuit_checks()
    q6_view_factor_checks()
    q7_contrast_check()
    q8_h_theorem_checks()
    print(f"Q2 critical x/l = {critical:.12f}")
    print("Q1-Q8 independent checks passed")


if __name__ == "__main__":
    main()
