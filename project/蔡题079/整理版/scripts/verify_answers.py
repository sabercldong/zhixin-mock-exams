from __future__ import annotations

import math
import sympy as sp


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a=} != {b=}")


def main() -> None:
    # 1. 两种曲梁柔度积分
    phi = sp.symbols("phi", real=True)
    ia = sp.integrate(sp.sin(phi) ** 2, (phi, 0, sp.pi / 2))
    ib = sp.integrate((1 - sp.cos(phi)) ** 2, (phi, 0, sp.pi / 2))
    assert sp.simplify(ia - sp.pi / 4) == 0
    assert sp.simplify(ib - (3 * sp.pi / 4 - 2)) == 0
    assert float(ia - ib) > 0

    # 2. 两种电磁角冲量相等
    Q, B, R, d = sp.symbols("Q B R d", positive=True)
    exact = Q * B * (R**2 - (R - d) ** 2) / 2
    assert sp.series(exact, d, 0, 2).removeO() == Q * B * R * d

    # 3. 碰撞统一解同时满足三条方程
    m, v0, w0 = sp.symbols("m v0 w0", positive=True)
    vf = sp.Rational(3, 5) * v0 + sp.Rational(2, 5) * R * w0
    wf = vf / R
    J = m * (vf - v0)
    I = sp.Rational(2, 3) * m * R**2
    assert sp.simplify(I * (wf - w0) + J * R) == 0

    # 4. 半圆薄板虚功系数
    rho, Y, a = sp.symbols("rho Y a", positive=True)
    L = sp.pi * R
    U = Y * a * d**3 * L / (24 * rho**2)
    chord = 2 * rho * sp.sin(L / (2 * rho))
    force = -sp.diff(U, rho) / sp.diff(chord, rho)
    assert sp.simplify(force.subs(rho, R) - sp.pi * Y * a * d**3 / (24 * R**2)) == 0

    # 5. 交流电场位移满足初始条件和运动方程
    t, omega, A0 = sp.symbols("t omega A0", positive=True)
    x = A0 / omega * (t - sp.sin(omega * t) / omega)
    assert x.subs(t, 0) == 0
    assert sp.diff(x, t).subs(t, 0) == 0
    assert sp.simplify(sp.diff(x, t, 2) - A0 * sp.sin(omega * t)) == 0

    # 6. 三角形边参数的不动点、两端换算与功率递推
    e0, R0, k0, ell = sp.symbols("e0 R0 k0 ell", positive=True)
    xnet = sp.solve(sp.Eq(sp.Rational(1, 3) + sp.Rational(5, 9) * sp.Symbol("xnet"), sp.Symbol("xnet")))[0]
    assert xnet == sp.Rational(3, 4)
    assert sp.Rational(2, 3) * xnet == sp.Rational(1, 2)
    It = 7 * e0 / (54 * R0)
    beta = sp.symbols("beta")
    child_power = R0 * It**2 / 6 + beta * e0**2 / (27 * R0)
    power_recursion = sp.Eq(beta * e0**2 / R0, 3 * child_power + R0 * It**2)
    assert sp.solve(power_recursion, beta)[0] == sp.Rational(49, 1728)
    p = 49 * e0**2 / (1728 * R0)
    substituted = sp.simplify(p.subs(e0, k0 * sp.sqrt(3) * ell**2 / 4))
    assert substituted == 49 * k0**2 * ell**4 / (9216 * R0)

    # 7. 加权几何平均满足总熵不变
    Ca, Cb, Ta, Tb = sp.symbols("Ca Cb Ta Tb", positive=True)
    Tf = Ta ** (Ca / (Ca + Cb)) * Tb ** (Cb / (Ca + Cb))
    assert sp.simplify(Ca * sp.log(Tf / Ta) + Cb * sp.log(Tf / Tb), force=True) == 0

    # 8. 偶极受迫振动：约化质量 m/2，驱动频率 2 omega
    alpha, E0, eps0, k = sp.symbols("alpha E0 eps0 k", positive=True)
    F0 = 3 * alpha**2 * E0**2 / (4 * sp.pi * eps0 * R**4)
    mean = -F0 / k
    amp = -F0 / (k - 2 * m * omega**2)
    delta = mean + amp * sp.cos(2 * omega * t)
    residual = sp.simplify(m * sp.diff(delta, t, 2) / 2 + k * delta + F0 * (1 + sp.cos(2 * omega * t)))
    assert residual == 0

    print("蔡题079：曲梁、电磁角冲量、碰撞、弯曲能、开放系统与偶极振动核验通过。")


if __name__ == "__main__":
    main()
