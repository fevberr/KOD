import os
import sys
import time
import json
import re
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
        import subprocess
        subprocess.run([sys.executable, "installer.py"], check=True)
    except Exception as e:
        print(f"\033[91m[!] Failed to run installer: {e}\033[0m")
        time.sleep(2)

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

def a22(s, w):
    if len(s) > w:
        return s[:w-1] + "…"
    return s

def a23(query, items):
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    for item in items:
        item_lower = item.lower()
        score = 0
        if query_lower == item_lower:
            score = 1000
        elif item_lower.startswith(query_lower):
            score = 500
        elif f" {query_lower} " in f" {item_lower} ":
            score = 300
        elif query_lower in item_lower:
            score = 200
        else:
            word_matches = 0
            for word in query_words:
                if word in item_lower:
                    word_matches += 1
            if word_matches > 0:
                score = 100 * (word_matches / len(query_words))
        if score == 0 and len(query_lower) > 2:
            matches = 0
            qi = 0
            for char in item_lower:
                if qi < len(query_lower) and char == query_lower[qi]:
                    matches += 1
                    qi += 1
            if matches > 0:
                score = 50 * (matches / len(query_lower))
        if score > 0:
            results.append((item, score))
    results.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in results]

def a24(query, modules):
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    for module in modules:
        module_lower = module.lower()
        tab = None
        for tn, mods in get_tabs().items():
            if module in mods:
                tab = tn
                break
        display_name = f"{tab}: {module}" if tab else module
        display_lower = display_name.lower()
        score = 0
        if query_lower == module_lower or query_lower == display_lower:
            score = 1000
        elif module_lower.startswith(query_lower) or display_lower.startswith(query_lower):
            score = 500
        elif f" {query_lower} " in f" {module_lower} " or f" {query_lower} " in f" {display_lower} ":
            score = 300
        elif query_lower in module_lower or query_lower in display_lower:
            score = 200
        else:
            word_matches = 0
            for word in query_words:
                if word in module_lower or word in display_lower:
                    word_matches += 1
            if word_matches > 0:
                score = 100 * (word_matches / len(query_words))
        if score == 0 and len(query_lower) > 2:
            matches = 0
            qi = 0
            for char in module_lower:
                if qi < len(query_lower) and char == query_lower[qi]:
                    matches += 1
                    qi += 1
            if matches > 0:
                score = 50 * (matches / len(query_lower))
        if score > 0:
            results.append((display_name, score, module, tab))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

def a25(inp, ol, co, mo):
    parts = inp.strip().split()
    if not parts:
        return False, None, None
    if not parts[0].isdigit():
        if '=' in inp or ':' in inp:
            sep = '=' if '=' in inp else ':'
            kv = inp.split(sep)
            if len(kv) == 2:
                key = kv[0].strip()
                val = kv[1].strip()
                for i, k in enumerate(ol, 1):
                    if k.lower() == key.lower():
                        return True, i, val
        return False, None, None
    num = int(parts[0])
    if num < 1 or num > len(ol):
        return False, None, None
    if len(parts) == 1:
        return True, num, None
    val = ' '.join(parts[1:])
    return True, num, val

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
            print(f"{c}╔═══ 23 KOD{rs}")
            print(f"{gr}  ║ Banner error: {e}{rs}")
        if w < 40:
            print(f"{c}╔═══ 23 KOD{rs}")
            print(f"{c}║{rs} {wc}{a22(host, 15)}{rs}")
            print(f"{c}║{rs} {wc}Port: {port}{rs}")
            print(f"{c}║{rs} {y}Ping: {ping}ms{rs}")
            print(f"{c}╚═══{rs} {g}READY{rs}")
        elif w < 60:
            print(f"{c}╔═══ 23 KOD{rs}")
            print(f"{c}║{rs} {wc}{a22(host, 25)}{rs}")
            print(f"{c}║{rs} {wc}Port: {port}{rs}")
            print(f"{c}║{rs} {y}Ping: {ping}ms{rs}")
            print(f"{c}╚═══{rs} {g}READY{rs}")
        else:
            print(f"{c}╔═══ 23 KOD{rs}")
            print(f"{c}║{rs} {wc}Host: {host}{rs}")
            print(f"{c}║{rs} {wc}Port: {port}{rs}")
            print(f"{c}║{rs} {y}Ping: {ping}ms{rs}")
            print(f"{c}║{rs} {m}Device: {device}{rs}")
            print(f"{c}║{rs} {m}System: {system}{rs}")
            print(f"{c}╚═══{rs} {g}Status: READY{rs}")
        n2 = a14()
        t1 = max(1, len(n2))
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        c2 = a15(p4)
        tw = min(w - 4, 60)
        td = []
        for i, name in enumerate(n2):
            dn = a22(name, max(3, (tw // max(1, len(n2))) - 1))
            if i == p4:
                td.append(f"{g}▸{rs}{c}{dn}{rs}{g}◂{rs}")
            else:
                td.append(f"{gr}┆{rs}{gr}{dn}{rs}")
        tl = ' '.join(td)
        if len(tl) > tw:
            td = []
            visible = max(1, min(len(n2), tw // 8))
            for i, name in enumerate(n2[:visible]):
                dn = a22(name, max(3, (tw // visible) - 1))
                if i == p4:
                    td.append(f"{g}▸{rs}{c}{dn}{rs}{g}◂{rs}")
                else:
                    td.append(f"{gr}┆{rs}{gr}{dn}{rs}")
            if len(n2) > visible:
                td.append(f"{gr}…{rs}")
            tl = ' '.join(td)
        menu_w = min(w - 2, 50)
        print(f"\n{g}╔═══ Menu{rs}")
        print(f"{g}║{rs} {c}Tabs:{rs} {tl}")
        print(f"{g}╠═══{rs}")
        if not c2:
            print(f"{g}║{rs} {r}No modules available{rs}")
        else:
            max_items = min(len(c2), max(1, h - 10))
            for i, m5 in enumerate(c2[:max_items], 1):
                dn = a22(m5, max(1, w - 8))
                if w < 30:
                    print(f"{g}║{rs} {y}{i}{rs}. {c}{dn}{rs}")
                else:
                    print(f"{g}║{rs} {y}{i:2}{rs}. {c}{dn}{rs}")
            if len(c2) > max_items:
                print(f"{g}║{rs} {gr}... and {len(c2)-max_items} more{rs}")
        print(f"{g}╠═══{rs}")
        if w < 30:
            print(f"{g}║{rs} {r}0{rs} {y}s{rs} {c}t{rs} {b}i{rs} {m}c{rs}")
            print(f"{g}║{rs} {gr}Exit Find Tabs Inst Color{rs}")
        elif w < 50:
            print(f"{g}║{rs} {r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t]{rs} Tabs  {b}[i]{rs} Install  {m}[c]{rs} Color")
        else:
            print(f"{g}║{rs} {r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t]{rs} Tabs  {b}[i]{rs} Install  {m}[c]{rs} Colors")
        print(f"{g}╚═══{rs}")
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
        if ch == "t":
            os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
            bw = min(w-2, 50)
            print(f"\n{c}╔═══ SEARCH{rs}")
            print(f"{c}║{rs} {gr}Search modules{rs}")
            print(f"{c}╚═══{rs}")
            print()
            q1 = input(f"{y}Search: {rs}").strip()
            if q1:
                os.system('cls' if os.name == 'nt' else 'clear')
                all_modules = []
                for tn, mods in get_tabs().items():
                    for mod in mods:
                        all_modules.append(mod)
                results = a24(q1, all_modules)
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
                        dn = a22(display, w - 8)
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
                                            valid, num2, val = a25(inp, ol, co, mo)
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
                            valid, num2, val = a25(inp, ol, co, mo)
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
