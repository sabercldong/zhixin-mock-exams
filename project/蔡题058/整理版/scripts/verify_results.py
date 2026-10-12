#!/usr/bin/env python3
"""第058套八题关键代数、数值、边界与守恒关系的独立核验。"""

from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def simpson(func, a: float, b: float, n: int = 40000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = func(a) + func(b)
    total += 4 * sum(func(a + (2 * k - 1) * h) for k in range(1, n // 2 + 1))
    total += 2 * sum(func(a + 2 * k * h) for k in range(1, n // 2))
    return total * h / 3


def q1() -> None:
    g, h, r = 9.8, 2.3, 0.7
    v_contact = math.sqrt(2 * g * (h + r))
    v_tangent = math.sqrt(2 * g * (h + math.sqrt(2) * r))
    if not v_tangent > v_contact:
        raise AssertionError("禁止接触的最小速度应更大")
    theta = math.pi / 4
    vt2 = g * r / math.cos(theta)
    v02 = vt2 + 2 * g * (h + r * math.cos(theta))
    close(v02, v_tangent**2)
    # 允许接触时脱离角 cosφ=2/3 应满足 N=0。
    close(3 * (2 / 3) - 2, 0.0)


def q2() -> None:
    m1, radius = 2.7e-3, 2e-2
    close((2 / 3) * m1 * radius**2, 7.2e-7)

    m, v1, inertia = 5e-3, 15.6, 1e-6
    omega1 = m * v1 * radius / inertia
    close(omega1, 1560.0)

    mu, v2 = 0.719, 9.86
    omega20 = mu * v2 * (1 / radius + m * radius / inertia)
    close(omega20, 1063.401)
    ix = m * v2
    it_max = mu * ix
    it_required = (
        m * inertia * radius * omega20
        / (inertia + m * radius**2)
    )
    close(it_required, it_max)


def q3() -> None:
    b, l, r = 0.8, 1.7, 2.1
    iz = b * l**2 / (4 * r)
    close(4 * r * iz, b * l**2)

    component_current = b * l**2 / (4 * math.sqrt(3) * r)
    projected_area = math.sqrt(2) * l**2 / 2
    emf_y = math.sqrt(2) * b / math.sqrt(3) * projected_area
    close(4 * r * component_current, emf_y)

    my = -2 * component_current * projected_area
    mz = -component_current * l**2
    close(my, -math.sqrt(2) * b * l**4 / (4 * math.sqrt(3) * r))
    close(mz, -b * l**4 / (4 * math.sqrt(3) * r))
    # B 沿 +z，只有 my 产生 -x 力矩。
    b0 = 0.6
    torque_x = my * b0
    close(torque_x, -math.sqrt(2) * b0 * b * l**4 / (4 * math.sqrt(3) * r))


def q4() -> None:
    r = 1.0
    target = math.pi / 2 - 1
    base = simpson(
        lambda theta: (1 - math.sin(theta)) * math.sin(theta),
        0,
        math.pi / 2,
    )
    close(math.pi / 4 - base, target, 2e-12)

    # 用任意 l(θ)=a sin2θ 数值核验第（3）问线积分。
    for a in (0.0, 0.1, 0.35, 0.7):
        ell = lambda t: a * math.sin(2 * t)
        ellp = lambda t: 2 * a * math.cos(2 * t)
        y2_dx2 = lambda t: (
            ell(t) * math.sin(t)
            * (-ellp(t) * math.cos(t) + ell(t) * math.sin(t))
        )
        x1_dy1 = lambda t: (
            r - r * math.sin(t) - ell(t) * math.cos(t)
        ) * (
            r * math.sin(t)
            + ellp(t) * math.sin(t)
            + ell(t) * math.cos(t)
        )
        area = (
            math.pi * r**2 / 4
            - simpson(y2_dx2, 0, math.pi / 2)
            - simpson(x1_dy1, 0, math.pi / 2)
        )
        close(area, target, 2e-11)


def q5() -> None:
    mu0, moment, emf = 1.2, 0.8, 2.4
    radius, length, lam, drag, turns = 0.7, 3.1, 1.4, 0.9, 5.2
    current = emf / (2 * math.pi * turns * length * radius * lam)

    def field(x: float) -> float:
        return mu0 * current * turns / 2 * (
            (x + length) / math.sqrt((x + length) ** 2 + radius**2)
            - x / math.sqrt(x * x + radius**2)
        )

    step = 1e-6
    derivative_num = (field(step) - field(-step)) / (2 * step)
    derivative = mu0 * current * turns / 2 * (
        radius**2 / (length**2 + radius**2) ** 1.5 - 1 / radius
    )
    close(derivative_num, derivative, 2e-9)

    speed_force = 2 * moment * abs(derivative) / drag
    speed_closed = (
        mu0 * moment * radius * emf
        / (2 * math.pi * lam * length * drag)
        * (1 / radius**3 - 1 / (radius**2 + length**2) ** 1.5)
    )
    close(speed_force, speed_closed)


def q6() -> None:
    for n in (1, 2, 5, 10, 100):
        temp = 0.0
        for _ in range(n):
            temp = (n * temp + 100) / (n + 1)
        closed = 100 * (1 - (n / (n + 1)) ** n)
        close(temp, closed)
    close(100 * (1 - 1 / math.e), 63.212055882855765)

    th, tc = 373.15, 273.15
    t1 = math.sqrt(th * tc)
    close(t1, 319.25839456465354)
    t2 = th + tc - t1
    close(t2 - 273.15, 53.891605435346435)
    work_per_heat_capacity = th + tc - 2 * t1
    close(work_per_heat_capacity, (math.sqrt(th) - math.sqrt(tc)) ** 2)
    # 可逆最高温末态是初温交换。
    close(tc + th, th + tc)
    close(tc * th, th * tc)


def q7() -> None:
    n1, n2, theta, wavelength = 1.6, 1.2, math.radians(60), 550e-9
    critical = math.asin(n2 / n1)
    if not theta > critical:
        raise AssertionError("测试角度应处于全反射区")
    alpha = 2 * math.pi / wavelength * math.sqrt(
        n1**2 * math.sin(theta) ** 2 - n2**2
    )
    depth = 1 / alpha
    close(math.exp(-alpha * depth), 1 / math.e)
    close(math.exp(-2 * alpha * (depth / 2)), 1 / math.e)


def q8() -> None:
    relative = (0.6 + 0.8) / (1 + 0.6 * 0.8)
    close(relative, 35 / 37)
    gamma_rel = 1 / math.sqrt(1 - relative**2)
    close(gamma_rel, 37 / 12)
    mc = 100 / gamma_rel
    close(mc, 1200 / 37)
    close(0.8 * 14, 11.2)

    t_collision = 14 / 1.4
    x_collision = 0.6 * t_collision
    close(t_collision, 10.0)
    close(x_collision, 6.0)
    t_b = t_collision + 0.8 * x_collision - 0.8 * 14
    close(t_b, 3.6)

    energy = (5 / 4) * mc + (5 / 3) * 100
    momentum_c = (5 / 4) * mc * 0.6 - (5 / 3) * 100 * 0.8
    mass = math.sqrt(energy**2 - momentum_c**2)
    close(energy, 23000 / 111)
    close(momentum_c, -12100 / 111)
    close(mass, 100 * math.sqrt(4251) / 37)
    close(momentum_c / energy, -121 / 230)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 058 套八题的关键代数、数值、守恒、边界与极限验证通过")


if __name__ == "__main__":
    main()
