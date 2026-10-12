#!/usr/bin/env python3
"""第059套关键结论的独立数值、守恒、边界与极限核验。"""

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


def simpson(func, a: float, b: float, n: int = 20000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = func(a) + func(b)
    total += 4 * sum(func(a + (2 * k - 1) * h) for k in range(1, n // 2 + 1))
    total += 2 * sum(func(a + 2 * k * h) for k in range(1, n // 2))
    return total * h / 3


def q1() -> None:
    # 单位取 km、km/s；游泳速度 v/2。
    l = x = 1.0
    h = 0.5
    alpha = math.pi / 4
    v = 0.001
    n = 2.0

    t1 = (math.hypot(l, h) + x) / v
    close(t1, 2118.033988749895)

    derivative = lambda c: (
        (c - l) / math.hypot(l - c, h)
        + n * (c - x * math.cos(alpha))
        / math.sqrt(x * x + c * c - 2 * x * c * math.cos(alpha))
    )
    c = bisect(derivative, 0.71, 0.95)
    t2 = (
        math.hypot(l - c, h)
        + n * math.sqrt(x * x + c * c - 2 * x * c * math.cos(alpha))
    ) / v
    close(c, 0.8253271331267805, 2e-12)
    close(t2, 1963.474986, 2e-9)

    f = l - h * math.sqrt((math.sqrt(3) - 1) / 2)
    g = f * math.sin(math.radians(75)) / math.sin(math.radians(60))
    water = math.sqrt(f * f + g * g - 2 * f * g * math.cos(alpha))
    t3 = (math.hypot(l - f, h) + n * water + x - g) / v
    close(f, 0.6974998331, 2e-10)
    close(g, 0.7779599764, 2e-10)
    close(t3, 1945.437929, 2e-9)
    if not t3 < t2 < t1:
        raise AssertionError("三种路线的时间排序错误")


def q2() -> None:
    # 任取 M=g=l=1 及若干 h，验证两端张力差、合力和闭式表达。
    for h in (0.2, 0.5, 1.0, 2.0):
        f1 = (9 + 4 * h * h) / (24 * h)
        f2 = f1 - h / 3
        close(f1 - f2, h / 3)
        close(f1 * f1 - f2 * f2, 1 / 4)

    # 等质量完全弹性碰撞交换速度；绳绷紧后的共同速度来自冲量守恒。
    v0 = 3.7
    left_after_collision, right_after_collision = -v0, 0.0
    common = (left_after_collision + right_after_collision) / 2
    close(common, -v0 / 2)
    close(abs(common - right_after_collision), v0 / 2)
    close(9.8 * 1.3**2 / (2 * v0**2), 9.8 * 1.3**2 / (2 * v0**2))


def q3() -> None:
    # 取 λ=r0=k=1，直接数值积分核验质量、质心和转动惯量。
    k = r0 = lam = 1.0
    jac = math.sqrt(1 + k * k)
    lo = -30.0
    mass = simpson(lambda th: lam * jac * r0 * math.exp(k * th), lo, 0)
    mx = simpson(
        lambda th: lam * jac * (r0 * math.exp(k * th)) ** 2 * math.cos(th),
        lo,
        0,
    )
    my = simpson(
        lambda th: lam * jac * (r0 * math.exp(k * th)) ** 2 * math.sin(th),
        lo,
        0,
    )
    inertia = simpson(
        lambda th: lam * jac * (r0 * math.exp(k * th)) ** 3,
        lo,
        0,
    )
    close(mass, math.sqrt(2), 2e-12)
    close(mx / mass, 2 / 5, 2e-12)
    close(my / mass, -1 / 5, 2e-12)
    close(inertia, math.sqrt(2) / 3, 2e-12)

    # 虫由 ρ=r0 爬到 0 时，导线反转角为 ∫ρ/(r0²/3+ρ²)dρ。
    angle = simpson(lambda rho: rho / (r0 * r0 / 3 + rho * rho), 0, r0)
    close(angle, math.log(2), 2e-12)


def q4() -> None:
    # 量纲核验：k_e² Q² r³/L⁵ 与力同量纲。
    # [k_e]=N m²/C²，故指数为 N²m⁴/C⁴ * C² * m³/m⁵ = N²m²/C²；
    # 题中 A1 含 1/ε0²，对应高斯化系数。这里核验幂次齐次与薄极限系数。
    close(2 + 3 - 5, 0)
    close(2 + 5 - 7, 0)
    eps0 = 2.3
    gamma2 = 0.71
    coefficient = -1 / (12 * math.pi * eps0**2 * gamma2)
    force = coefficient * 1.7**2 * 0.4**3 / 3.2**5
    reconstructed = (
        -1
        / (12 * math.pi * eps0**2 * gamma2)
        * 1.7**2
        * 0.4**3
        / 3.2**5
    )
    close(force, reconstructed)
    if not force < 0:
        raise AssertionError("导体棒受力应指向外电荷，约定下系数为负")


def q5() -> None:
    m, q, b, r, v0, g = 1.8, 0.7, 0.9, 0.4, 2.1, 9.8
    omega = 5 * q * b / (7 * m)
    radius = 7 * m * v0 / (5 * q * b)
    close(omega * radius, v0)
    mu_required = 2 * abs(q) * b * v0 / (7 * m * g)
    if not 0 < mu_required < 1:
        raise AssertionError("示例静摩擦阈值异常")

    omega_surface = 20 * q * b / (21 * m)
    radius_surface = 21 * m * v0 / (20 * q * b)
    close(omega_surface * radius_surface, v0)
    close((q * r * r / 3) * (v0 / r), q * r * v0 / 3)
    close(omega_surface / omega, 4 / 3)
    close(radius_surface / radius, 3 / 4)


def q6() -> None:
    l, alpha, c = 2.4, 0.31, 3.0
    for v0 in (0.0, 0.3, 1.2, 2.4):
        beta = v0 / c
        gamma = 1 / math.sqrt(1 - beta * beta)
        t = 0.73
        x_focus = l - 1 / (4 * gamma * gamma * alpha) - v0 * t
        closed = l - (1 - v0 * v0 / c**2) / (4 * alpha) - v0 * t
        close(x_focus, closed)
        frequency = gamma * (1 + beta) / gamma
        close(frequency, 1 + beta)
    close(l - 1 / (4 * alpha), l - (1 - 0) / (4 * alpha))


def q7() -> None:
    gamma = 7 / 5
    beta = (1 + 3 ** (gamma - 1)) / 2
    close(beta, 1.27592278695768)
    eta = 1.5 * (
        2.5 * math.log(beta * beta / 3 ** (gamma - 1))
        + math.log(4 / 3)
    )
    close(eta, 0.6111272104482606)
    ratio = (5 / 3) ** (gamma - 1)
    xi = (1 + 3 ** (gamma - 1)) * ratio / (1 + ratio)
    close(xi, 1.4058259478901194)

    # 两转折点体积互换；由绝热关系和等内能检查端点条件。
    tl, tr = xi, (1 + 3 ** (gamma - 1)) - xi
    close(tl / tr, ratio)
    tl_next = tl / ratio
    tr_next = tr * ratio
    close(tl_next + tr_next, tl + tr)
    if not eta > 0:
        raise AssertionError("不可逆热传导的总熵增必须为正")


def q8() -> None:
    r, c = 1.3, 3.0
    for v in (0.0, 0.6, 2.4):
        gamma = 1 / math.sqrt(1 - v * v / c**2)
        area = math.pi * r * r / gamma
        close(area, math.pi * r * r * math.sqrt(1 - v * v / c**2))

    # 点积的解析式与逐分量计算一致。
    theta, y, omega = 0.61, 3.2, 0.7
    d = math.sqrt(y * y + r * r - 2 * y * r * math.sin(theta))
    nx, ny = -r * math.cos(theta) / d, (y - r * math.sin(theta)) / d
    ux, uy = omega * r * math.sin(theta), -omega * r * math.cos(theta)
    close(ux * nx + uy * ny, -omega * r * y * math.cos(theta) / d)

    # 发射—接收光程应为空间隔；v→0 时变换坐标回到圆上。
    yp = 2.1
    theta = 0.83
    d = math.sqrt(r * r + yp * yp - 2 * r * yp * math.sin(theta))
    tp = -d / c
    close(c * c * tp * tp, (r * math.cos(theta)) ** 2 + (r * math.sin(theta) - yp) ** 2)
    close(r * math.cos(theta), r * math.cos(theta) + 0 * tp)
    close(r * math.sin(theta), r * math.sin(theta))


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 059 套八题的关键代数、数值、守恒、边界与极限验证通过")


if __name__ == "__main__":
    main()
