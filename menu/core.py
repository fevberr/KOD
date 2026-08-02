import os
import sys
import time
import json
import random
import subprocess
from config import a7 as get_tabs, a8 as get_tab
from config import host, port, device, system, ping
from utils.colors import hex_to_ansi, is_hex_color
from utils.modUI import a1 as mod_load, a2, a3, a4, a5, a6, a7, a8
from .tabs import get_tab_list, get_current_tab_modules, get_tab_count
from .search import search_modules
from .ui import draw_banner, clear_screen, get_terminal_size, truncate, get_current_path
from .options import parse_option_input

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

def a22(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"\033[91m{result.stderr}\033[0m")
        return result.returncode == 0
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")
        return False

def a23():
    c1 = a20()
    rs = '\033[0m'
    g = a21(c1.get('primary', '#7b2fbe'))
    r = a21(c1.get('error', '#e74c3c'))
    c = a21(c1.get('secondary', '#9b59b6'))
    y = a21(c1.get('warning', '#f1c40f'))
    wc = a21(c1.get('highlight', '#ffffff'))
    gr = a21(c1.get('dim', '#7f8c8d'))
    m = a21(c1.get('tab', '#8e44ad'))
    b = a21(c1.get('info', '#3498db'))
    o = a21(c1.get('accent', '#f1c40f'))
    pi = a21(c1.get('highlight', '#ff6bff'))
    
    clear_screen()
    path = get_current_path()
    path_display = truncate(path, 50)
    
    print(f"\n{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
    print(f"{g}║{rs} {c}╔══════════════════════════════════════════════════════════════╗{rs}")
    print(f"{g}║{rs} {c}║{rs} {wc}                    CREDITS                      {rs}{c}║{rs}")
    print(f"{g}║{rs} {c}╠══════════════════════════════════════════════════════════════╣{rs}")
    print(f"{g}║{rs} {c}║{rs}                                                         {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}  {y}Developer:{rs} {wc}fevber{rs}                            {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}  {y}Version:{rs}  {wc}1.3.4{rs}                              {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}  {y}GitHub:{rs}  {wc}https://github.com/fevberr/KOD{rs}      {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}  {y}Discord:{rs} {wc}https://discord.gg/xrvgQD9s9b{rs}        {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}                                                         {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}  {pi}Thanks to all contributors and users!{rs}              {c}║{rs}")
    print(f"{g}║{rs} {c}║{rs}                                                         {c}║{rs}")
    print(f"{g}║{rs} {c}╚══════════════════════════════════════════════════════════════╝{rs}")
    print(f"{g}╚═══{rs}")
    print()
    input(f"{g}Press Enter to continue{rs}")

def m1():
    p4 = 0
    while True:
        c1 = a20()
        rs = '\033[0m'
        w, h = get_terminal_size()
        clear_screen()
        
        g = a21(c1.get('primary', '#7b2fbe'))
        r = a21(c1.get('error', '#e74c3c'))
        c = a21(c1.get('secondary', '#9b59b6'))
        y = a21(c1.get('warning', '#f1c40f'))
        wc = a21(c1.get('highlight', '#ffffff'))
        gr = a21(c1.get('dim', '#7f8c8d'))
        b = a21(c1.get('info', '#3498db'))
        m = a21(c1.get('tab', '#8e44ad'))
        
        try:
            from display.banner import a3 as b1
            b1()
        except:
            pass
        
        path = get_current_path()
        path_display = truncate(path, w - 20)
        
        print(f"\n{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
        print(f"{g}║{rs} {wc}Host: {host}{rs}")
        print(f"{g}║{rs} {wc}Port: {port}{rs}")
        print(f"{g}║{rs} {y}Ping: {ping}ms{rs}")
        print(f"{g}║{rs} {m}Device: {device}{rs}")
        print(f"{g}║{rs} {m}System: {system}{rs}")
        print(f"{g}║{rs} {g}Status: READY{rs}")
        print(f"{g}╚═══{rs}")
        
        n2 = get_tab_list()
        t1 = get_tab_count()
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        c2 = get_current_tab_modules(p4)
        
        tw = min(w - 4, 60)
        td = []
        for i, name in enumerate(n2):
            dn = truncate(name, max(3, (tw // max(1, len(n2))) - 1))
            if i == p4:
                td.append(f"{g}▸{rs}{c}{dn}{rs}{g}◂{rs}")
            else:
                td.append(f"{gr}┆{rs}{gr}{dn}{rs}")
        tl = ' '.join(td)
        if len(tl) > tw:
            td = []
            visible = max(1, min(len(n2), tw // 8))
            for i, name in enumerate(n2[:visible]):
                dn = truncate(name, max(3, (tw // visible) - 1))
                if i == p4:
                    td.append(f"{g}▸{rs}{c}{dn}{rs}{g}◂{rs}")
                else:
                    td.append(f"{gr}┆{rs}{gr}{dn}{rs}")
            if len(n2) > visible:
                td.append(f"{gr}…{rs}")
            tl = ' '.join(td)
        
        print(f"\n{g}╔═══ Menu{rs}")
        print(f"{g}║{rs} {c}Tabs:{rs} {tl}")
        print(f"{g}╠═══{rs}")
        
        if not c2:
            print(f"{g}║{rs} {r}No modules available{rs}")
        else:
            max_items = min(len(c2), max(1, h - 14))
            for i, m5 in enumerate(c2[:max_items], 1):
                dn = truncate(m5, max(1, w - 8))
                if w < 30:
                    print(f"{g}║{rs} {y}{i}{rs}. {c}{dn}{rs}")
                else:
                    print(f"{g}║{rs} {y}{i:2}{rs}. {c}{dn}{rs}")
            if len(c2) > max_items:
                print(f"{g}║{rs} {gr}... and {len(c2)-max_items} more{rs}")
        
        print(f"{g}╠═══{rs}")
        if w < 30:
            print(f"{g}║{rs} {r}0{rs} {y}s{rs} {c}t{rs} {b}i{rs} {m}c{rs} {pi}p{rs}")
            print(f"{g}║{rs} {gr}Exit Find Tabs Inst Color Crd{rs}")
        elif w < 50:
            print(f"{g}║{rs} {r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t]{rs} Tabs  {b}[i]{rs} Install  {m}[c]{rs} Color  {pi}[p]{rs} Crd")
        else:
            print(f"{g}║{rs} {r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t]{rs} Tabs  {b}[i]{rs} Install  {m}[c]{rs} Colors  {pi}[p]{rs} Credits")
        print(f"{g}╚═══{rs}")
        print()
        
        print(f"{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
        print(f"{g}╚══ ▶{rs} ", end="")
        sys.stdout.flush()
        
        try:
            ch = input().strip()
        except KeyboardInterrupt:
            print(f"\n{r}[!] Exiting...{rs}")
            break
        
        if not ch:
            continue
        
        # Check for tab switching - any number followed by 't' or just 't' + number
        # Examples: 2t, t2, 2, tab2, t 2
        ch_lower = ch.lower()
        
        # Handle tab switching more flexibly
        if ch_lower.startswith('t') or ch_lower.endswith('t') or ch_lower == 't':
            # Extract number from various formats: t2, 2t, tab2, t 2, tab 2
            import re
            # Try to find any number in the input
            numbers = re.findall(r'\d+', ch_lower)
            if numbers:
                try:
                    t2 = int(numbers[0])
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
                # Just 't' - show tab list
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
                print(f"{gr}Type t# to switch (e.g., t2 or 2t or tab2){rs}")
                print(f"{gr}Or just type the number: 2{rs}")
                print()
                tab_choice = input(f"{g}> {rs}").strip().lower()
                if tab_choice:
                    nums = re.findall(r'\d+', tab_choice)
                    if nums:
                        try:
                            t2 = int(nums[0])
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
                continue
        
        # Check if just a number (for tab switching)
        if ch.isdigit():
            num = int(ch)
            if 1 <= num <= t1:
                # Check if it's a tab number (if user just typed a number)
                # We need to differentiate between tab numbers and module numbers
                # If the number is within tab count, we can ask or switch to tab
                p4 = num - 1
                continue
            else:
                # It's a module number (higher than tab count)
                i2 = num - 1
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
                        print(f"\n{r}[!] Invalid module number{rs}")
                    else:
                        print(f"\n{r}[!] No modules in this tab{rs}")
                    time.sleep(1)
                continue
        
        # Regular command handling
        special_cmds = ['0', 'exit', 's', 'search', 'i', 'install', 'c', 'color', 'colors', 'help', 'p', 'credits']
        
        if ch_lower not in special_cmds and not ch.isdigit():
            print(f"{g}▶ {rs}{ch}")
            a22(ch)
            input(f"\n{g}Press Enter to continue{rs}")
            continue
        
        if ch == "0" or ch_lower == "exit":
            print(f"{r}[!] Exiting...{rs}")
            break
        
        if ch_lower == "p" or ch_lower == "credits":
            a23()
            continue
        
        if ch_lower == "s" or ch_lower == "search":
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
                    for i, (display, module, tab) in enumerate(results[:max_show], 1):
                        dn = truncate(display, w - 8)
                        if w < 40:
                            print(f"{c}║{rs} {y}{i}{rs}. {c}{dn}{rs}")
                        else:
                            print(f"{c}║{rs} {y}{i:2}{rs}. {c}{dn}{rs}")
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
                            module = results[num-1][1]
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
        
        if ch_lower == "i" or ch_lower == "install":
            a16()
            continue
        
        if ch_lower == "c" or ch_lower == "color" or ch_lower == "colors":
            a19()
            continue
        
        if ch_lower == "help":
            clear_screen()
            print(f"\n{c}╔═══ HELP{rs}")
            print(f"{c}║{rs} {g}Commands:{rs}")
            print(f"{c}║{rs}  {y}0{rs} or {y}exit{rs}    - Exit KOD")
            print(f"{c}║{rs}  {y}s{rs} or {y}search{rs}   - Search modules")
            print(f"{c}║{rs}  {y}t{rs}           - List tabs")
            print(f"{c}║{rs}  {y}t# {rs}          - Switch tab (e.g., t2, 2t, tab2)")
            print(f"{c}║{rs}  {y}# {rs}            - Switch tab (just type number)")
            print(f"{c}║{rs}  {y}i{rs} or {y}install{rs}   - Install packages")
            print(f"{c}║{rs}  {y}c{rs} or {y}colors{rs}    - Color settings")
            print(f"{c}║{rs}  {y}p{rs} or {y}credits{rs}   - Show credits")
            print(f"{c}║{rs}  {y}help{rs}        - Show this help")
            print(f"{c}║{rs}  {y}<number>{rs}      - Run module")
            print(f"{c}║{rs}  {y}<command>{rs}     - Run system command")
            print(f"{c}╚═══{rs}")
            input(f"\n{g}Press Enter to continue{rs}")
            continue
        
        if not ch.isdigit():
            print(f"\n{r}[!] Unknown command: {ch}{rs}")
            print(f"{gr}Type 'help' for available commands{rs}")
            time.sleep(1.5)
            continue

__all__ = ['m1']
