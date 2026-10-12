"""验证当前三版本与审读证据一致；技术通过不等于未决条件已解决。"""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from audit_sources import inspect,MODULES,metrics
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    issues=[]
    for q in range(1,9):
        assert not inspect(f'{q:02}')['issues']
        report=json.loads((ROOT/f'build/verification-q{q:02}.json').read_text())
        assert report['verified_math'] and report['document_complete']
        assert not report.get('unresolved_critical_condition')
        for rel,digest in report['source_sha256'].items():
            assert sha(ROOT/rel)==digest,('stale_math_evidence',rel)
    teacher=(ROOT/'markdown/蔡题018_教师备课.md').read_text()
    student=(ROOT/'markdown/蔡题018_学生详解.md').read_text()
    paper=(ROOT/'markdown/蔡题018_试卷.md').read_text()
    def chunks(text):
        parts=re.split(r'(?m)^# 第(\d+)题\n',text)[1:]
        return [re.sub(r'(?m)^\\newpage\s*$','',parts[i+1]).strip() for i in range(0,len(parts),2)]
    for texts in [teacher,student,paper]:assert texts.count(r'\newpage')==7
    tc,sc,pc=map(chunks,[teacher,student,paper]);assert len(tc)==len(sc)==len(pc)==8
    for t,s,p in zip(tc,sc,pc):
        assert t.split('## 六、关键洞察')[0].strip()==s
        assert re.findall(r'(?m)^## (.*)$',s)==MODULES[:5]
        assert re.findall(r'(?m)^## (.*)$',t)==MODULES
        assert re.search(r'<!-- question-start -->(.*?)<!-- question-end -->',t,re.S).group(1).strip()==p
    visual=json.loads((ROOT/'preview/visual-reviewed-full.json').read_text());assert visual['actual_reviewed']
    assert set(visual['verification_sha256'])=={f'{q:02}' for q in range(1,9)}
    assert set(visual['question_review_sha256'])=={f'{q:02}' for q in range(1,9)}
    for q in range(1,9):
        key=f'{q:02}'
        assert sha(ROOT/f'build/verification-q{key}.json')==visual['verification_sha256'][key]
        assert sha(ROOT/f'preview/visual-reviewed-q{key}.json')==visual['question_review_sha256'][key]
    compiled=json.loads((ROOT/'build/pdf-build-manifest.json').read_text())
    documents=[]
    for item,kind in zip(compiled['documents'],['paper','student','teacher']):
        path=Path(item['path']);digest=sha(path)
        assert digest==item['pdf_sha256']==visual[kind]['pdf_sha256']==sha(ROOT/'build'/path.name)
        subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
        for rel,page_digest in visual[kind].get('page_png_sha256',{}).items():
            assert sha(ROOT/'preview'/f'full-{kind}'/rel)==page_digest
        assert sha(ROOT/'markdown'/f'蔡题018_{item["version"]}.md')==visual[kind]['source_sha256']
        with fitz.open(path) as doc:
            assert visual[kind]['overview_page_range']==[1,len(doc)]
            assert set(visual[kind]['page_png_sha256'])=={f'page-{p:03}.png' for p in range(1,len(doc)+1)}
            assert all(1<=p<=len(doc) for p in visual[kind]['high_resolution_pages_reviewed'])
        assert not item['low_density_pages'] and not item['layout_errors']
        if kind=='student':assert item['body_pages']>=56
        if kind=='teacher':assert item['body_pages']>=71
        log=(ROOT/'build'/path.with_suffix('.log').name).read_text(errors='replace')
        assert not any(tag in log for tag in ['Overfull','Missing character','Undefined control sequence','! '])
        documents.append({k:item[k] for k in ['version','total_pages','body_pages','pdf_extracted_body_nonspace','source_metrics','pdf_sha256','path']})
    all_figure_pdfs=list((ROOT/'figures').glob('*.pdf'))
    figures=[p for p in all_figure_pdfs if not p.stem.startswith('题')];assert len(figures)==41
    assert {p.stem:sha(p) for p in figures}==visual['figures_sha256']
    for path in all_figure_pdfs:subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
    transition=visual['final_change']
    baseline=json.loads((ROOT/transition['baseline_record']).read_text())
    assert baseline['actual_reviewed']
    unchanged=0
    for kind in ['paper','student','teacher']:
        older=baseline[kind]['page_png_sha256'];newer=visual[kind]['page_png_sha256']
        assert set(older)==set(newer)
        changed=[name for name in sorted(newer) if older[name]!=newer[name]]
        assert changed==transition['changed_pages'][kind]
        assert all(int(name[5:8]) in transition['current_high_resolution_rechecked'].get(kind,[]) for name in changed)
        unchanged+=len(newer)-len(changed)
        assert sha(ROOT/baseline[kind]['pdf_backup'])==baseline[kind]['pdf_sha256']
    assert unchanged==transition['unchanged_pixel_pages']
    original=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,item in original.items():assert sha(ROOT.parent/name)==item['sha256']
    template=(ROOT/'latex/template.tex').read_text()
    assert sha(ROOT/'latex/template.tex')=='434e4734708ef9c12c4be4629709e370fa5fe9a67a4cc88709ee13ffa571673b'
    for required in ['12pt,a4paper','top=22mm,bottom=22mm,left=22mm,right=22mm',r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}']:assert required in template
    result=dict(technical_checks_passed=True,actual_visual_review=True,set_accepted=not visual['unresolved'],
                unresolved=visual['unresolved'],figures=len(figures),question_count=8,
                student_core_identical_to_teacher=True,originals_unchanged=True,
                visual_record_sha256=sha(ROOT/'preview/visual-reviewed-full.json'),documents=documents)
    (ROOT/'build/delivery-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
