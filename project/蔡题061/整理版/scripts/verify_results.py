from __future__ import annotations

import cmath
import math


def close(actual: float, expected: float, tol: float = 1.0e-10) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{actual} != {expected}")


def bisect(function, left: float, right: float, iterations: int = 100) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left * f_right > 0.0:
        raise AssertionError("求根区间未包围零点")
    for _ in range(iterations):
        middle = 0.5 * (left + right)
        f_middle = function(middle)
        if f_left * f_middle <= 0.0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return 0.5 * (left + right)


def q1() -> None:
    # 取教师版示例参数，复核静止条件、纯滚动加速度及隐式方向方程。
    g, m1, m2, m, radius, axle = 9.81, 1.0, 1.0, 1.0, 2.0, 0.5
    total = m1 + 2.0 * m2
    inertia = 0.5 * m1 * axle**2 + m2 * radius**2
    theta0 = math.asin(m * axle / (radius * (total + m)))
    mu_min = math.tan(theta0)
    close(mu_min, m * axle / math.sqrt(radius**2 * (total + m) ** 2 - m**2 * axle**2))
    a0 = m * g * radius * axle / (m * axle**2 + inertia + total * radius**2)
    close((total + inertia / radius**2 + m * (axle / radius) ** 2) * a0,
          m * g * axle / radius)

    theta1 = theta0 / 2.0
    ratio = axle / radius

    def effective_mass(alpha: float) -> float:
        return total + inertia / radius**2 + m * (
            1.0 + ratio**2 - 2.0 * ratio * math.sin(alpha + theta1)
        )

    def direction_equation(alpha: float) -> float:
        acceleration = g * (
            m * ratio * math.cos(alpha) - (total + m) * math.sin(theta1)
        ) / effective_mass(alpha)
        return acceleration * math.cos(alpha + theta1) - g * math.sin(alpha)

    alpha = bisect(direction_equation, 0.02, 0.03)
    close(direction_equation(alpha), 0.0, 1.0e-12)
    if not 0.0 < alpha < math.pi / 2.0 or effective_mass(alpha) <= 0.0:
        raise AssertionError("第 1 题数值根不在物理解区间")


def q2() -> None:
    # 直接递推与闭式结果逐项比较，并复核最大碰撞次数。
    close(6.0 * 5.0 / 2.0, 15.0)
    for count in (2, 3, 6, 100):
        u2_over_gh = 0.0
        for k in range(1, count):
            u2_over_gh = (k / (k + 1.0)) ** 2 * (u2_over_gh + 2.0)
        expected_u2 = (count - 1.0) * (2.0 * count - 1.0) / (3.0 * count)
        close(u2_over_gh, expected_u2)
        v2_over_gh = u2_over_gh + 2.0
        expected_v2 = (count + 1.0) * (2.0 * count + 1.0) / (3.0 * count)
        close(v2_over_gh, expected_v2)
    close((6.0 + 1.0) * (2.0 * 6.0 + 1.0) / (3.0 * 6.0), 91.0 / 18.0)
    close((100.0 + 1.0) * (2.0 * 100.0 + 1.0) / (3.0 * 100.0), 20301.0 / 300.0)


def q3() -> None:
    # AU-y 单位中 GM_sun=4pi^2；随后转回 SI 复核入轨速度与爆炸能量。
    period, perihelion = 1200.0, 0.1
    semi_major = period ** (2.0 / 3.0)
    aphelion = 2.0 * semi_major - perihelion
    close(semi_major, 112.9243234657, 1.0e-10)
    close(aphelion, 225.7486469314, 1.0e-10)
    v_earth = 2.0 * math.pi
    v_comet = v_earth * math.sqrt(2.0 - 1.0 / semi_major)
    v_tangent = v_earth * math.sqrt(2.0 * perihelion * aphelion / (perihelion + aphelion))
    v_radial = math.sqrt(v_comet**2 - v_tangent**2)
    theta = math.atan2(v_radial, v_tangent)
    v_relative = math.hypot(v_tangent - v_earth, v_radial)
    close(theta, 1.248, 5.0e-4)
    close(v_relative, 9.099, 5.0e-4)

    g, earth_radius, r3 = 10.0, 6.4e6, 1.0e8
    gm_earth = g * earth_radius**2
    target_speed = math.sqrt(2.0 * gm_earth * earth_radius / (r3 * (r3 + earth_radius)))
    close(target_speed, 701.9628763, 1.0e-9)
    relative_si = v_relative * 1.5e11 / (365.0 * 86400.0)
    delta_v = relative_si - target_speed
    explosion_energy = 1.0e6 * delta_v**2 / 18.0
    if not 1.00e14 < explosion_energy < 1.02e14:
        raise AssertionError("第 3 题爆炸能量超出复核区间")


def q4() -> None:
    # 任选一组无全反射的折射参数，复核 n^2 dS_perp dOmega 的雅可比。
    n1, n2, theta1 = 1.0, 1.5, 0.73
    theta2 = math.asin(n1 * math.sin(theta1) / n2)
    dtheta2_dtheta1 = n1 * math.cos(theta1) / (n2 * math.cos(theta2))
    solid_angle_ratio = (
        math.sin(theta2) / math.sin(theta1) * dtheta2_dtheta1
    )
    projected_area_ratio = math.cos(theta2) / math.cos(theta1)
    invariant_ratio = (n2 / n1) ** 2 * projected_area_ratio * solid_angle_ratio
    close(invariant_ratio, 1.0)


def q5() -> None:
    # 以无量纲参数复核磁通、势能导数、临界速度和最大力位置。
    mu0, moment, radius, inductance, mass = 1.7, 2.3, 0.8, 1.4, 3.2

    def flux(x: float) -> float:
        return mu0 * moment * radius**2 / (2.0 * (x**2 + radius**2) ** 1.5)

    def energy(x: float) -> float:
        return flux(x) ** 2 / (2.0 * inductance)

    def force(x: float) -> float:
        return 3.0 * mu0**2 * moment**2 * radius**4 * x / (
            4.0 * inductance * (x**2 + radius**2) ** 4
        )

    x, step = 1.1, 1.0e-5
    numerical_force = -(energy(x + step) - energy(x - step)) / (2.0 * step)
    close(numerical_force, force(x), 1.0e-9)
    critical_speed = mu0 * moment / (2.0 * radius * math.sqrt(mass * inductance))
    close(0.5 * mass * critical_speed**2, energy(0.0))
    peak_x = radius / math.sqrt(7.0)
    if not force(peak_x) > force(0.99 * peak_x) or not force(peak_x) > force(1.01 * peak_x):
        raise AssertionError("第 5 题最大排斥力位置复核失败")


def q6() -> None:
    # Jones 分量的精确投影与小误差近似相互复核。
    birefringence, dispersion = 0.18, 1.2e-3
    epsilon = 0.5 * math.pi * dispersion / birefringence
    exact_ratio = math.tan(epsilon / 2.0) ** 2
    approximation = math.pi**2 / 16.0 * (dispersion / birefringence) ** 2
    close(exact_ratio, approximation, 1.0e-4)
    field = (1.0 / math.sqrt(2.0), 1j * cmath.exp(1j * epsilon) / math.sqrt(2.0))
    e_plus = (1.0 / math.sqrt(2.0), 1j / math.sqrt(2.0))
    e_minus = (1.0 / math.sqrt(2.0), -1j / math.sqrt(2.0))
    amp_plus = e_plus[0].conjugate() * field[0] + e_plus[1].conjugate() * field[1]
    amp_minus = e_minus[0].conjugate() * field[0] + e_minus[1].conjugate() * field[1]
    close(abs(amp_minus) ** 2 / abs(amp_plus) ** 2, exact_ratio)


def q7() -> None:
    # 内外标势在柱面连续，法向 H 跃变等于 M cos(phi)。
    radius, magnetization, phi = 1.9, 2.4, 0.67
    a = magnetization / 2.0
    b = magnetization * radius**2 / 2.0
    close(a * radius * math.cos(phi), b / radius * math.cos(phi))
    h_rho_out = b / radius**2 * math.cos(phi)
    h_rho_in = -a * math.cos(phi)
    close(h_rho_out - h_rho_in, magnetization * math.cos(phi))
    h_phi_out = b / radius**2 * math.sin(phi)
    h_phi_in = a * math.sin(phi)
    close(h_phi_out, h_phi_in)


def q8() -> None:
    # 令 mu=GM/c^2=1、m0=c=1，复核 ISCO 的一、二阶条件和频移。
    mu, mass, c = 1.0, 1.0, 1.0
    radius = 6.0 * mu
    angular_momentum = 2.0 * math.sqrt(3.0) * mu * mass * c

    first = (
        mu * mass * c**2 / radius**2
        - angular_momentum**2 / (mass * radius**3)
        + 3.0 * mu * angular_momentum**2 / (mass * radius**4)
    )
    second = (
        -2.0 * mu * mass * c**2 / radius**3
        + 3.0 * angular_momentum**2 / (mass * radius**4)
        - 12.0 * mu * angular_momentum**2 / (mass * radius**5)
    )
    close(first, 0.0)
    close(second, 0.0)
    gamma = math.sqrt(2.0)
    impact = radius * math.sqrt(1.0 / (1.0 - 2.0 * mu / radius))
    close(impact, 3.0 * math.sqrt(6.0) * mu)
    omega = math.sqrt(mu / radius**3)
    close(omega * impact, 0.5)
    frequency_ratio = 1.0 / (gamma * (1.0 - omega * impact))
    close(frequency_ratio, math.sqrt(2.0))


def main() -> None:
    for verify in (q1, q2, q3, q4, q5, q6, q7, q8):
        verify()
    print("第 061 套八题的关键代数、数值、边界与极限验证通过")


if __name__ == "__main__":
    main()
