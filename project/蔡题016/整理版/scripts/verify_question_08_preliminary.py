"""Q8: independently test definitions and transverse forces; not acceptance.

Natural units c=1 are used for Lorentz tests. No gravity prescription is
chosen. Two explicitly different weak-metric examples prove non-uniqueness.
"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    b, e, p, rho = sp.symbols('beta epsilon pressure rho', real=True)
    gamma = 1 / sp.sqrt(1 - b**2)
    boost = sp.Matrix([[gamma, -gamma*b, 0, 0],
                       [-gamma*b, gamma, 0, 0],
                       [0, 0, 1, 0], [0, 0, 0, 1]])
    eta = sp.diag(-1, 1, 1, 1)
    assert all(sp.simplify(value) == 0 for value in boost.T*eta*boost-eta)
    current = boost*sp.Matrix([rho, 0, 0, 0])
    stress = sp.simplify(boost*sp.diag(e, p, p, p)*boost.T)
    assert sp.simplify(current[0]-gamma*rho) == 0
    assert sp.simplify(stress[0, 0]-(gamma**2*(e+p)-p)) == 0
    assert sp.simplify(stress[3, 3]-p) == 0

    # Transform actual four-momentum derivatives, not a memorized force rule.
    F = sp.symbols('F', real=True)
    U = sp.Matrix([gamma, gamma*b, 0, 0])
    four_force = sp.Matrix([0, 0, 0, gamma*F])
    boat_U = sp.simplify(boost*U)
    boat_four_force = sp.simplify(boost*four_force)
    assert boat_U == sp.Matrix([1, 0, 0, 0])
    assert sp.simplify(U.dot(eta*four_force)) == 0
    assert sp.simplify(boat_four_force[3]/boat_U[0]-gamma*F) == 0

    # Derive Christoffel symbols from two metric families at z=0.
    # These are explicit alternative assumptions, NOT a selected gravity law.
    t, x, y, z, g, kappa = sp.symbols('t x y z g kappa', real=True)
    coords = [t, x, y, z]
    metric = sp.diag(-1-2*g*z, 1-2*kappa*g*z,
                     1-2*kappa*g*z, 1-2*kappa*g*z)
    inv = metric.inv()
    def christoffel(a, mu, nu):
        return sp.simplify(sum(inv[a, s]*(sp.diff(metric[s, nu], coords[mu])
                              +sp.diff(metric[s, mu], coords[nu])
                              -sp.diff(metric[mu, nu], coords[s]))/2
                              for s in range(4)).subs(z, 0))
    C00 = christoffel(3, 0, 0)
    C11 = christoffel(3, 1, 1)
    C01 = christoffel(3, 0, 1)
    assert sp.simplify(C00-g) == 0 and sp.simplify(C11-kappa*g) == 0
    assert C01 == 0
    # dp_z/dt = (m/gamma) dU_z/dtau at the chosen local origin.
    weight_per_mass = sp.simplify((C00*gamma**2+C11*gamma**2*b**2)/gamma)
    assert sp.simplify(weight_per_mass-gamma*g*(1+kappa*b**2)) == 0

    cases = []
    impulse_cases = []
    for beta in [0., .1, .4, .7, .9, .99]:
        gam = 1/math.sqrt(1-beta*beta)
        L = np.array([[gam, -gam*beta, 0, 0],
                      [-gam*beta, gam, 0, 0],
                      [0, 0, 1, 0], [0, 0, 0, 1]])
        # Two independent spacetime events on the moving front/back surfaces,
        # simultaneous in the boat frame, recover the proper length.
        l0 = 2.3
        front_water = np.array([beta*gam*l0, gam*l0, 0, 0])
        front_boat = L@front_water
        assert abs(front_boat[0]) < 2e-13
        assert abs(front_boat[1]-l0) < 2e-13
        length_water = l0/gam
        h, width, K, p_top = .7, .8, 9.3, 18.
        A0 = l0*width
        V0 = A0*h
        A1 = length_water*width
        # Independently integrate top/bottom pressure traction over both
        # coordinate surface areas; do not assume rho_2*g for moving water.
        lower = p_top+K*h
        F1 = quad(lambda s: (lower-p_top)*width, 0, length_water)[0]
        F2 = quad(lambda s: (lower-p_top)*width, 0, l0)[0]
        assert abs(F1-K*V0/gam) < 2e-13
        assert abs(F2-gam*F1) < 2e-13
        water_density = 1.7  # deliberately unequal to boat density
        rest_mass_current = L@np.array([water_density, 0, 0, 0])
        for pressure_fraction in [0., .03, .4]:
            water_pressure = pressure_fraction*water_density
            transformed = L@np.diag([water_density, water_pressure,
                                     water_pressure, water_pressure])@L.T
            expected = gam*gam*water_density+(gam*gam-1)*water_pressure
            assert abs(transformed[0, 0]-expected) < 4e-12
            assert abs(transformed[3, 3]-water_pressure) < 2e-14
            cases.append(dict(beta=beta, gamma=gam, V0=V0,
                V1=V0/gam, force_water=F1, force_boat=F2,
                original_given_pressure_gradient=K,
                rest_mass_density_moving_water=rest_mass_current[0],
                pressure_fraction=pressure_fraction,
                energy_density_moving_water=transformed[0, 0],
                normal_stress_in_boat_frame=transformed[3, 3]))

        # Apply a real transverse momentum impulse. Integrate dx/dt from the
        # mass-shell energy and transform its two events, then divide dp'_z
        # by the transformed elapsed time. This recovers gamma*F, not F/gamma.
        actual_F = .6
        px = gam*beta
        E0 = gam
        for dt in [1e-3, 1e-4, 1e-5]:
            dx = quad(lambda tau: px/math.sqrt(E0*E0+(actual_F*tau)**2),
                      0, dt, epsabs=1e-16)[0]
            transformed_interval = L@np.array([dt, dx, 0, 0])
            measured_force = actual_F*dt/transformed_interval[0]
            rel_error = abs(measured_force/(gam*actual_F)-1)
            assert rel_error < 2e-7
            impulse_cases.append(dict(beta=beta, dt=dt,
                measured_force_boat=measured_force,
                expected_instantaneous_force=gam*actual_F,
                relative_error=rel_error))

    from sympy.physics.units import kilogram, meter, second, newton, pascal
    from sympy.physics.units import convert_to
    K_units = kilogram/meter**3 * meter/second**2
    assert sp.simplify(convert_to(K_units*meter**3, newton)/newton-1) == 0
    assert sp.simplify(convert_to(K_units*meter, pascal)/pascal-1) == 0
    result = dict(question=8, stage='preliminary-model-and-source-verification',
        verified_relativistic_kinematics=True, document_complete=False,
        model_condition_resolved=False, question_accepted=False, set_accepted=False,
        gravity_prescription_selected=False,
        direct_surface_traction_and_fluid_tensor_cases=cases,
        actual_transverse_impulse_cases=impulse_cases,
        maximum_impulse_relative_error=max(case['relative_error'] for case in impulse_cases),
        unambiguous_results=dict(volume='V0/gamma',
            boat_rest_mass_density='gamma*rho0',
            water_rest_mass_density_in_boat_frame='gamma*rho',
            water_energy_density_in_boat_frame='gamma^2*rho+(gamma^2-1)*p/c^2',
            original_pressure_force_water='rho0*g*V0/gamma',
            original_pressure_force_boat='rho0*g*V0',
            transverse_force_transform='F_boat=gamma*F_water'),
        illustrative_gravity_metrics=dict(kappa0='G1=gamma*m0*g',
            kappa1='G1=gamma*(1+beta^2)*m0*g',
            derived_from='Christoffel symbols of explicitly different weak static metrics'),
        unresolved=['density convention and cold-matter approximation',
                    'whether rho equals rho0',
                    'gravity prescription needed to determine G1(v)'],
        confirmed_handwritten_error='F2=F1/gamma is inconsistent with transverse four-force and direct stress integration',
        original_hashes={name:sha(ROOT.parent/name) for name in ['试卷.pdf', '答案.pdf']},
        source_detail_hashes={name:sha(ROOT/'preview/originals'/name)
                             for name in ['q08-paper-detail.png', 'q08-hand-detail.png']},
        verification_script_sha256=sha(Path(__file__)))
    target = ROOT/'build/verification-q08-preliminary.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(saved=str(target), model_condition_resolved=False,
        tensor_cases=len(cases), impulse_cases=len(impulse_cases),
        maximum_impulse_relative_error=result['maximum_impulse_relative_error']),
        ensure_ascii=False))


if __name__ == '__main__':
    main()
