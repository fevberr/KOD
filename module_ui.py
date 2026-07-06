from config import host, port, device, system, ping
from display.banner import b1
from display.panels import p1
import os
import time
import importlib.util

def load_module(module_path):
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def show_module(module_name, options=None, current_options=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    b1()
    i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}ms\ndevice:   {device}\nsystem:    {system}"
    p1(f"23 KOD :: [{module_name}]", i1, "READY")
    
    if current_options:
        print("\n[+] Current Options:")
        for key, value in current_options.items():
            print(f"    {key}   = {value}")
    
    if options:
        print("\n[+] Available Options:")
        for key, value in options.items():
            default = value.get('default', '')
            desc = value.get('description', '')
            print(f"    {key}   = {default}  ({desc})")
    
    print("\n[+] Menu:")
    print("    (1) Run")
    if options:
        print("    (2) Set options")
    print("    (3) Back")
    print("    (0) Exit")
    print("\n------------------------------")
    return input("Select > ").strip()

def run_module(module_path, options=None):
    try:
        module = load_module(module_path)
        if hasattr(module, 'run'):
            if options:
                return module.run(options)
            else:
                return module.run()
        else:
            return "[!] No run() function"
    except Exception as e:
        return f"[!] Error: {e}"
