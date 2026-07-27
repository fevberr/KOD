from config import host, port, device, system, ping
import os
import sys
import time
import importlib.util
import random
import shutil
from utils.colors import green, red, cyan, yellow, white, gray, blue, magenta, dim, bold, reload_colors, teal, gold, lime, orange, purple, pink, hot_pink, lavender, mint, peach, coral, sky_blue, neon_green, neon_pink, neon_blue, neon_purple, sunset, ocean, forest, rose, color_settings_menu

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

def a6(module_name, options=None, current_options=None):
    reload_colors()
    a2()
    a5()
    
    try:
        from display.banner import a3 as b1
        b1()
    except:
        print(cyan("+--- 23 KOD"))
    
    w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    
    print(f"\n{cyan('┌─')} {yellow('Module:')} {white(module_name)}")
    print(f"{cyan('├─')} {yellow('Host:')} {white(host)}")
    print(f"{cyan('├─')} {yellow('Port:')} {white(port)}")
    print(f"{cyan('├─')} {yellow('Ping:')} {lime(str(ping) + 'ms')}")
    print(f"{cyan('├─')} {yellow('Device:')} {magenta(device)}")
    print(f"{cyan('└─')} {yellow('System:')} {magenta(system)}")
    print()
    
    if current_options:
        print(f"{gray('┌' + '─' * min(w-4, 50) + '┐')}")
        for key, value in current_options.items():
            print(f"{gray('│')} {cyan(key)}: {white(value)}")
        print(f"{gray('└' + '─' * min(w-4, 50) + '┘')}")
        print()
    
    if options:
        print(f"{gray('┌' + '─' * min(w-4, 50) + '┐')}")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            print(f"{gray('│')} {yellow(f'{i:2}.')} {cyan(key)} {gray('[')}{gold(current)}{gray(']')}")
        print(f"{gray('└' + '─' * min(w-4, 50) + '┘')}")
        print()
    
    print(f"{gray('┌' + '─' * min(w-4, 50) + '┐')}")
    print(f"{gray('│')} {green('[1] Run')}  {yellow('[2] Opt')}  {blue('[3] Back')}  {red('[0] Exit')}{' ' * (min(w-4, 50) - 27)}{gray('│')}")
    print(f"{gray('└' + '─' * min(w-4, 50) + '┘')}")
    print()
    
    return input(f"{green('>')} ").strip()

def a7(module_path, options=None):
    reload_colors()
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
            a3(f"\n{cyan('┌─ Output ')}{cyan('─' * min(w-15, 40))}", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    a3(f"{cyan('│')} {lime('✓')} {white(line[3:])}", 0.002)
                elif line.startswith('[!]'):
                    a3(f"{cyan('│')} {red('✗')} {white(line[3:])}", 0.002)
                elif line.startswith('[*]'):
                    a3(f"{cyan('│')} {blue('●')} {white(line[3:])}", 0.002)
                elif line.startswith('[#]'):
                    a3(f"{cyan('│')} {gold('◆')} {white(line[3:])}", 0.002)
                elif line.startswith('[~]'):
                    a3(f"{cyan('│')} {purple('〜')} {white(line[3:])}", 0.002)
                else:
                    a3(f"{cyan('│')} {gray(line)}", 0.002)
            
            a3(f"{cyan('└' + '─' * min(w-4, 50))}", 0.002)
            a3(f"\n{lime('[✓]')} {white(random.choice(['SYSTEM', 'OK', 'DONE', 'COMPLETE', 'SUCCESS']))}")
            
            input(f"\n{green('>')} ")
            return result
        else:
            a3(f"\n{red('[!] No run() function')}")
            input(f"\n{green('>')} ")
            return None
    except Exception as e:
        a3(f"\n{red('[!]')} {white(str(e))}")
        input(f"\n{green('>')} ")
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
        return f"{red('[!]')} No run() function"
    except Exception as e:
        return f"{red('[!]')} Error: {e}"
