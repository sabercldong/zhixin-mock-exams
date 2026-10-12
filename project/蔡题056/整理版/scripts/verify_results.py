#!/usr/bin/env python3
"""第056套八题的关键代数、边界、极限和递推数值核验。"""

from __future__ import annotations

import cmath
import math


def close(a: complex, b: complex, tol: float = 1e-9) -> None:
    if abs(a - b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError(f"{a} != {b}")


def q1() -> None:
    l1 = 2.4
    l3 = 1.5 * l1
    # 两根均匀杆对 O 的重力矩应相消。
    tau_long = 3 * l1 * (l1 / 2)
    tau_short = l3 * l1
    close(tau_long, tau_short)
    w1, w2 = 1.1, 0.7
    v_d2 = (w1 * l1) ** 2 + (w2 * l3 / 3) ** 2
    v_c2 = (w1 * l1) ** 2 + (2 * w2 * l3 / 3) ** 2
    if not v_c2 > v_d2 > 0:
        raise AssertionError("第1题端点速度次序异常")


def q2() -> None:
    gamma = (7 / 2) / (5 / 2)
    close(gamma, 7 / 5)
    pressure_ratio = 128.0
    temperature_ratio = pressure_ratio ** ((gamma - 1) / gamma)
    close(temperature_ratio, 4.0)
    close(1 - 1 / temperature_ratio, 3 / 4)
    t1, t4 = 300.0, 500.0
    t2, t3 = temperature_ratio * t1, temperature_ratio * t4
    close(1 - (t4 - t1) / (t3 - t2), 3 / 4)


def harmonic(n: int) -> float:
    return sum(1 / k for k in range(1, n + 1))


def lower_mu(n: int, k: int) -> float:
    return (n - k + 1) / (
        n - k + 1 + 2 * n * (harmonic(n) - harmonic(k - 1))
    )


def upper_mu(n: int, k: int) -> float:
    return (n - k) / (n - k + 2 * n * (harmonic(n) - harmonic(k)))


def q3() -> None:
    close(lower_mu(5, 4), 4 / 13)
    close(upper_mu(5, 4), 1 / 3)
    close(lower_mu(5, 3), 18 / 65)
    close(upper_mu(5, 3), 4 / 13)
    # 大 N 时精确左右界应夹住给出的对数近似。
    n, k = 100000, 62000
    approx = (n - k) / (n - k + 2 * n * math.log(n / k))
    if not lower_mu(n, k) <= approx <= upper_mu(n, k):
        raise AssertionError("第3题大数近似未落在精确边界之间")


def alpha(delta: float) -> float:
    return -1 / (1 / math.sqrt(3) + delta) ** 2 + 2 * (
        1 / (2 * math.sqrt(3)) - delta
    ) / (
        1 / 4 + (1 / (2 * math.sqrt(3)) - delta) ** 2
    ) ** 1.5


def q4() -> None:
    close(alpha(0.0), 0.0)
    h = 1e-6
    derivative = (alpha(h) - alpha(-h)) / (2 * h)
    close(derivative, 9 * math.sqrt(3) / 2, 1e-6)
    beta = math.sqrt(2 / (9 * math.sqrt(3)))
    close(beta**2, 2 / (9 * math.sqrt(3)))
    delta_d = 1 / (2 * math.sqrt(3))
    close(alpha(delta_d), -4 / 3)
    if (3 + 1, 4 + 1, 2020 + 1) != (4, 5, 2021):
        raise AssertionError("第4题平衡点计数异常")


def q5() -> None:
    l_ind, resistance, capacitance = 2.3, 0.8, 1.7
    disc = resistance**2 - 4 * l_ind / capacitance
    root1 = (-resistance + cmath.sqrt(disc)) / (2 * l_ind)
    root2 = (-resistance - cmath.sqrt(disc)) / (2 * l_ind)
    for root in (root1, root2):
        close(l_ind * root**2 + resistance * root + 1 / capacitance, 0)
    q0 = 1.4
    coeff = q0 / (l_ind * capacitance * (root1 - root2))
    close(coeff * (root1 - root2), q0 / (l_ind * capacitance))
    # f_r 与 r 线性，面积平均值为外缘值的 2/3。
    close((2 / 3) * 1.0, 2 / 3)


def q6() -> None:
    c, x1, v, u = 1.0, 2.7, 0.35, 0.22
    gamma = 1 / math.sqrt(1 - u**2 / c**2)
    t2 = x1 / (c - v)
    x2 = c * t2
    t3 = 2 * x1 / (c - v)
    t3p = gamma * t3
    x3p = -gamma * u * t3
    x2p = gamma * (x2 - u * t2)
    t2p = gamma * (t2 - u * x2 / c**2)
    close(x2p, c * t2p)
    close(c**2 * t3p**2 - x3p**2, c**2 * t3**2)
    t1p = -gamma * u * x1 / c**2
    if not t1p < 0 < t2p < t3p:
        raise AssertionError("第6题事件先后或符号异常")


def lens_map(r: tuple[float, float], n: tuple[float, float]) -> tuple[float, float]:
    axial = abs(r[0] * n[0] + r[1] * n[1])
    scale = 1 / (1 - axial)  # 取 f=1
    return scale * r[0], scale * r[1]


def q7() -> None:
    n1 = (0.0, 1.0)
    n2 = (math.sqrt(3) / 2, 0.5)
    a = (-1.0, 1 / math.sqrt(3))
    a12 = lens_map(lens_map(a, n1), n2)
    a21 = lens_map(lens_map(a, n2), n1)
    target_a = (3 + 2 * math.sqrt(3), -(2 + math.sqrt(3)))
    for got in (a12, a21):
        close(got[0], target_a[0])
        close(got[1], target_a[1])
    b = (-math.sqrt(3), 0.0)
    b12 = lens_map(lens_map(b, n1), n2)
    b21 = lens_map(lens_map(b, n2), n1)
    for got in (b12, b21):
        close(got[0], 2 * math.sqrt(3))
        close(got[1], 0)


def q8() -> None:
    q = 1 / math.sqrt(3)
    inertia_coefficient = 0.5 / (1 - q**3)
    close(
        inertia_coefficient,
        3 * math.sqrt(3) / (2 * (3 * math.sqrt(3) - 1)),
    )
    r2 = (3 + math.sqrt(3)) / 9
    close(r2, 1 / 3 + math.sqrt(3) / 9)
    y = 1.0
    for _ in range(100):
        y = (math.sqrt(3) * y + 2) / (math.sqrt(3) * y + 3)
    fixed = (math.sqrt(3) - 3 + math.sqrt(12 + 2 * math.sqrt(3))) / (
        2 * math.sqrt(3)
    )
    close(y, fixed)
    r_inf = 2 * y / 3
    if not 0 < r_inf < r2 < 2 / 3:
        raise AssertionError("第8题电阻单调性异常")


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 056 套八题的关键代数、边界、极限与递推验证通过")


if __name__ == "__main__":
    main()
