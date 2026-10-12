from __future__ import annotations

import cmath
import math


def close(a: float, b: float, tol: float = 1.0e-10) -> None:
    scale = max(1.0, abs(a), abs(b))
    assert abs(a - b) <= tol * scale, (a, b)


def verify_q1() -> None:
    roots = [(12.0 - math.sqrt(134.0)) / 5.0,
             (12.0 + math.sqrt(134.0)) / 5.0]
    for x in roots:
        close(5.0 * x * x - 24.0 * x + 2.0, 0.0)
        assert x > 0.0
    close(math.sqrt(roots[0]), 0.2912603980, 1.0e-8)
    close(math.sqrt(roots[1]), 2.1714436167, 1.0e-8)


def verify_q2() -> None:
    n = 7
    z = cmath.exp(2j * math.pi / n)
    weighted = sum(j * z**j for j in range(1, n + 1))
    target = -n * z / (1.0 - z)
    close(abs(weighted - target), 0.0)
    close(abs(weighted), n / (2.0 * math.sin(math.pi / n)))

    # 数值积分交叉检查连续电荷的两个分量。
    count = 200_000
    dtheta = 2.0 * math.pi / count
    ix = 0.0
    iy = 0.0
    for j in range(count):
        theta = (j + 0.5) * dtheta
        ix += theta * math.cos(theta) * dtheta
        iy += theta * math.sin(theta) * dtheta
    close(ix, 0.0, 2.0e-9)
    close(iy, -2.0 * math.pi, 2.0e-9)


def verify_q3() -> None:
    mu1 = (7.0 - math.sqrt(37.0)) / 6.0
    mu2 = (7.0 + math.sqrt(37.0)) / 6.0
    close(mu1 + mu2, 7.0 / 3.0)
    close(mu1 * mu2, 1.0 / 3.0)
    assert 0.0 < mu1 < mu2

    cos2 = 0.5 * (1.0 + 1.0 / math.sqrt(37.0))
    sin2 = 1.0 - cos2
    # theta(t) 在 t=0 必须给出 theta_dot(0)=V/l。
    close(cos2 + sin2, 1.0)
    w1 = math.sqrt(1.0 / mu1)
    w2 = math.sqrt(1.0 / mu2)
    assert w1 > w2 > 0.0


def verify_q4() -> None:
    x = (5.0 / 8.0) ** (3.0 / 5.0)
    n1 = 2.0 * x
    t1 = 2.0 * x ** (2.0 / 3.0)
    n2 = 3.0 - n1
    t2 = n1 * t1 / n2
    close(n1 * t1 + n2 * t2, 5.0)
    close(n1 * t1, n2 * t2)
    close(t1, 2.0 * (5.0 / 8.0) ** (2.0 / 5.0))
    close(n1, 1.5085440841, 1.0e-8)
    close(n2, 1.4914559159, 1.0e-8)
    close(t2, 1.6762144784, 1.0e-8)


def verify_q5() -> None:
    mutual = 0.5
    i2 = -mutual
    source = 1.0 + mutual * i2
    meter = mutual * (1.0 + i2)
    close(source, 0.75)
    close(meter, 0.25)
    close(meter / source, 1.0 / 3.0)


def verify_q6() -> None:
    mu = 273.0
    beta2 = (mu * mu - 2.0) / (2.0 * (mu * mu - 1.0))
    assert 0.0 < beta2 < 1.0
    close(math.sqrt(beta2), 0.7071020373, 1.0e-8)

    # 在固定乘积 E_e E_nu 下，和在两者相等时最小。
    product = (mu * mu - 1.0) / 2.0
    equal_sum = 2.0 * math.sqrt(product)
    for ratio in (0.2, 0.5, 1.0, 2.0, 5.0):
        ee = math.sqrt(product * ratio)
        enu = math.sqrt(product / ratio)
        assert ee + enu >= equal_sum - 1.0e-12


def verify_q7() -> None:
    # 取 k=m=B=a=1，对无量纲方程和转折点能量式做相互检验。
    lo, hi = 1.0, 10.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        value = (mid + 1.0) ** 2 * (mid - 1.0) - 24.0 * mid
        if value < 0.0:
            lo = mid
        else:
            hi = mid
    s = 0.5 * (lo + hi)
    initial_energy = 3.0
    final_energy = 3.0 / s + 0.125 * (s * s - 1.0) ** 2 / (s * s)
    close(initial_energy, final_energy)
    assert 1.0 < s < 10.0


def verify_q8() -> None:
    wavelength = 6.3e-7
    alpha = math.radians(5.7)
    deviation = 0.8 * alpha
    spacing = wavelength / (2.0 * math.sin(deviation))
    speed = 1.0e4 * spacing
    close(spacing, 3.962113545e-6, 1.0e-8)
    close(speed, 3.962113545e-2, 1.0e-8)

    gamma, omega, drive = 1.7, 2.3, 0.8
    xi, vi = -0.4, 0.6
    c = vi - drive * gamma / (gamma * gamma + omega * omega)

    def velocity(t: float) -> float:
        return (c * math.exp(-gamma * t)
                + drive * (gamma * math.cos(omega * t)
                           + omega * math.sin(omega * t))
                / (gamma * gamma + omega * omega))

    def position(t: float) -> float:
        return (xi + c / gamma * (1.0 - math.exp(-gamma * t))
                + drive / (gamma * gamma + omega * omega)
                + drive * (gamma * math.sin(omega * t)
                           - omega * math.cos(omega * t))
                / (omega * (gamma * gamma + omega * omega)))

    close(position(0.0), xi)
    close(velocity(0.0), vi)
    dt = 1.0e-6
    close((position(dt) - position(-dt)) / (2.0 * dt), vi, 1.0e-7)


def main() -> None:
    checks = [verify_q1, verify_q2, verify_q3, verify_q4,
              verify_q5, verify_q6, verify_q7, verify_q8]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")


if __name__ == "__main__":
    main()
