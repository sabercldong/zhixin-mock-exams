from __future__ import annotations

import math
from fractions import Fraction

import sympy as sp


def close(actual: float, expected: float, tol: float = 1e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{actual=} != {expected=}")


def main() -> None:
    # 第 1 题：碰撞位置同余
    assert Fraction(3 * 2, 2 + 3) % 1 == Fraction(1, 5)
    assert Fraction(9 * 2, 2 + 9) % 1 == Fraction(7, 11)
    assert math.gcd(11, 14) == 1
    assert (11 * 2016) % 14 == 0

    # 第 2 题：RLC 数值与谐振频率
    resistance = 150.0
    omega_1 = 2 * math.pi * 1000
    inductance = resistance / (math.sqrt(3) * omega_1)
    capacitance = math.sqrt(3) / (4 * resistance * omega_1)
    close(inductance, 0.013783222385544804)
    close(capacitance, 4.594407461848267e-7)
    close(1 / (2 * math.pi * math.sqrt(inductance * capacitance)), 2000.0)

    # 第 3 题：调速器
    k, h1, alpha, ell = 350.0, 2.41, 485.0, 3.62
    mass_slider, mass_ball, gravity = 0.651, 1.25, 10.0
    omega_trial = math.sqrt(k * h1 / (2 * alpha * (ell**2 - h1**2 / 4)))
    h = 2 * ell * math.sqrt(
        alpha * (mass_slider + mass_ball) * gravity
        / (k * mass_ball + alpha * (mass_slider + mass_ball) * gravity)
    )
    omega = math.sqrt(
        2 * (mass_slider + mass_ball) * gravity / (mass_ball * h)
    )
    close(omega_trial, 0.27318034549204245)
    close(h, 7.074105107039137)
    close(omega, 2.0735537410949174)

    # 第 4 题：离焦眼模型
    close(2 * 25 / 2.4, 20.833333333333332)
    image_distance = 25 / 26 * 2.4
    focal_length = 15 * image_distance / (15 + image_distance)
    close(focal_length, 2.0)
    close(1.0 * 2 / 8, 0.25)

    # 第 5 题：六节点循环网络。
    # m=3 时 cos(2π)=1，故本征值为零；手写稿的 1/2 是代算错误。
    lambdas: list[float | None] = []
    for mode in range(6):
        phi = mode * math.pi / 3
        denominator = 2 - 2 * math.cos(phi)
        if abs(denominator) < 1e-12:
            lambdas.append(None)
        else:
            lambdas.append((2 - 2 * math.cos(2 * phi)) / denominator)
    close(lambdas[1] or 0, 3.0)
    close(lambdas[2] or 0, 1.0)
    close(lambdas[3] or 0, 0.0)
    close(lambdas[4] or 0, 1.0)
    close(lambdas[5] or 0, 3.0)

    # 第 6 题：用 SymPy 重新解两条杆长的一、二阶约束。
    l, w, v0, a0 = sp.symbols("l w v0 a0", positive=True, real=True)
    root3 = sp.sqrt(3)
    e2 = sp.Matrix([sp.Rational(1, 2), root3 / 2])
    e3 = sp.Matrix([sp.Rational(1, 2), -root3 / 2])
    n2 = sp.Matrix([-root3 / 2, sp.Rational(1, 2)])
    n3 = sp.Matrix([root3 / 2, sp.Rational(1, 2)])
    vx, vy = sp.symbols("vx vy")
    velocity_a = sp.Matrix([-w * l, 0])
    velocity_b = sp.Matrix([vx, vy])
    velocity_c = sp.Matrix([0, v0])
    solved_velocity = sp.solve(
        [
            (velocity_b - velocity_a).dot(e2),
            (velocity_c - velocity_b).dot(e3),
        ],
        [vx, vy],
        dict=True,
    )[0]
    assert sp.simplify(solved_velocity[vx] + w * l / 2 + root3 * v0 / 2) == 0
    assert sp.simplify(solved_velocity[vy] - v0 / 2 + w * l / (2 * root3)) == 0
    velocity_b = velocity_b.subs(solved_velocity)
    omega_2 = sp.simplify((velocity_b - velocity_a).dot(n2) / (3 * l))
    omega_3 = sp.simplify((velocity_c - velocity_b).dot(n3) / (3 * l))
    assert sp.simplify(omega_3 - (v0 / (3 * l) + w / (3 * root3))) == 0
    ax, ay = sp.symbols("ax ay")
    acceleration_a = sp.Matrix([0, -w**2 * l])
    acceleration_b = sp.Matrix([ax, ay])
    acceleration_c = sp.Matrix([0, a0])
    solved_acceleration = sp.solve(
        [
            (acceleration_b - acceleration_a).dot(e2) + 3 * l * omega_2**2,
            (acceleration_c - acceleration_b).dot(e3) + 3 * l * omega_3**2,
        ],
        [ax, ay],
        dict=True,
    )[0]
    alpha_3 = sp.simplify(
        (acceleration_c - acceleration_b.subs(solved_acceleration)).dot(n3) / (3 * l)
    )
    expected_alpha_3 = (
        27 * a0 * l
        + (27 + root3) * w**2 * l**2
        - 18 * l * v0 * w
        + 3 * root3 * v0**2
    ) / (81 * l**2)
    assert sp.simplify(alpha_3 - expected_alpha_3) == 0

    # 第 7 题：数值结果与分离角三次方程
    radius, n, theta = 0.105, 1.19, 0.831
    speed_b1 = 2 * radius * math.sqrt(
        (2 * 10 / radius)
        * (math.sqrt(3) - 2 * math.sin(theta))
        / (4 + 16 * n * math.sin(theta) ** 2)
    )
    close(speed_b1, 0.3857328890831943)
    s = sp.symbols("s", real=True)
    roots = [
        complex(root)
        for root in sp.nroots(32 * s**3 + sp.Rational(149, 5) * s - 5 * sp.sqrt(3))
    ]
    physical_root = [root.real for root in roots if abs(root.imag) < 1e-10 and 0 < root.real < 1][0]
    close(physical_root, 0.269575888572386)
    landing_speed = math.sqrt(6 * 10 * radius * physical_root)
    close(landing_speed, 1.3031991648160504, tol=1e-4)

    # 第 8 题：洛伦兹变换保持发射—接收事件的间隔。
    beta = sp.symbols("beta", real=True)
    gamma = 1 / sp.sqrt(1 - beta**2)
    ct = gamma * (sp.sqrt(5) + beta)
    x = gamma * (1 + sp.sqrt(5) * beta)
    assert sp.simplify(ct**2 - x**2 - 4) == 0

    print("蔡题081：关键数值、符号推导与相对论不变量核验通过。")


if __name__ == "__main__":
    main()
