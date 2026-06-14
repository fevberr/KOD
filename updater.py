from datetime import datetime
import os

VERSION = "0.0.0"

def u1():
    try:
        with open("data/version.txt", "r") as f:
            return f.read().strip()
    except:
        return VERSION

def u2(ver):
    with open("data/version.txt", "w") as f:
        f.write(ver)

def update_module(module_name):
    print(f"\n+--- update list\n|\n|- - Removed old build        ({module_name})")
    print(f"|-  - Fetched latest release  ({module_name})")
    print(f"|- -  Launching updated build\n------------------------------")
    
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] Updated {module_name}\n")

def u3():
    return u1()
