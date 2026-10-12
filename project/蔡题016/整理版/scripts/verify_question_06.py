"""Q6: actual ordered-body collision events, not merely final-formula substitution.

Slow/fast speed carriers pass through B-C collisions. Physical B never crosses C.
The handwritten 4:3 counts carrier crossings (=B-C), not A-B end collisions.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def collide(u, v, a, b):
    return ((a-b)*u+2*b*v)/(a+b), (2*a*u+(b-a)*v)/(a+b)

def events(mu, bpos=-.637, cpos=-.219, final_distance=2., snapshot=False, kfast=2.):
    # l=v0=m=1; positive direction points to the wall at z=0.
    z = np.array([-1., bpos, cpos], dtype=float)
    v = np.array([0., 1., kfast], dtype=float)
    masses = np.array([mu, 1., 1.])
    labels = [None, 's', 'f']
    counts = {'AB': 0, 'BC': 0, 'Cwall': 0}
    carrier = {k: {'A': 0, 'wall': 0} for k in ['s', 'f']}
    E0 = .5*np.dot(masses, v*v)
    t = 0.
    max_energy_error = 0.
    history = []
    for number in range(1000000):
        candidates = [
            ((z[1]-z[0])/(v[0]-v[1]) if v[0]>v[1] else math.inf, 'AB'),
            ((z[2]-z[1])/(v[1]-v[2]) if v[1]>v[2] else math.inf, 'BC'),
            (-z[2]/v[2] if v[2]>0 else math.inf, 'Cwall'),
        ]
        dt, kind = min(candidates)
        finish = ((-final_distance-z[0])/v[0] if v[0]<0 else math.inf)
        if finish <= dt:
            z += finish*v
            t += finish
            break
        assert dt >= -1e-10, (z, v, dt)
        if sum(abs(q-dt)<1e-10 for q, _ in candidates)>1:
            raise ValueError('Simultaneous collision: select generic initial phases')
        z += dt*v
        t += dt
        before = v.copy()
        counts[kind] += 1
        if kind == 'AB':
            carrier[labels[1]]['A'] += 1
            v[0], v[1] = collide(v[0], v[1], mu, 1.)
            assert v[1] > 0., 'Mass ratio too small for stated endpoint alternation'
        elif kind == 'BC':
            v[1], v[2] = collide(v[1], v[2], 1., 1.)
            labels[1], labels[2] = labels[2], labels[1]
        else:
            carrier[labels[2]]['wall'] += 1
            v[2] = -v[2]
        err = abs(.5*np.dot(masses, v*v)/E0-1.)
        max_energy_error = max(max_energy_error, err)
        if snapshot and number < 18:
            history.append(dict(t=t, kind=kind, positions=z.tolist(),
                                before=before.tolist(), after=v.tolist(),
                                carrier_on_B=labels[1], carrier_on_C=labels[2]))
        assert z[0] <= z[1]+1e-10 and z[1] <= z[2]+1e-10 and z[2] <= 1e-10
    else:
        raise RuntimeError('Collision loop exceeded limit')
    expected = (1.+kfast)/2*math.sqrt(mu/(1.+kfast*kfast))*math.acos(1./final_distance)
    approx_speed = math.sqrt((1.+kfast*kfast)/mu*(1.-final_distance**-2))
    assert max_energy_error < 2e-10
    assert 0 <= counts['Cwall']-counts['AB'] <= 2
    assert all(0 <= data['wall']-data['A'] <= 1 for data in carrier.values())
    return dict(M_over_m=mu, initial_B=bpos, initial_C=cpos,
                fast_initial_speed=kfast, final_distance=final_distance,
                counts=counts, speed_carrier_counts=carrier,
                final_A_speed=-v[0], leading_A_speed=approx_speed,
                speed_ratio=-v[0]/approx_speed, leading_endpoint_count=expected,
                wall_count_ratio=counts['Cwall']/expected,
                AB_count_ratio=counts['AB']/expected,
                BC_count_ratio=counts['BC']/expected,
                elapsed_time=t, averaged_time=math.sqrt(mu/(1.+kfast*kfast))*math.sqrt(final_distance**2-1.),
                energy_relative_error=max_energy_error,
                history=history)

def folded_crossings(alpha, beta):
    # y_s=f(s+alpha), y_f=f(2s+beta), 0<s<2. Generic phases avoid endpoints.
    roots = []
    for k in range(-8, 9):
        for value, kind in [(alpha-beta+2*k, 'same-direction'),
                            ((2*k-alpha-beta)/3., 'opposite-direction')]:
            if 1e-10 < value < 2.-1e-10:
                roots.append((value, kind))
    roots.sort()
    assert len(roots)==4 and len({round(t, 9) for t,_ in roots})==4
    def fold(s):
        return 1.-abs(1.-s%2.)
    assert max(abs(fold(t+alpha)-fold(2*t+beta)) for t,_ in roots)<2e-14
    return [dict(s=t, y=fold(t+alpha), kind=kind) for t,kind in roots]

def main():
    p = argparse.ArgumentParser(); p.add_argument('--complete', action='store_true')
    args = p.parse_args()
    m, M, x, l, v0, t = sp.symbols('m M x l v0 t', positive=True)
    u, v = sp.symbols('u v', real=True)
    a, b = sp.symbols('a b', positive=True)
    up = ((a-b)*u+2*b*v)/(a+b)
    vp = (2*a*u+(b-a)*v)/(a+b)
    assert sp.simplify(a*up+b*vp-a*u-b*v)==0
    assert sp.simplify(a*up**2+b*vp**2-a*u**2-b*v**2)==0
    assert sp.simplify(up.subs(a,b)-v)==0
    assert sp.simplify(vp.subs(a,b)-u)==0
    F = 5*m*v0**2*l**2/x**3
    V = sp.sqrt(5*m/M)*v0*sp.sqrt(x*x-l*l)/x
    E = M*V**2/2+5*m*v0**2*l*l/(2*x*x)
    assert sp.simplify(E-5*m*v0**2/2)==0
    assert sp.simplify(M*V*sp.diff(V,x)-F)==0
    xt = l*sp.sqrt(1+5*m*v0**2*t*t/(M*l*l))
    assert sp.simplify(M*sp.diff(xt,t,2)-F.subs(x,xt))==0
    theta = sp.symbols('theta', positive=True)
    kernel = l/(x*sp.sqrt(x*x-l*l))
    transformed = sp.simplify(kernel.subs(x,l/sp.cos(theta))*
                              sp.diff(l/sp.cos(theta),theta))
    # 0<theta<=pi/3 implies tan(theta)>0; positivity is not automatic in SymPy.
    assert sp.simplify(sp.refine(transformed, sp.Q.positive(sp.tan(theta)))-1)==0
    invariant_ODE = []
    for ratio in [1e3, 1e4, 1e6]:
        # Integrate F/m from impulse-frequency averaging; do not insert x(t).
        tf = math.sqrt(3.*ratio/5.)
        def ode(time, y):
            distance, speed, slow, fast, ns, nf = y
            return [speed, (slow*slow+fast*fast)/(ratio*distance),
                    -slow*speed/distance, -fast*speed/distance,
                    slow/(2*distance), fast/(2*distance)]
        sol = solve_ivp(ode,[0,tf],[1.,0.,1.,2.,0.,0.],rtol=2e-11,atol=1e-12)
        assert sol.success
        distance, speed, slow, fast, ns, nf = sol.y[:,-1]
        assert abs(distance-2.)<2e-10
        assert abs(slow*distance-1.)<2e-10 and abs(fast*distance-2.)<4e-10
        assert abs(ns-math.pi/6*math.sqrt(ratio/5.))<2e-7
        invariant_ODE.append(dict(M_over_m=ratio, distance=distance, speed=speed,
                                  slow=slow, fast=fast, n_s=ns, n_f=nf))
    numerical_events = []
    for mu in [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
        for bp, cp in [(-.637,-.219),(-.811,-.337),(-.473,-.123)]:
            row = events(mu,bp,cp,snapshot=(mu==1e3 and bp==-.637))
            assert abs(row['speed_ratio']-1)<3./math.sqrt(mu)
            assert abs(row['counts']['Cwall']-row['leading_endpoint_count'])<4.
            assert abs(row['counts']['AB']-row['leading_endpoint_count'])<4.
            assert abs(row['counts']['BC']-4./3*row['leading_endpoint_count'])<8.
            numerical_events.append(row)
    general_events = []
    for kv in [1.5, 3.]:
        for final in [1.5, 2., 3.]:
            for ratio in [1e4, 1e6]:
                row = events(ratio, final_distance=final, kfast=kv)
                assert abs(row['speed_ratio']-1)<5./math.sqrt(ratio)
                assert abs(row['counts']['Cwall']-row['leading_endpoint_count'])<6.
                assert abs(row['counts']['AB']-row['leading_endpoint_count'])<6.
                general_events.append(row)
    # General k formula from energy and frequency, independently integrated above.
    k = sp.symbols('k', positive=True)
    S = 1+k*k
    general_V = sp.sqrt(S*m/M)*v0*sp.sqrt(1-l*l/x/x)
    assert sp.simplify(M*general_V**2/2+m*S*v0*v0*l*l/(2*x*x)-m*S*v0*v0/2)==0
    variant2 = dict(M=100.,m=.01,v0=2.,l=.5,k=3.)
    variant2['V_final'] = 2.*math.sqrt(.75*.001)
    variant2['time'] = .25*math.sqrt(300./.1)
    variant2['endpoint_count'] = 4.*math.pi/6*math.sqrt(100./.1)
    variant2['initial_energy'] = .5*.01*10*4
    variant2['A_final_energy'] = .5*100.*variant2['V_final']**2
    variant2['light_final_energy'] = .5*.01*(1.+3.**2)
    assert abs(variant2['initial_energy']-variant2['A_final_energy']-variant2['light_final_energy'])<1e-14
    numeric_variant = events(1e4, kfast=3.)
    assert abs(numeric_variant['final_A_speed']*2/variant2['V_final']-1)<.025
    ratio_inverse = 15/(4*.02**2)
    assert ratio_inverse==9375.
    inverse_count = math.pi/2*math.sqrt(ratio_inverse/5)
    assert abs(inverse_count-25*math.sqrt(3)*math.pi/2)<1e-12
    # Independent integral evaluation removes the integrable starting singularity.
    quadrature = quad(lambda angle: .5*math.sqrt(1e4/5.),0,math.pi/3)[0]
    assert abs(quadrature-math.pi/6*math.sqrt(1e4/5.))<1e-12
    from sympy.physics.units import meter, second, kilogram, newton
    from sympy.physics.units import convert_to
    assert sp.simplify(convert_to((kilogram*(meter/second)**2/meter),newton)-newton)==0
    sources = {'scripts/verify_question_06.py':sha(Path(__file__))}
    figures = {}
    if args.complete:
        source = ROOT/'drafts/question-06.md'
        text = source.read_text()
        assert '<!-- question-complete -->' in text and text.count('\n## ')==9
        sources['drafts/question-06.md'] = sha(source)
        sources['figures/题06_图稿源文件.tex'] = sha(ROOT/'figures/题06_图稿源文件.tex')
        import subprocess
        subprocess.run(['python3',str(ROOT/'scripts/check_projected_question_06.py')],check=True)
        geometry = ROOT/'build/projected-geometry-q06.json'
        assert json.loads(geometry.read_text())['passed']
        sources['scripts/check_projected_question_06.py'] = sha(ROOT/'scripts/check_projected_question_06.py')
        sources['build/projected-geometry-q06.json'] = sha(geometry)
        for name in ['question-06','exchange-06','impulse-06','energy-06','count-06','crossings-06']:
            figures[name] = sha(ROOT/f'figures/{name}.pdf')
    result = dict(question=6, verified_math=True, document_complete=args.complete,
        model_condition_resolved=True, set_accepted=False,
        approximation='leading order as m/M tends to zero; O(1) counts depend on initial phases',
        original_handwritten_error='part (3) 4:3 ratio counts B-C carrier crossings, not A-B endpoint events',
        corrected_leading_answers=dict(A_speed='sqrt(15*m/(4*M))*v0, away from wall',
            C_wall='pi/2*sqrt(M/(5*m))', A_B='pi/2*sqrt(M/(5*m))'),
        exact_collision_simulations=numerical_events,
        general_speed_ratio_and_terminal_distance_events=general_events,
        impulse_averaged_independent_ODE=invariant_ODE,
        folded_carrier_crossings=folded_crossings(.173,.617),
        solved_variants=dict(general_numeric=variant2, general_numeric_exact_events=numeric_variant,
                            inverse_mass_ratio=ratio_inverse, inverse_endpoint_count=inverse_count,
                            inverse_fractional_spacing_change=.08,
                            one_percent_spacing_required_mass_ratio=60/.01**2),
        source_sha256=sources, figures_sha256=figures,
        originals_sha256={n:sha(ROOT.parent/n) for n in ['试卷.pdf','答案.pdf']})
    dest = ROOT/('build/verification-q06.json' if args.complete else 'build/verification-q06-preliminary.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=6,verified_math=True,document_complete=args.complete,
        exact_event_cases=len(numerical_events), last_event_case=numerical_events[-1],
        folded_crossings=result['folded_carrier_crossings']),ensure_ascii=False))

if __name__ == '__main__':
    main()
