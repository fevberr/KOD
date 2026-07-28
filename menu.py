import os
import sys
import time
from config import a7 as get_tabs, a8 as get_tab
from config import host, port, device, system, ping
import random
import shutil
from utils.colors import reload_colors, color_settings_menu
from utils.modUI import a1 as mod_load, a2, a3, a4, a5, a6, a7, a8

def a9(n):
    if os.path.exists(f"modules/{n}"):
        return f"modules/{n}"
    if os.path.exists("modules"):
        for r, d, f in os.walk("modules"):
            if n in f:
                return os.path.join(r, n)
    if os.path.exists("."):
        for r, d, f in os.walk("."):
            if ".git" in r or "__pycache__" in r:
                continue
            if n in f:
                return os.path.join(r, n)
    return None

def a10():
    try:
        return shutil.get_terminal_size()
    except:
        return os.terminal_size((80, 24))

def a11():
    return a10().columns

def a12():
    return a10().lines

def a13():
    m = []
    t = get_tabs()
    for t2, m3 in t.items():
        for m4 in m3:
            if m4 not in m:
                m.append(m4)
    return sorted(m)

def a14():
    t = get_tabs()
    return list(t.keys())

def a15(p):
    t = get_tabs()
    n = list(t.keys())
    if p < len(n):
        return t[n[p]]
    return []

def a16():
    try:
        from installer import a11 as installer_main
        installer_main()
    except:
        print(f"\033[91m[!] installer.py not found\033[0m")
        time.sleep(1)

def a17(t, m):
    if len(t) > m:
        return t[:m-2] + "…"
    return t

def a18(t, w):
    if len(t) >= w:
        return t
    p = (w - len(t)) // 2
    return " " * p + t

def a19():
    try:
        color_settings_menu()
        reload_colors()
    except Exception as e:
        print(f"\033[91m[!] Color error:\033[0m {e}")
        time.sleep(2)

def col1(t): return f"\033[92m{t}\033[0m"
def col2(t): return f"\033[91m{t}\033[0m"
def col3(t): return f"\033[96m{t}\033[0m"
def col4(t): return f"\033[93m{t}\033[0m"
def col5(t): return f"\033[97m{t}\033[0m"
def col6(t): return f"\033[90m{t}\033[0m"
def col7(t): return f"\033[94m{t}\033[0m"
def col8(t): return f"\033[95m{t}\033[0m"

def m1():
    p4 = 0
    q1 = ""
    
    reload_colors()
    
    while True:
        reload_colors()
        
        w = a11()
        h = a12()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        try:
            from display.banner import a3 as b1
            b1()
        except Exception as e:
            print(col3("+--- 23 KOD"))
            print(f"{col6('  (Banner error:')} {e}{col6(')')}")
        
        w = a11()
        if w < 60:
            i1 = f"host: {a17(host, 20)}\nport:{port}\nping:{ping}ms\ndev:{a17(device, 10)}"
            try:
                from display.panels import p1
                p1("23 KOD", i1, "READY")
            except:
                print(col3("+--- 23 KOD"))
                print(col3("| ") + col5(f"{a17(host, 25)}"))
                print(col3("| ") + col5(f"{port}"))
                print(col3("| ") + col4(f"{ping}ms"))
                print(col3("|- ") + col1("READY"))
                print(col3("-" * min(w, 30)))
        else:
            i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
            try:
                from display.panels import p1
                p1("23 KOD", i1, "READY")
            except:
                print(col3("+--- 23 KOD"))
                print(col3("| ") + col5(f"host:      {host}"))
                print(col3("| ") + col5(f"Port:        {port}"))
                print(col3("| ") + col4(f"Ping:     {ping}"))
                print(col3("| ") + col8(f"device:   {device}"))
                print(col3("| ") + col8(f"system:    {system}"))
                print(col3("|- ") + col1("Status: READY"))
                print(col3("-" * min(w, 30)))
        
        n2 = a14()
        t1 = max(1, len(n2))
        
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        
        c2 = a15(p4)
        
        tw = min(w - 14, 60)
        td = []
        for i, name in enumerate(n2):
            dn = a17(name, max(4, (tw // max(1, len(n2))) - 2))
            if i == p4:
                td.append(f"{col1('[')}{col3(dn)}{col1(']')}")
            else:
                td.append(f"{col6(' ' + dn + ' ')}")
        
        tl = ' '.join(td)
        if len(tl) > tw:
            td = []
            visible = max(1, min(len(n2), tw // 8))
            for i, name in enumerate(n2[:visible]):
                dn = a17(name, max(3, (tw // visible) - 2))
                if i == p4:
                    td.append(f"{col1('[')}{col3(dn)}{col1(']')}")
                else:
                    td.append(f"{col6(dn)}")
            if len(n2) > visible:
                td.append(f"{col6('…')}")
            tl = ' '.join(td)
        
        print(f"\n{col1('┌─ Menu ')}{col1('─' * min(w-10, 40))}")
        print(f"{col1('│')} {col3('Tabs:')} {tl}")
        print(f"{col1('├' + '─' * min(w-4, 50))}")
        
        if not c2:
            print(f"{col1('│')} {col2('(coming soon...)')}")
        else:
            max_items = min(len(c2), max(1, h - 10))
            for i, m5 in enumerate(c2[:max_items], 1):
                dn = a17(m5, max(1, w - 14))
                if w < 60:
                    print(f"{col1('│')} {col4(str(i))}.{col3(dn)}")
                else:
                    print(f"{col1('│')} {col4(f'{i:2}')}. {col3(dn)}")
            if len(c2) > max_items:
                print(f"{col1('│ ...')} {len(c2)-max_items} more")
        
        if w < 60:
            print(f"{col1('├' + '─' * min(w-4, 30))}")
            print(f"{col1('│')} {col2('[0]')} {col4('[s]')} {col3('[t#]')} {col7('[i]')} {col8('[c]')}")
            print(f"{col1('│')} {col6('  Exit   Search   Tab     Install  Colors')}")
        else:
            print(f"{col1('├' + '─' * min(w-4, 50))}")
            print(f"{col1('│')} {col2('[0]')} Exit  {col4('[s]')} Search  {col3('[t#]')} Tab  {col7('[i]')} Install  {col8('[c]')} Colors")
        
        print(f"{col1('└' + '─' * min(w-4, 50))}")
        print()
        
        sys.stdout.flush()
        try:
            ch = input(f"{col1('>')} ").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{col2('[!] Exiting...')}")
            break
        
        if ch == "0":
            print(f"{col2('[!] Exiting...')}")
            break
        
        if ch == "s":
            q1 = input(f"{col4('Search:')} ").strip()
            found = []
            for tn, mods in get_tabs().items():
                for mod in mods:
                    if q1.lower() in mod.lower():
                        found.append(f"{tn}: {mod}")
            if found:
                print(f"\n{col1('[+] Found:')}")
                for f in found[:min(10, h-6)]:
                    print(f"    {col3('-')} {a17(f, w-6)}")
                if len(found) > 10:
                    print(f"    ... and {len(found)-10} more")
            else:
                print(f"\n{col2('[!] No matches found')}")
            input(f"\n{col1('>')} ")
            continue
        
        if ch == "i":
            a16()
            continue
        
        if ch == "c":
            a19()
            continue
        
        if ch.startswith('t') and len(ch) > 1:
            try:
                t2 = int(ch[1:])
                if 1 <= t2 <= t1:
                    p4 = t2 - 1
                    print(f"\n{col1('[✓] Switched to:')} {col3(n2[p4])}")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"\n{col2('[!] Tab')} {t2} {col2('invalid (1-')}{t1}{col2(')')}")
                    time.sleep(1)
                    continue
            except:
                print(f"\n{col2('[!] Invalid tab number')}")
                time.sleep(1)
                continue
        
        if not ch.isdigit():
            print(f"\n{col2('[!] Invalid option')}")
            time.sleep(1)
            continue
        
        i2 = int(ch) - 1
        c2 = a15(p4)
        
        if c2 and 0 <= i2 < len(c2):
            m5 = c2[i2]
            m6 = a9(m5)
            if m6:
                mod = mod_load(m6)
                mo = {}
                co = {}
                
                if hasattr(mod, 'OPTIONS'):
                    mo = mod.OPTIONS
                    for key, value in mo.items():
                        if 'default' in value:
                            co[key] = value['default']
                
                while True:
                    choice = a6(m5[:-3], mo, co)
                    
                    if choice == "1":
                        a7(m6, co if co else None)
                        
                    elif choice == "2" and mo:
                        print(f"\n{col1('┌─ Options ')}{col1('─' * min(w-15, 40))}")
                        ol = list(mo.keys())
                        for i, key in enumerate(ol, 1):
                            cur = co.get(key, mo[key].get('default', ''))
                            print(f"{col1('│')} {col4(f'{i}')}. {col3(key)} = {col4(cur)}")
                        print(f"{col1('└' + '─' * min(w-4, 50))}")
                        print()
                        print(f"  {col4('Format:')} {col3('<num> <val>')}")
                        print(f"  {col6('Enter to keep current')}")
                        print()
                        
                        try:
                            inp = input(f"{col1('>')} ").strip()
                            if inp and inp != "0":
                                parts = inp.split()
                                if len(parts) >= 2:
                                    num = int(parts[0])
                                    val = ' '.join(parts[1:])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        co[key] = val
                                        print(f"\n{col1('[✓]')} {key} = {val}")
                                    else:
                                        print(f"\n{col2('[!] Invalid number')}")
                                elif len(parts) == 1 and parts[0].isdigit():
                                    num = int(parts[0])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        cur = co.get(key, mo[key].get('default', ''))
                                        print(f"\n{col4('  ')}{key} = {cur}")
                                        new_val = input(f"{col1('  New:')} ").strip()
                                        if new_val:
                                            co[key] = new_val
                                            print(f"\n{col1('[✓]')} {key} = {new_val}")
                                    else:
                                        print(f"\n{col2('[!] Invalid number')}")
                                else:
                                    print(f"\n{col2('[!] Format: <num> <val>')}")
                        except ValueError:
                            print(f"\n{col2('[!] Invalid input')}")
                        time.sleep(0.8)
                            
                    elif choice == "3":
                        print(f"\n{col7('[✓] Returning...')}")
                        time.sleep(0.5)
                        break
                        
                    elif choice == "0":
                        print(f"{col2('[!] Exiting...')}")
                        sys.exit(0)
                    else:
                        print(f"\n{col2('[!] Invalid')}")
                        time.sleep(0.5)
            else:
                print(f"\n{col2('[!] Module')} {m5} {col2('not found!')}")
                print(f"{col6('  Searched: EVERYWHERE')}")
                input(f"{col1('>')} ")
        else:
            if c2:
                print(f"\n{col2('[!] Invalid option')}")
            else:
                print(f"\n{col2('[!] No modules')}")
            time.sleep(1)

__all__ = ['m1']
