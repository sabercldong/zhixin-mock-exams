"""Exact-pixel reuse candidates after authorized revisions; NEVER visual acceptance."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
HISTORY=ROOT/'revision-history/before-four-model-revisions-20261009'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    snapshot=json.loads((HISTORY/'snapshot-manifest.json').read_text())
    result={'scope':'Review candidates only; current unseen pages are not accepted','actual_visual_review_inferred':False,'questions':{},'new_unique_page_candidates':[]}
    old_pixels={}
    for q in ['01','03','05','06']:
        oldpath=HISTORY/f'preview/visual-reviewed-q{q}.json'
        assert sha(oldpath)==snapshot['files'][str(oldpath.relative_to(HISTORY))]
        old=json.loads(oldpath.read_text())
        assert old['actual_visual_reviewed']
        for version,info in old['pdfs'].items():
            assert info['high_resolution_pages_reviewed']==list(range(1,info['total_pages']+1))
            for filename,digest in info['page_png_sha256'].items():
                p=HISTORY/f'preview/working-q{q}-{version}'/filename
                assert sha(p)==digest==snapshot['files'][str(p.relative_to(HISTORY))]
                old_pixels.setdefault(digest,[]).append({'path':str(p),'old_actual_record_sha256':sha(oldpath),'question':int(q),'version':version,'page':int(filename[5:8])})
    groups={}
    for q in ['01','03','05','06']:
        old=json.loads((HISTORY/f'preview/visual-reviewed-q{q}.json').read_text())
        math=json.loads((ROOT/f'build/question-{q}-verification.json').read_text())
        quality=json.loads((ROOT/f'build/source-quality-q{q}.json').read_text())
        assert math['verified_math'] and math['model_condition_resolved'] and quality['passed']
        for value in math['bound_files'].values():assert sha(Path(value['path']))==value['sha256']
        data={'old_actual_review_record_sha256':sha(HISTORY/f'preview/visual-reviewed-q{q}.json'),'pdfs':{},'unchanged_actual_pixel_reuse':[]}
        for version in ['student','teacher']:
            folder=ROOT/f'preview/working-q{q}-{version}';base=folder/folder.name
            with fitz.open(base.with_suffix('.pdf')) as doc:
                densities=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:]
                pages={f'page-{i:03}.png':sha(folder/f'page-{i:03}.png') for i in range(1,len(doc)+1)}
                info={'pdf_sha256':sha(base.with_suffix('.pdf')),'total_pages':len(doc),'body_pages':len(doc)-1,'body_nonspace':sum(densities),'per_page_nonspace':densities,'page_png_sha256':pages,
                      'overview_sha256':{f'overview-{i:02}.jpg':sha(folder/f'overview-{i:02}.jpg') for i in range(1,(len(doc)+11)//12+1)}}
            data['pdfs'][version]=info
            for name,digest in pages.items():
                rel=str((folder/name).relative_to(ROOT))
                if digest in old_pixels:data['unchanged_actual_pixel_reuse'].append({'current':rel,'sha256':digest,'historical_actual_pages':old_pixels[digest]})
                else:groups.setdefault(digest,[]).append(rel)
            log=base.with_suffix('.log').read_text()
            assert not re.search(r'Warning|Underfull|Overfull|Missing character|^!',log,re.M)
            subprocess.run(['qpdf','--check',str(base.with_suffix('.pdf'))],capture_output=True,check=True)
        result['questions'][q]=data
    result['new_unique_page_candidates']=[{'sha256':digest,'direct_read_candidate':paths[0],'identical_current_pages':paths} for digest,paths in groups.items()]
    target=ROOT/'build/model-revision-page-candidates.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'new_unique_pages':len(groups),'historical_exact_page_reuse':sum(len(v['unchanged_actual_pixel_reuse']) for v in result['questions'].values()),'new_paths':[r['direct_read_candidate'] for r in result['new_unique_page_candidates']],'ensure_no_review_inference':True}))
if __name__=='__main__':main()
