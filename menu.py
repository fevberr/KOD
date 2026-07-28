from config import host, port, device, system, ping
import os
import sys
import time
import importlib.util
import random
import shutil
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

def c1(t): return f"\033[92m{t}\033[0m"
def c2(t): return f"\033[91m{t}\033[0m"
def c3(t): return f"\033[96m{t}\033[0m"
def c4(t): return f"\033[93m{t}\033[0m"
def c5(t): return f"\033[97m{t}\033[0m"
def c6(t): return f"\033[90m{t}\033[0m"
def c7(t): return f"\033[94m{t}\033[0m"
def c8(t): return f"\033[95m{t}\033[0m"

def a6(module_name, options=None, current_options=None):
    reload_colors()
    a2()
    a5()
    
    try:
        from display.banner import a3 as b1
        b1()
    except:
        print(c3("+--- 23 KOD"))
    
    w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    
    print(f"\n{c3('┌─')} {c4('Module:')} {c5(module_name)}")
    print(f"{c3('├─')} {c4('Host:')} {c5(host)}")
    print(f"{c3('├─')} {c4('Port:')} {c5(port)}")
    print(f"{c3('├─')} {c4('Ping:')} {c1(str(ping) + 'ms')}")
    print(f"{c3('├─')} {c4('Device:')} {c8(device)}")
    print(f"{c3('└─')} {c4('System:')} {c8(system)}")
    print()
    
    if current_options:
        print(f"{c6('┌' + '─' * min(w-4, 50) + '┐')}")
        for key, value in current_options.items():
            print(f"{c6('│')} {c3(key)}: {c5(value)}")
        print(f"{c6('└' + '─' * min(w-4, 50) + '┘')}")
        print()
    
    if options:
        print(f"{c6('┌' + '─' * min(w-4, 50) + '┐')}")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            print(f"{c6('│')} {c4(f'{i:2}.')} {c3(key)} {c6('[')}{c4(current)}{c6(']')}")
        print(f"{c6('└' + '─' * min(w-4, 50) + '┘')}")
        print()
    
    print(f"{c6('┌' + '─' * min(w-4, 50) + '┐')}")
    print(f"{c6('│')} {c1('[1] Run')}  {c4('[2] Opt')}  {c7('[3] Back')}  {c2('[0] Exit')}{' ' * (min(w-4, 50) - 27)}{c6('│')}")
    print(f"{c6('└' + '─' * min(w-4, 50) + '┘')}")
    print()
    
    return input(f"{c1('>')} ").strip()

def a7(module_path, options=None):
    reload_colors()
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
            a3(f"\n{c3('┌─ Output ')}{c3('─' * min(w-15, 40))}", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    a3(f"{c3('│')} {c1('✓')} {c5(line[3:])}", 0.002)
                elif line.startswith('[!]'):
                    a3(f"{c3('│')} {c2('✗')} {c5(line[3:])}", 0.002)
                elif line.startswith('[*]'):
                    a3(f"{c3('│')} {c7('●')} {c5(line[3:])}", 0.002)
                elif line.startswith('[#]'):
                    a3(f"{c3('│')} {c4('◆')} {c5(line[3:])}", 0.002)
                elif line.startswith('[~]'):
                    a3(f"{c3('│')} {c8('〜')} {c5(line[3:])}", 0.002)
                else:
                    a3(f"{c3('│')} {c6(line)}", 0.002)
            
            a3(f"{c3('└' + '─' * min(w-4, 50))}", 0.002)
            a3(f"\n{c1('[✓]')} {c5(random.choice(['SYSTEM', 'OK', 'DONE', 'COMPLETE', 'SUCCESS']))}")
            
            input(f"\n{c1('>')} ")
            return result
        else:
            a3(f"\n{c2('[!] No run() function')}")
            input(f"\n{c1('>')} ")
            return None
    except Exception as e:
        a3(f"\n{c2('[!]')} {c5(str(e))}")
        input(f"\n{c1('>')} ")
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
        return f"{c2('[!]')} No run() function"
    except Exception as e:
        return f"{c2('[!]')} Error: {e}"
