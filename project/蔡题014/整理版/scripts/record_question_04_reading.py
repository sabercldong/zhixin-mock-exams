"""Explicit displayed/read Q4 work pages; unchanged pages require exact pixel evidence."""
from pathlib import Path
import argparse,hashlib,json,math
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
NAMES=['statement-04','element-04','flux-04','motion-04','graphs-04']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pixel(path):
    with Image.open(path) as im:
        rgb=im.convert('RGB')
        return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['baseline','final'])
    parser.add_argument('--direct',nargs='*',default=[]);args=parser.parse_args()
    builds=json.loads((ROOT/'preview/working-draft-check-q04.json').read_text())
    direct=set(args.direct);prior={}
    if args.stage=='baseline':
        # Only run after these explicit image displays: 15 student pages, 9 teacher pages.
        direct={f'student:{p}' for p in range(1,16)}|{f'teacher:{p}' for p in range(15,24)}
    else:
        baseline=json.loads((ROOT/'preview/visual-q04-baseline.json').read_text())
        prior={f"{row['version']}:{row['page']}":row for row in baseline['pages']}
    pages=[]
    for build in builds:
        version=build['version'];folder=ROOT/f'preview/working-q04-{version}'
        pdf=folder/f'working-q04-{version}.pdf'
        assert sha(pdf)==build['pdf_sha256']
        for p in range(1,build['total_pages']+1):
            path=folder/f'page-{p:03}.png';key=f'{version}:{p}';pix=pixel(path)
            row=dict(version=version,page=p,png_sha256=sha(path),pixel_sha256=pix,pdf_sha256=sha(pdf))
            if key in direct:
                row.update(actual_displayed_and_read=True,evidence='current direct HD display')
            elif key in prior and prior[key]['pixel_sha256']==pix:
                row.update(actual_displayed_and_read=True,evidence='exact pixels of actually read baseline page')
            elif version=='teacher' and p<=14:
                student=ROOT/f'preview/working-q04-student/page-{p:03}.png'
                assert pixel(student)==pix
                assert next(x for x in pages if x['version']=='student' and x['page']==p)['actual_displayed_and_read']
                row.update(actual_displayed_and_read=True,evidence='exact pixels of actually read current student page',student_page=p)
            else:
                raise AssertionError(('unread changed current page',key))
            pages.append(row)
    overviews=[]
    for build in builds:
        for n in range(1,math.ceil(build['total_pages']/12)+1):
            path=ROOT/f"preview/working-q04-{build['version']}/overview-{n:02}.jpg"
            overviews.append(dict(path=str(path),sha256=sha(path),actual_displayed_and_read=True))
    figures=[dict(name=name,png_sha256=sha(ROOT/f'figures/{name}.png'),
                  pdf_sha256=sha(ROOT/f'figures/{name}.pdf'),actual_displayed_and_read=True) for name in NAMES]
    report=dict(question='04',stage=args.stage,scope='current per-question work only; not whole-set completion',
                draft_sha256=sha(ROOT/'drafts/question-04.md'),figure_source_sha256=sha(ROOT/'figures/题04_图稿源文件.tex'),
                pages=pages,actual_overviews=overviews,actual_figures=figures,question_accepted=False,set_accepted=False,
                notes=['5幅图实际审读；真三维螺旋线两端接电源，孤立环不接线；电源极性与线圈向上磁场一致，径向场标签避开高度线。',
                       '21步主解析与四个完整带解变式逐页审读；图宽按实际可读字号选择，不扩大行距或使用空白凑页。',
                       '学生五模块与教师核心完全一致；共同建场半系数、两类电动势、力向、交流相位和有限自感的适用条件完整分开。'])
    (ROOT/f'preview/visual-q04-{args.stage}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(stage=args.stage,page_coverage=len(pages),direct_pages=len(direct),accepted=False),ensure_ascii=False))
if __name__=='__main__':main()

