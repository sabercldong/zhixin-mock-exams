"""Bind whole-set review only to an explicit actual-reading ledger and exact-pixel proofs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def main():
    ledger_path=ROOT/'preview/full-actual-reading-ledger.json'
    ledger=read(ledger_path)
    assert ledger['actual_reading_attested']
    comparison_path=ROOT/'build/final-working-body-comparison.json'
    comparison=read(comparison_path)
    overviews={x['path']:x['sha256'] for x in ledger['overviews']}
    assert len(overviews)==28
    direct={x['path']:x for x in ledger['direct_hd_pages']}
    for x in ledger['overviews']+ledger['direct_hd_pages']:
        assert sha(ROOT/x['path'])==x['sha256']
    prior=read(ROOT.parents[1]/'蔡题016/整理版/preview/visual-reviewed-full.json')
    result=dict(paper='015',actual_reviewed=True,review_saved_utc=datetime.now(timezone.utc).isoformat(),
        scope='Current whole PDF page overview reading; exact current reviewed working-body pixel reuse plus direct HD reading',
        unresolved=[],set_accepted=False,manual_ledger_sha256=sha(ledger_path),
        body_comparison_sha256=sha(comparison_path),benchmark101=prior['benchmark101'],
        template_sha256=sha(ROOT/'latex/template.tex'),reader_notes=ledger['notes'],
        verification_sha256={},question_review_sha256={},source_quality_sha256={},
        figures_sha256={},density_exceptions={})
    for q in range(1,9):
        k=f'{q:02}'
        review=read(ROOT/f'preview/visual-reviewed-q{k}.json')
        assert review['question_accepted'] and review['actual_visual_reviewed']
        result['verification_sha256'][k]=sha(ROOT/f'build/question-{k}-verification.json')
        result['question_review_sha256'][k]=sha(ROOT/f'preview/visual-reviewed-q{k}.json')
        result['source_quality_sha256'][k]=sha(ROOT/f'build/source-quality-q{k}.json')
        for name,fig in review['figures_reviewed'].items():
            assert sha(ROOT/f'figures/{name}.pdf')==fig['pdf_sha256']
            result['figures_sha256'][name]=fig['pdf_sha256']
    for kind,label in [('paper','试卷'),('student','学生详解'),('teacher','教师备课')]:
        pdf=ROOT/f'output/pdf/蔡题015_{label}.pdf'
        row=comparison['versions'][kind]
        assert row['pdf_sha256']==sha(pdf)
        with fitz.open(pdf) as document:count=len(document)
        exact=[x['page'] for x in row['exact_reviewed_working_body_matches']]
        actually_direct=sorted(x['page'] for x in ledger['direct_hd_pages'] if x['variant']==kind)
        assert set(exact)|set(actually_direct)==set(range(1,count+1))
        folder=ROOT/f'preview/full-{kind}'
        pages={f'page-{p:03}.png':sha(folder/f'page-{p:03}.png') for p in range(1,count+1)}
        ovs={f'overview-{i:02}.jpg':sha(folder/f'overview-{i:02}.jpg') for i in range(1,(count+11)//12+1)}
        for name,digest in ovs.items():assert overviews[str((folder/name).relative_to(ROOT))]==digest
        record=dict(pdf_sha256=sha(pdf),source_sha256=sha(ROOT/f'markdown/蔡题015_{label}.md'),
            total_pages=count,body_pages=count-1,page_png_sha256=pages,overview_sha256=ovs,
            overview_page_range=[1,count],overview_pages_reviewed=list(range(1,count+1)),
            high_resolution_pages_reviewed=list(range(1,count+1)),
            direct_final_high_resolution_pages_reviewed=actually_direct,
            exact_reviewed_working_body_pages=[x for x in exact if x>1],
            cover_actual_hd_reuse=1 in exact,
            high_resolution_method='Direct final-page reading or exact current actually-reviewed working-body raster, never inferred from text similarity')
        if kind=='paper':record['all_question_pages_high_resolution_reviewed']=set(range(2,10))<=set(actually_direct)
        result[kind]=record
        if kind!='paper':
            result['density_exceptions'][kind]={}
            for p,reason in ledger['density_reasons'][kind].items():
                rel=f'preview/full-{kind}/page-{int(p):03}.png'
                assert rel in direct
                result['density_exceptions'][kind][p]=dict(actual_checked=True,reason=reason,png_sha256=pages[f'page-{int(p):03}.png'])
    path=ROOT/'preview/visual-reviewed-full.json'
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'actual_reviewed':True,'set_accepted':False,'current_pages':{k:result[k]['total_pages'] for k in ['paper','student','teacher']},'overview_count':len(overviews),'direct_final_hd_count':len(direct)}))
if __name__=='__main__':main()
