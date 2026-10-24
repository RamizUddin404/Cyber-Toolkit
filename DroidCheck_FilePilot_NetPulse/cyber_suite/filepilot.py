"""Conservative file utilities; no deletion is implemented."""
import os, hashlib, shutil
from pathlib import Path
from collections import Counter

def safe_root(path):
    p=Path(path).expanduser().resolve()
    if not p.exists() or not p.is_dir(): raise ValueError('Choose an existing directory.')
    return p

def browse(path, limit=60):
    root=safe_root(path); entries=[]
    for p in sorted(root.iterdir(), key=lambda x:(not x.is_dir(),x.name.lower()))[:limit]:
        try: entries.append({'name':p.name+('/' if p.is_dir() else ''),'type':'directory' if p.is_dir() else 'file','size_bytes':p.stat().st_size if p.is_file() else None})
        except OSError: entries.append({'name':p.name,'type':'unavailable','size_bytes':None})
    return {'root':str(root),'entries':entries}

def search_names(path, query, limit=100):
    root=safe_root(path); found=[]; needle=query.casefold()
    for base,dirs,names in os.walk(root,followlinks=False):
        dirs[:]=[d for d in dirs if not (Path(base)/d).is_symlink()]
        for name in names:
            if needle in name.casefold():
                found.append(str(Path(base)/name))
                if len(found)>=limit: return {'root':str(root),'matches':found,'truncated':True}
    return {'root':str(root),'matches':found,'truncated':False}

def sha256_file(path):
    p=Path(path).expanduser().resolve(strict=True)
    if not p.is_file(): raise ValueError('Target must be a regular file.')
    digest=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): digest.update(chunk)
    return {'path':str(p),'sha256':digest.hexdigest(),'size_bytes':p.stat().st_size}

def large_files(path,min_mb=10,limit=30):
    root=safe_root(path); threshold=max(0,float(min_mb))*1024*1024; found=[]
    for base,dirs,names in os.walk(root,followlinks=False):
        dirs[:]=[d for d in dirs if not (Path(base)/d).is_symlink()]
        for name in names:
            p=Path(base)/name
            try:
                if p.is_symlink(): continue
                size=p.stat().st_size
                if size>=threshold: found.append({'path':str(p),'size_bytes':size})
            except OSError: continue
    found.sort(key=lambda x:x['size_bytes'],reverse=True)
    return {'root':str(root),'minimum_mb':min_mb,'files':found[:limit]}

def organize_by_extension(path,dry_run=True):
    """Preview first, then move files into extension folders; never overwrite."""
    root=safe_root(path); plan=[]
    for p in root.iterdir():
        if p.is_symlink() or not p.is_file(): continue
        ext=p.suffix.lower().lstrip('.') or 'no_extension'; dest=root/ext/p.name
        plan.append({'source':str(p),'destination':str(dest),'status':'skipped_exists' if dest.exists() else 'planned'})
    if not dry_run:
        for item in plan:
            if item['status']!='planned': continue
            src,dst=Path(item['source']),Path(item['destination'])
            try:
                dst.parent.mkdir(exist_ok=True)
                if dst.exists(): item['status']='skipped_exists'
                else: shutil.move(str(src),str(dst)); item['status']='moved'
            except OSError as exc: item['status']=f'error: {exc}'
    return {'root':str(root),'dry_run':dry_run,'items':plan,'counts':dict(Counter(x['status'] for x in plan))}
