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
    "primary": "BRIGHT_WHITE",
    "secondary": "WHITE",
    "success": "BRIGHT_WHITE",
    "error": "WHITE",
    "warning": "BRIGHT_WHITE",
    "info": "WHITE",
    "highlight": "BRIGHT_WHITE",
    "dim": "GRAY",
    "prompt": "BRIGHT_WHITE",
    "border": "WHITE",
    "title": "BRIGHT_WHITE",
    "status": "BRIGHT_WHITE",
    "module": "WHITE",
    "input": "BRIGHT_WHITE",
    "output": "WHITE",
    "banner": "BRIGHT_WHITE",
    "tab": "WHITE",
    "number": "BRIGHT_WHITE",
    "separator": "GRAY",
    "gradient_start": "BRIGHT_WHITE",
    "gradient_end": "WHITE",
    "accent": "BRIGHT_WHITE",
    "menu_bg": "BLACK",
    "menu_text": "BRIGHT_WHITE",
    "menu_highlight": "WHITE",
    "status_good": "BRIGHT_WHITE",
    "status_warn": "BRIGHT_WHITE",
    "status_bad": "WHITE",
    "header": "BRIGHT_WHITE",
    "footer": "GRAY",
    "divider": "GRAY",
    "label": "BRIGHT_WHITE",
    "value": "WHITE",
    "command": "BRIGHT_WHITE",
    "result": "WHITE",
    "timestamp": "GRAY",
    "count": "BRIGHT_WHITE",
    "progress": "BRIGHT_WHITE",
    "bar": "WHITE",
    "loading": "GRAY",
    "ascii_bg": "BLACK",
    "ascii_char": "BRIGHT_CYAN",
    "ascii_shadow": "GRAY",
    "ascii_highlight": "BRIGHT_WHITE",
    "ascii_gradient1": "HOT_PINK",
    "ascii_gradient2": "NEON_PINK",
    "ascii_gradient3": "PINK",
    "ascii_gradient4": "MAGENTA",
    "ascii_gradient5": "PURPLE",
    "ascii_gradient6": "LAVENDER",
    "ascii_gradient7": "SKY_BLUE",
    "ascii_gradient8": "BRIGHT_CYAN",
    "ascii_gradient9": "CYAN"
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
    "CRIMSON": '\033[38;5;160m', "AMBER": '\033[38;5;214m',
    "INDIGO": '\033[38;5;18m', "VIOLET": '\033[38;5;128m',
    "SCARLET": '\033[38;5;196m', "EMERALD": '\033[38;5;46m',
    "SAPPHIRE": '\033[38;5;21m', "RUBY": '\033[38;5;196m',
    "TOPAZ": '\033[38;5;178m', "TURQUOISE": '\033[38;5;44m',
    "AMETHYST": '\033[38;5;98m', "OPAL": '\033[38;5;254m',
    "JADE": '\033[38;5;47m', "ONYX": '\033[38;5;232m',
    "PEARL": '\033[38;5;255m', "CITRINE": '\033[38;5;226m',
    "PERIDOT": '\033[38;5;191m', "MOONSTONE": '\033[38;5;248m',
    "SUNSTONE": '\033[38;5;208m', "AQUA": '\033[38;5;80m',
    "LILAC": '\033[38;5;183m', "FUCHSIA": '\033[38;5;197m',
    "CERULEAN": '\033[38;5;38m', "VERMILLION": '\033[38;5;202m',
    "CHARTREUSE": '\033[38;5;119m', "MAUVE": '\033[38;5;148m',
    "TAUPE": '\033[38;5;102m', "CREAM": '\033[38;5;230m',
    "IVORY": '\033[38;5;231m', "CHARCOAL": '\033[38;5;238m',
    "SLATE": '\033[38;5;245m', "SAND": '\033[38;5;222m',
    "RESET": '\033[0m', "BOLD": '\033[1m', "DIM": '\033[2m'
}

ALL_COLORS = [
    "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE",
    "BRIGHT_RED", "BRIGHT_GREEN", "BRIGHT_YELLOW", "BRIGHT_BLUE", 
    "BRIGHT_MAGENTA", "BRIGHT_CYAN", "BRIGHT_WHITE",
    "GRAY", "PURPLE", "ORANGE", "PINK", "LIME", "TEAL", "GOLD", "SILVER", "BROWN",
    "HOT_PINK", "LAVENDER", "MINT", "PEACH", "CORAL", "SKY_BLUE",
    "NEON_GREEN", "NEON_PINK", "NEON_BLUE", "NEON_PURPLE",
    "SUNSET", "OCEAN", "FOREST", "ROSE",
    "CRIMSON", "AMBER", "INDIGO", "VIOLET", "SCARLET", "EMERALD",
    "SAPPHIRE", "RUBY", "TOPAZ", "TURQUOISE", "AMETHYST", "OPAL",
    "JADE", "ONYX", "PEARL", "CITRINE", "PERIDOT", "MOONSTONE",
    "SUNSTONE", "AQUA", "LILAC", "FUCHSIA", "CERULEAN", "VERMILLION",
    "CHARTREUSE", "MAUVE", "TAUPE", "CREAM", "IVORY", "CHARCOAL",
    "SLATE", "SAND"
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
            "FOREST": '\033[38;5;28m', "ROSE": '\033[38;5;162m',
            "CRIMSON": '\033[38;5;160m', "AMBER": '\033[38;5;214m',
            "INDIGO": '\033[38;5;18m', "VIOLET": '\033[38;5;128m',
            "SCARLET": '\033[38;5;196m', "EMERALD": '\033[38;5;46m',
            "SAPPHIRE": '\033[38;5;21m', "RUBY": '\033[38;5;196m',
            "TOPAZ": '\033[38;5;178m', "TURQUOISE": '\033[38;5;44m',
            "AMETHYST": '\033[38;5;98m', "OPAL": '\033[38;5;254m',
            "JADE": '\033[38;5;47m', "ONYX": '\033[38;5;232m',
            "PEARL": '\033[38;5;255m', "CITRINE": '\033[38;5;226m',
            "PERIDOT": '\033[38;5;191m', "MOONSTONE": '\033[38;5;248m',
            "SUNSTONE": '\033[38;5;208m', "AQUA": '\033[38;5;80m',
            "LILAC": '\033[38;5;183m', "FUCHSIA": '\033[38;5;197m',
            "CERULEAN": '\033[38;5;38m', "VERMILLION": '\033[38;5;202m',
            "CHARTREUSE": '\033[38;5;119m', "MAUVE": '\033[38;5;148m',
            "TAUPE": '\033[38;5;102m', "CREAM": '\033[38;5;230m',
            "IVORY": '\033[38;5;231m', "CHARCOAL": '\033[38;5;238m',
            "SLATE": '\033[38;5;245m', "SAND": '\033[38;5;222m'
        }
    return {k: '' for k in DEFAULT_COLORS.keys()}

def a7():
    s1 = a2()
    c1 = a6()
    r1 = {}
    for k in DEFAULT_COLORS.keys():
        r1[k] = c1.get(s1.get(k, DEFAULT_COLORS[k]), '')
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
    global PURPLE, ORANGE, PINK, LIME, TEAL, GOLD, SILVER, BROWN
    global HOT_PINK, LAVENDER, MINT, PEACH, CORAL, SKY_BLUE
    global NEON_GREEN, NEON_PINK, NEON_BLUE, NEON_PURPLE
    global SUNSET, OCEAN, FOREST, ROSE
    global CRIMSON, AMBER, INDIGO, VIOLET, SCARLET, EMERALD
    global SAPPHIRE, RUBY, TOPAZ, TURQUOISE, AMETHYST, OPAL
    global JADE, ONYX, PEARL, CITRINE, PERIDOT, MOONSTONE
    global SUNSTONE, AQUA, LILAC, FUCHSIA, CERULEAN, VERMILLION
    global CHARTREUSE, MAUVE, TAUPE, CREAM, IVORY, CHARCOAL, SLATE, SAND
    
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
    CRIMSON = a6().get('CRIMSON', '')
    AMBER = a6().get('AMBER', '')
    INDIGO = a6().get('INDIGO', '')
    VIOLET = a6().get('VIOLET', '')
    SCARLET = a6().get('SCARLET', '')
    EMERALD = a6().get('EMERALD', '')
    SAPPHIRE = a6().get('SAPPHIRE', '')
    RUBY = a6().get('RUBY', '')
    TOPAZ = a6().get('TOPAZ', '')
    TURQUOISE = a6().get('TURQUOISE', '')
    AMETHYST = a6().get('AMETHYST', '')
    OPAL = a6().get('OPAL', '')
    JADE = a6().get('JADE', '')
    ONYX = a6().get('ONYX', '')
    PEARL = a6().get('PEARL', '')
    CITRINE = a6().get('CITRINE', '')
    PERIDOT = a6().get('PERIDOT', '')
    MOONSTONE = a6().get('MOONSTONE', '')
    SUNSTONE = a6().get('SUNSTONE', '')
    AQUA = a6().get('AQUA', '')
    LILAC = a6().get('LILAC', '')
    FUCHSIA = a6().get('FUCHSIA', '')
    CERULEAN = a6().get('CERULEAN', '')
    VERMILLION = a6().get('VERMILLION', '')
    CHARTREUSE = a6().get('CHARTREUSE', '')
    MAUVE = a6().get('MAUVE', '')
    TAUPE = a6().get('TAUPE', '')
    CREAM = a6().get('CREAM', '')
    IVORY = a6().get('IVORY', '')
    CHARCOAL = a6().get('CHARCOAL', '')
    SLATE = a6().get('SLATE', '')
    SAND = a6().get('SAND', '')

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
def crimson(t1): return a10(t1, CRIMSON)
def amber(t1): return a10(t1, AMBER)
def indigo(t1): return a10(t1, INDIGO)
def violet(t1): return a10(t1, VIOLET)
def scarlet(t1): return a10(t1, SCARLET)
def emerald(t1): return a10(t1, EMERALD)
def sapphire(t1): return a10(t1, SAPPHIRE)
def ruby(t1): return a10(t1, RUBY)
def topaz(t1): return a10(t1, TOPAZ)
def turquoise(t1): return a10(t1, TURQUOISE)
def amethyst(t1): return a10(t1, AMETHYST)
def opal(t1): return a10(t1, OPAL)
def jade(t1): return a10(t1, JADE)
def onyx(t1): return a10(t1, ONYX)
def pearl(t1): return a10(t1, PEARL)
def citrine(t1): return a10(t1, CITRINE)
def peridot(t1): return a10(t1, PERIDOT)
def moonstone(t1): return a10(t1, MOONSTONE)
def sunstone(t1): return a10(t1, SUNSTONE)
def aqua(t1): return a10(t1, AQUA)
def lilac(t1): return a10(t1, LILAC)
def fuchsia(t1): return a10(t1, FUCHSIA)
def cerulean(t1): return a10(t1, CERULEAN)
def vermillion(t1): return a10(t1, VERMILLION)
def chartreuse(t1): return a10(t1, CHARTREUSE)
def mauve(t1): return a10(t1, MAUVE)
def taupe(t1): return a10(t1, TAUPE)
def cream(t1): return a10(t1, CREAM)
def ivory(t1): return a10(t1, IVORY)
def charcoal(t1): return a10(t1, CHARCOAL)
def slate(t1): return a10(t1, SLATE)
def sand(t1): return a10(t1, SAND)
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
           'crimson', 'amber', 'indigo', 'violet', 'scarlet', 'emerald',
           'sapphire', 'ruby', 'topaz', 'turquoise', 'amethyst', 'opal',
           'jade', 'onyx', 'pearl', 'citrine', 'peridot', 'moonstone',
           'sunstone', 'aqua', 'lilac', 'fuchsia', 'cerulean', 'vermillion',
           'chartreuse', 'mauve', 'taupe', 'cream', 'ivory', 'charcoal',
           'slate', 'sand',
           'dim', 'bold', 'reload_colors', 'color_settings_menu',
           'GREEN', 'RED', 'CYAN', 'YELLOW', 'WHITE', 'GRAY', 'BLUE', 'MAGENTA',
           'RESET', 'DIM', 'BOLD']
