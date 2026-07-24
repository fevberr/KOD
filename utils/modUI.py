from config import host, port, device, system, ping
import os
import sys
import time
import importlib.util
import random
import shutil

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
    a2()
    a5()
    
    try:
        from display.banner import b1
        b1()
    except:
        print("+--- 23 KOD")
    
    print(f"\n\033[96m┌─ \033[93mModule:\033[0m \033[97m{module_name}\033[0m")
    print(f"\033[96m├─ \033[93mHost:\033[0m \033[97m{host}\033[0m")
    print(f"\033[96m├─ \033[93mPort:\033[0m \033[97m{port}\033[0m")
    print(f"\033[96m├─ \033[93mPing:\033[0m \033[97m{ping}ms\033[0m")
    print(f"\033[96m├─ \033[93mDevice:\033[0m \033[97m{device}\033[0m")
    print(f"\033[96m└─ \033[93mSystem:\033[0m \033[97m{system}\033[0m")
    print()
    
    if current_options:
        print("\033[90m┌──────────────────────────────────────────────────────────────┐\033[0m")
        for key, value in current_options.items():
            print(f"\033[90m│ \033[93m{key}:\033[0m \033[97m{value}\033[0m")
        print("\033[90m└──────────────────────────────────────────────────────────────┘\033[0m")
        print()
    
    if options:
        print("\033[90m┌──────────────────────────────────────────────────────────────┐\033[0m")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            print(f"\033[90m│ \033[96m{i:2}.\033[0m \033[97m{key}\033[0m \033[90m[\033[93m{current}\033[90m]\033[0m")
        print("\033[90m└──────────────────────────────────────────────────────────────┘\033[0m")
        print()
    
    print("\033[90m┌──────────────────────────────────────────────────────────────┐\033[0m")
    print("\033[90m│ \033[92m[1] Run\033[0m  \033[93m[2] Opt\033[0m  \033[94m[3] Back\033[0m  \033[91m[0] Exit\033[0m                   \033[90m│\033[0m")
    print("\033[90m└──────────────────────────────────────────────────────────────┘\033[0m")
    print()
    
    return input("\033[92m>\033[0m ").strip()

def a7(module_path, options=None):
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            a3("\n\033[96m┌─ Output ───────────────────────────────────────────────────┐\033[0m", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    a3(f"\033[92m│ ✓ {line[3:]}\033[0m", 0.002)
                elif line.startswith('[!]'):
                    a3(f"\033[91m│ ✗ {line[3:]}\033[0m", 0.002)
                elif line.startswith('[*]'):
                    a3(f"\033[94m│ ● {line[3:]}\033[0m", 0.002)
                else:
                    a3(f"\033[90m│ {line}\033[0m", 0.002)
            
            a3("\033[96m└──────────────────────────────────────────────────────────────┘\033[0m", 0.002)
            a3(f"\n\033[92m[✓] {random.choice(['SYSTEM', 'OK', 'DONE', 'COMPLETE'])}\033[0m")
            
            input("\n\033[92m>\033[0m ")
            return result
        else:
            a3("\n\033[91m[!] No run() function\033[0m")
            input("\n\033[92m>\033[0m ")
            return None
    except Exception as e:
        a3(f"\n\033[91m[!] {e}\033[0m")
        input("\n\033[92m>\033[0m ")
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
        return f"[!] Error: {e}"
