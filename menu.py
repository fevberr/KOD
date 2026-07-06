import os
import sys
import time
from config import g1, g2, host, port, device, system, ping

I1 = 5

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

def s2(m1, q1):
    if not q1:
        return m1
    return [x for x in m1 if q1.lower() in x.lower()]

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        from display.banner import b1
        from display.panels import p1
        b1()
        i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
        p1("23 KOD", i1, "READY")
        
        n2 = n1()
        t1 = max(1, len(n2))
        
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        
        c2 = o1(p4)
        
        tab_display = []
        for i, name in enumerate(n2):
            if i == p4:
                tab_display.append(f"[{name}]")
            else:
                tab_display.append(f" {name} ")
        
        tab_line = ' '.join(tab_display)
        print(f"\n* menu | {tab_line}")
        print("|")
        if not c2:
            print("|   (coming soon...)")
        else:
            for i, m5 in enumerate(c2, 1):
                print(f"| > {i}  | {m5}")
        
        print(f"|\n|- 0  Exit")
        print(f"|- s  Search")
        print(f"|- i  Install packages")
        print(f"|- t1, t2, t3... to switch tabs")
        print("------------------------")
        
        sys.stdout.flush()
        try:
            c1 = input("Select option > ").strip().lower()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        
        if c1 == "0":
            print("Exiting...")
            break
        
        if c1 == "s":
            q1 = input("Enter search term: ").strip()
            p4 = 0
            continue
        
        if c1 == "i":
            try:
                from installer import a11
                a11()
            except ImportError:
                print("\n[!] installer.py not found!")
                print("[*] Creating installer.py...")
                # Create installer on the fly
                create_installer()
                from installer import a11
                a11()
            continue
        
        if c1.startswith('t') and len(c1) > 1:
            try:
                t2 = int(c1[1:])
                if 1 <= t2 <= t1:
                    p4 = t2 - 1
                    print(f"\nSwitched to tab: {n2[p4]}")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"Tab {t2} doesn't exist (1-{t1})")
                    time.sleep(1)
                    continue
            except:
                print("Invalid tab number")
                time.sleep(1)
                continue
        
        if not c1.isdigit():
            print("Invalid option")
            time.sleep(1)
            continue
        
        i2 = int(c1) - 1
        c2 = o1(p4)
        
        if c2 and 0 <= i2 < len(c2):
            m5 = c2[i2]
            m6 = f"modules/{m5}"
            if os.path.exists(m6):
                import importlib.util
                spec = importlib.util.spec_from_file_location(m5[:-3], m6)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, 'run'):
                    print("\n[+] Running...")
                    result = module.run()
                    print(result)
                    input("\nPress Enter...")
                else:
                    print("\n[!] No run() function found")
                    input("Press Enter...")
            else:
                print(f"\nModule {m5} not found!")
                input("Press Enter...")
        else:
            if c2:
                print("Invalid option")
            else:
                print("No modules")
            time.sleep(1)

def create_installer():
    """Create installer.py if missing"""
    installer_code = '''
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
        print("\\n[!] requirements.txt not found!")
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
    
    print("\\n" + "━" * w)
    print("Package Installer")
    print("━" * w)
    print("\\n[+] Checking installed packages...\\n")
    
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
    
    print("\\n" + "━" * w)
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
    
    print("\\n" + "━" * w)
    print("Installing All Packages")
    print("━" * w)
    print(f"\\nTotal: {len(p)} packages\\n")
    
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
    input("\\nPress Enter...")

def a10():
    w = a1()
    p = a2()
    if not p:
        return
    
    print("\\n" + "━" * w)
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
        print("\\n[+] All packages installed!")
        input("\\nPress Enter...")
        return
    
    print("\\n" + "━" * w)
    print("Installing Missing Packages")
    print("━" * w)
    print(f"\\nMissing: {len(m)}\\n")
    
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
    input("\\nPress Enter...")

def a11():
    w = a1()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        a9()
        return
    
    print("\\n" + "━" * w)
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
            input("\\nPress Enter...")
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
            print("\\n[!] Invalid choice")
            input("\\nPress Enter...")

if __name__ == "__main__":
    a11()
'''
    with open('installer.py', 'w') as f:
        f.write(installer_code)
    print("[+] installer.py created!")
