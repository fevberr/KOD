from updater import update_module
from utils.loader import load_module
from spinner import spinner
import os
import sys

def get_modules():
    modules = []
    if os.path.exists("modules"):
        for file in os.listdir("modules"):
            if file.endswith((".py", ".lua")) and file != "__init__.py":
                modules.append(file)
    return modules

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        from display.banner import show_banner
        from display.panels import draw_panel
        from config import host, port, device, system, ping
        show_banner()
        info = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
        draw_panel("23 KOD", info, "READY")
        
        modules = get_modules()
        print("\n* menu\n|")
        for i, mod in enumerate(modules, 1):
            print(f"| > {i}  | {mod}")
        print("|\n|- 0  Exit")
        print("------------------------")
        
        choice = input("Select option > ").strip()
        
        if choice == "0":
            print("Exiting...")
            break
        
        if not choice.isdigit():
            print("Invalid option")
            input("\nPress Enter to continue...")
            continue
        
        idx = int(choice) - 1
        if 0 <= idx < len(modules):
            module_name = modules[idx]
            with spinner(f"Loading {module_name}"):
                update_module(module_name)
                load_module(f"modules/{module_name}")
            print(f"\nModule {module_name} finished.")
            input("Press Enter to continue...")
        else:
            print("Invalid option")
            input("\nPress Enter to continue...")
