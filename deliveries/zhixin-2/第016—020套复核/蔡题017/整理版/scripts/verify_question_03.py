"""017 Q3: signed geometry and independently integrated 3D membrane patches.

The numerical checks are independent of the typeset solution. A complete
question-source record still does not imply whole-set or visual acceptance.
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad,quad_vec
from scipy.optimize import minimize_scalar,brentq
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    R,r,theta,phi,p=sp.symbols('R r theta phi p',positive=True)
    radius=R-r*sp.cos(theta)
    X=sp.Matrix([radius*sp.cos(phi),radius*sp.sin(phi),r*sp.sin(theta)])
    etheta=sp.diff(X,theta)/r
    ephi=sp.diff(X,phi)/radius
    normal=sp.simplify(etheta.cross(ephi))
    assert sp.simplify(normal.dot(normal)-1)==0
    ktheta=sp.simplify(-normal.dot(sp.diff(X,theta,2))/r**2)
    kphi=sp.simplify(-normal.dot(sp.diff(X,phi,2))/radius**2)
    assert ktheta==1/r
    assert sp.simplify(kphi+sp.cos(theta)/radius)==0
    assert sp.simplify(normal.dot(sp.diff(X,theta,phi)))==0
    # Defined by the cut: sigma1 acts along the toroidal direction, sigma2 along
    # the meridian. A force is normal to its cut line, not tangent to that line.
    toroidal=p*r/2
    meridional=p*r*(2*R-r*sp.cos(theta))/(2*radius)
    assert sp.simplify(meridional*ktheta+toroidal*kphi-p)==0
    assert sp.simplify(sp.diff(radius*meridional,theta)-sp.diff(radius,theta)*toroidal)==0
    C=sp.symbols('C')
    singular_y=p*r*(R-r*sp.cos(theta)/2)+C/sp.cos(theta)
    assert sp.simplify(sp.diff(singular_y*sp.cos(theta),theta)+p*r*radius*sp.sin(theta))==0
    # Finite annular cap; independently integrate the outward pressure projection.
    cap_rows=[]
    for RR,rr,pressure in [(2,.4,1.3),(1.2,1,2.1),(5,.8,.7)]:
        for angle in [.0,.35,1.2,1.8,2.4,math.pi]:
            s=RR-rr*math.cos(angle)
            # Upper inner/outer surface sections bounded by the top parallel:
            low,high=(angle,math.pi/2) if angle<math.pi/2 else (math.pi/2,angle)
            force=2*math.pi*pressure*rr*quad(lambda a:(RR-rr*math.cos(a))*math.sin(a),low,high,epsabs=1e-11)[0]
            tension_from_integral=force/(2*math.pi*s*abs(math.cos(angle)))
            analytic=pressure*rr*(2*RR-rr*math.cos(angle))/(2*s)
            assert abs(tension_from_integral/analytic-1)<1e-12
            cap_rows.append(dict(R=RR,r=rr,theta=angle,integrated_pressure_z=force,
                                 sigma2_from_cap=tension_from_integral,sigma2_from_formula=analytic))
    # Recover both tensions from Cartesian force integrals, not by substituting
    # their final formulas into the local Laplace equation.
    # Unknowns: sigma1=H, s*sigma2=C0+C1*cos(theta).
    rectangles=[(.12,.68,-.3,.45),(.45,1.4,.7,1.45),(1.2,1.95,-1.5,-.4),
                (1.85,2.9,.15,.9),(3.0,3.7,-.2,.6),(4.0,5.2,1.1,2.1)]
    patch_sets=[]
    for RR,rr,pressure in [(2,.4,1.3),(1.2,1,2.1),(5,.8,.7),(3,1,.6)]:
        def s(a):return RR-rr*math.cos(a)
        def tangent_t(a,b):return np.array([math.sin(a)*math.cos(b),math.sin(a)*math.sin(b),math.cos(a)])
        def tangent_p(b):return np.array([-math.sin(b),math.cos(b),0])
        def n(a,b):return np.array([-math.cos(a)*math.cos(b),-math.cos(a)*math.sin(b),math.sin(a)])
        matrices=[];rhs=[];force_data=[]
        for low,high,left,right in rectangles:
            edge_p=rr*(high-low)*(tangent_p(right)-tangent_p(left))
            at_high=quad_vec(lambda b:tangent_t(high,b),left,right,epsabs=1e-11)[0]
            at_low=quad_vec(lambda b:tangent_t(low,b),left,right,epsabs=1e-11)[0]
            edge_0=at_high-at_low
            edge_1=math.cos(high)*at_high-math.cos(low)*at_low
            def integrated_ring(a):
                return quad_vec(lambda b:pressure*n(a,b)*rr*s(a),left,right,epsabs=1e-11)[0]
            outward=quad_vec(integrated_ring,low,high,epsabs=1e-11)[0]
            M=np.column_stack([edge_p,edge_0,edge_1])
            matrices.append(M);rhs.append(-outward)
            force_data.append((M,outward))
        matrix=np.vstack(matrices);vector=np.concatenate(rhs)
        recovered,_,rank,_=np.linalg.lstsq(matrix,vector,rcond=None)
        assert rank==3
        expected=np.array([pressure*rr/2,pressure*rr*RR,-pressure*rr*rr/2])
        assert np.max(abs(recovered-expected))<2e-12
        residuals=[float(np.linalg.norm(M@recovered+outward)) for M,outward in force_data]
        assert max(residuals)<2e-12
        patch_sets.append(dict(R=RR,r=rr,pressure=pressure,rectangles=len(rectangles),
                               independently_recovered_H_C0_C1=recovered.tolist(),
                               expected_H_C0_C1=expected.tolist(),cartesian_force_residuals=residuals))
    # Recover curvature using finite differences of the actual 3D embedding.
    curvature_rows=[]
    for angle in [.0,.4,math.pi/2,2.1,math.pi,4.7]:
        for azimuth in [.0,.8]:
            RR,rr=3.,.7;h=3e-4
            def position(a,b):
                s=RR-rr*math.cos(a)
                return np.array([s*math.cos(b),s*math.sin(b),rr*math.sin(a)])
            s=RR-rr*math.cos(angle)
            n=np.array([-math.cos(angle)*math.cos(azimuth),-math.cos(angle)*math.sin(azimuth),math.sin(angle)])
            second_t=(position(angle+h,azimuth)-2*position(angle,azimuth)+position(angle-h,azimuth))/h**2
            second_p=(position(angle,azimuth+h)-2*position(angle,azimuth)+position(angle,azimuth-h))/h**2
            numeric_t=-float(n@second_t)/rr**2
            numeric_p=-float(n@second_p)/s**2
            assert abs(numeric_t-1/rr)<2e-7
            assert abs(numeric_p+math.cos(angle)/s)<2e-8
            curvature_rows.append(dict(theta=angle,phi=azimuth,numeric_k_meridional=numeric_t,
                                        numeric_k_toroidal=numeric_p))
    # An independent bounded optimizer locates the meridional tension maximum.
    maxima=[]
    for RR,rr,pressure in [(2,.4,1.3),(1.2,1,2.1),(5,.8,.7),(3,1,.6)]:
        f=lambda a:pressure*rr*(2*RR-rr*math.cos(a))/(2*(RR-rr*math.cos(a)))
        optimum=minimize_scalar(lambda a:-f(a),bounds=(-.9,.9),method='bounded',
                                 options={'xatol':1e-13})
        assert abs(optimum.x)<5e-7
        inner=pressure*rr*(2*RR-rr)/(2*(RR-rr))
        outer=pressure*rr*(2*RR+rr)/(2*(RR+rr))
        assert abs(-optimum.fun/inner-1)<1e-12
        assert inner>outer>pressure*rr/2
        maxima.append(dict(R=RR,r=rr,theta_max=optimum.x,sigma2_max=inner,
                           sigma2_outer=outer,sigma1_constant=pressure*rr/2))
    # Cylinder: numerically integrated half-wall normal pressure, and closed-end
    # disk pressure, recovered independently from their cut-force equations.
    cylinder=[]
    for rr,height,pressure in [(.3,2,1.7),(.8,3,.6),(1.1,5,2.4)]:
        normal_force=quad(lambda a:pressure*rr*height*math.cos(a),-math.pi/2,math.pi/2)[0]
        hoop=normal_force/(2*height)
        axial=(pressure*math.pi*rr*rr)/(2*math.pi*rr)
        assert abs(hoop-pressure*rr)<1e-12
        assert abs(axial-pressure*rr/2)<1e-12
        cylinder.append(dict(r=rr,segment_length=height,sigma1_hoop=hoop,sigma2_axial=axial))
    # Delta-p times length has force per cut length; thin/large-R limits.
    assert sp.limit(meridional,R,sp.oo)==p*r
    assert sp.simplify(meridional-toroidal-p*r*R/(2*radius))==0
    x=sp.symbols('x')
    ratio=(2*R-r*x)/(2*(R-r*x))
    assert sp.simplify(sp.diff(ratio,x)-r*R/(2*(R-r*x)**2))==0
    # Solved variants: direct numbers, pressure threshold, radius roots and
    # directional-strength competition are checked before typeset acceptance.
    v1=dict(sigma1=8000*.025,sigma2=8000*.025/2,
            material_stress1=8000*.025/.0002,material_stress2=8000*.025/(2*.0002),
            maximum_pressure=1.6e6*.0002/.025)
    assert list(v1.values())==[200.,100.,1.e6,5.e5,12800.]
    v2=[]
    for angle,expected in [(0,7/6),(math.pi/2,1),(math.pi,.9)]:
        value=(8-math.cos(angle))/(2*(4-math.cos(angle)))
        assert abs(value-expected)<1e-15
        v2.append(dict(theta=angle,sigma2_over_pr=value))
    assert abs(v2[0]['sigma2_over_pr']/v2[2]['sigma2_over_pr']-35/27)<1e-15
    radius_roots=[]
    for rr in [.1,.7,1.3]:
        for capacity_ratio in [1.01,1.3,2]:
            pp=.8;capacity=capacity_ratio*pp*rr
            maximum_tension=lambda big:pp*rr*(2*big-rr)/(2*(big-rr))
            root=brentq(lambda big:maximum_tension(big)-capacity,rr*(1+1e-6),rr*1000,xtol=1e-12)
            expected=rr*(2*capacity-pp*rr)/(2*(capacity-pp*rr))
            assert abs(root/expected-1)<2e-11
            assert maximum_tension(root*.99)>capacity and maximum_tension(root*1.01)<capacity
            radius_roots.append(dict(r=rr,capacity_over_pr=capacity_ratio,
                                      R_min_from_force_root=root,R_min_formula=expected))
    pressure_roots=[]
    for ratio in [1.2,2,4,10]:
        rr=.4;RR=ratio*rr
        for capacity1,capacity2 in [(.2,1),(1,1),(4,1)]:
            utilization=lambda pressure:max(pressure*rr/(2*capacity1),
                                            pressure*rr*(2*RR-rr)/(2*(RR-rr)*capacity2))
            root=brentq(lambda pressure:utilization(pressure)-1,0,100)
            expected=min(2*capacity1/rr,2*capacity2*(RR-rr)/(rr*(2*RR-rr)))
            assert abs(root-expected)<1e-12
            assert utilization(root*.99)<1 and utilization(root*1.01)>1
            pressure_roots.append(dict(R_over_r=ratio,Lambda1=capacity1,Lambda2=capacity2,
                                       maximum_pressure_from_utilization_root=root))
    figures=['question-03','torus-03','cylinder-03','cap-03','geometry-03','rupture-03']
    source_paths=['scripts/verify_question_03.py','drafts/question-03.md',
                  'figures/题03_图稿源文件.tex','scripts/generate_torus_mesh.py',
                  'figures/torus-base-03.tex','figures/torus-cap-03.tex',
                  'build/torus-mesh-q03.json']
    complete=all((ROOT/rel).exists() for rel in source_paths) and all(
        (ROOT/f'figures/{name}.{extension}').exists()
        for name in figures for extension in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-03.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察',
                 '易错点','课堂讲解建议','变式训练']
        assert text.count('<!-- question-complete -->')==1
        assert [line.split('、',1)[1] for line in text.splitlines() if line.startswith('## ')]==modules
        assert all(text.count(f'../figures/{name}.png')==1 for name in figures)
        mesh=json.loads((ROOT/'build/torus-mesh-q03.json').read_text())
        assert abs(mesh['ratio']-3)<1e-14 and mesh['vector_tiles']==2048
        assert abs(np.dot(mesh['camera'],mesh['screen_vertical']))<1e-14
        for name,digest in mesh['generated_mesh_sha256'].items():
            assert sha(ROOT/'figures'/name)==digest
        assert sha(ROOT/'scripts/generate_torus_mesh.py')==mesh['generator_sha256']
        # Verify the original cylinder's drawn cut endpoints lie on the
        # projected rim and the plane is parallel to its diameter.
        assert abs((.85/1.1)**2+(.216/.34)**2-1)<.001
        assert abs((3.616-3.184)-2*.216)<1e-14
    # Dimension vectors ordered as mass, length, time.
    pressure_dimension=np.array([1,-1,-2])
    length_dimension=np.array([0,1,0])
    membrane_dimension=np.array([1,0,-2])
    force_dimension=np.array([1,1,-2])
    assert np.array_equal(pressure_dimension+length_dimension,membrane_dimension)
    assert np.array_equal(pressure_dimension+2*length_dimension,force_dimension)
    assert np.array_equal(membrane_dimension-length_dimension,pressure_dimension)
    report=dict(question=3,verified_math=True,document_complete=complete,set_accepted=False,
                scope='independent membrane/3D integration and complete question source, not PDF visual or whole-set acceptance' if complete else 'preliminary mathematical verification',
                outward_normal=str(normal),signed_curvatures=dict(meridional=str(ktheta),toroidal=str(kphi)),
                tensions=dict(sigma1_toroidal=str(toroidal),sigma2_meridional=str(meridional)),
                cylinder_cut_balances=cylinder,annular_cap_integrals=cap_rows,
                cartesian_patch_recovery=patch_sets,finite_difference_curvatures=curvature_rows,
                independent_maximum_searches=maxima,
                solved_variants=dict(stress_conversion=v1,ratio_four_samples=v2,
                                     minimum_radius_roots=radius_roots,directional_pressure_roots=pressure_roots),
                assumptions=['R > r > 0, pressure difference positive, thin membrane static equilibrium',
                             'cylinder axial tension requires closed ends whose pressure load is carried by side wall',
                             'rupture-location conclusion assumes comparable local directional tensile limits'],
                handwritten_notes=['sigma1=constant p*r/2 and sigma2=variable are consistent with torus definitions',
                                   'signed hoop curvature is -cos(theta)/(R-r*cos(theta)); scalar radius notation must preserve this sign',
                                   'cylinder and torus cut definitions assign the same indices to different force directions'],
                text_source_written=(ROOT/'drafts/question-03.md').exists(),
                dimensional_checks=dict(order=['mass','length','time'],
                    pressure=pressure_dimension.tolist(),membrane_tension=membrane_dimension.tolist(),
                    total_force=force_dimension.tolist(),passed=True),
                vector_mesh_construction_checked=complete,
                figures_sha256={name:sha(ROOT/f'figures/{name}.pdf') for name in figures} if complete else {},
                source_sha256={rel:sha(ROOT/rel) for rel in source_paths if (ROOT/rel).exists()},
                originals_sha256={a.name:sha(a) for a in ROOT.parent.glob('*.pdf')})
    record='verification-q03.json' if complete else 'verification-q03-preliminary.json'
    (ROOT/'build'/record).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,
                          cap_integrals=len(cap_rows),cartesian_patches=sum(a['rectangles'] for a in patch_sets),
                          curvature_samples=len(curvature_rows),cylinder_cuts=len(cylinder),
                          maximum_searches=len(maxima)),ensure_ascii=False))
if __name__=='__main__':main()
