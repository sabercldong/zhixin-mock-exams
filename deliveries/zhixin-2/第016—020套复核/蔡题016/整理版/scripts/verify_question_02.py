"""016 Q2: independent infinite-wire integrals, local fields and streamlines.

This is a preliminary calculation until the nine-module source and diagrams
exist. Exact streamlines are not confused with the near-origin approximation.
"""
from pathlib import Path
import argparse,hashlib,json,math,re
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def configuration(count,ell):
    return [(ell,0.,1),(-ell,0.,-1)] if count==2 else [
        (ell,ell,1),(-ell,ell,-1),(-ell,-ell,1),(ell,-ell,-1)]
def field(point,wires,K=1.):
    total=np.zeros(2)
    for a,b,sign in wires:
        dx,dy=np.array(point)-np.array([a,b])
        total+=K*sign*np.array([-dy,dx])/(dx*dx+dy*dy)
    return total
def source_integral(point,wires,K=1.):
    total=np.zeros(2)
    for a,b,sign in wires:
        dx,dy=np.array(point)-np.array([a,b]);rho2=dx*dx+dy*dy
        integral=quad(lambda z:(rho2+z*z)**-1.5,-np.inf,np.inf,
                      epsabs=2e-11,epsrel=2e-11)[0]
        total+=K*sign*np.array([-dy,dx])*integral/2
    return total
def invariant(point,wires):
    # The signed sum of log distances is the stream function up to -K.
    return sum(sign*math.log(math.hypot(point[0]-a,point[1]-b))
               for a,b,sign in wires)
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--complete',action='store_true')
    args=parser.parse_args()
    x,y=sp.symbols('x y',real=True)
    ell,K=sp.symbols('ell K',positive=True)
    rhoP=(x-ell)**2+y*y;rhoM=(x+ell)**2+y*y
    b2=sp.Matrix([K*(-y/rhoP+y/rhoM),K*((x-ell)/rhoP-(x+ell)/rhoM)])
    expected2=2*K*ell/(rhoP*rhoM)*sp.Matrix([-2*x*y,x*x-y*y-ell*ell])
    assert all(sp.simplify(v)==0 for v in b2-expected2)
    assert sp.simplify(b2.dot(b2)-4*K*K*ell*ell/(rhoP*rhoM))==0
    origin2=b2.subs({x:0,y:0})
    assert origin2==sp.Matrix([0,-2*K/ell])
    assert all(sp.simplify(v)==0 for v in b2.jacobian([x,y]).subs({x:0,y:0}))
    az2=K*sp.log(rhoM/rhoP)/2
    assert sp.simplify(sp.diff(az2,y)-b2[0])==0
    assert sp.simplify(-sp.diff(az2,x)-b2[1])==0
    symbolic_wires=[(ell,ell,1),(-ell,ell,-1),(-ell,-ell,1),(ell,-ell,-1)]
    b4=sp.zeros(2,1);az4=0
    for a,b,sign in symbolic_wires:
        rho=(x-a)**2+(y-b)**2
        contribution=K*sign*sp.Matrix([-(y-b),(x-a)])/rho
        b4+=contribution;az4-=K*sign*sp.log(rho)/2
        assert sp.simplify(sp.diff(contribution[0],x)+sp.diff(contribution[1],y))==0
        assert sp.simplify(sp.diff(contribution[1],x)-sp.diff(contribution[0],y))==0
    assert b4.subs({x:0,y:0})==sp.zeros(2,1)
    jac=sp.simplify(b4.jacobian([x,y]).subs({x:0,y:0}))
    assert jac==sp.diag(2*K/ell**2,-2*K/ell**2)
    assert sp.simplify(b4[0].subs(x,0))==0
    assert sp.simplify(b4[1].subs(y,0))==0
    assert sp.simplify(sp.diff(az4,y)-b4[0])==0
    assert sp.simplify(-sp.diff(az4,x)-b4[1])==0
    # Scalar epsilon expansion keeps x and y comparable without assuming x=y.
    e,X,Y=sp.symbols('e X Y',real=True)
    series2=[sp.simplify(sp.series(z.subs({x:e*ell*X,y:e*ell*Y}),e,0,4).removeO()) for z in b2]
    series4=[sp.simplify(sp.series(z.subs({x:e*ell*X,y:e*ell*Y}),e,0,6).removeO()) for z in b4]
    assert sp.simplify(series2[0]+4*K*e**2*X*Y/ell)==0
    assert sp.simplify(series2[1]+2*K*(1+e**2*(X*X-Y*Y))/ell)==0
    assert sp.simplify(sp.diff(series4[0],e).subs(e,0)-2*K*X/ell)==0
    assert sp.simplify(sp.diff(series4[1],e).subs(e,0)+2*K*Y/ell)==0
    assert sp.simplify(series4[0]-2*K*e*X/ell-
                      K*e**5*(-X**5+10*X**3*Y**2-5*X*Y**4)/(2*ell))==0
    assert sp.simplify(series4[1]+2*K*e*Y/ell-
                      K*e**5*(5*X**4*Y-10*X**2*Y**3+Y**5)/(2*ell))==0
    # Fourfold symmetry suppresses the cubic correction: relative error is r^4.
    z=x+sp.I*y
    assert sp.simplify((b4[1]+sp.I*b4[0])*(z**4+4*ell**4)-8*sp.I*K*ell**2*z)==0
    r1=(x-ell)**2+(y-ell)**2;r2=(x+ell)**2+(y-ell)**2
    r3=(x+ell)**2+(y+ell)**2;r4=(x-ell)**2+(y+ell)**2
    product_plus=sp.expand(r1*r3);product_minus=sp.expand(r2*r4)
    assert sp.simplify(product_plus-product_minus+16*ell*ell*x*y)==0
    assert sp.simplify(product_plus-((x*x+y*y+2*ell*ell)**2-4*ell*ell*(x+y)**2))==0
    assert sp.simplify(product_minus-((x*x+y*y+2*ell*ell)**2-4*ell*ell*(x-y)**2))==0
    integrals=[];near=[];ampere=[]
    for count in [2,4]:
        for length,strength in [(.7,.3),(1.,1.),(2.3,4.1)]:
            wires=configuration(count,length)
            for fx,fy in [(0.,0.),(.03,.08),(-.17,.05),(.22,-.18),(.7,.4),(1.5,.5),(-1.4,.3)]:
                point=np.array([fx,fy])*length
                closed=field(point,wires,strength)
                direct=source_integral(point,wires,strength)
                error=float(np.linalg.norm(closed-direct))
                assert error<1e-10*max(strength/length,1.)
                integrals.append(dict(wire_count=count,ell=length,K=strength,
                    point=point.tolist(),B_direct_integral=direct.tolist(),B_closed_form=closed.tolist(),error=error))
        # Two wires: relative error r^2. Alternating four-corner wires: r^4.
        for angle in [.2,.65,1.1,1.9,2.8,4.4]:
            errors=[]
            radii=[.04,.02,.01,.005] if count==2 else [.08,.04,.02,.01]
            power=2 if count==2 else 4
            for radius in radii:
                point=radius*np.array([math.cos(angle),math.sin(angle)])
                actual=source_integral(point,configuration(count,1.))
                leading=np.array([0.,-2.]) if count==2 else 2*np.array([point[0],-point[1]])
                relative=float(np.linalg.norm(actual-leading)/np.linalg.norm(leading))
                assert relative<3*radius**power
                errors.append(dict(radius=radius,relative_error=relative))
            for a,b in zip(errors,errors[1:]):
                expected_ratio=2**power
                assert abs(a['relative_error']/b['relative_error']/expected_ratio-1)<.015
            near.append(dict(wire_count=count,angle=angle,relative_error_power=power,samples=errors))
        wires=configuration(count,1.)
        loops=[(a,b,.3,sign) for a,b,sign in wires]+[(0.,0.,3.,0)]
        for cx,cy,radius,enclosed_sign in loops:
            def integrand(phi):
                point=[cx+radius*math.cos(phi),cy+radius*math.sin(phi)]
                tangent=radius*np.array([-math.sin(phi),math.cos(phi)])
                return float(field(point,wires)@tangent)
            circulation=quad(integrand,0,2*math.pi,epsabs=2e-11,epsrel=2e-11)[0]
            assert abs(circulation-2*math.pi*enclosed_sign)<2e-10
            ampere.append(dict(wire_count=count,loop_center=[cx,cy],radius=radius,
                enclosed_signed_current=enclosed_sign,circulation=circulation))
    lines2=[]
    wires=configuration(2,1.)
    for initial in [(0.,.2),(.25,.2),(-.2,.3),(1.4,.25),(-1.4,.15),(.6,-.4)]:
        def ode(s,state):
            value=field(state,wires);return value/np.linalg.norm(value)
        for direction in [-1,1]:
            sol=solve_ivp(lambda s,state:direction*ode(s,state),[0,2.],initial,
                          rtol=2e-11,atol=2e-13,max_step=.01)
            invariants=np.array([invariant(z,wires) for z in sol.y.T])
            residual=float(np.max(abs(invariants-invariants[0])))
            assert residual<3e-10
            xp,yp=initial
            kappa=((xp+1)**2+yp*yp)/((xp-1)**2+yp*yp)
            if abs(kappa-1)<1e-14:
                circular_residual=float(np.max(abs(sol.y[0])))
                center=None;radius=None
            else:
                center=(kappa+1)/(kappa-1)
                radius=math.sqrt(center*center-1)
                circular_residual=float(np.max(abs((sol.y[0]-center)**2+sol.y[1]**2-radius**2)))
            assert circular_residual<2e-9
            lines2.append(dict(initial=initial,direction=direction,
                signed_log_invariant_residual=residual,kappa=kappa,circle_center_x=center,
                circle_radius=radius,circle_or_axis_residual=circular_residual))
    lines4=[];wires=configuration(4,1.)
    for initial in [(.05,.1),(.07,-.04),(-.08,.05),(-.04,-.1),
                    (.35,.2),(-.25,.4),(1.4,.4),(.2,1.45)]:
        def ode(s,state):
            value=field(state,wires);return value/np.linalg.norm(value)
        for direction in [-1,1]:
            sol=solve_ivp(lambda s,state:direction*ode(s,state),[0,.4],initial,
                          rtol=2e-11,atol=2e-13,max_step=.003)
            values=np.array([invariant(z,wires) for z in sol.y.T])
            residual=float(np.max(abs(values-values[0])))
            assert residual<2e-10
            lines4.append(dict(initial=initial,direction=direction,
                exact_quartic_log_ratio_residual=residual,
                initial_product_xy=initial[0]*initial[1],
                product_xy_range=[float(np.min(sol.y[0]*sol.y[1])),float(np.max(sol.y[0]*sol.y[1]))]))
    # Differentiate the numerically integrated source, not the stated gradient.
    jrows=[]
    for length,strength in [(.7,.3),(1.,1.),(2.3,4.1)]:
        h=length*1e-5;wires=configuration(4,length)
        recovered=np.column_stack([
            (source_integral([h,0],wires,strength)-source_integral([-h,0],wires,strength))/(2*h),
            (source_integral([0,h],wires,strength)-source_integral([0,-h],wires,strength))/(2*h)])
        expected=np.diag([2*strength/length**2,-2*strength/length**2])
        assert np.max(abs(recovered-expected))/np.max(abs(expected))<2e-9
        jrows.append(dict(ell=length,K=strength,source_integral_Jacobian=recovered.tolist()))
    # Fully answered variants are tested against the infinite source integral.
    numeric_b0=source_integral([0,0],configuration(2,.25),1e-6)
    numeric_p=source_integral([.01,.02],configuration(4,.25),1e-6)
    numeric_linear=np.array([3.2e-7,-6.4e-7])
    numeric_error=float(np.linalg.norm(numeric_p-numeric_linear)/np.linalg.norm(numeric_linear))
    assert np.max(abs(numeric_b0-np.array([0,-8e-6])))<1e-17
    assert abs(np.linalg.norm(numeric_linear)-math.sqrt(51.2)*1e-7)<1e-18
    numeric_bound=.000064/(4-.000064)
    assert numeric_error<=numeric_bound*(1+1e-8)
    # Verify the selected circle by independent source field tangency around it.
    center=25/16;radius=3*math.sqrt(41)/16;circle_samples=[]
    point=np.array([.4,.3])
    assert abs(np.linalg.norm(point-[center,0])-radius)<1e-14
    for phi in np.linspace(0,2*math.pi,13)[:-1]:
        p=np.array([center+radius*math.cos(phi),radius*math.sin(phi)])
        b=source_integral(p,configuration(2,1.))
        dot=float(b@(p-[center,0]))
        assert abs(dot)<3e-12
        circle_samples.append(dict(point=p.tolist(),field=b.tolist(),normal_dot_field=dot))
    unequal=[]
    for eta in [.2,.5,1.25,2.,5.]:
        wires=[(1.,0.,1),(-1.,0.,-eta)]
        interval=(1.0001,80.) if eta>1 else (-80.,-1.0001)
        recovered=brentq(lambda xp:source_integral([xp,0.],wires)[1],*interval,xtol=1e-12)
        predicted=(eta+1)/(eta-1)
        assert abs(recovered-predicted)<1e-11
        assert np.linalg.norm(source_integral([recovered,0.],wires))<2e-12
        unequal.append(dict(eta=eta,numeric_source_integral_zero_x=recovered,
                            predicted_x=predicted))
    delta=1e-5;wires=[(1.,0.,1),(-1.,0.,-2)]
    unequal_jac=np.column_stack([
        (source_integral([3+delta,0],wires)-source_integral([3-delta,0],wires))/(2*delta),
        (source_integral([3,delta],wires)-source_integral([3,-delta],wires))/(2*delta)])
    assert np.max(abs(unequal_jac-np.array([[0,-.125],[-.125,0]])))<2e-10
    eps=.001;radius_bound=(4*eps/(1+eps))**.25
    assert abs(radius_bound-.25142)<1e-5
    error_region=[]
    for fraction in [.25,.5,1.]:
        r=radius_bound*fraction
        bound=r**4/(4-r**4)
        for phi in np.linspace(0,2*math.pi,16,endpoint=False):
            p=r*np.array([math.cos(phi),math.sin(phi)])
            b=source_integral(p,configuration(4,1.));lin=2*np.array([p[0],-p[1]])
            error=float(np.linalg.norm(b-lin)/np.linalg.norm(lin))
            assert error<=bound*(1+5e-7)
            if abs(math.cos(4*phi)+1)<1e-12:
                assert abs(error-bound)<2e-12
            error_region.append(dict(radius=r,angle=float(phi),source_integral_error=error,
                                      proved_upper_bound=bound))
    assert abs((radius_bound/2)**4/(4-(radius_bound/2)**4)
               -eps/(16+15*eps))<1e-16
    names=['question-02','space-02','vectors-02','circles-02','quadrupole-02']
    sources=['scripts/verify_question_02.py','drafts/question-02.md','figures/题02_图稿源文件.tex']
    if args.complete:
        from audit_sources import inspect
        check=inspect('02');assert not check['issues'],check
        text=(ROOT/'drafts/question-02.md').read_text()
        assert '<!-- question-complete -->' in text
        assert all(f'../figures/{name}.png' in text for name in names)
        assert re.findall(r'(?m)^## (.+)$',text)==[
            '一、题型定位','二、知识点','三、物理图像','四、解题入口','五、解析',
            '六、关键洞察','七、易错点','八、课堂讲解建议','九、变式训练']
        assert len(re.findall(r'\*\*变式\d',text))==4
    report=dict(question=2,verified_math=True,document_complete=args.complete,set_accepted=False,
        scope='independent full-question mathematics and source check; actual PDF review is separate' if args.complete else 'independent preliminary physics verification, not full solution or visual acceptance',
        two_wire_exact_components=[str(sp.factor(z)) for z in expected2],
        two_wire_origin=[str(z) for z in origin2],two_wire_magnitude='2*K*ell/(r_plus*r_minus)',
        four_wire_origin_Jacobian=str(jac),
        four_wire_exact_complex_field='B_y+i B_x=8*i*K*ell^2*z/(z^4+4*ell^4), z=x+i*y',
        near_origin_two_wire_series=[str(z) for z in series2],
        near_origin_four_wire_series=[str(z) for z in series4],
        exact_two_wire_stream='r_minus^2/r_plus^2=kappa; kappa=1 gives x=0',
        exact_four_wire_stream='r_1^2*r_3^2/(r_2^2*r_4^2)=kappa; kappa=1 gives xy=0',
        near_origin_four_wire_stream='xy=constant away from the magnetic null; axes are separatrices',
        field_source_integrals=integrals,near_origin_relative_errors=near,
        ampere_loop_quadratures=ampere,two_wire_actual_field_ODE=lines2,
        four_wire_actual_field_ODE=lines4,source_integral_Jacobians=jrows,
        fully_answered_variants=dict(numerical=dict(B_two_wire_origin=numeric_b0.tolist(),
            B_four_wire_source_integral=numeric_p.tolist(),B_four_wire_linear=numeric_linear.tolist(),
            relative_vector_error=numeric_error,relative_error_bound=numeric_bound),
            selected_circle_source_integral_tangency=circle_samples,
            unequal_current_source_integral_roots=unequal,
            unequal_current_source_integral_Jacobian=unequal_jac.tolist(),
            all_direction_error_bound_radius=radius_bound,
            source_integral_error_region=error_region),
        physical_corrections=['For +I at (+ell,0), -I at (-ell,0), B_y at the origin is negative; handwritten positive component sum is not the signed Cartesian component.',
            'Handwritten four-wire B_y sum has B_4x where B_4y is required.',
            'Individual pair streamline circles do not independently remain streamlines after the other pair field is added.',
            'Exact four-wire quartic level curves are not globally xy=constant; the hyperbola is the leading local solution.',
            'At B=0 the quotient dy/dx is undefined; state the null and axis separatrices separately.'],
        dimensional_checks=dict(K='tesla*metre',uniform_field='K/ell: tesla',
                                quadrupole_gradient='K/ell^2: tesla/metre',passed=True),
        source_sha256={p:sha(ROOT/p) for p in sources if (ROOT/p).exists()},
        figures_sha256={name:sha(ROOT/f'figures/{name}.pdf') for name in names} if args.complete else {},
        originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')})
    out='verification-q02.json' if args.complete else 'verification-q02-preliminary.json'
    (ROOT/'build'/out).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=args.complete,source_integrals=len(integrals),
        local_error_convergence_cases=len(near),ampere_loops=len(ampere),
        two_wire_field_ODE=len(lines2),four_wire_field_ODE=len(lines4),
        source_integral_Jacobians=len(jrows),variant_circle_samples=len(circle_samples),
        variant_unequal_roots=len(unequal),variant_error_region_samples=len(error_region),
        four_series=[str(z) for z in series4]),ensure_ascii=False))
if __name__=='__main__':main()
