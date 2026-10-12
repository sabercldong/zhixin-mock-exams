"""渲染第029套原始资料并记录校验和，不改动原件。"""
from pathlib import Path
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]

def main():
    dest = ROOT / 'preview/originals'
    dest.mkdir(parents=True, exist_ok=True)
    record = {}
    for name, stem in [('试卷.pdf', 'paper'), ('答案.pdf', 'answer')]:
        source = ROOT.parent / name
        doc = fitz.open(source)
        record[name] = {'pages': len(doc), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}
        for i, page in enumerate(doc, 1):
            page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False).save(dest / f'{stem}-{i:02}.png')
    (dest / 'source-manifest.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(record, ensure_ascii=False))

if __name__ == '__main__':
    main()
