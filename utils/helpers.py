import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)
        
def log_message(message):
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
