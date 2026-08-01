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

def a11(s, w):
    if s is None:
        return ""
    if len(s) > w:
        return s[:w-1] + "…"
    return s

def get_current_path():
    return os.getcwd()

def truncate_path(s, w):
    if len(s) > w:
        return s[:w-1] + "…"
    return s

def a6(module_name, options=None, current_options=None):
    a2()
    a5()
    c1 = a9()
    rs = '\033[0m'
    term_w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    
    try:
        from display.banner import a3 as b1
        b1()
    except:
        pass
    
    w = min(term_w, 80)
    path = get_current_path()
    path_display = truncate_path(path, w - 20)
    
    g = a10(c1.get('primary', '#7b2fbe'))
    r = a10(c1.get('error', '#e74c3c'))
    c = a10(c1.get('secondary', '#9b59b6'))
    y = a10(c1.get('warning', '#f1c40f'))
    wc = a10(c1.get('highlight', '#ffffff'))
    gr = a10(c1.get('dim', '#7f8c8d'))
    b = a10(c1.get('info', '#3498db'))
    m = a10(c1.get('tab', '#8e44ad'))
    
    # Header with KOD style
    print(f"\n{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
    print(f"{g}║{rs} {c}Module:{rs} {wc}{module_name}{rs}")
    print(f"{g}║{rs} {c}Host:{rs} {wc}{host}{rs}")
    print(f"{g}║{rs} {c}Port:{rs} {wc}{port}{rs}")
    print(f"{g}║{rs} {c}Ping:{rs} {y}{ping}ms{rs}")
    print(f"{g}║{rs} {c}Device:{rs} {m}{device}{rs}")
    print(f"{g}║{rs} {c}System:{rs} {m}{system}{rs}")
    print(f"{g}╚═══{rs}")
    
    if current_options:
        bw = min(w-4, 40)
        print(f"\n{g}╔═══ Current{rs}")
        for key, value in current_options.items():
            if value is None:
                value = ""
            print(f"{g}║{rs} {c}{a11(key, 10)}{rs}: {wc}{a11(str(value), 15)}{rs}")
        print(f"{g}╚═══{rs}")
    
    if options:
        bw = min(w-4, 40)
        print(f"\n{g}╔═══ Options{rs}")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            if current is None:
                current = ""
            print(f"{g}║{rs} {y}{i:2}.{rs} {c}{a11(key, 12)}{rs} {gr}[{wc}{a11(str(current), 10)}{rs}{gr}]{rs}")
        print(f"{g}╚═══{rs}")
    
    # KOD prompt style
    print(f"\n{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
    print(f"{g}║{rs} {c}[1]{rs} Run  {c}[2]{rs} Opt  {c}[3]{rs} Back  {c}[0]{rs} Exit{rs}")
    print(f"{g}╚═══{rs}")
    print()
    
    print(f"{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
    print(f"{g}╚══ ▶{rs} ", end="")
    
    return input().strip()

def a7(module_path, options=None):
    c1 = a9()
    rs = '\033[0m'
    term_w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    w = min(term_w, 80)
    path = get_current_path()
    path_display = truncate_path(path, w - 20)
    
    g = a10(c1.get('primary', '#7b2fbe'))
    r = a10(c1.get('error', '#e74c3c'))
    c = a10(c1.get('secondary', '#9b59b6'))
    y = a10(c1.get('warning', '#f1c40f'))
    wc = a10(c1.get('highlight', '#ffffff'))
    gr = a10(c1.get('dim', '#7f8c8d'))
    b = a10(c1.get('info', '#3498db'))
    m = a10(c1.get('tab', '#8e44ad'))
    
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            print(f"\n{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
            print(f"{g}║{rs} {c}Output:{rs}")
            print(f"{g}╠═══{rs}")
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    print(f"{g}║{rs} {g}+{rs} {wc}{a11(line[3:], w-6)}{rs}")
                elif line.startswith('[!]'):
                    print(f"{g}║{rs} {r}!{rs} {wc}{a11(line[3:], w-6)}{rs}")
                elif line.startswith('[*]'):
                    print(f"{g}║{rs} {b}*{rs} {wc}{a11(line[3:], w-6)}{rs}")
                elif line.startswith('[#]'):
                    print(f"{g}║{rs} {y}#{rs} {wc}{a11(line[3:], w-6)}{rs}")
                elif line.startswith('[~]'):
                    print(f"{g}║{rs} {m}~{rs} {wc}{a11(line[3:], w-6)}{rs}")
                else:
                    print(f"{g}║{rs} {gr}{a11(line, w-4)}{rs}")
            
            print(f"{g}╚═══{rs}")
            print(f"\n{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
            print(f"{g}║{rs} {g}[OK]{rs} {wc}{random.choice(['SYSTEM', 'OK', 'DONE', 'SUCCESS', 'COMPLETE'])}{rs}")
            print(f"{g}╚═══{rs}")
            print()
            
            print(f"{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
            print(f"{g}╚══ ▶{rs} ", end="")
            input()
            return result
        else:
            print(f"\n{r}[!] No run() function{rs}")
            print(f"{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
            print(f"{g}╚══ ▶{rs} ", end="")
            input()
            return None
    except Exception as e:
        print(f"\n{r}[!] {str(e)}{rs}")
        print(f"{g}╔══[ {wc}KOD by fevber{rs}{g} ]══ {wc}{path_display}{rs}{g} ══╗{rs}")
        print(f"{g}╚══ ▶{rs} ", end="")
        input()
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
