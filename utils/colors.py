import os
import sys
import platform
import json
import time
import re
import shutil
import random

CACHE_DIR = "cache"
COLORS_FILE = os.path.join(CACHE_DIR, "CSET.json")

DEFAULT_COLORS = {
  "primary": "#7b2fbe",
  "secondary": "#9b59b6",
  "success": "#2ecc71",
  "error": "#e74c3c",
  "warning": "#f1c40f",
  "info": "#3498db",
  "highlight": "#bb8fce",
  "dim": "#7f8c8d",
  "prompt": "#7b2fbe",
  "border": "#9b59b6",
  "title": "#ffffff",
  "status": "#2ecc71",
  "module": "#bb8fce",
  "input": "#ffffff",
  "output": "#ecf0f1",
  "banner": "#7b2fbe",
  "tab": "#8e44ad",
  "number": "#f1c40f",
  "separator": "#7f8c8d",
  "gradient_start": "#7b2fbe",
  "gradient_end": "#bb8fce",
  "accent": "#f1c40f",
  "menu_bg": "#2c0e3e",
  "menu_text": "#ffffff",
  "menu_highlight": "#9b59b6",
  "status_good": "#2ecc71",
  "status_warn": "#f1c40f",
  "status_bad": "#e74c3c",
  "header": "#7b2fbe",
  "footer": "#2c0e3e",
  "divider": "#7f8c8d",
  "label": "#bb8fce",
  "value": "#9b59b6",
  "command": "#f1c40f",
  "result": "#ecf0f1",
  "timestamp": "#7f8c8d",
  "count": "#f1c40f",
  "progress": "#2ecc71",
  "bar": "#7b2fbe",
  "loading": "#3498db",
  "ascii_bg": "#2c0e3e",
  "ascii_char": "#ffffff",
  "ascii_shadow": "#7f8c8d",
  "ascii_highlight": "#bb8fce",
  "ascii_gradient1": "#2c0e3e",
  "ascii_gradient2": "#4a1a6b",
  "ascii_gradient3": "#7b2fbe",
  "ascii_gradient4": "#9b59b6",
  "ascii_gradient5": "#bb8fce",
  "ascii_gradient6": "#9b59b6",
  "ascii_gradient7": "#7b2fbe",
  "ascii_gradient8": "#4a1a6b",
  "ascii_gradient9": "#2c0e3e"
}

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

def color_preview(hex_color):
    if hex_color and is_hex_color(hex_color):
        ansi = hex_to_ansi(hex_color)
        return f"{ansi}██████\033[0m"
    return "░░░░░░"

def gradient_bar(width=30):
    colors = ['#7b2fbe', '#9b59b6', '#bb8fce', '#2ecc71', '#3498db', '#f1c40f', '#e74c3c']
    bar = ""
    for i in range(width):
        pos = i / width
        idx = int(pos * (len(colors) - 1))
        if idx >= len(colors):
            idx = len(colors) - 1
        c = colors[idx]
        ansi = hex_to_ansi(c)
        bar += f"{ansi}█\033[0m"
    return bar

def random_color():
    return f"#{random.randint(0,0xFFFFFF):06x}"

def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return None

def complementary_color(hex_color):
    rgb = hex_to_rgb(hex_color)
    if rgb:
        comp = tuple(255 - x for x in rgb)
        return rgb_to_hex(comp[0], comp[1], comp[2])
    return None

def darken_color(hex_color, factor=0.7):
    rgb = hex_to_rgb(hex_color)
    if rgb:
        dark = tuple(int(x * factor) for x in rgb)
        return rgb_to_hex(dark[0], dark[1], dark[2])
    return None

def lighten_color(hex_color, factor=1.3):
    rgb = hex_to_rgb(hex_color)
    if rgb:
        light = tuple(min(255, int(x * factor)) for x in rgb)
        return rgb_to_hex(light[0], light[1], light[2])
    return None

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

CATEGORIES = {
    "MAIN": ["primary", "secondary", "success", "error", "warning", "info", "highlight", "dim"],
    "UI": ["prompt", "border", "title", "status", "module", "input", "output", "banner", "tab", "number", "separator"],
    "ACCENT": ["gradient_start", "gradient_end", "accent"],
    "MENU": ["menu_bg", "menu_text", "menu_highlight"],
    "STATUS": ["status_good", "status_warn", "status_bad"],
    "TEXT": ["header", "footer", "divider", "label", "value", "command", "result", "timestamp", "count"],
    "PROGRESS": ["progress", "bar", "loading"],
    "ASCII": ["ascii_bg", "ascii_char", "ascii_shadow", "ascii_highlight"],
    "GRADIENT": ["ascii_gradient1", "ascii_gradient2", "ascii_gradient3", "ascii_gradient4", "ascii_gradient5", "ascii_gradient6", "ascii_gradient7", "ascii_gradient8", "ascii_gradient9"]
}

def a1():
    try:
        with open(COLORS_FILE, 'r') as f:
            return json.load(f)
    except:
        return DEFAULT_COLORS.copy()

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
    bold = '\033[1m'
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        bw = min(w-2, 70)
        
        print(f"{c}╔{'═' * bw}╗{rs}")
        print(f"{c}║{rs}{bold}{wc}{' COLOR STUDIO '.center(bw)}{rs}{c}║{rs}")
        print(f"{c}╠{'═' * bw}╣{rs}")
        
        grad = gradient_bar(min(bw-4, 40))
        print(f"{c}║{rs} {gr}Gradient:{rs} {grad}{rs} {c}║{rs}")
        print(f"{c}╠{'═' * bw}╣{rs}")
        
        if not s1:
            print(f"{c}║{rs} {r}WARNING: No colors set. Using defaults.{rs} {c}║{rs}")
        else:
            for cat_name, keys in CATEGORIES.items():
                print(f"{c}║{rs} {bold}{y}{cat_name}{rs} {c}║{rs}")
                for k in keys:
                    val = s1.get(k, '')
                    preview = color_preview(val)
                    label = truncate(LABELS.get(k, k), 14)
                    hex_display = truncate(val if val else 'EMPTY', 10)
                    
                    if w < 50:
                        print(f"{c}║{rs} {m}{k[:2]}{rs} {label} {preview} {c}║{rs}")
                    else:
                        print(f"{c}║{rs} {m}{k[:3]}{rs} {label:<14} {preview}  {gr}[{hex_display}]{rs} {c}║{rs}")
                print(f"{c}╠{'═' * bw}╣{rs}")
        
        print(f"{c}║{rs} {bold}{g}[1]{rs} Edit  {bold}{y}[2]{rs} Reset  {bold}{b}[3]{rs} Random All  {bold}{r}[0]{rs} Back  {c}║{rs}")
        print(f"{c}╚{'═' * bw}╝{rs}")
        print()
        print(f"{gr} Enter number, or paste: primary = #FF6B6B{rs}")
        print(f"{gr} Or: random, complement, darken, lighten{rs}")
        print()
        
        c1 = input(f"{g}> {rs}").strip()
        
        if c1 == "0":
            break
        elif c1 == "1":
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{c}╔{'═' * bw}╗{rs}")
            print(f"{c}║{rs}{bold}{wc}{' EDIT COLOR '.center(bw)}{rs}{c}║{rs}")
            print(f"{c}╠{'═' * bw}╣{rs}")
            
            for i, k in enumerate(SETTINGS_KEYS, 1):
                val = s1.get(k, '')
                preview = color_preview(val)
                label = truncate(LABELS.get(k, k), 16)
                print(f"{c}║{rs} {y}{i:2}{rs}. {label} {preview} {c}║{rs}")
            
            print(f"{c}╚{'═' * bw}╝{rs}")
            print()
            choice = input(f"{g}Select number (or 0 to go back): {rs}").strip()
            if choice.isdigit():
                num = int(choice)
                if 1 <= num <= len(SETTINGS_KEYS):
                    k = SETTINGS_KEYS[num-1]
                    label = LABELS.get(k, k)
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print(f"{c}╔{'═' * bw}╗{rs}")
                    print(f"{c}║{rs}{bold}{wc}{f' {label} '.center(bw)}{rs}{c}║{rs}")
                    print(f"{c}╠{'═' * bw}╣{rs}")
                    print(f"{c}║{rs} Current: {color_preview(s1.get(k, ''))} {gr}{s1.get(k, 'not set')}{rs} {c}║{rs}")
                    print(f"{c}╚{'═' * bw}╝{rs}")
                    print()
                    print(f"{gr}Options:{rs}")
                    print(f"  {g}[1]{rs} Enter HEX (e.g., #FF6B6B)")
                    print(f"  {y}[2]{rs} Random color")
                    print(f"  {b}[3]{rs} Complementary color")
                    print(f"  {m}[4]{rs} Darken")
                    print(f"  {c}[5]{rs} Lighten")
                    print()
                    opt = input(f"{g}> {rs}").strip()
                    
                    if opt == "1":
                        print(f"{gr}Enter HEX: {rs}")
                        new_val = input(f"{g}> {rs}").strip()
                        if new_val:
                            if not new_val.startswith('#'):
                                new_val = '#' + new_val
                            if is_hex_color(new_val):
                                s1[k] = new_val
                                a2(s1)
                                print(f"\n{g}SUCCESS{rs} {label} set to {new_val}")
                                time.sleep(1)
                            else:
                                print(f"\n{r}ERROR{rs} Invalid HEX color!")
                                time.sleep(1)
                    elif opt == "2":
                        new_val = random_color()
                        s1[k] = new_val
                        a2(s1)
                        print(f"\n{g}SUCCESS{rs} {label} set to {new_val}")
                        time.sleep(1)
                    elif opt == "3":
                        current = s1.get(k, '')
                        if current and is_hex_color(current):
                            new_val = complementary_color(current)
                            if new_val:
                                s1[k] = new_val
                                a2(s1)
                                print(f"\n{g}SUCCESS{rs} {label} set to {new_val}")
                                time.sleep(1)
                            else:
                                print(f"\n{r}ERROR{rs} Could not calculate complement")
                                time.sleep(1)
                        else:
                            print(f"\n{r}ERROR{rs} No valid color set")
                            time.sleep(1)
                    elif opt == "4":
                        current = s1.get(k, '')
                        if current and is_hex_color(current):
                            new_val = darken_color(current, 0.7)
                            if new_val:
                                s1[k] = new_val
                                a2(s1)
                                print(f"\n{g}SUCCESS{rs} {label} set to {new_val}")
                                time.sleep(1)
                            else:
                                print(f"\n{r}ERROR{rs} Could not darken")
                                time.sleep(1)
                        else:
                            print(f"\n{r}ERROR{rs} No valid color set")
                            time.sleep(1)
                    elif opt == "5":
                        current = s1.get(k, '')
                        if current and is_hex_color(current):
                            new_val = lighten_color(current, 1.3)
                            if new_val:
                                s1[k] = new_val
                                a2(s1)
                                print(f"\n{g}SUCCESS{rs} {label} set to {new_val}")
                                time.sleep(1)
                            else:
                                print(f"\n{r}ERROR{rs} Could not lighten")
                                time.sleep(1)
                        else:
                            print(f"\n{r}ERROR{rs} No valid color set")
                            time.sleep(1)
        elif c1 == "2":
            a2(DEFAULT_COLORS)
            s1 = DEFAULT_COLORS.copy()
            print(f"\n{g}SUCCESS{rs} Reset to default colors!")
            time.sleep(1)
        elif c1 == "3":
            for k in SETTINGS_KEYS:
                s1[k] = random_color()
            a2(s1)
            print(f"\n{g}SUCCESS{rs} All colors randomized!")
            time.sleep(1)
        else:
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
                        if c2.lower() == "random":
                            c2 = random_color()
                        elif c2.lower() == "complement" and s1.get(k1):
                            comp = complementary_color(s1.get(k1))
                            if comp:
                                c2 = comp
                        elif c2.lower() == "darken" and s1.get(k1):
                            dark = darken_color(s1.get(k1))
                            if dark:
                                c2 = dark
                        elif c2.lower() == "lighten" and s1.get(k1):
                            light = lighten_color(s1.get(k1))
                            if light:
                                c2 = light
                        elif c2.lower() == "invert" and s1.get(k1):
                            comp = complementary_color(s1.get(k1))
                            if comp:
                                c2 = comp
                        if is_hex_color(c2):
                            s1[k1] = c2
                            a2(s1)
                            print(f"\n{g}SUCCESS{rs} {k1} = {c2}")
                            time.sleep(1.5)
                            m1 = True
                            break
                        else:
                            print(f"\n{r}ERROR{rs} Invalid color: {c2}")
                            time.sleep(2)
                            m1 = True
                            break
                    else:
                        print(f"\n{r}ERROR{rs} Invalid setting: {k1}")
                        time.sleep(2)
                        m1 = True
                        break
            if m1:
                continue
            
            print(f"\n{r}ERROR{rs} Invalid input!")
            time.sleep(1)

__all__ = ['reload_colors', 'color_settings_menu', 'a1', 'a2', 'hex_to_ansi', 'is_hex_color']
