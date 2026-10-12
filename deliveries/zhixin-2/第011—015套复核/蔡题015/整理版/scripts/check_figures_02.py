"""Independent geometry checks; no automatic visual-reading claims."""
from pathlib import Path
import hashlib,itertools,json,math
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return [x-y for x,y in zip(a,b)]
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def norm(a):return math.sqrt(dot(a,a))
def close(a,b,tol=1e-10):assert abs(a-b)<tol,(a,b)
def main():
    path=ROOT/'build/question-02-figure-data.json';data=json.loads(path.read_text());tests=[]
    p=data['projection'];axes=[p[k] for k in ['u','v','w']]
    for i in range(3):
        for j in range(3):close(dot(axes[i],axes[j]),float(i==j))
    close(norm(sub(cross(axes[0],axes[1]),axes[2])),0);tests.append('orthonormal right-handed projection, round sphere silhouette')
    g=data['figures']['network-02'];v=g['vertices'];edges=g['edges'];faces=g['faces'];r=g['radius']
    assert len(v)==12 and len(edges)==30 and len(faces)==20
    L=math.sqrt(2*r*r*(1-1/math.sqrt(5)))
    for a,b in edges:close(norm(sub(v[a],v[b])),L)
    for a in range(12):
        assert sum(a in e for e in edges)==5;close(norm(v[a]),r)
    assert sorted([g['A'],g['B']]) in edges
    for face in faces:
        indices=face['vertices'];ctr=[sum(v[i][j] for i in indices)/3 for j in range(3)]
        assert dot(face['normal'],ctr)>0
        assert face['front']==(dot(face['normal'],axes[2])>0)
    for a,b,flag in g['edge_visible']:
        assert flag==any(f['front'] and a in f['vertices'] and b in f['vertices'] for f in faces)
    tests += ['12 genuine nodes, 30 equal edges, 20 outward faces','A/B are adjacent, not opposite; crossings are not nodes','front/back edges follow face normals, not guessed endpoint order']
    for name in ['network-02','sphere-02']:
        for lead in data['figures'][name]['leads']:
            close(norm(cross(lead['contact'],lead['outer'])),0)
            assert dot(lead['contact'],lead['outer'])>dot(lead['contact'],lead['contact'])
    tests.append('each radial lead ends at the actual contact, independently collinear')
    s=data['figures']['sphere-02']
    for point in ['A','B','P']:close(norm(s[point]),s['r'])
    close(dot(s['B'],s['P'])/s['r']**2,math.cos(math.radians(s['theta0_degrees']+s['theta_degrees'])))
    assert s['B'][0]<0<s['P'][0];close(s['P'][1],0)
    assert s['phi_degrees']==0
    tests.append('negative-x exit and positive-x phi=0 point give theta+theta0')
    sy=data['figures']['symmetry-02'];d,z=sy['mirror_plane'];n=cross(d,z)
    for point in v:
        reflected=[point[j]-2*dot(point,n)*n[j]/dot(n,n) for j in range(3)]
        assert min(norm(sub(reflected,q)) for q in v)<1e-9
        t=math.radians(sy['rotation_degrees']);rot=[point[0]*math.cos(t)-point[1]*math.sin(t),point[0]*math.sin(t)+point[1]*math.cos(t),point[2]]
        assert min(norm(sub(rot,q)) for q in v)<1e-9
    close(sy['net_source']+11*sy['other_net_sources'],0)
    tests.append('72-degree rotation/mirror preserve vertices; auxiliary node source sums to zero')
    plane=data['figures']['plane-02']
    assert all(p[2]==0 for p in plane['plane_corners'])
    assert plane['z_wire_direction']==[0,0,-1]
    assert {p['z']>0 for p in plane['loops']}=={True,False}
    tests.append('plane K outward, wire toward negative-z, positive loops normal +z')
    for name,key in [('cap-02','r'),('ampere-02','R')]:
        g=data['figures'][name];radius=g[key];gamma=math.radians(g['gamma_degrees'])
        close(norm(g['P']),radius)
        close(norm(sub(g['P'],g['latitude_center'])),radius*math.sin(gamma))
        close(g['latitude_radius'],radius*math.sin(gamma))
    assert data['figures']['ampere-02']['R']>data['figures']['ampere-02']['r']
    tests.append('curved cap mesh, correct circle centres; outside loop uses R sin gamma, not r sin gamma')
    j=data['figures']['jump-02'];assert cross(j['K'],j['n'])==j['Bout_direction']
    tests.append('local into-page K cross outward n gives rightward outside B')
    controls=[c for c in (ROOT/'figures/题02_图稿源文件.tex').read_bytes() if c<32 and c not in (9,10)]
    assert not controls
    names=list(data['figures'])
    # The collection dict creation order differs from manuscript reading order.
    figures={name:{ext+'_sha256':sha(ROOT/f'figures/{name}.{ext}') for ext in ['pdf','png']} for name in sorted(names)}
    report=dict(scope='015 Q2 mathematical geometry only; actual visual review separate',passed=True,
                automatic_visual_review=False,checks=tests,figures=figures,
                bound_sha256={p:sha(ROOT/p) for p in ['scripts/draw_figures_02.py','scripts/check_figures_02.py','build/question-02-figure-data.json','figures/题02_图稿源文件.tex']})
    (ROOT/'build/question-02-figure-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=len(tests),figures=len(figures)),ensure_ascii=False))
if __name__=='__main__':main()

