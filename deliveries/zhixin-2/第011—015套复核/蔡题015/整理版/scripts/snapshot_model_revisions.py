"""Recoverable snapshot before the user's four authorized model revisions."""
from pathlib import Path
import hashlib,json,shutil
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def main():
    target=ROOT/'revision-history/before-four-model-revisions-20261009'
    assert not target.exists(), 'Snapshot already exists; do not replace it'
    target.mkdir(parents=True)
    for name in ['drafts','build','scripts','figures','latex']:
        shutil.copytree(ROOT/name,target/name)
    for q in ['01','03','05','06']:
        for version in ['student','teacher']:
            folder=Path(f'preview/working-q{q}-{version}')
            shutil.copytree(ROOT/folder,target/folder)
        for path in (ROOT/'preview').glob(f'*q{q}.json'):
            dest=target/path.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(path,dest)
    files={str(p.relative_to(target)):hashlib.sha256(p.read_bytes()).hexdigest()
           for p in target.rglob('*') if p.is_file()}
    manifest=dict(created_utc=datetime.now(timezone.utc).isoformat(),source=str(ROOT),
                  scope='pre-revision historical evidence, not current acceptance',files=files)
    (target/'snapshot-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(snapshot=str(target),files=len(files))))
if __name__=='__main__':main()
