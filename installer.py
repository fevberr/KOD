import subprocess
import sys
import os
import time
import platform
import json
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

def a1():
    try:
        w = shutil.get_terminal_size().columns
        return min(w, 80)
    except:
        return 60

def a2():
    try:
        with open('requirements.txt', 'r') as f:
            p = []
            for l in f:
                l = l.strip()
                if l and not l.startswith('#'):
                    p.append(l)
            return p
    except FileNotFoundError:
        print("\n[!] requirements.txt not found!")
        return []

def a3():
    try:
        subprocess.run([sys.executable, '-m', 'pip', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def a4():
    print("[*] Installing pip...")
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade'], check=True)
        return True
    except:
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
            return True
        except:
            return False

def a5(p):
    try:
        pn = p.split('>=')[0].split('==')[0].strip()
        r = subprocess.run([sys.executable, '-m', 'pip', 'show', pn], capture_output=True, text=True)
        return r.returncode == 0
    except:
        return False

def a6(p):
    try:
        r = subprocess.run([sys.executable, '-m', 'pip', 'install', p], capture_output=True, text=True)
        if r.returncode == 0:
            return True
        return False
    except:
        return False

def a7(c, t, w=30):
    p = c / t if t > 0 else 0
    f = int(w * p)
    b = '█' * f + '░' * (w - f)
    return f"{b} {int(p * 100)}%"

def a8():
    try:
        with open("cache/CSET.json", 'r') as f:
            return json.load(f)
    except:
        return {}

def a9(c):
    if c and isinstance(c, str):
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

def a10(s, w):
    if len(s) > w:
        return s[:w-1] + "…"
    return s

def a11():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    w = a1()
    c1 = a8()
    rs = '\033[0m'
    g = a9(c1.get('primary', '#00ffcc'))
    r = a9(c1.get('error', '#ff0044'))
    c = a9(c1.get('secondary', '#ff6bff'))
    y = a9(c1.get('warning', '#ffaa00'))
    wc = a9(c1.get('highlight', '#ffffff'))
    gr = a9(c1.get('dim', '#888888'))
    b = a9(c1.get('info', '#0088ff'))
    
    p = a2()
    if not p:
        return
    
    bw = min(w-2, 50)
    print(f"\n{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs}{wc}{' PACKAGE INSTALLER '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}├{'─' * bw}┤{rs}")
    print(f"{c}│{rs}{gr}{' Checking installed packages... '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    i = []
    m = []
    
    print(f"{gr}Scanning packages...{rs}")
    with ThreadPoolExecutor(max_workers=10) as e:
        fs = {e.submit(a5, pkg): pkg for pkg in p}
        for f in as_completed(fs):
            pkg = fs[f]
            if f.result():
                i.append(pkg)
                print(f"  {g}[+]{rs} {wc}{a10(pkg, w-6)}{rs}")
            else:
                m.append(pkg)
                print(f"  {r}[-]{rs} {wc}{a10(pkg, w-6)}{rs}")
    
    t = len(p)
    ins = len(i)
    mis = len(m)
    
    print()
    print(f"{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs}{wc}{' PACKAGE INSTALLER '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}├{'─' * bw}┤{rs}")
    print(f"{c}│{rs} {gr}Status:{rs} {'Ready' if not m else 'Missing packages'}")
    print(f"{c}│{rs} {gr}Installed:{rs} {g}{ins}/{t}{rs}")
    print(f"{c}│{rs} {gr}Missing:{rs} {r}{mis}{rs}")
    print(f"{c}│{rs} {gr}Progress:{rs} {a7(ins, t, min(30, w-20))}")
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    if i:
        print(f"{c}┌{'─' * bw}┐{rs}")
        print(f"{c}│{rs}{g}{' INSTALLED '.center(bw)}{rs}{c}│{rs}")
        print(f"{c}├{'─' * bw}┤{rs}")
        md = min(8, w // 15)
        for pkg in i[:md]:
            print(f"{c}│{rs} {g}[+]{rs} {wc}{a10(pkg, w-6)}{rs}")
        if len(i) > md:
            print(f"{c}│{rs} {gr}... and {len(i)-md} more{rs}")
        print(f"{c}└{'─' * bw}┘{rs}")
        print()
    
    if m:
        print(f"{c}┌{'─' * bw}┐{rs}")
        print(f"{c}│{rs}{r}{' MISSING '.center(bw)}{rs}{c}│{rs}")
        print(f"{c}├{'─' * bw}┤{rs}")
        md = min(8, w // 15)
        for pkg in m[:md]:
            print(f"{c}│{rs} {r}[-]{rs} {wc}{a10(pkg, w-6)}{rs}")
        if len(m) > md:
            print(f"{c}│{rs} {gr}... and {len(m)-md} more{rs}")
        print(f"{c}└{'─' * bw}┘{rs}")
        print()
    
    print(f"{c}┌{'─' * bw}┐{rs}")
    if w < 30:
        print(f"{c}│{rs} {g}[1]{rs} {y}[2]{rs} {b}[3]{rs} {r}[4]{rs}")
        print(f"{c}│{rs} {gr}All Miss Ref Back{rs}")
    elif w < 50:
        print(f"{c}│{rs} {g}[1]{rs} All  {y}[2]{rs} Miss  {b}[3]{rs} Ref  {r}[4]{rs} Back")
    else:
        print(f"{c}│{rs} {g}[1]{rs} Install all  {y}[2]{rs} Install missing  {b}[3]{rs} Refresh  {r}[4]{rs} Back")
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    return input(f"{c}> {rs}").strip()

def a12():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    w = a1()
    c1 = a8()
    rs = '\033[0m'
    g = a9(c1.get('primary', '#00ffcc'))
    r = a9(c1.get('error', '#ff0044'))
    c = a9(c1.get('secondary', '#ff6bff'))
    wc = a9(c1.get('highlight', '#ffffff'))
    gr = a9(c1.get('dim', '#888888'))
    
    p = a2()
    if not p:
        return
    
    bw = min(w-2, 50)
    print(f"\n{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs}{wc}{' INSTALLING ALL PACKAGES '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}├{'─' * bw}┤{rs}")
    print(f"{c}│{rs}{gr} Total: {len(p)} packages{rs}")
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    s = 0
    f = 0
    
    with ThreadPoolExecutor(max_workers=5) as e:
        fs = {e.submit(a6, pkg): pkg for pkg in p}
        for fu in as_completed(fs):
            pkg = fs[fu]
            if fu.result():
                print(f"{c}│{rs} {g}[+]{rs} {wc}{a10(pkg, w-6)} {gr}installed{rs}")
                s += 1
            else:
                print(f"{c}│{rs} {r}[-]{rs} {wc}{a10(pkg, w-6)} {gr}failed{rs}")
                f += 1
    
    print()
    print(f"{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs} {g}Complete:{rs} {s}/{len(p)} installed")
    if f > 0:
        print(f"{c}│{rs} {r}Failed:{rs} {f}")
    print(f"{c}└{'─' * bw}┘{rs}")
    input(f"\n{c}Press Enter to continue{rs}")

def a13():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    w = a1()
    c1 = a8()
    rs = '\033[0m'
    g = a9(c1.get('primary', '#00ffcc'))
    r = a9(c1.get('error', '#ff0044'))
    c = a9(c1.get('secondary', '#ff6bff'))
    wc = a9(c1.get('highlight', '#ffffff'))
    gr = a9(c1.get('dim', '#888888'))
    
    p = a2()
    if not p:
        return
    
    bw = min(w-2, 50)
    print(f"\n{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs}{wc}{' INSTALLING MISSING '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    m = []
    
    print(f"{gr}Checking packages...{rs}")
    with ThreadPoolExecutor(max_workers=10) as e:
        fs = {e.submit(a5, pkg): pkg for pkg in p}
        for f in as_completed(fs):
            pkg = fs[f]
            if not f.result():
                m.append(pkg)
                print(f"  {r}[-]{rs} {wc}{a10(pkg, w-6)} {gr}missing{rs}")
            else:
                print(f"  {g}[+]{rs} {wc}{a10(pkg, w-6)} {gr}installed{rs}")
    
    if not m:
        print()
        print(f"{c}┌{'─' * bw}┐{rs}")
        print(f"{c}│{rs}{g}{' All packages installed! '.center(bw)}{rs}{c}│{rs}")
        print(f"{c}└{'─' * bw}┘{rs}")
        input(f"\n{c}Press Enter to continue{rs}")
        return
    
    print()
    print(f"{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs}{r}{' INSTALLING MISSING '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}├{'─' * bw}┤{rs}")
    print(f"{c}│{rs}{gr} Missing: {len(m)} packages{rs}")
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    s = 0
    f = 0
    
    with ThreadPoolExecutor(max_workers=5) as e:
        fs = {e.submit(a6, pkg): pkg for pkg in m}
        for fu in as_completed(fs):
            pkg = fs[fu]
            if fu.result():
                print(f"{c}│{rs} {g}[+]{rs} {wc}{a10(pkg, w-6)} {gr}installed{rs}")
                s += 1
            else:
                print(f"{c}│{rs} {r}[-]{rs} {wc}{a10(pkg, w-6)} {gr}failed{rs}")
                f += 1
    
    print()
    print(f"{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs} {g}Complete:{rs} {s}/{len(m)} installed")
    if f > 0:
        print(f"{c}│{rs} {r}Failed:{rs} {f}")
    print(f"{c}└{'─' * bw}┘{rs}")
    input(f"\n{c}Press Enter to continue{rs}")

def a14():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    w = a1()
    c1 = a8()
    rs = '\033[0m'
    g = a9(c1.get('primary', '#00ffcc'))
    r = a9(c1.get('error', '#ff0044'))
    c = a9(c1.get('secondary', '#ff6bff'))
    gr = a9(c1.get('dim', '#888888'))
    
    bw = min(w-2, 50)
    
    print(f"\n{c}┌{'─' * bw}┐{rs}")
    print(f"{c}│{rs}{' PACKAGE INSTALLER '.center(bw)}{rs}{c}│{rs}")
    print(f"{c}├{'─' * bw}┤{rs}")
    
    if not a3():
        print(f"{c}│{rs} {r}[!] Pip not installed!{rs}")
        print(f"{c}│{rs} {gr}[*] Attempting to install pip...{rs}")
        if a4():
            print(f"{c}│{rs} {g}[+] Pip installed successfully!{rs}")
        else:
            print(f"{c}│{rs} {r}[!] Could not install pip!{rs}")
            print(f"{c}│{rs} {gr}[*] Try: python -m ensurepip --upgrade{rs}")
            if platform.system() == "Linux" or "Android" in platform.system():
                print(f"{c}│{rs} {gr}[*] Or: apt install python3-pip{rs}")
            print(f"{c}└{'─' * bw}┘{rs}")
            input(f"\n{c}Press Enter to exit{rs}")
            return
    else:
        print(f"{c}│{rs} {g}[+] Pip is ready{rs}")
    
    print(f"{c}└{'─' * bw}┘{rs}")
    print()
    
    while True:
        ch = a11()
        
        if ch == "1":
            a12()
        elif ch == "2":
            a13()
        elif ch == "3":
            continue
        elif ch == "4":
            break
        else:
            print(f"\n{r}[!] Invalid choice{rs}")
            time.sleep(1)

if __name__ == "__main__":
    a14()
