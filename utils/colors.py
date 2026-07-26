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
    "primary": "ORANGE",
    "secondary": "GOLD",
    "success": "LIME",
    "error": "BRIGHT_RED",
    "warning": "BRIGHT_YELLOW",
    "info": "PURPLE",
    "highlight": "PINK",
    "dim": "BROWN",
    "prompt": "ORANGE",
    "border": "GOLD",
    "title": "BRIGHT_WHITE",
    "status": "BRIGHT_GREEN",
    "module": "BRIGHT_WHITE",
    "input": "BRIGHT_YELLOW",
    "output": "WHITE",
    "banner": "BRIGHT_CYAN",
    "tab": "BRIGHT_MAGENTA",
    "number": "BRIGHT_YELLOW",
    "separator": "GRAY",
    "gradient_start": "HOT_PINK",
    "gradient_end": "BRIGHT_CYAN",
    "accent": "GOLD",
    "menu_bg": "BLACK",
    "menu_text": "BRIGHT_WHITE",
    "menu_highlight": "BRIGHT_CYAN",
    "status_good": "LIME",
    "status_warn": "GOLD",
    "status_bad": "BRIGHT_RED",
    "header": "BRIGHT_CYAN",
    "footer": "GRAY",
    "divider": "GRAY",
    "label": "BRIGHT_WHITE",
    "value": "BRIGHT_CYAN",
    "command": "BRIGHT_YELLOW",
    "result": "WHITE",
    "timestamp": "GRAY",
    "count": "BRIGHT_MAGENTA",
    "progress": "LIME",
    "bar": "CYAN",
    "loading": "PURPLE",
    "success_icon": "LIME",
    "error_icon": "BRIGHT_RED",
    "warning_icon": "GOLD",
    "info_icon": "BRIGHT_BLUE",
    "highlight_icon": "BRIGHT_MAGENTA",
    "dim_icon": "GRAY",
    "border_icon": "BRIGHT_CYAN",
    "title_icon": "BRIGHT_WHITE",
    "status_icon": "BRIGHT_GREEN",
    "module_icon": "BRIGHT_WHITE",
    "input_icon": "BRIGHT_YELLOW",
    "output_icon": "WHITE",
    "banner_icon": "BRIGHT_CYAN",
    "tab_icon": "BRIGHT_MAGENTA",
    "number_icon": "BRIGHT_YELLOW",
    "separator_icon": "GRAY",
    "accent_icon": "GOLD"
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
    "HOT_PINK": '\033[38;5;205m', "LAVENDER": '\033[38;5;183m',
    "MINT": '\033[38;5;157m', "PEACH": '\033[38;5;216m',
    "CORAL": '\033[38;5;209m', "SKY_BLUE": '\033[38;5;117m',
    "NEON_GREEN": '\033[38;5;118m', "NEON_PINK": '\033[38;5;198m',
    "NEON_BLUE": '\033[38;5;45m', "NEON_PURPLE": '\033[38;5;93m',
    "SUNSET": '\033[38;5;202m', "OCEAN": '\033[38;5;39m',
    "FOREST": '\033[38;5;28m', "ROSE": '\033[38;5;162m',
    "RESET": '\033[0m', "BOLD": '\033[1m', "DIM": '\033[2m'
}

ALL_COLORS = [
    "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE",
    "BRIGHT_RED", "BRIGHT_GREEN", "BRIGHT_YELLOW", "BRIGHT_BLUE", 
    "BRIGHT_MAGENTA", "BRIGHT_CYAN", "BRIGHT_WHITE",
    "GRAY", "PURPLE", "ORANGE", "PINK", "LIME", "TEAL", "GOLD", "SILVER", "BROWN",
    "HOT_PINK", "LAVENDER", "MINT", "PEACH", "CORAL", "SKY_BLUE",
    "NEON_GREEN", "NEON_PINK", "NEON_BLUE", "NEON_PURPLE",
    "SUNSET", "OCEAN", "FOREST", "ROSE"
]

SETTINGS_KEYS = [
    "primary", "secondary", "success", "error", "warning", "info", 
    "highlight", "dim", "prompt", "border", "title", "status", 
    "module", "input", "output", "banner", "tab", "number", 
    "separator", "gradient_start", "gradient_end", "accent",
    "menu_bg", "menu_text", "menu_highlight",
    "status_good", "status_warn", "status_bad",
    "header", "footer", "divider", "label", "value", 
    "command", "result", "timestamp", "count", "progress", "bar", "loading",
    "success_icon", "error_icon", "warning_icon", "info_icon", 
    "highlight_icon", "dim_icon", "border_icon", "title_icon", 
    "status_icon", "module_icon", "input_icon", "output_icon",
    "banner_icon", "tab_icon", "number_icon", "separator_icon", "accent_icon"
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
    "success_icon": "✓ Icon", "error_icon": "✗ Icon", "warning_icon": "⚠ Icon",
    "info_icon": "ℹ Icon", "highlight_icon": "★ Icon", "dim_icon": "· Icon",
    "border_icon": "│ Icon", "title_icon": "► Icon", "status_icon": "● Icon",
    "module_icon": "■ Icon", "input_icon": "❯ Icon", "output_icon": "■ Icon",
    "banner_icon": "▲ Icon", "tab_icon": "▸ Icon", "number_icon": "# Icon",
    "separator_icon": "─ Icon", "accent_icon": "◆ Icon"
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
    if a1():
        return {
            "GREEN": '\033[92m', "RED": '\033[91m', "CYAN": '\033[96m',
            "YELLOW": '\033[93m', "WHITE": '\033[97m', "GRAY": '\033[90m',
            "BLUE": '\033[94m', "MAGENTA": '\033[95m', "BLACK": '\033[30m',
            "BRIGHT_RED": '\033[91m', "BRIGHT_GREEN": '\033[92m',
            "BRIGHT_YELLOW": '\033[93m', "BRIGHT_BLUE": '\033[94m',
            "BRIGHT_MAGENTA": '\033[95m', "BRIGHT_CYAN": '\033[96m',
            "BRIGHT_WHITE": '\033[97m',
            "PURPLE": '\033[95m', "ORANGE": '\033[38;5;208m',
            "PINK": '\033[38;5;201m', "LIME": '\033[38;5;154m',
            "TEAL": '\033[38;5;37m', "GOLD": '\033[38;5;220m',
            "SILVER": '\033[38;5;250m', "BROWN": '\033[38;5;130m',
            "HOT_PINK": '\033[38;5;205m', "LAVENDER": '\033[38;5;183m',
            "MINT": '\033[38;5;157m', "PEACH": '\033[38;5;216m',
            "CORAL": '\033[38;5;209m', "SKY_BLUE": '\033[38;5;117m',
            "NEON_GREEN": '\033[38;5;118m', "NEON_PINK": '\033[38;5;198m',
            "NEON_BLUE": '\033[38;5;45m', "NEON_PURPLE": '\033[38;5;93m',
            "SUNSET": '\033[38;5;202m', "OCEAN": '\033[38;5;39m',
            "FOREST": '\033[38;5;28m', "ROSE": '\033[38;5;162m'
        }
    return {k: '' for k in DEFAULT_COLORS.values()}

def a7():
    s1 = a2()
    c1 = a6()
    return {
        'primary': c1.get(s1.get('primary', 'ORANGE'), ''),
        'secondary': c1.get(s1.get('secondary', 'GOLD'), ''),
        'success': c1.get(s1.get('success', 'LIME'), ''),
        'error': c1.get(s1.get('error', 'BRIGHT_RED'), ''),
        'warning': c1.get(s1.get('warning', 'BRIGHT_YELLOW'), ''),
        'info': c1.get(s1.get('info', 'PURPLE'), ''),
        'highlight': c1.get(s1.get('highlight', 'PINK'), ''),
        'dim': c1.get(s1.get('dim', 'BROWN'), ''),
        'prompt': c1.get(s1.get('prompt', 'ORANGE'), ''),
        'border': c1.get(s1.get('border', 'GOLD'), ''),
        'title': c1.get(s1.get('title', 'BRIGHT_WHITE'), ''),
        'status': c1.get(s1.get('status', 'BRIGHT_GREEN'), ''),
        'module': c1.get(s1.get('module', 'BRIGHT_WHITE'), ''),
        'input': c1.get(s1.get('input', 'BRIGHT_YELLOW'), ''),
        'output': c1.get(s1.get('output', 'WHITE'), ''),
        'banner': c1.get(s1.get('banner', 'BRIGHT_CYAN'), ''),
        'tab': c1.get(s1.get('tab', 'BRIGHT_MAGENTA'), ''),
        'number': c1.get(s1.get('number', 'BRIGHT_YELLOW'), ''),
        'separator': c1.get(s1.get('separator', 'GRAY'), ''),
        'gradient_start': c1.get(s1.get('gradient_start', 'HOT_PINK'), ''),
        'gradient_end': c1.get(s1.get('gradient_end', 'BRIGHT_CYAN'), ''),
        'accent': c1.get(s1.get('accent', 'GOLD'), ''),
        'menu_bg': c1.get(s1.get('menu_bg', 'BLACK'), ''),
        'menu_text': c1.get(s1.get('menu_text', 'BRIGHT_WHITE'), ''),
        'menu_highlight': c1.get(s1.get('menu_highlight', 'BRIGHT_CYAN'), ''),
        'status_good': c1.get(s1.get('status_good', 'LIME'), ''),
        'status_warn': c1.get(s1.get('status_warn', 'GOLD'), ''),
        'status_bad': c1.get(s1.get('status_bad', 'BRIGHT_RED'), ''),
        'header': c1.get(s1.get('header', 'BRIGHT_CYAN'), ''),
        'footer': c1.get(s1.get('footer', 'GRAY'), ''),
        'divider': c1.get(s1.get('divider', 'GRAY'), ''),
        'label': c1.get(s1.get('label', 'BRIGHT_WHITE'), ''),
        'value': c1.get(s1.get('value', 'BRIGHT_CYAN'), ''),
        'command': c1.get(s1.get('command', 'BRIGHT_YELLOW'), ''),
        'result': c1.get(s1.get('result', 'WHITE'), ''),
        'timestamp': c1.get(s1.get('timestamp', 'GRAY'), ''),
        'count': c1.get(s1.get('count', 'BRIGHT_MAGENTA'), ''),
        'progress': c1.get(s1.get('progress', 'LIME'), ''),
        'bar': c1.get(s1.get('bar', 'CYAN'), ''),
        'loading': c1.get(s1.get('loading', 'PURPLE'), ''),
        'success_icon': c1.get(s1.get('success_icon', 'LIME'), ''),
        'error_icon': c1.get(s1.get('error_icon', 'BRIGHT_RED'), ''),
        'warning_icon': c1.get(s1.get('warning_icon', 'GOLD'), ''),
        'info_icon': c1.get(s1.get('info_icon', 'BRIGHT_BLUE'), ''),
        'highlight_icon': c1.get(s1.get('highlight_icon', 'BRIGHT_MAGENTA'), ''),
        'dim_icon': c1.get(s1.get('dim_icon', 'GRAY'), ''),
        'border_icon': c1.get(s1.get('border_icon', 'BRIGHT_CYAN'), ''),
        'title_icon': c1.get(s1.get('title_icon', 'BRIGHT_WHITE'), ''),
        'status_icon': c1.get(s1.get('status_icon', 'BRIGHT_GREEN'), ''),
        'module_icon': c1.get(s1.get('module_icon', 'BRIGHT_WHITE'), ''),
        'input_icon': c1.get(s1.get('input_icon', 'BRIGHT_YELLOW'), ''),
        'output_icon': c1.get(s1.get('output_icon', 'WHITE'), ''),
        'banner_icon': c1.get(s1.get('banner_icon', 'BRIGHT_CYAN'), ''),
        'tab_icon': c1.get(s1.get('tab_icon', 'BRIGHT_MAGENTA'), ''),
        'number_icon': c1.get(s1.get('number_icon', 'BRIGHT_YELLOW'), ''),
        'separator_icon': c1.get(s1.get('separator_icon', 'GRAY'), ''),
        'accent_icon': c1.get(s1.get('accent_icon', 'GOLD'), ''),
        'reset': '\033[0m' if a1() else '',
        'bold': '\033[1m' if a1() else '',
        'dim_text': '\033[2m' if a1() else ''
    }

GLOBAL_COLORS = {}

def a8():
    global GLOBAL_COLORS
    s1 = a2()
    c1 = a6()
    GLOBAL_COLORS = {
        'primary': c1.get(s1.get('primary', 'ORANGE'), ''),
        'secondary': c1.get(s1.get('secondary', 'GOLD'), ''),
        'success': c1.get(s1.get('success', 'LIME'), ''),
        'error': c1.get(s1.get('error', 'BRIGHT_RED'), ''),
        'warning': c1.get(s1.get('warning', 'BRIGHT_YELLOW'), ''),
        'info': c1.get(s1.get('info', 'PURPLE'), ''),
        'highlight': c1.get(s1.get('highlight', 'PINK'), ''),
        'dim': c1.get(s1.get('dim', 'BROWN'), ''),
        'prompt': c1.get(s1.get('prompt', 'ORANGE'), ''),
        'border': c1.get(s1.get('border', 'GOLD'), ''),
        'title': c1.get(s1.get('title', 'BRIGHT_WHITE'), ''),
        'status': c1.get(s1.get('status', 'BRIGHT_GREEN'), ''),
        'module': c1.get(s1.get('module', 'BRIGHT_WHITE'), ''),
        'input': c1.get(s1.get('input', 'BRIGHT_YELLOW'), ''),
        'output': c1.get(s1.get('output', 'WHITE'), ''),
        'banner': c1.get(s1.get('banner', 'BRIGHT_CYAN'), ''),
        'tab': c1.get(s1.get('tab', 'BRIGHT_MAGENTA'), ''),
        'number': c1.get(s1.get('number', 'BRIGHT_YELLOW'), ''),
        'separator': c1.get(s1.get('separator', 'GRAY'), ''),
        'gradient_start': c1.get(s1.get('gradient_start', 'HOT_PINK'), ''),
        'gradient_end': c1.get(s1.get('gradient_end', 'BRIGHT_CYAN'), ''),
        'accent': c1.get(s1.get('accent', 'GOLD'), ''),
        'menu_bg': c1.get(s1.get('menu_bg', 'BLACK'), ''),
        'menu_text': c1.get(s1.get('menu_text', 'BRIGHT_WHITE'), ''),
        'menu_highlight': c1.get(s1.get('menu_highlight', 'BRIGHT_CYAN'), ''),
        'status_good': c1.get(s1.get('status_good', 'LIME'), ''),
        'status_warn': c1.get(s1.get('status_warn', 'GOLD'), ''),
        'status_bad': c1.get(s1.get('status_bad', 'BRIGHT_RED'), ''),
        'header': c1.get(s1.get('header', 'BRIGHT_CYAN'), ''),
        'footer': c1.get(s1.get('footer', 'GRAY'), ''),
        'divider': c1.get(s1.get('divider', 'GRAY'), ''),
        'label': c1.get(s1.get('label', 'BRIGHT_WHITE'), ''),
        'value': c1.get(s1.get('value', 'BRIGHT_CYAN'), ''),
        'command': c1.get(s1.get('command', 'BRIGHT_YELLOW'), ''),
        'result': c1.get(s1.get('result', 'WHITE'), ''),
        'timestamp': c1.get(s1.get('timestamp', 'GRAY'), ''),
        'count': c1.get(s1.get('count', 'BRIGHT_MAGENTA'), ''),
        'progress': c1.get(s1.get('progress', 'LIME'), ''),
        'bar': c1.get(s1.get('bar', 'CYAN'), ''),
        'loading': c1.get(s1.get('loading', 'PURPLE'), ''),
        'success_icon': c1.get(s1.get('success_icon', 'LIME'), ''),
        'error_icon': c1.get(s1.get('error_icon', 'BRIGHT_RED'), ''),
        'warning_icon': c1.get(s1.get('warning_icon', 'GOLD'), ''),
        'info_icon': c1.get(s1.get('info_icon', 'BRIGHT_BLUE'), ''),
        'highlight_icon': c1.get(s1.get('highlight_icon', 'BRIGHT_MAGENTA'), ''),
        'dim_icon': c1.get(s1.get('dim_icon', 'GRAY'), ''),
        'border_icon': c1.get(s1.get('border_icon', 'BRIGHT_CYAN'), ''),
        'title_icon': c1.get(s1.get('title_icon', 'BRIGHT_WHITE'), ''),
        'status_icon': c1.get(s1.get('status_icon', 'BRIGHT_GREEN'), ''),
        'module_icon': c1.get(s1.get('module_icon', 'BRIGHT_WHITE'), ''),
        'input_icon': c1.get(s1.get('input_icon', 'BRIGHT_YELLOW'), ''),
        'output_icon': c1.get(s1.get('output_icon', 'WHITE'), ''),
        'banner_icon': c1.get(s1.get('banner_icon', 'BRIGHT_CYAN'), ''),
        'tab_icon': c1.get(s1.get('tab_icon', 'BRIGHT_MAGENTA'), ''),
        'number_icon': c1.get(s1.get('number_icon', 'BRIGHT_YELLOW'), ''),
        'separator_icon': c1.get(s1.get('separator_icon', 'GRAY'), ''),
        'accent_icon': c1.get(s1.get('accent_icon', 'GOLD'), ''),
        'reset': '\033[0m' if a1() else '',
        'bold': '\033[1m' if a1() else '',
        'dim_text': '\033[2m' if a1() else ''
    }

def a9():
    a8()
    global GREEN, RED, CYAN, YELLOW, WHITE, GRAY, BLUE, MAGENTA, RESET, DIM, BOLD
    global PURPLE, ORANGE, PINK, LIME, TEAL, GOLD, SILVER, BROWN
    global HOT_PINK, LAVENDER, MINT, PEACH, CORAL, SKY_BLUE
    global NEON_GREEN, NEON_PINK, NEON_BLUE, NEON_PURPLE
    global SUNSET, OCEAN, FOREST, ROSE
    
    c1 = GLOBAL_COLORS
    GREEN = c1['primary']
    RED = c1['error']
    CYAN = c1['secondary']
    YELLOW = c1['warning']
    WHITE = c1['highlight']
    GRAY = c1['dim']
    BLUE = c1['info']
    MAGENTA = c1['highlight']
    RESET = c1['reset']
    DIM = c1['dim_text']
    BOLD = c1['bold']
    PURPLE = a6().get('PURPLE', '')
    ORANGE = a6().get('ORANGE', '')
    PINK = a6().get('PINK', '')
    LIME = a6().get('LIME', '')
    TEAL = a6().get('TEAL', '')
    GOLD = a6().get('GOLD', '')
    SILVER = a6().get('SILVER', '')
    BROWN = a6().get('BROWN', '')
    HOT_PINK = a6().get('HOT_PINK', '')
    LAVENDER = a6().get('LAVENDER', '')
    MINT = a6().get('MINT', '')
    PEACH = a6().get('PEACH', '')
    CORAL = a6().get('CORAL', '')
    SKY_BLUE = a6().get('SKY_BLUE', '')
    NEON_GREEN = a6().get('NEON_GREEN', '')
    NEON_PINK = a6().get('NEON_PINK', '')
    NEON_BLUE = a6().get('NEON_BLUE', '')
    NEON_PURPLE = a6().get('NEON_PURPLE', '')
    SUNSET = a6().get('SUNSET', '')
    OCEAN = a6().get('OCEAN', '')
    FOREST = a6().get('FOREST', '')
    ROSE = a6().get('ROSE', '')

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
def purple(t1): return a10(t1, PURPLE)
def orange(t1): return a10(t1, ORANGE)
def pink(t1): return a10(t1, PINK)
def lime(t1): return a10(t1, LIME)
def teal(t1): return a10(t1, TEAL)
def gold(t1): return a10(t1, GOLD)
def silver(t1): return a10(t1, SILVER)
def brown(t1): return a10(t1, BROWN)
def hot_pink(t1): return a10(t1, HOT_PINK)
def lavender(t1): return a10(t1, LAVENDER)
def mint(t1): return a10(t1, MINT)
def peach(t1): return a10(t1, PEACH)
def coral(t1): return a10(t1, CORAL)
def sky_blue(t1): return a10(t1, SKY_BLUE)
def neon_green(t1): return a10(t1, NEON_GREEN)
def neon_pink(t1): return a10(t1, NEON_PINK)
def neon_blue(t1): return a10(t1, NEON_BLUE)
def neon_purple(t1): return a10(t1, NEON_PURPLE)
def sunset(t1): return a10(t1, SUNSET)
def ocean(t1): return a10(t1, OCEAN)
def forest(t1): return a10(t1, FOREST)
def rose(t1): return a10(t1, ROSE)
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
            c2 = COLOR_CODES.get(s1.get(k1, ''), '')
            n1 = s1.get(k1, '')
            l1 = LABELS.get(k1, k1)
            print(f"{CYAN}│ {i:2}. {l1:<16} [{n1:<12}]".ljust(w1 - 10) + f"{c2}██████{RESET}".ljust(10) + f"{CYAN}│{RESET}")
        print(f"{CYAN}├{'─' * (w1 - 2)}┤{RESET}")
        print(f"{CYAN}│{RESET}{GREEN} [T] Load Theme  [R] Reset  [0] Back{RESET}".ljust(w1 - 2) + f"{CYAN}│{RESET}")
        print(f"{CYAN}└{'─' * (w1 - 2)}┘{RESET}")
        print()
        print(f"{GRAY} Enter number to change, or paste: ui.theme.primary = ORANGE{RESET}")
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
        p1 = [
            r'(?:ui\.theme\.|cfg\.ui\.color\.)(\w+)\s*[=:]\s*(\w+)',
            r'(?:ui\.theme\.|cfg\.ui\.color\.)(\w+)\s*->\s*(\w+)',
            r'(\w+)\s*[=:]\s*(\w+)',
            r'(\w+)\s*->\s*(\w+)',
        ]
        m1 = False
        for p2 in p1:
            m2 = re.search(p2, c1.lower())
            if m2:
                k1 = m2.group(1)
                c2 = m2.group(2).upper()
                if k1 in s1:
                    if c2 in COLOR_CODES or c2 in ALL_COLORS:
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
                print("Available colors:")
                print()
                for i, c2 in enumerate(ALL_COLORS):
                    c3 = COLOR_CODES.get(c2, '')
                    print(f"  {i+1:2}. {c2:<15} {c3}██████{RESET}")
                    if (i + 1) % 4 == 0:
                        print()
                if len(ALL_COLORS) % 4 != 0:
                    print()
                print()
                c2 = input(f"{GREEN}Enter color number: {RESET}").strip()
                if c2.isdigit() and 1 <= int(c2) <= len(ALL_COLORS):
                    s1[k1] = ALL_COLORS[int(c2) - 1]
                    a3(s1)
                    a9()
                    print(f"{GREEN}\n[✓] {l1} changed to {s1[k1]}{RESET}")
                    time.sleep(1)
                else:
                    print(f"{RED}\n[!] Invalid choice!{RESET}")
                    time.sleep(1)
            else:
                print(f"{RED}\n[!] Invalid number!{RESET}")
                time.sleep(1)
        else:
            print(f"{RED}\n[!] Invalid input! Use number or: ui.theme.primary = ORANGE{RESET}")
            time.sleep(2)

a9()

__all__ = ['green', 'red', 'cyan', 'yellow', 'white', 'gray', 'blue', 'magenta',
           'purple', 'orange', 'pink', 'lime', 'teal', 'gold', 'silver', 'brown',
           'hot_pink', 'lavender', 'mint', 'peach', 'coral', 'sky_blue',
           'neon_green', 'neon_pink', 'neon_blue', 'neon_purple',
           'sunset', 'ocean', 'forest', 'rose',
           'dim', 'bold', 'reload_colors', 'color_settings_menu',
           'GREEN', 'RED', 'CYAN', 'YELLOW', 'WHITE', 'GRAY', 'BLUE', 'MAGENTA',
           'RESET', 'DIM', 'BOLD']
