"""Rich terminal dashboard: colorful panels, animated status and 15 menu items."""
import json, os, socket, sys, time
from . import droidcheck,filepilot,netpulse
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt
    from rich.align import Align
    from rich.columns import Columns
    from rich import box
    RICH=True; console=Console()
except ImportError:
    RICH=False; console=None
MENU=[('01','System & runtime summary','DroidCheck'),('02','Storage usage','DroidCheck'),('03','Process overview','DroidCheck'),('04','Python package inventory','DroidCheck'),('05','Export diagnostic report','DroidCheck'),('06','Browse a directory','FilePilot'),('07','Search filenames','FilePilot'),('08','Organize by extension (preview first)','FilePilot'),('09','SHA-256 file hash','FilePilot'),('10','Find large files','FilePilot'),('11','Internet connectivity & latency','NetPulse'),('12','DNS lookup','NetPulse'),('13','Local network interfaces','NetPulse'),('14','Check one host + TCP port','NetPulse'),('15','Save network report','NetPulse')]
def say(message=''):
    console.print(message) if RICH else print(message)
def ask(prompt,default=''):
    if RICH: return Prompt.ask(prompt,default=default)
    value=input(f'{prompt} [{default}]: ').strip(); return value or default
def banner():
    if RICH:
        title=Text('DROIDCHECK  /  FILEPILOT  /  NETPULSE',style='bold bright_cyan')
        sub=Text('LOCAL DIAGNOSTICS  •  FILE WORKFLOW  •  AUTHORIZED NETWORK AUDIT',style='bold magenta')
        state=Text('◆ SYSTEMS READY     ◈ SAFE MODE     ◉ 15 UTILITIES',style='bold bright_green')
        console.print(Panel(Align.center(Text.assemble(title,'\n',sub,'\n\n',state)),border_style='bright_cyan',box=box.DOUBLE,padding=(1,2)))
    else:
        print('\033[96m╔════ DROIDCHECK / FILEPILOT / NETPULSE ════╗\033[0m')
        print('\033[95m  SYSTEM DIAGNOSTICS • FILE AUTOMATION • NETWORK\033[0m')
        print('\033[92m  SAFE MODE ENABLED • 15 UTILITIES\033[0m')
def intro():
    frames=['[■□□□□□□□□□]','[■■■□□□□□□□]','[■■■■■■□□□□]','[■■■■■■■■□□]','[■■■■■■■■■■]']
    if RICH:
        with console.status('[bold bright_cyan]Initializing modules...',spinner='dots') as s:
            for frame in frames: s.update(f'[bold bright_cyan]Initializing modules {frame}'); time.sleep(.07)
    elif sys.stdout.isatty():
        for frame in frames: print(f'\r\033[96mBoot {frame}\033[0m',end='',flush=True); time.sleep(.07)
        print()
def menu():
    if RICH:
        groups={}
        for n,label,group in MENU: groups.setdefault(group,[]).append((n,label))
        styles={'DroidCheck':'bright_cyan','FilePilot':'bright_magenta','NetPulse':'bright_green'}; panels=[]
        for group,items in groups.items():
            table=Table(box=box.SIMPLE_HEAVY,show_header=False,expand=True,padding=(0,1)); table.add_column('ID',style=styles[group],width=4); table.add_column('UTILITY',style='white')
            for n,label in items: table.add_row(n,label)
            panels.append(Panel(table,title=f'[bold {styles[group]}]{group}[/]',border_style=styles[group],padding=(0,1)))
        console.print(Columns(panels,equal=True,expand=True)); console.print('[dim]Enter 00 to exit • Ctrl+C also exits[/dim]')
    else:
        for n,label,group in MENU: print(f'\033[96m{n}\033[0m  {label:39} [{group}]')
        print('00 Exit')
def show(data):
    rendered=json.dumps(data,indent=2,ensure_ascii=False,default=str)
    console.print(Panel(rendered,border_style='bright_blue',title='[bold]RESULT[/]')) if RICH else print(rendered)
def path_prompt(label='Directory',default=None): return ask(label,default or os.getcwd()).strip()
def run_action(c):
    if c=='01': show(droidcheck.system_summary())
    elif c=='02': show(droidcheck.storage_summary(path_prompt('Path',os.path.expanduser('~'))))
    elif c=='03': show(droidcheck.process_overview())
    elif c=='04': show(droidcheck.package_inventory())
    elif c=='05':
        data={'system':droidcheck.system_summary(),'storage':droidcheck.storage_summary(os.path.expanduser('~')),'processes':droidcheck.process_overview(),'packages':droidcheck.package_inventory()}
        show({'saved_to':droidcheck.export_report(data,ask('Output filename','droidcheck_report.json'))})
    elif c=='06': show(filepilot.browse(path_prompt()))
    elif c=='07': show(filepilot.search_names(path_prompt(),ask('Filename contains')))
    elif c=='08':
        root=path_prompt(); show(filepilot.organize_by_extension(root,True))
        if ask('Type MOVE to apply preview','CANCEL')=='MOVE': show(filepilot.organize_by_extension(root,False))
        else: say('[yellow]No files moved. Preview only.[/]' if RICH else 'No files moved. Preview only.')
    elif c=='09': show(filepilot.sha256_file(ask('File path')))
    elif c=='10': show(filepilot.large_files(path_prompt(),float(ask('Minimum size in MB','10'))))
    elif c=='11': show(netpulse.connectivity_check(ask('HTTPS URL','https://example.com')))
    elif c=='12': show(netpulse.dns_lookup(ask('Hostname')))
    elif c=='13': show(netpulse.interface_summary())
    elif c=='14':
        host=ask('Authorized host name or IP'); port=ask('Single TCP port','443')
        if ask('Type CHECK to test only this host/port','CANCEL')=='CHECK': show(netpulse.check_single_tcp_port(host,int(port)))
        else: say('Cancelled.')
    elif c=='15': show({'saved_to':netpulse.save_report({'connectivity':netpulse.connectivity_check(),'interfaces':netpulse.interface_summary()},ask('Output filename','netpulse_report.json'))})
    else: say('Unknown menu item.')
def main():
    intro()
    while True:
        try:
            if RICH: console.clear()
            banner(); menu(); c=ask('\nSelect utility','00').strip().lower()
            if c in {'00','0','q','quit','exit'}: say('[bold bright_cyan]Session closed. Stay curious. Stay ethical.[/]' if RICH else 'Session closed.'); break
            started=time.perf_counter()
            try: run_action(c.zfill(2))
            except Exception as exc: say(f'[bold red]Operation failed:[/] {type(exc).__name__}: {exc}' if RICH else f'Operation failed: {type(exc).__name__}: {exc}')
            say(f'[dim]Completed in {time.perf_counter()-started:.2f}s[/]' if RICH else f'Completed in {time.perf_counter()-started:.2f}s')
            ask('Press Enter to return to menu','')
        except (KeyboardInterrupt,EOFError): say('\nSession closed.'); break
