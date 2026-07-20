import os
import sys
import time
from config import g1, g2, host, port, device, system, ping
import random
import shutil
from utils.colors import *

def a3():
    try:
        return shutil.get_terminal_size()
    except:
        return os.terminal_size((80, 24))

def a4():
    return a3().columns

def a5():
    return a3().lines

def a6(text, max_len):
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

def a7(text, delay=0.008):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def a8(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def a9():
    chars = "01!@#$%^&*()_+{}|:<>?~"
    width = a4()
    for _ in range(2):
        line = ''.join(random.choice(chars) for _ in range(min(width, 50)))
        sys.stdout.write(f"\r{gr1(line)}")
        sys.stdout.flush()
        time.sleep(0.015)
    print("\r" + " " * min(width, 50), end="")
    print("\r", end="")

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        width = a4()
        height = a5()
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
            display_name = a6(name, 12)
            if i == p4:
                tab_display.append(f"{g1('[')}{display_name}{g1(']')}")
            else:
                tab_display.append(f"{gr1(' ' + display_name + ' ')}")
        
        tab_line = ' '.join(tab_display)
        if len(tab_line) > tab_width:
            tab_display = []
            for i, name in enumerate(n2):
                display_name = a6(name, 8)
                if i == p4:
                    tab_display.append(f"{g1('[')}{display_name}{g1(']')}")
                else:
                    tab_display.append(f"{gr1(display_name)}")
            tab_line = ' '.join(tab_display)
            if len(tab_line) > tab_width:
                tab_display = []
                for i, name in enumerate(n2[:5]):
                    display_name = a6(name, 6)
                    if i == p4:
                        tab_display.append(f"{g1('[')}{display_name}{g1(']')}")
                    else:
                        tab_display.append(f"{gr1(display_name)}")
                if len(n2) > 5:
                    tab_display.append(f"{gr1('...')}")
                tab_line = ' '.join(tab_display)
        
        print(f"\n{gr1('┌─ Menu ─')}")
        print(f"{gr1('│')} {c2('Tabs:')} {tab_line}")
        
        if width < 50:
            print(f"{gr1('├──┤')}")
        else:
            print(f"{gr1('├──────────────────┤')}")
        
        if not c2:
            print(f"{gr1('│')} {r1('(soon)')}")
        else:
            max_items = min(len(c2), height - 8)
            for i, m5 in enumerate(c2[:max_items], 1):
                display_name = a6(m5, width - 10)
                if width < 50:
                    print(f"{gr1('│')} {g1(str(i))}.{display_name}")
                else:
                    print(f"{gr1('│')} {g1(f'{i:2}')}. {display_name}")
            if len(c2) > max_items:
                print(f"{gr1('│ ...')} {len(c2)-max_items} more")
        
        if width < 40:
            print(f"{gr1('├──┤')}")
            print(f"{gr1('│')} {r1('[0]')} {y1('[s]')} {c2('[t#]')} {gr1('│')}")
        else:
            print(f"{gr1('├──────────────────┤')}")
            print(f"{gr1('│')} {r1('[0]')} Exit  {y1('[s]')} Search  {c2('[t#]')} Tab  {b1('[i]')} Install{gr1('│')}")
        
        print(f"{gr1('└──────────────────┘')}")
        print()
        
        sys.stdout.flush()
        try:
            c1 = input(f"{g1('>')} ").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{r1('[!] Exiting...')}")
            break
        
        if c1 == "0":
            print(f"{r1('[!] Exiting...')}")
            break
        
        if c1 == "s":
            q1 = input(f"{y1('Search:')} ").strip()
            found = []
            for tab_name, modules in g1().items():
                for mod in modules:
                    if q1.lower() in mod.lower():
                        found.append(f"{tab_name}: {mod}")
            if found:
                print(f"\n{g1('[+] Found:')}")
                for f in found[:10]:
                    print(f"    {c2('-')} {f}")
                if len(found) > 10:
                    print(f"    ... and {len(found)-10} more")
            else:
                print(f"\n{r1('[!] No matches found')}")
            input(f"\n{g1('>')} ")
            continue
        
        if c1 == "i":
            try:
                from installer import a11
                a11()
            except:
                print(f"{r1('[!] installer.py not found')}")
                time.sleep(1)
            continue
        
        if c1.startswith('t') and len(c1) > 1:
            try:
                t2 = int(c1[1:])
                if 1 <= t2 <= t1:
                    p4 = t2 - 1
                    print(f"\n{g1('[✓] Switched to:')} {n2[p4]}")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"\n{r1('[!] Tab')} {t2} {r1("doesn't exist (1-")}{t1}{r1(')')}")
                    time.sleep(1)
                    continue
            except:
                print(f"\n{r1('[!] Invalid tab number')}")
                time.sleep(1)
                continue
        
        if not c1.isdigit():
            print(f"\n{r1('[!] Invalid option')}")
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
                        print(f"\n{gr1('┌─ Options ─')}")
                        opt_list = list(module_options.keys())
                        for i, key in enumerate(opt_list, 1):
                            current = current_options.get(key, module_options[key].get('default', ''))
                            display = a6(f"{i}. {key} = {current}", opt_width - 4)
                            print(f"{gr1('│')} {g1(display)}")
                        print(f"{gr1('└───────────')}")
                        print()
                        print(f"  {y1('Format:')} {c2('<num> <val>')}")
                        print(f"  {gr1('Enter to keep current')}")
                        print()
                        
                        try:
                            inp = input(f"{g1('>')} ").strip()
                            if inp and inp != "0":
                                parts = inp.split()
                                if len(parts) >= 2:
                                    num = int(parts[0])
                                    val = ' '.join(parts[1:])
                                    if 1 <= num <= len(opt_list):
                                        key = opt_list[num - 1]
                                        current_options[key] = val
                                        print(f"\n{g1('[✓]')} {key} = {val}")
                                    else:
                                        print(f"\n{r1('[!] Invalid number')}")
                                elif len(parts) == 1 and parts[0].isdigit():
                                    num = int(parts[0])
                                    if 1 <= num <= len(opt_list):
                                        key = opt_list[num - 1]
                                        current = current_options.get(key, module_options[key].get('default', ''))
                                        print(f"\n{y1('  ')}{key} = {current}")
                                        new_val = input(f"{g1('  New value:')} ").strip()
                                        if new_val:
                                            current_options[key] = new_val
                                            print(f"\n{g1('[✓]')} {key} = {new_val}")
                                    else:
                                        print(f"\n{r1('[!] Invalid number')}")
                                else:
                                    print(f"\n{r1('[!] Format: <number> <value>')}")
                        except ValueError:
                            print(f"\n{r1('[!] Invalid input')}")
                        time.sleep(0.8)
                            
                    elif choice == "3":
                        print(f"\n{b1('[✓] Returning...')}")
                        time.sleep(0.5)
                        break
                        
                    elif choice == "0":
                        print(f"{r1('[!] Exiting...')}")
                        sys.exit(0)
                    else:
                        print(f"\n{r1('[!] Invalid')}")
                        time.sleep(0.5)
            else:
                print(f"\n{r1('[!] Module')} {m5} {r1('not found!')}")
                input(f"{g1('>')} ")
        else:
            if c2:
                print(f"\n{r1('[!] Invalid option')}")
            else:
                print(f"\n{r1('[!] No modules')}")
            time.sleep(1)
