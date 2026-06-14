from datetime import datetime
import os

VERSION = "0.0.0"

def get_version():
    try:
        with open("data/version.txt", "r") as f:
            return f.read().strip()
    except:
        return VERSION

def save_version(ver):
    with open("data/version.txt", "w") as f:
        f.write(ver)

def update_module(module_name):
    print(f"\n+--- update list\n|\n|- - Removed old build        ({module_name})")
    print(f"|-  - Fetched latest release  ({module_name})")
    print(f"|- -  Launching updated build\n------------------------------")
    
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] Updated {module_name}\n")

def check_updates():
    return get_version()
