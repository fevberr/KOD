import os
import sys
import time
import json
import random
from config import a7 as get_tabs, a8 as get_tab
from config import host, port, device, system, ping
from utils.colors import hex_to_ansi, is_hex_color
from utils.modUI import a1 as mod_load, a2, a3, a4, a5, a6, a7, a8
from .tabs import get_tab_list, get_current_tab_modules, get_tab_count
from .search import search_modules
from .ui import draw_banner, draw_header, draw_tabs, draw_modules, draw_footer, clear_screen, get_terminal_size, truncate
from .options import parse_option_input
from .event import xmas, newyear, halloween, easter

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

def a16():
    try:
        import subprocess
        subprocess.run([sys.executable, "installer.py"], check=True)
    except Exception as e:
        print(f"\033[91m[!] Failed to run installer: {e}\033[0m")
        time.sleep(2)

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
    while True:
        c1 = a20()
        rs = '\033[0m'
        w, h = get_terminal_size()
        clear_screen()
        
        g = a21(c1.get('primary', '#00ffcc'))
        r = a21(c1.get('error', '#ff0044'))
        c = a21(c1.get('secondary', '#ff6bff'))
        y = a21(c1.get('warning', '#ffaa00'))
        wc = a21(c1.get('highlight', '#ffffff'))
        gr = a21(c1.get('dim', '#888888'))
        b = a21(c1.get('info', '#0088ff'))
        m = a21(c1.get('tab', '#ff44ff'))
        
        draw_banner(c, gr)
        draw_header(c, wc, y, m, g, host, port, ping, device, system, w)
        
        n2 = get_tab_list()
        t1 = get_tab_count()
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        c2 = get_current_tab_modules(p4)
        
        draw_tabs(g, c, gr, n2, p4, w)
        draw_modules(g, y, c, gr, r, c2, h, w)
        draw_footer(g, r, y, c, b, m, gr, w)
        
        sys.stdout.flush()
        try:
            ch = input(f"{g}> {rs}").strip().lower()
        except KeyboardInterrupt:
            print(f"\n{r}[!] Exiting...{rs}")
            break
        
        if ch == "0":
            print(f"{r}[!] Exiting...{rs}")
            break
        
        # Events
        if ch == "xmas":
            xmas()
            continue
        if ch == "newyear" or ch == "ny":
            newyear()
            continue
        if ch == "halloween" or ch == "hall":
            halloween()
            continue
        if ch == "easter":
            easter()
            continue
        
        if ch == "t":
            clear_screen()
            bw = min(w-2, 50)
            print(f"\n{c}╔═══ TABS{rs}")
            print(f"{c}║{rs}")
            for i, name in enumerate(n2, 1):
                if i-1 == p4:
                    print(f"{c}║{rs} {g}▶ {i}{rs}. {c}{name}{rs} {g}← active{rs}")
                else:
                    print(f"{c}║{rs} {y}  {i}{rs}. {gr}{name}{rs}")
            print(f"{c}║{rs}")
            print(f"{c}╚═══{rs}")
            print(f"{gr}Type t# to switch (e.g., t2){rs}")
            print()
            tab_choice = input(f"{g}> {rs}").strip().lower()
            if tab_choice.startswith('t') and len(tab_choice) > 1:
                try:
                    t2 = int(tab_choice[1:])
                    if 1 <= t2 <= t1:
                        p4 = t2 - 1
                        continue
                    else:
                        print(f"\n{r}[!] Tab {t2} invalid (1-{t1}){rs}")
                        time.sleep(1)
                        continue
                except:
                    print(f"\n{r}[!] Invalid tab number{rs}")
                    time.sleep(1)
                    continue
            elif tab_choice.isdigit():
                try:
                    t2 = int(tab_choice)
                    if 1 <= t2 <= t1:
                        p4 = t2 - 1
                        continue
                    else:
                        print(f"\n{r}[!] Tab {t2} invalid (1-{t1}){rs}")
                        time.sleep(1)
                        continue
                except:
                    print(f"\n{r}[!] Invalid tab number{rs}")
                    time.sleep(1)
                    continue
            else:
                continue
        
        if ch.startswith('t') and len(ch) > 1:
            try:
                t2 = int(ch[1:])
                if 1 <= t2 <= t1:
                    p4 = t2 - 1
                    continue
                else:
                    print(f"\n{r}[!] Tab {t2} invalid (1-{t1}){rs}")
                    time.sleep(1)
                    continue
            except:
                print(f"\n{r}[!] Invalid tab number{rs}")
                time.sleep(1)
                continue
        
        if ch == "s":
            clear_screen()
            bw = min(w-2, 50)
            print(f"\n{c}╔═══ SEARCH{rs}")
            print(f"{c}║{rs} {gr}Search modules{rs}")
            print(f"{c}╚═══{rs}")
            print()
            q1 = input(f"{y}Search: {rs}").strip()
            if q1:
                clear_screen()
                all_modules = []
                for tn, mods in get_tabs().items():
                    for mod in mods:
                        all_modules.append(mod)
                results = search_modules(q1, all_modules)
                bw = min(w-2, 50)
                print(f"\n{c}╔═══ SEARCH RESULTS{rs}")
                print(f"{c}║{rs} {gr}Query:{rs} {y}{q1}{rs}")
                print(f"{c}║{rs} {gr}Found:{rs} {len(results)} results{rs}")
                print(f"{c}╠═══{rs}")
                if results:
                    max_show = min(len(results), h - 10)
                    for i, (display_name, score, module, tab) in enumerate(results[:max_show], 1):
                        if tab:
                            display = f"{tab}: {module}"
                        else:
                            display = module
                        dn = truncate(display, w - 8)
                        bar_len = min(int(score / 20), 10)
                        bar = '█' * bar_len + '░' * (10 - bar_len)
                        if w < 40:
                            print(f"{c}║{rs} {y}{i}{rs}. {c}{dn}{rs}")
                        else:
                            print(f"{c}║{rs} {y}{i:2}{rs}. {c}{dn:<30} {gr}{bar}{rs}")
                    if len(results) > max_show:
                        print(f"{c}║{rs} {gr}... and {len(results)-max_show} more{rs}")
                    print(f"{c}╠═══{rs}")
                    print(f"{c}║{rs} {gr}Enter number to run, or 0 to go back{rs}")
                    print(f"{c}╚═══{rs}")
                    print()
                    choice = input(f"{g}> {rs}").strip()
                    if choice.isdigit():
                        num = int(choice)
                        if 1 <= num <= len(results):
                            module = results[num-1][2]
                            m6 = a9(module)
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
                                    choice2 = a6(module[:-3], mo, co)
                                    if choice2 == "1":
                                        a7(m6, co if co else None)
                                    elif choice2 == "2" and mo:
                                        print(f"\n{g}╔═══ Options{rs}")
                                        ol = list(mo.keys())
                                        for i, key in enumerate(ol, 1):
                                            cur = co.get(key, mo[key].get('default', ''))
                                            print(f"{g}║{rs} {y}{i}{rs}. {c}{key}{rs} = {y}{cur}{rs}")
                                        print(f"{g}╚═══{rs}")
                                        print()
                                        print(f"  {y}Format:{rs} {c}<num> <val>{rs}")
                                        print(f"  {gr}Enter to keep or paste: 4 true{rs}")
                                        print()
                                        while True:
                                            inp = input(f"{g}> {rs}").strip()
                                            if inp == "0":
                                                break
                                            valid, num2, val = parse_option_input(inp, ol, co, mo)
                                            if valid and num2 is not None:
                                                key = ol[num2 - 1]
                                                if val is None:
                                                    cur = co.get(key, mo[key].get('default', ''))
                                                    print(f"\n{y}  {key} = {cur}{rs}")
                                                    new_val = input(f"{g}  New: {rs}").strip()
                                                    if new_val:
                                                        co[key] = new_val
                                                        print(f"\n{g}[✓] {key} = {new_val}{rs}")
                                                else:
                                                    co[key] = val
                                                    print(f"\n{g}[✓] {key} = {val}{rs}")
                                                    print(f"{gr}  Continue pasting or press 0 to go back{rs}")
                                            else:
                                                print(f"\n{r}[!] Invalid format! Use: 4 true  or  key = value{rs}")
                                                print(f"{gr}  Examples: 4 true, 5 false, 3 8080, verbose = true{rs}")
                                    elif choice2 == "3":
                                        print(f"\n{b}[✓] Returning...{rs}")
                                        time.sleep(0.5)
                                        break
                                    elif choice2 == "0":
                                        print(f"{r}[!] Exiting...{rs}")
                                        sys.exit(0)
                                    else:
                                        print(f"\n{r}[!] Invalid{rs}")
                                        time.sleep(0.5)
                            else:
                                print(f"\n{r}[!] Module not found{rs}")
                                input(f"\n{g}> {rs}")
                else:
                    print(f"{c}║{rs} {r}No results found{rs}")
                    print(f"{c}╚═══{rs}")
                    print()
                    print(f"{gr}No modules matched '{q1}'{rs}")
                    input(f"\n{g}> {rs}")
            continue
        
        if ch == "i":
            a16()
            continue
        
        if ch == "c":
            a19()
            continue
        
        if not ch.isdigit():
            print(f"\n{r}[!] Invalid{rs}")
            time.sleep(1)
            continue
        
        i2 = int(ch) - 1
        c2 = get_current_tab_modules(p4)
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
                        print(f"\n{g}╔═══ Options{rs}")
                        ol = list(mo.keys())
                        for i, key in enumerate(ol, 1):
                            cur = co.get(key, mo[key].get('default', ''))
                            print(f"{g}║{rs} {y}{i}{rs}. {c}{key}{rs} = {y}{cur}{rs}")
                        print(f"{g}╚═══{rs}")
                        print()
                        print(f"  {y}Format:{rs} {c}<num> <val>{rs}")
                        print(f"  {gr}Enter to keep or paste: 4 true{rs}")
                        print()
                        while True:
                            inp = input(f"{g}> {rs}").strip()
                            if inp == "0":
                                break
                            valid, num2, val = parse_option_input(inp, ol, co, mo)
                            if valid and num2 is not None:
                                key = ol[num2 - 1]
                                if val is None:
                                    cur = co.get(key, mo[key].get('default', ''))
                                    print(f"\n{y}  {key} = {cur}{rs}")
                                    new_val = input(f"{g}  New: {rs}").strip()
                                    if new_val:
                                        co[key] = new_val
                                        print(f"\n{g}[✓] {key} = {new_val}{rs}")
                                else:
                                    co[key] = val
                                    print(f"\n{g}[✓] {key} = {val}{rs}")
                                    print(f"{gr}  Continue pasting or press 0 to go back{rs}")
                            else:
                                print(f"\n{r}[!] Invalid format! Use: 4 true  or  key = value{rs}")
                                print(f"{gr}  Examples: 4 true, 5 false, 3 8080, verbose = true{rs}")
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
                print(f"\n{r}[!] Invalid{rs}")
            else:
                print(f"\n{r}[!] No modules{rs}")
            time.sleep(1)

__all__ = ['m1']
