import subprocess
import os

def l1(m1):
    if m1.endswith('.py'):
        with open(m1, 'r') as f:
            exec(f.read())
    elif m1.endswith('.lua'):
        try:
            r1 = subprocess.run(['lua', m1], capture_output=True, text=True)
            print(r1.stdout)
            if r1.stderr:
                print(f"Lua error: {r1.stderr}")
        except FileNotFoundError:
            print("Lua interpreter not found")
    else:
        print(f"Unknown module type: {m1}")
