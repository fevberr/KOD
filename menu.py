from updater import update_module
from utils.loader import load_module
from spinner import spinner
import os

def g1():
    modules = []
    if os.path.exists("modules"):
        for file in os.listdir("modules"):
            if file.endswith((".py", ".lua")) and file != "__init__.py":
                modules.append(file)
    return modules

def g2():
    modules = g1()
    print("\n* menu\n|")
    for i, mod in enumerate(modules, 1):
        print(f"| > {i}  | {mod}")
    print("|\n|- 0  Exit")
    print("------------------------")
    return modules

def menu():
    while True:
        modules = g2()
        choice = input("Select option > ").strip()
        
        if choice == "0":
            print("Exiting...")
            break
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(modules):
                module_name = modules[idx]
                with spinner(f"Loading {module_name}"):
                    update_module(module_name)
                    load_module(f"modules/{module_name}")
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input")
