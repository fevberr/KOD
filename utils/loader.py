import subprocess
import os

def l1(module_path):
    if module_path.endswith('.py'):
        with open(module_path, 'r') as f:
            exec(f.read())
    elif module_path.endswith('.lua'):
        try:
            result = subprocess.run(['lua', module_path], capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print(f"Lua error: {result.stderr}")
        except FileNotFoundError:
            print("Lua interpreter not found")
    else:
        print(f"Unknown module type: {module_path}")
