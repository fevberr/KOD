from config import host, port, device, system, ping
import os
import sys
import time
import importlib.util
import random
import shutil
import json
from utils.colors import hex_to_ansi, is_hex_color

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
    if c and isinstance(c, str):
        return hex_to_ansi(c)
    return ''

def a6(module_name, options=None, current_options=None):
    a2()
    a5()
    c1 = a9()
    rs = '\033[0m'
    
    try:
        from display.banner import a3 as b1
        b1()
    except:
        print("+--- 23 KOD")
    
    w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    
    print(f"\n{a10(c1.get('secondary', '#ff6bff'))}┌─{rs} {a10(c1.get('warning', '#ffaa00'))}Module:{rs} {a10(c1.get('highlight', '#ffffff'))}{module_name}{rs}")
    print(f"{a10(c1.get('secondary', '#ff6bff'))}├─{rs} {a10(c1.get('warning', '#ffaa00'))}Host:{rs} {a10(c1.get('highlight', '#ffffff'))}{host}{rs}")
    print(f"{a10(c1.get('secondary', '#ff6bff'))}├─{rs} {a10(c1.get('warning', '#ffaa00'))}Port:{rs} {a10(c1.get('highlight', '#ffffff'))}{port}{rs}")
    print(f"{a10(c1.get('secondary', '#ff6bff'))}├─{rs} {a10(c1.get('warning', '#ffaa00'))}Ping:{rs} {a10(c1.get('primary', '#00ffcc'))}{ping}ms{rs}")
    print(f"{a10(c1.get('secondary', '#ff6bff'))}├─{rs} {a10(c1.get('warning', '#ffaa00'))}Device:{rs} {a10(c1.get('tab', '#ff44ff'))}{device}{rs}")
    print(f"{a10(c1.get('secondary', '#ff6bff'))}└─{rs} {a10(c1.get('warning', '#ffaa00'))}System:{rs} {a10(c1.get('tab', '#ff44ff'))}{system}{rs}")
    print()
    
    if current_options:
        print(f"{a10(c1.get('dim', '#888888'))}┌{'─' * min(w-4, 50)}┐{rs}")
        for key, value in current_options.items():
            print(f"{a10(c1.get('dim', '#888888'))}│{rs} {a10(c1.get('secondary', '#ff6bff'))}{key}{rs}: {a10(c1.get('highlight', '#ffffff'))}{value}{rs}")
        print(f"{a10(c1.get('dim', '#888888'))}└{'─' * min(w-4, 50)}┘{rs}")
        print()
    
    if options:
        print(f"{a10(c1.get('dim', '#888888'))}┌{'─' * min(w-4, 50)}┐{rs}")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            print(f"{a10(c1.get('dim', '#888888'))}│{rs} {a10(c1.get('warning', '#ffaa00'))}{f'{i:2}.{rs}'} {a10(c1.get('secondary', '#ff6bff'))}{key}{rs} {a10(c1.get('dim', '#888888'))}[{rs}{a10(c1.get('warning', '#ffaa00'))}{current}{rs}{a10(c1.get('dim', '#888888'))}]{rs}")
        print(f"{a10(c1.get('dim', '#888888'))}└{'─' * min(w-4, 50)}┘{rs}")
        print()
    
    print(f"{a10(c1.get('dim', '#888888'))}┌{'─' * min(w-4, 50)}┐{rs}")
    print(f"{a10(c1.get('dim', '#888888'))}│{rs} {a10(c1.get('primary', '#00ffcc'))}[1]{rs} Run  {a10(c1.get('warning', '#ffaa00'))}[2]{rs} Opt  {a10(c1.get('info', '#0088ff'))}[3]{rs} Back  {a10(c1.get('error', '#ff0044'))}[0]{rs} Exit{' ' * (min(w-4, 50) - 27)}{a10(c1.get('dim', '#888888'))}│{rs}")
    print(f"{a10(c1.get('dim', '#888888'))}└{'─' * min(w-4, 50)}┘{rs}")
    print()
    
    return input(f"{a10(c1.get('primary', '#00ffcc'))}> {rs}").strip()

def a7(module_path, options=None):
    c1 = a9()
    rs = '\033[0m'
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
            a3(f"\n{a10(c1.get('secondary', '#ff6bff'))}┌─ Output {rs}{a10(c1.get('secondary', '#ff6bff'))}{'─' * min(w-15, 40)}{rs}", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}│{rs} {a10(c1.get('primary', '#00ffcc'))}✓{rs} {a10(c1.get('highlight', '#ffffff'))}{line[3:]}{rs}", 0.002)
                elif line.startswith('[!]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}│{rs} {a10(c1.get('error', '#ff0044'))}✗{rs} {a10(c1.get('highlight', '#ffffff'))}{line[3:]}{rs}", 0.002)
                elif line.startswith('[*]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}│{rs} {a10(c1.get('info', '#0088ff'))}●{rs} {a10(c1.get('highlight', '#ffffff'))}{line[3:]}{rs}", 0.002)
                elif line.startswith('[#]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}│{rs} {a10(c1.get('warning', '#ffaa00'))}◆{rs} {a10(c1.get('highlight', '#ffffff'))}{line[3:]}{rs}", 0.002)
                elif line.startswith('[~]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}│{rs} {a10(c1.get('tab', '#ff44ff'))}〜{rs} {a10(c1.get('highlight', '#ffffff'))}{line[3:]}{rs}", 0.002)
                else:
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}│{rs} {a10(c1.get('dim', '#888888'))}{line}{rs}", 0.002)
            
            a3(f"{a10(c1.get('secondary', '#ff6bff'))}└{'─' * min(w-4, 50)}{rs}", 0.002)
            a3(f"\n{a10(c1.get('primary', '#00ffcc'))}[✓]{rs} {a10(c1.get('highlight', '#ffffff'))}{random.choice(['SYSTEM', 'OK', 'DONE', 'COMPLETE', 'SUCCESS'])}{rs}")
            
            input(f"\n{a10(c1.get('primary', '#00ffcc'))}> {rs}")
            return result
        else:
            a3(f"\n{a10(c1.get('error', '#ff0044'))}[!] No run() function{rs}")
            input(f"\n{a10(c1.get('primary', '#00ffcc'))}> {rs}")
            return None
    except Exception as e:
        a3(f"\n{a10(c1.get('error', '#ff0044'))}[!]{rs} {a10(c1.get('highlight', '#ffffff'))}{str(e)}{rs}")
        input(f"\n{a10(c1.get('primary', '#00ffcc'))}> {rs}")
        return None

def a8(module_path, options=None):
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
