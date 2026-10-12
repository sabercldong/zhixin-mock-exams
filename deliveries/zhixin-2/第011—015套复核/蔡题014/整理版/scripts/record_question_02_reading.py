"""Explicit current reading events, with exact-pixel reuse after wording repairs."""
from pathlib import Path
import argparse,hashlib,json
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pixel(path):
    with Image.open(path) as im:
        rgb=im.convert('RGB');return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['baseline','final']);parser.add_argument('--direct',nargs='*',default=[]);args=parser.parse_args()
    builds=json.loads((ROOT/'preview/working-draft-check-q02.json').read_text())
    direct=set(args.direct)
    prior=None
    if args.stage=='baseline':
        direct={f'student:{p}' for p in range(1,13)}|{f'teacher:{p}' for p in range(11,18)}
    else:
        prior=json.loads((ROOT/'preview/visual-q02-baseline.json').read_text())
        prior={f"{row['version']}:{row['page']}":row for row in prior['pages']}
    pages=[]
    for build in builds:
        version=build['version']
        pdf=ROOT/f'preview/working-q02-{version}/working-q02-{version}.pdf'
        assert sha(pdf)==build['pdf_sha256']
        for p in range(1,build['total_pages']+1):
            path=ROOT/f'preview/working-q02-{version}/page-{p:03}.png'
            key=f'{version}:{p}';pix=pixel(path)
            event=dict(version=version,page=p,png_sha256=sha(path),pixel_sha256=pix,pdf_sha256=sha(pdf))
            if key in direct:
                event.update(actual_displayed_and_read=True,evidence='current direct HD display')
            elif prior and prior[key]['pixel_sha256']==pix:
                event.update(actual_displayed_and_read=True,evidence='exact pixels of actually read baseline page',baseline_key=key)
            elif version=='teacher' and p<=10:
                student=ROOT/f'preview/working-q02-student/page-{p:03}.png'
                assert pixel(student)==pix
                student_event=next(row for row in pages if row['version']=='student' and row['page']==p)
                assert student_event['actual_displayed_and_read']
                event.update(actual_displayed_and_read=True,evidence='exact pixels of actually read current student page',student_page=p)
            else:raise AssertionError(('unread changed current page',key))
            pages.append(event)
    overview=[]
    for version,counts in [('student',1),('teacher',2)]:
        for n in range(1,counts+1):
            path=ROOT/f'preview/working-q02-{version}/overview-{n:02}.jpg'
            overview.append(dict(path=str(path),sha256=sha(path),actual_displayed_and_read=True))
    figures=[]
    for name in ['cell-02','dipole-02','slab-02','disks-02']:
        path=ROOT/f'figures/{name}.png';figures.append(dict(name=name,png_sha256=sha(path),pdf_sha256=sha(path.with_suffix('.pdf')),actual_displayed_and_read=True))
    record=dict(question='02',scope='explicit work PDF readings, not formal whole-set acceptance',stage=args.stage,
                draft_sha256=sha(ROOT/'drafts/question-02.md'),figure_source_sha256=sha(ROOT/'figures/题02_图稿源文件.tex'),
                pages=pages,actual_overviews=overview,actual_figures=figures,question_accepted=False,set_accepted=False,
                notes=['三维晶胞六面心/八角点/钛偏移均实际审图，尺寸线端点已校正；极化与去极化场相反。',
                '15步学生核心与教师四个带解变式均实际审读；先前稀疏末页经有限检验逻辑块与完整补偿边界推导修正。'])
    dest=ROOT/f'preview/visual-q02-{args.stage}.json';dest.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(stage=args.stage,pages=len(pages),direct_events=len(direct),accepted=False),ensure_ascii=False))
if __name__=='__main__':main()
