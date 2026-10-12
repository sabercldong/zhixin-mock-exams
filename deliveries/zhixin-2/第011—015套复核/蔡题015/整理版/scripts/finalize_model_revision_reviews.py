"""Assemble saved reviews from explicit manual reading and exact-pixel proofs.
No rendering or unread-page acceptance is inferred here.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
HIST=ROOT/'revision-history/before-four-model-revisions-20261009'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
    ledger=read(ROOT/'preview/revision-actual-reading-ledger.json')
    assert ledger['actual_reading_attested'] and not ledger['whole_set_accepted']
    candidates=read(ROOT/'build/model-revision-page-candidates.json')
    direct={v['sha256']:v['path'] for v in ledger['new_hd_pages']}
    for p in candidates['new_unique_page_candidates']:
        assert p['sha256'] in direct,p['direct_read_candidate']
        assert sha(ROOT/direct[p['sha256']])==p['sha256']
        for rel in p['identical_current_pages']:assert sha(ROOT/rel)==p['sha256']
    over={v['path']:v['sha256'] for v in ledger['overview_images']}
    figs={v['path']:v['sha256'] for v in ledger['direct_figures']}
    snapshot=read(HIST/'snapshot-manifest.json')
    for q,info in candidates['questions'].items():
        oldrel=f'preview/visual-reviewed-q{q}.json'
        assert sha(HIST/oldrel)==snapshot['files'][oldrel]==info['old_actual_review_record_sha256']
        old=read(HIST/oldrel)
        physics=read(ROOT/f'build/question-{q}-verification.json')
        quality=read(ROOT/f'build/source-quality-q{q}.json')
        geometry=read(ROOT/f'build/question-{q}-figure-geometry.json')
        assert physics['verified_math'] and physics['model_condition_resolved'] and quality['passed'] and geometry['passed']
        for v in physics['bound_files'].values():assert sha(Path(v['path']))==v['sha256']
        source=ROOT/f'drafts/question-{q}.md'
        assert quality['questions'][0]['sha256']==sha(source)
        history_pages={v['current']:v for v in info['unchanged_actual_pixel_reuse']}
        figure_proofs={}
        for name,figure in physics['figures'].items():
            rel=f'figures/{name}.png'
            assert sha(ROOT/rel)==figure['png_sha256']
            if old['figures_reviewed'][name]['png_sha256']==figure['png_sha256']:
                historical=HIST/rel
                assert sha(historical)==snapshot['files'][rel]==figure['png_sha256']
                figure_proofs[name]={'method':'historical actual-read identical PNG','historical_actual_review_sha256':sha(HIST/oldrel),'png_sha256':figure['png_sha256']}
            else:
                assert figs[rel]==figure['png_sha256']
                figure_proofs[name]={'method':'direct actual standalone image read','png_sha256':figure['png_sha256']}
        coverage={};identical=[]
        for version,pdf in info['pdfs'].items():
            folder=ROOT/f'preview/working-q{q}-{version}'
            path=folder/(folder.name+'.pdf')
            assert sha(path)==pdf['pdf_sha256']
            with fitz.open(path) as doc:assert len(doc)==pdf['total_pages']
            pdf['overview_pages_reviewed']=list(range(1,pdf['total_pages']+1))
            pdf['high_resolution_pages_reviewed']=list(range(1,pdf['total_pages']+1))
            coverage[version]=[]
            for name,digest in pdf['page_png_sha256'].items():
                rel=str((folder/name).relative_to(ROOT));assert sha(ROOT/rel)==digest
                if rel in history_pages:
                    v=history_pages[rel]
                    for h in v['historical_actual_pages']:
                        assert sha(Path(h['path']))==digest
                    proof={'page':int(name[5:8]),'method':'historical actual-read exact full-page PNG','sha256':digest,'historical_evidence':v['historical_actual_pages']}
                else:
                    assert digest in direct
                    proof={'page':int(name[5:8]),'method':'current direct read or exact full-page duplicate','sha256':digest,'actually_read_path':direct[digest]}
                coverage[version].append(proof)
            for name,digest in pdf['overview_sha256'].items():
                rel=str((folder/name).relative_to(ROOT))
                assert over[rel]==sha(ROOT/rel)==digest
            assert not re.search(r'Warning|Underfull|Overfull|Missing character|^!',path.with_suffix('.log').read_text(),re.M)
        for i in range(1,min(p['total_pages'] for p in info['pdfs'].values())+1):
            key=f'page-{i:03d}.png'
            if info['pdfs']['student']['page_png_sha256'][key]==info['pdfs']['teacher']['page_png_sha256'][key]:
                identical.append({'student_page':i,'teacher_page':i,'png_sha256':info['pdfs']['student']['page_png_sha256'][key]})
        original=old['original_images_actually_reviewed']
        for rel,digest in original.items():assert sha(ROOT/rel)==digest
        paths=list(old['bound_sha256'])+[
            'preview/revision-actual-reading-ledger.json','build/model-revision-page-candidates.json',
            'build/model-revisions-015-2026-10-09.json','scripts/collect_revision_read_candidates.py',
            'scripts/finalize_model_revision_reviews.py',str((HIST/'snapshot-manifest.json').relative_to(ROOT)),
            str((HIST/oldrel).relative_to(ROOT))]
        for version in ['student','teacher']:
            base=f'preview/working-q{q}-{version}/working-q{q}-{version}'
            paths += [base+'.'+ext for ext in ['md','tex','pdf','log']]
        bound={rel:sha(ROOT/rel) for rel in dict.fromkeys(paths)}
        qpdf=[]
        for rel in dict.fromkeys(item['path'] for item in old['qpdf_checks']):
            subprocess.run(['qpdf','--check',str(ROOT/rel)],capture_output=True,check=True)
            qpdf.append({'path':rel,'sha256':sha(ROOT/rel),'passed':True})
        record={
            'paper':'015','question':int(q),'review_saved_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Human-authorized revised question current actual-page review; not whole-set acceptance',
            'actual_visual_reviewed':True,'conditional_draft_reviewed':False,'user_reply_received':True,
            'model_condition_resolved':True,'question_accepted':True,'set_accepted':False,
            'remaining_visual_issues':[],'remaining_model_issues':[],
            'source_sha256':sha(source),'source_quality_sha256':sha(ROOT/f'build/source-quality-q{q}.json'),
            'verification_sha256':sha(ROOT/f'build/question-{q}-verification.json'),
            'geometry_sha256':sha(ROOT/f'build/question-{q}-figure-geometry.json'),
            'template_sha256':sha(ROOT/'latex/template.tex'),'bound_sha256':bound,
            'pdfs':info['pdfs'],'identical_page_reuse':identical,'actual_page_coverage':coverage,
            'figures_reviewed':physics['figures'],'figure_actual_read_proofs':figure_proofs,
            'original_images_actually_reviewed':original,'original_reading':old.get('original_reading',{}),
            'qpdf_checks':qpdf,'source_metrics':{v:quality['questions'][0][v] for v in ['student','teacher']},
            'independent_verification':({k:physics[k] for k in ['symbolic_count','numeric_count','max_normalized_error']} if 'symbolic_count' in physics else {
                'symbolic_count':len(physics['symbolic_checks']),
                'numeric_count':len(physics['independent_numerical_checks']),
                'per_check_errors_retained_in_verification':True}),
            'layout':{'paper':'A4','font_pt':12,'margin_mm':22,'line_spacing':1.24,'paragraph_spacing_em':0.35,'local_spacing_expansion':False},
            'corrections_actually_reviewed':ledger['notes'],'formal_delivery':False,
            'next':'Whole-paper rebuild and current actual PDF review before set acceptance'}
        visual=ROOT/oldrel
        save(visual,record)
        work={
            'paper':'015','question':int(q),'scope':'Current revised question working acceptance only',
            'saved_utc':record['review_saved_utc'],'question_accepted':True,'model_condition_resolved':True,
            'document_complete':True,'verified_math':True,'actual_visual_reviewed':True,'set_accepted':False,
            'formal_delivery_allowed':False,'issues':[],'remaining_model_issues':[],
            'pdfs':info['pdfs'],'source_metrics':record['source_metrics'],'figures':len(physics['figures']),
            'independent_verification':record['independent_verification'],'geometry_checks':geometry.get('check_count'),
            'geometry_passed':geometry['passed'],
            'bound_sha256':{rel:sha(ROOT/rel) for rel in [
                f'drafts/question-{q}.md',f'build/source-quality-q{q}.json',
                f'build/question-{q}-verification.json',f'build/question-{q}-figure-geometry.json',
                oldrel,'preview/revision-actual-reading-ledger.json','build/model-revisions-015-2026-10-09.json']},
            'next':'Whole-paper rebuild and current actual PDF review before set acceptance'}
        save(ROOT/f'build/question-{q}-work-check.json',work)
        print(json.dumps({'question':int(q),'working_accepted':True,'current_pages':{v:d['total_pages'] for v,d in info['pdfs'].items()},'set_accepted':False}))
if __name__=='__main__':main()
