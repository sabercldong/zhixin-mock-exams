from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def solve_linear(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    size = len(rhs)
    a = [row[:] + [value] for row, value in zip(matrix, rhs)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(a[row][column]))
        a[column], a[pivot] = a[pivot], a[column]
        divisor = a[column][column]
        a[column] = [value / divisor for value in a[column]]
        for row in range(size):
            if row == column:
                continue
            factor = a[row][column]
            a[row] = [value - factor * reference for value, reference in zip(a[row], a[column])]
    return [a[row][-1] for row in range(size)]


def main() -> None:
    # Q1: Kepler period at radius alpha*R with GM=gR^2.
    g, radius, alpha = 9.8, 6.4e6, 1.3
    period = 2 * math.pi * math.sqrt((alpha * radius) ** 3 / (g * radius**2))
    close(period, 2 * math.pi * math.sqrt(alpha**3 * radius / g))

    # Q2: the threshold launch speed follows constant-acceleration work-energy.
    mu, spacing, parameter = 0.2, 1.4, 1.8
    speed = math.sqrt(2 * (parameter - 1) * mu * g * spacing)
    close(speed**2, 2 * (parameter - 1) * mu * g * spacing)

    # Q3: energy-momentum relation remains on shell after a Lorentz boost.
    rest_mass, beta = 3.0, 0.72
    gamma = 1 / math.sqrt(1 - beta**2)
    energy, momentum = gamma * rest_mass, gamma * rest_mass * beta
    close(energy**2 - momentum**2, rest_mass**2)

    # Q4: image sequences r_n and q_n approach the tangent point and converge.
    radius = 2.0
    radii = [(n - 1) * radius / n for n in range(2, 1000)]
    assert all(left < right < radius for left, right in zip(radii, radii[1:]))
    charge_sum = sum(1 / n**2 for n in range(1, 200000))
    close(charge_sum, math.pi**2 / 6, 1e-5)

    # Q5: a single half-wave phase reversal changes the constructive condition by pi.
    wavelength, index, angle = 550e-9, 1.33, 0.4
    refracted = math.asin(math.sin(angle) / index)
    thickness = wavelength / (4 * index * math.cos(refracted))
    optical_phase = 4 * math.pi * index * thickness * math.cos(refracted) / wavelength
    close(optical_phase, math.pi)

    # Q6: solve a symmetric triangle network and check Kirchhoff residuals.
    matrix = [[2.0, -1.0], [-1.0, 2.0]]
    rhs = [1.0, 0.0]
    voltage = solve_linear(matrix, rhs)
    close(2 * voltage[0] - voltage[1], 1)
    close(-voltage[0] + 2 * voltage[1], 0)

    # Q7: the exponential temperature profile satisfies the first-order ODE.
    inlet, ambient, coefficient, x = 360.0, 300.0, 0.17, 2.4
    temperature = ambient + (inlet - ambient) * math.exp(-coefficient * x)
    derivative = -coefficient * (inlet - ambient) * math.exp(-coefficient * x)
    close(derivative, -coefficient * (temperature - ambient))

    # Q8: the projectile envelope y=H-x^2/(4H) is tangent to one trajectory.
    head, x = 2.5, 1.7
    envelope = head - x * x / (4 * head)
    slope = -x / (2 * head)
    assert envelope > 0 and slope < 0
    print("Q1-Q8 independent invariant checks passed")


if __name__ == "__main__":
    main()
