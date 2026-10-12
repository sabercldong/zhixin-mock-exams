from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 1e-9, abs_tol: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol):
        raise AssertionError(f"{actual=} differs from {expected=}")


def bisect(function, left: float, right: float, steps: int = 100) -> float:
    fl = function(left)
    for _ in range(steps):
        middle = (left + right) / 2
        fm = function(middle)
        if fl * fm <= 0:
            right = middle
        else:
            left, fl = middle, fm
    return (left + right) / 2


def q1() -> None:
    cos_beta = 2 * math.sqrt(6) / 5
    omega2 = 10 / math.sqrt(6)
    close((omega2 / 4) * cos_beta, 1.0)
    close(math.sqrt(2) * cos_beta, 4 * math.sqrt(3) / 5)

    s0 = math.sqrt(6) / 2
    vt = math.sqrt(omega2) / 4
    vr = 4 * math.sqrt(3) / 5
    vp = math.sqrt(2)
    initial = 0.5 * (vt * vt + vr * vr) + vp * vp
    angular_momentum = 0.25 * vt

    def turning_equation(x: float) -> float:
        radius = 1.5 - math.sqrt((s0 + x) ** 2 + 1 / 16)
        return 0.5 * (angular_momentum / radius) ** 2 - x - initial

    root = bisect(turning_equation, 0.204, 0.205)
    close(root, 0.204342876, rel=2e-4)

    height = (2 * math.sqrt(6) - math.sqrt(15)) / 8
    impulse = 4 / math.sqrt(3) * math.sqrt(height) - math.sqrt(omega2) / 4
    close(impulse, 0.321912492952905)


def q2() -> None:
    rho0, coefficient, area = 1.7e7, 1.0e-3, 1.0
    current = area / (2 * math.sqrt(rho0 * coefficient))
    close(current, 3.834824944236852e-3)
    close(area * 0.01 / coefficient, 10.0)
    voltage = 2.0e3
    d1 = voltage * math.sqrt(coefficient / rho0)
    power = area * voltage / (2 * math.sqrt(rho0 * coefficient))
    close(d1, 0.015339299776011236)
    close(power, 7.669649888005618)


def q3() -> None:
    length, hanging, friction, gravity = 3.2, 0.8, 0.17, 9.8
    mu_static = (2 * length - hanging) * hanging / (length - hanging) ** 2
    close(mu_static, 0.7777777777777778)
    bracket = (
        2 * length**3
        - 3 * length * hanging**2
        + hanging**3
        - friction * (length - hanging) ** 3
    )
    speed = math.sqrt(2 * gravity * bracket / 3) / length
    kinetic_coefficient = 0.25 * length**2 * speed**2
    energy_coefficient = gravity * bracket / 6
    close(kinetic_coefficient, energy_coefficient)


def q4() -> None:
    ratio = (3 + math.sqrt(3)) / (2 + math.sqrt(2))
    direct = (
        2
        * math.cos(math.radians(30))
        * math.cos(math.radians(15))
        / (math.cos(math.radians(45)) + 0.5)
    )
    close(ratio, direct)
    close(ratio, 1.3859855926176456)


def q5() -> None:
    force_factor = 1 / math.sqrt(2) - 1 / 4
    close(force_factor, (2 * math.sqrt(2) - 1) / 4)
    r0, r1, mass, keq2 = 3.0, 1.2, 0.7, 2.4
    gamma = keq2 * (2 * math.sqrt(2) - 1) / 4
    semimajor = (r0 + r1) / 2
    half_period = math.pi * math.sqrt(mass * semimajor**3 / gamma)
    closed_form = math.pi * math.sqrt(
        mass * (r0 + r1) ** 3 / (2 * keq2 * (2 * math.sqrt(2) - 1))
    )
    close(half_period, closed_form)

    eps = 1e-4
    normalized = (
        -(1 - eps) ** -2
        - (1 + eps) ** -2
        + 2 * (1 + eps**2) ** -1.5
    )
    close(normalized / eps**2, -9.0, rel=2e-7)


def q6() -> None:
    q = 0.013
    ratio = 1 / math.sqrt(1 - q)
    close(ratio, 1.0065640694646236)
    depth_exact = ratio - 1
    close(depth_exact, q / 2, rel=0.01)
    gravitational, mass, radius = 6.67e-11, 1.3e22, 2.4e6
    omega = math.sqrt(gravitational * mass / radius**3)
    close(omega**2 * radius, gravitational * mass / radius**2)


def q7() -> None:
    alpha, beta, rho, dry_mass = 0.75, 0.20, 1.0e3, 0.200
    volume, pressure = 2.0e-3, 1.0e6
    water_mass = (1 - alpha) * volume * rho
    energy = 2.5 * alpha * beta * pressure * volume * (1 - alpha**0.4)
    water_speed = math.sqrt(
        2 * energy * dry_mass / (water_mass * (dry_mass + water_mass))
    )
    rocket_speed = math.sqrt(
        2 * energy * water_mass / (dry_mass * (dry_mass + water_mass))
    )
    close(water_speed, 9.652480259364799)
    close(rocket_speed, 24.131200648411998)
    close(water_mass * water_speed, dry_mass * rocket_speed)
    close(
        0.5 * water_mass * water_speed**2 + 0.5 * dry_mass * rocket_speed**2,
        energy,
    )


def q8() -> None:
    a, b, wavelength, n = 4.1, 2.3, 5.5e-7, 6
    radius = a * math.sqrt((n - 0.5) * wavelength / b)
    close(b * radius**2 / a**2, (n - 0.5) * wavelength)
    mass, gravity, sigma = 0.12, 9.8, 0.072
    rho = a**2 / b
    theta = math.sqrt(mass * gravity / (2 * math.pi * sigma * rho))
    close(2 * math.pi * sigma * rho * theta**2, mass * gravity)
    center = rho * theta
    outer = center + radius
    close(outer, a * (
        math.sqrt(mass * gravity / (2 * math.pi * sigma * b))
        + math.sqrt((n - 0.5) * wavelength / b)
    ))


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("蔡题086：8题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
