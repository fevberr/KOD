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
    class b1:
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
    return b1

if a1():
    _c = a2()
    G = _c.BG
    R = _c.BR
    C = _c.BC
    Y = _c.BY
    W = _c.BW
    GR = _c.GR
    B = _c.BB
    M = _c.BM
    RS = _c.RS
    D = _c.D
    BL = _c.B
else:
    G = R = C = Y = W = GR = B = M = RS = D = BL = ''

def c1(text, code):
    return f"{code}{text}{RS}" if a1() else text

def g1(text): return c1(text, G)
def r1(text): return c1(text, R)
def c2(text): return c1(text, C)
def y1(text): return c1(text, Y)
def w1(text): return c1(text, W)
def gr1(text): return c1(text, GR)
def b1(text): return c1(text, B)
def m1(text): return c1(text, M)
def d1(text): return f"{D}{text}{RS}" if a1() else text
def b2(text): return f"{BL}{text}{RS}" if a1() else text
