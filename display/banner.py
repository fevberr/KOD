import os
import sys
import time
import json
from config import a7 as get_tabs, a8 as get_tab
from config import host, port, device, system, ping
import random
import shutil
from utils.colors import hex_to_ansi, is_hex_color
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
        print("[!] installer.py not found")
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
        from utils.colors import color_settings_menu
        color_settings_menu()
    except:
        pass

def a20():
    try:
        with open("cache/CSET.json", 'r') as f:
            return json.load(f)
    except:
        return {}

def a21(c):
    if c and isinstance(c, str):
        return hex_to_ansi(c)
    return ''

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        c1 = a20()
        rs = '\033[0m'
        
        w = a11()
        h = a12()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        g = a21(c1.get('primary', '#00ffcc'))
        r = a21(c1.get('error', '#ff0044'))
        c = a21(c1.get('secondary', '#ff6bff'))
        y = a21(c1.get('warning', '#ffaa00'))
        wc = a21(c1.get('highlight', '#ffffff'))
        gr = a21(c1.get('dim', '#888888'))
        b = a21(c1.get('info', '#0088ff'))
        m = a21(c1.get('tab', '#ff44ff'))
        
        try:
            from display.banner import a3 as b1
            b1()
        except Exception as e:
            print(f"{c}+--- 23 KOD{rs}")
            print(f"{gr}  (Banner error: {e}){rs}")
        
        w = a11()
        if w < 60:
            i1 = f"host: {a17(host, 20)}\nport:{port}\nping:{ping}ms\ndev:{a17(device, 10)}"
            try:
                from display.panels import p1
                p1("23 KOD", i1, "READY")
            except:
                print(f"{c}+--- 23 KOD{rs}")
                print(f"{c}| {rs}{wc}{a17(host, 25)}{rs}")
                print(f"{c}| {rs}{wc}{port}{rs}")
                print(f"{c}| {rs}{y}{ping}ms{rs}")
                print(f"{c}|- {rs}{g}READY{rs}")
                print(f"{c}{'-' * min(w, 30)}{rs}")
        else:
            i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
            try:
                from display.panels import p1
                p1("23 KOD", i1, "READY")
            except:
                print(f"{c}+--- 23 KOD{rs}")
                print(f"{c}| {rs}{wc}host:      {host}{rs}")
                print(f"{c}| {rs}{wc}Port:        {port}{rs}")
                print(f"{c}| {rs}{y}Ping:     {ping}{rs}")
                print(f"{c}| {rs}{m}device:   {device}{rs}")
                print(f"{c}| {rs}{m}system:    {system}{rs}")
                print(f"{c}|- {rs}{g}Status: READY{rs}")
                print(f"{c}{'-' * min(w, 30)}{rs}")
        
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
                td.append(f"{g}[{rs}{c}{dn}{rs}{g}]{rs}")
            else:
                td.append(f"{gr} {dn} {rs}")
        
        tl = ' '.join(td)
        if len(tl) > tw:
            td = []
            visible = max(1, min(len(n2), tw // 8))
            for i, name in enumerate(n2[:visible]):
                dn = a17(name, max(3, (tw // visible) - 2))
                if i == p4:
                    td.append(f"{g}[{rs}{c}{dn}{rs}{g}]{rs}")
                else:
                    td.append(f"{gr}{dn}{rs}")
            if len(n2) > visible:
                td.append(f"{gr}…{rs}")
            tl = ' '.join(td)
        
        print(f"\n{g}┌─ Menu {rs}{g}{'─' * min(w-10, 40)}{rs}")
        print(f"{g}│ {rs}{c}Tabs:{rs} {tl}")
        print(f"{g}├{'─' * min(w-4, 50)}{rs}")
        
        if not c2:
            print(f"{g}│ {rs}{r}(coming soon...){rs}")
        else:
            max_items = min(len(c2), max(1, h - 10))
            for i, m5 in enumerate(c2[:max_items], 1):
                dn = a17(m5, max(1, w - 14))
                if w < 60:
                    print(f"{g}│ {rs}{y}{str(i)}{rs}.{c}{dn}{rs}")
                else:
                    print(f"{g}│ {rs}{y}{f'{i:2}'}{rs}. {c}{dn}{rs}")
            if len(c2) > max_items:
                print(f"{g}│ ... {rs}{len(c2)-max_items} more")
        
        if w < 60:
            print(f"{g}├{'─' * min(w-4, 30)}{rs}")
            print(f"{g}│ {rs}{r}[0]{rs} {y}[s]{rs} {c}[t#]{rs} {b}[i]{rs} {m}[c]{rs}")
            print(f"{g}│ {rs}{gr}  Exit   Search   Tab     Install  Colors{rs}")
        else:
            print(f"{g}├{'─' * min(w-4, 50)}{rs}")
            print(f"{g}│ {rs}{r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t#]{rs} Tab  {b}[i]{rs} Install  {m}[c]{rs} Colors")
        
        print(f"{g}└{'─' * min(w-4, 50)}{rs}")
        print()
        
        sys.stdout.flush()
        try:
            ch = input(f"{g}> {rs}").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{r}[!] Exiting...{rs}")
            break
        
        if ch == "0":
            print(f"{r}[!] Exiting...{rs}")
            break
        
        if ch == "s":
            q1 = input(f"{y}Search: {rs}").strip()
            found = []
            for tn, mods in get_tabs().items():
                for mod in mods:
                    if q1.lower() in mod.lower():
                        found.append(f"{tn}: {mod}")
            if found:
                print(f"\n{g}[+] Found:{rs}")
                for f in found[:min(10, h-6)]:
                    print(f"    {c}-{rs} {a17(f, w-6)}")
                if len(found) > 10:
                    print(f"    ... and {len(found)-10} more")
            else:
                print(f"\n{r}[!] No matches found{rs}")
            input(f"\n{g}> {rs}")
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
                    print(f"\n{g}[✓] Switched to: {rs}{c}{n2[p4]}{rs}")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"\n{r}[!] Tab {t2} invalid (1-{t1}){rs}")
                    time.sleep(1)
                    continue
            except:
                print(f"\n{r}[!] Invalid tab number{rs}")
                time.sleep(1)
                continue
        
        if not ch.isdigit():
            print(f"\n{r}[!] Invalid option{rs}")
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
                        print(f"\n{g}┌─ Options {rs}{g}{'─' * min(w-15, 40)}{rs}")
                        ol = list(mo.keys())
                        for i, key in enumerate(ol, 1):
                            cur = co.get(key, mo[key].get('default', ''))
                            print(f"{g}│ {rs}{y}{f'{i}'}{rs}. {c}{key}{rs} = {y}{cur}{rs}")
                        print(f"{g}└{'─' * min(w-4, 50)}{rs}")
                        print()
                        print(f"  {y}Format:{rs} {c}<num> <val>{rs}")
                        print(f"  {gr}Enter to keep current{rs}")
                        print()
                        
                        try:
                            inp = input(f"{g}> {rs}").strip()
                            if inp and inp != "0":
                                parts = inp.split()
                                if len(parts) >= 2:
                                    num = int(parts[0])
                                    val = ' '.join(parts[1:])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        co[key] = val
                                        print(f"\n{g}[✓] {key} = {val}{rs}")
                                    else:
                                        print(f"\n{r}[!] Invalid number{rs}")
                                elif len(parts) == 1 and parts[0].isdigit():
                                    num = int(parts[0])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        cur = co.get(key, mo[key].get('default', ''))
                                        print(f"\n{y}  {key} = {cur}{rs}")
                                        new_val = input(f"{g}  New: {rs}").strip()
                                        if new_val:
                                            co[key] = new_val
                                            print(f"\n{g}[✓] {key} = {new_val}{rs}")
                                    else:
                                        print(f"\n{r}[!] Invalid number{rs}")
                                else:
                                    print(f"\n{r}[!] Format: <num> <val>{rs}")
                        except ValueError:
                            print(f"\n{r}[!] Invalid input{rs}")
                        time.sleep(0.8)
                            
                    elif choice == "3":
                        print(f"\n{b}[✓] Returning...{rs}")
                        time.sleep(0.5)
                        break
                        
                    elif choice == "0":
                        print(f"{r}[!] Exiting...{rs}")
                        sys.exit(0)
                    else:
                        print(f"\n{r}[!] Invalid{rs}")
                        time.sleep(0.5)
            else:
                print(f"\n{r}[!] Module {m5} not found!{rs}")
                print(f"{gr}  Searched: EVERYWHERE{rs}")
                input(f"{g}> {rs}")
        else:
            if c2:
                print(f"\n{r}[!] Invalid option{rs}")
            else:
                print(f"\n{r}[!] No modules{rs}")
            time.sleep(1)

__all__ = ['m1']
