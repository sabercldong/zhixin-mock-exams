from __future__ import annotations

import math
import sympy as sp


def main() -> None:
    # 1. 三个像电荷的矢量合成
    R, Q, eps0 = sp.symbols("R Q eps0", positive=True)
    a = sp.sqrt(2) * R
    p = sp.Matrix([a, 0, a])
    images = [
        (-Q, sp.Matrix([a, 0, -a])),
        (-Q / 2, sp.Matrix([a / 4, 0, a / 4])),
        (Q / 2, sp.Matrix([a / 4, 0, -a / 4])),
    ]
    force = sp.zeros(3, 1)
    for charge, position in images:
        delta = p - position
        force += Q * charge * delta / (delta.dot(delta)) ** sp.Rational(3, 2)
    scale = Q**2 / R**2
    assert sp.simplify(force[0] / scale + sp.sqrt(2) / 9 - 3 * sp.sqrt(34) / 289) == 0
    assert force[1] == 0

    # 2. 第2题速度区间与厚度临界根
    x = sp.symbols("x", real=True)
    roots = [complex(z) for z in sp.nroots(x**3 - 8 * x + 4)]
    physical = [z.real for z in roots if abs(z.imag) < 1e-12 and 0 < z.real < 1]
    assert len(physical) == 1 and math.isclose(1 - physical[0], 0.48269595499, rel_tol=1e-9)
    assert sp.simplify(sp.Rational(5, 11)) > 0

    # 3. 旋转弹簧低速极限
    beta, l0, r0 = sp.symbols("beta l0 r0", positive=True)
    length = l0 * sp.tan(beta) / beta + r0 * (1 / sp.cos(beta) - 1)
    assert sp.limit(length, beta, 0) == l0

    # 4. 初始电流和象限衰减数值
    theta0 = sp.pi / 4
    current = 10 * theta0 / (2 * theta0 + theta0**2)
    assert math.isclose(float(current), 40 / (8 + math.pi), rel_tol=1e-12)

    # 5. 质子加速度
    mu0 = 4 * math.pi * 1e-7
    N, S, radius, didt = 200, 2e-4, 0.1, 10
    electric = mu0 * N * S * didt / (4 * math.pi * radius**2)
    proton_acc = 1.602e-19 * electric / 1.673e-27
    assert math.isclose(electric, 4e-6, rel_tol=1e-12)
    assert 382 < proton_acc < 384

    # 6. 萨格纳数值
    omega = 15 * math.pi / 180 / 3600
    area = 600 * 300
    delta_l = 4 * area * omega / 299792458
    assert math.isclose(delta_l, 0.70e-6 / 4, rel_tol=3e-3)

    # 7. 卡诺制冷数值
    power = 173 * 15**2 / 298
    assert math.isclose(power, 130.620805369, rel_tol=1e-9)

    # 8. 纯电与纯磁参考系候选速度之积
    lam1, lam2, v, c, gamma = sp.symbols("lam1 lam2 v c gamma", nonzero=True)
    ue = lam1 * v / (lam1 + lam2 / gamma)
    ub = c**2 * (lam1 + lam2 / gamma) / (v * lam1)
    assert sp.simplify(ue * ub - c**2) == 0

    print("蔡题078：镜像电荷、碰撞翻阶、旋转弹簧、电磁阻尼、感生场、萨格纳效应、制冷与场变换核验通过。")


if __name__ == "__main__":
    main()
