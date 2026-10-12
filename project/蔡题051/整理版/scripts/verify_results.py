#!/usr/bin/env python3
"""第051套八题关键几何、方程、数值与极限的独立核验。"""

from __future__ import annotations

import cmath
import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if abs(a - b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError(f"{a} != {b}")


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def q1() -> None:
    ell, d1, d2, theta, omega1, x = 0.12, 0.04, 0.07, 0.8, 25.0, 0.01
    factor = 0.5 * math.tan(theta / 2)
    r1, r2 = factor * (ell - d1), factor * (ell - d2)
    r1p, r2p = factor * (ell - d1 + x), factor * (ell - d2 - x)
    close((r1p - r1) + (r2p - r2), 0)
    close(omega1 * r1 / r2, omega1 * (ell - d1) / (ell - d2))
    close(omega1 * r1p / r2p, omega1 * (ell - d1 + x) / (ell - d2 - x))


def q2() -> None:
    abar = math.acos(5 / 13) - 60 / 169
    density_ratio = 2 * abar / math.pi
    close(density_ratio, 0.52265, 2e-5)
    h_over_r = 4 / (3 * math.pi)
    t1 = 2 * math.pi * math.sqrt(13 * abar / 24)
    t2 = 2 * math.pi * math.sqrt(3 * math.pi / 8)
    if not (0 < density_ratio < 1 and t1 > 0 and t2 > 0):
        raise AssertionError("第2题无量纲量异常")
    n = 1e4 * h_over_r * 0.01 / 4
    close(n, 100 / (3 * math.pi))


def q3() -> None:
    mu, alpha, radius = 0.8, 0.7, 2.0
    theta_c = 2 * math.atan(math.exp(-mu * math.pi / 2))
    close(math.tan(theta_c / 2), math.exp(-mu * math.pi / 2))
    psi = 2 * math.atan(math.exp(-mu * alpha))
    close(math.sin(psi), 1 / math.cosh(mu * alpha))
    close(math.cos(psi), math.tanh(mu * alpha))
    z = radius / mu * (math.cosh(mu * alpha) - 1)
    dz = radius * math.sinh(mu * alpha)
    close(dz, radius / math.tan(psi))
    if not (0 < theta_c < math.pi / 2 and z > 0):
        raise AssertionError("第3题临界角或轨迹异常")


def q4() -> None:
    q = 1 / 81
    uxx, uyy = 3 / 4, 9 / 4
    uxy = 3 * math.sqrt(3) / 4 * (1 - 2 * q)
    close(uxx * uyy - uxy * uxy, 27 * q * (1 - q) / 4)
    disc = 1 - 27 * q * (1 - q)
    if not disc > 0:
        raise AssertionError("第4题地月质量比不稳定")
    x1 = (-1 + math.sqrt(disc)) / 2
    x2 = (-1 - math.sqrt(disc)) / 2
    if not (x1 < 0 and x2 < 0):
        raise AssertionError("第4题特征根的平方不全为负")
    qc = 0.5 * (1 - math.sqrt(23 / 27))
    if not q < qc:
        raise AssertionError("第4题临界质量分数异常")


def q5() -> None:
    rt = math.sqrt
    pts = {
        "A": (1 / rt(3), 0, -1 / (2 * rt(6))),
        "B": (-1 / (2 * rt(3)), 1 / 2, -1 / (2 * rt(6))),
        "C": (-1 / (2 * rt(3)), -1 / 2, -1 / (2 * rt(6))),
        "D": (0, 0, rt(6) / 4),
    }
    for i in pts:
        summed = [0.0, 0.0, 0.0]
        for j in pts:
            if i == j:
                continue
            c = cross(pts[i], pts[j])
            for k in range(3):
                summed[k] += c[k]
        close(sum(abs(v) for v in summed), 0)
    ead = -0.5 * cross(pts["A"], pts["D"])[1]
    eab_y = -0.5 * cross(pts["A"], pts["B"])[1]
    eab_x = -0.5 * cross(pts["A"], pts["B"])[0]
    close(ead, math.sqrt(2) / 8)
    close(abs(eab_y), math.sqrt(2) / 16)
    close(abs(complex(eab_y, eab_x)) ** 2, 1 / 96)
    close(abs(ead) ** 2 / 2, 1 / 64)


def q6() -> None:
    qa, qb, qc = 2.5, 7.0, -9.0
    wa, wb, wc = 0.0, 2.0, -1.5
    close(qa + qb + qc, wa + wb + wc)
    close((wa + wb + wc) / (qa + qb), 1 / 19)
    close(math.sqrt(4), 2)


def q7() -> None:
    cosc, sinc = -math.sqrt(2 / 5), -math.sqrt(3 / 5)
    close(2 * sinc * sinc, 3 * cosc * cosc)
    time = 3 * math.sqrt(2) * (3 / 5) ** 0.25
    close(time, 6 / math.sqrt(2) * math.sqrt(math.sqrt(3 / 5)))
    delta = math.atan(1 / math.sqrt(2))
    close(math.tan(delta) ** 3, 1 / (2 * math.sqrt(2)))
    i1 = math.pi + math.atan(1 / (2 * math.sqrt(2)))
    i3 = 3 * math.pi / 2 - math.atan(1 / (2 * math.sqrt(2)))
    close(math.degrees(i1), 199.471220634, 1e-9)
    close(math.degrees(i3), 250.528779366, 1e-9)


def q8() -> None:
    hbar, c, p, d = 1.054571817e-34, 2.99792458e8, 2000, 1e-3
    force = math.pi * hbar * c * p * (p + 1) / (4 * d * d)
    close(force, 9.94e-14, 3e-4)
    energy = math.pi * hbar * c * p * (p + 1) / (4 * d)
    close(force, energy / d)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 051 套八题的关键几何、方程、数值与极限验证通过")


if __name__ == "__main__":
    main()
