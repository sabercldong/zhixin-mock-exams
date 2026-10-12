"""Q5 acceptance is bound to current math, figures, source and actually read work PDFs."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from audit_sources import inspect
from record_question_05_reading import pixel,NAMES
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    draft=ROOT/'drafts/question-05.md';text=draft.read_text()
    source_metrics=inspect('05');assert not source_metrics['issues']
    assert len(re.findall(r'\*\*第\d+步：',text))==21
    assert len(re.findall(r'\*\*变式\d+：',text))==4
    math=json.loads((ROOT/'verification/question-05-math.json').read_text())
    geometry=json.loads((ROOT/'verification/question-05-geometry.json').read_text())
    visual=json.loads((ROOT/'preview/visual-q05-final.json').read_text())
    build=json.loads((ROOT/'preview/working-draft-check-q05.json').read_text())
    manifest=json.loads((ROOT/'preview/working-page-manifest-q05.json').read_text())
    assert math['math_passed'] and geometry['geometry_passed']
    assert math['draft_sha256']==visual['draft_sha256']==sha(draft)
    assert math['script_sha256']==sha(ROOT/'scripts/verify_question_05.py')
    figure_source=ROOT/'figures/题05_图稿源文件.tex'
    assert math['figure_source_sha256']==geometry['figure_source_sha256']==visual['figure_source_sha256']==sha(figure_source)
    originals=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,row in originals.items():
        assert sha(ROOT.parent/name)==row['sha256']==math['source_sha256'][name]
    assert sha(ROOT/'latex/template.tex')==sha(ROOT.parents[1]/'蔡题015/整理版/latex/template.tex')
    assert not re.search(r'\\(?:newpage|clearpage|setstretch|fontsize|enlargethispage|vspace|baselinestretch)',text)
    for item in build:
        version=item['version'];name=f'working-q05-{version}';folder=ROOT/'preview'/name
        pdf=folder/(name+'.pdf');assert sha(pdf)==item['pdf_sha256']==manifest[name]['pdf_sha256']
        assert item['draft_sha256']==sha(draft) and not item['layout_warnings']
        readings=[x for x in visual['pages'] if x['version']==version]
        assert len(readings)==item['total_pages']
        for reading in readings:
            path=folder/f"page-{reading['page']:03}.png"
            assert sha(path)==reading['png_sha256'] and pixel(path)==reading['pixel_sha256']
            assert reading['actual_displayed_and_read'] and reading['pdf_sha256']==sha(pdf)
        with fitz.open(pdf) as doc:
            assert len(doc)==item['total_pages']
            assert re.sub(r'\s','',doc[0].get_text())=='第014套'
            assert all('\ufffd' not in page.get_text() for page in doc)
            assert all(v>200 for v in item['per_page_nonspace'])
        log=(folder/(name+'.log')).read_text(errors='replace')
        assert not any(key in log for key in ['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:'])
        subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        work=(folder/(name+'.md')).read_text()
        body=re.sub(r'\A---\n.*?\n---\n','',work,flags=re.S)
        expected=text.split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else text
        assert body==expected
    for item in geometry['figures']:
        read=next(x for x in visual['actual_figures'] if x['name']==item['name'])
        for suffix in ['png','pdf']:
            assert sha(ROOT/f"figures/{item['name']}.{suffix}")==item[f'{suffix}_sha256']==read[f'{suffix}_sha256']
        assert read['actual_displayed_and_read']
    for row in visual['actual_overviews']:
        assert sha(Path(row['path']))==row['sha256'] and row['actual_displayed_and_read']
    figure_log=figure_source.with_suffix('.log').read_text(errors='replace')
    assert not any(key in figure_log for key in ['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:'])
    for path in [figure_source.with_suffix('.pdf')]+[ROOT/f'figures/{name}.pdf' for name in NAMES]:
        subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
    report=dict(paper='014',question='05',question_accepted=True,set_accepted=False,
                draft_sha256=sha(draft),math_record_sha256=sha(ROOT/'verification/question-05-math.json'),
                geometry_record_sha256=sha(ROOT/'verification/question-05-geometry.json'),
                visual_record_sha256=sha(ROOT/'preview/visual-q05-final.json'),
                baseline_visual_record_sha256=sha(ROOT/'preview/visual-q05-baseline.json'),
                versions=build,source_metrics=source_metrics,symbolic_checks=math['symbolic_count'],
                numeric_checks=math['numeric_count'],geometrical_checks=geometry['check_count'],
                figures=len(NAMES),qpdf_files=8,original_hashes_unchanged=True,
                baseline_direct_hd_pages=22,actual_current_page_coverage=len(visual['pages']),
                pending=['第6—8题尚未编写验收；本套无正式完整PDF'])
    (ROOT/'verification/question-05-accepted.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question_accepted=True,set_accepted=False,body_pages={x['version']:x['body_pages'] for x in build},
                         figures=len(NAMES),actual_page_coverage=len(visual['pages'])),ensure_ascii=False))
if __name__=='__main__':main()


