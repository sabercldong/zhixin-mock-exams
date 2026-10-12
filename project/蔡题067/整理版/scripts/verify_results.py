from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 2e-3) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=rel):
        raise AssertionError(f"{actual=} != {expected=}")


def simpson(function, left: float, right: float, intervals: int = 200_000) -> float:
    if intervals % 2:
        intervals += 1
    step = (right - left) / intervals
    total = function(left) + function(right)
    total += 4 * sum(function(left + index * step) for index in range(1, intervals, 2))
    total += 2 * sum(function(left + index * step) for index in range(2, intervals, 2))
    return total * step / 3


def main() -> None:
    # Q1: second-collision threshold and limiting displacement.
    lambda_min = 6 * math.pi / (3 * math.sqrt(3) - math.pi)
    close(lambda_min, 9.176_58)
    close(math.pi / 9, 0.349_066)
    assert math.pi / 9 < math.sqrt(3) / 3

    # Q2: the two stable wells have curvature ratio three.
    kappa_zero = 2 / 5
    kappa_pi = 6 / 5
    close(math.sqrt(kappa_pi / kappa_zero), math.sqrt(3))

    # Q3: direct eigenvalue check for the dimensionless stiffness matrix
    # [[k+K,-K],[-K,k+K]] with k=3, K=5 and m=2.
    k, coupling, mass = 3.0, 5.0, 2.0
    omega_same = math.sqrt(k / mass)
    omega_opposite = math.sqrt((k + 2 * coupling) / mass)
    close(omega_same**2, 1.5)
    close(omega_opposite**2, 6.5)

    # Q5: numerical integration of the disk angle.
    disk_angle = -simpson(
        lambda theta: (2 * theta / math.pi) ** 2
        / (1 + (2 * theta / math.pi) ** 2),
        0,
        math.pi / 2,
    )
    disk_angle_exact = -math.pi / 2 * (1 - math.pi / 4)
    close(disk_angle, disk_angle_exact, rel=1e-10)
    close(math.pi / 2 + disk_angle, math.pi**2 / 8, rel=1e-10)

    # Q6: reproduce the component inversion from the plotted central readings.
    resistance = 100.0
    frequency = 1000.0
    omega = 2 * math.pi * frequency
    capacitance = 1 / (omega * resistance)
    close(capacitance * 1e6, 1.59, rel=5e-3)
    h2 = 3.95 / 5.00
    alpha = math.radians(29.8)
    internal_resistance = resistance / h2 * math.cos(alpha) - resistance
    inductance = resistance / h2 * math.sin(alpha) / omega
    close(internal_resistance, 9.83, rel=3e-3)
    close(inductance * 1e3, 10.0, rel=3e-3)
    resonance = 1 / (2 * math.pi * math.sqrt(10e-3 * 1.60e-6))
    close(resonance, 1.26e3, rel=3e-3)

    # Q7: the subtraction and ratio forms for ballast are equivalent once
    # the maximum-height balance is imposed.
    rho_zero, volume, density_ratio = 1.2, 100.0, 0.73
    rho_height = rho_zero * density_ratio
    fixed_mass = rho_height * volume
    ballast_by_difference = volume * (rho_zero - rho_height)
    ballast_by_ratio = fixed_mass * (1 / density_ratio - 1)
    close(ballast_by_difference, ballast_by_ratio, rel=1e-12)

    # Q8: intensity bookkeeping.
    i_ex, i_ey, i_unpolarized = 0.75, 0.25, 1.50
    close(i_ey / i_ex, 1 / 3)
    close(i_ex + i_ey + i_unpolarized / 2, 1.75)
    close(i_unpolarized / (i_ex + i_ey + i_unpolarized), 0.60)

    print("蔡题067：数值、极限与等价式核验通过。")


if __name__ == "__main__":
    main()
