from __future__ import annotations

import math


def close(name: str, actual: float, expected: float, tol: float = 1e-9) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{name}: {actual} != {expected}")
    print(f"[PASS] {name}: {actual:.12g}")


def main() -> None:
    # 第 1 题：后轴摩擦圆与前轴单独极限。
    mu, g, acc, radius = 0.5, 9.8, 2.0, 500.0
    t_rear = math.sqrt(radius * math.sqrt(mu**2 * g**2 - 4 * acc**2)) / acc
    t_front = math.sqrt(mu * g * radius) / acc
    close("第 1 题后轴临界时间", t_rear, 18.808888655423605)
    assert t_rear < t_front
    print(f"[PASS] 第 1 题由后轴先限制：{t_rear:.4f} < {t_front:.4f}")

    # 第 2 题：四问分段相位数值。
    h, rho, theta, alpha = 1.0, 10.0, 0.01, math.pi / 4
    w1 = math.sqrt(g / rho)
    ts = math.sqrt(2 * h / (g * math.cos(alpha) ** 2))
    u1 = math.sqrt(2 * g * h)
    tc = math.atan(rho * theta * w1 / u1) / w1
    close("第 2 题固定山体周期", 4 * (ts + tc), 2.645841996341163)

    m = M = 1.0
    mes = m * (M + m * math.cos(alpha) ** 2) / (M + m)
    mec = m * M / (M + m)
    ts = math.sqrt(2 * h * mes / (m * g * math.cos(alpha) ** 2))
    u1 = math.sqrt(2 * m * g * h / mes)
    wc = math.sqrt(m * g / (rho * mec))
    tc = math.atan(rho * theta * wc / u1) / wc
    close("第 2 题可动山体质点周期", 4 * (ts + tc), 2.2913598676116074)

    mes += 2 * m / 5
    mec += 2 * m / 5
    ts = math.sqrt(2 * h * mes / (m * g * math.cos(alpha) ** 2))
    u1 = math.sqrt(2 * m * g * h / mes)
    wc = math.sqrt(m * g / (rho * mec))
    tc = math.atan(rho * theta * wc / u1) / wc
    close("第 2 题可动山体滚动周期", 4 * (ts + tc), 2.8373449583424777)

    # 第 3 题：AC 松弛支的 T 必须同时满足 B、D 端加速度约束。
    length, l1, l2, aa, bb = 3.0, 0.8, 1.1, 0.7, 0.9
    A0 = aa**2 + l1**2
    force_per_m = g * bb**2 * (A0 - length * l1) / (
        bb**2 * (A0 + length**2) + (length - l2) ** 2 * A0
    )
    alpha1 = (g * l1 + force_per_m * length) / A0
    a_b = length * alpha1
    alpha2 = -force_per_m * (length - l2) / bb**2
    a_d = g - force_per_m + (length - l2) * alpha2
    close("第 3 题松绳支端点加速度约束", a_d, a_b)

    # 第 4 题：正根位于实像区间并满足二次式。
    u3 = (1 + math.sqrt(13)) / 3
    assert 4 / 3 < u3 < 2
    close("第 4 题物像等距方程", 3 * u3**2 - 2 * u3 - 4, 0.0)
    print(f"[PASS] 第 4 题正根位于允许区间：{u3:.12g}")

    # 第 5 题：空间均匀极限与同步行波极限。
    r, cap, omega = 2.0, 0.3, 1.7
    q = 0.0
    numerator = 2 - 2 * math.cos(q)
    z = 4 * r - 2 * r * math.cos(q) - 1j * numerator / (omega * cap)
    close("第 5 题空间均匀极限", abs(numerator / z), 0.0)
    q = 0.8
    s = 2 - 2 * math.cos(q)
    for om in (1e-3, 1e-4, 1e-5):
        z = 4 * r - 2 * r * math.cos(q) - 1j * s / (om * cap)
        response = om * s / z
        assert abs(response) < 2 * om**2 * cap
    print("[PASS] 第 5 题同步行波极限：I_AC -> 0")

    # 第 6 题：赤道场、回旋尺度和慢振频率。
    mu0, moment, earth_r = 4 * math.pi * 1e-7, 8.1e22, 3e7
    b0 = mu0 * moment / (4 * math.pi * earth_r**3)
    close("第 6 题赤道磁场", b0, 3e-7)
    charge, me, c = 1.602176634e-19, 9.1093837e-31, 299792458.0
    energy = 10e6 * charge
    rest = 0.511e6 * charge
    gamma = energy / rest
    p = math.sqrt(energy**2 - rest**2) / c
    gyro = charge * b0 / (gamma * me)
    gyroradius = p / (charge * b0)
    bounce = 3 / math.sqrt(2) * gyroradius * gyro / earth_r
    close("第 6 题回旋半径", gyroradius, 111042.76919281296, 1e-8)
    close("第 6 题回旋角频率", gyro, 2696.2710769577093, 1e-8)
    close("第 6 题慢振角频率", bounce, 21.170876510155022, 1e-8)

    # 第 7 题：有限递推、指数极限和快速度反解。
    U1 = 2 / 5
    U2 = 3 / 5 * U1 + 2 / 5
    close("第 7 题 N=4 末速比", U2, 16 / 25)
    n_large = 1_000_000
    classical = 1 - ((n_large - 1) / (n_large + 1)) ** (n_large / 2)
    close("第 7 题经典连续极限", classical, 1 - math.exp(-1), 1e-6)
    ratio = 0.4
    rapidity_exp = 1 + ratio
    beta = (rapidity_exp**2 - 1) / (rapidity_exp**2 + 1)
    close("第 7 题快速度反解", math.tanh(math.log(rapidity_exp)), beta)

    # 第 8 题：三角映射及周期性。
    def triangular(lam: float) -> float:
        x = lam % 4.0
        if x <= 1:
            return x
        if x <= 3:
            return 2 - x
        return x - 4

    samples = {0.8: 0.8, 2.0: 0.0, 3.5: -0.5, 4.5: 0.5, 6.0: 0.0}
    for lam, expected in samples.items():
        close(f"第 8 题 F({lam})", triangular(lam), expected)
        close(f"第 8 题周期 F({lam}+4)", triangular(lam + 4), triangular(lam))
    print("[PASS] 第 8 题分段反射映射与周期性")


if __name__ == "__main__":
    main()
