import os
import sys
import time
from config import g1, g2, host, port, device, system, ping
import random
import shutil
from utils.colors import green, red, cyan, yellow, white, gray, blue, magenta, dim, bold
from utils.modUI import a1, a2, a3, a4, a5, a6, a7, a8

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
    m1 = []
    t1 = g1()
    for t2, m3 in t1.items():
        for m4 in m3:
            if m4 not in m1:
                m1.append(m4)
    return sorted(m1)

def a14():
    t1 = g1()
    return list(t1.keys())

def a15(p4):
    t1 = g1()
    n2 = list(t1.keys())
    if p4 < len(n2):
        return t1[n2[p4]]
    return []

def a16():
    try:
        from installer import a11 as installer_main
        installer_main()
    except:
        print(f"{red('[!] installer.py not found')}")
        time.sleep(1)

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        w = a11()
        h = a12()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        try:
            from display.banner import b1
            b1()
        except:
            print("+--- 23 KOD")
        
        i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
        try:
            from display.panels import p1
            p1("23 KOD", i1, "READY")
        except:
            print("+--- 23 KOD")
            print(f"| host:      {host}")
            print(f"| Port:        {port}")
            print(f"| Ping:     {ping}")
            print(f"| device:   {device}")
            print(f"| system:    {system}")
            print("|- Status: READY")
            print("------------------------------")
        
        n2 = a14()
        t1 = max(1, len(n2))
        
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        
        c2 = a15(p4)
        
        td = []
        for i, name in enumerate(n2):
            if i == p4:
                td.append(f"{green('[')}{name}{green(']')}")
            else:
                td.append(f"{gray(' ' + name + ' ')}")
        
        tl = ' '.join(td)
        print(f"\n{green('┌──────────────────────────────────────────────────────────┐')}")
        print(f"{green('│')} {cyan('Tabs:')} {tl}")
        print(f"{green('├──────────────────────────────────────────────────────────┤')}")
        
        if not c2:
            print(f"{green('│')} {red('(coming soon...)')}")
        else:
            for i, m5 in enumerate(c2, 1):
                print(f"{green('│')} {green(f'{i:2}')}. {m5}")
        
        print(f"{green('├──────────────────────────────────────────────────────────┤')}")
        print(f"{green('│')} {red('[0]')} Exit  {yellow('[s]')} Search  {cyan('[t#]')} Tab  {blue('[i]')} Install")
        print(f"{green('└──────────────────────────────────────────────────────────┘')}")
        print()
        
        sys.stdout.flush()
        try:
            c1 = input(f"{green('>')} ").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{red('[!] Exiting...')}")
            break
        
        if c1 == "0":
            print(f"{red('[!] Exiting...')}")
            break
        
        if c1 == "s":
            q1 = input(f"{yellow('Search:')} ").strip()
            found = []
            for tn, mods in g1().items():
                for mod in mods:
                    if q1.lower() in mod.lower():
                        found.append(f"{tn}: {mod}")
            if found:
                print(f"\n{green('[+] Found:')}")
                for f in found:
                    print(f"    {cyan('-')} {f}")
            else:
                print(f"\n{red('[!] No matches found')}")
            input(f"\n{green('>')} ")
            continue
        
        if c1 == "i":
            a16()
            continue
        
        if c1.startswith('t') and len(c1) > 1:
            try:
                t2 = int(c1[1:])
                if 1 <= t2 <= t1:
                    p4 = t2 - 1
                    print(f"\n{green('[✓] Switched to:')} {n2[p4]}")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"\n{red('[!] Tab')} {t2} {red('invalid (1-')}{t1}{red(')')}")
                    time.sleep(1)
                    continue
            except:
                print(f"\n{red('[!] Invalid tab number')}")
                time.sleep(1)
                continue
        
        if not c1.isdigit():
            print(f"\n{red('[!] Invalid option')}")
            time.sleep(1)
            continue
        
        i2 = int(c1) - 1
        c2 = a15(p4)
        
        if c2 and 0 <= i2 < len(c2):
            m5 = c2[i2]
            m6 = a9(m5)
            if m6:
                mod = a1(m6)
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
                        print(f"\n{green('┌──────────────────────────────────────────────────────────┐')}")
                        ol = list(mo.keys())
                        for i, key in enumerate(ol, 1):
                            cur = co.get(key, mo[key].get('default', ''))
                            print(f"{green('│')} {green(f'{i}')}. {key} = {yellow(cur)}")
                        print(f"{green('└──────────────────────────────────────────────────────────┘')}")
                        print()
                        print(f"  {yellow('Format:')} {cyan('<num> <val>')}")
                        print(f"  {gray('Enter to keep current')}")
                        print()
                        
                        try:
                            inp = input(f"{green('>')} ").strip()
                            if inp and inp != "0":
                                parts = inp.split()
                                if len(parts) >= 2:
                                    num = int(parts[0])
                                    val = ' '.join(parts[1:])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        co[key] = val
                                        print(f"\n{green('[✓]')} {key} = {val}")
                                    else:
                                        print(f"\n{red('[!] Invalid number')}")
                                elif len(parts) == 1 and parts[0].isdigit():
                                    num = int(parts[0])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        cur = co.get(key, mo[key].get('default', ''))
                                        print(f"\n{yellow('  ')}{key} = {cur}")
                                        new_val = input(f"{green('  New:')} ").strip()
                                        if new_val:
                                            co[key] = new_val
                                            print(f"\n{green('[✓]')} {key} = {new_val}")
                                    else:
                                        print(f"\n{red('[!] Invalid number')}")
                                else:
                                    print(f"\n{red('[!] Format: <num> <val>')}")
                        except ValueError:
                            print(f"\n{red('[!] Invalid input')}")
                        time.sleep(0.8)
                            
                    elif choice == "3":
                        print(f"\n{blue('[✓] Returning...')}")
                        time.sleep(0.5)
                        break
                        
                    elif choice == "0":
                        print(f"{red('[!] Exiting...')}")
                        sys.exit(0)
                    else:
                        print(f"\n{red('[!] Invalid')}")
                        time.sleep(0.5)
            else:
                print(f"\n{red('[!] Module')} {m5} {red('not found!')}")
                print(f"{gray('  Searched: EVERYWHERE')}")
                input(f"{green('>')} ")
        else:
            if c2:
                print(f"\n{red('[!] Invalid option')}")
            else:
                print(f"\n{red('[!] No modules')}")
            time.sleep(1)
