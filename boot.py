import os                                             import sys                                            import time
import json
import urllib.request
import urllib.error
import hashlib
import shutil
import zipfile
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed

def banner():
    print(r"""
+--- 23 KOD UPDATER
|  by fevber on discord
------------------------------""")

def b1():
    os.system('clear')
    banner()

def b2():
    print("|  Initializing...")
    time.sleep(0.2)

def b3():
    print("|  Fetching files from GitHub...")
    time.sleep(0.2)

    try:
        url = "https://api.github.com/repos/fevberr/KOD/contents"
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        req.add_header('Accept', 'application/vnd.github.v3+json')
        r = urllib.request.urlopen(req, timeout=15)
        data = json.loads(r.read().decode())
        print("|  Connected to GitHub (API)")
        return data
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("|  API rate limited, downloading ZIP...")
            return b3_zip()
    except Exception as e:
        print(f"|  API error: {str(e)[:40]}")

    return b3_zip()

def b3_zip():
    print("|  Downloading repository as ZIP...")
    try:
        zip_url = "https://github.com/fevberr/KOD/archive/refs/heads/main.zip"
        req = urllib.request.Request(zip_url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        r = urllib.request.urlopen(req, timeout=30)

        temp_zip = tempfile.mktemp(suffix='.zip')
        with open(temp_zip, 'wb') as f:
            f.write(r.read())

        print("|  Extracting ZIP...")
        extract_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        os.remove(temp_zip)

        items = os.listdir(extract_dir)
        repo_dir = None
        for item in items:
            full_path = os.path.join(extract_dir, item)
            if os.path.isdir(full_path) and ('KOD' in item or 'main' in item):
                repo_dir = full_path
                break

        if not repo_dir:
            repo_dir = extract_dir

        print(f"|  Found repo at: {repo_dir}")

        files = []
        for root, dirs, filenames in os.walk(repo_dir):
            for filename in filenames:
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, repo_dir)
                if rel_path == '.' or rel_path.startswith('.'):
                    continue
                try:
                    with open(full_path, 'rb') as f:
                        sha = hashlib.sha1(f.read()).hexdigest()
                    files.append({
                        'name': filename,
                        'path': rel_path,
                        'type': 'file',
                        'sha': sha,
                        'download_url': None
                    })
                except:
                    pass

        print(f"|  Found {len(files)} files in ZIP")

        print("|  Copying files...")
        for file in files:
            src = os.path.join(repo_dir, file['path'])
            dst = file['path']
            try:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                print(f"|  [COPY] {dst}")
            except Exception as e:
                print(f"|  [FAIL] {dst}: {str(e)[:30]}")

        shutil.rmtree(extract_dir)
        print(f"|  Downloaded {len(files)} files via ZIP")
        return files

    except Exception as e:
        print(f"|  ZIP error: {str(e)[:50]}")
        return None

def b4():
    files = b3()
    if not files:
        print("|  No files from GitHub, using local")
        return

    github_files = {}
    total = up_to_date = changed = new_files = deleted = 0
    changed_list, new_list, deleted_list = [], [], []

    print("|")
    print("|  Scanning files...")
    print("|")

    def sync_file(path, sha, download_url):
        nonlocal total, up_to_date, changed, new_files
        total += 1
        github_files[path] = sha

        if os.path.exists(path):
            try:
                with open(path, 'rb') as f:
                    local = hashlib.sha1(f.read()).hexdigest()
                if local == sha:
                    up_to_date += 1
                    print(f"|  [OK] {path}")
                else:
                    changed += 1
                    changed_list.append(path)
                    print(f"|  [CHANGED] {path}")
            except:
                changed += 1
                changed_list.append(path)
                print(f"|  [ERROR] {path}")
        else:
            new_files += 1
            new_list.append(path)
            print(f"|  [NEW] {path}")

    for item in files:
        if item.get('type') == 'file':
            sync_file(item.get('path'), item.get('sha'), item.get('download_url'))
        elif item.get('type') == 'dir':
            folder = item.get('path')
            try:
                url = f"https://api.github.com/repos/fevberr/KOD/contents/{folder}"
                req = urllib.request.Request(url)
                req.add_header('User-Agent', 'Mozilla/5.0')
                req.add_header('Accept', 'application/vnd.github.v3+json')
                r = urllib.request.urlopen(req, timeout=15)
                sub = json.loads(r.read().decode())
                for s in sub:
                    if s.get('type') == 'file':
                        sync_file(s.get('path'), s.get('sha'), s.get('download_url'))
            except:
                pass

    print("|")
    print("|  Checking for deleted files...")
    print("|")

    for root, dirs, files_local in os.walk("."):
        for f in files_local:
            if ".git" in root or "__pycache__" in root or f == "boot.py":
                continue
            path = os.path.join(root, f).lstrip("./")
            if path not in github_files:
                deleted += 1
                deleted_list.append(path)
                print(f"|  [DELETED] {path}")
                try:
                    os.remove(path)
                    print(f"|  [REMOVED] {path}")
                except:
                    print(f"|  [FAILED] {path}")

    for root, dirs, files_local in os.walk(".", topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if ".git" in dir_path or "__pycache__" in dir_path:
                continue
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"|  [REMOVED DIR] {dir_path}")
            except:
                pass

    print("|")
    print("|  " + "-" * 40)
    print(f"|  Total files: {total}")
    print(f"|  Up to date: {up_to_date}")
    if changed > 0:
        print(f"|  Changed: {changed}")
        print("|")
        print("|  Changed files:")
        for f in changed_list[:10]:
            print(f"|    - {f}")
        if len(changed_list) > 10:
            print(f"|    ... and {len(changed_list)-10} more")
    if new_files > 0:
        print(f"|  New: {new_files}")
        print("|")
        print("|  New files:")
        for f in new_list[:10]:
            print(f"|    - {f}")
        if len(new_list) > 10:
            print(f"|    ... and {len(new_list)-10} more")
    if deleted > 0:
        print(f"|  Deleted: {deleted}")
        print("|")
        print("|  Deleted files:")
        for f in deleted_list[:10]:
            print(f"|    - {f}")
        if len(deleted_list) > 10:
            print(f"|    ... and {len(deleted_list)-10} more")
    print("|  " + "-" * 40)

    if changed == 0 and new_files == 0 and deleted == 0:
        print("|  Everything is up to date!")

def b5():
    print("|")
    print("|- Sync complete")
    print("|")
    version = "1.3.4"
    if os.path.exists("data/version.txt"):
        try:
            with open("data/version.txt", "r") as f:
                version = f.read().strip()
        except:
            pass
    print(f"|- Version: {version}")
    print("|")
    print("|- Join our Discord for updates?")
    print("|  [OK] [NO]")
    print("|")

    choice = input("|- Select > ").strip().lower()

    if choice == "ok":
        print("|")
        print("|- Thanks :D")
        print("|  https://discord.gg/xrvgQD9s9b")
    elif choice == "no":
        print("|")
        print("|- idc have the invite :D")
        print("|  https://discord.gg/xrvgQD9s9b")
    else:
        print("|")
        print("|- Invalid choice")

    print("|")
    print("|- 23 KOD Framework loaded")
    print("------------------------------")

def b12():
    b1()
    b2()
    b4()
    b5()

if __name__ == "__main__":