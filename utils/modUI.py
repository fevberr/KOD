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
        print("╔═══ 23 KOD")
    
    w = min(term_w, 80)
    
    if w < 30:
        print(f"\n{a10(c1.get('secondary', '#ff6bff'))}╔═══ Module{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(module_name, 15)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('highlight', '#ffffff'))}H: {a11(host, 10)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('highlight', '#ffffff'))}P: {port}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('primary', '#00ffcc'))}Pi: {ping}ms{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('tab', '#ff44ff'))}D: {a11(device, 8)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('tab', '#ff44ff'))}S: {a11(system, 8)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}╚═══{rs}")
        print()
    elif w < 50:
        print(f"\n{a10(c1.get('secondary', '#ff6bff'))}╔═══ Module{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Module:{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(module_name, 20)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Host:{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(host, 15)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Port:{rs} {a10(c1.get('highlight', '#ffffff'))}{port}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Ping:{rs} {a10(c1.get('primary', '#00ffcc'))}{ping}ms{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Device:{rs} {a10(c1.get('tab', '#ff44ff'))}{a11(device, 12)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}System:{rs} {a10(c1.get('tab', '#ff44ff'))}{a11(system, 12)}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}╚═══{rs}")
        print()
    else:
        print(f"\n{a10(c1.get('secondary', '#ff6bff'))}╔═══ Module{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Module:{rs} {a10(c1.get('highlight', '#ffffff'))}{module_name}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Host:{rs} {a10(c1.get('highlight', '#ffffff'))}{host}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Port:{rs} {a10(c1.get('highlight', '#ffffff'))}{port}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Ping:{rs} {a10(c1.get('primary', '#00ffcc'))}{ping}ms{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}Device:{rs} {a10(c1.get('tab', '#ff44ff'))}{device}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}System:{rs} {a10(c1.get('tab', '#ff44ff'))}{system}{rs}")
        print(f"{a10(c1.get('secondary', '#ff6bff'))}╚═══{rs}")
        print()
    
    if current_options:
        bw = min(w-4, 40)
        print(f"{a10(c1.get('dim', '#888888'))}╔═══ Current{rs}")
        for key, value in current_options.items():
            if value is None:
                value = ""
            print(f"{a10(c1.get('dim', '#888888'))}║{rs} {a10(c1.get('secondary', '#ff6bff'))}{a11(key, 10)}{rs}: {a10(c1.get('highlight', '#ffffff'))}{a11(str(value), 15)}{rs}")
        print(f"{a10(c1.get('dim', '#888888'))}╚═══{rs}")
        print()
    
    if options:
        bw = min(w-4, 40)
        print(f"{a10(c1.get('dim', '#888888'))}╔═══ Options{rs}")
        opt_list = list(options.keys())
        for i, key in enumerate(opt_list, 1):
            default = options[key].get('default', '')
            current = current_options.get(key, default) if current_options else default
            if current is None:
                current = ""
            print(f"{a10(c1.get('dim', '#888888'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}{i:2}.{rs} {a10(c1.get('secondary', '#ff6bff'))}{a11(key, 12)}{rs} [{a10(c1.get('warning', '#ffaa00'))}{a11(str(current), 10)}{rs}]")
        print(f"{a10(c1.get('dim', '#888888'))}╚═══{rs}")
        print()
    
    bw = min(w-4, 40)
    print(f"{a10(c1.get('dim', '#888888'))}╔═══{rs}")
    if w < 30:
        print(f"{a10(c1.get('dim', '#888888'))}║{rs} {a10(c1.get('primary', '#00ffcc'))}1R{rs} {a10(c1.get('warning', '#ffaa00'))}2O{rs} {a10(c1.get('info', '#0088ff'))}3B{rs} {a10(c1.get('error', '#ff0044'))}0E{rs}")
    elif w < 50:
        print(f"{a10(c1.get('dim', '#888888'))}║{rs} {a10(c1.get('primary', '#00ffcc'))}[1]{rs} Run  {a10(c1.get('warning', '#ffaa00'))}[2]{rs} Opt  {a10(c1.get('info', '#0088ff'))}[3]{rs} Back  {a10(c1.get('error', '#ff0044'))}[0]{rs} Exit")
    else:
        print(f"{a10(c1.get('dim', '#888888'))}║{rs} {a10(c1.get('primary', '#00ffcc'))}[1]{rs} Run  {a10(c1.get('warning', '#ffaa00'))}[2]{rs} Options  {a10(c1.get('info', '#0088ff'))}[3]{rs} Back  {a10(c1.get('error', '#ff0044'))}[0]{rs} Exit")
    print(f"{a10(c1.get('dim', '#888888'))}╚═══{rs}")
    print()
    
    return input(f"{a10(c1.get('primary', '#00ffcc'))}> {rs}").strip()

def a7(module_path, options=None):
    c1 = a9()
    rs = '\033[0m'
    term_w = shutil.get_terminal_size().columns if hasattr(shutil, 'get_terminal_size') else 80
    w = min(term_w, 80)
    
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            bw = min(w-4, 40)
            a3(f"\n{a10(c1.get('secondary', '#ff6bff'))}╔═══ Output{rs}", 0.002)
            
            if options:
                result = module.run(options)
            else:
                result = module.run()
            
            for line in result.split('\n'):
                if line.startswith('[+]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('primary', '#00ffcc'))}+{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(line[3:], w-6)}{rs}", 0.002)
                elif line.startswith('[!]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('error', '#ff0044'))}!{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(line[3:], w-6)}{rs}", 0.002)
                elif line.startswith('[*]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('info', '#0088ff'))}*{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(line[3:], w-6)}{rs}", 0.002)
                elif line.startswith('[#]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('warning', '#ffaa00'))}#{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(line[3:], w-6)}{rs}", 0.002)
                elif line.startswith('[~]'):
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('tab', '#ff44ff'))}~{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(line[3:], w-6)}{rs}", 0.002)
                else:
                    a3(f"{a10(c1.get('secondary', '#ff6bff'))}║{rs} {a10(c1.get('dim', '#888888'))}{a11(line, w-4)}{rs}", 0.002)
            
            a3(f"{a10(c1.get('secondary', '#ff6bff'))}╚═══{rs}", 0.002)
            a3(f"\n{a10(c1.get('primary', '#00ffcc'))}[OK]{rs} {a10(c1.get('highlight', '#ffffff'))}{random.choice(['SYSTEM', 'OK', 'DONE', 'SUCCESS', 'COMPLETE'])}{rs}")
            
            input(f"\n{a10(c1.get('primary', '#00ffcc'))}> {rs}")
            return result
        else:
            a3(f"\n{a10(c1.get('error', '#ff0044'))}[!] No run() function{rs}")
            input(f"\n{a10(c1.get('primary', '#00ffcc'))}> {rs}")
            return None
    except Exception as e:
        a3(f"\n{a10(c1.get('error', '#ff0044'))}[!]{rs} {a10(c1.get('highlight', '#ffffff'))}{a11(str(e), w-4)}{rs}")
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
