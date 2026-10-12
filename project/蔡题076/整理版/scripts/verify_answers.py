from __future__ import annotations

import math

import mpmath as mp
import sympy as sp


def main() -> None:
    # 第 1 题：均匀球引力能、黑体功率与相似恒星温标。
    G, M, R, c = sp.symbols("G M R c", positive=True)
    binding = sp.Rational(3, 5) * G * M**2 / R
    temperature = binding / (M * c)
    assert sp.simplify(temperature - sp.Rational(3, 5) * G * M / (R * c)) == 0

    # 第 2 题：三电荷能量式及周期积分系数。
    s = sp.symbols("s", positive=True)
    velocity_factor = (2 * s**2 - s) / (9 - 6 * s**2)
    assert sp.simplify(velocity_factor.subs(s, 1) - sp.Rational(1, 3)) == 0
    integral = mp.quad(
        lambda th: mp.sin(th)
        * mp.sqrt((9 - 6 * mp.sin(th) ** 2) / (2 * mp.sin(th) ** 2 - mp.sin(th))),
        [mp.pi / 6, mp.pi / 2],
    )
    assert abs(float(mp.re(integral)) - 3.28556) < 1e-4

    # 第 3 题：三圆盘零合力方程的唯一相关数值根。
    root = mp.findroot(
        lambda lam: mp.log(lam**2 / (lam**2 - 1)) / (2 * lam**2)
        - 2 * (1 - 1 / lam**2),
        1.16,
    )
    assert abs(float(root) - 1.158384762) < 1e-8

    # 第 4 题：半功率两根的差。
    a, L, C = sp.symbols("a L C", positive=True)
    omega_plus = (sp.sqrt(1 + a**2) + a) / sp.sqrt(L * C)
    omega_minus = (sp.sqrt(1 + a**2) - a) / sp.sqrt(L * C)
    assert sp.simplify(omega_plus - omega_minus - 2 * a / sp.sqrt(L * C)) == 0

    # 第 5 题：最高点角加速度、法向铰链力及可行域判定。
    alpha, beta, theta, omega0 = sp.symbols("alpha beta theta omega0", positive=True)
    f = (1 + sp.pi * alpha) ** 2 - (1 + alpha * theta) ** 2 - beta * (1 + sp.cos(theta))
    assert sp.simplify(omega0**2 * sp.diff(f, theta).subs(theta, 0) + 2 * omega0**2 * alpha) == 0
    top_speed_sq = 2 * omega0**2 * f.subs(theta, 0)
    # 使用 omega0^2=k/m，并提出公共因子 kL 后，F_perp/(kL) 如下。
    f_perp_scaled = sp.simplify(top_speed_sq / (2 * omega0**2) - 1 - beta)
    expected_f_perp = (1 + sp.pi * alpha) ** 2 - 2 - 3 * beta
    assert sp.simplify(f_perp_scaled - expected_f_perp) == 0
    # 可达性与防倾覆若要同时成立，至少要求
    # 8 alpha^2 > (1+pi alpha)^2+1；但其左右差对 alpha>0 恒负。
    feasibility_gap = sp.expand(8 * alpha**2 - (1 + sp.pi * alpha) ** 2 - 1)
    assert sp.expand(feasibility_gap - ((8 - sp.pi**2) * alpha**2 - 2 * sp.pi * alpha - 2)) == 0
    assert float(8 - sp.pi**2) < 0

    # 第 6 题：热力学数值核验。
    n, gas_R, t1, p1 = 2, 8.314, 298.0, 1.01e5
    v1 = n * gas_R * t1 / p1
    v2, v3 = v1 / 4, 15.0e-3
    gamma = 7 / 5
    t3 = t1 * (v2 / v3) ** (gamma - 1)
    work_a = n * gas_R * t1 * math.log(4)
    q_out = n * (5 * gas_R / 2) * (t1 - t3) + n * gas_R * t3 * math.log(v1 / v3)
    efficiency = 1 - q_out / work_a
    assert 0.071 < efficiency < 0.073

    # 第 7 题：镜像线电荷修正的量纲结构。
    k_e, q, ell, radius, distance = sp.symbols("k_e q ell radius distance", positive=True)
    electric_energy = k_e * q**2 / ell * sp.log(2 * distance / radius)
    electric_force = -sp.diff(electric_energy, ell)
    correction = ell / (sp.pi * radius**2) * sp.diff(electric_force, ell)
    expected = -2 * k_e * q**2 / (sp.pi * radius**2 * ell**2) * sp.log(2 * distance / radius)
    assert sp.simplify(correction - expected) == 0

    # 第 8 题：配方后的场致能量平移。
    x, mass, omega, charge, field = sp.symbols("x mass omega charge field", positive=True)
    potential = mass * omega**2 * x**2 / 2 - charge * field * x
    shifted = mass * omega**2 * (x - charge * field / (mass * omega**2)) ** 2 / 2 - charge**2 * field**2 / (2 * mass * omega**2)
    assert sp.expand(potential - shifted) == 0

    print("蔡题076：八题解析中的关键代数式、数值根、积分系数与热力学数值核验通过。")


if __name__ == "__main__":
    main()
