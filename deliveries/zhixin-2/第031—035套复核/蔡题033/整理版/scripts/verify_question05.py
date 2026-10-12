#!/usr/bin/env python3
import json
import math
import random
from pathlib import Path


def recover(a, d, h, n0, b, c):
    k = a * b * c / (b - c)
    d2 = (-a + math.sqrt(a * a + 4.0 * k)) / 2.0
    n = h / (d2 - d / n0)
    d1 = d2 + a
    r = (n + 1.0) / (1.0 / d1 - 1.0 / b)
    return d1, d2, n, r


def main():
    rng = random.Random(3305)
    max_n_rel = 0.0
    max_r_rel = 0.0
    max_coincidence = 0.0
    max_ray_error = 0.0

    # Given numerical data.
    d1, d2, n, r = recover(4.0, 1.0, 5.0, 1.5, 24.37, 6.73)
    assert abs(n - 1.3328656595414732) < 1e-12
    assert abs(r - 30.001133083251737) < 1e-10

    # Synthetic inverse tests: generate physically valid observations from
    # known n and R, then recover both unknowns from b and c.
    for _ in range(500):
        a = rng.uniform(0.5, 8.0)
        d = rng.uniform(0.2, 3.0)
        h = rng.uniform(1.0, 10.0)
        n0 = rng.uniform(1.2, 2.0)
        n_true = rng.uniform(1.05, 1.8)
        d2_true = d / n0 + h / n_true
        d1_true = d2_true + a
        r_true = rng.uniform(3.0, 12.0) * (n_true + 1.0) * d1_true

        inv_b = 1.0 / d1_true - (n_true + 1.0) / r_true
        inv_c = 1.0 / d2_true - (n_true + 1.0) / r_true
        assert inv_b > 0.0 and inv_c > 0.0
        b = 1.0 / inv_b
        c = 1.0 / inv_c
        assert b > c > 0.0

        d1_rec, d2_rec, n_rec, r_rec = recover(a, d, h, n0, b, c)
        max_n_rel = max(max_n_rel, abs(n_rec - n_true) / n_true)
        max_r_rel = max(max_r_rel, abs(r_rec - r_true) / r_true)

        lhs1 = 1.0 / d1_rec - 1.0 / b
        lhs2 = 1.0 / d2_rec - 1.0 / c
        rhs = (n_rec + 1.0) / r_rec
        max_coincidence = max(
            max_coincidence, abs(lhs1 - rhs), abs(lhs2 - rhs)
        )

        # Direct paraxial-ray check at a random small ray height.
        y = rng.uniform(1e-5, 2e-3) * d1_true
        p_before = y / d1_true
        p_after = p_before - (n_true - 1.0) * y / r_true
        q_s = 1.0 / (1.0 / d1_true - (n_true - 1.0) / r_true)
        max_ray_error = max(max_ray_error, abs(p_after - y / q_s))

        q_e = 1.0 / (1.0 / b + 2.0 / r_true)
        max_coincidence = max(max_coincidence, abs(q_s - q_e))

    # Flat-interface limit: the eye image depth equals the multilayer view depth.
    for _ in range(200):
        a = rng.uniform(0.1, 5.0)
        d = rng.uniform(0.1, 2.0)
        h = rng.uniform(0.5, 8.0)
        n0 = rng.uniform(1.2, 2.0)
        n_true = rng.uniform(1.05, 1.8)
        b = a + d / n0 + h / n_true
        n_rec = h / (b - a - d / n0)
        max_n_rel = max(max_n_rel, abs(n_rec - n_true) / n_true)

    assert max_n_rel < 2e-12
    assert max_r_rel < 2e-11
    assert max_coincidence < 2e-10
    assert max_ray_error < 2e-15

    report = {
        "status": "pass",
        "given_data": {
            "D1_cm": d1,
            "D2_cm": d2,
            "n": n,
            "R_cm": r,
        },
        "synthetic_inverse_cases": 500,
        "flat_limit_cases": 200,
        "max_relative_error_n": max_n_rel,
        "max_relative_error_R": max_r_rel,
        "max_coincidence_error": max_coincidence,
        "max_paraxial_ray_error": max_ray_error,
    }
    out = Path(__file__).resolve().parents[1] / "build" / "question05-verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
