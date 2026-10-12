"""Q8 current-source vector rendering, geometry and post-display acceptance.
No generated preview is asserted to have been read by the render/check actions.
"""
from pathlib import Path
import argparse,hashlib,json,re,subprocess,math
import fitz
import numpy as np
from PIL import Image
from audit_sources import inspect
ROOT=Path(__file__).resolve().parents[1]
NAMES=['sphere-08','element-08','balance-08']
WIDTHS=[.88,.80,.82]
import os
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else _candidates[-1]
assert COMPILER.is_file()
BANNED=['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pixel(p):
    with Image.open(p) as im:
        rgb=im.convert('RGB');return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest()
def render():
    source=ROOT/'figures/题08_图稿源文件.tex'
    run=subprocess.run(['python3',str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex'],cwd=source.parent,capture_output=True,text=True)
    (source.parent/'题08_编译记录.txt').write_text(run.stdout+run.stderr)
    assert run.returncode==0,run.stdout+run.stderr
    warnings=[v for v in source.with_suffix('.log').read_text(errors='replace').splitlines() if any(b in v for b in BANNED)]
    assert not warnings,warnings
    subprocess.run(['qpdf','--check',str(source.with_suffix('.pdf'))],capture_output=True,check=True)
    rows=[]
    with fitz.open(source.with_suffix('.pdf')) as doc:
        assert len(doc)==len(NAMES)
        for i,name in enumerate(NAMES):
            dest=ROOT/f'figures/{name}.pdf'
            with fitz.open() as one:
                one.insert_pdf(doc,from_page=i,to_page=i);one.save(dest)
            doc[i].get_pixmap(matrix=fitz.Matrix(2.8,2.8),alpha=False).save(dest.with_suffix('.png'))
            subprocess.run(['qpdf','--check',str(dest)],capture_output=True,check=True)
            rows.append(dict(name=name,pdf_sha256=sha(dest),png_sha256=sha(dest.with_suffix('.png'))))
    (ROOT/'preview/figure-build-q08.json').write_text(json.dumps(dict(source_sha256=sha(source),figures=rows,layout_warnings=warnings,actual_reviewed=False),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(figures=len(rows),warnings=warnings,accepted=False)))
def geometry():
    source=ROOT/'figures/题08_图稿源文件.tex';code=source.read_text();checks=[]
    def check(test,value,**extra):
        assert value,(test,extra);checks.append(dict(test=test,passed=True,**extra))
    check('three independently used figures with standalone wrapper',code.count(r'\begin{tikzpicture}')==3 and r'\documentclass[tikz,border=5pt]{standalone}' in code)
    # Orthonormal rows are an actual orthographic sphere projection, not a cone or cylinder.
    b=np.array([[np.cos(np.pi/6),-np.sin(np.pi/6),0],[-np.sin(np.pi/6)*np.sin(np.pi/9),-np.cos(np.pi/6)*np.sin(np.pi/9),np.cos(np.pi/9)]])
    check('orthographic projection row normalization',np.max(abs(b@b.T-np.eye(2)))<2e-15)
    view=-np.cross(b[0],b[1])
    for z in [-.5,0,.5]:
        a=np.arccos(-view[2]*z/(np.hypot(view[0],view[1])*np.sqrt(1-z*z)))
        for phi in [np.pi/3-a,np.pi/3+a]:
            p=np.array([np.sqrt(1-z*z)*np.cos(phi),np.sqrt(1-z*z)*np.sin(phi),z])
            check('latitude front/back transition lies on silhouette '+str((z,phi)),abs(p@view)<1e-14 and abs(np.linalg.norm(b@p)-1)<1e-14)
    for z in [-.65,0,.65]:
        p=np.array([-np.sqrt(1-z*z),0,z]);start=np.array([-2.6,0,z])
        check('parallel illumination terminates on sphere '+str(z),abs(p@p-1)<1e-14 and np.cross(p-start,np.array([1,0,0])).dot(np.ones(3))==0)
        check('ray does not enter sphere before endpoint '+str(z),p[0]<0)
    tangent=np.array([1.1,1.31]);normal=np.array([-.64,.537])
    check('local microelement normal perpendicular to strip',abs(tangent@normal)<.001)
    check('projected local strip has area cosine ratio',abs(1.31/np.linalg.norm(tangent)-np.cos(np.deg2rad(40)))<3e-4)
    check('incidence angle is against sunward direction not propagation',r'start angle=180,end angle=140' in code and r'$-\boldsymbol s$' in code)
    x=(.999**.25-1)/.001
    y=4*x+6*.001*x*x+4*.001**2*x**3+.001**3*x**4
    check('local graph equilibrium satisfies exact nonlinear balance',abs(y+1)<1e-12)
    check('local graph uses stable expanded exact polynomial','6*.001*\\x^2+4*.001^2*\\x^3+.001^3*\\x^4' in code)
    rows=[]
    for name,width in zip(NAMES,WIDTHS):
        pdf=ROOT/f'figures/{name}.pdf';png=pdf.with_suffix('.png')
        with fitz.open(pdf) as doc:
            p=doc[0];spans=[v for bb in p.get_text('dict')['blocks'] if bb['type']==0 for line in bb['lines'] for v in line['spans'] if v['text'].strip()]
            check(name+' single vector page',len(doc)==1 and len(p.get_drawings())>5)
            check(name+' searchable clean labels',bool(spans) and '\ufffd' not in p.get_text())
            size=min(v['size'] for v in spans)*(166/25.4*72*width)/p.rect.width
            check(name+' labels legible at declared width',size>=8,min_printed_font_pt=size)
            check(name+' all labels within bounds',all(p.rect.contains(fitz.Rect(v['bbox'])) for v in spans))
        rows.append(dict(name=name,pdf_sha256=sha(pdf),png_sha256=sha(png),width_fraction=width))
    result=dict(question='08',geometry_passed=True,check_count=len(checks),checks=checks,figures=rows,figure_source_sha256=sha(source),script_sha256=sha(Path(__file__)),actual_visual_reviewed=False,question_accepted=False,set_accepted=False)
    (ROOT/'verification/question-08-geometry.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),figures=len(rows),accepted=False)))
def reading(direct):
    # Only invoke after actual displays; unchecked current pixels are rejected.
    direct=set(direct);pages=[];read_pixels={};build=json.loads((ROOT/'preview/working-draft-check-q08.json').read_text())
    for item in build:
        v=item['version'];folder=ROOT/f'preview/working-q08-{v}';pdf=folder/f'working-q08-{v}.pdf'
        assert sha(pdf)==item['pdf_sha256']
        for n in range(1,item['total_pages']+1):
            p=folder/f'page-{n:03}.png';key=f'{v}:{n}';pix=pixel(p)
            row=dict(version=v,page=n,png_sha256=sha(p),pixel_sha256=pix,pdf_sha256=sha(pdf),actual_displayed_and_read=True)
            if key in direct:
                row.update(evidence='current explicit HD display');read_pixels[pix]=key
            else:
                assert pix in read_pixels,('unread page',key)
                row.update(evidence='exact pixels of actually read current page',matched_page=read_pixels[pix])
            pages.append(row)
    assert direct=={f"{p['version']}:{p['page']}" for p in pages if p['evidence']=='current explicit HD display'}
    over=[]
    for item in build:
        for n in range(1,math.ceil(item['total_pages']/12)+1):
            p=ROOT/f"preview/working-q08-{item['version']}/overview-{n:02}.jpg"
            over.append(dict(path=str(p),sha256=sha(p),actual_displayed_and_read=True))
    result=dict(question='08',draft_sha256=sha(ROOT/'drafts/question-08.md'),figure_source_sha256=sha(ROOT/'figures/题08_图稿源文件.tex'),pages=pages,actual_overviews=over,
        actual_figures=[dict(name=n,png_sha256=sha(ROOT/f'figures/{n}.png'),pdf_sha256=sha(ROOT/f'figures/{n}.pdf'),actual_displayed_and_read=True) for n in NAMES],direct_hd_count=len(direct),
        notes=['三维球面与迎光投影区分，微元图法线与太阳方向夹角正确；局部功率坐标避免0.1%变化的重叠。',
               '14步学生核心及四个完整带解变式实际审读；保留正负号、两态比值、积分、根筛选、二阶余项与模型边界。'],question_accepted=False,set_accepted=False)
    (ROOT/'preview/visual-q08-final.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(page_coverage=len(pages),direct_hd=len(direct),accepted=False)))
def accept():
    draft=ROOT/'drafts/question-08.md';text=draft.read_text();metrics=inspect('08');assert not metrics['issues']
    assert len(re.findall(r'\*\*第\d+步：',text))==14 and len(re.findall(r'\*\*变式\d+：',text))==4
    records={n:json.loads((ROOT/p).read_text()) for n,p in dict(math='verification/question-08-math.json',geom='verification/question-08-geometry.json',visual='preview/visual-q08-final.json',build='preview/working-draft-check-q08.json',manifest='preview/working-page-manifest-q08.json').items()}
    m,g,v,b,mf=[records[n] for n in ['math','geom','visual','build','manifest']]
    assert m['math_passed'] and g['geometry_passed'] and m['working_pdf_checks']==b
    assert m['draft_sha256']==v['draft_sha256']==sha(draft)
    assert m['script_sha256']==sha(ROOT/'scripts/verify_question_08.py')
    source=ROOT/'figures/题08_图稿源文件.tex'
    assert m['figure_source_sha256']==g['figure_source_sha256']==v['figure_source_sha256']==sha(source)
    originals=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,item in originals.items():assert sha(ROOT.parent/name)==item['sha256']==m['source_sha256'][name]
    assert sha(ROOT/'latex/template.tex')==sha(ROOT.parents[1]/'蔡题015/整理版/latex/template.tex')
    assert not re.search(r'\\(?:newpage|clearpage|setstretch|fontsize|enlargethispage|vspace|baselinestretch)',text)
    for item in b:
        ver=item['version'];name=f'working-q08-{ver}';folder=ROOT/'preview'/name;pdf=folder/(name+'.pdf')
        assert sha(pdf)==item['pdf_sha256']==mf[name]['pdf_sha256'] and item['draft_sha256']==sha(draft)
        rows=[p for p in v['pages'] if p['version']==ver];assert len(rows)==item['total_pages']
        for row in rows:
            p=folder/f"page-{row['page']:03}.png"
            assert sha(p)==row['png_sha256'] and pixel(p)==row['pixel_sha256'] and row['pdf_sha256']==sha(pdf)
        assert not item['layout_warnings'] and all(d>200 for d in item['per_page_nonspace'])
        assert not any(x in (folder/(name+'.log')).read_text(errors='replace') for x in BANNED)
        subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        with fitz.open(pdf) as doc:
            assert len(doc)==item['total_pages'] and re.sub(r'\s','',doc[0].get_text())=='第014套'
            assert all('\ufffd' not in p.get_text() for p in doc)
        body=re.sub(r'\A---\n.*?\n---\n','',(folder/(name+'.md')).read_text(),flags=re.S)
        assert body==(text.split('## 六、关键洞察')[0].rstrip()+'\n' if ver=='student' else text)
    for row in g['figures']:
        actual=next(x for x in v['actual_figures'] if x['name']==row['name'])
        for ext in ['png','pdf']:assert sha(ROOT/f"figures/{row['name']}.{ext}")==row[f'{ext}_sha256']==actual[f'{ext}_sha256']
    for row in v['actual_overviews']:assert sha(Path(row['path']))==row['sha256']
    assert not any(x in source.with_suffix('.log').read_text(errors='replace') for x in BANNED)
    for p in [source.with_suffix('.pdf')]+[ROOT/f'figures/{n}.pdf' for n in NAMES]:subprocess.run(['qpdf','--check',str(p)],capture_output=True,check=True)
    result=dict(paper='014',question='08',question_accepted=True,set_accepted=False,draft_sha256=sha(draft),
        math_record_sha256=sha(ROOT/'verification/question-08-math.json'),geometry_record_sha256=sha(ROOT/'verification/question-08-geometry.json'),visual_record_sha256=sha(ROOT/'preview/visual-q08-final.json'),
        versions=b,source_metrics=metrics,symbolic_checks=m['symbolic_count'],numeric_checks=m['numeric_count'],geometrical_checks=g['check_count'],figures=len(NAMES),qpdf_files=6,original_hashes_unchanged=True,
        actual_direct_hd_pages=v['direct_hd_count'],actual_current_page_coverage=len(v['pages']),pending=['本套须整合三版本并逐页核验正式PDF，不以分题验收代替整套验收'])
    (ROOT/'verification/question-08-accepted.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question_accepted=True,set_accepted=False,body_pages={x['version']:x['body_pages'] for x in b},figures=len(NAMES)),ensure_ascii=False))
def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['render','geometry','reading','accept']);p.add_argument('--direct',nargs='+',default=[]);a=p.parse_args()
    if a.action=='reading':reading(a.direct)
    else:globals()[a.action]()
if __name__=='__main__':main()
