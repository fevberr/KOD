import os
import sys
import platform

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
        RS = '\033[0m'
        B = '\033[1m'
        D = '\033[2m'
        BL = '\033[30m'
        R = '\033[31m'
        G = '\033[32m'
        Y = '\033[33m'
        BLU = '\033[34m'
        M = '\033[35m'
        C = '\033[36m'
        W = '\033[37m'
        BR = '\033[91m'
        BG = '\033[92m'
        BY = '\033[93m'
        BB = '\033[94m'
        BM = '\033[95m'
        BC = '\033[96m'
        BW = '\033[97m'
        GR = '\033[90m'
    return a3

if a1():
    _c = a2()
    GREEN = _c.BG
    RED = _c.BR
    CYAN = _c.BC
    YELLOW = _c.BY
    WHITE = _c.BW
    GRAY = _c.GR
    BLUE = _c.BB
    MAGENTA = _c.BM
    RESET = _c.RS
    DIM = _c.D
    BOLD = _c.B
else:
    GREEN = RED = CYAN = YELLOW = WHITE = GRAY = BLUE = MAGENTA = RESET = DIM = BOLD = ''

def a4(text, code):
    return f"{code}{text}{RESET}" if a1() else text

def green(text): return a4(text, GREEN)
def red(text): return a4(text, RED)
def cyan(text): return a4(text, CYAN)
def yellow(text): return a4(text, YELLOW)
def white(text): return a4(text, WHITE)
def gray(text): return a4(text, GRAY)
def blue(text): return a4(text, BLUE)
def magenta(text): return a4(text, MAGENTA)
def dim(text): return f"{DIM}{text}{RESET}" if a1() else text
def bold(text): return f"{BOLD}{text}{RESET}" if a1() else text
