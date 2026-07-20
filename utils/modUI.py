from config import host, port, device, system, ping
import os
import sys
import time
import importlib.util
import random
import shutil

def get_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def truncate(text, max_len):
    if len(text) > max_len:
        return text[:max_len-3] + "..."
    return text

def a1(path):
    spec = importlib.util.spec_from_file_location("module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fast(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_rain(lines=2):
    chars = "01!@#$%^&*()_+{}|:<>?~"
    width = get_width()
    for _ in range(lines):
        line = ''.join(random.choice(chars) for _ in range(min(width, 50)))
        sys.stdout.write(f"\r\033[2m{line}\033[0m")
        sys.stdout.flush()
        time.sleep(0.015)
    print("\r" + " " * min(width, 50), end="")
    print("\r", end="")

def show_header(module_name):
    clear()
    matrix_rain(1)
    width = get_width()
    
    print(f"\n\033[96m┌─ \033[93mModule:\033[0m \033[97m{module_name}\033[0m")
    print(f"\033[96m├─ \033[93mHost:\033[0m \033[97m{host}\033[0m")
    print(f"\033[96m├─ \033[93mPort:\033[0m \033[97m{port}\033[0m")
    print(f"\033[96m├─ \033[93mPing:\033[0m \033[97m{ping}ms\033[0m")
    print(f"\033[96m├─ \033[93mDevice:\033[0m \033[97m{device}\033[0m")
    print(f"\033[96m└─ \033[93mSystem:\033[0m \033[97m{system}\033[0m")
    print()

def a2(module_name, options=None, current_options=None):
    show_header(module_name)
    width = get_width()
    
    if current_options:
        print("\033[90m┌──────────────────────────────────────────────────────────────┐\033[0m")
        for key, value in current_options.items():
            display = truncate(f"{key}: {value}", width - 6)
            print(f"\033[90m│ \033[93m{display}\033[0m")
        print("\033[90m└──────────────────────────────────────────────────────────────┘\033[0m")
        print()
    
    if options:
        print("\033[90m┌──────────────────────────────────────────────────────────────┐\033[0m")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            display = truncate(f"{i}. {key} [{current}]", width - 6)
            print(f"\033[90m│ \033[96m{display}\033[0m")
        print("\033[90m└──────────────────────────────────────────────────────────────┘\033[0m")
        print()
    
    print("\033[90m┌──────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[90m│ \033[92m[1] Run\033[0m  \033[93m[2] Opt\033[0m  \033[94m[3] Back\033[0m  \033[91m[0] Exit\033[0m                   \033[90m│\033[0m")
    print("\033[90m└──────────────────────────────────────────────────────────────┘\033[0m")
    print()
    
    return input("\033[92m>\033[0m ").strip()

def a3(module_path, options=None):
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            fast("\n\033[96m┌─ Output ───────────────────────────────────────────────────┐\033[0m", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            width = get_width()
            for line in result.split('\n'):
                display = truncate(line, width - 6)
                if line.startswith('[+]'):
                    fast(f"\033[92m│ ✓ {display[3:]}\033[0m", 0.002)
                elif line.startswith('[!]'):
                    fast(f"\033[91m│ ✗ {display[3:]}\033[0m", 0.002)
                elif line.startswith('[*]'):
                    fast(f"\033[94m│ ● {display[3:]}\033[0m", 0.002)
                else:
                    fast(f"\033[90m│ {display}\033[0m", 0.002)
            
            fast("\033[96m└──────────────────────────────────────────────────────────────┘\033[0m", 0.002)
            input("\n\033[92m>\033[0m ")
            return result
        else:
            fast("\n\033[91m[!] No run() function\033[0m")
            input("\n\033[92m>\033[0m ")
            return None
    except Exception as e:
        fast(f"\n\033[91m[!] {e}\033[0m")
        input("\n\033[92m>\033[0m ")
        return None
