from pathlib import Path
import argparse,sys,runpy
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'工具'))
import build
p=argparse.ArgumentParser(description='从最终教师Markdown与图稿源文件重新生成五套交付。')
p.add_argument('sets',nargs='*',type=int,choices=[42,41,40,39,38])
p.add_argument('--only-documents',action='store_true',help='沿用现有矢量图，仅重建三种文档。')
a=p.parse_args();sets=a.sets or [42,41,40,39,38]
if not a.only_documents:
    for n in sets:
        if n<=40:build.split_figures(ROOT/f'蔡题{n:03}',n)
    # Matplotlib generators contain the full batch; regenerate the corrected overlays last.
    runpy.run_path(str(ROOT/'工具/render_figures.py'),run_name='__main__')
    runpy.run_path(str(ROOT/'工具/correct_figures.py'),run_name='__main__')
for n in sets:build.build(ROOT/f'蔡题{n:03}',n)
print('三种文档、模块数、最低正文页数及零错误日志验证通过。')
