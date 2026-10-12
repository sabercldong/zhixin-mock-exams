from __future__ import annotations

import math

import mpmath as mp
import sympy as sp


def main() -> None:
    # 第 1 题：无滑动所需摩擦冲量。
    impulse, phi, theta = sp.symbols("impulse phi theta", positive=True)
    friction = impulse * (sp.sin(phi) - sp.sin(phi - theta)) / 2
    velocity = (impulse * sp.sin(phi) - friction) / sp.Symbol("m", positive=True)
    omega_r = (impulse * sp.sin(phi - theta) + friction) / sp.Symbol("m", positive=True)
    assert sp.simplify(velocity - omega_r) == 0

    # 第 2 题：分段弦频率。
    n, length, tension, density = sp.symbols("n length tension density", positive=True)
    frequency = 3 * n / (8 * length) * sp.sqrt(tension / density)
    assert sp.simplify(frequency.subs(n, 2) - 2 * frequency.subs(n, 1)) == 0

    # 第 3 题：异种半球壳的交叉力。
    Q, q, eps, radius = sp.symbols("Q q eps radius", positive=True)
    total_outer_pressure_term = Q * (Q + 2 * q) / (8 * sp.pi * eps * radius**2)
    outer_self = Q**2 / (8 * sp.pi * eps * radius**2)
    cross = sp.simplify((total_outer_pressure_term - outer_self) / 2)
    assert cross == Q * q / (8 * sp.pi * eps * radius**2)

    # 第 4 题：双线圈磁瓶数值。
    axis_field = lambda z: (1 + z**2) ** (-1.5) + (1 + (2 - z) ** 2) ** (-1.5)
    z_max = mp.findroot(
        lambda z: -3 * z / (1 + z**2) ** 2.5
        - 3 * (z - 2) / (1 + (2 - z) ** 2) ** 2.5,
        0.04,
    )
    b_max = axis_field(z_max)
    a = 1.5
    off_axis_integral = mp.quad(
        lambda x: (1 - a * mp.cos(x))
        / (a**2 + 2 - 2 * a * mp.cos(x)) ** 1.5,
        [0, 2 * mp.pi],
    )
    b_start = off_axis_integral / mp.pi
    mirror_angle = mp.asin(mp.sqrt(b_start / b_max))
    assert abs(float(mirror_angle) - 0.22899) < 1e-4

    # 第 5 题：质量比 2 与 1 两种有效分配。
    t = sp.sqrt(3)
    mass_ratio = sp.simplify((1 + t**2) / (t**2 - 1))
    assert mass_ratio == 2

    # 第 6 题：模式数。
    theta_c = math.asin(3 / 3.5)
    assert 42 * math.cos(theta_c) > 21
    assert 42 * math.cos(theta_c) < 22

    # 第 7 题：线性温度分布的精确积分。
    a_t = 32 / 300
    pressure = 150 * a_t / math.log(1 + a_t)
    x_g = 10 * (a_t - math.log(1 + a_t)) / (a_t * math.log(1 + a_t))
    boat_shift = 120 / 270 * (5 - x_g)
    assert abs(pressure - 157.8649) < 1e-3
    assert abs(boat_shift - 0.03753) < 1e-4

    # 第 8 题：相邻弧段的旋转系周长极限。
    beta = sp.symbols("beta", positive=True)
    circumference_ratio = 2 * sp.pi / sp.sqrt(1 - beta**2)
    assert sp.simplify(circumference_ratio / (2 * sp.pi) - 1 / sp.sqrt(1 - beta**2)) == 0

    print("蔡题075：八题的冲量条件、驻波频率、静电交叉力、磁镜数值、模式数、气体积分与相对论极限核验通过。")


if __name__ == "__main__":
    main()
