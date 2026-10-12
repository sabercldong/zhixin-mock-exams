#!/usr/bin/env python3
"""第055套八题关键代数、边界条件与数值结果的独立核验。"""

from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if abs(a - b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError(f"{a} != {b}")


def q1() -> None:
    theta, omega, v0, t = 0.43, 1.27, 2.1, 0.83
    x = v0 * math.sin(theta) ** 2 * t + v0 * math.cos(theta) ** 2 * math.sin(omega * t) / omega
    y = v0 * math.cos(theta) * (math.cos(omega * t) - 1) / omega
    z = v0 * math.sin(theta) * math.cos(theta) * t - v0 * math.sin(theta) * math.cos(theta) * math.sin(omega * t) / omega
    # 参数方程对时间求导后速度模应恒为 v0。
    vx = v0 * math.sin(theta) ** 2 + v0 * math.cos(theta) ** 2 * math.cos(omega * t)
    vy = -v0 * math.cos(theta) * math.sin(omega * t)
    vz = v0 * math.sin(theta) * math.cos(theta) * (1 - math.cos(omega * t))
    close(vx * vx + vy * vy + vz * vz, v0 * v0)
    period = 2 * math.pi / omega
    x_period = v0 * math.sin(theta) ** 2 * period
    z_period = v0 * math.sin(theta) * math.cos(theta) * period
    close(math.hypot(x_period, z_period) / period, v0 * math.sin(theta))
    if abs(y) + abs(x) + abs(z) <= 0:
        raise AssertionError("第1题轨迹退化")


def q2() -> None:
    lam0 = 589.3e-9
    delta_d = 20 * lam0 / 2
    close(delta_d, 5.893e-6)
    delta_lam = lam0 / 985
    close(delta_lam * 1e9, 0.5982741116751269)
    mirror_speed, beat = 6e-4, 2.54e3
    wavelength = 2 * mirror_speed / beat
    close(wavelength, 4.7244094488188975e-7)
    close(2 * mirror_speed * delta_lam / lam0**2, 2.0673241331666836)


def q3() -> None:
    alpha = 0.91
    u1, u2 = 1.3, -0.4
    tx = (1.0, 0.0)
    ty = (math.cos(alpha), math.sin(alpha))
    # 解 V·t1=u1, V·t2=u2，并复核两条无滑动投影约束。
    vx = u1
    vy = (u2 - u1 * math.cos(alpha)) / math.sin(alpha)
    close(vx * tx[0] + vy * tx[1], u1)
    close(vx * ty[0] + vy * ty[1], u2)
    speed = math.sqrt(u1**2 + u2**2 - 2 * u1 * u2 * math.cos(alpha)) / abs(math.sin(alpha))
    close(math.hypot(vx, vy), speed)


def q4() -> None:
    theta, length, gravity = 1.0, 2.3, 9.8
    c = math.cos(theta)
    omega2 = 3 * gravity * (1 - c) / length
    angular_acc = 3 * gravity * math.sin(theta) / (2 * length)
    if not omega2 > 0 or not angular_acc > 0:
        raise AssertionError("第4题转动状态符号异常")
    u0 = c / (3 * (1 - c))
    # 选取的角度应使拉力极大点落在杆内，且二阶导数为负。
    if not 0 < u0 < 1:
        raise AssertionError("第4题极值点不在实体区间")
    if not -3 * (1 - c) < 0:
        raise AssertionError("第4题拉力驻点不是极大值")


def lens_image(s: float, focal: float) -> float:
    return 1 / (1 / focal - 1 / s)


def q5() -> None:
    f = 1.0
    s1p = lens_image(1.5 * f, f)
    close(s1p, 3 * f)
    s2 = f - s1p
    close(s2, -2 * f)
    close(lens_image(s2, -f), -2 * f)
    close(lens_image(2 * f, f), 2 * f)
    a = 1 + math.sqrt(2)
    close(1 / (a - 2), a)


def q6() -> None:
    # 取 m=R=k=Q=g=1，验证第(1)问的势能抵消与各时间系数。
    m = r = k = charge = g = 1.0
    q = 2 * m * g * r**2 / (k * charge)
    close(m * g * r, k * charge * q / (2 * r))
    omega0 = math.sqrt(k * charge * q / (m * r**3))
    close(omega0**2, 2 * g / r)
    close(math.pi / omega0, math.pi * math.sqrt(r / (2 * g)))
    omega = math.sqrt(k * charge**2 / (m * r**3))
    v_surface = math.sqrt(k * charge**2 / (m * r))
    close(v_surface, omega * r)
    t_out = (math.pi + 2) / 2 * math.sqrt(m * r**3 / (k * charge**2))
    t_in = math.pi / 4 * math.sqrt(m * r**3 / (k * charge**2))
    if not t_out > t_in > 0:
        raise AssertionError("第6题分段时间次序异常")


def q7() -> None:
    theta = 0.77
    ratio = 0.5 * math.sqrt(1 + 3 * math.sin(theta) ** 2)
    omega_a2 = 3 * math.cos(theta)
    omega_b2 = 12 * math.cos(theta) / (1 + 3 * math.sin(theta) ** 2)
    close(math.sqrt(omega_a2 / omega_b2), ratio)
    # 取 m=l=I=1，复核三个冲量方程与整体角冲量。
    omega = 6 / 11
    h_joint = -omega / 3
    h = 6 / 11
    close(1 + h_joint, 1.5 * omega)
    close((0.5 - h) - h_joint * 0.5, omega / 12)
    close(2 - h, (8 / 3) * omega)


def q8() -> None:
    beta = 3 / 5
    gamma = 5 / 4
    root = 5 * (math.sqrt(41) - 3) / 16
    close((1 - beta**2) * root**2 + 2 * beta * root - 2, 0)
    nx = (math.sqrt(41) + 3) / 10
    ny = (math.sqrt(41) - 3) / 10
    close(nx * nx + ny * ny, 1)
    nxp = (nx - beta) / (1 - beta * nx)
    close(nxp, 5 / math.sqrt(41))
    close(math.sqrt(1 - nxp**2), 4 / math.sqrt(41))
    tprime_coeff = gamma * (root - beta)
    close(tprime_coeff, (25 * math.sqrt(41) - 123) / 64)
    distance_coeff = math.hypot(1 / gamma, 1 - beta**2)
    close(distance_coeff, 4 * math.sqrt(41) / 25)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 055 套八题的关键代数、边界条件与数值结果验证通过")


if __name__ == "__main__":
    main()
