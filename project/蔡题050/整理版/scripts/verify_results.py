from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-10) -> None:
    scale = max(1.0, abs(a), abs(b))
    assert abs(a - b) <= tol * scale, (a, b)


def main() -> None:
    # Q1: cutoff radii and the sphere/cylinder ratio.
    eta, rho0, h0, rho = 0.1, 1.29, 1.0e-2, 2.0e3
    r_cyl = 8 * eta * rho0 * h0 / rho
    r_sph = 6 * eta * rho0 * h0 / rho
    close(r_cyl, 5.16e-6)
    close(r_sph, 3.87e-6)
    close(r_sph / r_cyl, 0.75)

    # Q2: small-angle coefficient from direct finite-amplitude expressions.
    R, L = 3.0, 1.0
    d2 = R * R - L * L / 4
    K = R * R - L * L / 6
    x = d2 / K
    alpha = -2 * x + 0.5 * x * x
    th = 1.0e-4
    w0sq = 2 * 9.8 * math.sqrt(d2) * (1 - math.cos(th)) / K
    n0 = 1 + math.sqrt(d2) * w0sq / 9.8
    nm = math.sqrt(
        math.cos(th) ** 2
        + math.sin(th) ** 2 * (1 - d2 / K) ** 2
    )
    close((nm - n0) / (th * th), alpha, 5e-7)

    # Q3: critical circle geometry.
    R1, R2 = 2.0, 5.0
    rc = (R2 * R2 - R1 * R1) / (2 * R1)
    close(math.sqrt(R2 * R2 + rc * rc) - rc, R1)
    bx_over_b0 = -(R2 * R2 - R1 * R1) / (R1 * R1)
    close(bx_over_b0, -5.25)

    # Q4: collision energy ratio and trigonometric maximum.
    r, h, mu, k = 2.0, 0.3, 0.25, 0.1
    ratio = (2 * r - h) ** 2 / (4 * r * r)
    assert 0 < ratio < 1
    A, B = r - k * mu, r * mu + k
    theta = math.atan2(A, B)
    direct = A * math.sin(theta) + B * math.cos(theta)
    close(direct, math.sqrt((1 + mu * mu) * (r * r + k * k)))

    # Q5: both quadratic matrices are proportional.
    g, ell = 9.8, 1.7
    mass = ((3.0, 1.0), (1.0, 3.0))
    stiff = tuple(tuple((g / ell) * v for v in row) for row in mass)
    for i in range(2):
        for j in range(2):
            close(stiff[i][j] / mass[i][j], g / ell)

    # Q6: early and late limits of collision formulas.
    for a in (0.01, 0.1, 1.0, 5.0):
        f = 0.5 * math.sqrt(math.pi) * math.erf(a)
        hit_fraction = (
            0.5 - f / math.sqrt(math.pi)
            + (1 - math.exp(-a * a)) / (2 * math.sqrt(math.pi) * a)
        )
        assert 0 <= hit_fraction <= 0.5
        impulse_factor = f / (math.sqrt(math.pi) * a)
        assert 0 < impulse_factor <= 1 / math.sqrt(math.pi)

    # Q7: ray tracing with f2=1 reproduces the stated aperture ratios.
    f = 1.0
    f1, l2, l1 = 1.5 * f, 3 * f, 6 * f
    u = 0.2
    y1 = l1 * u
    u1 = u - y1 / f1
    y2 = y1 + l2 * u1
    close(y1, 6 * f * u)
    close(y2, -3 * f * u)

    # Q8: the exact root satisfies the simultaneity quadratic.
    s, lam = 0.4, 0.01
    disc = (1 - s * s) ** 2 - 2 * s * s * lam
    delta = ((1 - s * s) - math.sqrt(disc)) / s
    residual = 0.5 * s * delta * delta - (1 - s * s) * delta + s * lam
    close(residual, 0.0)
    exact_length_scaled = (delta / s) * math.sqrt(1 - s * s)
    approx_length_scaled = lam / math.sqrt(1 - s * s)
    close(exact_length_scaled, approx_length_scaled, 1e-2)

    print("第050套数值、极限、几何与代数交叉验证通过")


if __name__ == "__main__":
    main()
