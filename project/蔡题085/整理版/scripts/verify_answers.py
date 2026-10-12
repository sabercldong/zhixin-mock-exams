from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 1e-9, abs_tol: float = 1e-12) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_tol):
        raise AssertionError(f"{actual=} differs from {expected=}")


def q1() -> None:
    m, mass_cart, force, length = 2.0, 10.0, 3.0, 4.0
    lam = mass_cart / m
    t0 = math.sqrt(2 * length * m / force)
    u0 = force * t0 / m
    close(u0 * u0, 2 * force * length / m)
    e = 1 / (math.sqrt(1 + lam) - 1)
    close(1 + 2 * e, lam * e * e)
    assert 0 < e < 1 and lam > 3
    stable = t0 * (1 + e) / (1 - e)
    partial = t0 + sum(2 * t0 * e**j for j in range(1, 80))
    close(partial, stable)
    displacement = length / (1 + lam) * (((1 + e) / (1 - e)) ** 2 + lam)
    backward = length * (lam * e - 1) ** 2 / (1 + lam) ** 2
    path = displacement + 2 * backward
    assert path > displacement > 0
    close(0.5 * (force / m) * t0**2, length)
    close(e**2 * length, (e * u0) ** 2 / (2 * force / m))


def q2() -> None:
    alpha, d, beta, area = 168.0, 0.010, 1.16, 7.75
    voltage, eps0 = 940.0, 8.85e-12
    logarithm = math.log((alpha * d + beta) / beta)
    d0 = alpha * eps0 * voltage / logarithm
    capacitance = alpha * eps0 * area / logarithm
    close(d0, 1.560885526827349e-6)
    close(capacitance, 1.286900301373612e-8)
    sigma_left = d0 * (beta - 1) / beta
    sigma_right = -d0 * (alpha * d + beta - 1) / (alpha * d + beta)
    volume_per_area = d0 * (1 / beta - 1 / (alpha * d + beta))
    close(sigma_left + sigma_right + volume_per_area, 0.0, abs_tol=1e-18)
    x = 0.00378
    rho = d0 * alpha / (alpha * x + beta) ** 2
    close(rho, 8.138269623035318e-5)


def q3() -> None:
    radius, mu, beta, t, gravity, acceleration, h = 2.0, 0.35, 0.8, 1.1, 9.8, 15.0, 0.6
    a0 = radius / mu * math.sqrt(beta**2 + beta**4 * t**4) - gravity
    required_edge_friction = radius * math.sqrt(beta**2 + beta**4 * t**4)
    close(mu * (gravity + a0), required_edge_friction)
    flight = (acceleration * t + math.sqrt((acceleration * t) ** 2 + 2 * gravity * h)) / gravity
    close(acceleration * t * flight - 0.5 * gravity * flight**2, -h)
    k = math.sqrt(1 + (beta * t * flight) ** 2)
    close(math.pi * (k * radius) ** 2 / k**2, math.pi * radius**2)
    wz = math.sqrt((acceleration * t) ** 2 + 2 * gravity * h)
    rc = mu * wz / (beta * t)
    omega, length_scale, impulse_scale = beta * t, beta * t * flight, mu * wz
    y = length_scale * rc + (omega * rc - impulse_scale) ** 2 / (2 * mu * gravity)
    final_radius = math.sqrt(rc**2 + y**2)
    close(final_radius, k * rc)


def q4() -> None:
    sigma, a, gas_constant, temperature = 0.072, 0.12, 8.314, 300.0
    p0 = 4 * sigma / a
    n0 = 16 * math.pi * sigma * a**2 / (3 * gas_constant * temperature)
    r = a * math.sqrt(2 / 7)
    pa = 2 * sigma / r
    pb = 6 * sigma / r
    va = 4 * math.pi * ((2 * r) ** 3 - r**3) / 3
    vb = 4 * math.pi * r**3 / 3
    nb = 16 * math.pi * sigma * a**2 / (7 * gas_constant * temperature)
    close(p0 * 4 * math.pi * a**3 / 3, n0 * gas_constant * temperature)
    close(pa * va, n0 * gas_constant * temperature)
    close(pb * vb, nb * gas_constant * temperature)
    close(pb / pa, 3.0)
    close(nb / n0, 3 / 7)


def q5() -> None:
    h, length, mass, gravity, wheel_radius = 0.02, 4.0, 60.0, 9.8, 0.35
    theta = 3 * h / (2 * length)
    torque = mass * gravity * wheel_radius * theta / 2
    friction = theta / 2
    close(torque, 3 * mass * gravity * h * wheel_radius / (4 * length))
    close(friction, 3 * h / (4 * length))
    alpha_exact = math.atan(3 * h / length)
    beta_exact = math.atan(3 * h / (2 * length))
    t0 = mass * gravity / (math.tan(alpha_exact) + math.tan(beta_exact))
    torque_exact = wheel_radius * t0 * (1 / math.cos(alpha_exact) - 1 / math.cos(beta_exact))
    mu_exact = math.log(math.cos(beta_exact) / math.cos(alpha_exact)) / (alpha_exact + beta_exact)
    close(torque_exact, torque, rel=2e-4)
    close(mu_exact, friction, rel=2e-4)


def q6() -> None:
    side = 2.3
    f_equivalent = 1.5 * side
    focal_length = 2 * f_equivalent
    ua, va, ub, vb = 3 * side, 3 * side, 6 * side, 2 * side
    close(1 / ua + 1 / va, 1 / f_equivalent)
    close(1 / ub + 1 / vb, 1 / f_equivalent)
    close(ua / vb, 1.5)
    close(ub - ua, 3 * side)
    close(focal_length, 3 * side)
    height = side * ub / vb
    close(height, ub - ua)
    ac = (-(ub - ua), height)
    acp = (ua - vb, -(ua - vb))
    cross = ac[0] * acp[1] - ac[1] * acp[0]
    dot = ac[0] * acp[0] + ac[1] * acp[1]
    close(cross, 0.0)
    assert dot < 0


def q7() -> None:
    charge, h, speed, magnetic_a = 1.7e-9, 0.25, 0.03, 0.8
    radius = 0.41
    sigma = -charge * h / (2 * math.pi * (h * h + radius * radius) ** 1.5)
    assert sigma < 0
    q_disk = -charge * (1 - h / math.sqrt(h * h + radius * radius))
    derivative = charge * speed * radius**2 / (h * h + radius * radius) ** 1.5
    alpha = -charge * speed * radius / (2 * math.pi * (h * h + radius * radius) ** 1.5)
    close(derivative + 2 * math.pi * radius * alpha, 0.0)
    total_torque = -charge * speed * magnetic_a / h
    integrated = 2 * math.pi * magnetic_a * (
        -charge * speed / (2 * math.pi)
    ) * (1 / h)
    close(integrated, total_torque)
    assert q_disk < 0 and total_torque < 0


def q8() -> None:
    m, c = 2.45e-26, 3.0e8
    de1, de2 = 8.31e-19, 2.95e-19
    photon = de1 + de2
    e1 = m * c**2 + de1
    e2 = m * c**2 + photon
    x = de2 * (2 * m * c**2 + 2 * de1 + de2) / (2 * photon * e1)
    beta0 = (1 - x * x) / (1 + x * x)
    beta0_after = (2 * x * photon + e1 * (1 - x * x)) / (
        2 * x * photon + e1 * (1 + x * x)
    )
    y = (2 * m * c**2 + photon) / (2 * e2)
    beta1 = (1 - y * y) / (1 + y * y)
    beta1_after = (e2 * (1 - y * y) - 2 * y * photon) / (
        e2 * (1 + y * y) - 2 * y * photon
    )
    close(x, 0.2619893428003209)
    close(beta0, 0.8715404298752878)
    close(beta0_after, 0.8715404299070988)
    close(beta1, 2.553288692161375e-10, rel=2e-7, abs_tol=1e-16)
    close(beta1_after, -2.553287270127138e-10, rel=2e-7, abs_tol=1e-16)
    close(math.sqrt((1 - beta0) / (1 + beta0)), x)
    close(math.sqrt((1 - beta1) / (1 + beta1)), y)


def main() -> None:
    for check in (q1, q2, q3, q4, q5, q6, q7, q8):
        check()
    print("蔡题085：8题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
