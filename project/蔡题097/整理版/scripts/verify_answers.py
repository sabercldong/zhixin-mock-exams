from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def main() -> None:
    # Q1: separation angle and endpoint contact condition.
    theta = math.acos(2 / 3)
    close(3 * math.cos(theta) - 2, 0)
    a, b = 3.0, 2.0
    rho = math.hypot(a, b)
    close(3 * b / rho - 2 * a / rho, 0)

    # Q2: two relative flights give 6 m and 2 m.
    u = w = 5 * math.sqrt(2)
    mu, g = 0.1, 10.0
    dt = 2 * w / g
    s1 = (u - 4 * mu * w) * dt
    s2 = (u - 8 * mu * w) * dt
    close(s1, 6.0)
    close(s2, 2.0)
    close(s1 + s2, 8.0)
    contact_relative = u - 9 * mu * w
    assert contact_relative > 0

    # Q3: demagnetizing factors for a thin disk, long cylinder and sphere.
    radius, height = 100.0, 1.0
    exact_disk_factor = height / (2 * math.sqrt(radius**2 + (height / 2) ** 2))
    thin_disk_factor = height / (2 * radius)
    close(exact_disk_factor, thin_disk_factor, 2e-5)
    long_cylinder_factor = 1.0
    sphere_factor = 2 / 3
    assert 0 < exact_disk_factor < sphere_factor < long_cylinder_factor + 1e-12

    # Q4: the spring trajectory reduces to the cyclotron circle at k=0.
    m, q, B, v0 = 2.3, 1.7, 0.8, 4.1
    omega = q * B / (2 * m)
    close(v0 / omega, 2 * m * v0 / (q * B))
    close(2 * m * omega / (q * B), 1.0)

    # Q5: electromechanical power equals minus Joule heating.
    mu0, I0, r0, R0, angle, resistance, speed = 1.2, 2.1, 0.3, 4.0, 0.7, 3.2, 0.08
    A = math.pi * mu0 * r0**2 * math.sin(angle) ** 3 / 2
    current = A * I0 * speed * math.sin(angle) / (resistance * R0**2)
    force = -A**2 * I0**2 * speed * math.sin(angle) ** 2 / (resistance * R0**4)
    close(force * speed + current**2 * resistance, 0.0)

    # Q6: temperature entropy term is nonnegative.
    T0, T1 = 280.0, 520.0
    Tf = (T0 + T1) / 2
    assert math.log(Tf**2 / (T0 * T1)) >= 0
    # The stem defines N atoms on each side, hence N/2 diatomic molecules
    # on each side in part (4).  This is the factor-of-two that the
    # handwritten solution silently changes.
    N, k = 200.0, 1.0
    molecules_per_side = N / 2
    spatial_entropy = 2 * molecules_per_side * k * math.log(2)
    pairing_entropy = molecules_per_side * k * math.log(2)
    close(spatial_entropy + pairing_entropy, 1.5 * N * k * math.log(2))

    # Q7: phase-vector and geometric optical-path formulas coincide.
    no, ne, inc = 1.55, 1.62, 0.6
    io = math.asin(math.sin(inc) / no)
    cot_ie = no * math.sqrt(1 / math.sin(inc) ** 2 - 1 / ne**2)
    direct = math.sin(inc) * (1 / math.tan(io) - cot_ie)
    vector = math.sqrt(no**2 - math.sin(inc) ** 2) - no * math.sqrt(1 - math.sin(inc) ** 2 / ne**2)
    close(direct, vector)

    # Q8: relativistic recurrence tends to the nonrelativistic multiplier.
    N = 8
    delta = math.pi / (N - 1)
    s = math.sin(delta)
    classical = math.cos(delta) / (1 + s)
    beta = 1e-8
    relativistic = math.sqrt(1 - s**2) / (1 + s * math.sqrt(1 - beta**2))
    close(classical, relativistic)

    print("Q1-Q8 independent checks passed")


if __name__ == "__main__":
    main()
