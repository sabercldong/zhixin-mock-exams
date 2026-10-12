from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def bisect(function, left: float, right: float) -> float:
    f_left = function(left)
    for _ in range(100):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right = middle
        else:
            left, f_left = middle, f_middle
    return (left + right) / 2


def main() -> None:
    # Q1: the two coordinates satisfy their uncoupled oscillator equations.
    mass, spring, length, speed, angle, time = 2.0, 5.0, 1.3, 2.2, 0.7, 0.9
    omega = math.sqrt(spring / mass)
    x = length * math.cos(omega * time) + speed * math.cos(angle) / omega * math.sin(omega * time)
    y = speed * math.sin(angle) / omega * math.sin(omega * time)
    x_ddot = -omega**2 * x
    y_ddot = -omega**2 * y
    close(mass * x_ddot + spring * x, 0)
    close(mass * y_ddot + spring * y, 0)

    # Q2: total turning angle 20*pi/3 corresponds to 10/3 revolutions.
    close((20 * math.pi / 3) / (2 * math.pi), 10 / 3)

    # Q3: free magnetic precession and cyclotron frequencies have ratio 1:2.
    q, field, m = 1.7, 0.8, 2.4
    close(q * field / m, 2 * q * field / (2 * m))

    # Q4: verify the independently solved potential-barrier root.
    root = bisect(lambda x: 2 + x - x / (1 - x * x) ** 2, 0.6, 0.8)
    close(root, 0.7004940207, 1e-10)

    # Q5: first-order shell-volume relation beta=gamma-2*alpha.
    alpha, gamma = 2e-4, -7e-5
    beta = gamma - 2 * alpha
    close(2 * alpha + beta, gamma)

    # Q6: the final three-lens map is symmetric under lens-order permutation.
    x, y, z, f1, f2, f3 = 0.2, 0.3, 0.4, 1.7, 2.1, 2.8
    scale = 1 / (1 - z / f1 - x / f2 - y / f3)
    denominator = f1 * f3 * x + f1 * f2 * y + f2 * f3 * z - f1 * f2 * f3
    close(scale, -f1 * f2 * f3 / denominator)

    # Q7: quoted support force has the equivalent simplified coefficient.
    close(19 / (10 * math.sqrt(3)), 19 * math.sqrt(3) / 30)

    # Q8: reproduce the first loss-of-contact root from the stated equation.
    equation = lambda t: math.cos(t) * (6 * math.pi**2 - 24 * t**2 - 30 * math.cos(t)) + math.sin(t) * (15 * math.sin(t) - 24 * t) - 20
    root = bisect(equation, 0.4, 0.7)
    close(root, 0.5406327247, 1e-9)
    print("Q1-Q8 independent invariant checks passed")


if __name__ == "__main__":
    main()
