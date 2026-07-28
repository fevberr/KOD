import json
from utils.colors import hex_to_ansi, is_hex_color

def a1():
    try:
        with open("cache/CSET.json", 'r') as f:
            return json.load(f)
    except:
        return {}

def a2(c):
    if c and isinstance(c, str):
        return hex_to_ansi(c)
    return ''

def p1(t1, c1, s1=""):
    c = a1()
    rs = '\033[0m'
    g = a2(c.get('primary', '#00ffcc'))
    y = a2(c.get('warning', '#ffaa00'))
    m = a2(c.get('tab', '#ff44ff'))
    w = a2(c.get('highlight', '#ffffff'))
    
    print(f"\n{g}+---{rs} {w}{t1}{rs}")
    l1 = c1.split('\n')
    for l2 in l1:
        if 'host:' in l2 or 'Port:' in l2:
            print(f"{g}|{rs} {w}{l2}{rs}")
        elif 'Ping:' in l2:
            print(f"{g}|{rs} {y}{l2}{rs}")
        elif 'device:' in l2 or 'system:' in l2:
            print(f"{g}|{rs} {m}{l2}{rs}")
        else:
            print(f"{g}|{rs} {w}{l2}{rs}")
    if s1:
        print(f"{g}|-{rs} {g}Status:{rs} {w}{s1}{rs}")
    print(f"{g}{'-' * 30}{rs}")
