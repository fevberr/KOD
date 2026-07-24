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
    
