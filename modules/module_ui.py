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

def show_module(module_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    b1()
    i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}ms\ndevice:   {device}\nsystem:    {system}"
    p1(f"23 KOD :: [{module_name}]", i1, "READY")
    print("\n[+] Menu:")
    print("    (1) Run")
    print("    (2) Back")
    print("    (0) Exit")
    print("\n------------------------------")
    return input("Select > ").strip()

def run_module(module_path):
    try:
        module = load_module(module_path)
        if hasattr(module, 'run'):
            return module.run()
        else:
            return "[!] No run() function"
    except Exception as e:
        return f"[!] Error: {e}"
