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

def color_preview(hex_color):
    if hex_color and is_hex_color(hex_color):
        ansi = hex_to_ansi(hex_color)
        return f"{ansi}██████\033[0m"
    return "░░░░░░"

def gradient_bar(width=30):
    colors = ['#ff0000', '#ff8800', '#ffff00', '#00ff00', '#0088ff', '#8800ff', '#ff00ff']
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
    "🎨 Main": ["primary", "secondary", "success", "error", "warning", "info", "highlight", "dim"],
    "🖼️ UI": ["prompt", "border", "title", "status", "module", "input", "output", "banner", "tab", "number", "separator"],
    "🎯 Accent": ["gradient_start", "gradient_end", "accent"],
    "📱 Menu": ["menu_bg", "menu_text", "menu_highlight"],
    "✅ Status": ["status_good", "status_warn", "status_bad"],
    "📝 Text": ["header", "footer", "divider", "label", "value", "command", "result", "timestamp", "count"],
    "📊 Progress": ["progress", "bar", "loading"],
    "🎭 ASCII": ["ascii_bg", "ascii_char", "ascii_shadow", "ascii_highlight"],
    "🌈 Gradient": ["ascii_gradient1", "ascii_gradient2", "ascii_gradient3", "ascii_gradient4", "ascii_gradient5", "ascii_gradient6", "ascii_gradient7", "ascii_gradient8", "ascii_gradient9"]
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
    
    # Theme colors
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
        
        # Header with gradient
        print(f"{c}╔{'═' * bw}╗{rs}")
        print(f"{c}║{rs}{bold}{wc}{' 🎨 COLOR STUDIO 🎨 '.center(bw)}{rs}{c}║{rs}")
        print(f"{c}╠{'═' * bw}╣{rs}")
        
        # Show gradient bar preview
        grad = gradient_bar(min(bw-4, 40))
        print(f"{c}║{rs} {gr}Gradient:{rs} {grad}{rs} {c}║{rs}")
        print(f"{c}╠{'═' * bw}╣{rs}")
        
        # Show categories and colors
        if not s1:
            print(f"{c}║{rs} {r}⚠ No colors set. Add HEX values below.{rs} {c}║{rs}")
        else:
            for cat_name, keys in CATEGORIES.items():
                print(f"{c}║{rs} {bold}{y}{cat_name}{rs} {c}║{rs}")
                for k in keys:
                    val = s1.get(k, '')
                    preview = color_preview(val)
                    label = truncate(LABELS.get(k, k), 14)
                    hex_display = truncate(val if val else '─', 10)
                    
                    if w < 50:
                        print(f"{c}║{rs} {m}{k[:2]}{rs} {label} {preview} {c}║{rs}")
                    else:
                        print(f"{c}║{rs} {m}{k[:3]}{rs} {label:<14} {preview}  {gr}[{hex_display}]{rs} {c}║{rs}")
                print(f"{c}╠{'═' * bw}╣{rs}")
        
        # Footer menu
        print(f"{c}║{rs} {bold}{g}[1]{rs} Edit  {bold}{y}[2]{rs} Reset  {bold}{b}[3]{rs} Hex Help  {bold}{r}[0]{rs} Back  {c}║{rs}")
        print(f"{c}╚{'═' * bw}╝{rs}")
        print()
        print(f"{gr} Enter number, or paste: primary = #FF6B6B{rs}")
        print()
        
        c1 = input(f"{g}> {rs}").strip()
        
        if c1 == "0":
            break
        elif c1 == "1":
            # Edit menu - show list of all settings with numbers
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
                    print(f"{gr}Enter HEX (e.g., #FF6B6B or FF6B6B){rs}")
                    print(f"{gr}Or enter: random for a random color{rs}")
                    print()
                    new_val = input(f"{g}> {rs}").strip()
                    if new_val:
                        if new_val.lower() == "random":
                            import random
                            new_val = f"#{random.randint(0,0xFFFFFF):06x}"
                        if not new_val.startswith('#'):
                            new_val = '#' + new_val
                        if is_hex_color(new_val):
                            s1[k] = new_val
                            a2(s1)
                            print(f"\n{g}✓{rs} {label} set to {new_val}")
                            time.sleep(1)
                        else:
                            print(f"\n{r}✗{rs} Invalid HEX color!")
                            time.sleep(1)
        elif c1 == "2":
            # Reset all colors
            a2({})
            s1 = {}
            print(f"\n{g}✓{rs} All colors cleared!")
            time.sleep(1)
        elif c1 == "3":
            # Hex help
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{c}╔{'═' * bw}╗{rs}")
            print(f"{c}║{rs}{bold}{wc}{' HEX COLOR HELP '.center(bw)}{rs}{c}║{rs}")
            print(f"{c}╠{'═' * bw}╣{rs}")
            print(f"{c}║{rs} {gr}Enter HEX colors like: #FF6B6B{rs} {c}║{rs}")
            print(f"{c}║{rs} {gr}Or: FF6B6B (without #){rs} {c}║{rs}")
            print(f"{c}║{rs} {gr}Or: random for random color{rs} {c}║{rs}")
            print(f"{c}║{rs}{rs} {c}║{rs}")
            print(f"{c}║{rs} {bold}{y}Example colors:{rs} {c}║{rs}")
            examples = [
                ("#FF6B6B", "Red"),
                ("#4ECDC4", "Teal"),
                ("#45B7D1", "Blue"),
                ("#96CEB4", "Green"),
                ("#FFEAA7", "Yellow"),
                ("#DDA0DD", "Plum"),
                ("#FF9FF3", "Pink"),
                ("#54A0FF", "Sky Blue")
            ]
            for hex_val, name in examples:
                preview = color_preview(hex_val)
                print(f"{c}║{rs} {preview} {hex_val} - {name}{rs} {c}║{rs}")
            print(f"{c}╚{'═' * bw}╝{rs}")
            print()
            input(f"{g}Press Enter to continue{rs}")
        else:
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
                        if c2.lower() == "random":
                            import random
                            c2 = f"#{random.randint(0,0xFFFFFF):06x}"
                        if is_hex_color(c2):
                            s1[k1] = c2
                            a2(s1)
                            print(f"\n{g}✓{rs} {k1} = {c2}")
                            time.sleep(1.5)
                            m1 = True
                            break
                        else:
                            print(f"\n{r}✗{rs} Invalid color: {c2}")
                            time.sleep(2)
                            m1 = True
                            break
                    else:
                        print(f"\n{r}✗{rs} Invalid setting: {k1}")
                        print(f"{gr}  Valid: {', '.join(list(LABELS.keys())[:5])}...{rs}")
                        time.sleep(2)
                        m1 = True
                        break
            if m1:
                continue
            
            print(f"\n{r}✗{rs} Invalid input!")
            time.sleep(1)

__all__ = ['reload_colors', 'color_settings_menu', 'a1', 'a2', 'hex_to_ansi', 'is_hex_color']
