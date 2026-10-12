"""输出重点复审页面；不修改PDF或正文。页码为PDF物理页码。"""
from pathlib import Path
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    'paper': [3, 6, 7],
    'student': [11, 13, 15, 16, 17, 18, 19, 20, 21, 22,
                32, 36, 41, 48, 53, 65, 66, 69, 70, 75, 77],
    'teacher': [25, 26, 27, 88, 89, 100],
}


def main():
    dest = ROOT / 'preview/formal'
    dest.mkdir(exist_ok=True)
    for kind, label in [('paper', '试卷'), ('student', '学生详解'), ('teacher', '教师备课')]:
        doc = fitz.open(ROOT / 'output' / f'第034套_{label}版.pdf')
        for page in PAGES[kind]:
            assert 1 <= page <= len(doc)
            doc[page-1].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False).save(
                dest / f'{kind}-highres-{page:03}.png')
    (dest / 'highres-pages.json').write_text(json.dumps(PAGES, ensure_ascii=False, indent=2)+'\n')
    print(PAGES)


if __name__ == '__main__':
    main()
