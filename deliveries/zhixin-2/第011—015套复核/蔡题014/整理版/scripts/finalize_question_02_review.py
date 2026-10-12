"""Accept only the current Q2 work files, retaining whole-set status false."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from audit_sources import inspect
from record_question_02_reading import pixel
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    draft=ROOT/'drafts/question-02.md'
    metrics=inspect('02');assert not metrics['issues']
    math=json.loads((ROOT/'verification/question-02-math.json').read_text())
    geometry=json.loads((ROOT/'verification/question-02-geometry.json').read_text())
    visual=json.loads((ROOT/'preview/visual-q02-final.json').read_text())
    build=json.loads((ROOT/'preview/working-draft-check-q02.json').read_text())
    manifest=json.loads((ROOT/'preview/working-page-manifest-q02.json').read_text())
    assert math['math_passed'] and math['model_authorized'] and geometry['geometry_passed']
    assert math['draft_sha256']==visual['draft_sha256']==sha(draft)
    assert math['figure_source_sha256']==geometry['figure_source_sha256']==visual['figure_source_sha256']==sha(ROOT/'figures/题02_图稿源文件.tex')
    originals=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,row in originals.items():assert sha(ROOT.parent/name)==row['sha256']==math['source_sha256'][name]
    template=ROOT/'latex/template.tex'
    assert sha(template)==sha(ROOT.parents[1]/'蔡题015/整理版/latex/template.tex')
    assert not re.search(r'\\(?:newpage|clearpage|setstretch|fontsize|enlargethispage|vspace|baselinestretch)',draft.read_text())
    for row in build:
        version=row['version'];name=f'working-q02-{version}';folder=ROOT/'preview'/name
        pdf=folder/(name+'.pdf')
        assert sha(pdf)==row['pdf_sha256']==manifest[name]['pdf_sha256']
        assert row['draft_sha256']==sha(draft) and not row['layout_warnings']
        readings=[x for x in visual['pages'] if x['version']==version]
        assert len(readings)==row['total_pages']
        for reading in readings:
            path=folder/f"page-{reading['page']:03}.png"
            assert sha(path)==reading['png_sha256'] and pixel(path)==reading['pixel_sha256']
            assert reading['actual_displayed_and_read'] and reading['pdf_sha256']==sha(pdf)
        with fitz.open(pdf) as doc:
            assert len(doc)==row['total_pages']
            assert re.sub(r'\s','',doc[0].get_text())=='第014套'
            assert all('\ufffd' not in p.get_text() for p in doc)
            assert all(v>200 for v in row['per_page_nonspace'])
        log=(folder/(name+'.log')).read_text(errors='replace')
        assert not any(key in log for key in ['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:'])
        subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        work=(folder/(name+'.md')).read_text()
        body=re.sub(r'\A---\n.*?\n---\n','',work,flags=re.S)
        expected=draft.read_text().split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else draft.read_text()
        assert body==expected
    for item in geometry['figures']:
        matching=next(x for x in visual['actual_figures'] if x['name']==item['name'])
        for suffix in ['png','pdf']:
            assert sha(ROOT/f"figures/{item['name']}.{suffix}")==item[f'{suffix}_sha256']==matching[f'{suffix}_sha256']
        assert matching['actual_displayed_and_read']
    for row in visual['actual_overviews']:assert sha(Path(row['path']))==row['sha256'] and row['actual_displayed_and_read']
    for path in [ROOT/'figures/题02_图稿源文件.pdf']+[ROOT/f"figures/{row['name']}.pdf" for row in geometry['figures']]:
        subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
    report=dict(paper='014',question='02',question_accepted=True,set_accepted=False,
                model_authorization='用户2026-10-10：四项均按建议修订并注明',
                draft_sha256=sha(draft),math_record_sha256=sha(ROOT/'verification/question-02-math.json'),
                geometry_record_sha256=sha(ROOT/'verification/question-02-geometry.json'),
                visual_record_sha256=sha(ROOT/'preview/visual-q02-final.json'),baseline_visual_record_sha256=sha(ROOT/'preview/visual-q02-baseline.json'),
                versions=build,source_metrics=metrics,symbolic_checks=math['symbolic_count'],numeric_checks=math['numeric_count'],
                geometrical_checks=geometry['check_count'],figures=4,qpdf_files=7,original_hashes_unchanged=True,
                baseline_direct_hd_pages=19,current_repaired_direct_hd_pages=1,actual_current_page_coverage=29,
                pending=['第3—8题尚未编写验收；本套无正式完整PDF'])
    (ROOT/'verification/question-02-accepted.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question_accepted=True,set_accepted=False,body_pages={x['version']:x['body_pages'] for x in build},figures=4,actual_page_coverage=29),ensure_ascii=False))
if __name__=='__main__':main()
