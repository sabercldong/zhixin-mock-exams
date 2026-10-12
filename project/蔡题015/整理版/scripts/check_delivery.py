"""验收当前正式成品：独立计算、源稿、逐页视觉证据及文件校验和必须一致。"""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from audit_sources import inspect,MODULES,metrics,BANNED
from prepare_documents import normalize_boundaries
ROOT=Path(__file__).resolve().parents[1]
TEMPLATE_SHA='434e4734708ef9c12c4be4629709e370fa5fe9a67a4cc88709ee13ffa571673b'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def chunks(text):
    parts=re.split(r'(?m)^# 第(\d+)题\n',text)[1:]
    assert parts[::2]==list(map(str,range(1,9)))
    return [re.sub(r'(?m)^\\newpage\s*$','',parts[i+1]).strip() for i in range(0,len(parts),2)]
def main():
    visual=json.loads((ROOT/'preview/visual-reviewed-full.json').read_text())
    assert visual['actual_reviewed'] and not visual['unresolved']
    ledger_path=ROOT/'preview/full-actual-reading-ledger.json'
    assert sha(ledger_path)==visual['manual_ledger_sha256']
    ledger=json.loads(ledger_path.read_text())
    assert ledger['actual_reading_attested']
    for item in ledger['overviews']+ledger['direct_hd_pages']:
        assert sha(ROOT/item['path'])==item['sha256']
    assert len(ledger['overviews'])==28
    for kind in ['paper','student','teacher']:
        direct={x['page'] for x in ledger['direct_hd_pages'] if x['variant']==kind}
        assert direct==set(visual[kind]['direct_final_high_resolution_pages_reviewed'])
    assert set(range(2,10))<=set(visual['paper']['direct_final_high_resolution_pages_reviewed'])
    # The final full-page overviews are read directly. Reuse a previous HD
    # review only for an exactly matching current body raster, not similar text.
    subprocess.run(['python3',str(ROOT/'scripts/compare_final_working_bodies.py')],capture_output=True,check=True)
    comparison_path=ROOT/'build/final-working-body-comparison.json'
    assert visual['body_comparison_sha256']==sha(comparison_path)
    comparison=json.loads(comparison_path.read_text())
    for kind in ['student','teacher']:
        row=comparison['versions'][kind]
        assert row['pdf_sha256']==visual[kind]['pdf_sha256']
        assert {x['page'] for x in row['exact_reviewed_working_body_matches'] if x['page']>1}==set(range(2,row['total_pages']+1))
        assert visual[kind]['exact_reviewed_working_body_pages']==list(range(2,row['total_pages']+1))
    qa=[]
    for q in range(1,9):
        key=f'{q:02}';row=inspect(key);assert not row['issues'];qa.append(row)
        report=json.loads((ROOT/f'build/question-{key}-verification.json').read_text())
        assert report['verified_math'] and report.get('document_complete', report.get('document_contains_all_three_parts', False))
        assert report.get('model_condition_resolved',True)
        assert not report.get('unresolved_critical_condition')
        for item in report['bound_files'].values():
            assert sha(Path(item['path']))==item['sha256'],('stale_math_source',item['path'])
        assert sha(ROOT/f'build/question-{key}-verification.json')==visual['verification_sha256'][key]
        assert sha(ROOT/f'preview/visual-reviewed-q{key}.json')==visual['question_review_sha256'][key]
        assert sha(ROOT/f'build/source-quality-q{key}.json')==visual['source_quality_sha256'][key]
    subprocess.run(['python3',str(ROOT/'scripts/check_saved_reviews.py')],capture_output=True,check=True)
    labels=[('paper','试卷'),('student','学生详解'),('teacher','教师备课')]
    texts={kind:(ROOT/'markdown'/f'蔡题015_{version}.md').read_text() for kind,version in labels}
    for text in texts.values():
        assert text.count(r'\newpage')==7
        assert not any(term in text for term in BANNED+['不把未求解的额外问题塞入','继续下一题'])
        assert not re.search(r'\\(?:linespread|setstretch|fontsize|vspace|enlargethispage)\b',text)
        for match in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)',text):
            assert (ROOT/'markdown'/match.group(1)).is_file(),match.group(1)
    tc,sc,pc=map(chunks,[texts['teacher'],texts['student'],texts['paper']])
    for q,(t,s,p) in enumerate(zip(tc,sc,pc),1):
        retained=normalize_boundaries((ROOT/f'drafts/question-{q:02}.md').read_text().rstrip().lstrip())
        assert retained.split('\n',1)[1].strip()==t,('retained_draft_content_mismatch',q)
        assert t.split('## 六、关键洞察')[0].strip()==s
        assert re.findall(r'(?m)^## (.*)$',s)==MODULES[:5]
        assert re.findall(r'(?m)^## (.*)$',t)==MODULES
        expected=re.search(r'<!-- question-start -->(.*?)<!-- question-end -->',t,re.S).group(1).strip()
        assert expected==p,('question_text_mismatch',q)
    compiled=json.loads((ROOT/'build/pdf-build-manifest.json').read_text())
    documents=[]
    for item,(kind,version) in zip(compiled['documents'],labels):
        path=Path(item['path']);record=visual[kind];digest=sha(path)
        assert digest==item['pdf_sha256']==record['pdf_sha256']==sha(ROOT/'build'/path.name)
        assert record['source_sha256']==sha(ROOT/'markdown'/f'蔡题015_{version}.md')
        subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
        with fitz.open(path) as doc:
            count=len(doc);assert record['overview_page_range']==[1,count]
            assert set(record['page_png_sha256'])=={f'page-{p:03}.png' for p in range(1,count+1)}
            assert set(record['overview_sha256'])=={f'overview-{i:02}.jpg' for i in range(1,(count+11)//12+1)}
            assert record['overview_pages_reviewed']==list(range(1,count+1))
            assert all(1<=p<=count for p in record['high_resolution_pages_reviewed'])
            assert all(len(re.sub(r'\s','',p.get_text()))>20 for p in list(doc)[1:])
            extracted='\n'.join(p.get_text() for p in doc)
            assert '\ufffd' not in extracted and not any(term in extracted for term in BANNED)
            for page in item['low_density_pages']:
                if kind=='paper':
                    assert count==9 and record['all_question_pages_high_resolution_reviewed']
                else:
                    note=visual['density_exceptions'][kind][str(page)]
                    assert page in record['high_resolution_pages_reviewed']
                    assert note['png_sha256']==record['page_png_sha256'][f'page-{page:03}.png']
                    assert note['actual_checked'] and len(doc[page-1].get_xobjects())>0
            if kind=='student':
                assert count-1>=56 and item['pdf_extracted_body_nonspace']>=31218
            if kind=='teacher':
                assert count-1>=71 and item['pdf_extracted_body_nonspace']>=45411
        folder=ROOT/'preview'/f'full-{kind}'
        for mapping in ['page_png_sha256','overview_sha256']:
            for name,digest in record[mapping].items():assert sha(folder/name)==digest,(kind,name)
        assert not item['layout_errors']
        log=(ROOT/'build'/path.with_suffix('.log').name).read_text(errors='replace')
        assert not any(tag in log for tag in ['Warning','Underfull','Overfull','Missing character','Undefined control sequence','! '])
        documents.append({k:item[k] for k in ['version','total_pages','body_pages','pdf_extracted_body_nonspace','source_metrics','pdf_sha256','path']})
    figures=list((ROOT/'figures').glob('*.pdf'))
    singles=[p for p in figures if not p.stem.startswith('题')]
    assert len(singles)==49 and len(figures)==57
    assert {p.stem:sha(p) for p in singles}==visual['figures_sha256']
    for path in figures:subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
    for log in (ROOT/'figures').glob('题*_图稿源文件.log'):
        assert not re.search(r'Warning|Underfull|Overfull|Missing character|^!',log.read_text(),re.M),str(log)
    originals=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,item in originals.items():assert sha(ROOT.parent/name)==item['sha256']
    assert sha(ROOT/'latex/template.tex')==TEMPLATE_SHA==visual['template_sha256']
    template=(ROOT/'latex/template.tex').read_text()
    for param in ['12pt,a4paper','top=22mm,bottom=22mm,left=22mm,right=22mm',r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}']:
        assert param in template
    benchmark=visual['benchmark101']
    reference_template=Path(benchmark['学生详解']['markdown_path']).parents[1]/'latex/template.tex'
    reference_template_text=reference_template.read_text()
    for param in ['12pt,a4paper','top=22mm,bottom=22mm,left=22mm,right=22mm',r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}']:
        assert param in reference_template_text
    for version,kind in [('学生详解','student'),('教师备课','teacher')]:
        ref=benchmark[version]
        assert sha(Path(ref['markdown_path']))==ref['markdown_sha256']
        assert sha(Path(ref['pdf_path']))==ref['pdf_sha256']
        assert metrics(texts[kind])['body_net_characters']>=ref['source_metrics']['body_net_characters']
    result=dict(technical_checks_passed=True,actual_visual_review=True,set_accepted=True,unresolved=[],
        figures=49,figure_pdf_collections=8,qpdf_checked_files=60,question_count=8,
        student_core_identical_to_teacher=True,originals_unchanged=True,
        template_identical_to101=sha(ROOT/'latex/template.tex')==sha(reference_template),
        main_typesetting_parameters_match101=True,benchmark101_template_sha256=sha(reference_template),
        visual_record_sha256=sha(ROOT/'preview/visual-reviewed-full.json'),documents=documents,
        final_body_review_reuse_verified=True,body_comparison_sha256=sha(comparison_path),
        per_question_depth=qa,benchmark101=benchmark,density_exceptions=visual['density_exceptions'])
    (ROOT/'build/delivery-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    # Build tools deliberately create an unaccepted candidate. Once the
    # separate actual-review and current-hash checks pass, remove stale pending
    # labels without changing any PDF, Markdown or question-level evidence.
    for name in ['pdf-build-manifest.json','document-source-manifest.json']:
        manifest_path=ROOT/'build'/name
        manifest=json.loads(manifest_path.read_text())
        manifest['accepted']=True
        manifest['actual_visual_review']=True
        manifest['pending']=[]
        manifest['acceptance_report']='build/delivery-check.json'
        manifest['acceptance_report_sha256']=sha(ROOT/'build/delivery-check.json')
        manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
