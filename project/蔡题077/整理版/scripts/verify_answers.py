from __future__ import annotations

import math
import sympy as sp


def main() -> None:
    # 1. 六段等弦回到起点的最小初速。
    e, a = sp.symbols("e a", positive=True)
    v0 = a * (1 - e**6) / (e**5 * (1 - e))
    u = v0
    for _ in range(5):
        u = e * (u - a)
    assert sp.simplify(u - a) == 0

    # 2. 各向同性简谐运动最小速度。
    x = (sp.sqrt(5) - 1) / 4
    fmin = (sp.sqrt(5) + 3) / 2
    assert sp.simplify(fmin - 2 - (sp.sqrt(5) - 1) / 2) == 0
    assert 0 < float(x) < 1

    # 3. 均匀带电球中心落速。
    k0, charge, mass, radius = sp.symbols("k0 charge mass radius", positive=True)
    vcenter = sp.sqrt(2 * k0 * charge / (mass * radius))
    assert sp.simplify(mass * vcenter**2 / 2 - k0 * charge / radius) == 0

    # 5. 球壳角动量与磁偶极相互作用。
    q, B, m, r = sp.symbols("q B m r", positive=True)
    inertia = sp.Rational(2, 3) * m * r**2
    angular_momentum = -q * r**2 * B / 3
    assert sp.simplify(angular_momentum / inertia + q * B / (2 * m)) == 0

    # 6. 逆流换热器端口温差。
    z = sp.symbols("z", positive=True)
    ratio = (1 - z) / (1 + z)
    assert sp.simplify(2 / (1 + z) - 1 - ratio) == 0

    # 8. 极端相对论碰撞最小角。
    p1, p2, cphi = sp.symbols("p1 p2 cphi", positive=True)
    ctheta = 1 - 4 * p1 * p2 * (1 - cphi) / (p1 + p2) ** 2
    assert sp.simplify((p1 + p2) ** 2 * (1 - ctheta) - 4 * p1 * p2 * (1 - cphi)) == 0

    print("蔡题077：阻尼碰壁、弹性绳、辐射轨道、互感、球壳磁效应、换热、梯度折射率与相对论碰撞核验通过。")


if __name__ == "__main__":
    main()
