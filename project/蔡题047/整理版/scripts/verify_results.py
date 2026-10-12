from __future__ import annotations

import math


def bisect(function, left: float, right: float, iterations: int = 120) -> float:
    f_left = function(left)
    for _ in range(iterations):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right = middle
        else:
            left = middle
            f_left = f_middle
    return (left + right) / 2


def close(actual: float, expected: float, tolerance: float) -> None:
    if abs(actual - expected) > tolerance:
        raise AssertionError(f"{actual=} 与 {expected=} 不符")


def main() -> None:
    # 第1题：约束方程与高度。
    f1 = lambda x: 1 / math.sqrt(1 + 9 * x * x) + 1 / math.sqrt(1 + x * x) - 1.6
    x = bisect(f1, 0.0, 2.0)
    h1 = 0.5 * (
        3 * x / math.sqrt(1 + 9 * x * x)
        + x / math.sqrt(1 + x * x)
    )
    close(x, 0.3755342531, 5e-10)
    close(h1, 0.5497203176, 5e-10)

    # 第2题：首次撞击的较小正根、位置和速度。
    v0, g, h = 40.0, 10.0, 15.0
    theta, alpha = math.radians(35), math.radians(30)
    coefficient = v0 * (math.sin(theta) + math.cos(theta) * math.tan(alpha))
    t = (coefficient - math.sqrt(coefficient**2 - 2 * g * h)) / g
    x2 = v0 * math.cos(theta) * t
    y2 = h - x2 * math.tan(alpha)
    vy2 = v0 * math.sin(theta) - g * t
    close(t, 0.3751420540, 5e-10)
    close(x2, 12.2919352160, 5e-9)
    close(y2, 7.9032478942, 5e-9)
    close(vy2, 19.1916369144, 5e-9)

    # 第5题：汽化量和刚性容器的内能增量。
    gas_constant, temperature, latent, heat_capacity = 8.31, 373.0, 40_800.0, 75.8
    delta_n = (latent / (gas_constant * temperature) - 1) / temperature
    heat = heat_capacity + 3 * gas_constant + delta_n * (latent - gas_constant * temperature)
    close(delta_n, 0.0326, 7e-5)
    close(heat / 1000, 1.33, 0.006)

    # 第6题：自洽函数在原点的线性系数为 2qJ/(3kT)。
    # 令无量纲 y 很小，用中心差分核对 G'(0)=2/3。
    eps = 1e-6
    gfun = lambda y: 2 * math.sinh(y) / (1 + 2 * math.cosh(y))
    slope = (gfun(eps) - gfun(-eps)) / (2 * eps)
    close(slope, 2 / 3, 1e-10)

    # 第7题：支持力临界值和摩擦比极值。
    support_peak = 1 + 2 * (1 / 3) - 3 * (1 / 3) ** 2
    close(support_peak, 4 / 3, 1e-12)
    c_star = (7 - math.sqrt(34)) / 15
    ratio = math.sqrt(1 - c_star**2) * abs(3 * c_star - 2) / (1 - 2 * c_star + 3 * c_star**2)
    close(ratio, 2.041885, 2e-6)

    # 第8题：临界根、物理解和两个速度分支。
    parameter = lambda c: (3 - c) ** 2 / ((2 - c) * c)
    close(parameter(1.0), 4.0, 1e-12)
    lam = 10.0
    c_allowed = (lam + 3 - math.sqrt(lam**2 - 3 * lam)) / (lam + 1)
    close(parameter(c_allowed), lam, 1e-10)
    c = math.cos(1.0)
    w_abs = math.sqrt((10 * c - c * c / 6) / (0.5 - c * c / 6))
    u_minus = c * (-w_abs + 1) / 3
    u_plus = c * (w_abs + 1) / 3
    close(w_abs, 3.4442886598, 5e-10)
    close(abs(u_minus), 0.4402182664, 5e-10)
    close(abs(u_plus), 0.8004198036, 5e-10)

    print("第047套数值与符号核验通过")
    print(f"Q1: x={x:.10f}, h={h1:.10f} m")
    print(f"Q2: t={t:.10f} s, (x,y)=({x2:.10f},{y2:.10f}) m")
    print(f"Q5: delta_n={delta_n:.10f} mol, Q={heat/1000:.10f} kJ")
    print(f"Q7: lambda_c={support_peak:.10f}, mu_2={ratio:.10f}")
    print(f"Q8: |beta_dot|={w_abs:.10f}, |x_dot|=({abs(u_minus):.10f},{abs(u_plus):.10f})")


if __name__ == "__main__":
    main()
