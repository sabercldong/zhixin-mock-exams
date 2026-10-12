from __future__ import annotations

import math


def close(actual: float, expected: float, rel: float = 2e-3) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=rel):
        raise AssertionError(f"{actual=} != {expected=}")


def solve_two_by_two(a: float, b: float, y1: float, y2: float) -> tuple[float, float]:
    determinant = a * a - b * b
    return ((a * y1 - b * y2) / determinant,
            (a * y2 - b * y1) / determinant)


def main() -> None:
    # Q1: reflection at the smooth step and the second-impact friction test.
    theta = math.pi / 3
    vx = -math.cos(2 * theta)
    vy = math.sin(2 * theta)
    close(vx, 0.5)
    close(vy, math.sqrt(3) / 2)
    required_impulse = 3 / 7
    limiting_impulse = math.sqrt(3) / 7
    assert limiting_impulse < required_impulse

    # Q2: charge fraction, scale law and interaction energy.
    charge_fraction = (1 - (3 / 4) ** 3) / ((3 / 2) ** 3 - (3 / 4) ** 3)
    close(charge_fraction, 37 / 189, rel=1e-12)
    close(1 / (3 / 2), 2 / 3, rel=1e-12)
    potential_at_q1 = -48 / 35 + 1
    potential_at_q2 = -2 / 9 + 1 / 2
    energy_coefficient = 0.5 * (potential_at_q1 + potential_at_q2)
    close(energy_coefficient, -59 / 1260, rel=1e-12)

    # Q3: cone precession formula and dimensional scaling.
    mass, height, beta, spin, gravity = 2.1, 0.42, math.radians(50), 130.0, 9.81
    radius = height * math.tan(beta / 2)
    inertia = 3 * mass * radius**2 / 10
    h_c = 3 * height / 4
    omega_from_torque = mass * gravity * h_c / (inertia * spin)
    omega_closed = 5 * gravity / (2 * spin * height * math.tan(beta / 2) ** 2)
    close(omega_from_torque, omega_closed, rel=1e-12)

    # Q4: bridge balance and resistivity, independently evaluated in SI units.
    standard = 0.6000
    r1 = r2 = 4004.7
    r3 = r4 = 3000.1
    unknown = standard * r1 / r4
    close(r1 / r4, r2 / r3, rel=1e-12)
    close(unknown, 0.8009, rel=2e-4)
    length = 1.059
    diameter = 0.4856e-3
    resistivity = unknown * math.pi * diameter**2 / (4 * length)
    close(resistivity, 1.401e-7, rel=5e-4)

    # Q5: direct substitution into the two-source thermal-resistance matrix.
    conductivity, sphere_radius, separation = 1.7, 0.08, 0.63
    delta1, delta2 = 13.0, 7.0
    scale = 4 * math.pi * conductivity
    p1, p2 = solve_two_by_two(1 / sphere_radius, 1 / separation,
                              scale * delta1, scale * delta2)
    check1 = p1 / sphere_radius + p2 / separation
    check2 = p1 / separation + p2 / sphere_radius
    close(check1, scale * delta1, rel=1e-12)
    close(check2, scale * delta2, rel=1e-12)
    far_p1 = 4 * math.pi * conductivity * sphere_radius * delta1
    assert p1 > far_p1 * 0.9

    # Q6: equal powers of a test point with respect to two coaxial circles.
    big_radius, small_radius, center_distance = 4.2, 1.7, 6.3
    x = (big_radius**2 - small_radius**2 - center_distance**2) / (2 * center_distance)
    power_big = (x + center_distance) ** 2 - big_radius**2
    power_small = x**2 - small_radius**2
    close(power_big, power_small, rel=1e-12)

    # Q7: exact full-bridge response and its small-signal form.
    resistance, change, source = 120.0, 0.012, 5.0
    node_a = source * (resistance - change) / (2 * resistance)
    node_b = source * (resistance + change) / (2 * resistance)
    close(node_a - node_b, -source * change / resistance, rel=1e-12)

    # Q8: invariant mass, centre-of-momentum boost and tangent-angle bounds.
    total_energy = 15 / 2
    px, py = 4.0, 3 / 2
    momentum = math.hypot(px, py)
    beta_c = momentum / total_energy
    gamma_c = 1 / math.sqrt(1 - beta_c**2)
    close(beta_c, math.sqrt(73) / 15, rel=1e-12)
    close(gamma_c, 15 / (2 * math.sqrt(38)), rel=1e-12)
    invariant_mass = math.sqrt(total_energy**2 - momentum**2)
    close(invariant_mass, math.sqrt(38), rel=1e-12)
    p_star = math.sqrt(13 * 29 / (4 * 38))
    e1_star = 53 / (2 * math.sqrt(38))
    shift = gamma_c * beta_c * e1_star
    parallel_scale = gamma_c * p_star
    assert shift > parallel_scale
    cos_alpha = -parallel_scale / shift
    alpha = math.acos(cos_alpha)
    phi = math.atan2(p_star * math.sin(alpha), parallel_scale * math.cos(alpha) + shift)
    theta_c = math.atan2(py, px)
    close(math.degrees(phi), 34.620, rel=5e-4)
    close(math.degrees(theta_c - phi), -14.064, rel=5e-4)
    close(math.degrees(theta_c + phi), 55.176, rel=5e-4)

    print("蔡题068：数值、量纲、极限与等价式核验通过。")


if __name__ == "__main__":
    main()
