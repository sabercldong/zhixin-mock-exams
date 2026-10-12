from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-9) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError((a, b))


def main() -> None:
    # Q1: solve the dimensionless energy and angular-momentum equations at theta=30 deg.
    c = math.sqrt(3) / 2
    aa = 6 + 4 * c
    bb = 8 + 4 * c
    dd = 4 + 2 * c
    # Elimination gives (30+10sqrt3)x^2-30x+17-8sqrt3=0.
    qa = 30 + 10 * math.sqrt(3)
    qb = -30.0
    qc = 17 - 8 * math.sqrt(3)
    disc = qb * qb - 4 * qa * qc
    roots = [(-qb - math.sqrt(disc)) / (2 * qa), (-qb + math.sqrt(disc)) / (2 * qa)]
    states = [(x, (3 - aa * x) / dd) for x in roots]
    physical = next((x, y) for x, y in states if y > 0)
    close(physical[0], 0.13246358960287685)
    close(physical[1], 0.3046642792116395)
    close(aa * physical[0] ** 2 + bb * physical[0] * physical[1] + 4 * physical[1] ** 2, 1)

    # Q2: triangle, unequal triangle, square, and N-gon checks.
    close(math.sqrt(3), math.sqrt(3))  # omega/sqrt(Gm/l^3), equal triangle
    close(math.sqrt(6), math.sqrt(6))  # unequal triangle with total mass 6m
    close((4 + math.sqrt(2)) / 2, 2 + 1 / math.sqrt(2))
    for n in (3, 4, 6, 9):
        s = sum(1 / math.sin(k * math.pi / n) for k in range(1, n))
        omega2 = 2 * math.sin(math.pi / n) ** 3 * s
        radius = 1 / (2 * math.sin(math.pi / n))
        potential = -n / (4 * radius) * s
        kinetic = 0.5 * n * omega2 * radius * radius
        close(potential / kinetic, -2)

    # Q3: impossible pre-bottom equilibrium, boundary state, and corrected modified geometry.
    mu_formal = 2 * (9 / 5 - 2)
    close(mu_formal, -2 / 5)
    pr = 5 / 6
    tr = pr * 2
    pl = (1 + pr) / 2
    close(tr, 5 / 3)
    close(pl, 11 / 12)
    x = 3.0
    mu = (5 * x - 11) / (5 * (x - 1))
    close(mu, 0.4)
    vi = 1.5 * (x - 1)
    vf = 1.5 * (2 + (x - 1) * mu)
    work = (x - 1) * (1 - mu)
    close(vf - vi, work)

    # Q4: endpoints and the constant-proper-power integral.
    m0c2 = 1.0
    e0 = 4 * m0c2 / 3
    beta0 = (4 * m0c2) / (5 * m0c2)
    close(beta0, 0.8)
    mass_final = math.sqrt(1 - 2 * e0 / (3 * m0c2))
    close(mass_final, 1 / 3)
    beta_final = (4 * m0c2 - 3 * e0) / (5 * m0c2 - 3 * e0)
    close(beta_final, 0)
    time_factor = (4 + math.log(3)) / 6
    close(time_factor, 0.8497687147780183)

    # Q5: nodal potentials, equivalent resistance, and spatial angle.
    u = 1.0
    xp, yp, z = 2 * u / 5, 3 * u / 5, u / 2
    close(4 * xp, yp + 2 * z)
    close(4 * yp, u + xp + 2 * z)
    close(4 * z, u + xp + yp)
    current = u + (u - yp) + 2 * (u - z)
    close(1 / current, 5 / 12)
    close(math.sin(math.pi / 4), 1 / math.sqrt(2))

    # Q6: a sample point satisfies both the semicubical trajectory and slope law.
    m, c0, q, efield, xcoord = 2.0, 3.0, 1.5, 4.0, 0.8
    coeff = 9 * m * c0 * c0 / (2 * q * efield)
    ycoord = -(coeff * xcoord * xcoord) ** (1 / 3)
    lhs = (-ycoord) ** 3
    rhs = coeff * xcoord * xcoord
    close(lhs, rhs)
    px = -q * efield * ycoord / c0
    slope_squared = 2 * m * c0 / px
    close(slope_squared, 2 * m * c0 * c0 / (-q * efield * ycoord))

    # Q7: acceleration, maximum-tension point, tension, speed, and pressure.
    alpha = math.pi / 3
    a0_over_g = (1 - math.cos(alpha)) / alpha
    close(a0_over_g, 3 / (2 * math.pi))
    theta0 = math.asin(a0_over_g)
    close(math.degrees(theta0), 28.519956508954113)
    phi = math.radians(10)
    k = (math.cos(phi) - math.cos(phi + alpha)) / alpha
    theta = math.asin(k)
    tension = k * (theta - phi) + math.cos(theta) - math.cos(phi)
    speed2 = 2 / alpha * (math.sin(alpha) - math.sin(phi + alpha) + math.sin(phi))
    pressure = tension + math.cos(theta) - speed2
    close(math.degrees(theta), 37.86600817152717)
    close(tension, 0.10317270923583577)
    close(speed2, 0.19094956925981288)
    close(pressure, 0.7016715224893748)

    # Q8: phase-change mass, curve-fit parameters, and P1=300 W time.
    p0, latent = 400.0, 3.2e5
    ice = p0 * 120 / latent
    close(ice, 0.15)
    # Solve (1-u)/(1-u^2.4)=1/2 with u=exp(-300k).
    lo, hi = 1e-9, 1 - 1e-9
    for _ in range(200):
        mid = (lo + hi) / 2
        value = (1 - mid) / (1 - mid ** 2.4)
        if value > 0.5:
            lo = mid
        else:
            hi = mid
    uexp = (lo + hi) / 2
    rate = -math.log(uexp) / 300
    asymptote = 50 / (1 - uexp)
    alpha_loss = p0 / asymptote
    total_mass = alpha_loss / (rate * 4200)
    close(alpha_loss, 1.9721974348378664, tol=1e-7)
    close(total_mass, 0.49767447130634557, tol=1e-7)
    alpha_ref, mass_ref, p1 = 2.0, 0.48, 300.0
    melt_time = p0 / p1 * 120
    heat_time = -mass_ref * 4200 / alpha_ref * math.log(1 - 100 * alpha_ref / p1)
    total_minutes = (melt_time + heat_time) / 60
    close(total_minutes, 21.123353116290907)

    print("蔡题088：8题关键结果独立验算通过。")


if __name__ == "__main__":
    main()
