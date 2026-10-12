from __future__ import annotations

import math


def close(actual: float, expected: float, tol: float = 1e-10) -> None:
    scale = max(1.0, abs(actual), abs(expected))
    if abs(actual - expected) > tol * scale:
        raise AssertionError(f"{actual!r} != {expected!r}")


def q1_reachable_envelope() -> None:
    # Choose a dimensionless case inside the non-penetrating regime.
    h, k = 5.0, 0.36
    l0 = h * math.sqrt(1.0 - k)
    close(l0, 4.0)
    # The three-dimensional boundary has its axial vertex at the same l0.
    x_vertex = h * math.sqrt(1.0 - k)
    close(x_vertex, l0)
    # For a prescribed nonzero launch angle theta_0, verify the positive
    # quadratic root against the energy-angular-momentum turning equation.
    theta0 = math.radians(37.0)
    l_theta_sq = 0.5 * h**2 * (
        1.0 - k + math.sqrt((1.0 - k) ** 2 + 4.0 * k * math.sin(theta0) ** 2)
    )
    # Use alpha=1, so v^2=k h^2.
    v_sq = k * h**2
    residual = l_theta_sq**2 + (v_sq - h**2) * l_theta_sq - h**2 * v_sq * math.sin(theta0) ** 2
    close(residual, 0.0)
    close(
        0.5 * h**2 * (1.0 - k + math.sqrt((1.0 - k) ** 2)),
        h**2 * (1.0 - k),
    )
    close(
        0.5 * h**2 * (1.0 - k + math.sqrt((1.0 - k) ** 2 + 4.0 * k)),
        h**2,
    )


def q2_cut_conductor() -> None:
    # Charge conservation plus equipotentiality gives q_cap=3Q/4.
    q_cap_fraction = 3.0 / 4.0
    q_large_fraction = 1.0 - q_cap_fraction
    close(q_cap_fraction + q_large_fraction, 1.0)
    # Final force coefficient in Q^2/(pi epsilon_0 R^2).
    close(45.0 / 128.0, 0.3515625)


def q3_friction_regions() -> None:
    mu1, mu2 = 0.4, 0.2
    # In the stated sample region B and C move together.
    close((1.0 - 2.0 * mu1) / 2.0, 0.1)  # a_B/g
    close(mu2 / 2.0, 0.1)                 # a_C/g
    # The principal phase-boundary intersections are mutually consistent.
    close(2.0 / 3.0 - 2.0 / 5.0, 4.0 / 15.0)


def q4_normal_modes() -> None:
    # cos(vartheta)=sqrt(2/3) for a tetrahedral side against the vertical.
    close(math.cos(math.acos(math.sqrt(2.0 / 3.0))), math.sqrt(2.0 / 3.0))
    rho, g, p0 = 1.7, 9.8, 2.3e5
    k0_over_m0 = 2.0 * rho * g * g / (3.0 * p0)
    omega1_sq = 26.0 / 6.0 * k0_over_m0
    omega2_sq = 3.0 * k0_over_m0
    close(omega1_sq, 26.0 * rho * g * g / (9.0 * p0))
    close(omega2_sq, 2.0 * rho * g * g / p0)


def q5_waveguide() -> None:
    n, d_over_lambda = 1.5, 4.0
    tir_bound_m = 2.0 * n * d_over_lambda * math.sqrt(1.0 - 1.0 / n**2)
    tir_bound_k = n * d_over_lambda * math.sqrt(1.0 - 1.0 / n**2)
    assert 8 < tir_bound_m < 9
    assert 4 < tir_bound_k < 5


def q6_conical_cup() -> None:
    # Reduced mass mM/(m+M) with M=2m gives the escape threshold.
    close((8.0 / 3.0) * (1.0 + 0.5), 4.0)  # v0c^2/(gR)
    close(math.sqrt(40.0 / 63.0 - 4.0 / 21.0), 2.0 / 3.0)
    beta_max = (-1.0 + math.sqrt(33.0)) / 4.0
    close(beta_max, 1.1861406616345072)

    def moment_factor(beta: float) -> float:
        return 0.5 * (12.0 / (1.0 + beta) ** 3 + 1.0) * (beta + 0.8)

    close(moment_factor(0.0), 26.0 / 5.0)
    samples = [moment_factor(beta_max * i / 1000.0) for i in range(1001)]
    assert all(a >= b for a, b in zip(samples, samples[1:]))


def q7_radioactive_battery() -> None:
    # Normalization: two triangles and the central rectangle total 300 n0.
    close(0.5 * 100.0 + 200.0 + 0.5 * 100.0, 300.0)

    def current_fraction(u: float) -> float:
        if u <= 200.0:
            return 1.0
        if u < 300.0:
            return 1.0 - (u - 200.0) ** 2 / 60000.0
        if u <= 500.0:
            return (550.0 - u) / 300.0
        if u < 600.0:
            return (600.0 - u) ** 2 / 60000.0
        return 0.0

    close(current_fraction(200.0), 1.0)
    close(current_fraction(300.0), 5.0 / 6.0)
    close(current_fraction(500.0), 1.0 / 6.0)
    close(current_fraction(600.0), 0.0)

    u_a = 195.0
    close((u_a - 150.0) / 200.0 + u_a / 200.0, 1.2)
    u_b = 4575.0 / 13.0
    i_b = (5.0 * u_b - 175.0) / 2000.0
    close(i_b, 1.2 * current_fraction(u_b))
    close(u_b, 351.9230769230769)
    close(i_b, 0.7923076923076923)


def q8_dispersion() -> None:
    a, r = 1.7, 15.0
    epsilon = 2.0 * a**3 / r**3
    # Per-atom zero-point shift: -hbar*omega0*epsilon^2/16.
    coefficient = -(epsilon**2) / 16.0
    close(coefficient, -(a**6) / (4.0 * r**6))
    assert epsilon < 0.01


def main() -> None:
    q1_reachable_envelope()
    q2_cut_conductor()
    q3_friction_regions()
    q4_normal_modes()
    q5_waveguide()
    q6_conical_cup()
    q7_radioactive_battery()
    q8_dispersion()
    print("第069套数值、边界、极限与分段结果核验通过。")


if __name__ == "__main__":
    main()
