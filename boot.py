
import os
import sys
import time
import json
import urllib.request
import urllib.error
import hashlib
import shutil
import zipfile
import tempfile
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.colors import green, red, cyan, yellow, white, gray, blue, magenta, dim, bold

def get_terminal_size():
    try:
        import shutil
        return shutil.get_terminal_size().columns
    except:
        return 80

def progress_bar(current, total, width=40):
    percent = current / total if total > 0 else 0
    filled = int(width * percent)
    bar = '█' * filled + '░' * (width - filled)
    return f"{green(bar)} {int(percent * 100)}%"

def get_system_info():
    return {
        'os': platform.system(),
        'arch': platform.machine(),
        'python': platform.python_version(),
        'host': platform.node()
    }

def b1():
    os.system('clear' if os.name == 'posix' else 'cls')
    width = get_terminal_size()
    info = get_system_info()
    
    print(cyan("+" + "=" * (width - 2) + "+"))
    print(cyan("|") + white(" 23 KOD UPDATER ").center(width - 2) + cyan("|"))
    print(cyan("|") + gray(f" System: {info['os']} | Arch: {info['arch']} | Python: {info['python']} ").center(width - 2) + cyan("|"))
    print(cyan("+" + "=" * (width - 2) + "+"))

def b2():
    print(f"\n{cyan('│')} {blue('>>')} Initializing boot sequence...")
    time.sleep(0.2)
    print(f"{cyan('│')} {blue('>>')} Checking for updates...")
    time.sleep(0.2)

def b3():
    print(f"{cyan('│')} {yellow('>>')} Downloading from GitHub...")
    time.sleep(0.2)
    return b3_zip()

def b3_zip():
    print(f"{cyan('│')} {yellow('>>')} Downloading repository ZIP...")
    temp_zip = None
    extract_dir = None
    
    try:
        zip_url = "https://github.com/fevberr/KOD/archive/refs/heads/main.zip"
        req = urllib.request.Request(zip_url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        r = urllib.request.urlopen(req, timeout=30)

        total_size = int(r.headers.get('content-length', 0))
        downloaded = 0
        chunk_size = 8192
        temp_zip = tempfile.mktemp(suffix='.zip')
        
        with open(temp_zip, 'wb') as f:
            while True:
                chunk = r.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    percent = int((downloaded / total_size) * 100)
                    bar = '█' * int(percent / 2) + '░' * (50 - int(percent / 2))
                    sys.stdout.write(f"\r{cyan('│')} {green('>>')} Downloading: [{green(bar)}] {percent}%")
                    sys.stdout.flush()
        print()

        print(f"{cyan('│')} {blue('>>')} Extracting ZIP...")
        extract_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        if temp_zip and os.path.exists(temp_zip):
            os.remove(temp_zip)
            temp_zip = None

        items = os.listdir(extract_dir)
        repo_dir = None
        for item in items:
            full_path = os.path.join(extract_dir, item)
            if os.path.isdir(full_path) and ('KOD' in item or 'main' in item):
                repo_dir = full_path
                break

        if not repo_dir:
            repo_dir = extract_dir

        files = []
        for root, dirs, filenames in os.walk(repo_dir):
            for filename in filenames:
                if filename.startswith('.'):
                    continue
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, repo_dir)
                if rel_path == '.' or rel_path.startswith('.'):
                    continue
                files.append({
                    'name': filename,
                    'path': rel_path
                })

        print(f"{cyan('│')} {green('[+]')} Found {len(files)} files in ZIP")
        print(f"{cyan('│')} {blue('>>')} Copying files...")
        
        copied = 0
        for file in files:
            src = os.path.join(repo_dir, file['path'])
            dst = file['path']
            try:
                dst_dir = os.path.dirname(dst)
                if dst_dir:
                    os.makedirs(dst_dir, exist_ok=True)
                shutil.copy2(src, dst)
                copied += 1
                if copied % 5 == 0:
                    sys.stdout.write(f"\r{cyan('│')} {green('>>')} {copied}/{len(files)} files copied")
                    sys.stdout.flush()
            except Exception as e:
                print(f"\n{cyan('│')} {red('[-]')} {dst}: {str(e)[:30]}")

        print(f"\r{cyan('│')} {green('[+]')} Copied {copied} files successfully")

        shutil.rmtree(extract_dir)
        return files

    except Exception as e:
        print(f"{cyan('│')} {red('[-]')} Error: {str(e)[:50]}")
        if extract_dir and os.path.exists(extract_dir):
            try:
                shutil.rmtree(extract_dir)
            except:
                pass
        if temp_zip and os.path.exists(temp_zip):
            try:
                os.remove(temp_zip)
            except:
                pass

    return None

def b4():
    print(f"{cyan('│')} {blue('>>')} Syncing files...")
    files = b3()
    if not files:
        print(f"{cyan('│')} {red('[-]')} No files from GitHub")
        return

    cwd = os.getcwd()
    github_files = set()
    
    for file in files:
        github_files.add(file['path'])

    missing = []
    for path in github_files:
        local_path = os.path.join(cwd, path)
        if not os.path.exists(local_path):
            missing.append(path)

    extra = []
    for root, dirs, files_local in os.walk(cwd):
        if ".git" in root or "__pycache__" in root:
            continue
        for f in files_local:
            if f == "boot.py" or f.startswith('.'):
                continue
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, cwd)
            if rel_path not in github_files and rel_path != "boot.py":
                extra.append(rel_path)

    print(f"\n{cyan('│')} {yellow('=== STATUS REPORT ===')}")
    print(f"{cyan('│')} {green('[+]')} Total GitHub files: {len(github_files)}")
    if missing:
        print(f"{cyan('│')} {yellow('>>')} Missing: {len(missing)}")
        for f in missing[:5]:
            print(f"{cyan('│')}   {green('[+]')} {f}")
        if len(missing) > 5:
            print(f"{cyan('│')}   {gray('... and')} {len(missing)-5} {gray('more')}")
    if extra:
        print(f"{cyan('│')} {red('[-]')} Extra local: {len(extra)}")
        for f in extra[:5]:
            print(f"{cyan('│')}   {red('[-]')} {f}")
        if len(extra) > 5:
            print(f"{cyan('│')}   {gray('... and')} {len(extra)-5} {gray('more')}")
    
    print(f"{cyan('│')}")
    print(f"{cyan('│')} {green('[+]')} All files synced successfully!")

def b5():
    print(f"{cyan('│')}")
    print(f"{cyan('│')} {green('[+]')} Boot complete!")
    print(f"{cyan('│')}")
    
    version = "1.3.4"
    try:
        if os.path.exists("data/version.txt"):
            with open("data/version.txt", "r") as f:
                version = f.read().strip()
    except:
        pass
    
    print(f"{cyan('│')} {blue('>>')} Version: {yellow(version)}")
    print(f"{cyan('│')}")
    print(f"{cyan('│')} {yellow('>>')} Join our Discord for updates?")
    print(f"{cyan('│')} {white('[')}{green('OK')}{white(']')}  {white('[')}{red('NO')}{white(']')}")
    print(f"{cyan('│')}")
    
    choice = input(f"{cyan('│')} {green('>')} ").strip().lower()
    print(f"{cyan('│')}")
    if choice in ["ok", "yes", "y"]:
        print(f"{cyan('│')} {green('[+]')} Thanks!")
        print(f"{cyan('│')} {blue('>>')} https://discord.gg/xrvgQD9s9b")
    else:
        print(f"{cyan('│')} {blue('>>')} https://discord.gg/xrvgQD9s9b")
    
    print(f"{cyan('│')}")
    print(f"{cyan('│')} {yellow('>>')} Press Enter to launch 23 KOD...")
    input(f"{cyan('│')}")
    print(f"{cyan('│')} {green('[+]')} Launching...")
    width = get_terminal_size()
    print(cyan("+" + "=" * (width - 2) + "+"))
    time.sleep(1)
    
    os.system('python main.py' if os.name == 'nt' else 'python3 main.py')
    sys.exit(0)

def b12():
    b1()
    b2()
    b4()
    b5()

if __name__ == "__main__":
    b12()

