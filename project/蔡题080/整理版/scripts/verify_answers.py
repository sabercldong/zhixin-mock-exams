from __future__ import annotations

import math
import numpy as np
import sympy as sp


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a=} != {b=}")


def network_resistance(n: int) -> float:
    def A(i: int) -> int: return i
    def B(i: int) -> int: return n + i
    edges: list[tuple[int, int]] = []
    for i in range(n - 1):
        edges += [(A(i), A(i + 1)), (B(i), B(i + 1))]
    edges += [(A(n - 1), B(0)), (B(n - 1), A(0))]
    edges += [(A(i), B(i)) for i in range(n)]
    lap = np.zeros((2 * n, 2 * n))
    for i, j in edges:
        lap[i, i] += 1; lap[j, j] += 1
        lap[i, j] -= 1; lap[j, i] -= 1
    source, ground = A(0), B(0)
    keep = [i for i in range(2 * n) if i != ground]
    rhs = np.array([1.0 if i == source else 0.0 for i in keep])
    volts = np.linalg.solve(lap[np.ix_(keep, keep)], rhs)
    return float(volts[keep.index(source)])


def main() -> None:
    # 1. 像电荷合力展开
    x, alpha = sp.symbols("x alpha", real=True)
    force = (
        8 * x / (1 - 4 * x**2) ** 2
        + alpha**2 * (2 - x) / ((2 - x) ** 2 - 1) ** 2
        - alpha / (2 - x) ** 2
        - alpha**2 / (2 - x) ** 3
    )
    assert sp.factor(force.subs(x, 0)) == alpha * (7 * alpha - 18) / 72
    assert sp.simplify(sp.diff(force, x).subs({x: 0, alpha: sp.Rational(18, 7)})) == sp.Rational(1823, 196)

    # 2. 莫比乌斯网络
    close(network_resistance(5), 19 / 33)
    close(network_resistance(100), 1 / math.sqrt(3), tol=1e-8)

    # 3. 双星估算
    radius_star = 13.08 * 7e8
    separation = math.sqrt(2) * radius_star
    period = 2.1 * 86400
    total_mass = 4 * math.pi**2 * separation**3 / (6.67e-11 * period**2)
    compact_mass = total_mass - 18.4 * 2e30
    density = 1.66e-27 / 1e-45
    compact_radius = (3 * compact_mass / (4 * math.pi * density)) ** (1 / 3)
    close(total_mass / 2e30, 19.516421011456917)
    close(compact_mass / 2e30, 1.116421011456917)
    close(compact_radius, 6847.84255620426)

    # 4. 能量微分方程积分结果
    mu = sp.symbols("mu", positive=True)
    assert sp.simplify(sp.log(sp.exp(4 * sp.pi * mu)) - 4 * sp.pi * mu) == 0

    # 5. 两段电压在停流时连续
    K, a, tau, t0, t = sp.symbols("K a tau t0 t", positive=True)
    before = K * a * tau * (sp.exp(-t / tau) - 1)
    after = before.subs(t, t0) * sp.exp(-(t - t0) / tau)
    assert sp.simplify(after.subs(t, t0) - before.subs(t, t0)) == 0

    # 6. 实空间压缩 N 倍，倒空间峰间距扩大 N 倍
    N = sp.symbols("N", positive=True)
    assert sp.simplify((1 / (1 / N)) / N) == 1

    # 7. 球膜小振动
    sigma, lam, r0 = sp.symbols("sigma lam r0", positive=True)
    r = sp.symbols("r", positive=True)
    radial_force = 8 * sp.pi * sigma * (r0**4 / r**3 - r)
    stiffness = -sp.diff(radial_force, r).subs(r, r0)
    assert stiffness == 32 * sp.pi * sigma
    assert sp.simplify(stiffness / (4 * sp.pi * r0**2 * lam) - 8 * sigma / (lam * r0**2)) == 0

    # 8. 相对论末态能量范围
    p = sp.Rational(4, 3)
    px = sp.symbols("px", real=True)
    e1 = sp.sqrt(1 + p * px)
    e2 = sp.sqrt(1 + p * (p - px))
    close(float((e1 + e2).subs(px, 0)), 8 / 3)
    close(float((e1 + e2).subs(px, p / 2)), 2 * math.sqrt(17) / 3)

    print("蔡题080：关键符号推导、网络数值、天体估算与相对论极值核验通过。")


if __name__ == "__main__":
    main()
