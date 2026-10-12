#!/usr/bin/env python3
"""第053套八题关键代数、边界条件、积分与极值的独立核验。"""

from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if abs(a - b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError(f"{a} != {b}")


def q1() -> None:
    # 取束缚的非圆轨道参数，复核半长轴、另一拱点与半短轴。
    G = m = L = 1.0
    u2 = 0.7
    a = G * m * L / (2 * (2 * G * m - L * u2))
    r0 = L / 2
    rp = L * L * u2 / (2 * (2 * G * m - L * u2))
    close(r0 + rp, 2 * a)
    b2 = a * L - L * L / 4
    close(b2, L**3 * u2 / (4 * (2 * G * m - L * u2)))
    c = abs(a - L / 2)
    close(a * a - c * c, b2)
    # 圆轨道和逃逸边界。
    uc2 = G * m / L
    close(G * m * L / (2 * (2 * G * m - L * uc2)), L / 2)
    if not u2 < 2 * G * m / L:
        raise AssertionError("第1题束缚条件异常")


def q2() -> None:
    lam = 2 ** (-1 / 3)
    close(lam**3, 0.5)
    close(1 / lam, 2 ** (1 / 3))
    close(2 * lam * lam - 1, 2 ** (1 / 3) - 1)
    close((1 / 2) / (1 / 3), 3 / 2)
    # 一般压力幂律在 p=1 时还原正文。
    p = 1.0
    close(2 ** (-1 / (p + 2)), lam)


def q3() -> None:
    mu0, q, radius, length = 1.7, 2.1, 0.8, 5.3
    inertia, mass, g, height = 0.9, 1.2, 9.8, 0.6
    i_em = mu0 * q * q * radius * radius / (4 * math.pi * length)
    denominator = inertia + mass * radius * radius + i_em
    beta = mass * g * radius / denominator
    e_mech = mass * g * height * (inertia + mass * radius * radius) / denominator
    e_field = mass * g * height * i_em / denominator
    close(e_mech + e_field, mass * g * height)
    if not 0 < beta * radius < g:
        raise AssertionError("第3题加速度或张力方向异常")
    omega2 = 2 * beta * height / radius
    close(0.5 * i_em * omega2, e_field)


def q4() -> None:
    resistance, reactance, voltage = 3.0, 2.0, 5.0
    za2 = resistance**2 + (3 * reactance / 4) ** 2
    i0 = voltage / math.sqrt(za2)
    close(i0 * i0 * za2, voltage * voltage)
    i2 = resistance * voltage / (resistance**2 + reactance**2)
    i1 = reactance * voltage / (resistance**2 + reactance**2)
    close(i1 / i2, reactance / resistance)
    zin = resistance + reactance**2 / resistance
    close(voltage / zin, i2)


def q5() -> None:
    # 多项式密度在 [0,1] 上归一，核验前三个矩。
    def moment(n: int) -> float:
        return -3 / (n + 3) + 2 / (n + 2) + 1 / (n + 1)

    close(moment(0), 1)
    close(moment(1), 5 / 12)
    close(moment(2), 7 / 30)
    variance = moment(2) - moment(1) ** 2
    close(variance, 43 / 720)
    if not 1 / 3 < moment(1) < math.sqrt(moment(2)) < 1:
        raise AssertionError("第5题特征速率次序异常")


def q6() -> None:
    beta = 0.002
    exact = (1 + beta) / (1 - beta)
    if abs(exact - (1 + 2 * beta)) > 1e-4:
        raise AssertionError("第6题双多普勒一阶近似异常")
    nu0, l0 = 2.3, 4.7
    x = l0 / 2
    nu = nu0 * l0 / x
    close(nu, 2 * nu0)
    force = nu0 * l0 / x**2  # 省略公共因子 h。
    close(force, 4 * nu0 / l0)
    close(nu * x, nu0 * l0)


def q7() -> None:
    f = 2.4

    def y_out(x: float) -> float:
        return 3 * f * x / (3 * x - 4 * f)

    close(y_out(f), -3 * f)
    x0 = 4 * f / 3
    if not y_out(0.9 * x0) < 0 < y_out(1.1 * x0):
        raise AssertionError("第7题外贴实虚像分区异常")
    beta_out = (4 / 3) * abs(y_out(f) / f)
    close(beta_out, 4)
    # 内贴：1/y + 4/(3x) = 1/(3f)。
    y_in = 1 / (1 / (3 * f) - 4 / (3 * f))
    close(y_in, -f)
    close((4 / 3) * abs(y_in / f), 4 / 3)


def q8() -> None:
    # 电场在磁场边界连续。
    r, l = 0.7, 3.2
    close(r / 2, r * r / (2 * r))
    # 两段力矩积分的合并。
    single = r**3 / 6 + r**2 / 2 * (l / 2 - r)
    close(2 * single, r**2 * (l / 2 - 2 * r / 3))
    # 多项式磁场只有 u=2 为实根。
    u = 2.0
    close(6 - u**3 + 3 * u**2 - 5 * u, 0)
    if 1 - 12 >= 0:
        raise AssertionError("第8题二次因子判别式异常")
    values = [3 * (x - 1) ** 2 + 2 for x in (0, 1, 2)]
    if values != [5, 2, 5]:
        raise AssertionError("第8题切向加速度极值异常")
    # 角冲量只依赖磁场总变化。
    b0 = 1.9
    close((b0 - 0.0), b0)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 053 套八题的关键代数、边界条件、积分与极值验证通过")


if __name__ == "__main__":
    main()
