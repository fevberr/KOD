from config import host, port, device, system, ping
import os
import sys
import importlib.util

def a1(module_path):
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def a2(module_name, options=None, current_options=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"+--- 23 KOD :: [{module_name}]")
    print(f"| host:      {host}")
    print(f"| Port:        {port}")
    print(f"| Ping:     {ping}")
    print(f"| device:   {device}")
    print(f"| system:    {system}")
    print("|- Status: READY")
    print("------------------------------")
    
    if current_options:
        print("\n[+] Current:")
        for key, value in current_options.items():
            print(f"    {key}   = {value}")
    
    print("\n[+] Menu:")
    print("    (1) Run")
    if options:
        print("    (2) Set options")
    print("    (3) Back")
    print("    (0) Exit")
    print("\n------------------------------")
    return input("Select > ").strip()

def a3(module_path, options=None):
    try:
        module = a1(module_path)
        if hasattr(module, 'run'):
            if options:
                return module.run(options)
            else:
                return module.run()
        else:
            return "[!] No run() function"
    except Exception as e:
        return f"[!] Error: {e}"
