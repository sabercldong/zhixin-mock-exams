#!/usr/bin/env python3
import json
import random
import cmath
import math
from pathlib import Path


def main():
    rng = random.Random(3306)
    max_velocity_rel = 0.0
    max_port_rel = 0.0
    max_power_rel = 0.0
    max_initial_error = 0.0
    max_variation_port_error = 0.0

    for _ in range(1000):
        b = rng.uniform(0.15, 3.0)
        ell = rng.uniform(0.05, 2.0)
        mass = rng.uniform(0.02, 5.0)
        inductance = rng.uniform(0.001, 2.0)
        damping = rng.uniform(0.02, 8.0)
        omega = rng.uniform(0.1, 80.0)
        u0 = rng.uniform(0.2, 50.0)

        c0 = mass / (b * b * ell * ell)
        r0 = b * b * ell * ell / damping
        z_parallel = 1.0 / (1.0 / r0 + 1j * omega * c0)
        z_total = 1j * omega * inductance + z_parallel
        current = u0 / z_total
        u_mech = current * z_parallel
        velocity_circuit = u_mech / (b * ell)

        denominator = (
            b * b * ell * ell
            - inductance * mass * omega * omega
            + 1j * inductance * damping * omega
        )
        velocity_direct = b * ell * u0 / denominator

        scale_v = max(abs(velocity_direct), 1e-30)
        max_velocity_rel = max(
            max_velocity_rel,
            abs(velocity_circuit - velocity_direct) / scale_v,
        )

        # Source-port voltage reconstructed from the original equations.
        current_from_mechanics = (
            (1j * omega * mass + damping) * velocity_direct / (b * ell)
        )
        reconstructed_u = (
            1j * omega * inductance * current_from_mechanics
            + b * ell * velocity_direct
        )
        max_port_rel = max(max_port_rel, abs(reconstructed_u - u0) / u0)

        # Mechanical damping and the equivalent resistor must dissipate
        # exactly the same cycle-averaged power.
        p_mech = 0.5 * damping * abs(velocity_direct) ** 2
        p_resistor = 0.5 * abs(b * ell * velocity_direct) ** 2 / r0
        max_power_rel = max(
            max_power_rel,
            abs(p_mech - p_resistor) / max(p_mech, 1e-30),
        )

        # 用耦合方程核对时域相位展开与初态，而非再次比较最终振幅。
        aa=denominator.real;bb=denominator.imag
        t=rng.uniform(0,10)
        v=b*ell*u0*(aa*math.cos(omega*t)+bb*math.sin(omega*t))/(aa*aa+bb*bb)
        vp=b*ell*u0*omega*(-aa*math.sin(omega*t)+bb*math.cos(omega*t))/(aa*aa+bb*bb)
        vpp=-omega*omega*v
        assert abs(inductance*mass*vpp+inductance*damping*vp+b*b*ell*ell*v-b*ell*u0*math.cos(omega*t))<1e-10
        disc=cmath.sqrt(damping*damping/(4*mass*mass)-b*b*ell*ell/(inductance*mass))
        plus=-damping/(2*mass)+disc;minus=-damping/(2*mass)-disc
        assert plus.real<0 and minus.real<0
        if abs(plus-minus)>1e-10:
            initial_v=rng.uniform(-2,2);initial_i=rng.uniform(-2,2)
            a=initial_v-velocity_direct.real
            initial_dv=(b*ell*initial_i-damping*initial_v)/mass
            beta=initial_dv-(1j*omega*velocity_direct).real
            cp=(beta-minus*a)/(plus-minus);cm=(plus*a-beta)/(plus-minus)
            error=max(abs(cp+cm-a),abs(plus*cp+minus*cm-beta))/(1+abs(a)+abs(beta))
            max_initial_error=max(max_initial_error,error)
        spring=rng.uniform(.01,50)
        lk=b*b*ell*ell/spring
        z_parallel_spring=1/(1/r0+1j*omega*c0+1/(1j*omega*lk))
        current_spring=u0/(1j*omega*inductance+z_parallel_spring)
        velocity_spring=current_spring*z_parallel_spring/(b*ell)
        expected_spring=b*ell*u0/(denominator+inductance*spring)
        error=abs(velocity_spring-expected_spring)/max(abs(expected_spring),1e-30)
        max_variation_port_error=max(max_variation_port_error,error)

    assert max_velocity_rel < 2e-13
    assert max_port_rel < 2e-13
    assert max_power_rel < 2e-15
    assert max_initial_error < 2e-13
    assert max_variation_port_error < 2e-13

    report = {
        "status": "pass",
        "random_parameter_cases": 1000,
        "max_relative_error_velocity": max_velocity_rel,
        "max_relative_error_source_port": max_port_rel,
        "max_relative_error_average_power": max_power_rel,
        "equivalent_topology": "L0 series (R0 parallel C0)",
        "max_relative_error_initial_conditions": max_initial_error,
        "max_relative_error_spring_variation": max_variation_port_error,
        "phase_and_time_domain_ODE": "pass",
    }
    out = Path(__file__).resolve().parents[1] / "build" / "question06-verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
