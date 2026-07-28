import os
import sys
import platform
import json
import time
import re
import glob

COLORS_FILE = "color_settings.json"
THEMES_DIR = "themes"
CURRENT_THEME = None

DEFAULT_COLORS = {
    "primary": "#00ffcc",
    "secondary": "#ff6bff",
    "success": "#00ff88",
    "error": "#ff0044",
    "warning": "#ffaa00",
    "info": "#0088ff",
    "highlight": "#ff44ff",
    "dim": "#888888",
    "prompt": "#00ffcc",
    "border": "#ff6bff",
    "title": "#ffffff",
    "status": "#00ff88",
    "module": "#ffffff",
    "input": "#ffdd00",
    "output": "#ffffff",
    "banner": "#00ffcc",
    "tab": "#ff44ff",
    "number": "#ffdd00",
    "separator": "#888888",
    "gradient_start": "#ff1493",
    "gradient_end": "#00ffcc",
    "accent": "#ffaa00",
    "menu_bg": "#000000",
    "menu_text": "#ffffff",
    "menu_highlight": "#00ffcc",
    "status_good": "#00ff88",
    "status_warn": "#ffaa00",
    "status_bad": "#ff0044",
    "header": "#00ffcc",
    "footer": "#888888",
    "divider": "#888888",
    "label": "#ffffff",
    "value": "#00ffcc",
    "command": "#ffdd00",
    "result": "#ffffff",
    "timestamp": "#888888",
    "count": "#ff44ff",
    "progress": "#00ff88",
    "bar": "#00ffcc",
    "loading": "#ff44ff",
    "ascii_bg": "#000000",
    "ascii_char": "#00ffcc",
    "ascii_shadow": "#888888",
    "ascii_highlight": "#ffffff",
    "ascii_gradient1": "#ff1493",
    "ascii_gradient2": "#ff6bff",
    "ascii_gradient3": "#ff44ff",
    "ascii_gradient4": "#cc00ff",
    "ascii_gradient5": "#8800ff",
    "ascii_gradient6": "#4444ff",
    "ascii_gradient7": "#0088ff",
    "ascii_gradient8": "#00ccff",
    "ascii_gradient9": "#00ffcc"
}

HEX_CACHE = {}

def hex_to_ansi(hex_color):
    if hex_color in HEX_CACHE:
        return HEX_CACHE[hex_color]
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    if len(hex_color) == 6:
        try:
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            ansi = f'\033[38;2;{r};{g};{b}m'
            HEX_CACHE[hex_color] = ansi
            return ansi
        except:
            pass
    return ''

def is_hex_color(color):
    if isinstance(color, str):
        color = color.strip()
        if color.startswith('#'):
            color = color[1:]
        return len(color) in (3, 6) and all(c in '0123456789ABCDEFabcdef' for c in color)
    return False

SETTINGS_KEYS = [
    "primary", "secondary", "success", "error", "warning", "info", 
    "highlight", "dim", "prompt", "border", "title", "status", 
    "module", "input", "output", "banner", "tab", "number", 
    "separator", "gradient_start", "gradient_end", "accent",
    "menu_bg", "menu_text", "menu_highlight",
    "status_good", "status_warn", "status_bad",
    "header", "footer", "divider", "label", "value", 
    "command", "result", "timestamp", "count", "progress", "bar", "loading",
    "ascii_bg", "ascii_char", "ascii_shadow", "ascii_highlight",
    "ascii_gradient1", "ascii_gradient2", "ascii_gradient3",
    "ascii_gradient4", "ascii_gradient5", "ascii_gradient6",
    "ascii_gradient7", "ascii_gradient8", "ascii_gradient9"
]

LABELS = {
    "primary": "Primary", "secondary": "Secondary", "success": "Success",
    "error": "Error", "warning": "Warning", "info": "Info",
    "highlight": "Highlight", "dim": "Dim", "prompt": "Prompt", 
    "border": "Border", "title": "Title", "status": "Status",
    "module": "Module", "input": "Input", "output": "Output",
    "banner": "Banner", "tab": "Tab", "number": "Number", 
    "separator": "Separator", "gradient_start": "Gradient Start", 
    "gradient_end": "Gradient End", "accent": "Accent",
    "menu_bg": "Menu BG", "menu_text": "Menu Text", "menu_highlight": "Menu Highlight",
    "status_good": "Status Good", "status_warn": "Status Warn", "status_bad": "Status Bad",
    "header": "Header", "footer": "Footer", "divider": "Divider",
    "label": "Label", "value": "Value", "command": "Command",
    "result": "Result", "timestamp": "Timestamp", "count": "Count",
    "progress": "Progress", "bar": "Bar", "loading": "Loading",
    "ascii_bg": "ASCII BG", "ascii_char": "ASCII Char", 
    "ascii_shadow": "ASCII Shadow", "ascii_highlight": "ASCII Highlight",
    "ascii_gradient1": "Gradient 1", "ascii_gradient2": "Gradient 2",
    "ascii_gradient3": "Gradient 3", "ascii_gradient4": "Gradient 4",
    "ascii_gradient5": "Gradient 5", "ascii_gradient6": "Gradient 6",
    "ascii_gradient7": "Gradient 7", "ascii_gradient8": "Gradient 8",
    "ascii_gradient9": "Gradient 9"
}

def a1():
    if not hasattr(sys.stdout, 'isatty') or not sys.stdout.isatty():
        return False
    if os.environ.get('NO_COLOR'):
        return False
    if os.environ.get('FORCE_COLOR'):
        return True
    t1 = os.environ.get('TERM', '')
    if t1 in ('dumb', 'linux'):
        return False
    if platform.system() == 'Windows':
        try:
            import ctypes
            k1 = ctypes.windll.kernel32
            h1 = k1.GetStdHandle(-11)
            m1 = ctypes.c_ulong()
            if k1.GetConsoleMode(h1, ctypes.byref(m1)):
                k1.SetConsoleMode(h1, m1.value | 0x0004)
                return True
            return False
        except:
            return False
    return t1 not in ('', 'dumb', 'linux')

def a2():
    try:
        with open(COLORS_FILE, 'r') as f:
            return json.load(f)
    except:
        return DEFAULT_COLORS.copy()

def a3(s1):
    with open(COLORS_FILE, 'w') as f:
        json.dump(s1, f, indent=2)

def a4(p1):
    global CURRENT_THEME
    try:
        with open(p1, 'r') as f:
            t1 = json.load(f)
        if 'colors' in t1:
            CURRENT_THEME = t1
            a3(t1['colors'])
            a9()
            return True
    except:
        pass
    return False

def a5():
    t1 = []
    if os.path.exists(THEMES_DIR):
        for f in glob.glob(f"{THEMES_DIR}/*.json"):
            try:
                with open(f, 'r') as file:
                    d1 = json.load(file)
                    n1 = d1.get('name', os.path.basename(f).replace('.json', ''))
                    t1.append((os.path.basename(f), n1))
            except:
                t1.append((os.path.basename(f), os.path.basename(f).replace('.json', '')))
    return t1

def a6():
    return {}

def a7():
    s1 = a2()
    r1 = {}
    for k in DEFAULT_COLORS.keys():
        val = s1.get(k, DEFAULT_COLORS[k])
        if is_hex_color(val):
            r1[k] = hex_to_ansi(val)
        else:
            r1[k] = ''
    r1['reset'] = '\033[0m' if a1() else ''
    r1['bold'] = '\033[1m' if a1() else ''
    r1['dim_text'] = '\033[2m' if a1() else ''
    return r1

GLOBAL_COLORS = {}

def a8():
    global GLOBAL_COLORS
    GLOBAL_COLORS = a7()

def a9():
    a8()
    global GREEN, RED, CYAN, YELLOW, WHITE, GRAY, BLUE, MAGENTA, RESET, DIM, BOLD
    c1 = GLOBAL_COLORS
    GREEN = c1.get('primary', '')
    RED = c1.get('error', '')
    CYAN = c1.get('secondary', '')
    YELLOW = c1.get('warning', '')
    WHITE = c1.get('highlight', '')
    GRAY = c1.get('dim', '')
    BLUE = c1.get('info', '')
    MAGENTA = c1.get('highlight', '')
    RESET = c1.get('reset', '')
    DIM = c1.get('dim_text', '')
    BOLD = c1.get('bold', '')

def a10(t1, c1):
    return f"{c1}{t1}{RESET}" if a1() else t1

def green(t1): return a10(t1, GREEN)
def red(t1): return a10(t1, RED)
def cyan(t1): return a10(t1, CYAN)
def yellow(t1): return a10(t1, YELLOW)
def white(t1): return a10(t1, WHITE)
def gray(t1): return a10(t1, GRAY)
def blue(t1): return a10(t1, BLUE)
def magenta(t1): return a10(t1, MAGENTA)
def dim(t1): return f"{DIM}{t1}{RESET}" if a1() else t1
def bold(t1): return f"{BOLD}{t1}{RESET}" if a1() else t1

def reload_colors():
    a9()

def color_settings_menu():
    s1 = a2()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        w1 = 80
        print(f"{CYAN}┌{'─' * (w1 - 2)}┐{RESET}")
        print(f"{CYAN}│{RESET}{WHITE}{' 23 KOD COLOR SETTINGS '.center(w1 - 2)}{RESET}{CYAN}│{RESET}")
        print(f"{CYAN}├{'─' * (w1 - 2)}┤{RESET}")
        if CURRENT_THEME:
            print(f"{CYAN}│{RESET}{GREEN} Theme: {CURRENT_THEME.get('name', 'Custom')}{RESET}".ljust(w1 - 2) + f"{CYAN}│{RESET}")
        print(f"{CYAN}├{'─' * (w1 - 2)}┤{RESET}")
        for i, k1 in enumerate(SETTINGS_KEYS, 1):
            val = s1.get(k1, '')
            c2 = ''
            if is_hex_color(val):
                c2 = hex_to_ansi(val)
            n1 = val
            l1 = LABELS.get(k1, k1)
            print(f"{CYAN}│ {i:2}. {l1:<16} [{n1:<12}]".ljust(w1 - 10) + f"{c2}██████{RESET}".ljust(10) + f"{CYAN}│{RESET}")
        print(f"{CYAN}├{'─' * (w1 - 2)}┤{RESET}")
        print(f"{CYAN}│{RESET}{GREEN} [T] Load Theme  [R] Reset  [0] Back  [H] HEX Color{RESET}".ljust(w1 - 2) + f"{CYAN}│{RESET}")
        print(f"{CYAN}└{'─' * (w1 - 2)}┘{RESET}")
        print()
        print(f"{GRAY} Enter number to change, or paste: ui.theme.primary = #FF6B6B{RESET}")
        print()
        c1 = input(f"{GREEN}> {RESET}").strip()
        if c1 == "0":
            break
        elif c1.lower() == "t":
            t1 = a5()
            if t1:
                print(f"\n{CYAN}Available Themes:{RESET}")
                for i, (f1, n1) in enumerate(t1, 1):
                    print(f"  {i}. {n1}")
                print()
                t2 = input(f"{GREEN}Select theme: {RESET}").strip()
                if t2.isdigit() and 1 <= int(t2) <= len(t1):
                    if a4(os.path.join(THEMES_DIR, t1[int(t2)-1][0])):
                        print(f"{GREEN}\n[✓] Loaded theme: {t1[int(t2)-1][0]}{RESET}")
                        time.sleep(1)
            else:
                print(f"{RED}\n[!] No themes found{RESET}")
                time.sleep(1)
            continue
        elif c1.lower() == "r":
            a3(DEFAULT_COLORS)
            a9()
            print(f"{GREEN}\n[✓] Reset to default colors!{RESET}")
            time.sleep(1)
            continue
        elif c1.lower() == "h":
            print(f"\n{CYAN}Enter HEX color (e.g., #FF6B6B or FF6B6B):{RESET}")
            hex_in = input(f"{GREEN}> {RESET}").strip()
            if hex_in:
                if not hex_in.startswith('#'):
                    hex_in = '#' + hex_in
                if is_hex_color(hex_in):
                    ansi = hex_to_ansi(hex_in)
                    print(f"{GREEN}[✓] HEX {hex_in} converted to ANSI{RESET}")
                    print(f"  Preview: {ansi}██████{RESET}")
                    print(f"\n{GRAY}Paste this in color settings:{RESET}")
                    print(f"  ui.theme.primary = {hex_in}")
                    input(f"\n{GREEN}> {RESET}")
                else:
                    print(f"{RED}[!] Invalid HEX color{RESET}")
                    time.sleep(1)
            continue
        p1 = [
            r'(?:ui\.theme\.|cfg\.ui\.color\.)(\w+)\s*[=:]\s*(#[0-9a-fA-F]{3,6}|[^\s]+)',
            r'(?:ui\.theme\.|cfg\.ui\.color\.)(\w+)\s*->\s*(#[0-9a-fA-F]{3,6}|[^\s]+)',
            r'(\w+)\s*[=:]\s*(#[0-9a-fA-F]{3,6}|[^\s]+)',
            r'(\w+)\s*->\s*(#[0-9a-fA-F]{3,6}|[^\s]+)',
        ]
        m1 = False
        for p2 in p1:
            m2 = re.search(p2, c1.lower())
            if m2:
                k1 = m2.group(1)
                c2 = m2.group(2)
                if k1 in s1:
                    if is_hex_color(c2):
                        s1[k1] = c2
                        a3(s1)
                        a9()
                        print(f"{GREEN}\n[✓] {k1} set to {c2}{RESET}")
                        time.sleep(1.5)
                        m1 = True
                        break
                    else:
                        print(f"{RED}\n[!] Invalid color: {c2}{RESET}")
                        time.sleep(2)
                        m1 = True
                        break
                else:
                    print(f"{RED}\n[!] Invalid setting: {k1}{RESET}")
                    time.sleep(2)
                    m1 = True
                    break
        if m1:
            continue
        if c1.isdigit():
            n1 = int(c1)
            if 1 <= n1 <= len(SETTINGS_KEYS):
                k1 = SETTINGS_KEYS[n1 - 1]
                l1 = LABELS.get(k1, k1)
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"{CYAN}┌{'─' * (w1 - 2)}┐{RESET}")
                print(f"{CYAN}│{RESET}{WHITE} Select Color for: {l1} {RESET}".center(w1 - 2) + f"{CYAN}│{RESET}")
                print(f"{CYAN}└{'─' * (w1 - 2)}┘{RESET}")
                print()
                print("Enter HEX color (e.g., #FF6B6B or FF6B6B):")
                print()
                c2 = input(f"{GREEN}> {RESET}").strip()
                if c2:
                    if not c2.startswith('#'):
                        c2 = '#' + c2
                    if is_hex_color(c2):
                        s1[k1] = c2
                        a3(s1)
                        a9()
                        print(f"{GREEN}\n[✓] {l1} changed to {s1[k1]}{RESET}")
                        time.sleep(1)
                    else:
                        print(f"{RED}\n[!] Invalid color!{RESET}")
                        time.sleep(1)
            else:
                print(f"{RED}\n[!] Invalid number!{RESET}")
                time.sleep(1)
        else:
            print(f"{RED}\n[!] Invalid input! Use number or: ui.theme.primary = #FF6B6B{RESET}")
            time.sleep(2)

a9()

__all__ = ['green', 'red', 'cyan', 'yellow', 'white', 'gray', 'blue', 'magenta',
           'dim', 'bold', 'reload_colors', 'color_settings_menu',
           'GREEN', 'RED', 'CYAN', 'YELLOW', 'WHITE', 'GRAY', 'BLUE', 'MAGENTA',
           'RESET', 'DIM', 'BOLD']
