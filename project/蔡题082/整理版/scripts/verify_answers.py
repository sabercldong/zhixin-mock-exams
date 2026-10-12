from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 1e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=1e-12):
        raise AssertionError(f"{actual=} differs from {expected=}")


def q1() -> None:
    g, radius = 9.8, 6.370e6
    a_min = 0.5 * radius * (1 + math.sin(math.radians(29)))
    velocity = math.sqrt(2 * g * radius**2 * (1 / radius - 1 / (2 * a_min)))
    close(velocity, 6384.810029883694)
    period = 8 * 3600
    a = (g * radius**2 * period**2 / (4 * math.pi**2)) ** (1 / 3)
    distance = 4 * a - 2 * radius
    close(distance, 6.842523511859915e7)


def q2() -> None:
    # Work in units B=omega=d=R=1 and compare both compact forms.
    emf = 3 * math.sqrt(3) / 16
    current = emf / 2.5
    close(current, 3 * math.sqrt(3) / 40)
    for x in (0.0, 1 / 28, 0.5):
        direct = math.sqrt(3) / 32 + math.sqrt(3) * x / 4 - current * (0.5 + x)
        compact = math.sqrt(3) / 4 * (0.7 * x - 1 / 40)
        close(direct, compact)


def q3() -> None:
    mass, force, gravity = 1.0, 6.0, 10.0
    acceleration = 2 * 4 / 2**2
    mu = (force - mass * acceleration) / (mass * gravity)
    close(mu, 0.4)
    theta = math.atan(mu)
    a_max = force / mass * math.sqrt(1 + mu**2) - mu * gravity
    close(math.degrees(theta), 21.80140948635181)
    close(a_max, 2.4621977685614063)
    x0 = 10 / 3
    work_force = 0.5 * 10 * x0 * math.cos(math.radians(30))
    work_friction = -mu * mass * gravity * x0 + 0.5 * mu * 10 * x0 * math.sin(math.radians(30))
    v2 = 2 * (work_force + work_friction) / mass
    close(v2, 8.867513459481287)
    assert x0 + v2 / (2 * mu * gravity) > 4


def q4() -> None:
    q12, w23, q23 = 2.5, 4.0, 14.0
    w34, du34 = -1.5, -10.0
    q34 = w34 + du34
    w41, du41 = -1.0, -2.5
    q41 = w41 + du41
    close(q34, -11.5)
    close(q41, -3.5)
    close((w23 + w34 + w41) / (q12 + q23), 1 / 11)


def q5() -> None:
    mu = 0.2
    phi = math.atan(mu)
    close(1 + 2 * math.cos(phi), 2.9611613513818404)
    close(math.degrees(math.pi / 3 + phi), 71.30993247402021)


def q6() -> None:
    # Use g=H=1. The relative distance and work coefficients are scale-free.
    v1 = math.sqrt(2)
    dt = v1 / 4
    common = -v1 + 3 * dt
    close(common, -v1 / 4)
    height_at_equal = v1 * dt - 2.5 * dt**2
    v2 = math.sqrt((v1 / 4) ** 2 + 2 * height_at_equal)
    close(v2, v1 / 2)
    close(sum(0.5 * (0.25**n) for n in range(100)), 2 / 3)
    close(-4 * (2 / 3), -8 / 3)
    assert 2 / 3 < 3 / 4


def q7() -> None:
    # Set Q=R=1; compare k/2 with 1/(8*pi*eps0), taking eps0=1.
    close((1 / (4 * math.pi)) / 2, 1 / (8 * math.pi))


def q8() -> None:
    tan_theta = math.sqrt(3) / 5
    cosine = 1 / math.sqrt(1 + tan_theta**2)
    close(cosine, 5 * math.sqrt(7) / 14)
    close(1 - cosine, 0.05508881747693193)


if __name__ == "__main__":
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("蔡题082：8题关键结果独立验算通过。")
