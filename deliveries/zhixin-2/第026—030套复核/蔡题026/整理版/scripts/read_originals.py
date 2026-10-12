"""第026套原始试卷只读提取和渲染，不修改源PDF。"""
from pathlib import Path
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]

def main():
    source = ROOT.parent / '试卷.pdf'
    dest = ROOT / 'preview/originals'
    dest.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(source)
    record = {'试卷.pdf': {'pages': len(doc), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}}
    for i, page in enumerate(doc, 1):
        page.get_pixmap(matrix=fitz.Matrix(1.9, 1.9), alpha=False).save(dest / f'paper-{i:02}.png')
        print(f'PAGE {i}: {page.get_text()}')
    (dest / 'source-manifest.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(record, ensure_ascii=False))

if __name__ == '__main__':
    main()
