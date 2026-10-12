from __future__ import annotations

import math
from itertools import product

import numpy as np


def close(actual: float, expected: float, tol: float = 1.0e-10) -> None:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{actual} != {expected}")


def q1() -> None:
    mu = (3.0 + math.sqrt(3.0)) / 6.0
    jt_over_m_v = (3.0 * math.sqrt(2.0) + math.sqrt(6.0)) / 6.0
    jn_over_m_v = math.sqrt(2.0)
    close(jt_over_m_v / jn_over_m_v, mu)
    threshold = (15.0 * math.sqrt(2.0) + 7.0 * math.sqrt(6.0)) / 12.0
    reconstructed = math.sqrt(6.0) / 6.0 + 2.5 * jt_over_m_v
    close(threshold, reconstructed)


def q2() -> None:
    impulse_over_mv = math.sqrt(3.0) / 3.0
    rod_radial = impulse_over_mv / 2.0
    c_radial = math.sqrt(3.0) / 2.0 - impulse_over_mv
    close(rod_radial, c_radial)
    c_speed_sq = c_radial**2 + 0.5**2
    close(c_speed_sq, 1.0 / 3.0)
    final_energy_over_mv2 = 2.0 * 0.5 * rod_radial**2 + 0.5 * c_speed_sq
    close(final_energy_over_mv2, 0.25)
    close(4.0 * ((math.pi / 2.0) / 0.25 + math.pi / 0.5), 16.0 * math.pi)


def q3() -> None:
    triangle = 1.0 / 12.0
    j0 = 6.0 * (2.0 * triangle + 1.0 / 3.0 + 4.0 / 3.0)
    close(j0, 11.0)
    close(j0 + 12.0 * 3.0, 47.0)
    lower_sq = (188.0 / 3.0) * (2.0 * math.sqrt(3.0) - 3.0)
    upper_sq = 3572.0 / 27.0
    if not 0.0 < lower_sq < upper_sq:
        raise AssertionError("翻越冲量窗口为空")


def q4() -> None:
    l1, l2, l3 = 2.0, 5.0, 3.0
    np_over_n0 = (1.0 / l1 + 1.0 / l2) / (1.0 / l1 + 1.0 / l2 + 1.0 / l3)
    left_rate = (1.0 - np_over_n0) / l1
    right_rate = (1.0 - np_over_n0) / l2
    ta = 1.0 / left_rate
    remaining_right = 1.0 - right_rate * ta
    tb = remaining_right * (l2 + l3)
    t1 = l1 + l3
    close((ta + tb) / t1, (l2 + 2.0 * l3) / (l1 + l3))


def potential(charges: list[tuple[float, np.ndarray]], point: np.ndarray) -> float:
    return sum(charge / np.linalg.norm(point - position) for charge, position in charges)


def q5() -> None:
    q, radius, a, theta = 1.0, 1.3, 3.1, 0.61
    b = radius**2 / a
    upper = np.array([a * math.sin(theta), 0.0, a * math.cos(theta)])
    lower = np.array([a * math.sin(theta), 0.0, -a * math.cos(theta)])
    image_upper = upper * (radius**2 / a**2)
    image_lower = lower * (radius**2 / a**2)
    charges = [
        (q, upper),
        (-q, lower),
        (-q * radius / a, image_upper),
        (q * radius / a, image_lower),
    ]
    close(potential(charges, np.array([0.7, -0.4, 0.0])), 0.0, 1.0e-9)
    for polar, azimuth in [(0.4, 0.2), (1.1, 2.0), (2.2, -0.7)]:
        point = radius * np.array(
            [
                math.sin(polar) * math.cos(azimuth),
                math.sin(polar) * math.sin(azimuth),
                math.cos(polar),
            ]
        )
        close(potential(charges, point), 0.0, 1.0e-9)
    distance = math.sqrt(a * a + b * b + 2.0 * radius**2 * math.cos(2.0 * theta))
    close(distance, np.linalg.norm(upper - image_lower))


def q6() -> None:
    beta, omega_r_over_c = 0.63, 0.08
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    ntheta, nphi = 500, 720
    theta = (np.arange(ntheta) + 0.5) * math.pi / ntheta
    phi = (np.arange(nphi) + 0.5) * 2.0 * math.pi / nphi
    th, ph = np.meshgrid(theta, phi, indexing="ij")
    geometric = np.sqrt(1.0 + (gamma**2 - 1.0) * np.sin(th) ** 2 * np.cos(ph) ** 2)
    sigma_prime = gamma * (1.0 + beta * omega_r_over_c * np.sin(th) * np.sin(ph)) / geometric
    ds_prime = np.sin(th) * geometric / gamma
    total_over_sigma_r2 = np.sum(sigma_prime * ds_prime) * (math.pi / ntheta) * (2.0 * math.pi / nphi)
    close(total_over_sigma_r2, 4.0 * math.pi, 2.0e-5)
    torque_factor = -gamma + gamma * beta**2
    close(torque_factor, -1.0 / gamma)


def q7() -> None:
    k_a = 0.02 * math.pi
    rho = (np.arange(1_000_000) + 0.5) * k_a / 1_000_000
    density_radial = 2.0 / (math.pi * np.sqrt(k_a * k_a - rho * rho))
    normalization = np.sum(density_radial) * k_a / 1_000_000
    close(normalization, 1.0, 8.0e-4)
    theta = 0.83
    jacobian = np.linalg.det(np.diag([2.0 * math.cos(theta), 2.0]))
    close(jacobian, 4.0 * math.cos(theta))


OFFSETS = [
    offset
    for zero_axis in range(3)
    for signs in product((-1, 1), repeat=2)
    for offset in [
        tuple(
            0 if axis == zero_axis else signs[axis - (axis > zero_axis)]
            for axis in range(3)
        )
    ]
]


def fcc_torus(length: int) -> tuple[list[tuple[int, int, int]], np.ndarray]:
    size = 2 * length
    nodes = [p for p in product(range(size), repeat=3) if sum(p) % 2 == 0]
    index = {p: i for i, p in enumerate(nodes)}
    laplacian = np.zeros((len(nodes), len(nodes)))
    for p, i in index.items():
        for offset in OFFSETS:
            neighbor = tuple((p[axis] + offset[axis]) % size for axis in range(3))
            j = index[neighbor]
            laplacian[i, i] += 1.0
            laplacian[i, j] -= 1.0
    return nodes, laplacian


def resistance(laplacian: np.ndarray, ia: int, ib: int) -> float:
    keep = [i for i in range(len(laplacian)) if i != ib]
    source = np.zeros(len(laplacian))
    source[ia] = 1.0
    source[ib] = -1.0
    voltage = np.linalg.solve(laplacian[np.ix_(keep, keep)], source[keep])
    return voltage[keep.index(ia)]


def q8() -> None:
    values = []
    for length in (2, 3, 4):
        nodes, laplacian = fcc_torus(length)
        index = {p: i for i, p in enumerate(nodes)}
        a = index[(0, 0, 0)]
        b = index[(1, 1, 0)]
        c = index[(2, 0, 0)]
        d = index[(2, 1, 1)]
        e = index[(2, 2, 0)]
        rab = resistance(laplacian, a, b)
        expected_foster = 2.0 * (len(nodes) - 1.0) / (12.0 * len(nodes))
        close(rab, expected_foster, 1.0e-9)
        combination = 2.0 * resistance(laplacian, a, c) + 4.0 * resistance(laplacian, a, d) + resistance(laplacian, a, e)
        values.append((len(nodes), rab, combination))
    if not values[-1][1] < 1.0 / 6.0 or not values[-1][2] < 4.0 / 3.0:
        raise AssertionError("周期网络未向无限网络结果的下方收敛")
    print("FCC 周期逼近：", values)


def main() -> None:
    for verify in (q1, q2, q3, q4, q5, q6, q7, q8):
        verify()
    print("八题关键代数、边界、归一化与有限网络数值验证通过")


if __name__ == "__main__":
    main()
