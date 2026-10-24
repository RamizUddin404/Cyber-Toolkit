"""Local device/runtime diagnostics. No privileged access is attempted."""
import os, sys, json, platform, shutil, importlib.metadata
from datetime import datetime, timezone
try:
    import psutil
except ImportError:
    psutil = None

def system_summary():
    result = {'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'platform': platform.platform(), 'system': platform.system(), 'release': platform.release(), 'machine': platform.machine(), 'python': sys.version.split()[0], 'executable': sys.executable, 'working_directory': os.getcwd(), 'home_directory': os.path.expanduser('~'), 'cpu_count_logical': os.cpu_count()}
    if psutil:
        try:
            result['boot_time_epoch'] = psutil.boot_time()
            vm = psutil.virtual_memory()
            result['memory'] = {'total_bytes': vm.total, 'available_bytes': vm.available, 'percent_used': vm.percent}
        except (OSError, PermissionError): pass
    return result

def storage_summary(path=None):
    path = os.path.abspath(path or os.path.expanduser('~'))
    total, used, free = shutil.disk_usage(path)
    return {'path': path, 'total_bytes': total, 'used_bytes': used, 'free_bytes': free, 'percent_used': round(used / total * 100, 2) if total else 0}

def process_overview(limit=15):
    if not psutil: return {'note': 'Install psutil for process details.', 'processes': []}
    rows=[]
    for p in psutil.process_iter(['pid','name','username','memory_info']):
        try:
            i=p.info; m=i.get('memory_info')
            rows.append({'pid':i.get('pid'),'name':i.get('name') or '?','user':i.get('username') or '?','rss_bytes':m.rss if m else None})
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess): continue
    rows.sort(key=lambda x:x['rss_bytes'] or 0, reverse=True)
    return {'processes': rows[:max(1,min(limit,50))]}

def package_inventory(limit=150):
    pkgs=sorted([{'name':d.metadata.get('Name','unknown'),'version':d.version} for d in importlib.metadata.distributions()], key=lambda x:x['name'].lower())
    return {'total':len(pkgs),'packages':pkgs[:limit],'truncated':len(pkgs)>limit}

def export_report(data, filename='droidcheck_report.json'):
    target=os.path.abspath(filename)
    with open(target,'w',encoding='utf-8') as f: json.dump(data,f,indent=2,default=str)
    return target
