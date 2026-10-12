from __future__ import annotations

import math


def close(actual: float, expected: float, tol: float = 1.0e-9) -> None:
    scale = max(1.0, abs(actual), abs(expected))
    if abs(actual - expected) > tol * scale:
        raise AssertionError(f"{actual=} {expected=}")


def verify_q1() -> None:
    M, m, L, s, z = 10.0, 2.0, 5.0, 0.4, 0.6
    total = M + 4 * m
    people = [z + i * s for i in range(4)]
    xcm = (M * L / 2 + m * sum(people)) / total
    recovered_z = (2 * total * xcm - M * L) / (8 * m) - 1.5 * s
    close(recovered_z, z)

    Ic = M * L**2 / 12 + M * (L / 2 - xcm) ** 2
    Ic += m * sum((position - xcm) ** 2 for position in people)
    hI = Ic / total
    gravity = 7.3
    R1, R2 = 0.8, 1.3

    def period(radius: float) -> float:
        return 2 * math.pi * math.sqrt((hI + radius**2) / (gravity * radius))

    T1, T2 = period(R1), period(R2)
    recovered_g = 4 * math.pi**2 * (R1**2 - R2**2) / (R1 * T1**2 - R2 * T2**2)
    close(recovered_g, gravity)
    recovered_hI = R1 * R2 * (R1 * T2**2 - R2 * T1**2) / (R1 * T1**2 - R2 * T2**2)
    close(recovered_hI, hI)

    delta = xcm - L / 2
    dp = z + 1.5 * s - L / 2
    C = 5 * s**2 / 4 - L**2 / 12
    A = (hI - L**2 / 12 + delta**2) / delta
    close(dp**2 - A * dp + C, 0.0)


def verify_q2() -> None:
    u = (35 + math.sqrt(108025)) / 6
    f, d = 20.0, 15.0
    v1 = f * u / (u - f)
    u2 = d - v1
    v2 = -10 * u2 / (u2 + 10)
    u3 = d - v2
    v3 = f * u3 / (u3 - f)
    close(v3, u - 25)
    close(v3, 20 * (420 - u) / (3 * u + 20))
    beta = (-v1 / u) * (-v2 / u2) * (-v3 / u3)
    close(beta, -160 / (3 * u + 20))
    close(beta, -0.7927236518465497)


def verify_q3() -> None:
    theta2 = math.acos(0.5)
    close(theta2, math.pi / 3)
    alpha = math.acos(math.sqrt(3) / 2)
    close(alpha, math.pi / 6)
    theta1 = (math.pi + 1) / 2 * (2 / 3) ** 1.5
    close(theta1, math.sqrt(6) * (math.pi + 1) / 9)
    n = (math.sqrt(10) - 2 * math.sqrt(2)) / (math.sqrt(5) + 2 * math.sqrt(2))
    close(n, 0.06591980615681407)
    vc, vf, after = math.sqrt(10), math.sqrt(5), 2 * math.sqrt(2)
    close(vc - n * vf, (1 + n) * after)


def verify_q4() -> None:
    B, D, d, mass, resistance = 0.7, 1.4, 0.5, 2.3, 4.1
    threshold = 2 * B**2 * (D**3 + d**3) / (3 * mass * resistance)
    # Midpoint quadrature of the two chord-square contributions.
    intervals = 200000
    small = 0.0
    large = 0.0
    for i in range(intervals):
        xs = d * (i + 0.5) / intervals
        xL = D * (i + 0.5) / intervals
        small += 4 * (d * xs - xs**2) * d / intervals
        large += 4 * (D * xL - xL**2) * D / intervals
    numerical = B**2 * (small + large) / (mass * resistance)
    close(numerical, threshold, 2.0e-10)
    charge = B * math.pi * (D**2 - d**2) / (4 * resistance)
    if charge <= 0:
        raise AssertionError("Q4 charge must be positive")


def verify_q5() -> None:
    a, d, h, theta, drive = 1.3, 2.1, 0.8, 0.42, 0.17
    length = math.sqrt(a**2 + d**2 + 2 * a * d * math.cos(2 * theta))
    theta_dot = -length * drive / (2 * a * d * math.sin(2 * theta))

    def position(angle: float) -> tuple[float, float]:
        radius = 2 * h * (1 - math.sin(angle))
        return radius * math.cos(angle), radius * math.sin(angle)

    x, y = position(theta)
    radius = math.hypot(x, y)
    close(x**2 + y**2 + 2 * h * y - 2 * h * radius, 0.0)
    vx = -2 * h * (math.cos(2 * theta) + math.sin(theta)) * theta_dot
    vy = 2 * h * math.cos(theta) * (1 - 2 * math.sin(theta)) * theta_dot
    speed = h * length * math.sqrt(2 - 2 * math.sin(theta)) * drive / (a * d * math.sin(2 * theta))
    close(math.hypot(vx, vy), speed)
    dt = 1.0e-6
    xp, yp = position(theta + theta_dot * dt)
    close((xp - x) / dt, vx, 2.0e-6)
    close((yp - y) / dt, vy, 2.0e-6)


def verify_q6() -> None:
    # Dimensionless hemisphere integral for several axial positions.
    for a in (0.0, 0.2, 0.8, 2.0, 10.0):
        intervals = 200000
        total = 0.0
        for i in range(intervals):
            u = (i + 0.5) / intervals
            total += (a + u) / (a * a + 1 + 2 * a * u) ** 1.5 / intervals
        exact = 1 / (math.sqrt(1 + a * a) * (1 + math.sqrt(1 + a * a)))
        close(total, exact, 2.0e-10)
    xmax = 1 / math.sqrt(2)
    normalized_emax = xmax / (1 + xmax**2) ** 1.5
    close(normalized_emax, 2 / (3 * math.sqrt(3)))


def verify_q7() -> None:
    def length(theta: float) -> float:
        return 2 * math.cos(theta) * (1 + 1 / math.cos(2 * theta))

    close(length(0.0), 4.0)
    close(length(math.pi / 6), 3 * math.sqrt(3))
    previous = length(0.0)
    for i in range(1, 1000):
        theta = (math.pi / 4 - 1.0e-4) * i / 1000
        current = length(theta)
        if current <= previous:
            raise AssertionError("Q7 length is not increasing")
        previous = current


def verify_q8() -> None:
    k, gas_constant, temperature = 0.002, 8.31, 300.0
    omega, width, rho0 = 70.0, 0.02, 1.29
    theta, r1, r2 = 0.9, 0.07, 0.2
    A = 9 * omega * width * (r2**2 - r1**2) * math.sin(theta)
    ratio = 2 * k * gas_constant * temperature / (2 * k * gas_constant * temperature + A)
    ventilation = ratio * A / 2
    power = ratio * 9 / 2 * rho0 * width * omega**3 * math.sin(theta) ** 3 * (r2**4 - r1**4)
    close(ratio, 0.9664257043547696)
    close(ventilation, 0.1674014380871186)
    close(power, 29.15260767622419)


def main() -> None:
    verify_q1()
    verify_q2()
    verify_q3()
    verify_q4()
    verify_q5()
    verify_q6()
    verify_q7()
    verify_q8()
    print("蔡题083：8题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
