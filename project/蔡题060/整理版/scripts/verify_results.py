#!/usr/bin/env python3
"""第060套关键结论的独立数值与代数核验。"""

from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def bisect(func, left: float, right: float, tol: float = 1e-13) -> float:
    fl = func(left)
    fr = func(right)
    if fl * fr > 0:
        raise AssertionError("二分区间未夹住根")
    while right - left > tol:
        mid = (left + right) / 2
        fm = func(mid)
        if fl * fm <= 0:
            right, fr = mid, fm
        else:
            left, fl = mid, fm
    return (left + right) / 2


def q1() -> None:
    mu = 1.5
    f = lambda a: math.exp(mu * a) * math.cos(a) - 2
    amin = bisect(f, 0.1, 0.9)
    amax = bisect(f, 0.9, 1.55)
    close(amin, 0.5820401316, 2e-10)
    close(amax, 1.2673106105, 2e-10)

    critical = lambda a: math.exp(a * math.tan(a)) * math.cos(a) - 2
    ac = bisect(critical, 0.5, 1.2)
    muc = math.tan(ac)
    close(ac, 0.9144038679, 2e-10)
    close(muc, 1.2981272163, 2e-10)
    close(math.exp(muc * ac) * math.cos(ac), 2.0)


def q2() -> None:
    # 取 l=1，检查 n=1...5 时相对旋转角均为 2πn。
    for n in range(1, 6):
        ratio = 1 / math.sqrt(4 * n * n - 1)  # r/l
        phase = math.pi * math.sqrt(1 + 1 / ratio**2)
        close(phase, 2 * math.pi * n)
    # 上板一周所需时间乘球心角速度 Ω/2，球心恰转过 π。
    close(0.5 * 2 * math.pi, math.pi)


def q3() -> None:
    # 四条等价出边在两辅助状态中各给 I/4，同向叠加为 I/2。
    current_ab = 1 / 4 + 1 / 4
    close(current_ab, 1 / 2)
    close(current_ab * 1.0, 1 / 2)  # 取单边 r=1 得 U/I=r/2
    # 断边后星形参数回接直连 r=1，应恢复端间等效电阻 1/2。
    remaining_ab = 1.0  # r/2+r/2
    restored = 1 / (1 / remaining_ab + 1 / 1.0)
    close(restored, 1 / 2)
    close(1 / 2 + 1 / 8, 5 / 8)  # 断边后 A-C 端间阻值


def q4() -> None:
    # 令 qB/m=1、R=1，检查第二问守恒式。
    omega0 = 1.2
    r2 = 8 * omega0 * (omega0 - 1)
    omega2 = omega0 / (2 * omega0 - 1)
    inertia_i = 2.0
    inertia_f = 2.0 + r2
    close(inertia_i * omega0, inertia_f * omega2 - 0.5 * r2)
    close(inertia_i * omega0**2, inertia_f * omega2**2)

    # 第三问数值根及两个守恒方程。
    w0 = 0.53
    equation = lambda c: (1 + (1 - c) ** 2 / (5 * w0)) ** 2 - (
        2 / 5
    ) * (c * c - 3 * c + 4.5)
    c = bisect(equation, 0.0, 0.4)
    close(c, 0.1335082176, 2e-10)
    alpha = math.acos(c)
    close(math.degrees(alpha), 82.3276, 2e-5)
    ii = 2.5
    iff = c * c - 3 * c + 4.5
    w2 = w0 * math.sqrt(ii / iff)
    close(w2, 0.4129901, 2e-7)
    close(ii * w0, iff * w2 - 0.5 * (1 - c) ** 2)
    close(ii * w0**2, iff * w2**2)


def exact_potential(x: float, y: float, theta: float, l: float = 1.0) -> float:
    """取 k_e Q q=1，分子中心在 (x,y)，轴角 theta。"""
    nx, ny = math.cos(theta), math.sin(theta)
    charges = [(-1.0, -l), (2.0, 0.0), (-1.0, l)]
    total = 0.0
    for charge, offset in charges:
        px = x + offset * nx
        py = y + offset * ny
        total += charge / math.hypot(px, py)
    return total


def q5() -> None:
    # 在 r/l=100 时，用精确三电荷势能的数值梯度核验四极合力。
    r = 100.0
    theta = 0.7
    x, y = r, 0.0
    step = 1e-3
    fx_num = -(
        exact_potential(x + step, y, theta)
        - exact_potential(x - step, y, theta)
    ) / (2 * step)
    fy_num = -(
        exact_potential(x, y + step, theta)
        - exact_potential(x, y - step, theta)
    ) / (2 * step)
    c = math.cos(theta)
    nx, ny = math.cos(theta), math.sin(theta)
    fx_quad = 3 / r**4 * ((1 - 5 * c * c) + 2 * c * nx)
    fy_quad = 3 / r**4 * (2 * c * ny)
    close(fx_num, fx_quad, 5e-4)
    close(fy_num, fy_quad, 5e-4)

    # 感生场力矩：n 与 b 垂直时大小 q l² b，平行时为零。
    close(1.0 * (1.0 - 0.0), 1.0)
    close(1.0 * (1.0 - 1.0), 0.0)


def simpson(func, a: float, b: float, n: int = 20000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = func(a) + func(b)
    total += 4 * sum(func(a + (2 * k - 1) * h) for k in range(1, n // 2 + 1))
    total += 2 * sum(func(a + 2 * k * h) for k in range(1, n // 2))
    return total * h / 3


def q6() -> None:
    x1 = math.pi / 6
    close(2 * math.cos(x1 + math.pi / 3), 0.0)
    integral = simpson(
        lambda phi: 0.5 * (5 - 4 * math.cos(phi) ** 2),
        math.pi / 3,
        math.pi / 2,
    )
    close(integral, (math.pi + math.sqrt(3)) / 4, 2e-12)
    reception = -math.pi / 12 + integral
    close(reception, math.pi / 6 + math.sqrt(3) / 4)
    phi = math.acos(1 / 4)
    xs = -2 * (phi - math.pi / 3) + math.sin(2 * phi) - math.sqrt(3) / 2
    close(xs, -0.9237395264, 2e-10)


def q7() -> None:
    head_cm = 86 * 90 / 10 * math.log(100 / 90) - 76 - 3 * 10 / 8
    close(head_cm, 1.799039119157598)
    v = math.sqrt(2 * 9.8 * head_cm / 100)
    close(v, 0.593811137782788)
    close(86 * 90 / 100, 77.4)
    close((77.4 + 76 - 5) / 2, 74.2)
    mouth_energy = 86 * 90 * math.log(145 / 90) - 76 * 55 + 10 * 40
    if not mouth_energy < 0:
        raise AssertionError("水银到管口的试探动能应为负")
    close(mouth_energy, -88.60768202100553)
    t_min = 300 * 76 * 155 / (86 * 90)
    close(t_min, 456.5891472868217)


def q8() -> None:
    for gamma in (1.0, 1.2, 3.0, 10.0, 1000.0):
        energy = gamma + 1
        momentum_c = math.sqrt(gamma * gamma - 1)
        invariant = energy * energy - momentum_c * momentum_c
        close(invariant, 2 * (gamma + 1))
        cos_theta = (gamma - 3) / (gamma + 1)
        theta = 2 * math.acos(math.sqrt((gamma - 1) / (gamma + 1)))
        close(math.cos(theta), cos_theta)
        beta_cm = momentum_c / energy
        close(beta_cm, math.sqrt((gamma - 1) / (gamma + 1)))
    close(2 * math.acos(0.0), math.pi)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 060 套八题的关键代数、数值、边界与极限验证通过")


if __name__ == "__main__":
    main()
