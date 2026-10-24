"""Narrow, timeout-limited network diagnostics."""
import json, socket, time, urllib.request
from datetime import datetime, timezone

def connectivity_check(url='https://example.com',timeout=4):
    started=time.perf_counter(); req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'NetPulse/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=max(1,min(float(timeout),8))) as response:
            return {'url':url,'reachable':True,'status':response.status,'latency_ms':round((time.perf_counter()-started)*1000,2)}
    except Exception as exc:
        return {'url':url,'reachable':False,'error':str(exc),'latency_ms':round((time.perf_counter()-started)*1000,2)}

def dns_lookup(hostname):
    hostname=hostname.strip()
    if not hostname or len(hostname)>253 or any(c.isspace() for c in hostname): raise ValueError('Enter a valid hostname.')
    addresses=sorted({item[4][0] for item in socket.getaddrinfo(hostname,None,type=socket.SOCK_STREAM)})
    return {'hostname':hostname,'addresses':addresses}

def interface_summary():
    try: import psutil
    except ImportError: return {'note':'Install psutil for interface details.','interfaces':{}}
    result={}
    for name,addresses in psutil.net_if_addrs().items():
        result[name]=[]
        for a in addresses:
            family='IPv4' if a.family==socket.AF_INET else 'IPv6' if a.family==socket.AF_INET6 else str(a.family)
            result[name].append({'family':family,'address':a.address,'netmask':a.netmask,'broadcast':a.broadcast})
    return {'interfaces':result}

def check_single_tcp_port(host,port,timeout=2.5):
    """Check one explicitly provided host and TCP port. This is not a scanner."""
    host=host.strip(); port=int(port)
    if not host or len(host)>253: raise ValueError('Enter a valid host.')
    if not 1<=port<=65535: raise ValueError('Port must be between 1 and 65535.')
    started=time.perf_counter()
    try:
        with socket.create_connection((host,port),timeout=max(.5,min(float(timeout),4))):
            return {'host':host,'port':port,'reachable':True,'elapsed_ms':round((time.perf_counter()-started)*1000,2)}
    except OSError as exc:
        return {'host':host,'port':port,'reachable':False,'error':str(exc),'elapsed_ms':round((time.perf_counter()-started)*1000,2)}

def save_report(data,filename='netpulse_report.json'):
    with open(filename,'w',encoding='utf-8') as f: json.dump({'generated_utc':datetime.now(timezone.utc).isoformat(),'report':data},f,indent=2,default=str)
    return filename
