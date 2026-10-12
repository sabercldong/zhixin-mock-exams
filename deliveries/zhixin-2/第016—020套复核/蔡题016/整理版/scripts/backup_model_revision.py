"""Recoverable snapshot of generated files before the five approved revisions."""
from pathlib import Path
import hashlib, json, shutil

PROJECT = Path(__file__).resolve().parents[3]
TAG = '2026-10-09_五项模型修订前'

def main():
    for number in ['020', '019', '016']:
        root = PROJECT / ('蔡题'+number) / '整理版'
        dest = root / 'revisions' / TAG
        marker = dest / 'snapshot-manifest.json'
        if marker.exists():
            print(number, 'snapshot already exists; unchanged', flush=True)
            continue
        dest.mkdir(parents=True, exist_ok=True)
        files = []
        for dirname in ['drafts', 'scripts', 'markdown', 'latex', 'build', 'output/pdf']:
            folder = root / dirname
            if folder.exists():
                files += [path for path in folder.rglob('*') if path.is_file()
                          and '__pycache__' not in path.parts]
        preview = root/'preview'
        files += list(preview.glob('visual-reviewed-*.json'))
        for dirname in ['full-paper', 'full-student', 'full-teacher']:
            folder = preview / dirname
            if folder.exists(): files += [path for path in folder.rglob('*') if path.is_file()]
        record = []
        for path in sorted(set(files)):
            rel = path.relative_to(root)
            target = dest/rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
            record.append(dict(path=str(rel), sha256=digest))
        marker.write_text(json.dumps(dict(reason='retain all pre-revision generated sources and evidence',
            originals_not_copied_or_changed=True, files=record), ensure_ascii=False, indent=2)+'\n')
        print(number, len(record), 'files preserved', flush=True)

if __name__ == '__main__': main()
