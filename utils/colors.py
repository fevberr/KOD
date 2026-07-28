import os
import sys
import platform
import json
import time
import re
import shutil

CACHE_DIR = "cache"
COLORS_FILE = os.path.join(CACHE_DIR, "CSET.json")

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

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

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def truncate(s, w):
    if len(s) > w:
        return s[:w-1] + "…"
    return s

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
    try:
        with open(COLORS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def a2(s1):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    with open(COLORS_FILE, 'w') as f:
        json.dump(s1, f, indent=2)

def reload_colors():
    pass

def color_settings_menu():
    s1 = a1()
    w = get_terminal_width()
    rs = '\033[0m'
    g = '\033[92m'
    r = '\033[91m'
    c = '\033[96m'
    y = '\033[93m'
    wc = '\033[97m'
    gr = '\033[90m'
    m = '\033[95m'
    b = '\033[94m'
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        bw = min(w-2, 60)
        
        print(f"{c}┌{'─' * bw}┐{rs}")
        print(f"{c}│{rs}{wc}{' COLOR SETTINGS '.center(bw)}{rs}{c}│{rs}")
        print(f"{c}├{'─' * bw}┤{rs}")
        
        if not s1:
            print(f"{c}│{rs}{gr}{' No colors set. Add HEX below. '.center(bw)}{rs}{c}│{rs}")
        else:
            for i, k1 in enumerate(SETTINGS_KEYS, 1):
                val = s1.get(k1, '')
                c2 = ''
                if is_hex_color(val):
                    c2 = hex_to_ansi(val)
                n1 = truncate(val if val else '(not set)', 10)
                l1 = truncate(LABELS.get(k1, k1), 12)
                color_block = f"{c2}██████{rs}" if c2 else f"{gr}──────{rs}"
                if w < 40:
                    print(f"{c}│{rs} {y}{i:2}{rs} {l1} {color_block}")
                elif w < 60:
                    print(f"{c}│{rs} {y}{i:2}{rs}. {l1:<12} [{n1:<10}] {color_block}")
                else:
                    print(f"{c}│{rs} {y}{i:2}{rs}. {l1:<16} [{n1:<12}] {color_block}")
        print(f"{c}├{'─' * bw}┤{rs}")
        
        if w < 30:
            print(f"{c}│{rs} {g}[R]{rs} {r}[0]{rs} {m}[H]{rs}")
            print(f"{c}│{rs} {gr}Rst  Back  Hex{rs}")
        elif w < 50:
            print(f"{c}│{rs} {g}[R]{rs} Reset  {r}[0]{rs} Back  {m}[H]{rs} HEX")
        else:
            print(f"{c}│{rs} {g}[R]{rs} Reset  {r}[0]{rs} Back  {m}[H]{rs} HEX Color")
        print(f"{c}└{'─' * bw}┘{rs}")
        print()
        print(f"{gr} Enter number or: primary = #FF6B6B{rs}")
        print()
        
        c1 = input(f"{g}> {rs}").strip()
        
        if c1 == "0":
            break
        elif c1.lower() == "r":
            a2({})
            s1 = {}
            print(f"\n{g}[✓]{rs} All colors cleared!")
            time.sleep(1)
            continue
        elif c1.lower() == "h":
            print(f"\n{c}Enter HEX color (e.g., #FF6B6B):{rs}")
            hex_in = input(f"{g}> {rs}").strip()
            if hex_in:
                if not hex_in.startswith('#'):
                    hex_in = '#' + hex_in
                if is_hex_color(hex_in):
                    ansi = hex_to_ansi(hex_in)
                    print(f"\n{g}[✓]{rs} HEX {hex_in} converted")
                    print(f"  Preview: {ansi}██████{rs}")
                    print(f"\n{gr}Paste: primary = {hex_in}{rs}")
                    input(f"\n{g}> {rs}")
                else:
                    print(f"\n{r}[!]{rs} Invalid HEX")
                    time.sleep(1)
            continue
        
        # Check for setting = value pattern
        p1 = [
            r'(\w+)\s*[=:]\s*(#[0-9a-fA-F]{3,6}|[^\s]+)',
            r'(\w+)\s*->\s*(#[0-9a-fA-F]{3,6}|[^\s]+)',
        ]
        m1 = False
        for p2 in p1:
            m2 = re.search(p2, c1.lower())
            if m2:
                k1 = m2.group(1)
                c2 = m2.group(2)
                if k1 in LABELS:
                    if is_hex_color(c2):
                        s1[k1] = c2
                        a2(s1)
                        print(f"\n{g}[✓]{rs} {k1} = {c2}")
                        time.sleep(1.5)
                        m1 = True
                        break
                    else:
                        print(f"\n{r}[!]{rs} Invalid color: {c2}")
                        time.sleep(2)
                        m1 = True
                        break
                else:
                    print(f"\n{r}[!]{rs} Invalid setting: {k1}")
                    print(f"{gr}  Valid: {', '.join(list(LABELS.keys())[:5])}...{rs}")
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
                print(f"{c}┌{'─' * bw}┐{rs}")
                print(f"{c}│{rs}{wc}{f' Select Color: {l1} '.center(bw)}{rs}{c}│{rs}")
                print(f"{c}└{'─' * bw}┘{rs}")
                print()
                print(f"{gr}Enter HEX (e.g., #FF6B6B){rs}")
                print()
                c2 = input(f"{g}> {rs}").strip()
                if c2:
                    if not c2.startswith('#'):
                        c2 = '#' + c2
                    if is_hex_color(c2):
                        s1[k1] = c2
                        a2(s1)
                        print(f"\n{g}[✓]{rs} {l1} = {c2}")
                        time.sleep(1)
                    else:
                        print(f"\n{r}[!]{rs} Invalid color!")
                        time.sleep(1)
            else:
                print(f"\n{r}[!]{rs} Invalid number!")
                time.sleep(1)
        else:
            print(f"\n{r}[!]{rs} Invalid input!")
            print(f"{gr}  Use: primary = #FF6B6B{rs}")
            time.sleep(2)

__all__ = ['reload_colors', 'color_settings_menu', 'a1', 'a2', 'hex_to_ansi', 'is_hex_color']
