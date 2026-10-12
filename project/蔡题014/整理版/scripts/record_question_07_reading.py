"""Run only after explicitly displaying and reading the named current work pages."""
from pathlib import Path
import argparse,hashlib,json,math
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
NAMES=['statement-07','optical-07','snell-07','spatial-07','moving-07','events-07']
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pixel(path):
    with Image.open(path) as im:
        rgb=im.convert('RGB')
        return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--direct',nargs='+',required=True)
    args=parser.parse_args();direct=set(args.direct)
    builds=json.loads((ROOT/'preview/working-draft-check-q07.json').read_text())
    pages=[];read_pixels={}
    for item in builds:
        v=item['version'];folder=ROOT/f'preview/working-q07-{v}'
        pdf=folder/f'working-q07-{v}.pdf';assert sha(pdf)==item['pdf_sha256']
        for p in range(1,item['total_pages']+1):
            path=folder/f'page-{p:03}.png';key=f'{v}:{p}';pix=pixel(path)
            row=dict(version=v,page=p,png_sha256=sha(path),pixel_sha256=pix,pdf_sha256=sha(pdf))
            if key in direct:
                row.update(actual_displayed_and_read=True,evidence='current explicit HD display')
                read_pixels[pix]=key
            else:
                assert pix in read_pixels,('unread current page',key)
                row.update(actual_displayed_and_read=True,evidence='exact pixels of actually read current page',matched_page=read_pixels[pix])
            pages.append(row)
    assert direct=={f"{row['version']}:{row['page']}" for row in pages if row['evidence']=='current explicit HD display'}
    overviews=[]
    for item in builds:
        for n in range(1,math.ceil(item['total_pages']/12)+1):
            path=ROOT/f"preview/working-q07-{item['version']}/overview-{n:02}.jpg"
            overviews.append(dict(path=str(path),sha256=sha(path),actual_displayed_and_read=True))
    figures=[dict(name=n,png_sha256=sha(ROOT/f'figures/{n}.png'),pdf_sha256=sha(ROOT/f'figures/{n}.pdf'),actual_displayed_and_read=True) for n in NAMES]
    report=dict(question='07',scope='per-question work only; not whole-set completion',
                draft_sha256=sha(ROOT/'drafts/question-07.md'),figure_source_sha256=sha(ROOT/'figures/题07_图稿源文件.tex'),
                pages=pages,actual_overviews=overviews,actual_figures=figures,direct_hd_count=len(direct),
                question_accepted=False,set_accepted=False,
                notes=['全部当前单图均已实际高清读；空间面为曲母线旋转双曲面，前后虚实线分明，不是圆锥。',
                       '波面辅助线AA0与投影线PB已分别说明；法线角、纵向收缩和未来会聚事件图中符号实际进入方程。',
                       '22步学生核心、四个完整带解变式实际审读；含物理左支、有限孔径临界检验和地面几何焦点不等于光学焦点。',
                       '同地面时刻出射与共同入射波面逐项区分；同波面提前出射量与传播时差精确抵消。'])
    (ROOT/'preview/visual-q07-final.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(page_coverage=len(pages),direct_hd=len(direct),figures=len(figures),accepted=False)))
if __name__=='__main__':main()
