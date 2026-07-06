
import subprocess
import sys
import os
import time
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed

def a1():
    try:
        import shutil
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
        r = subprocess.run([sys.executable, '-m', 'pip', 'install', p, '--quiet'], capture_output=True, text=True)
        return r.returncode == 0
    except:
        return False

def a7(c, t, w=30):
    p = c / t if t > 0 else 0
    f = int(w * p)
    b = '█' * f + '░' * (w - f)
    return f"{b} {int(p * 100)}%"

def a8():
    w = a1()
    p = a2()
    if not p:
        return
    
    print("\n" + "━" * w)
    print("Package Installer")
    print("━" * w)
    print("\n[+] Checking installed packages...\n")
    
    i = []
    m = []
    
    with ThreadPoolExecutor(max_workers=10) as e:
        fs = {e.submit(a5, pkg): pkg for pkg in p}
        for f in as_completed(fs):
            pkg = fs[f]
            if f.result():
                i.append(pkg)
            else:
                m.append(pkg)
    
    t = len(p)
    ins = len(i)
    mis = len(m)
    
    print("\n" + "━" * w)
    print("Package Installer")
    print("━" * w)
    print()
    print(f"Status      : {'Ready' if not m else 'Missing packages'}")
    print(f"Installed   : {ins}/{t}")
    print(f"Missing     : {mis}")
    print(f"Progress    : {a7(ins, t, min(30, w-20))}")
    print()
    
    if i:
        print("Installed")
        print("──────────")
        md = min(8, w // 15)
        for pkg in i[:md]:
            print(f"  {pkg}")
        if len(i) > md:
            print(f"  ... and {len(i)-md} more")
        print()
    
    if m:
        print("Missing")
        print("───────")
        md = min(8, w // 15)
        for pkg in m[:md]:
            print(f"  {pkg}")
        if len(m) > md:
            print(f"  ... and {len(m)-md} more")
        print()
    
    print("━" * w)
    print()
    print("  [1] Install all packages")
    print("  [2] Install missing only")
    print("  [3] Refresh status")
    print("  [4] Back")
    print()
    
    return input("Select > ").strip()

def a9():
    w = a1()
    p = a2()
    if not p:
        return
    
    print("\n" + "━" * w)
    print("Installing All Packages")
    print("━" * w)
    print(f"\nTotal: {len(p)} packages\n")
    
    s = 0
    f = 0
    
    with ThreadPoolExecutor(max_workers=5) as e:
        fs = {e.submit(a6, pkg): pkg for pkg in p}
        for fu in as_completed(fs):
            pkg = fs[fu]
            if fu.result():
                print(f"  [+] {pkg}")
                s += 1
            else:
                print(f"  [!] {pkg}")
                f += 1
    
    print()
    print("━" * w)
    print(f"Complete: {s}/{len(p)} installed")
    if f > 0:
        print(f"Failed: {f}")
    print("━" * w)
    input("\nPress Enter...")

def a10():
    w = a1()
    p = a2()
    if not p:
        return
    
    print("\n" + "━" * w)
    print("Checking installed packages...")
    print("━" * w)
    print()
    
    m = []
    
    with ThreadPoolExecutor(max_workers=10) as e:
        fs = {e.submit(a5, pkg): pkg for pkg in p}
        for f in as_completed(fs):
            pkg = fs[f]
            if not f.result():
                m.append(pkg)
    
    if not m:
        print("\n[+] All packages installed!")
        input("\nPress Enter...")
        return
    
    print("\n" + "━" * w)
    print("Installing Missing Packages")
    print("━" * w)
    print(f"\nMissing: {len(m)}\n")
    
    s = 0
    f = 0
    
    with ThreadPoolExecutor(max_workers=5) as e:
        fs = {e.submit(a6, pkg): pkg for pkg in m}
        for fu in as_completed(fs):
            pkg = fs[fu]
            if fu.result():
                print(f"  [+] {pkg}")
                s += 1
            else:
                print(f"  [!] {pkg}")
                f += 1
    
    print()
    print("━" * w)
    print(f"Complete: {s}/{len(m)} installed")
    if f > 0:
        print(f"Failed: {f}")
    print("━" * w)
    input("\nPress Enter...")

def a11():
    w = a1()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        a9()
        return
    
    print("\n" + "━" * w)
    print("Package Installer")
    print("━" * w)
    print()
    
    if not a3():
        print("[!] Pip not installed!")
        print("[*] Attempting to install pip...")
        if a4():
            print("[+] Pip installed successfully!")
        else:
            print("[!] Could not install pip!")
            print("[*] Try: python -m ensurepip --upgrade")
            if platform.system() == "Linux" or "Android" in platform.system():
                print("[*] Or: apt install python3-pip")
            input("\nPress Enter...")
            return
    
    print("[+] Pip is ready")
    print()
    
    while True:
        c = a8()
        
        if c == "1":
            a9()
        elif c == "2":
            a10()
        elif c == "3":
            continue
        elif c == "4":
            break
        else:
            print("\n[!] Invalid choice")
            input("\nPress Enter...")

if __name__ == "__main__":
    a11()
