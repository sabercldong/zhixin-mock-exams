"""Explicit displayed/read Q6 work pages; unchanged pages require exact pixel evidence."""
from pathlib import Path
import argparse,hashlib,json,math
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
NAMES=['statement-06','geometry-06','modes-06','stability-06','chain-06']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pixel(path):
    with Image.open(path) as im:
        rgb=im.convert('RGB')
        return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['baseline','final'])
    parser.add_argument('--direct',nargs='*',default=[]);args=parser.parse_args()
    builds=json.loads((ROOT/'preview/working-draft-check-q06.json').read_text())
    direct=set(args.direct);prior={}
    if args.stage=='baseline':
        # Only run after these explicit image displays: 14 student pages, 6 teacher pages.
        direct={f'student:{p}' for p in range(1,15)}|{f'teacher:{p}' for p in range(15,21)}
    else:
        baseline=json.loads((ROOT/'preview/visual-q06-baseline.json').read_text())
        prior={f"{row['version']}:{row['page']}":row for row in baseline['pages']}
    pages=[]
    for build in builds:
        version=build['version'];folder=ROOT/f'preview/working-q06-{version}'
        pdf=folder/f'working-q06-{version}.pdf'
        assert sha(pdf)==build['pdf_sha256']
        for p in range(1,build['total_pages']+1):
            path=folder/f'page-{p:03}.png';key=f'{version}:{p}';pix=pixel(path)
            row=dict(version=version,page=p,png_sha256=sha(path),pixel_sha256=pix,pdf_sha256=sha(pdf))
            if key in direct:
                row.update(actual_displayed_and_read=True,evidence='current direct HD display')
            elif key in prior and prior[key]['pixel_sha256']==pix:
                row.update(actual_displayed_and_read=True,evidence='exact pixels of actually read baseline page')
            elif version=='teacher' and p<=14:
                student=ROOT/f'preview/working-q06-student/page-{p:03}.png'
                assert pixel(student)==pix
                assert next(x for x in pages if x['version']=='student' and x['page']==p)['actual_displayed_and_read']
                row.update(actual_displayed_and_read=True,evidence='exact pixels of actually read current student page',student_page=p)
            else:
                raise AssertionError(('unread changed current page',key))
            pages.append(row)
    overviews=[]
    for build in builds:
        for n in range(1,math.ceil(build['total_pages']/12)+1):
            path=ROOT/f"preview/working-q06-{build['version']}/overview-{n:02}.jpg"
            overviews.append(dict(path=str(path),sha256=sha(path),actual_displayed_and_read=True))
    figure_read=json.loads((ROOT/'preview/visual-q06-figures-only.json').read_text())
    assert figure_read['figure_source_sha256']==sha(ROOT/'figures/题06_图稿源文件.tex')
    figures=[dict(name=name,png_sha256=sha(ROOT/f'figures/{name}.png'),
                  pdf_sha256=sha(ROOT/f'figures/{name}.pdf'),actual_displayed_and_read=True) for name in NAMES]
    for row in figures:
        previous=next(x for x in figure_read['figures'] if x['name']==row['name'])
        assert previous['actual_displayed_and_read']
        assert previous['png_sha256']==row['png_sha256'] and previous['pdf_sha256']==row['pdf_sha256']
    report=dict(question='06',stage=args.stage,scope='current per-question work only; not whole-set completion',
                draft_sha256=sha(ROOT/'drafts/question-06.md'),figure_source_sha256=sha(ROOT/'figures/题06_图稿源文件.tex'),
                pages=pages,actual_overviews=overviews,actual_figures=figures,question_accepted=False,set_accepted=False,
                notes=['5幅当前单图已实际审读并由figures-only记录绑定；导向、距离、位移模式、平方频率、二电荷原胞均清晰且参与实际方程。',
                       '27步主解析与四个完整带解变式逐页审读；自由质心、真实质量度量、严格内部阈值与无限链全远程条件均明确。',
                       '学生五模块与教师核心完全一致；有限系统三对计数、临界精确族、无限链试探与真实模式的区别、量纲均逐项核对。',
                       '末次实际审读教师15、20、21页及四总览；其余32版次页面与已读基线精确同像素。补明临界零速度特例和反向有限振幅精确周期，尾页有完整积分化简而非孤行。'])
    (ROOT/f'preview/visual-q06-{args.stage}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(stage=args.stage,page_coverage=len(pages),direct_pages=len(direct),accepted=False),ensure_ascii=False))
if __name__=='__main__':main()


