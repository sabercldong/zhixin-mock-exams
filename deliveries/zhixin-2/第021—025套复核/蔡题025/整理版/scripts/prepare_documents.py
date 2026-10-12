"""教师主文件为编辑入口；首次可显式从分题稿汇入。"""
from pathlib import Path
import argparse
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parents[1]))
from document_pipeline import prepare_set


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--from-drafts',action='store_true')
    args=parser.parse_args()
    md=ROOT/'markdown';md.mkdir(exist_ok=True)
    master=md/'蔡题025_教师备课.md'
    if args.from_drafts:
        blocks=[(ROOT/'drafts'/f'question-{q:02}.md').read_text().strip() for q in range(1,9)]
        front='---\ntitle: "第025套"\nshorttitle: "第025套"\nauthor: "物理竞赛资料"\ntoc: false\n---\n'
        master.write_text(front+'\n\n\\newpage\n\n'.join(blocks)+'\n')
    assert master.exists(),'首次汇入请使用 --from-drafts；以后直接编辑教师主文件。'
    prepare_set('025')


if __name__=='__main__':main()
