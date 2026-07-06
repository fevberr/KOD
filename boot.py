import os
import sys
import time
import json
import urllib.request
import urllib.error
import shutil
import platform
from urllib.parse import urlparse

def a1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
+--- 23 KOD
|  Loader
|  Starting system...
------------------------------
""")

def a2():
    steps = [
        "Fetching file list",
        "Downloading core files",
        "Downloading modules",
        "Downloading display files",
        "Downloading utils",
        "Verifying integrity",
        "Ready"
    ]
    
    all_files = a8()
    
    for step in steps:
        sys.stdout.write(f"|  {step}")
        sys.stdout.flush()
        time.sleep(0.3)
        
        if step == "Fetching file list":
            files = a8()
            if files:
                sys.stdout.write(" [OK]")
                sys.stdout.flush()
                time.sleep(0.2)
                print()
                continue
            else:
                sys.stdout.write(" [FAILED]")
                sys.stdout.flush()
                time.sleep(0.3)
                print()
                return False
        
        if step == "Downloading core files":
            a9(all_files, "", ["config.py", "loader.py", "menu.py", "main.py"])
        elif step == "Downloading modules":
            a9(all_files, "modules/")
        elif step == "Downloading display files":
            a9(all_files, "display/")
        elif step == "Downloading utils":
            a9(all_files, "utils/")
        
        sys.stdout.write(" [OK]")
        sys.stdout.flush()
        time.sleep(0.2)
        print()
    return True

def a8():
    try:
        api_url = "https://api.github.com/repos/fevberr/KOD/contents"
        req = urllib.request.Request(api_url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        response = urllib.request.urlopen(req, timeout=10)
        data = json.loads(response.read().decode())
        return data
    except:
        return []

def a7(folder_path):
    try:
        api_url = f"https://api.github.com/repos/fevberr/KOD/contents/{folder_path}"
        req = urllib.request.Request(api_url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        response = urllib.request.urlopen(req, timeout=10)
        data = json.loads(response.read().decode())
        return data
    except:
        return []

def a6(url, path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        response = urllib.request.urlopen(req, timeout=10)
        with open(path, 'wb') as f:
            f.write(response.read())
        return True
    except:
        return False

def a9(files, folder="", specific=None):
    for file in files:
        if file.get('type') == 'file':
            name = file.get('name')
            if specific and name not in specific:
                continue
            if folder and not name.endswith('.py'):
                continue
            if folder and folder in file.get('path', ''):
                download_url = file.get('download_url')
                if download_url:
                    path = file.get('path')
                    sys.stdout.write(f"\r|  downloading {path}")
                    sys.stdout.flush()
                    if a6(download_url, path):
                        time.sleep(0.1)
                        sys.stdout.write(f"\r|  downloading {path} [OK]")
                        sys.stdout.flush()
                        time.sleep(0.1)
                        print()
                    else:
                        sys.stdout.write(f"\r|  downloading {path} [FAILED]")
                        sys.stdout.flush()
                        time.sleep(0.1)
                        print()
        elif file.get('type') == 'dir':
            sub_files = a7(file.get('path'))
            for sub_file in sub_files:
                if sub_file.get('type') == 'file':
                    download_url = sub_file.get('download_url')
                    if download_url:
                        path = sub_file.get('path')
                        sys.stdout.write(f"\r|  downloading {path}")
                        sys.stdout.flush()
                        if a6(download_url, path):
                            time.sleep(0.1)
                            sys.stdout.write(f"\r|  downloading {path} [OK]")
                            sys.stdout.flush()
                            time.sleep(0.1)
                            print()
                        else:
                            sys.stdout.write(f"\r|  downloading {path} [FAILED]")
                            sys.stdout.flush()
                            time.sleep(0.1)
                            print()

def a3():
    print("|")
    print("|  Progress:")
    for i in range(101):
        time.sleep(0.015)
        p = i / 100
        f = int(30 * p)
        bar = '█' * f + '░' * (30 - f)
        sys.stdout.write(f"\r|  [{bar}] {i}%")
        sys.stdout.flush()
    print()

def a4():
    print("|")
    print("|- Boot complete")
    print("|- loaded successfully")
    print("|")
    print("|- Join our Discord for updates?")
    print("|  [OK] [NO]")
    print("|")
    
    try:
        choice = input("|- Select > ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\n|")
        print("|- Exiting...")
        print("------------------------------")
        sys.exit(0)
    
    if choice == "ok":
        print("|")
        print("|- Thanks :D")
        print("|  https://discord.gg/xrvgQD9s9b")
    elif choice == "no":
        print("|")
        print("|- fuck u :(")
    else:
        print("|")
        print("|- Invalid choice")
    
    print("|")
    print("|- Starting 23 KOD...")
    print("------------------------------")
    time.sleep(2)
    
    os.system('python main.py' if os.name == 'nt' else 'python3 main.py')
    sys.exit(0)

def a5():
    a1()
    a2()
    a3()
    a4()

if __name__ == "__main__":
    a5()
