from config import host, port, device, system, ping
import os
import sys
import time
import importlib.util
import random
import shutil
import json
from utils.colors import reload_colors, color_settings_menu

def a1(path):
    spec = importlib.util.spec_from_file_location("module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def a2():
    os.system('cls' if os.name == 'nt' else 'clear')

def a3(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def a4(text, delay=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def a5():
    chars = "01!@#$%^&*()_+{}|:<>?~"
    width = min(shutil.get_terminal_size().columns, 80)
    for _ in range(2):
        line = ''.join(random.choice(chars) for _ in range(min(width, 50)))
        sys.stdout.write(f"\r\033[2m{line}\033[0m")
        sys.stdout.flush()
        time.sleep(0.015)
    print("\r" + " " * min(width, 50), end="")
    print("\r", end="")

def a9():
    try:
        with open("cache/CSET.json", 'r') as f:
            return json.load(f)
    except:
        return {}

def a10(c):
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

def a6(module_name, options=None, current_options=None):
    reload_colors()
    a2()
    a5()
    c1 = a9()
    
    try:
        from display.banner import a3 as b1
        b1()
    except:
        print("+--- 23 KOD")
    
    return input("> ").strip()

def a7(module_path, options=None):
    reload_colors()
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            a3("\n┌─ Output ─────────────────────────────────────────────────────┐", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    a3("│ ✓ " + line[3:], 0.002)
                elif line.startswith('[!]'):
                    a3("│ ✗ " + line[3:], 0.002)
                elif line.startswith('[*]'):
                    a3("│ ● " + line[3:], 0.002)
                elif line.startswith('[#]'):
                    a3("│ ◆ " + line[3:], 0.002)
                elif line.startswith('[~]'):
                    a3("│ 〜 " + line[3:], 0.002)
                else:
                    a3("│ " + line, 0.002)
            
            a3("└──────────────────────────────────────────────────────────────────┘", 0.002)
            a3("\n[✓] " + random.choice(['SYSTEM', 'OK', 'DONE', 'COMPLETE', 'SUCCESS']))
            
            input("\n> ")
            return result
        else:
            a3("\n[!] No run() function")
            input("\n> ")
            return None
    except Exception as e:
        a3("\n[!] " + str(e))
        input("\n> ")
        return None

def a8(module_path, options=None):
    reload_colors()
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            if options:
                return module.run(options)
            else:
                return module.run()
        return "[!] No run() function"
    except Exception as e:
        return "[!] Error: " + str(e)
