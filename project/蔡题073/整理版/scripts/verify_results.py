from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1.0e-10) -> None:
    scale = max(1.0, abs(a), abs(b))
    assert abs(a - b) <= tol * scale, (a, b)


def verify_q1() -> None:
    # 十九条像线的径向分量等大，交替符号和为 -1。
    close(sum((-1) ** j for j in range(1, 20)), -1.0)
    radius = 2.7
    for j in range(1, 20):
        phi = j * math.pi / 10.0
        separation = 2.0 * radius * math.sin(phi / 2.0)
        radial_factor = math.sin(phi / 2.0)
        close(radial_factor / separation, 1.0 / (2.0 * radius))


def verify_q2() -> None:
    # 对余弦定理作有限差分，核验 dtheta/dx=-1/l。
    length = 3.2
    step = 1.0e-6 * length

    def theta(x: float) -> float:
        cosine = (length**2 + x**2 - 2.0 * length**2) / (2.0 * length * x)
        return math.acos(cosine)

    derivative = (theta(length + step) - theta(length - step)) / (2.0 * step)
    close(derivative, -1.0 / length, 1.0e-8)

    g_load, p_load, mu = 11.0, 7.0, 0.6
    support = g_load / 2.0 + p_load / 6.0
    pressure_min = (g_load + p_load) / 2.0 - mu * support
    pressure_max = (g_load + p_load) / 2.0 + mu * support
    close(pressure_min,
          (0.5 - mu / 2.0) * g_load + (0.5 - mu / 6.0) * p_load)
    close(pressure_max,
          (0.5 + mu / 2.0) * g_load + (0.5 + mu / 6.0) * p_load)
    assert pressure_min >= 0.0


def verify_q3() -> None:
    g, length = 9.81, 2.4
    omega0_sq = 2.0 * g / (3.0 * length)
    omega1_sq = g / (2.0 * length)
    v1_sq = omega1_sq * ((5.0 * length / 4.0) ** 2 - length**2)
    v0_sq = v1_sq + omega0_sq * (3.0 * length / 4.0) ** 2
    v2_sq = 2.0 * (g / 2.0) * (length / 4.0)
    u1_sq = v2_sq + omega0_sq * (3.0 * length / 4.0) ** 2
    u2_sq = omega0_sq * (3.0 * length / 4.0) ** 2
    close(v1_sq, 9.0 * g * length / 32.0)
    close(v0_sq, 21.0 * g * length / 32.0)
    close(v2_sq, g * length / 4.0)
    close(u1_sq, 5.0 * g * length / 8.0)
    close(u2_sq, 3.0 * g * length / 8.0)
    assert v0_sq > u1_sq > u2_sq

    mu = 0.5
    switch = (1.0 - mu / 2.0) * length
    close(switch, 3.0 * length / 4.0)
    close(2.0 * mu * g / ((2.0 - mu) * length), omega0_sq)


def verify_q4() -> None:
    mass, g, x0 = 1.7, 9.81, 0.42
    field, rail_gap = 0.8, 0.31
    theta = math.pi / 6.0
    k = field**2 * rail_gap**2 / (4.0 * mass * g)
    x = 2.0 * x0
    current = field * rail_gap * math.cos(theta) / k * (1.0 - x0 / x)
    support = mass * g * math.cos(theta) - field * current * rail_gap * math.sin(theta)
    magnetic = 0.5 * k * x * current**2
    gravity_gain = mass * g * (x - x0) * math.sin(theta)
    close(support, 0.0)
    close(magnetic, 3.0 * mass * g * x0 / 4.0)
    close(gravity_gain, mass * g * x0 / 2.0)
    close(magnetic + gravity_gain, 5.0 * mass * g * x0 / 4.0)


def verify_q5() -> None:
    length, k_speed, v0 = 1.3, 2.1, 0.9
    threshold_sq = 4.0 * k_speed * (k_speed + v0) / length**2
    omega0 = 1.2 * math.sqrt(threshold_sq)
    omega_pi = math.sqrt(omega0**2 - threshold_sq)
    width_rotation = length * (
        2.0 + (omega0 * length
               - math.sqrt(omega0**2 * length**2
                           - 4.0 * k_speed * (k_speed + v0)))
        / (k_speed + v0)
    )
    close(width_rotation,
          2.0 * length + length**2 * (omega0 - omega_pi) / (k_speed + v0))

    omega_small = 0.6 * math.sqrt(threshold_sq)
    cosine_turn = 1.0 - omega_small**2 * length**2 / (
        2.0 * k_speed * (k_speed + v0))
    assert -1.0 < cosine_turn < 1.0
    width_swing = 2.0 * length * (
        1.0 + omega_small * length / (k_speed + v0))
    assert width_swing > 2.0 * length


def verify_q6() -> None:
    p0, patm, v0 = 3.4, 1.0, 2.7
    v_star = v0 * (p0 / patm) ** (5.0 / 7.0)

    def pressure(volume: float) -> float:
        return p0 * (v0 / volume) ** (7.0 / 5.0)

    def kinetic(volume: float) -> float:
        return (2.5 * p0 * v0 * (1.0 - (v0 / volume) ** (2.0 / 5.0))
                - patm * (volume - v0))

    close(pressure(v_star), patm)
    step = 1.0e-5 * v_star
    derivative = (kinetic(v_star + step) - kinetic(v_star - step)) / (2.0 * step)
    assert abs(derivative) < 1.0e-8
    assert kinetic(v_star) > kinetic(v_star - 0.1 * v_star)
    assert kinetic(v_star) > kinetic(v_star + 0.1 * v_star)
    formula = v0 * (2.5 * p0 + patm
                    - 3.5 * p0 * (patm / p0) ** (2.0 / 7.0))
    close(kinetic(v_star), formula)


def verify_q7() -> None:
    f, p, delta, wavelength, screen = 0.10, 0.20, 1.0e-3, 0.5e-6, 0.50
    q = p * f / (p - f)
    h = screen - q
    image_gap = p * delta / (p - f)
    spacing = wavelength * h / image_gap
    overlap = delta * (p + screen) / p
    close(q, 0.20)
    close(h, 0.30)
    close(image_gap, 2.0e-3)
    close(spacing, 75.0e-6)
    close(overlap, 3.5e-3)
    max_order = math.floor((overlap / 2.0) / spacing)
    assert 2 * max_order + 1 == 47


def verify_q8() -> None:
    c = 3.00e8
    wavelength1, wavelength2 = 580.000, 580.001
    vmax, eta = 5000.0, 5.00e6
    close(wavelength1 * (1.0 + vmax / c), 580.0096666666667)
    close(wavelength2 * (1.0 + vmax / c), 580.0106666833333)

    def endpoint_difference(s: float) -> float:
        return (wavelength1 * (1.0 + math.sqrt(vmax**2 + s**2) / c)
                - wavelength2 * (1.0 + s / c))

    low, high = 0.0, 1.0e6
    for _ in range(200):
        middle = (low + high) / 2.0
        if endpoint_difference(middle) > 0.0:
            low = middle
        else:
            high = middle
    s = (low + high) / 2.0
    voltage = s**2 / (2.0 * eta)
    close(endpoint_difference(s), 0.0)
    close(s, 2.390609975e4, 1.0e-9)
    close(voltage, 57.15016053, 1.0e-9)
    assert round(voltage, 1) == 57.2


def main() -> None:
    checks = [verify_q1, verify_q2, verify_q3, verify_q4,
              verify_q5, verify_q6, verify_q7, verify_q8]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")


if __name__ == "__main__":
    main()
