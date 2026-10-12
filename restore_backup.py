#!/usr/bin/env python3
"""Restore the complete project snapshot from all release backup ZIP files."""
import argparse,ctypes,hashlib,json,os,shutil,stat,sys,zipfile
from pathlib import Path,PurePosixPath

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(4*1024**2),b''):h.update(b)
    return h.hexdigest()

def safe_path(root,name):
    p=PurePosixPath(name)
    if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe archive path: '+name)
    return root.joinpath(*p.parts)

def copy_file(src,dest):
    if sys.platform=='darwin':
        lib=ctypes.CDLL('/usr/lib/libSystem.B.dylib',use_errno=True)
        if lib.clonefile(os.fsencode(src),os.fsencode(dest),0)==0:return
    shutil.copy2(src,dest)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--destination',required=True,type=Path)
    ap.add_argument('--assets',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args();assets=args.assets.resolve();dest=args.destination.resolve()
    if dest.exists() and any(dest.iterdir()):raise SystemExit('Destination must be empty: '+str(dest))
    sums={}
    for line in (assets/'SHA256SUMS.txt').read_text().splitlines():
        sha,name=line.split('  ',1);sums[name]=sha
    archives=sorted(assets.glob('backup-*.zip'))
    expected=sorted(name for name in sums if name.startswith('backup-') and name.endswith('.zip'))
    if [p.name for p in archives]!=expected:raise SystemExit('Missing or unexpected backup ZIP files')
    for name,sha in sums.items():
        p=assets/name
        if not p.is_file() or digest(p)!=sha:raise SystemExit('Checksum failed: '+name)
    parts_index=assets/'archive-parts.json'
    if parts_index.exists():
        archives=[]
        assembly=assets/'.assembled';assembly.mkdir(exist_ok=True)
        for record in json.loads(parts_index.read_text())['archives']:
            if record['parts']:
                archive=assembly/record['name'];h=hashlib.sha256()
                with archive.open('wb') as out:
                    for name in record['parts']:
                        with (assets/name).open('rb') as part:
                            for b in iter(lambda:part.read(4*1024**2),b''):out.write(b);h.update(b)
                actual_sha=h.hexdigest()
            else:
                archive=assets/record['name'];actual_sha=digest(archive)
            if actual_sha!=record['sha256'] or archive.stat().st_size!=record['size']:
                raise SystemExit('Archive reconstruction failed: '+record['name'])
            archives.append(archive)
            print('Verified archive:',record['name'],flush=True)
    manifest=json.loads((assets/'snapshot-manifest.json').read_text())
    records=manifest['files'];canonical={r['path']:r for r in records if r['path']==r['canonical']}
    extracted=set();dest.mkdir(parents=True,exist_ok=True)
    for archive in archives:
        with zipfile.ZipFile(archive) as z:
            for item in z.infolist():
                name=item.filename
                if name not in canonical or name in extracted:raise SystemExit('Unexpected or duplicate member: '+name)
                target=safe_path(dest,name);target.parent.mkdir(parents=True,exist_ok=True);h=hashlib.sha256()
                with z.open(item) as src,target.open('xb') as out:
                    for b in iter(lambda:src.read(4*1024**2),b''):out.write(b);h.update(b)
                record=canonical[name]
                if h.hexdigest()!=record['sha256'] or target.stat().st_size!=record['size']:raise SystemExit('File checksum failed: '+name)
                os.chmod(target,record['mode']);os.utime(target,ns=(record['mtime_ns'],record['mtime_ns']))
                extracted.add(name)
        print('Restored archive:',archive.name,flush=True)
    if extracted!=set(canonical):raise SystemExit('Canonical files are missing')
    for r in records:
        target=safe_path(dest,r['path'])
        if r['path']!=r['canonical']:
            target.parent.mkdir(parents=True,exist_ok=True);copy_file(safe_path(dest,r['canonical']),target)
            os.chmod(target,r['mode']);os.utime(target,ns=(r['mtime_ns'],r['mtime_ns']))
        if not target.is_file() or target.stat().st_size!=r['size'] or digest(target)!=r['sha256']:raise SystemExit('Restored file failed: '+r['path'])
    for name in manifest['empty_directories']:safe_path(dest,name).mkdir(parents=True,exist_ok=True)
    for link in manifest['symlinks']:
        target=safe_path(dest,link['path']);target.parent.mkdir(parents=True,exist_ok=True)
        resolved=(target.parent/link['target']).resolve()
        if not resolved.is_relative_to(dest):raise SystemExit('Unsafe symbolic link: '+link['path'])
        os.symlink(link['target'],target)
    print('Complete:',len(records),'files;',len(manifest['symlinks']),'links;',manifest['logical_bytes'],'bytes',flush=True)
    print('Restored project:',dest,flush=True)
if __name__=='__main__':main()
