import os
from datetime import datetime

def c1():
    os.system('cls' if os.name == 'nt' else 'clear')

def r1(p1):
    try:
        with open(p1, 'r') as f:
            return f.read()
    except:
        return None

def w1(p1, c1):
    with open(p1, 'w') as f:
        f.write(c1)
        
def l2(m1):
    with open("data/logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {m1}\n")
