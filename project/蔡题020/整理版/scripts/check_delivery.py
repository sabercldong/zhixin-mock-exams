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
        for rel,digest in report['source_sha256'].items():
            assert sha(ROOT/rel)==digest,('stale_math_evidence',rel)
    teacher=(ROOT/'markdown/蔡题020_教师备课.md').read_text()
    student=(ROOT/'markdown/蔡题020_学生详解.md').read_text()
    paper=(ROOT/'markdown/蔡题020_试卷.md').read_text()
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
    compiled=json.loads((ROOT/'build/pdf-build-manifest.json').read_text())
    documents=[]
    for item,kind in zip(compiled['documents'],['paper','student','teacher']):
        path=Path(item['path']);digest=sha(path)
        assert digest==item['pdf_sha256']==visual[kind]['pdf_sha256']==sha(ROOT/'build'/path.name)
        subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
        with fitz.open(path) as doc:assert visual[kind]['overview_page_range']==[1,len(doc)]
        log=(ROOT/'build'/path.with_suffix('.log').name).read_text(errors='replace')
        assert not any(tag in log for tag in ['Overfull','Missing character','Undefined control sequence','! '])
        documents.append({k:item[k] for k in ['version','total_pages','body_pages','pdf_extracted_body_nonspace','source_metrics','pdf_sha256','path']})
    all_figure_pdfs=list((ROOT/'figures').glob('*.pdf'))
    figures=[p for p in all_figure_pdfs if not p.stem.startswith('题')];assert len(figures)==38
    for path in all_figure_pdfs:subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
    original=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,item in original.items():assert sha(ROOT.parent/name)==item['sha256']
    template=(ROOT/'latex/template.tex').read_text()
    for required in ['12pt,a4paper','top=22mm,bottom=22mm,left=22mm,right=22mm',r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}']:assert required in template
    approval=json.loads((ROOT/'build/question-03-条件确认.json').read_text())
    assert approval['approved'] and approval['document_revision_implemented']
    assert json.loads((ROOT/'build/verification-q03.json').read_text())['model_condition_resolved']
    assert visual.get('model_revision_current_evidence',{}).get('actual_reviewed')
    assert visual['model_revision_current_evidence']['approval_sha256']==sha(ROOT/'build/question-03-条件确认.json')
    result=dict(technical_checks_passed=True,actual_visual_review=True,set_accepted=not visual['unresolved'],
                unresolved=visual['unresolved'],figures=len(figures),question_count=8,
                student_core_identical_to_teacher=True,originals_unchanged=True,documents=documents)
    (ROOT/'build/delivery-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
