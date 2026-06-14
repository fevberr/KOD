import os
from datetime import datetime

def h1():
    os.system('clear' if os.name == 'posix' else 'cls')

def h2(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None

def h3(path, content):
    with open(path, 'w') as f:
        f.write(content)
        
def h4(message):
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
