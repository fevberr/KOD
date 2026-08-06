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
import signal
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

DEBUG_MODE = False

def load_colors():
    try:
        with open("cache/CSET.json", 'r') as f:
            c = json.load(f)
            return {
                'primary': c.get('primary', '#00ffcc'),
                'secondary': c.get('secondary', '#ff6bff'),
                'success': c.get('success', '#00ff66'),
                'error': c.get('error', '#ff0044'),
                'warning': c.get('warning', '#ffaa00'),
                'info': c.get('info', '#0088ff'),
                'highlight': c.get('highlight', '#ffffff'),
                'dim': c.get('dim', '#888888'),
                'border': c.get('border', '#ff6bff'),
                'accent': c.get('accent', '#ffaa00'),
            }
    except:
        return {
            'primary': '#00ffcc',
            'secondary': '#ff6bff',
            'success': '#00ff66',
            'error': '#ff0044',
            'warning': '#ffaa00',
            'info': '#0088ff',
            'highlight': '#ffffff',
            'dim': '#888888',
            'border': '#ff6bff',
            'accent': '#ffaa00',
        }

def hex_to_ansi(hex_color):
    try:
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        if len(hex_color) == 6:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return f'\033[38;2;{r};{g};{b}m'
    except:
        pass
    return ''

COLORS = load_colors()
C1 = hex_to_ansi(COLORS['primary'])
C2 = hex_to_ansi(COLORS['secondary'])
C3 = hex_to_ansi(COLORS['success'])
C4 = hex_to_ansi(COLORS['error'])
C5 = hex_to_ansi(COLORS['warning'])
C6 = hex_to_ansi(COLORS['info'])
C7 = hex_to_ansi(COLORS['highlight'])
C8 = hex_to_ansi(COLORS['dim'])
C9 = hex_to_ansi(COLORS['border'])
C10 = hex_to_ansi(COLORS['accent'])

def colorize(text, code): 
    return f"{code}{text}{RESET}" if sys.stdout.isatty() else text

def green(t): return colorize(t, C3)
def red(t): return colorize(t, C4)
def cyan(t): return colorize(t, C1)
def yellow(t): return colorize(t, C5)
def white(t): return colorize(t, C7)
def gray(t): return colorize(t, C8)
def blue(t): return colorize(t, C6)
def magenta(t): return colorize(t, C2)
def dim(t): return colorize(t, DIM)
def bold(t): return colorize(t, BOLD)
def border(t): return colorize(t, C9)
def accent(t): return colorize(t, C10)

TERM_WIDTH = 80
TERM_HEIGHT = 24

def update_term_size():
    global TERM_WIDTH, TERM_HEIGHT
    try:
        size = shutil.get_terminal_size()
        TERM_WIDTH = size.columns
        TERM_HEIGHT = size.lines
    except:
        TERM_WIDTH = 80
        TERM_HEIGHT = 24

def handle_resize(signum, frame):
    update_term_size()

def get_term_width():
    update_term_size()
    return TERM_WIDTH

def get_term_height():
    update_term_size()
    return TERM_HEIGHT

def progress_bar(current, total, width=40):
    try:
        update_term_size()
        max_width = min(width, TERM_WIDTH - 20)
        if total <= 0: return f"{gray('█' * max_width)}"
        p = max(0, min(1, current / total))
        filled = int(max_width * p)
        bar = f"{C3}{'█' * filled}{RESET}{C8}{'░' * (max_width - filled)}{RESET}"
        return f"{bar} {C5}{int(p * 100)}%{RESET}"
    except:
        return f"[{current}/{total}]"

def system_info():
    try:
        return {
            'os': platform.system(),
            'arch': platform.machine(),
            'python': platform.python_version(),
            'host': platform.node(),
            'release': platform.release(),
        }
    except:
        return {
            'os': 'Unknown',
            'arch': 'Unknown',
            'python': 'Unknown',
            'host': 'Unknown',
            'release': 'Unknown',
        }

def is_ignored(path):
    ignore = ['cache', '.git', '__pycache__', '.pyc', '.pyo', '.pyd', '.DS_Store', 'Thumbs.db']
    return any(i in path for i in ignore)

def draw_banner():
    try:
        from display.banner import a3 as b1
        b1()
    except:
        print(f"{C1}23 KOD{RESET}")
        print(f"{C8}Bootloader v2.0{RESET}")

def draw_header():
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
        update_term_size()
        w = TERM_WIDTH
        info = system_info()
        
        top = border('╔' + '═' * (w - 2) + '╗')
        bottom = border('╚' + '═' * (w - 2) + '╝')
        
        print(f"\n{top}")
        draw_banner()
        
        sub = gray(f'System: {info["os"]} {info["release"]}  |  Arch: {info["arch"]}  |  Python: {info["python"]}')
        print(f"{border('║')}{RESET} {sub} {' ' * (w - len(sub) - 4)}{border('║')}")
        
        if DEBUG_MODE:
            dbg = red('[DEBUG MODE]')
            print(f"{border('║')}{RESET} {dbg} {' ' * (w - len(dbg) - 4)}{border('║')}")
        
        print(f"{bottom}")
    except:
        pass

def print_step(msg, status='info'):
    try:
        update_term_size()
        icons = {'info': '◈', 'success': '✔', 'error': '✘', 'warn': '⚠', 'wait': '◉'}
        colors = {'info': C6, 'success': C3, 'error': C4, 'warn': C5, 'wait': C2}
        icon = icons.get(status, '◈')
        color = colors.get(status, C7)
        max_len = TERM_WIDTH - 6
        if len(msg) > max_len:
            msg = msg[:max_len-3] + '...'
        print(f"{border('│')}{RESET} {color}{icon}{RESET} {white(msg)}")
    except:
        pass

def draw_divider():
    try:
        update_term_size()
        print(f"{border('├' + '─' * (TERM_WIDTH - 2) + '┤')}")
    except:
        pass

def check_network():
    try:
        req = urllib.request.Request("https://github.com")
        req.add_header('User-Agent', 'Mozilla/5.0')
        urllib.request.urlopen(req, timeout=5)
        return True
    except:
        return False

def download_repo():
    print_step("Checking network...", 'wait')
    if not check_network():
        print_step("No network connection!", 'error')
        return None
    
    print_step("Connecting to GitHub...", 'wait')
    temp_zip = None
    extract_dir = None
    
    for attempt in range(3):
        try:
            zip_url = "https://github.com/fevberr/KOD/archive/refs/heads/main.zip"
            req = urllib.request.Request(zip_url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            req.add_header('Accept-Encoding', 'gzip, deflate')
            
            print_step(f"Downloading (attempt {attempt + 1}/3)...", 'wait')
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
                        bar = progress_bar(downloaded, total_size, 30)
                        sys.stdout.write(f"\r{border('│')}{RESET} {C3}⬇{RESET} {white('Downloading:')} {bar}")
                        sys.stdout.flush()
            print()

            print_step("Extracting archive...", 'wait')
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
                dirs[:] = [d for d in dirs if not is_ignored(d)]
                for filename in filenames:
                    if filename.startswith('.') or is_ignored(filename):
                        continue
                    full_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(full_path, repo_dir)
                    if rel_path == '.' or rel_path.startswith('.'):
                        continue
                    files.append({'name': filename, 'path': rel_path})

            print_step(f"Found {len(files)} files", 'success')

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
                    if copied % 10 == 0:
                        bar = progress_bar(copied, len(files), 25)
                        sys.stdout.write(f"\r{border('│')}{RESET} {C3}✓{RESET} {white('Copying:')} {bar}")
                        sys.stdout.flush()
                except Exception as e:
                    print(f"\n{border('│')}{RESET} {C4}✘{RESET} {gray(f'{dst}: {str(e)[:30]}')}")

            print(f"\r{border('│')}{RESET} {C3}✔{RESET} {white(f'Copied {copied}/{len(files)} files')}")
            shutil.rmtree(extract_dir)
            return files

        except urllib.error.HTTPError as e:
            print_step(f"HTTP {e.code}: {e.reason}", 'error')
            if attempt < 2:
                print_step(f"Retrying in 3s...", 'warn')
                time.sleep(3)
        except urllib.error.URLError as e:
            print_step(f"Connection error: {e.reason}", 'error')
            if attempt < 2:
                print_step(f"Retrying in 3s...", 'warn')
                time.sleep(3)
        except Exception as e:
            print_step(f"Error: {str(e)[:50]}", 'error')
            if attempt < 2:
                print_step(f"Retrying in 3s...", 'warn')
                time.sleep(3)
        finally:
            if temp_zip and os.path.exists(temp_zip):
                try: os.remove(temp_zip)
                except: pass
            if extract_dir and os.path.exists(extract_dir):
                try: shutil.rmtree(extract_dir)
                except: pass
    
    print_step("Download failed after 3 attempts", 'error')
    return None

def sync_files(files):
    print_step("Synchronizing files...", 'wait')
    if not files:
        print_step("No files from GitHub, using local", 'warn')
        return

    try:
        cwd = os.getcwd()
        github_files = {f['path'] for f in files}

        deleted = 0
        local_files_found = 0
        
        for root, dirs, local_files in os.walk(cwd, topdown=False):
            if is_ignored(root):
                continue
            for f in local_files:
                if f == "boot.py" or f.startswith('.') or is_ignored(f):
                    continue
                local_files_found += 1
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, cwd)
                if rel_path not in github_files and rel_path != "boot.py":
                    try:
                        os.remove(full_path)
                        deleted += 1
                        if deleted <= 5:
                            print(f"{border('│')}{RESET} {C4}✘{RESET} {gray(f'Deleted: {rel_path}')}")
                    except Exception as e:
                        print(f"{border('│')}{RESET} {C4}✘{RESET} {gray(f'Failed: {rel_path}')}")

        for root, dirs, local_files in os.walk(cwd, topdown=False):
            if is_ignored(root):
                continue
            try:
                if not os.listdir(root) and root != cwd:
                    os.rmdir(root)
                    rel_path = os.path.relpath(root, cwd)
                    print(f"{border('│')}{RESET} {C4}✘{RESET} {gray(f'Removed: {rel_path}')}")
            except:
                pass

        missing = []
        for path in github_files:
            if is_ignored(path):
                continue
            if not os.path.exists(os.path.join(cwd, path)):
                missing.append(path)

        w = TERM_WIDTH
        box_width = min(40, w - 4)
        
        print(f"\n{border('╔' + '═' * box_width + '╗')}")
        print(f"{border('║')}{RESET} {bold(accent('STATUS REPORT'))}")
        print(f"{border('╟' + '─' * box_width + '╢')}")
        print(f"{border('║')}{RESET}  {C3}✔{RESET} GitHub files: {white(str(len(github_files)))}")
        print(f"{border('║')}{RESET}  {C8}◈{RESET} Local files: {white(str(local_files_found))}")
        if deleted > 0:
            print(f"{border('║')}{RESET}  {C4}✘{RESET} Deleted: {white(str(deleted))}")
        if missing:
            print(f"{border('║')}{RESET}  {C5}⚠{RESET} Missing: {white(str(len(missing)))}")
            for f in missing[:3]:
                display = f[:box_width - 10] + '...' if len(f) > box_width - 10 else f
                print(f"{border('║')}{RESET}    {C3}+{RESET} {gray(display)}")
            if len(missing) > 3:
                print(f"{border('║')}{RESET}    {gray(f'... and {len(missing)-3} more')}")
        print(f"{border('╚' + '═' * box_width + '╝')}")
        
    except Exception as e:
        print_step(f"Sync error: {str(e)}", 'error')

def finish():
    try:
        print(f"\n{border('│')}{RESET} {C3}✦{RESET} {bold(white('Boot complete!'))}")
        print(f"{border('│')}{RESET}")
        
        version = "1.3.4"
        try:
            if os.path.exists("data/version.txt"):
                with open("data/version.txt", "r") as f:
                    version = f.read().strip()
        except:
            pass
        
        w = TERM_WIDTH
        ver_display = f"Version: {version}"
        print(f"{border('│')}{RESET}  {C6}◈{RESET} {white(ver_display)}")
        
        if DEBUG_MODE:
            print(f"{border('│')}{RESET}  {C8}◉{RESET} {gray('Debug mode active')}")
        
        print(f"{border('│')}{RESET}")
        
        prompt = "Join Discord?"
        ok = f"{C3}[ OK ]{RESET}"
        no = f"{C4}[ NO ]{RESET}"
        
        if w > 40:
            print(f"{border('│')}{RESET}  {C5}◇{RESET} {white(prompt)}  {ok}  {no}")
        else:
            print(f"{border('│')}{RESET}  {C5}◇{RESET} {white(prompt)}")
            print(f"{border('│')}{RESET}  {ok}  {no}")
        
        print(f"{border('│')}{RESET}")
        
        print(f"{border('│')}{RESET} {C3}›{RESET} ", end="")
        choice = input().strip().lower()
        
        print(f"{border('│')}{RESET}")
        if choice in ["ok", "yes", "y"]:
            print(f"{border('│')}{RESET} {C3}✔{RESET} {white('https://discord.gg/xrvgQD9s9b')}")
        else:
            print(f"{border('│')}{RESET} {C6}◈{RESET} {white('https://discord.gg/xrvgQD9s9b')}")
        
        print(f"{border('│')}{RESET}")
        print(f"{border('│')}{RESET} {C5}▶{RESET} {white('Launching 23 KOD...')}")
        print(f"{border('╚' + '═' * (TERM_WIDTH - 2) + '╝')}")
        time.sleep(1)
        
        os.system('python main.py' if os.name == 'nt' else 'python3 main.py')
        sys.exit(0)
        
    except Exception as e:
        print(f"\n{red('[!] Finish error:')} {str(e)}")
        sys.exit(1)

def main():
    global DEBUG_MODE
    
    if '--debug' in sys.argv or '-d' in sys.argv:
        DEBUG_MODE = True
    
    try:
        update_term_size()
        
        try:
            signal.signal(signal.SIGWINCH, handle_resize)
        except:
            pass
        
        draw_header()
        draw_divider()
        print_step("Initializing boot sequence...", 'wait')
        time.sleep(0.2)
        print_step("Checking for updates...", 'wait')
        time.sleep(0.2)
        print_step("Downloading from GitHub...", 'wait')
        time.sleep(0.2)
        
        files = download_repo()
        
        if files is None:
            print_step("Continuing with local files", 'warn')
        
        sync_files(files)
        finish()
        
    except KeyboardInterrupt:
        print(f"\n{red('[!] Interrupted by user')}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{red('[!] Fatal error:')} {str(e)}")
        if DEBUG_MODE:
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
