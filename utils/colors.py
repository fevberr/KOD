import os
import sys
import platform
import json
import time
import re

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

def a3():
    return a1()

def reload_colors():
    pass

def color_settings_menu():
    s1 = a1()
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        w1 = 80
        print("┌" + "─" * (w1 - 2) + "┐")
        print("│" + " 23 KOD COLOR SETTINGS ".center(w1 - 2) + "│")
        print("├" + "─" * (w1 - 2) + "┤")
        if not s1:
            print("│" + " No colors set. Add HEX values below.".center(w1 - 2) + "│")
        else:
            for i, k1 in enumerate(SETTINGS_KEYS, 1):
                val = s1.get(k1, '')
                c2 = ''
                if is_hex_color(val):
                    c2 = hex_to_ansi(val)
                n1 = val if val else '(not set)'
                l1 = LABELS.get(k1, k1)
                print("│ " + f"{i:2}. {l1:<16} [{n1:<12}]".ljust(w1 - 10) + c2 + "██████\033[0m".ljust(10) + "│")
        print("├" + "─" * (w1 - 2) + "┤")
        print("│" + " [R] Reset  [0] Back  [H] HEX Color".ljust(w1 - 2) + "│")
        print("└" + "─" * (w1 - 2) + "┘")
        print()
        print(" Enter number to change, or paste: primary = #FF6B6B")
        print()
        c1 = input("> ").strip()
        if c1 == "0":
            break
        elif c1.lower() == "r":
            a2({})
            s1 = {}
            print("\n[✓] All colors cleared!")
            time.sleep(1)
            continue
        elif c1.lower() == "h":
            print("\nEnter HEX color (e.g., #FF6B6B or FF6B6B):")
            hex_in = input("> ").strip()
            if hex_in:
                if not hex_in.startswith('#'):
                    hex_in = '#' + hex_in
                if is_hex_color(hex_in):
                    ansi = hex_to_ansi(hex_in)
                    print("[✓] HEX " + hex_in + " converted to ANSI")
                    print("  Preview: " + ansi + "██████\033[0m")
                    print("\nPaste this in color settings:")
                    print("  primary = " + hex_in)
                    input("\n> ")
                else:
                    print("[!] Invalid HEX color")
                    time.sleep(1)
            continue
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
                        print("\n[✓] " + k1 + " set to " + c2)
                        time.sleep(1.5)
                        m1 = True
                        break
                    else:
                        print("\n[!] Invalid color: " + c2)
                        time.sleep(2)
                        m1 = True
                        break
                else:
                    print("\n[!] Invalid setting: " + k1)
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
                print("┌" + "─" * (w1 - 2) + "┐")
                print("│" + (" Select Color for: " + l1).center(w1 - 2) + "│")
                print("└" + "─" * (w1 - 2) + "┘")
                print()
                print("Enter HEX color (e.g., #FF6B6B or FF6B6B):")
                print()
                c2 = input("> ").strip()
                if c2:
                    if not c2.startswith('#'):
                        c2 = '#' + c2
                    if is_hex_color(c2):
                        s1[k1] = c2
                        a2(s1)
                        print("\n[✓] " + l1 + " changed to " + s1[k1])
                        time.sleep(1)
                    else:
                        print("\n[!] Invalid color!")
                        time.sleep(1)
            else:
                print("\n[!] Invalid number!")
                time.sleep(1)
        else:
            print("\n[!] Invalid input! Use number or: primary = #FF6B6B")
            time.sleep(2)

__all__ = ['reload_colors', 'color_settings_menu', 'a1', 'a2', 'a3']
