from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def bisect(function, left: float, right: float, iterations: int = 200) -> float:
    f_left = function(left)
    for _ in range(iterations):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right = middle
        else:
            left = middle
            f_left = f_middle
    return (left + right) / 2


def golden_max(function, left: float, right: float, iterations: int = 300) -> float:
    phi = (1 + math.sqrt(5)) / 2
    c = right - (right - left) / phi
    d = left + (right - left) / phi
    for _ in range(iterations):
        if function(c) < function(d):
            left = c
            c = d
            d = left + (right - left) / phi
        else:
            right = d
            d = c
            c = right - (right - left) / phi
    return (left + right) / 2


def main() -> None:
    # Q1: recurrence and friction-cone critical eccentricity.
    f_over_mg = 3.0
    ratio = f_over_mg / (f_over_mg - 1)
    close(ratio, 1.5)
    n = 6
    d1 = 0.37
    direct_sum = sum(d1 * ratio**i for i in range(n))
    closed_sum = 2 * d1 * (ratio**n - 1)
    close(direct_sum, closed_sum)
    cot15 = 1 / math.tan(math.radians(15))
    y = (cot15 - 1) / (cot15 + 1)
    close(y, 1 / math.sqrt(3))
    close(y / 2, 1 / (2 * math.sqrt(3)))

    # Q2: collision recurrences.
    v_over_r = 2.7
    omega = 0.0
    for i in range(1, 8):
        omega = omega / 3 + 2 * v_over_r / 3
        close(omega, v_over_r * (1 - (1 / 3) ** i))
    omega = 0.0
    for k in range(1, 8):
        omega = 7 * omega / 13 + 6 * v_over_r / 13
        close(omega, v_over_r * (1 - (7 / 13) ** k))

    # Q3: field derivative and induced-dipole force.
    eps0, lam, radius, sphere, h = 2.1, 0.7, 1.3, 0.04, 0.8
    field = lambda x: lam * radius * x / (
        2 * eps0 * (radius**2 + x**2) ** 1.5
    )
    dh = 1e-6
    derivative = (field(h + dh) - field(h - dh)) / (2 * dh)
    force_gradient = 4 * math.pi * eps0 * sphere**3 * field(h) * derivative
    force_closed = (
        math.pi
        * lam**2
        * radius**2
        * sphere**3
        / eps0
        * h
        * (radius**2 - 2 * h**2)
        / (radius**2 + h**2) ** 4
    )
    close(force_gradient, force_closed, tol=1e-7)
    close(field(radius / math.sqrt(2)), lam / (3 * math.sqrt(3) * eps0 * radius))

    # Q4: CM/relative motion and second collision.
    m, k, v0, d = 1.7, 2.3, 4.2, 0.9
    omega_rel = math.sqrt(4 * k / (3 * m))
    lmax = math.sqrt(d**2 + 4 * m * v0**2 / (3 * k))
    relative_energy = 0.5 * k * (lmax**2 - d**2)
    close(relative_energy, 2 * m * v0**2 / 3)
    t2 = math.pi / omega_rel
    v_a_before = v0 / 3 + v0 * math.cos(omega_rel * t2)
    close(v_a_before, -2 * v0 / 3)
    v_b_after = (1 / 3) * (v0 / 3) + (2 / 3) * v_a_before
    close(v_b_after, -v0 / 3)

    # Q5: standard integral and focal length.
    r, mu0, current, charge, mass, speed, rho = 1.4, 0.8, 2.2, 0.3, 0.6, 5.1, 0.07
    integral_b2 = (mu0**2 * current**2 * r**4 / 4) * (3 * math.pi / (8 * r**5))
    v_rho = -charge**2 * rho * integral_b2 / (2 * mass**2 * speed)
    focal = rho * speed / abs(v_rho)
    closed_focal = 64 * mass**2 * speed**2 * r / (
        3 * math.pi * charge**2 * mu0**2 * current**2
    )
    close(focal, closed_focal)

    # Q6: latitude projection and the equivalent modulo-2pi holonomy.
    theta = 0.63
    circle_phase = 2 * math.pi * (1 - math.cos(theta))
    common_foucault = -2 * math.pi * math.cos(theta)
    close(circle_phase - common_foucault, 2 * math.pi)

    # Q7: reproduce the flux, flag the extrapolation roots, and optimize only on the liquid-water interval.
    boltzmann = 1.380649e-23
    t0 = 293.15
    avogadro = 6.02214076e23
    molar_mass = 0.01801528
    molecule = molar_mass / avogadro
    pressure = 2340.0
    latent = 2.45e6
    beta_heat = 20.0
    alpha = 0.06
    mean_speed = math.sqrt(8 * boltzmann * t0 / (math.pi * molecule))
    flux = 0.25 * pressure / (boltzmann * t0) * mean_speed
    close(mean_speed, 586.9641689809241)
    close(flux, 8.483875283615602e25)
    evap0 = latent * molecule * flux

    def evaporation(delta: float) -> float:
        return evap0 * math.exp(-alpha * delta) * math.sqrt(t0 / (t0 - delta))

    equilibrium = bisect(lambda delta: evaporation(delta) - beta_heat * delta, 0, 200)
    close(equilibrium, 134.2302027056623, tol=1e-8)
    # The model has no root in the unfrozen range; its 134 K root is an extrapolation.
    assert all(evaporation(20 * i / 200) > beta_heat * (20 * i / 200) for i in range(201))
    # The handwritten 13.8 K value is retained in the teacher notes only as a
    # traceable discrepancy; it fails the stated balance by about four orders
    # of magnitude when the printed SI units are used.
    handwritten_delta = 13.8
    assert evaporation(handwritten_delta) / (beta_heat * handwritten_delta) > 1e3

    def power(delta: float) -> float:
        return delta / (t0 - delta) * (evaporation(delta) - beta_heat * delta)

    optimum = golden_max(power, 1e-9, 20.0)
    close(optimum, 18.328025536718002, tol=1e-7)
    close(power(optimum), 142585.00228258895, tol=1e-7)
    close(power(20.0), 142030.19624138164, tol=1e-7)
    assert power(optimum) > power(20.0)
    # Unrestricted continuation is unbounded near T -> 0, outside the model's range.
    assert power(t0 - 1e-9) > power(t0 - 1e-8)
    assert abs(power(optimum) - 671.0) > 1e5

    # Q8: angular contraction and the observed receding clock.
    gamma_angle = math.tan(math.radians(60)) / math.tan(math.radians(30))
    close(gamma_angle, 3)
    close(math.sqrt(1 - 1 / gamma_angle**2), 2 * math.sqrt(2) / 3)
    beta_rel = 0.8
    gamma_rel = 1 / math.sqrt(1 - beta_rel**2)
    emission = 90 / (1 + beta_rel)
    observed_clock = emission / gamma_rel
    close(emission, 50)
    close(observed_clock, 30)
    close(observed_clock, 90 * math.sqrt((1 - beta_rel) / (1 + beta_rel)))

    print("All eight questions passed independent algebraic and numerical checks; Q7 max is restricted to 0–20 K")


if __name__ == "__main__":
    main()
