import os
import sys
import time
import json
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
        print("\033[91m[!] installer.py not found\033[0m")
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
        print("\033[91m[!] Color error:\033[0m " + str(e))
        time.sleep(2)

def a20():
    try:
        with open("cache/CSET.json", 'r') as f:
            return json.load(f)
    except:
        return {}

def a21(c):
    try:
        h = c.lstrip('#')
        if len(h) == 3:
            h = ''.join([x*2 for x in h])
        if len(h) == 6:
            r = int(h[0:2], 16)
            g = int(h[2:4], 16)
            b = int(h[4:6], 16)
            return f'\033[38;2;{r};{g};{b}m'
    except:
        pass
    return ''

def m1():
    p4 = 0
    q1 = ""
    
    reload_colors()
    
    while True:
        reload_colors()
        c1 = a20()
        
        w = a11()
        h = a12()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        try:
            from display.banner import a3 as b1
            b1()
        except Exception as e:
            print("+--- 23 KOD")
            print("  (Banner error: " + str(e) + ")")
        
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
                td.append("[" + dn + "]")
            else:
                td.append(" " + dn + " ")
        
        tl = ' '.join(td)
        if len(tl) > tw:
            td = []
            visible = max(1, min(len(n2), tw // 8))
            for i, name in enumerate(n2[:visible]):
                dn = a17(name, max(3, (tw // visible) - 2))
                if i == p4:
                    td.append("[" + dn + "]")
                else:
                    td.append(dn)
            if len(n2) > visible:
                td.append("…")
            tl = ' '.join(td)
        
        print("\n┌─ Menu " + "─" * min(w-10, 40))
        print("│ Tabs: " + tl)
        print("├" + "─" * min(w-4, 50))
        
        if not c2:
            print("│ (coming soon...)")
        else:
            max_items = min(len(c2), max(1, h - 10))
            for i, m5 in enumerate(c2[:max_items], 1):
                dn = a17(m5, max(1, w - 14))
                if w < 60:
                    print("│ " + str(i) + "." + dn)
                else:
                    print("│ " + f'{i:2}' + ". " + dn)
            if len(c2) > max_items:
                print("│ ... " + str(len(c2)-max_items) + " more")
        
        if w < 60:
            print("├" + "─" * min(w-4, 30))
            print("│ [0] [s] [t#] [i] [c]")
            print("│   Exit   Search   Tab     Install  Colors")
        else:
            print("├" + "─" * min(w-4, 50))
            print("│ [0] Exit  [s] Search  [t#] Tab  [i] Install  [c] Colors")
        
        print("└" + "─" * min(w-4, 50))
        print()
        
        sys.stdout.flush()
        try:
            ch = input("> ").strip().lower()
        except KeyboardInterrupt:
            print("\n[!] Exiting...")
            break
        
        if ch == "0":
            print("[!] Exiting...")
            break
        
        if ch == "s":
            q1 = input("Search: ").strip()
            found = []
            for tn, mods in get_tabs().items():
                for mod in mods:
                    if q1.lower() in mod.lower():
                        found.append(tn + ": " + mod)
            if found:
                print("\n[+] Found:")
                for f in found[:min(10, h-6)]:
                    print("    - " + a17(f, w-6))
                if len(found) > 10:
                    print("    ... and " + str(len(found)-10) + " more")
            else:
                print("\n[!] No matches found")
            input("\n> ")
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
                    print("\n[✓] Switched to: " + n2[p4])
                    time.sleep(0.5)
                    continue
                else:
                    print("\n[!] Tab " + str(t2) + " invalid (1-" + str(t1) + ")")
                    time.sleep(1)
                    continue
            except:
                print("\n[!] Invalid tab number")
                time.sleep(1)
                continue
        
        if not ch.isdigit():
            print("\n[!] Invalid option")
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
                        print("\n┌─ Options " + "─" * min(w-15, 40))
                        ol = list(mo.keys())
                        for i, key in enumerate(ol, 1):
                            cur = co.get(key, mo[key].get('default', ''))
                            print("│ " + str(i) + ". " + key + " = " + cur)
                        print("└" + "─" * min(w-4, 50))
                        print()
                        print("  Format: <num> <val>")
                        print("  Enter to keep current")
                        print()
                        
                        try:
                            inp = input("> ").strip()
                            if inp and inp != "0":
                                parts = inp.split()
                                if len(parts) >= 2:
                                    num = int(parts[0])
                                    val = ' '.join(parts[1:])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        co[key] = val
                                        print("\n[✓] " + key + " = " + val)
                                    else:
                                        print("\n[!] Invalid number")
                                elif len(parts) == 1 and parts[0].isdigit():
                                    num = int(parts[0])
                                    if 1 <= num <= len(ol):
                                        key = ol[num - 1]
                                        cur = co.get(key, mo[key].get('default', ''))
                                        print("\n  " + key + " = " + cur)
                                        new_val = input("  New: ").strip()
                                        if new_val:
                                            co[key] = new_val
                                            print("\n[✓] " + key + " = " + new_val)
                                    else:
                                        print("\n[!] Invalid number")
                                else:
                                    print("\n[!] Format: <num> <val>")
                        except ValueError:
                            print("\n[!] Invalid input")
                        time.sleep(0.8)
                            
                    elif choice == "3":
                        print("\n[✓] Returning...")
                        time.sleep(0.5)
                        break
                        
                    elif choice == "0":
                        print("[!] Exiting...")
                        sys.exit(0)
                    else:
                        print("\n[!] Invalid")
                        time.sleep(0.5)
            else:
                print("\n[!] Module " + m5 + " not found!")
                print("  Searched: EVERYWHERE")
                input("> ")
        else:
            if c2:
                print("\n[!] Invalid option")
            else:
                print("\n[!] No modules")
            time.sleep(1)

__all__ = ['m1']
