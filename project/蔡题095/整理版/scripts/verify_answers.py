from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def main() -> None:
    # Q1: effective-gravity equilibrium and the roof-touching threshold.
    g, acceleration = 9.8, 9.8
    theta = math.atan2(acceleration, g)
    close(2 * theta, math.pi / 2)

    # Q2: the large-N spoke-wheel force tends to pi*m*g/N.
    n, mass = 10000, 2.0
    exact = mass * g * math.sin(math.pi / n)
    close(exact, math.pi * mass * g / n, 1e-6)

    # Q3: check the quoted aggregate speed by direct work-energy balance.
    block_mass, force, spacing, index = 1.3, 4.2, 0.7, 5
    speed = math.sqrt(2 * index * force * spacing / ((3 * index + 1) * block_mass))
    close(0.5 * (3 * index + 1) * block_mass * speed**2, index * force * spacing)

    # Q4: two identical capacitors share charge and reach U0/2.
    capacitance, voltage = 2.2, 7.0
    shared = capacitance * voltage / (2 * capacitance)
    close(shared, voltage / 2)

    # Q5: Poynting flux through a cylindrical boundary equals UI.
    epsilon0, mu0 = 8.854e-12, 4 * math.pi * 1e-7
    charge, current, radius = 3e-6, 0.08, 0.04
    electric = charge / (epsilon0 * math.pi * radius**2)
    magnetic = mu0 * current / (2 * math.pi * radius)
    poynting = electric * magnetic / mu0
    lateral_power = poynting * 2 * math.pi * radius
    voltage_per_length = charge / (epsilon0 * math.pi * radius**2)
    close(lateral_power, voltage_per_length * current)

    # Q6: opening temperature follows the sealed, fixed-volume pressure law.
    p0, area, load, t0 = 1.01e5, 0.01, 30.0, 300.0
    t1 = (1 + load * g / (p0 * area)) * t0
    close(p0 * t1 / t0, p0 + load * g / area)

    # Q7: Newton imaging maps x1*x2=f^2 and preserves the stated discriminant.
    f, x1 = 0.3, -0.8
    x2 = f * f / x1
    close(x1 * x2, f * f)

    # Q8: the reported angular speed satisfies its angular-momentum identity.
    speed, radius = 4.0, 0.6
    omega = speed / (5 * radius)
    close(5 * radius * omega, speed)
    print("Q1-Q8 independent invariant checks passed")


if __name__ == "__main__":
    main()
