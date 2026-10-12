"""Finalize Q1 using only explicitly recorded actual readings and exact pixel reuse."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from PIL import Image
from audit_sources import inspect
ROOT=Path(__file__).resolve().parents[1]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pixels(path):
    with Image.open(path) as im:
        rgb=im.convert('RGB')
        return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest()
def main():
    draft=ROOT/'drafts/question-01.md'
    assert not inspect('01')['issues']
    math=json.loads((ROOT/'verification/question-01-math.json').read_text())
    geometry=json.loads((ROOT/'verification/question-01-geometry.json').read_text())
    assert math['math_passed'] and math['model_authorized'] and geometry['geometry_passed']
    assert math['draft_sha256']==digest(draft)
    assert math['figure_source_sha256']==geometry['figure_source_sha256']==digest(ROOT/'figures/题01_图稿源文件.tex')
    original=json.loads((ROOT/'preview/originals/source-manifest.json').read_text())
    for name,row in original.items():
        assert row['sha256']==digest(ROOT.parent/name)
    pages=json.loads((ROOT/'preview/working-page-manifest-q01.json').read_text())
    build=json.loads((ROOT/'preview/working-draft-check-q01.json').read_text())
    # Explicit reading events: all 15 student HD pages and teacher HD pages 15-20.
    # The list is entered only after the main agent has actually displayed them.
    explicit=[('student',p) for p in range(1,16)]+[('teacher',p) for p in range(15,21)]
    direct=[]
    for version,page in explicit:
        path=ROOT/f'preview/working-q01-{version}/page-{page:03}.png'
        direct.append(dict(version=version,page=page,path=str(path),file_sha256=digest(path),pixel_sha256=pixels(path),actual_displayed_and_read=True))
    overview=[]
    for version in ['student','teacher']:
        for n in [1,2]:
            path=ROOT/f'preview/working-q01-{version}/overview-{n:02}.jpg'
            overview.append(dict(path=str(path),sha256=digest(path),actual_displayed_and_read=True))
    reused=[]
    for p in range(1,15):
        student=ROOT/f'preview/working-q01-student/page-{p:03}.png'
        teacher=ROOT/f'preview/working-q01-teacher/page-{p:03}.png'
        assert pixels(student)==pixels(teacher),('pixel mismatch',p)
        reused.append(dict(version='teacher',page=p,read_from_version='student',read_from_page=p,pixel_sha256=pixels(teacher),exact_pixel_match=True))
    figures=[]
    for entry in geometry['figures']:
        png=ROOT/f"figures/{entry['name']}.png"
        pdf=png.with_suffix('.pdf')
        assert digest(png)==entry['png_sha256'] and digest(pdf)==entry['pdf_sha256']
        figures.append(dict(**entry,actual_displayed_and_read=True))
    for row in build:
        assert row['draft_sha256']==digest(draft) and not row['layout_warnings']
        version=row['version'];path=ROOT/f'preview/working-q01-{version}/working-q01-{version}.pdf'
        assert digest(path)==row['pdf_sha256']==pages[f'working-q01-{version}']['pdf_sha256']
        with fitz.open(path) as doc:
            assert len(doc)==row['total_pages']
            assert len(re.sub(r'\s','',doc[0].get_text()))==5
            assert re.sub(r'\s','',doc[0].get_text())=='第014套'
            for page in doc:
                assert '\ufffd' not in page.get_text()
            assert all(v>200 for v in row['per_page_nonspace'])
        subprocess.run(['qpdf','--check',str(path)],check=True,capture_output=True)
    for path in [ROOT/'figures/题01_图稿源文件.pdf']+[ROOT/f"figures/{entry['name']}.pdf" for entry in figures]:
        subprocess.run(['qpdf','--check',str(path)],check=True,capture_output=True)
    source=draft.read_text()
    for version in ['student','teacher']:
        work=(ROOT/f'preview/working-q01-{version}/working-q01-{version}.md').read_text()
        body=re.sub(r'\A---\n.*?\n---\n','',work,flags=re.S)
        expected=source.split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else source
        assert body==expected
    ledger=dict(question='01',scope='current question work PDFs only',read_date='2026-10-10',
                explicit_hd_pages=direct,exact_reuse_pages=reused,actual_overviews=overview,
                actual_figures=figures,notes=['全部工作稿页实际总览；21页直接高清审读，其余14页以像素完全相同的已读页复核。',
                '图1-2的投影与标注位置、图1-3半径尺寸线、图1-5分量标注经修改后按当前版本重新查看。',
                '公式无裁切、缺字或重叠；尾页不是仅一两句话，图前后使用对应符号建方程。'],
                set_accepted=False)
    path=ROOT/'preview/visual-reviewed-q01.json'
    path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    report=dict(paper='014',question='01',question_accepted=True,set_accepted=False,
                model_authorization='用户2026-10-10：四项均按建议修订并注明',
                draft_sha256=digest(draft),math_record_sha256=digest(ROOT/'verification/question-01-math.json'),
                geometry_record_sha256=digest(ROOT/'verification/question-01-geometry.json'),
                visual_record_sha256=digest(path),versions=build,source_metrics=inspect('01'),
                symbolic_checks=math['symbolic_count'],numeric_checks=math['numeric_count'],
                geometrical_checks=geometry['check_count'],figures=len(figures),qpdf_files=9,
                original_hashes_unchanged=True,pending=['第2—8题尚未编写验收；本套无正式完整PDF'])
    (ROOT/'verification/question-01-accepted.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question_accepted=True,set_accepted=False,body_pages={row['version']:row['body_pages'] for row in build},
                          figures=len(figures),explicit_hd_pages=len(direct),exact_reused_pages=len(reused)),ensure_ascii=False))
if __name__=='__main__':main()
