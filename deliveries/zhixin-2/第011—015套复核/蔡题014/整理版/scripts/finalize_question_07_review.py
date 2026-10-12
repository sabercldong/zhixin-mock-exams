"""Bind Q7 acceptance to current sources, actual reading and independent checks."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from audit_sources import inspect
from record_question_07_reading import pixel,NAMES
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    draft=ROOT/'drafts/question-07.md';text=draft.read_text()
    metrics=inspect('07');assert not metrics['issues']
    assert len(re.findall(r'\*\*第\d+步：',text))==22
    assert len(re.findall(r'\*\*变式\d+：',text))==4
    math=json.loads((ROOT/'verification/question-07-math.json').read_text())
    geom=json.loads((ROOT/'verification/question-07-geometry.json').read_text())
    visual=json.loads((ROOT/'preview/visual-q07-final.json').read_text())
    build=json.loads((ROOT/'preview/working-draft-check-q07.json').read_text())
    manifest=json.loads((ROOT/'preview/working-page-manifest-q07.json').read_text())
    assert math['math_passed'] and geom['geometry_passed']
    assert math['working_pdf_checks']==build
    assert math['draft_sha256']==visual['draft_sha256']==sha(draft)
    assert math['script_sha256']==sha(ROOT/'scripts/verify_question_07.py')
    fig_source=ROOT/'figures/题07_图稿源文件.tex'
    assert math['figure_source_sha256']==geom['figure_source_sha256']==visual['figure_source_sha256']==sha(fig_source)
    originals=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,row in originals.items():assert sha(ROOT.parent/name)==row['sha256']==math['source_sha256'][name]
    assert sha(ROOT/'latex/template.tex')==sha(ROOT.parents[1]/'蔡题015/整理版/latex/template.tex')
    assert not re.search(r'\\(?:newpage|clearpage|setstretch|fontsize|enlargethispage|vspace|baselinestretch)',text)
    banned=['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:']
    for item in build:
        v=item['version'];name=f'working-q07-{v}';folder=ROOT/'preview'/name
        pdf=folder/(name+'.pdf');assert sha(pdf)==item['pdf_sha256']==manifest[name]['pdf_sha256']
        assert item['draft_sha256']==sha(draft) and not item['layout_warnings']
        rows=[x for x in visual['pages'] if x['version']==v];assert len(rows)==item['total_pages']
        for row in rows:
            path=folder/f"page-{row['page']:03}.png"
            assert sha(path)==row['png_sha256'] and pixel(path)==row['pixel_sha256']
            assert row['actual_displayed_and_read'] and row['pdf_sha256']==sha(pdf)
        with fitz.open(pdf) as doc:
            assert len(doc)==item['total_pages']
            assert re.sub(r'\s','',doc[0].get_text())=='第014套'
            assert all('\ufffd' not in p.get_text() for p in doc)
            assert all(x>200 for x in item['per_page_nonspace'])
        assert not any(x in (folder/(name+'.log')).read_text(errors='replace') for x in banned)
        subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        work=(folder/(name+'.md')).read_text()
        body=re.sub(r'\A---\n.*?\n---\n','',work,flags=re.S)
        expected=text.split('## 六、关键洞察')[0].rstrip()+'\n' if v=='student' else text
        assert body==expected
    for row in geom['figures']:
        read=next(x for x in visual['actual_figures'] if x['name']==row['name'])
        for ext in ['png','pdf']:assert sha(ROOT/f"figures/{row['name']}.{ext}")==row[f'{ext}_sha256']==read[f'{ext}_sha256']
        assert read['actual_displayed_and_read']
    for row in visual['actual_overviews']:assert sha(Path(row['path']))==row['sha256'] and row['actual_displayed_and_read']
    assert not any(x in fig_source.with_suffix('.log').read_text(errors='replace') for x in banned)
    for p in [fig_source.with_suffix('.pdf')]+[ROOT/f'figures/{n}.pdf' for n in NAMES]:subprocess.run(['qpdf','--check',str(p)],capture_output=True,check=True)
    report=dict(paper='014',question='07',question_accepted=True,set_accepted=False,
                draft_sha256=sha(draft),math_record_sha256=sha(ROOT/'verification/question-07-math.json'),
                geometry_record_sha256=sha(ROOT/'verification/question-07-geometry.json'),
                visual_record_sha256=sha(ROOT/'preview/visual-q07-final.json'),versions=build,source_metrics=metrics,
                symbolic_checks=math['symbolic_count'],numeric_checks=math['numeric_count'],geometrical_checks=geom['check_count'],
                figures=len(NAMES),qpdf_files=9,original_hashes_unchanged=True,
                actual_direct_hd_pages=visual['direct_hd_count'],actual_current_page_coverage=len(visual['pages']),
                pending=['第8题尚未编写验收；本套无正式完整PDF'])
    (ROOT/'verification/question-07-accepted.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question_accepted=True,set_accepted=False,body_pages={x['version']:x['body_pages'] for x in build},figures=len(NAMES),actual_page_coverage=len(visual['pages'])),ensure_ascii=False))
if __name__=='__main__':main()
