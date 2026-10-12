"""Generate Q2 TikZ from true 3D geometry, preserving earlier question files.
Generated TeX/geometry data are reproducible outputs; render is not review.
"""
from pathlib import Path
import itertools, json, math
ROOT=Path(__file__).resolve().parents[1]
SQ=math.sqrt
U=(SQ(3)/2, .5, 0)
V=(-.25, SQ(3)/4, SQ(3)/2)
W=(SQ(3)/4, -.75, .5)
NAMES=['network-02','sphere-02','symmetry-02','plane-02','cap-02','ampere-02','jump-02']
records={}
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(a,s): return tuple(x*s for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def project(p): return (dot(p,U),dot(p,V))
def xy(p): return '('+','.join(f'{x:.6f}' for x in project(p))+')'
def p2(p): return '('+','.join(f'{x:.6f}' for x in p)+')'
def polar(r,t,f=0):
    t,f=math.radians(t),math.radians(f)
    return (r*math.sin(t)*math.cos(f),r*math.sin(t)*math.sin(f),r*math.cos(t))
def ring(r,t,f): return polar(r,t,f)
def equator(r,f,z=0):
    f=math.radians(f)
    return (r*math.cos(f),r*math.sin(f),z)
def path(points,style='',close=False):
    return r'\draw['+style+'] '+ ' -- '.join(xy(p) for p in points)+(r' -- cycle;' if close else ';')
def line(a,b,style=''):return path([a,b],style)
def curve(fun,a,b,style='',step=2):
    n=max(2,math.ceil(abs(b-a)/step))
    return path([fun(a+(b-a)*i/n) for i in range(n+1)],style)
def hidden_curve(fun,a,b,style='gray!65,thin',step=2):
    n=max(2,math.ceil(abs(b-a)/step));pts=[fun(a+(b-a)*i/n) for i in range(n+1)]
    out=[];seg=[pts[0]];front=None
    for p,q in zip(pts,pts[1:]):
        now=dot(mul(add(p,q),.5),W)>=0
        if front is not None and now!=front:
            out.append(path(seg,style+('' if front else ',dashed')))
            seg=[p]
        seg.append(q);front=now
    out.append(path(seg,style+('' if front else ',dashed')))
    return '\n'.join(out)
def node(p,text,opts='above right'):
    return r'\node['+opts+'] at '+xy(p)+' {'+text+'};'
def node2(p,text,opts='above right'):
    return r'\node['+opts+'] at '+p2(p)+' {'+text+'};'
def point(p,color='black'):
    return r'\fill['+color+'] '+xy(p)+r' circle (1.7pt);'
def start(): return r'\begin{tikzpicture}[>=Latex,line cap=round,line join=round,font=\small]'
def finish():return r'\end{tikzpicture}'
def sphere(r):
    return r'\fill[gray!5] (0,0) circle ('+str(r)+');\n'+hidden_curve(lambda f:equator(r,f),-150,210)+ '\n'+hidden_curve(lambda t:polar(r,t),-49.106605,310.893395)+ '\n'+r'\draw[black!75,thick] (0,0) circle ('+str(r)+');'
def capmesh(r,g,color='orange!22'):
    # Fill only visible spherical cells, not a flat latitude disk.
    out=[]
    for t0 in range(0,int(g),5):
        t1=min(t0+5,g)
        for f0 in range(-180,180,6):
            f1=f0+6
            if dot(polar(r,(t0+t1)/2,(f0+f1)/2),W)<0:continue
            pts=[polar(r,t0,f0),polar(r,t1,f0),polar(r,t1,f1),polar(r,t0,f1)]
            out.append(r'\fill['+color+'] '+' -- '.join(xy(p) for p in pts)+r' -- cycle;')
    return '\n'.join(out)
def arrowtangent(r,t,f,style='blue!75!black,very thick,->'):
    # Arc orientation is increasing polar angle, tangent away from north contact.
    return curve(lambda s:polar(r,s,f),t,t+13,style,1)
def radial_arrow(r,t,f,length=.4):
    a=polar(r,t,f)
    return line(a,mul(a,1+length/r),'teal!75!black,->,thick')
def ico():
    r=2.2;h=r/SQ(5);s=2*r/SQ(5);alpha=-20
    vertices=[(0,0,r),(0,0,-r)]
    for z,off in [(h,0),(-h,36)]:
        for k in range(5):
            f=math.radians(alpha+off+72*k);vertices.append((s*math.cos(f),s*math.sin(f),z))
    l=SQ(2*r*r*(1-1/SQ(5)))
    edges=[(i,j) for i,j in itertools.combinations(range(12),2) if abs(SQ(dot(sub(vertices[i],vertices[j]),sub(vertices[i],vertices[j])))-l)<1e-8]
    faces=[]
    for a,b,c in itertools.combinations(range(12),3):
        if all(tuple(sorted(e)) in edges for e in [(a,b),(b,c),(c,a)]):
            ctr=mul(add(add(vertices[a],vertices[b]),vertices[c]),1/3)
            normal=cross(sub(vertices[b],vertices[a]),sub(vertices[c],vertices[a]))
            if dot(normal,ctr)<0:normal=mul(normal,-1)
            faces.append(dict(vertices=[a,b,c],front=dot(normal,W)>0,normal=normal))
    visible={e:any(f['front'] and e[0] in f['vertices'] and e[1] in f['vertices'] for f in faces) for e in edges}
    return vertices,edges,faces,visible
def skeleton(verts,edges,faces,visible):
    out=[]
    for face in faces:
        if face['front']:
            out.append(r'\fill[gray!7] '+' -- '.join(xy(verts[i]) for i in face['vertices'])+r' -- cycle;')
    for flag in [False,True]:
        for e in edges:
            if visible[e]==flag:
                out.append(line(verts[e[0]],verts[e[1]],'black!75,thick' if flag else 'gray!55,dashed,thin'))
    for i,p in enumerate(verts):
        out.append(point(p,'black' if dot(p,W)>=0 else 'gray!65'))
    return '\n'.join(out)
def network():
    v,e,f,vis=ico();out=[start(),skeleton(v,e,f,vis)]
    a,b=v[0],v[2]
    out += [line((0,0,0),a,'gray,dashed'),line((0,0,0),b,'gray,dashed'),
            r'\draw[fill=white] (0,0) circle (1.5pt);',node2((-.13,-.15),'$O$','below left'),
            line(mul(a,1.58),a,'blue!75!black,very thick,->'),
            node(mul(a,1.4),'$I$','right'),
            line(b,mul(b,1.67),'blue!75!black,very thick,->'),
            node(mul(b,1.5),'$I$','above'),
            node(a,'$A$','above left'),node(b,'$B$','below right')]
    # Label one front edge not joining either special vertex.
    out.append(node(mul(add(v[5],v[6]),.5),'$l$','below left'))
    out.append(finish())
    records['network-02']=dict(vertices=v,edges=e,faces=f,edge_visible=[list(k)+[x] for k,x in vis.items()],radius=2.2,A=0,B=2,leads=[dict(contact=a,outer=mul(a,1.58),direction='in'),dict(contact=b,outer=mul(b,1.67),direction='out')])
    return '\n'.join(out)
def symmetry():
    v,e,f,vis=ico();a=v[0];d=mul(v[2],1/SQ(v[2][0]**2+v[2][1]**2))
    # Mirror plane contains vertical symmetry axis and one upper vertex.
    poly=[add(mul(d,s), (0,0,z)) for s,z in [(-2.35,-2.6),(2.35,-2.6),(2.35,2.6),(-2.35,2.6)]]
    out=[start(),r'\fill[blue!9] '+' -- '.join(xy(p) for p in poly)+r' -- cycle;',skeleton(v,e,f,vis),
         path(poly,'blue!45,dashed',True),line((0,0,-2.8),(0,0,3.25),'blue!65!black,->'),
         node((0,0,3.2),'$OA$','left'),node(mul(d,-2.5),r'$\Pi$','left'),
         line(mul(a,1.48),a,'orange!85!black,thick,->'),
         node(mul(a,1.25),r'$\frac{11I}{12}$','right'),node(a,'$A$','above left')]
    for i in [2,3,4,5,6,1]:
        p=v[i];out.append(line(p,mul(p,1.14),'orange!85!black,->'))
    out += [node(mul(v[3],1.3),'$-I/12$','above right'),
            curve(lambda f: equator(.65,f,1.5),-20,52,'blue!65!black,->,thick',2),
            node(equator(.78,16,1.5),r'$72^\circ$','right'),r'\draw[fill=white] (0,0) circle (1.5pt);',node2((-.1,-.12),'$O$','below left'),finish()]
    records['symmetry-02']=dict(mirror_plane=[d,(0,0,1)],rotation_degrees=72,net_source=11/12,other_net_sources=-1/12,geometry_same_as='network-02')
    return '\n'.join(out)
def real_sphere():
    r=2.2;a=polar(r,0);b=polar(r,45,180);p=polar(r,75)
    out=[start(),sphere(r),
         line((0,0,0),(2.95,0,0),'gray!70,->'),node((2.95,0,0),'$x$','right'),
         line((0,0,0),(0,0,3.75),'gray!70,->'),node((0,0,3.75),'$z$','above'),
         line((0,0,0),(0,2.6,0),'gray!65,dashed,->'),node((0,2.6,0),'$y$','above right'),
         line(mul(a,1.5),a,'blue!75!black,very thick,->'),node(mul(a,1.3),'$I$','right'),
         line(b,mul(b,1.65),'blue!75!black,very thick,->'),node(mul(b,1.48),'$I$','above left'),
         line((0,0,0),b,'black!70,dashed'),line((0,0,0),p,'black!70,dashed'),
         curve(lambda t:polar(.9,t,180),0,45,'orange!80!black,->'),
         node(polar(1.05,22.5,180),r'$\theta_0$','left'),
         curve(lambda t:polar(.64,t),0,75,'blue!75!black,->'),
         node(polar(.88,48),r'$\theta$','right'),
         arrowtangent(r,75,0),
         node(polar(r,88),r'$\mathbf K$','below right'),
         point(a),point(b),point(p),node(a,'$A$','above left'),node(b,'$B$','below left'),
         node(p,r'$P\;(\phi=0)$','above right'),node2((-.08,-.13),'$O$','below left'),finish()]
    records['sphere-02']=dict(r=r,theta0_degrees=45,theta_degrees=75,phi_degrees=0,A=a,B=b,P=p,leads=[dict(contact=a,outer=mul(a,1.5),direction='in'),dict(contact=b,outer=mul(b,1.65),direction='out')],K_arrow=[polar(r,75),polar(r,88)],angle_BOP_degrees=120)
    return '\n'.join(out)
def plane():
    out=[start()]
    poly=[(-2.6,-2.0,0),(2.6,-2.0,0),(2.6,2.0,0),(-2.6,2.0,0)]
    out.append(r'\fill[gray!12] '+' -- '.join(xy(p) for p in poly)+r' -- cycle;')
    out.append(path(poly,'gray!60',True))
    # Circular paths are mathematical loops, not conductors.
    for z,label in [(-1.25,r'$C_-$'),(1.25,r'$C_+$')]:
        out.append(curve(lambda f:equator(1.3,f,z),0,360,'orange!80!black,dashed' if z<0 else 'orange!80!black,thick'))
        out.append(curve(lambda f:equator(1.3,f,z),-30,3,'orange!85!black,->,thick',1))
        out.append(node(equator(1.3,10,z),label,'right'))
    out += [line((0,0,-1.9),(0,0,3.35),'gray!65,->'),node((0,0,3.35),'$z$','above'),
            line((0,0,0),(3.3,0,0),'gray!65,->'),node((3.3,0,0),'$x$','right'),
            line((0,0,0),(0,2.4,0),'gray!65,->'),node((0,2.4,0),'$y$','above right')]
    for f in range(0,360,45):
        a=equator(.32,f);b=equator(1.88,f)
        out.append(line(a,b,'blue!75!black,->,thick'))
    out += [line((0,0,3.05),(0,0,0),'black,very thick'),
            line((0,0,2.65),(0,0,1.75),'black,very thick,->'),node((0,0,2.5),'$I$','left'),
            point((0,0,0)),node2((-.08,-.10),'$O$','below left'),
            node(equator(1.72,-45),r'$\mathbf K$','below right'),
            line((0,0,1.25),equator(1.3,-30,1.25),'gray!65,dotted'),
            node(equator(.8,-30,1.25),r'$\rho$','above'),finish()]
    records['plane-02']=dict(plane_corners=poly,z_wire_direction=[0,0,-1],loops=[dict(z=-1.25,radius=1.3),dict(z=1.25,radius=1.3)],positive_loop_angle='increasing phi, normal +z',K='radially outward')
    return '\n'.join(out)
def auxiliary_cap():
    r=2.2;g=50
    out=[start(),r'\fill[gray!5] (0,0) circle (2.2);',capmesh(r,g),
         hidden_curve(lambda f:equator(r,f),-150,210),
         hidden_curve(lambda t:polar(r,t),-49.106605,310.893395),
         r'\draw[black!75,thick] (0,0) circle (2.2);',
         hidden_curve(lambda f:ring(r,g,f),-180,180,'orange!80!black,thick')]
    for t,f in [(35,0),(55,-60),(80,-90),(105,-75),(25,70),(70,-25)]:
        out.append(radial_arrow(r,t,f))
    out.append(arrowtangent(r,g,0))
    p=polar(r,g);c=(0,0,r*math.cos(math.radians(g)))
    out += [line((0,0,0),p,'black!70,dashed'),line((0,0,0),polar(r,0),'gray!65,dashed'),
            line(c,p,'orange!80!black,dotted'),
            node2((.48,1.16),r'$r\sin\gamma$','above'),
            curve(lambda t:polar(.95,t),0,g,'black!70,->'),node2((.05,.40),r'$\gamma$','right,inner sep=0pt'),
            node2((-.52,1.5),r'$S_\gamma$','above'),
            line(polar(r,0),polar(1.55*r,0),'black,very thick'),
            line(polar(1.48*r,0),polar(1.15*r,0),'black,->,very thick'),
            node(polar(1.35*r,0),'$I$','right'),
            point(p),node(p,'$P$','right'),
            node(polar(r+.44,35,0),r'$j_{\rm out}$','above right'),
            node(polar(r,g+10,5),r'$K_\gamma$','below right'),
            node2((-.1,-.15),'$O$','below left'),finish()]
    records['cap-02']=dict(r=r,gamma_degrees=g,latitude_center=c,latitude_radius=r*math.sin(math.radians(g)),P=p,mesh='visible spherical quadrilaterals',normal_outflow='radial outward',K_arrow='increasing gamma')
    return '\n'.join(out)
def ampere():
    r=1.25;R=2.4;g=50
    out=[start(),r'\fill[gray!3] (0,0) circle (2.4);',capmesh(R,g,'orange!13'),
         r'\draw[gray!45,dashed] (0,0) circle (2.4);',
         sphere(r),hidden_curve(lambda f:ring(R,g,f),-180,180,'orange!85!black,very thick')]
    for t,f in [(45,-25),(48,-90)]:
        out.append(line(polar(r,t,f),polar(R+.25,t,f),'teal!75!black,->,thick'))
    a=polar(r,0);p=polar(R,g);c=(0,0,R*math.cos(math.radians(g)))
    out += [line(polar(R*1.42,0),a,'black,very thick'),
            line(polar(R*1.33,0),polar(R*.98,0),'black,very thick,->'),
            node(polar(R*1.24,0),'$I$','right'),
            line((0,0,0),p,'gray!70,dashed'),node(polar(R*.65,g),'$R$','below right'),
            line((0,0,0),polar(r,110),'gray!65,dashed'),node(polar(r*.66,110),'$r$','below'),
            line(c,p,'orange!75!black,dotted'),node(mul(add(c,p),.5),r'$R\sin\gamma$','above=6pt'),
            curve(lambda t:polar(.8,t),0,g,'black!70,->'),node2((.04,.32),r'$\gamma$','right,inner sep=0pt'),
            curve(lambda f:ring(R,g,f),-30,8,'orange!85!black,very thick,->',1),
            node(polar(R,g,-150),r'$C_\gamma$','left'),
            node(polar(R,20,-65),r'$S_\gamma(R)$','above left'),
            point(p),node(p,'$P$','right'),node2((-.08,-.13),'$O$','below left'),finish()]
    records['ampere-02']=dict(r=r,R=R,gamma_degrees=g,latitude_center=c,latitude_radius=R*math.sin(math.radians(g)),P=p,normal_outflow='radial outward',loop_direction='increasing phi',negative_wire_current=-1)
    return '\n'.join(out)
def jump():
    out=[start(),r'\fill[gray!13] (-2.7,-.045) rectangle (2.7,.045);',
         r'\draw[gray!70] (-2.7,0)--(2.7,0);',
         r'\draw[orange!80!black,thick] (-.9,-.35) rectangle (.9,.35);',
         r'\draw[orange!85!black,->,thick] (-.65,.35)--(.25,.35);',
         r'\draw[orange!85!black,->,thick] (.65,-.35)--(-.25,-.35);',
         r'\draw[blue!75!black,very thick,->] (1.15,.85)--(2.35,.85);',
         r'\node[above] at (1.75,.85) {$\mathbf B_{\rm out}$};',
         r'\node at (1.72,-.8) {$\mathbf B_{\rm in}=0$};',
         r'\draw[teal!75!black,->,thick] (-1.6,.08)--(-1.6,1.25);',
         r'\node[left] at (-1.6,.85) {$\mathbf n$};',
         r'\node[fill=white,inner sep=1pt] at (0,0) {$\otimes$};',
         r'\node at (0,-.63) {$\mathbf K$};',
         r'\node[left] at (-2.7,0) {$R=r$};',
         r'\node at (0,-1.3) {$\mathbf B_{\rm out}-\mathbf B_{\rm in}=\mu_0\,\mathbf K\times\mathbf n$};',
         finish()]
    records['jump-02']=dict(n=[0,1,0],K=[0,0,-1],Bout_direction=[1,0,0],loop_direction='clockwise; area normal into page')
    return '\n'.join(out)
def main():
    figs=[network(),real_sphere(),symmetry(),plane(),auxiliary_cap(),ampere(),jump()]
    preamble=r"""\documentclass[tikz,border=5pt]{standalone}
\usepackage[UTF8]{ctex}
\usepackage{amsmath,amssymb}
\usetikzlibrary{arrows.meta}
\begin{document}
"""
    text=preamble+'\n\n'.join('% '+name+'\n'+fig for name,fig in zip(NAMES,figs))+'\n'+r'\end{document}'+'\n'
    (ROOT/'figures/题02_图稿源文件.tex').write_text(text)
    report=dict(scope='Q2 true 3D geometry, not automatic visual review',projection=dict(u=U,v=V,w=W),figures=records)
    (ROOT/'build/question-02-figure-data.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('Generated',len(figs),'figures; TeX characters',len(text))
if __name__=='__main__':main()
