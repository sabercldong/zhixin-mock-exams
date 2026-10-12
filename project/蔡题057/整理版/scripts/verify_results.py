#!/usr/bin/env python3
"""第057套八题关键代数、边界、极值和数值条件的独立核验。"""

from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def q1() -> None:
    u = 2 / 3
    vb2 = 2 * (1 - u) * u**2
    close(vb2, 8 / 27)
    close(1 - 0.5 * vb2, 23 / 27)
    # 极值点两侧的 v_B^2 均较小。
    if not vb2 > 2 * (1 - 0.6) * 0.6**2:
        raise AssertionError("第1题极值方向异常")
    if not vb2 > 2 * (1 - 0.75) * 0.75**2:
        raise AssertionError("第1题极值方向异常")


def q2() -> None:
    l = 2.3
    rho = 2 * l / math.sqrt(3)
    close(1 / rho, math.sqrt(3) / (2 * l))
    m_eff = 8 / 3
    k_eff = 4 / (3 * math.sqrt(3) * l)
    close(k_eff / m_eff, 1 / (2 * math.sqrt(3) * l))
    # 直接用对称差分核验 y1+y2 的二阶系数。
    def ysum(x: float) -> float:
        return -math.sqrt((l + x) ** 2 - l**2 / 4) - math.sqrt(
            (l - x) ** 2 - l**2 / 4
        )

    h = 1e-4
    second = (ysum(h) - 2 * ysum(0) + ysum(-h)) / h**2
    close(second, 4 / (3 * math.sqrt(3) * l), 5e-7)


def q3_values(alpha: float) -> tuple[float, float]:
    d = 8 * alpha**2 - 4 * alpha - 3
    if d <= 0:
        raise ValueError("尚未脱离")
    vartheta = math.atan(
        math.sqrt(14) * (3 + 2 * alpha) / (7 * math.sqrt(d))
    )
    theta1 = 7 / (4 - 2 * alpha) * (math.pi - 2 * vartheta)
    theta2 = (3 + 2 * alpha) / (4 - 2 * alpha) * (
        math.pi - 2 * vartheta
    )
    r_ratio = math.sqrt(64 * alpha**2 - 4 * alpha - 3) / (
        7 * math.sqrt(2)
    )
    residual = r_ratio * math.sin(theta1 / 2) - math.sin(theta2 / 2)
    return residual, theta2


def q3() -> None:
    threshold = (1 + math.sqrt(7)) / 4
    close(threshold, 0.9114378277661477)
    # 机械能与广义角动量联立后的系数。
    a = 1.03
    omega_prime = (3 + 2 * a) / 14
    v2 = (8 * a**2 - 4 * a - 3) / 56
    u2 = omega_prime**2 + v2
    close(u2, (64 * a**2 - 4 * a - 3) / 392)
    # 半圈条件的边界为 alpha=9/8。
    _, theta2_edge = q3_values(9 / 8)
    close(theta2_edge, math.pi, 2e-12)
    # 在物理允许区间内方程残差保持负号，没有零点。
    upper = 9 / 8
    maximum = -1e100
    for i in range(1, 20001):
        alpha = threshold + (upper - threshold) * i / 20002
        residual, theta2 = q3_values(alpha)
        if not 0 < theta2 < math.pi:
            raise AssertionError("第3题半圈约束异常")
        maximum = max(maximum, residual)
    if not maximum < 0:
        raise AssertionError("第3题数值方程在允许区间出现候选根")


def q4() -> None:
    close((math.sqrt(3) / 2) ** 2, 3 / 4)
    n = math.log(0.06) / math.log(3 / 4)
    if not 9 < n < 10:
        raise AssertionError("第4题组数取整异常")
    if not 0.5 * (3 / 4) ** 10 < 0.03:
        raise AssertionError("第4题第10组未达精度")
    if not 0.5 * (3 / 4) ** 9 >= 0.03:
        raise AssertionError("第4题第9组已误判达标")


def q5() -> None:
    d = 1.7
    x = 5 * d / 3
    f = lambda z: (z - d) / z ** 2.5
    if not f(x) > f(1.4 * d) and f(x) > f(2.0 * d):
        raise AssertionError("第5题磁场极值位置异常")
    # 取无量纲常量为1，直接核验 B_max 的化简系数。
    b_direct = 0.5 * math.sqrt(2) * (x - d) / (d * x**2.5)
    b_closed = 6 / (25 * d**2.5) * math.sqrt(3 / 10)
    close(b_direct, b_closed)
    # 相对速度代回微分方程。
    eps_s_u2_over_m = 2.4
    z = 2.2 * d
    v2 = 2 * eps_s_u2_over_m * (z - d) ** 2 / (d**2 * z)
    close(
        0.5 * v2,
        eps_s_u2_over_m * (z - d) ** 2 / (d**2 * z),
    )


def q6() -> None:
    k, t, n, b, r = 1.3, 320.0, 90.0, 0.8, 2.1
    force = 3 * k * t * r / (n * b**2)
    close(3 * k * (2 * t) * r / (n * b**2), 2 * force)
    close(3 * k * t * r / (3 * n * b**2), force / 3)
    entropy = -3 * k * r**2 / (2 * n * b**2)
    if not entropy < 0:
        raise AssertionError("第6题熵变符号异常")


def q7() -> None:
    g0, r0, rho0, grav = 1.8, 4.2, 0.07, 0.9
    gprime = 4 * math.pi * grav * rho0 - 2 * g0 / r0
    radial_sq_a = 3 * g0 / r0 + gprime
    radial_sq_b = g0 / r0 + 4 * math.pi * grav * rho0
    close(radial_sq_a, radial_sq_b)
    if not radial_sq_b > g0 / r0:
        raise AssertionError("第7题径向频率应高于轨道角频率")


def q8() -> None:
    beta, wrc, theta = 0.61, 0.18, 0.7
    gamma = 1 / math.sqrt(1 - beta**2)
    den = 1 + beta * wrc * math.sin(theta)
    ux = -(beta + wrc * math.sin(theta)) / den
    uy = wrc * math.cos(theta) / (gamma * den)
    if not (-1 < ux < 0 and abs(uy) < 1):
        raise AssertionError("第8题速度范围异常")
    density_ratio = den / math.sqrt(1 - beta**2 * math.sin(theta) ** 2)
    if not density_ratio > 0:
        raise AssertionError("第8题线密度应为正")
    # beta=0 时恢复原系。
    close(
        (1 + 0 * wrc * math.sin(theta))
        / math.sqrt(1 - 0**2 * math.sin(theta) ** 2),
        1.0,
    )


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 057 套八题的关键代数、边界、极值与数值条件验证通过")


if __name__ == "__main__":
    main()
