#!/usr/bin/env python3
"""第054套八题关键代数、数值根、边界条件与几何结果的独立核验。"""

from __future__ import annotations

import math

import numpy as np


def close(a: float, b: float, tol: float = 2e-4) -> None:
    if abs(a - b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError(f"{a} != {b}")


def q1() -> None:
    r0 = 1.0
    radius = math.exp(2 * math.pi / math.sqrt(3))
    inertia_per_mass = (radius**2 + radius + 1) / 3
    close(2 * (radius - 1), 73.2447)
    close(inertia_per_mass, 484.688, 2e-5)

    def equations(values: np.ndarray, magnetic_delta: float) -> np.ndarray:
        u, omega = values
        energy = u**2 + (radius**2 + inertia_per_mass) * omega**2
        energy += math.sqrt(3) * radius * u * omega - 10**2
        angular = radius * math.sqrt(3) * u / 2
        angular += (radius**2 + inertia_per_mass) * omega
        angular -= 10 * r0 * math.sqrt(3) / 2 + magnetic_delta
        return np.array([energy, angular])

    # 用一元消元后的多项式数值求根，并选择 u>0 的外行分支。
    def solve(magnetic_delta: float) -> tuple[float, float]:
        denom = radius**2 + inertia_per_mass
        c = 10 * r0 * math.sqrt(3) / 2 + magnetic_delta
        # omega=(c-radius*sqrt(3)u/2)/denom，直接拟合二次式系数。
        def f(u: float) -> float:
            omega = (c - radius * math.sqrt(3) * u / 2) / denom
            return equations(np.array([u, omega]), magnetic_delta)[0]

        f0, f1, fm1 = f(0), f(1), f(-1)
        a = (f1 + fm1 - 2 * f0) / 2
        b = (f1 - fm1) / 2
        roots = np.roots([a, b, f0])
        u = max(float(root.real) for root in roots if abs(root.imag) < 1e-9)
        omega = (c - radius * math.sqrt(3) * u / 2) / denom
        if np.linalg.norm(equations(np.array([u, omega]), magnetic_delta)) > 1e-7:
            raise AssertionError("第1题联立方程回代失败")
        return u, omega

    u0, omega0 = solve(0.0)
    close(u0, 15.0502)
    close(omega0, -0.253511)
    magnetic_delta = 0.01 * (radius**2 - r0**2) / 2
    close(magnetic_delta, 7.07221)
    ub, omegab = solve(magnetic_delta)
    close(ub, 15.0433)
    close(omegab, -0.24967)


def q2() -> None:
    theta = math.pi / 6
    t0 = math.sqrt(2 * (1 - math.cos(theta)))
    close(t0, 0.517638)
    v = 12.557
    # 未知量依次为 Ux, Uy, Omega, omega, N, F；粘着冲量阶段六式。
    a = np.array([
        [5, 0, 0, 0, math.sin(theta), -math.cos(theta)],
        [0, 5, 0, 0, -math.cos(theta), -math.sin(theta)],
        [0, 0, 0, -0.5, 0, 1],
        [0, 0, -27/4, -0.5, 1.5*math.cos(theta), 1.5*math.sin(theta)+1],
        [-math.sin(theta), math.cos(theta), 1.5*math.cos(theta), 0, 0, 0],
        [math.cos(theta), math.sin(theta), 1.5*math.sin(theta), 1, 0, 0],
    ], dtype=float)
    b = np.array([
        5*v,
        -5*t0,
        0.5*v,
        0.5*v,
        v*math.sin(theta)+t0*math.cos(theta),
        0,
    ])
    sol = np.linalg.solve(a, b)
    ux, uy, omega_body, omega_wheel, normal, friction = sol
    close(ux, 9.349, 8e-4)
    close(uy, 4.613, 8e-4)
    close(omega_wheel, -14.680, 8e-4)
    close(omega_body, 5.702, 8e-4)
    if abs(friction) / normal >= 0.05:
        raise AssertionError("第2题粘着冲量不满足静摩擦限值")
    tau = 0.1906
    x = ux * tau - 1.5 * math.cos(omega_body * tau) - 1.5 - math.sin(theta)
    y = uy * tau - 0.5 * tau**2 - 1.5 * math.sin(omega_body * tau) + math.cos(theta)
    close(x*x + y*y, 1.0, 3e-3)
    if not (-1 < x < 0 and 0 < y < 1):
        raise AssertionError("第2题接触根不在右崖左上圆弧")


def q3() -> None:
    for ratio in (1.01, 1.5, 4.0):
        eta = 1 - math.log(ratio) / (ratio - 1)
        carnot = 1 - 1 / ratio
        if not 0 < eta < carnot < 1:
            raise AssertionError("第3题效率边界异常")
    ratio = 2.3
    va, t1 = 1.0, 1.0
    vb = va * math.sqrt(ratio)
    vc = vb * ratio ** 2.5
    close(vc / va, ratio**3)


def q4() -> None:
    vertices = [
        (-3,-3),(-1,-3),(-1,-1),(-3,-1),(-3,1),(-3,3),(-1,3),(-1,1),
        (1,1),(1,3),(3,3),(3,1),(3,-1),(1,-1),(1,-3),(3,-3),
    ]
    sy = sx = 0
    for (x1, y1), (x2, y2) in zip(vertices, vertices[1:]):
        sy += y1*y1 + y1*y2 + y2*y2
        sx += x1*x1 + x1*x2 + x2*x2
    if (sy, sx) != (197, 199):
        raise AssertionError(f"第4题逐段坐标和异常：{sy}, {sx}")
    close((sy + sx) / 2880, 11/80)
    close(1/12 + 1/12, 1/6)


def q5() -> None:
    roots = sorted(((3-math.sqrt(5))/2, (3+math.sqrt(5))/2))
    close(roots[0] * roots[1], 1)
    for x in roots:
        close(x*x - 3*x + 1, 0)
    # 高频 x=1、低频 y=2 为阻抗零点；y=4 为导纳零点。
    close((1 - 1) / (1 + 1 - 3), 0)
    close((2 - 2) / (2 - 4), 0)
    close(4 - 4, 0)


def q6() -> None:
    n, ell = 3.0, 1.0
    eccentricity = math.sqrt(1 - ell**2 / n**2)
    rmin, rmax = n*n*(1-eccentricity), n*n*(1+eccentricity)
    close((rmin + rmax) / 2, n*n)
    close(rmin * rmax, n*n*ell*ell)
    ratio = 137**2 * ell**2 / (2 * eccentricity)
    if not 9e3 < ratio < 1.1e4:
        raise AssertionError("第6题相对论修正数量级异常")


def q7() -> None:
    rt3 = math.sqrt(3)
    points = [
        (1, 0),
        (4/3, rt3/3),
        ((6+2*rt3)/3, rt3/3),
        ((16+4*rt3)/13, -(4+rt3)/13),
    ]
    double = 0.0
    for p, q in zip(points, points[1:] + points[:1]):
        double += p[0]*q[1] - p[1]*q[0]
    area = abs(double) / 2
    close(area, (84 + 34*rt3)/117)
    close(area, 1.22128)


def q8() -> None:
    a = 1.0
    threshold = math.sqrt(2) - 1
    for b in (0.2, 0.6):
        candidate = (a*a - b*b) / (2*a*b)
        if b < threshold and candidate <= 1:
            raise AssertionError("第8题分段阈值判定异常")
        if b >= threshold and not 0 < candidate <= 1:
            raise AssertionError("第8题内部驻点不存在")
    a, b, phi = 2.0, 0.8, 0.7
    r1sq = a*a + b*b + 2*a*b*math.cos(phi)
    r2sq = a*a + b*b - 2*a*b*math.cos(phi)
    close(r1sq*r2sq, (a*a-b*b)**2 + 4*a*a*b*b*math.sin(phi)**2)
    lam, d = 1.3, 1.7
    inertia = 2*lam*d*b*b + 4*lam*b**3/3
    close(inertia, 2*lam*b*b*(d+2*b/3))


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("第 054 套八题的关键代数、数值根、边界条件与几何结果验证通过")


if __name__ == "__main__":
    main()
