"""只读复核既有第013套交付，不生成/覆盖成品或改写主稿。"""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import math
import re
import subprocess

import fitz
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'preview' / 'cross-thread-audit'
checks = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def symbolic(name, expression):
    residual = s.simplify(expression)
    assert residual == 0, (name, residual)
    checks.append({'name': name, 'kind': 'symbolic', 'passed': True})


def numeric(name, residual, tolerance):
    residual = float(abs(residual))
    assert residual < tolerance, (name, residual, tolerance)
    checks.append({'name': name, 'kind': 'numerical', 'residual': residual,
                   'tolerance': tolerance, 'passed': True})


def boost_event(event, V):
    # c=1；变换事件，不调用速度变换或讲义中的直线公式。
    t, x, y = event
    gamma = 1 / math.sqrt(1 - V * V)
    return np.array([gamma * (t - V * x), gamma * (x - V * t), y])


def transformed_line(x0, y0, ux, uy, V, times=(0.13, 0.91)):
    events = [boost_event((t, x0 + ux*t, y0 + uy*t), V) for t in times]
    velocity = (events[1][1:] - events[0][1:]) / (events[1][0] - events[0][0])
    intercept = events[0][1:] - velocity * events[0][0]
    return intercept, velocity


def audit_q2():
    ux, uy, V = s.symbols('ux uy V', real=True)
    numerator = (ux-V)*(-ux-V) - uy**2*(1-V**2)
    symbolic('Q2 直角分子逐项展开', numerator - (V**2*(1+uy**2)-ux**2-uy**2))
    for speed in np.linspace(0.07, 0.93, 9):
        for angle in np.linspace(0.11, math.pi-0.11, 9):
            u = np.array([speed*math.cos(angle), speed*math.sin(angle)])
            for sign in [-1, 1]:
                v = sign*speed/math.sqrt(1+u[1]**2)
                _, a = transformed_line(0, 0, *u, v)
                _, b = transformed_line(1, 0, *(-u), v)
                numeric('Q2 事件变换独立检验直角', np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)), 2e-12)
                assert np.linalg.norm(a) > 0 and np.linalg.norm(b) > 0
                assert np.linalg.norm(a) < 1 and np.linalg.norm(b) < 1
                # 初始位置、取样时刻均不同，排除 a-a 形式的自证。
                _, same = transformed_line(1, 0.4, *u, v, times=(0.22, 1.37))
                numeric('Q2 同向分支在独立事件取样后仍同速', np.linalg.norm(a-same), 3e-12)
    d, speed = 1.7, 0.6
    V = speed/math.sqrt(1+speed**2)
    a0, a = transformed_line(0, 0, 0, speed, V)
    b0, b = transformed_line(d, 0, 0, -speed, V)
    times = np.linalg.solve(np.column_stack([a,-b]), b0-a0)
    numeric('Q2 两次经过交点具有不同时间', times[1]-times[0]-d/speed, 2e-12)
    assert abs(times[1]-times[0]) > 1


def audit_q3():
    a, x, m, g, r = s.symbols('a x m g r', positive=True)
    cf = a/s.sqrt(3)
    y = s.sqrt(s.Rational(2,3)*(a*a-x*x))
    d1, d2 = a+x/s.sqrt(3), a-x/s.sqrt(3)
    symbolic('Q3 左段焦距恒等式', d1*d1-(cf+x)**2-y*y)
    symbolic('Q3 右段焦距恒等式', d2*d2-(cf-x)**2-y*y)
    t1, t2 = m*g*d1*(cf-x)/(2*cf*y), m*g*d2*(cf+x)/(2*cf*y)
    symbolic('Q3 水平平衡回代', -t1*(cf+x)/d1+t2*(cf-x)/d2)
    symbolic('Q3 竖直平衡回代', t1*y/d1+t2*y/d2-m*g)
    symbolic('Q3 转矩化简', r*(t1-t2)+2*m*g*r*x/s.sqrt(2*(a*a-x*x)))
    cf = 1/math.sqrt(3)
    for x in np.linspace(-0.97*cf, 0.97*cf, 101):
        p = np.array([x, -math.sqrt(2*(1-x*x)/3)])
        left, right = np.array([-cf,0])-p, np.array([cf,0])-p
        d1, d2 = np.linalg.norm(left), np.linalg.norm(right)
        e1, e2 = left/d1, right/d2
        tensions = np.linalg.solve(np.column_stack([e1,e2]), np.array([0.,1.]))
        assert min(tensions) > 0
        expected = np.array([d1*(cf-x), d2*(cf+x)])/(2*cf*(-p[1]))
        numeric('Q3 独立受力矩阵求两张力', np.linalg.norm(tensions-expected), 3e-13)
        incoming, outgoing = -e1, e2
        cross = incoming[0]*outgoing[1]-incoming[1]*outgoing[0]
        phi = math.atan2(cross, np.dot(incoming,outgoing))
        angular_formula = math.acos((cf+x)/d1)+math.acos((cf-x)/d2)
        numeric('Q3 实际切线转向角检验包角', phi-angular_formula, 4e-13)
        numeric('Q3 张力差转矩检验', tensions[1]-tensions[0]-2*x/math.sqrt(2*(1-x*x)), 4e-13)
        if abs(x) > 0.01:
            mu = abs(math.log(tensions[1]/tensions[0]))/phi
            low, high = min(tensions), max(tensions)
            ode = solve_ivp(lambda theta,T:[mu*T[0]], [0,phi], [low], method='DOP853', rtol=1e-12, atol=1e-13)
            assert ode.success
            numeric('Q3 接触微元ODE独立积分张力比', ode.y[0,-1]-high, 3e-10)
    x = .3
    y = math.sqrt(2*(1-x*x)/3)
    tensions = np.linalg.solve(np.array([[-(cf+x)/(1+x/math.sqrt(3)), (cf-x)/(1-x/math.sqrt(3))],
                                       [y/(1+x/math.sqrt(3)), y/(1-x/math.sqrt(3))]]), [0.,1.])
    phi = math.acos((cf+x)/(1+x/math.sqrt(3)))+math.acos((cf-x)/(1-x/math.sqrt(3)))
    numeric('Q3 印刷数值0.410126819核验', math.log(tensions[1]/tensions[0])/phi-.410126819, 1e-9)


def audit_q8():
    m, q, k, B, J, r = s.symbols('m q k B J r', nonzero=True)
    E = (J+q*B*r*r/2)**2/(2*m*r*r)-k/r
    expanded = J**2/(2*m*r*r)+q*B*J/(2*m)+q*q*B*B*r*r/(8*m)-k/r
    symbolic('Q8 动能平方展开及线性能量项', E-expanded)
    symbolic('Q8 圆轨道极值方程', s.diff(E,r)*m*r**3-(-J**2+q*q*B*B*r**4/4+m*k*r))
    numeric('Q8 线性能量随半径的导数为零', s.diff(q*B*J/(2*m),r), 1e-15)
    # 无量纲 m=q=k=1，以笛卡尔洛伦兹ODE核验有向角动量，而非代回 J 的导数。
    for B in [-.23, .17]:
        for direction in [-1,1]:
            def force(t, z):
                x,y,vx,vy = z
                norm = math.hypot(x,y)
                return [vx,vy,-x/norm**3-B*vy,-y/norm**3+B*vx]
            result = solve_ivp(force, [0,12], [.9,0,.11,direction*.91], t_eval=np.linspace(0,12,241),
                               method='DOP853', rtol=5e-13, atol=1e-13)
            assert result.success
            x,y,vx,vy = result.y
            invariant = x*vy-y*vx-B*(x*x+y*y)/2
            energy = (vx*vx+vy*vy)/2-1/np.hypot(x,y)
            numeric('Q8 独立洛伦兹ODE有向J守恒', np.max(np.abs(invariant-invariant[0])), 5e-10)
            numeric('Q8 独立洛伦兹ODE机械能守恒', np.max(np.abs(energy-energy[0])), 1e-9)
    for n in [1,2,3]:
        rn = n*n
        for epsilon in [.003,.006,.012]:
            field = 2*epsilon/n**3
            energies = []
            for B in [-field,field]:
                radius = brentq(lambda z:n*n-z-B*B*z**4/4, rn/3,rn,xtol=1e-14)
                velocity = (n+B*radius*radius/2)/radius
                direct_energy = velocity*velocity/2-1/radius
                energies.append(direct_energy)
                numeric('Q8 正半径根的二阶尺度', radius/rn-(1-epsilon*epsilon), 6*epsilon**4)
            numeric('Q8 正负场直接动能差的一阶系数', (energies[1]-energies[0])/(2*field)-n/2, 2e-10)
    # 题给圆整常数：通过周期、电流、圆电流中心场依次计算。
    mass, charge, K, h = .91e-30, 1.6e-19, 8.99e9, 6.628e-34
    hbar = h/(2*math.pi)
    radius, velocity = hbar*hbar/(mass*K*charge*charge), K*charge*charge/hbar
    period = 2*math.pi*radius/velocity
    current = charge/period
    field = (4*math.pi*1e-7)*current/(2*radius)
    numeric('Q8 核处磁场印刷数值', field-12.36484229, 6e-8)


def audit_files():
    baseline = json.loads((ROOT/'build_report.json').read_text())
    visual = json.loads((ROOT/'preview/full-review/visual-reviewed.json').read_text())
    documents = []
    for row in baseline['documents']:
        pdf = Path(row['path'])
        digest = sha(pdf)
        assert digest == row['sha256']
        with fitz.open(pdf) as doc:
            density = [len(re.sub(r'\s','',page.get_text())) for page in doc][1:]
            statements = {}
            if row['version'] == '试卷':
                for number in [2,3,8]:
                    text = doc[number].get_text()
                    statements[str(number)] = {'explicit_revision_label': '修订' in text}
        documents.append({'version':row['version'],'sha256':digest,'total_pages':len(density)+1,
                          'body_pages':len(density),'pdf_body_nonspace':sum(density),'revision_labels':statements})
    qpdf_paths = sorted(set((ROOT/'figures').glob('*.pdf')) | {Path(r['path']) for r in baseline['documents']})
    for path in qpdf_paths:
        result = subprocess.run(['qpdf','--check',str(path)], capture_output=True, text=True)
        assert result.returncode == 0, (path,result.stderr,result.stdout)
    changed_drafts = [name for name,digest in visual['draft_sha256'].items() if sha(ROOT/'drafts'/name)!=digest]
    assert not changed_drafts, changed_drafts
    source_review = []
    for path in sorted((ROOT/'drafts').glob('question-*.md')):
        text = path.read_text()
        source_review.append({'question':path.stem,'sha256':sha(path),'module_count':len(re.findall(r'^## ',text,re.M)),
                              'explicit_figure_number_mentions':re.findall(r'图\s*[1-8]-[1-5]',re.sub(r'!\[.*?\]\(.*?\)','',text)),
                              'statement_revision_label':'修订' in text.split('<!-- question-end -->')[0]})
    log_findings = {}
    for path in sorted((ROOT/'build').glob('*.log')):
        lines = [line for line in path.read_text(errors='replace').splitlines()
                 if re.search(r'Overfull|Underfull|Missing character|Undefined control sequence|^! |LaTeX Warning',line)]
        if lines: log_findings[path.name] = lines
    return {'documents':documents,'qpdf_checked_count':len(qpdf_paths),'unchanged_drafts':True,
            'source_review':source_review,'log_findings':log_findings,
            'stricter_gate_not_yet_passed':True,
            'pending':['第2、3、8题的条件已进入正文，但试卷题干尚无明确修订标识。',
                       '图文实质融合与图稿可读性仍需逐题复核；图数不能代替融合。',
                       '第013套教师PDF正文44413个去空白提取字符，低于本批既定45411下限，须补真实解释而非扩版。',
                       '本次不宣称完整套卷视觉复审完成，不覆盖另一对话的既有交付。']}


def main():
    audit_q2()
    audit_q3()
    audit_q8()
    report = {'checked_at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
              'scope':'用户确认的第013套第2、3、8题条件及现有成品技术复核；非整套终验。',
              'read_only_formal_deliverables':True,'script_sha256':sha(Path(__file__)),
              'checks':checks,'symbolic_count':sum(x['kind']=='symbolic' for x in checks),
              'numerical_count':sum(x['kind']=='numerical' for x in checks),
              'file_audit':audit_files(),'accepted_as_complete':False}
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    destination = EVIDENCE/'confirmed-revisions-audit.json'
    destination.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'evidence':str(destination),'symbolic':report['symbolic_count'],
                      'numerical':report['numerical_count'],'qpdf':report['file_audit']['qpdf_checked_count'],
                      'formal_files_unchanged':True,'accepted_as_complete':False},ensure_ascii=False))


if __name__ == '__main__':
    main()
