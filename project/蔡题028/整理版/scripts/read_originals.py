"""第028套仅有试卷原件；无手写答案。只读渲染并保存校验和。"""
from pathlib import Path
import hashlib, json, fitz
ROOT = Path(__file__).resolve().parents[1]
dest = ROOT / 'preview/originals'
dest.mkdir(parents=True, exist_ok=True)
source = ROOT.parent / '试卷.pdf'
doc = fitz.open(source)
record = {'试卷.pdf': {'pages': len(doc), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()}}
for i, page in enumerate(doc, 1):
    page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7), alpha=False).save(dest / f'paper-{i:02}.png')
(dest / 'source-manifest.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False))
