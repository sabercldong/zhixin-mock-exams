from __future__ import annotations

import math


G = 6.67430e-11


def close(actual: float, expected: float, rel: float = 5e-4) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=0.0):
        raise AssertionError(f"{actual=} 与 {expected=} 不符")


def verify_q1() -> None:
    R = 6.40e6
    rho = 5.5e3
    period = 27.3 * 24 * 3600
    mass = 4 * math.pi * R**3 * rho / 3
    radius = (G * mass * period**2 / (4 * math.pi**2)) ** (1 / 3)
    speed = 2 * math.pi * radius / period
    cylinder_speed = R * math.sqrt(2 * math.pi * G * rho)
    close(mass, 6.040e24, 2e-3)
    close(radius, 3.841e8, 2e-3)
    close(speed, 1.023e3, 2e-3)
    close(cylinder_speed, 9.719e3, 2e-3)


def verify_q3() -> None:
    eta = 1.0
    xi = ((1 + eta**2) ** 2 / (2 * eta**2)) * math.asin(
        2 * eta / (1 + eta**2)
    ) - (1 - eta**2) / eta
    close(xi, math.pi, 1e-12)
    for mu in (0.2, 0.5, 1.0):
        chi_prime = 0.5 * (mu + 1 / mu)
        assert chi_prime >= 1.0


def verify_q4() -> None:
    g, length, height, dh = 9.8, 2.0, 1.0, 0.08
    omega1_sq = 2 * g / (3 * length + height)
    area_factor = 3 * length + 2.5 * height + 3 * dh
    omega3_sq = omega1_sq * (1 + 6 * dh / area_factor)
    assert omega3_sq > omega1_sq
    close(2 * g * dh, 1.5 * (4 * g * dh / (3 * length**2)) * length**2)


def verify_q5() -> None:
    k, v, t = 0.7, 3.0, 2.5
    x = math.sqrt(v * t / k)
    area = 4 * v * t * x / 3
    dt = 1e-6
    x2 = math.sqrt(v * (t + dt) / k)
    area2 = 4 * v * (t + dt) * x2 / 3
    numerical = (area2 - area) / dt
    analytical = 2 * v * x
    close(numerical, analytical, 2e-6)


def brightness_ratio(q: float, n: float = 2.0) -> float:
    c = math.sqrt(1 - q * q)
    ci = math.sqrt(1 - q * q / (n * n))
    d = c * ci + q * q / n

    def p_of(x: float) -> float:
        cx = math.sqrt(1 - x * x)
        cix = math.sqrt(1 - x * x / (n * n))
        return (x / n) / (cx * cix + x * x / n)

    p = p_of(q)
    eps = 1e-6
    dp = (p_of(q + eps) - p_of(q - eps)) / (2 * eps)
    area_jacobian = abs((p / q) * dp)
    beta = math.asin(q) - math.asin(q / n)
    length = c / d
    denominator = 1 - n * ci / c * (1 - ci / length)
    image_length = c / denominator
    return (
        math.cos(beta)
        * area_jacobian
        * ci
        / c
        * (image_length / length) ** 2
    )


def verify_q6() -> None:
    center = brightness_ratio(1e-4)
    close(center, 0.25, 2e-5)
    values = [brightness_ratio(q) for q in (0.05, 0.25, 0.5, 0.75, 0.95)]
    assert all(a > b for a, b in zip(values, values[1:]))


def verify_q7() -> None:
    for n, order in ((4 / 3, 1), (4 / 3, 2), (2.03, 2)):
        sine_sq = ((order + 1) ** 2 - n**2) / (order * (order + 2))
        assert 0 <= sine_sq <= 1
        alpha = math.asin(math.sqrt(sine_sq))
        theta = math.asin(math.sin(alpha) / n)
        derivative = 2 - 2 * (order + 1) * math.cos(alpha) / (
            n * math.cos(theta)
        )
        assert abs(derivative) < 1e-12
    assert 2.03 > 2  # 第 1 级虹无内部驻值


def verify_q8() -> None:
    m_h = 1.672622e-27
    m_he = 6.644657e-27
    m_e = 9.109384e-31
    c = 299792458.0
    q_value = (4 * m_h - m_he - 2 * m_e) * c**2
    gamma_u = 1 + q_value / (m_he * c**2)
    u = c * math.sqrt(1 - 1 / gamma_u**2)
    thrust = 1e-3 / (4 * m_h) * gamma_u * m_he * u
    fuel_ratio = math.exp(c / u * math.atanh(0.2)) - 1
    cruise_rapidity = u / (2 * c) * math.log(101)
    distance_ly = 15 * math.sinh(cruise_rapidity)
    close(q_value, 3.95534e-12, 2e-6)
    close(u, 3.43338e7, 2e-6)
    close(thrust, 3.43244e4, 2e-6)
    close(fuel_ratio, 4.87203, 2e-6)
    close(distance_ly, 4.01041, 2e-6)


def main() -> None:
    verify_q1()
    verify_q3()
    verify_q4()
    verify_q5()
    verify_q6()
    verify_q7()
    verify_q8()
    print("第 046 套数值、极限、驻值和标度核验通过")


if __name__ == "__main__":
    main()
