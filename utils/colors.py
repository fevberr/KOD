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
        'status_icon': c1.get(s1.get
