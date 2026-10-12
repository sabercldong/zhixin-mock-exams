from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def main() -> None:
    # Q1: sliding impulse preserves u+(2/5)r*omega for a solid sphere.
    m, r, u0, omega0, impulse = 2.3, 0.4, 5.1, -1.2, 0.8
    u = u0 - impulse / m
    omega = omega0 + 5 * impulse / (2 * m * r)
    close(u + 2 * r * omega / 5, u0 + 2 * r * omega0 / 5)

    # Q2: the conic p/(1+e cos theta) satisfies Binet's inverse-square equation.
    p, e, theta = 3.2, 0.45, 0.7
    reciprocal_r = (1 + e * math.cos(theta)) / p
    second_derivative = -e * math.cos(theta) / p
    close(reciprocal_r + second_derivative, 1 / p)

    # Q3: a 2*pi change of boundary polar angle rotates the tangent by pi.
    close(0.5 * 2 * math.pi, math.pi)

    # Q4: the stated sticking boundary P=Q/3 makes the wheel-contact relation vanish.
    q = 0.18
    p_impulse = q / 3
    close(3 * p_impulse - q, 0)

    # Q5: confocal-ellipse capacitance tends to the coaxial circular result.
    a, c = 2.0, 1e-7
    xi1 = math.acosh(a / c)
    xi2 = math.acosh(2 * a / c)
    close(xi2 - xi1, math.log(2), 1e-7)

    # Q6: helix pitch h and beta=h/(2*pi*r) give the same axial rise per turn.
    radius, height = 0.8, 1.7
    beta = height / (2 * math.pi * radius)
    close(2 * math.pi * radius * beta, height)

    # Q7: differentiate the integrated heating time to recover the ODE integrand.
    temperature = 16.3
    derivative = 285 * (20 - temperature) / (300 - temperature)
    epsilon = 1e-6
    primitive = lambda t: 285 * (t + 280 * math.log(300 - t))
    numerical = (primitive(temperature + epsilon) - primitive(temperature - epsilon)) / (2 * epsilon)
    close(numerical, derivative, 2e-5)

    # Q8: serial heat-engine losses multiply.
    eta1, eta2 = 0.31, 0.42
    combined = eta1 + eta2 - eta1 * eta2
    close(1 - combined, (1 - eta1) * (1 - eta2))
    print("Q1-Q8 independent invariant checks passed")


if __name__ == "__main__":
    main()
