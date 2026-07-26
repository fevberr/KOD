import os
import sys
import platform
import json
import time
import re

COLORS_FILE = "color_settings.json"

DEFAULT_COLORS = {
    "primary": "GREEN",
    "secondary": "CYAN",
    "success": "GREEN",
    "error": "RED",
    "warning": "YELLOW",
    "info": "BLUE",
    "highlight": "MAGENTA",
    "dim": "GRAY",
    "prompt": "GREEN",
    "border": "CYAN"
}

COLOR_CODES = {
    "BLACK": '\033[30m', "RED": '\033[31m', "GREEN": '\033[32m',
    "YELLOW": '\033[33m', "BLUE": '\033[34m', "MAGENTA": '\033[35m',
    "CYAN": '\033[36m', "WHITE": '\033[37m',
    "BRIGHT_RED": '\033[91m', "BRIGHT_GREEN": '\033[92m',
    "BRIGHT_YELLOW": '\033[93m', "BRIGHT_BLUE": '\033[94m',
    "BRIGHT_MAGENTA": '\033[95m', "BRIGHT_CYAN": '\033[96m',
    "BRIGHT_WHITE": '\033[97m', "GRAY": '\033[90m',
    "PURPLE": '\033[95m', "ORANGE": '\033[38;5;208m',
    "PINK": '\033[38;5;201m', "LIME": '\033[38;5;154m',
    "TEAL": '\033[38;5;37m', "GOLD": '\033[38;5;220m',
    "SILVER": '\033[38;5;250m', "BROWN": '\033[38;5;130m',
    "RESET": '\033[0m', "BOLD": '\033[1m', "DIM": '\033[2m'
}

ALL_COLORS = ["GREEN", "RED", "CYAN", "YELLOW", "BLUE", "MAGENTA", "GRAY", "WHITE", 
              "BLACK", "BRIGHT_GREEN", "BRIGHT_RED", "BRIGHT_CYAN", "BRIGHT_YELLOW",
              "BRIGHT_BLUE", "BRIGHT_MAGENTA", "BRIGHT_WHITE",
              "PURPLE", "ORANGE", "PINK", "LIME", "TEAL", "GOLD", "SILVER", "BROWN"]

SETTINGS_KEYS = ["primary", "secondary", "success", "error", "warning", "info", 
                 "highlight", "dim", "prompt", "border"]

LABELS = {
    "primary": "Primary", "secondary": "Secondary", "success": "Success",
    "error": "Error", "warning": "Warning", "info": "Info",
    "highlight": "Highlight", "dim": "Dim", "prompt": "Prompt", "border": "Border"
}

def a1():
    if not hasattr(sys.stdout, 'isatty') or not sys.stdout.isatty():
        return False
    if os.environ.get('NO_COLOR'):
        return False
    if os.environ.get('FORCE_COLOR'):
        return True
    term = os.environ.get('TERM', '')
    if term in ('dumb', 'linux'):
        return False
    if platform.system() == 'Windows':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                kernel32.SetConsoleMode(handle, mode.value | 0x0004)
                return True
            return False
        except:
            return False
    return term not in ('', 'dumb', 'linux')

def a2():
    class a3:
        RS = '\033[0m'; B = '\033[1m'; D = '\033[2m'
        BL = '\033[30m'; R = '\033[31m'; G = '\033[32m'
        Y = '\033[33m'; BLU = '\033[34m'; M = '\033[35m'
        C = '\033[36m'; W = '\033[37m'
        BR = '\033[91m'; BG = '\033[92m'; BY = '\033[93m'
        BB = '\033[94m'; BM = '\033[95m'; BC = '\033[96m'
        BW = '\033[97m'; GR = '\033[90m'
        P = '\033[95m'; O = '\033[38;5;208m'
        PI = '\033[38;5;201m'; L = '\033[38;5;154m'
        T = '\033[38;5;37m'; GO = '\033[38;5;220m'
        SI = '\033[38;5;250m'; BRO = '\033[38;5;130m'
    return a3

def a4():
    try:
        with open(COLORS_FILE, 'r') as f:
            return json.load(f)
    except:
        return DEFAULT_COLORS.copy()

def a5(settings):
    with open(COLORS_FILE, 'w') as f:
        json.dump(settings, f, indent=2)

def a6():
    settings = a4()
    codes = a2()
    if a1():
        color_map = {
            "GREEN": codes.BG, "RED": codes.BR, "CYAN": codes.BC,
            "YELLOW": codes.BY, "WHITE": codes.BW, "GRAY": codes.GR,
            "BLUE": codes.BB, "MAGENTA": codes.BM, "BLACK": codes.BL,
            "BRIGHT_RED": codes.BR, "BRIGHT_GREEN": codes.BG,
            "BRIGHT_YELLOW": codes.BY, "BRIGHT_BLUE": codes.BB,
            "BRIGHT_MAGENTA": codes.BM, "BRIGHT_CYAN": codes.BC,
            "BRIGHT_WHITE": codes.BW,
            "PURPLE": codes.P, "ORANGE": codes.O,
            "PINK": codes.PI, "LIME": codes.L,
            "TEAL": codes.T, "GOLD": codes.GO,
            "SILVER": codes.SI, "BROWN": codes.BRO
        }
    else:
        color_map = {k: '' for k in DEFAULT_COLORS.values()}
    
    return {
        'primary': color_map.get(settings.get('primary', 'GREEN'), ''),
        'secondary': color_map.get(settings.get('secondary', 'CYAN'), ''),
        'success': color_map.get(settings.get('success', 'GREEN'), ''),
        'error': color_map.get(settings.get('error', 'RED'), ''),
        'warning': color_map.get(settings.get('warning', 'YELLOW'), ''),
        'info': color_map.get(settings.get('info', 'BLUE'), ''),
        'highlight': color_map.get(settings.get('highlight', 'MAGENTA'), ''),
        'dim': color_map.get(settings.get('dim', 'GRAY'), ''),
        'prompt': color_map.get(settings.get('prompt', 'GREEN'), ''),
        'border': color_map.get(settings.get('border', 'CYAN'), ''),
        'reset': codes.RS if a1() else '',
        'bold': codes.B if a1() else '',
        'dim_text': codes.D if a1() else ''
    }

if a1():
    _c = a2()
    GREEN = _c.BG; RED = _c.BR; CYAN = _c.BC
    YELLOW = _c.BY; WHITE = _c.BW; GRAY = _c.GR
    BLUE = _c.BB; MAGENTA = _c.BM
    PURPLE = _c.P; ORANGE = _c.O; PINK = _c.PI
    LIME = _c.L; TEAL = _c.T; GOLD = _c.GO
    SILVER = _c.SI; BROWN = _c.BRO
    RESET = _c.RS; DIM = _c.D; BOLD = _c.B
else:
    GREEN = RED = CYAN = YELLOW = WHITE = GRAY = BLUE = MAGENTA = RESET = DIM = BOLD = ''
    PURPLE = ORANGE = PINK = LIME = TEAL = GOLD = SILVER = BROWN = ''

def a7(text, code):
    return f"{code}{text}{RESET}" if a1() else text

def green(text): return a7(text, GREEN)
def red(text): return a7(text, RED)
def cyan(text): return a7(text, CYAN)
def yellow(text): return a7(text, YELLOW)
def white(text): return a7(text, WHITE)
def gray(text): return a7(text, GRAY)
def blue(text): return a7(text, BLUE)
def magenta(text): return a7(text, MAGENTA)
def purple(text): return a7(text, PURPLE)
def orange(text): return a7(text, ORANGE)
def pink(text): return a7(text, PINK)
def lime(text): return a7(text, LIME)
def teal(text): return a7(text, TEAL)
def gold(text): return a7(text, GOLD)
def silver(text): return a7(text, SILVER)
def brown(text): return a7(text, BROWN)
def dim(text): return f"{DIM}{text}{RESET}" if a1() else text
def bold(text): return f"{BOLD}{text}{RESET}" if a1() else text

def reload_colors():
    global GREEN, RED, CYAN, YELLOW, WHITE, GRAY, BLUE, MAGENTA, RESET, DIM, BOLD
    global PURPLE, ORANGE, PINK, LIME, TEAL, GOLD, SILVER, BROWN
    global green, red, cyan, yellow, white, gray, blue, magenta, dim, bold
    global purple, orange, pink, lime, teal, gold, silver, brown
    
    settings = a4()
    codes = a2()
    
    if a1():
        color_map = {
            "GREEN": codes.BG, "RED": codes.BR, "CYAN": codes.BC,
            "YELLOW": codes.BY, "WHITE": codes.BW, "GRAY": codes.GR,
            "BLUE": codes.BB, "MAGENTA": codes.BM, "BLACK": codes.BL,
            "BRIGHT_RED": codes.BR, "BRIGHT_GREEN": codes.BG,
            "BRIGHT_YELLOW": codes.BY, "BRIGHT_BLUE": codes.BB,
            "BRIGHT_MAGENTA": codes.BM, "BRIGHT_CYAN": codes.BC,
            "BRIGHT_WHITE": codes.BW,
            "PURPLE": codes.P, "ORANGE": codes.O,
            "PINK": codes.PI, "LIME": codes.L,
            "TEAL": codes.T, "GOLD": codes.GO,
            "SILVER": codes.SI, "BROWN": codes.BRO
        }
    else:
        color_map = {k: '' for k in DEFAULT_COLORS.values()}
    
    GREEN = color_map.get(settings.get('primary', 'GREEN'), '')
    RED = color_map.get(settings.get('error', 'RED'), '')
    CYAN = color_map.get(settings.get('secondary', 'CYAN'), '')
    YELLOW = color_map.get(settings.get('warning', 'YELLOW'), '')
    WHITE = color_map.get(settings.get('highlight', 'WHITE'), '')
    GRAY = color_map.get(settings.get('dim', 'GRAY'), '')
    BLUE = color_map.get(settings.get('info', 'BLUE'), '')
    MAGENTA = color_map.get(settings.get('highlight', 'MAGENTA'), '')
    PURPLE = color_map.get('PURPLE', '')
    ORANGE = color_map.get('ORANGE', '')
    PINK = color_map.get('PINK', '')
    LIME = color_map.get('LIME', '')
    TEAL = color_map.get('TEAL', '')
    GOLD = color_map.get('GOLD', '')
    SILVER = color_map.get('SILVER', '')
    BROWN = color_map.get('BROWN', '')
    RESET = codes.RS if a1() else ''
    DIM = codes.D if a1() else ''
    BOLD = codes.B if a1() else ''
    
    def a7(text, code):
        return f"{code}{text}{RESET}" if a1() else text
    
    green = lambda text: a7(text, GREEN)
    red = lambda text: a7(text, RED)
    cyan = lambda text: a7(text, CYAN)
    yellow = lambda text: a7(text, YELLOW)
    white = lambda text: a7(text, WHITE)
    gray = lambda text: a7(text, GRAY)
    blue = lambda text: a7(text, BLUE)
    magenta = lambda text: a7(text, MAGENTA)
    purple = lambda text: a7(text, PURPLE)
    orange = lambda text: a7(text, ORANGE)
    pink = lambda text: a7(text, PINK)
    lime = lambda text: a7(text, LIME)
    teal = lambda text: a7(text, TEAL)
    gold = lambda text: a7(text, GOLD)
    silver = lambda text: a7(text, SILVER)
    brown = lambda text: a7(text, BROWN)
    dim = lambda text: f"{DIM}{text}{RESET}" if a1() else text
    bold = lambda text: f"{BOLD}{text}{RESET}" if a1() else text

def a8():
    settings = a4()
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        width = 55
        print("┌" + "─" * (width - 2) + "┐")
        print("│" + " " * ((width - 16) // 2) + "Color Settings" + " " * ((width - 16) // 2) + "│")
        print("└" + "─" * (width - 2) + "┘")
        print()
        print("Choose the interface color you want to change.")
        print("Or paste: ui.theme.success = GREEN")
        print()
        
        for i, key in enumerate(SETTINGS_KEYS, 1):
            code = COLOR_CODES.get(settings.get(key, ''), '')
            color_name = settings.get(key, '')
            label = LABELS.get(key, key)
            print(f"  {i:2}. {label:<12} {code}{color_name}{RESET}")
        
        print()
        print("  0. Back")
        print()
        
        choice = input("Enter your choice or paste config: ").strip()
        
        if choice == "0":
            break
        
        paste_match = re.search(r'ui\.theme\.(\w+)\s*[=:]\s*(\w+)', choice.lower())
        if paste_match:
            key = paste_match.group(1)
            color = paste_match.group(2).upper()
            if key in settings and color in COLOR_CODES:
                settings[key] = color
                a5(settings)
                reload_colors()
                print(f"\n  {key} set to {color}")
                print("  Colors updated!")
                time.sleep(1.5)
                continue
            else:
                print(f"\n  Invalid: {key} or {color}")
                time.sleep(1)
                continue
        
        paste_match2 = re.search(r'cfg\.ui\.color\.(\w+)\s*->\s*(\w+)', choice.lower())
        if paste_match2:
            key = paste_match2.group(1)
            color = paste_match2.group(2).upper()
            if key in settings and color in COLOR_CODES:
                settings[key] = color
                a5(settings)
                reload_colors()
                print(f"\n  {key} set to {color}")
                print("  Colors updated!")
                time.sleep(1.5)
                continue
            else:
                print(f"\n  Invalid: {key} or {color}")
                time.sleep(1)
                continue
        
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(SETTINGS_KEYS):
                key = SETTINGS_KEYS[num - 1]
                label = LABELS.get(key, key)
                os.system('clear' if os.name == 'posix' else 'cls')
                print("┌" + "─" * (width - 2) + "┐")
                print("│" + " " * ((width - 16) // 2) + "Select Color" + " " * ((width - 16) // 2) + "│")
                print("└" + "─" * (width - 2) + "┘")
                print()
                print(f"Changing: {label}")
                print()
                print("Available colors:")
                print()
                
                for i, c in enumerate(ALL_COLORS, 1):
                    code = COLOR_CODES.get(c, '')
                    print(f"  {i:2}. {code}{c}{RESET}")
                
                print()
                c_choice = input("Enter your choice: ").strip()
                if c_choice.isdigit() and 1 <= int(c_choice) <= len(ALL_COLORS):
                    settings[key] = ALL_COLORS[int(c_choice) - 1]
                    a5(settings)
                    reload_colors()
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("┌" + "─" * (width - 2) + "┐")
                    print("│" + " " * ((width - 16) // 2) + "Color Settings" + " " * ((width - 16) // 2) + "│")
                    print("└" + "─" * (width - 2) + "┘")
                    print()
                    print(f"  {label} changed to {settings[key]}")
                    print("  Colors updated!")
                    print()
                    input("Press Enter to continue...")
                else:
                    print("\n  Invalid choice!")
                    time.sleep(1)
            else:
                print("\n  Invalid choice!")
                time.sleep(1)
        else:
            print("\n  Invalid input!")
            time.sleep(1)
