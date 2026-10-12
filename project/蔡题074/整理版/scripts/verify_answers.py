from __future__ import annotations

import math

import mpmath as mp
import sympy as sp


def main() -> None:
    mp.mp.dps = 50
    # 第1题：刚度标定与失稳力的量纲一致形式。
    weight, length, drop = sp.symbols("weight length drop", positive=True)
    bending_constant = weight * length**3 / (8 * drop)
    critical_force = sp.simplify(24 * bending_constant / length**2)
    assert sp.simplify(critical_force - 3 * weight * length / drop) == 0
    assert critical_force.subs({weight: 10, length: 1, drop: sp.Rational(1, 100)}) == 3000

    # 第2题：第二次斜碰与最高点。
    a = sp.sqrt(2 * (2 - sp.sqrt(2)))
    v2y = sp.Rational(3, 8) - a / 4
    height_ratio = 1 + sp.sqrt(2) + v2y**2 / 2
    assert abs(float(height_ratio) - 2.4196634459473647) < 1e-12
    lambda_max = 1 / (1 - sp.sqrt(2 - sp.sqrt(2)))
    assert abs(float(lambda_max) - 4.261972627395667) < 1e-12

    # 第3题：远拱点根与角积分。
    f = lambda beta: 1 - beta**2 + mp.mpf("0.5") * mp.log(beta)
    beta = mp.findroot(f, (mp.mpf("0.1"), mp.mpf("0.2")))
    theta = mp.quad(lambda value: 1 / mp.sqrt(f(value)), [beta, (1 + beta) / 2, 1])
    assert abs(float(beta) - 0.1408098053467102) < 1e-12
    assert abs(float(theta) - 2.0781403192652393) < 1e-10

    # 第4题：固定电荷能量求液体拉力。
    q, eps0, rho, gravity, side, gap, epsr = sp.symbols(
        "q eps0 rho gravity side gap epsr", positive=True
    )
    x = sp.symbols("x", positive=True)
    capacitance = eps0 * side / gap * (side + (epsr - 1) * x)
    energy = q**2 / (2 * capacitance)
    electric_force = sp.simplify(-sp.diff(energy, x).subs(x, side / 2))
    expected_force = 2 * q**2 * gap * (epsr - 1) / (eps0 * side**3 * (epsr + 1) ** 2)
    assert sp.simplify(electric_force - expected_force) == 0

    # 第5题：自由圆盘与固定轴两种冲击参数。
    mass, disk_mass, radius = sp.symbols("mass disk_mass radius", positive=True)
    b_free = (mass + disk_mass / 2) * radius / (mass + disk_mass)
    b_pin = (mass + disk_mass / 2) * radius / (disk_mass - mass)
    assert sp.limit(b_free / radius, mass, 0) == sp.Rational(1, 2)
    assert sp.limit(b_pin / radius, mass, 0) == sp.Rational(1, 2)

    # 第6题：四条边界与最小安全半径。
    def boundary(rho_lens: float, eta_ccd: float, radial: float) -> float:
        return 15 * (rho_lens - radial) / (eta_ccd + rho_lens / 2)

    assert boundary(5, 2, 4) == 10 / 3
    assert boundary(5, -2, 4) == 30
    minimum_safe_radius = min(
        5 - z / 30 if z <= 30 else 3 * z / 10 - 5
        for z in [value / 10 for value in range(1, 1001)]
    )
    assert abs(minimum_safe_radius - 4) < 1e-12

    # 第7题：离散长波速度化简。
    gamma, amount, gas_constant, temperature, piston_mass = sp.symbols(
        "gamma amount gas_constant temperature piston_mass", positive=True
    )
    wave_speed = sp.sqrt(gamma * amount * gas_constant * temperature / piston_mass)
    nitrogen_speed = wave_speed.subs(gamma, sp.Rational(7, 5))
    assert sp.simplify(nitrogen_speed**2 - 7 * amount * gas_constant * temperature / (5 * piston_mass)) == 0

    # 第8题：非相对论磁场数值与相对论因子抵消。
    magnetic_field = 2 * math.pi * 1.88e-28 / (1.602e-19 * 1.523e-6)
    assert abs(magnetic_field - 4.841448344484702e-3) < 1e-15
    lorentz_factor = sp.symbols("lorentz_factor", positive=True)
    assert sp.simplify((lorentz_factor * sp.Symbol("T0")) / (lorentz_factor * sp.Symbol("tau0"))) == sp.Symbol("T0") / sp.Symbol("tau0")

    print("蔡题074：八题的失稳力、双碰撞、轨道积分、介质拉力、偏心碰撞、光路边界、离散波速与相对论周期核验通过。")


if __name__ == "__main__":
    main()
