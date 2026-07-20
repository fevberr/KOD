import os
import sys
import time
from config import g1, g2, host, port, device, system, ping
import random
import shutil
from utils.colors import green, red, cyan, yellow, white, gray, blue, magenta, dim, bold

def get_terminal_size():
    try:
        return shutil.get_terminal_size()
    except:
        return os.terminal_size((80, 24))

def get_width():
    return get_terminal_size().columns

def get_height():
    return get_terminal_size().lines

def truncate(text, max_len):
    if len(text) > max_len:
        return text[:max_len-3] + "..."
    return text

def m2():
    m1 = []
    t1 = g1()
    for t2, m3 in t1.items():
        for m4 in m3:
            if m4 not in m1:
                m1.append(m4)
    return sorted(m1)

def n1():
    t1 = g1()
    return list(t1.keys())

def o1(p4):
    t1 = g1()
    n2 = list(t1.keys())
    if p4 < len(n2):
        return t1[n2[p4]]
    return []

def anim(text, delay=0.008):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fast(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_rain():
    chars = "01!@#$%^&*()_+{}|:<>?~"
    width = get_width()
    for _ in range(2):
        line = ''.join(random.choice(chars) for _ in range(min(width, 50)))
        sys.stdout.write(f"\r{gray(line)}")
        sys.stdout.flush()
        time.sleep(0.015)
    print("\r" + " " * min(width, 50), end="")
    print("\r", end="")

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        width = get_width()
        height = get_height()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if width < 40:
            try:
                from display.banner import b1
                b1()
            except:
                print("+--- 23 KOD")
            
            i1 = f"host: {host}\nport: {port}\nping: {ping}\ndevice: {device}"
            try:
                from display.panels import p1
                p1("23 KOD", i1, "READY")
            except:
                print("+--- 23 KOD")
                print(f"| {host}")
                print(f"| {port}")
                print(f"| {ping}ms")
                print("|- READY")
                print("------------------------------")
        else:
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
        
        n2 = n1()
        t1 = max(1, len(n2))
        
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        
        c2 = o1(p4)
        
        tab_width = min(width - 10, 60)
        tab_display = []
        for i, name in enumerate(n2):
            display_name = truncate(name, 12)
            if i == p4:
                tab_display.append(f"{green('[')}{display_name}{green(']')}")
            else:
                tab_display.append(f"{gray(' ' + display_name + ' ')}")
        
        tab_line = ' '.join(tab_display)
        if len(tab_line) > tab_width:
            tab_display = []
            for i, name in enumerate(n2):
                display_name = truncate(name, 8)
                if i == p4:
                    tab_display.append(f"{green('[')}{display_name}{green(']')}")
                else:
                    tab_display.append(f"{gray(display_name)}")
            tab_line = ' '.join(tab_display)
            if len(tab_line) > tab_width:
                tab_display = []
                for i, name in enumerate(n2[:5]):
                    display_name = truncate(name, 6)
                    if i == p4:
                        tab_display.append(f"{green('[')}{display_name}{green(']')}")
                    else:
                        tab_display.append(f"{gray(display_name)}")
                if len(n2) > 5:
                    tab_display.append(f"{gray('...')}")
                tab_line = ' '.join(tab_display)
        
        print(f"\n{gray('┌─ Menu ─')}")
        print(f"{gray('│')} {cyan('Tabs:')} {tab_line}")
        
        if width < 50:
            print(f"{gray('├──┤')}")
        else:
            print(f"{gray('├──────────────────┤')}")
        
        if not c2:
            print(f"{gray('│')} {red('(soon)')}")
        else:
            max_items = min(len(c2), height - 8)
            for i, m5 in enumerate(c2[:max_items], 1):
                display_name = truncate(m5, width - 10)
                if width < 50:
                    print(f"{gray('│')} {green(str(i))}.{display_name}")
                else:
                    print(f"{gray('│')} {green(f'{i:2}')}. {display_name}")
            if len(c2) > max_items:
                print(f"{gray('│ ...')} {len(c2)-max_items} more")
        
        if width < 40:
            print(f"{gray('├──┤')}")
            print(f"{gray('│')} {red('[0]')} {yellow('[s]')} {cyan('[t#]')} {gray('│')}")
        else:
            print(f"{gray('├──────────────────┤')}")
            print(f"{gray('│')} {red('[0]')} Exit  {yellow('[s]')} Search  {cyan('[t#]')} Tab  {blue('[i]')} Install{gray('│')}")
        
        print(f"{gray('└──────────────────┘')}")
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
            for tab_name, modules in g1().items():
                for mod in modules:
                    if q1.lower() in mod.lower():
                        found.append(f"{tab_name}: {mod}")
            if found:
                print(f"\n{green('[+] Found:')}")
                for f in found[:10]:
                    print(f"    {cyan('-')} {f}")
                if len(found) > 10:
                    print(f"    ... and {len(found)-10} more")
            else:
                print(f"\n{red('[!] No matches found')}")
            input(f"\n{green('>')} ")
            continue
        
        if c1 == "i":
            try:
                from installer import a11
                a11()
            except:
                print(f"{red('[!] installer.py not found')}")
                time.sleep(1)
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
                    print(f"\n{red('[!] Tab')} {t2} {red("doesn't exist (1-")}{t1}{red(')')}")
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
        c2 = o1(p4)
        
        if c2 and 0 <= i2 < len(c2):
            m5 = c2[i2]
            m6 = f"modules/{m5}"
            if os.path.exists(m6):
                from utils.modUI import a1, a2, a3
                
                module = a1(m6)
                module_options = {}
                current_options = {}
                
                if hasattr(module, 'OPTIONS'):
                    module_options = module.OPTIONS
                    for key, value in module_options.items():
                        if 'default' in value:
                            current_options[key] = value['default']
                
                while True:
                    choice = a2(m5[:-3], module_options, current_options)
                    
                    if choice == "1":
                        a3(m6, current_options if current_options else None)
                        
                    elif choice == "2" and module_options:
                        opt_width = min(width, 60)
                        print(f"\n{gray('┌─ Options ─')}")
                        opt_list = list(module_options.keys())
                        for i, key in enumerate(opt_list, 1):
                            current = current_options.get(key, module_options[key].get('default', ''))
                            display = truncate(f"{i}. {key} = {current}", opt_width - 4)
                            print(f"{gray('│')} {green(display)}")
                        print(f"{gray('└───────────')}")
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
                                    if 1 <= num <= len(opt_list):
                                        key = opt_list[num - 1]
                                        current_options[key] = val
                                        print(f"\n{green('[✓]')} {key} = {val}")
                                    else:
                                        print(f"\n{red('[!] Invalid number')}")
                                elif len(parts) == 1 and parts[0].isdigit():
                                    num = int(parts[0])
                                    if 1 <= num <= len(opt_list):
                                        key = opt_list[num - 1]
                                        current = current_options.get(key, module_options[key].get('default', ''))
                                        print(f"\n{yellow('  ')}{key} = {current}")
                                        new_val = input(f"{green('  New value:')} ").strip()
                                        if new_val:
                                            current_options[key] = new_val
                                            print(f"\n{green('[✓]')} {key} = {new_val}")
                                    else:
                                        print(f"\n{red('[!] Invalid number')}")
                                else:
                                    print(f"\n{red('[!] Format: <number> <value>')}")
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
                input(f"{green('>')} ")
        else:
            if c2:
                print(f"\n{red('[!] Invalid option')}")
            else:
                print(f"\n{red('[!] No modules')}")
            time.sleep(1)
