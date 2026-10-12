"""由节点方程及四种元件状态独立求解，不用分区闭式式构造数值答案。"""
from pathlib import Path
import itertools
import json
import math
import random

ROOT = Path(__file__).resolve().parents[1]

def eliminate(matrix, rhs):
    a = [list(map(float, row)) + [float(y)] for row, y in zip(matrix, rhs)]
    for col in range(len(a)):
        pivot = max(range(col, len(a)), key=lambda i: abs(a[i][col]))
        if abs(a[pivot][col]) < 1e-12:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        a[col] = [v / divisor for v in a[col]]
        for i in range(len(a)):
            if i != col:
                f = a[i][col]
                a[i] = [v - f * w for v, w in zip(a[i], a[col])]
    return [row[-1] for row in a]

def nodal(ia, ib, r=1., u1=2., u2=2.):
    # Units: mA, kohm and V; unknowns UA, UB, x, y.
    solutions = []
    for ac, bc in itertools.product((False, True), repeat=2):
        matrix = [[1/r, -1/r, 1, 0], [-1/r, 1/r, 0, 1]]
        rhs = [ia, ib]
        matrix.append([1, 0, -r, 0] if ac else [0, 0, 1, 0])
        rhs.append(u1 if ac else 0)
        matrix.append([0, 1, 0, -r] if bc else [0, 0, 0, 1])
        rhs.append(u2 if bc else 0)
        z = eliminate(matrix, rhs)
        if z is None:
            continue
        ua, ub, x, y = z
        da, db = ua-r*x, ub-r*y
        if x < -1e-9 or y < -1e-9 or da > u1+1e-9 or db > u2+1e-9:
            continue
        if abs(x*(u1-da)) > 1e-8 or abs(y*(u2-db)) > 1e-8:
            continue
        solutions.append(z)
    return solutions

def closed(ia, ib, r=1., u1=2., u2=2.):
    s = ia+ib
    assert s > 0
    x = max(0., min(s, (2*ia+ib)/3+(u2-u1)/(3*r)))
    y = s-x
    j = ia-x
    if x == 0:
        ub = u2+r*y
        ua = ub+r*j
    else:
        ua = u1+r*x
        ub = ua-r*j
    return [ua, ub, x, y]

def triangular(reverse):
    # Unknown VA, VB, VC=0 and signed forward diode current j.
    # First branch: VA-VB=6*i1; second branch VA=5*i2.
    candidates = []
    sign = -1 if reverse else 1  # BC orientation +1.
    for on in (False, True):
        matrix = [[1, -1, -6*sign], [1, 0, 5*sign]]
        rhs = [18, 5]
        matrix.append([0, sign, 0] if on else [0, 0, 1])
        rhs.append(2 if on else 0)
        va, vb, j = eliminate(matrix, rhs)
        vd = sign*vb
        if j >= -1e-12 and vd <= 2+1e-12 and abs(j*(2-vd)) < 1e-10:
            candidates.append(dict(va=va, vb=vb, diode_voltage=vd, current_mA=j))
    assert len(candidates) == 1
    return candidates[0]

def main():
    rng = random.Random(3405)
    cases = [(rng.uniform(-8, 8), rng.uniform(-8, 8),
              rng.uniform(.2, 4), rng.uniform(.3, 5), rng.uniform(.3, 5))
             for _ in range(1800)]
    cases += [(a, b, 1., 2., 2.) for a, b in
              [(1, 1), (-1, 3), (3, -1), (-1, 2), (2, -1), (-1, -1),
               (1, -2), (-2, 1), (0, 1), (1, 0)]]
    worst = power_worst = 0.
    feasible = infeasible = 0
    state_counts = {"both_on": 0, "ac_off": 0, "bc_off": 0}
    for ia, ib, r, u1, u2 in cases:
        s = ia+ib
        solved = nodal(ia, ib, r, u1, u2)
        if s < 0:
            assert not solved, (ia, ib, solved)
            infeasible += 1
            continue
        if s == 0:
            continue
        expected = closed(ia, ib, r, u1, u2)
        assert solved
        for actual in solved:
            err = max(abs(a-b) for a, b in zip(actual, expected))
            worst = max(worst, err)
            assert err < 1e-9
            ua, ub, x, y = actual
            j = (ua-ub)/r
            power = ua*ia+ub*ib
            dissipated = r*(j*j+x*x+y*y)+u1*x+u2*y
            perr = abs(power-dissipated)
            power_worst = max(power_worst, perr)
            assert perr < 1e-8 and power > -1e-9
        x, y = expected[2:]
        state = "ac_off" if x == 0 else "bc_off" if y == 0 else "both_on"
        state_counts[state] += 1
        feasible += 1
    # The singular zero-current boundary has a family, not a unique voltage.
    singular = []
    for ia in (-5., -1., 0., 1., 5.):
        r, u0 = 1., 2.
        maximum = min(u0, u0-r*ia)
        values = []
        for eta in (maximum, maximum-1, maximum-10):
            ua, ub = eta+r*ia, eta
            assert ua <= u0+1e-12 and ub <= u0+1e-12
            assert abs((ua-ub)/r-ia) < 1e-12
            values.append([ua, ub])
        singular.append(dict(ia=ia, ib=-ia, distinct_potentials=values))
    # Approach each positive-total-current switching boundary from both sides.
    boundary_error = 0.
    for magnitude in (.01, .3, 2, 7):
        for ia, ib in ((-magnitude, 2*magnitude), (2*magnitude, -magnitude)):
            at = closed(ia, ib)
            for eps in (-1e-8, 1e-8):
                near = closed(ia+eps, ib)
                boundary_error = max(boundary_error, max(abs(a-b) for a,b in zip(near, at)))
    assert boundary_error < 3e-8
    a, b = triangular(False), triangular(True)
    assert abs(a["diode_voltage"]+13) < 1e-10 and abs(a["current_mA"]) < 1e-10
    assert abs(b["diode_voltage"]-2) < 1e-10 and abs(b["current_mA"]-1) < 1e-10
    report = dict(method="四种状态的节点矩阵求解，逐一检验元件不等式；另查能量和状态连续性",
                  random_and_named_cases=len(cases), positive_total_cases=feasible,
                  impossible_negative_total_cases=infeasible, state_counts=state_counts,
                  max_closed_form_error=worst, max_power_error_mW=power_worst,
                  boundary_continuity_error=boundary_error,
                  part1=a, part2=b, zero_total_families=singular, status="pass")
    (ROOT/"build").mkdir(exist_ok=True)
    (ROOT/"build/question05-verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
if __name__ == "__main__":
    main()

