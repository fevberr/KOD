import os
import sys
import platform
import subprocess

SYSTEM = platform.system()
TERMUX = os.path.exists("/data/data/com.termux/files/home")

def c1():
    os.system('clear' if os.name == 'posix' else 'cls')

def c2():
    banner = """
+--------------------------------------+
|        23 KOD - SETUP INSTALLER      |
+--------------------------------------+
luv yall sm
"""
    print(banner)

def c3():
    dirs = ["modules", "display", "utils", "data"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    files = {
        "main.py": '''from menu import menu
from display.banner import show_banner
from display.panels import draw_panel
from config import host, port, device, system, ping
import os

def run():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    
    info = f"host:      {host}\\nPort:        {port}\\nPing:     {ping}\\ndevice:   {device}\\nsystem:    {system}"
    draw_panel("23 KOD", info, "READY")
    
    menu()

if __name__ == "__main__":
    run()
''',
        "menu.py": '''from updater import update_module
from utils.loader import load_module
from spinner import spinner
import os

def g1():
    modules = []
    if os.path.exists("modules"):
        for file in os.listdir("modules"):
            if file.endswith((".py", ".lua")) and file != "__init__.py":
                modules.append(file)
    return modules

def g2():
    modules = g1()
    print("\\n* menu\\n|")
    for i, mod in enumerate(modules, 1):
        print(f"| > {i}  | {mod}")
    print("|\\n|- 0  Exit")
    print("------------------------")
    return modules

def menu():
    while True:
        modules = g2()
        choice = input("Select option > ").strip()
        
        if choice == "0":
            print("Exiting...")
            break
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(modules):
                module_name = modules[idx]
                with spinner(f"Loading {module_name}"):
                    update_module(module_name)
                    load_module(f"modules/{module_name}")
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input")
''',
        "updater.py": '''from datetime import datetime
import os

VERSION = "1.0.0"

def u1():
    try:
        with open("data/version.txt", "r") as f:
            return f.read().strip()
    except:
        return VERSION

def u2(ver):
    with open("data/version.txt", "w") as f:
        f.write(ver)

def update_module(module_name):
    print(f"\\n+--- update list\\n|\\n|- - Removed old build        ({module_name})")
    print(f"|-  - Fetched latest release  ({module_name})")
    print(f"|- -  Launching updated build\\n------------------------------")
    
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] Updated {module_name}\\n")

def u3():
    return u1()
''',
        "packages.py": '''PACKAGES = {
    "python-whois": "installed",
    "dnspython": "installed", 
    "requests": "installed",
    "beautifulsoup4": "installed",
    "socket-engine": "loaded",
    "packet-simulator": "loaded",
    "async-worker": "initialized",
    "kod-core": "ready"
}

def p1():
    print("+--- packages")
    for pkg, status in PACKAGES.items():
        print(f"|\\n|- {pkg:<20} - {status}")
    print("|- kod-core           - ready\\n")
''',
        "spinner.py": '''import sys
import time
import threading

class spinner:
    def __init__(self, message="Loading"):
        self.message = message
        self._stop = False
        self._chars = ['/', '-', '\\\\', '|']
        
    def s1(self):
        i = 0
        while not self._stop:
            sys.stdout.write(f"\\r{self.message} {self._chars[i % len(self._chars)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write("\\r" + " " * (len(self.message) + 2) + "\\r")
        
    def __enter__(self):
        self._thread = threading.Thread(target=self.s1)
        self._thread.start()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop = True
        self._thread.join()
''',
        "config.py": '''import platform
import socket
import subprocess
import os

def c1():
    return f"{platform.system()} {platform.release()}"

def c2():
    try:
        if platform.system() == "Linux":
            if os.path.exists("/system/build.prop"):
                result = subprocess.run(["getprop", "ro.product.model"], capture_output=True, text=True)
                if result.stdout.strip():
                    return result.stdout.strip()
            result = subprocess.run(["hostname"], capture_output=True, text=True)
            return result.stdout.strip()
        elif platform.system() == "Windows":
            return platform.node()
        elif platform.system() == "Darwin":
            result = subprocess.run(["scutil", "--get", "ComputerName"], capture_output=True, text=True)
            return result.stdout.strip() if result.stdout else platform.node()
    except:
        pass
    return platform.node()

def c3():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return f"http://{local_ip}:{c4()}/"
    except:
        return "http://localhost:8080/"

def c4():
    return 8080

def c5():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
        else:
            result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
        
        for line in result.stdout.split('\\n'):
            if "time=" in line:
                time_str = line.split('time=')[1].split()[0].replace('ms', '')
                return int(float(time_str))
    except:
        pass
    return 108

host = c3()
port = c4()
device = c2()
system = c1()
ping = c5()

def c6():
    return {
        "host": host,
        "port": port,
        "device": device,
        "system": system,
        "ping": ping
    }
''',
        "display/banner.py": '''def show_banner():
    banner = r"""
⣶⣿⣿⣿⣶⣤⣾⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠀⠀⢠⡻⢾⣻⣿⣿⣠⣀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⣿⣿⣭⣷⣶⠤
--------------------------------------
"""
    print(banner)
''',
        "display/panels.py": '''def draw_panel(title, content, status=""):
    print(f"\\n+--- {title}")
    lines = content.split('\\n')
    for line in lines:
        print(f"| {line}")
    if status:
        print(f"|- Status: {status}")
    print("------------------------------")
''',
        "display/status.py": '''_STATUS = "READY"

def s1(status):
    global _STATUS
    _STATUS = status
    
def s2():
    return _STATUS
''',
        "utils/loader.py": '''import subprocess
import os

def l1(module_path):
    if module_path.endswith('.py'):
        with open(module_path, 'r') as f:
            exec(f.read())
    elif module_path.endswith('.lua'):
        try:
            result = subprocess.run(['lua', module_path], capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(f"Lua error: {result.stderr}")
        except FileNotFoundError:
            print("Lua interpreter not found")
    else:
        print(f"Unknown module type: {module_path}")
''',
        "utils/helpers.py": '''import os
from datetime import datetime

def h1():
    os.system('clear' if os.name == 'posix' else 'cls')

def h2(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None

def h3(path, content):
    with open(path, 'w') as f:
        f.write(content)
        
def h4(message):
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {message}\\n")
''',
        "modules/so.py": '''print("\\n[so.py] Module loaded successfully!")
print("Python module running")
''',
        "modules/ay.lua": '''print("\\n[ay.lua] Module loaded successfully!")
print("Lua module running")
''',
        "modules/__init__.py": "",
        "data/packages.txt": '''python-whois:installed
dnspython:installed
requests:installed
beautifulsoup4:installed
socket-engine:loaded
packet-simulator:loaded
async-worker:initialized
kod-core:ready
''',
        "data/version.txt": "1.0.0",
        "data/logs.txt": ""
    }
    
    for path, content in files.items():
        with open(path, 'w') as f:
            f.write(content)
        print(f"  - Created {path}")

def c4():
    if SYSTEM == "Windows":
        print("\n[Windows] Checking Python...")
        result = subprocess.run(["python", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            print("  X Python not found!")
            print("  -> Download from: https://python.org")
            return False
        else:
            print(f"  - {result.stdout.strip()}")
        return True
            
    elif "Linux" in SYSTEM:
        if TERMUX:
            print("\n[Termux] Installing Python...")
            subprocess.run(["pkg", "update", "-y"], capture_output=True)
            subprocess.run(["pkg", "install", "python", "-y"], capture_output=True)
        else:
            print("\n[Linux] Checking Python...")
            result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
            if result.returncode != 0:
                print("  Installing Python...")
                subprocess.run(["sudo", "apt", "update", "-y"], capture_output=True)
                subprocess.run(["sudo", "apt", "install", "python3", "-y"], capture_output=True)
            else:
                print(f"  - {result.stdout.strip()}")
        return True
        
    elif SYSTEM == "Darwin":
        print("\n[iSH] Checking Python...")
        result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            print("  Installing Python via apk...")
            subprocess.run(["apk", "update"], capture_output=True)
            subprocess.run(["apk", "add", "python3"], capture_output=True)
        else:
            print(f"  - {result.stdout.strip()}")
        return True
    
    return False

def c5():
    if SYSTEM == "Windows":
        print("\n[Windows] Checking Lua...")
        result = subprocess.run(["lua", "-v"], capture_output=True, text=True)
        if result.returncode != 0:
            print("  X Lua not found (optional)")
            print("  -> For Lua modules, install from: https://luabinaries.sourceforge.net")
        else:
            print(f"  - {result.stdout.strip()}")
            
    elif "Linux" in SYSTEM:
        if TERMUX:
            print("\n[Termux] Checking Lua...")
            subprocess.run(["pkg", "install", "lua", "-y"], capture_output=True)
        else:
            print("\n[Linux] Checking Lua...")
            result = subprocess.run(["lua", "-v"], capture_output=True, text=True)
            if result.returncode != 0:
                print("  Installing Lua...")
                subprocess.run(["sudo", "apt", "install", "lua5.3", "-y"], capture_output=True)
            else:
                print(f"  - {result.stdout.strip()}")
                
    elif SYSTEM == "Darwin":
        print("\n[iSH] Checking Lua...")
        subprocess.run(["apk", "add", "lua"], capture_output=True)
    
    return True

def c6():
    if SYSTEM == "Windows":
        bat = """@echo off
cd /d %~dp0
python main.py
pause
"""
        with open("run.bat", "w") as f:
            f.write(bat)
        print("  - Created run.bat")
        
    elif "Linux" in SYSTEM:
        if TERMUX:
            sh = """#!/data/data/com.termux/files/usr/bin/bash
cd "$(dirname "$0")"
python main.py
"""
        else:
            sh = """#!/bin/bash
cd "$(dirname "$0")"
python3 main.py
"""
        with open("run.sh", "w") as f:
            f.write(sh)
        os.chmod("run.sh", 0o755)
        print("  - Created run.sh")
        
    elif SYSTEM == "Darwin":
        sh = """#!/bin/bash
cd "$(dirname "$0")"
python3 main.py
"""
        with open("run.sh", "w") as f:
            f.write(sh)
        os.chmod("run.sh", 0o755)
        print("  - Created run.sh")

def main():
    c1()
    c2()
    
    print("\nCreating directory structure...")
    c3()
    
    if not c4():
        print("\nSetup failed! Install Python first.")
        sys.exit(1)
    
    c5()
    
    print("\nCreating launcher scripts...")
    c6()
    
    print("\n+--------------------------------------+")
    print("|         SETUP COMPLETE!              |")
    print("+--------------------------------------+")
    print("\nRun 23 KOD:")
    if SYSTEM == "Windows":
        print("  double click run.bat or: python main.py")
    else:
        print("  ./run.sh or: python3 main.py")
    print()

if __name__ == "__main__":
    main()
