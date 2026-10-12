from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def bisect(function, left: float, right: float, steps: int = 120) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left * f_right > 0:
        raise ValueError("root is not bracketed")
    for _ in range(steps):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return (left + right) / 2


def main() -> None:
    # Q1: finite spokes, not only their rim endpoints.
    t = bisect(lambda q:q-math.sin(2*q)/2-math.pi/12, .4, 1.0)
    lam_star = math.cos(t)**2
    close(lam_star, .52417407552, tol=1e-9)
    a = bisect(lambda q:q+math.sin(q)-math.pi/12, 0., .5)
    close(-math.cos(a), -.9914203631921377)
    lam=.3
    turn=math.acos(math.sqrt(lam))
    pstar=turn-math.sqrt(lam*(1-lam))-math.pi/6
    root=bisect(lambda q:q-lam*math.tan(q)-pstar, -.1,.1)
    alpha=math.sqrt(1-lam*lam)-lam*math.tan(root)
    close(alpha,.94995304862,tol=1e-9)
    close(1/alpha,1.05268360521,tol=1e-9)

    # Q2: force balance closes with the exponential capillary profile.
    rho, rho0, h, r, sigma, g = 7800.0, 1000.0, 1.2e-3, 0.012, 0.072, 9.8
    a = math.sqrt(sigma / (rho0 * g))
    depth = (rho - rho0) * h / (rho0 * (1 + 2 * a / r))
    theta0 = depth / a
    force_length = (rho - rho0) * h / rho0 - 2 * sigma * theta0 / (r * rho0 * g)
    close(depth, force_length)

    # Q3: terminal voltage and angular impulse give the same charge.
    m, length, B, C, omega0 = 0.8, 1.1, 0.45, 0.02, 1.7
    beta = B**2 * C * length**2 / (4 * m)
    omega1 = omega0 / (1 + beta)
    charge = C * B * length**2 * omega1 / 2
    angular_impulse = B * length**2 * charge / 2
    close(m * length**2 * (omega0 - omega1), angular_impulse)

    # Q4: plane integral and double-lamp second-order coefficient.
    l0 = 2.7
    plane_integral = 2 * math.pi * l0**2 * (1 / (2 * l0**2))
    close(plane_integral, math.pi)
    lamp_lambda = math.sqrt(3)
    quadratic = 2 * (3 - lamp_lambda**2) / (1 + lamp_lambda**2) ** 3
    close(quadratic, 0.0)

    # Q5: analytic pressure, work and entropy at mechanical equilibrium.
    lambda_m = 2 ** (-5 / 3)
    p_right = (1 - lambda_m ** (3 / 5)) ** (5 / 3)
    close(p_right, lambda_m)
    w = 1 - lambda_m - p_right
    close(w, 1 - 2 ** (-2 / 3))
    t_ratio = lambda_m ** (2 / 5)
    close(t_ratio, 2 ** (-2 / 3))
    entropy_per_mole = 1.5 * math.log(t_ratio) + math.log(2)
    close(entropy_per_mole, 0.0)

    # Q6: Maxwell reconstruction and superconducting force factor.
    mu0, current, radius, sep, moment, inductance = 1.0, 0.7, 1.3, 0.9, 0.4, 0.2
    k = mu0 * current / radius**3 * (12 * sep**2 - 3) / (1 + sep**2) ** 3.5
    assert k > 0 and sep > 0.5
    flux_slope = 3 * mu0 * moment * sep / (2 * radius**2 * (1 + sep**2) ** 2.5)
    induced_slope = -2 * flux_slope**2 / inductance
    total_force_slope = moment * k + induced_slope
    criterion_left = 9 * mu0 * moment * sep**2 / (
        2 * inductance * radius * (1 + sep**2) ** 1.5
    )
    criterion_right = current * (12 * sep**2 - 3)
    assert (total_force_slope < 0) == (criterion_left > criterion_right)

    # Q7: critical ray widths at the paraxial focus and y=10 cm.
    radius_cm, index = 5.0, 1.56
    h0 = index * radius_cm / (index - 1)
    theta_c = math.asin(1 / index)
    x_c = radius_cm * math.sin(theta_c)
    y_c = radius_cm * math.cos(theta_c)
    width_focus = 2 * ((h0 - y_c) / math.tan(theta_c) - x_c)
    width_10 = 2 * abs(x_c - (10.0 - y_c) / math.tan(theta_c))
    close(h0, 13.928571428571429)
    close(x_c, 3.205128205128205)
    close(width_focus, 17.75420299067057)
    close(width_10, 8.346607275353229)

    # Q8: energy and axial-angular-momentum thresholds.
    g_value, bowl_radius = 9.8, 2.4
    arbitrary = 2 * math.sqrt(g_value * bowl_radius / 3)
    horizontal = math.sqrt(3 * g_value * bowl_radius)
    rho_initial = math.sqrt(5) * bowl_radius / 3
    rim_speed_fraction = rho_initial / bowl_radius
    close(0.5 * arbitrary**2, 2 * g_value * bowl_radius / 3)
    close(
        0.5 * horizontal**2 + g_value * bowl_radius / 3,
        0.5 * (rim_speed_fraction * horizontal) ** 2 + g_value * bowl_radius,
    )

    print("All eight sets of independent numerical and algebraic checks passed")


if __name__ == "__main__":
    main()
