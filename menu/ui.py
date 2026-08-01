import os
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    try:
        s = shutil.get_terminal_size()
        return s.columns, s.lines
    except:
        return 80, 24

def truncate(s, w):
    if len(s) > w:
        return s[:w-1] + "…"
    return s

def draw_banner(c, gr):
    try:
        from display.banner import a3 as b1
        b1()
    except Exception as e:
        print(f"{c}╔═══ 23 KOD")
        print(f"{gr}  ║ Banner error: {e}")

def draw_header(c, wc, y, m, g, host, port, ping, device, system, w):
    if w < 40:
        print(f"{c}╔═══ 23 KOD")
        print(f"{c}║ {wc}{truncate(host, 15)}")
        print(f"{c}║ {wc}Port: {port}")
        print(f"{c}║ {y}Ping: {ping}ms")
        print(f"{c}╚═══ {g}READY")
    elif w < 60:
        print(f"{c}╔═══ 23 KOD")
        print(f"{c}║ {wc}{truncate(host, 25)}")
        print(f"{c}║ {wc}Port: {port}")
        print(f"{c}║ {y}Ping: {ping}ms")
        print(f"{c}╚═══ {g}READY")
    else:
        print(f"{c}╔═══ 23 KOD")
        print(f"{c}║ {wc}Host: {host}")
        print(f"{c}║ {wc}Port: {port}")
        print(f"{c}║ {y}Ping: {ping}ms")
        print(f"{c}║ {m}Device: {device}")
        print(f"{c}║ {m}System: {system}")
        print(f"{c}╚═══ {g}Status: READY")

def draw_tabs(g, c, gr, n2, p4, w):
    rs = '\033[0m'
    tw = min(w - 4, 60)
    td = []
    for i, name in enumerate(n2):
        dn = truncate(name, max(3, (tw // max(1, len(n2))) - 1))
        if i == p4:
            td.append(f"{g}▸{rs}{c}{dn}{rs}{g}◂{rs}")
        else:
            td.append(f"{gr}┆{rs}{gr}{dn}{rs}")
    tl = ' '.join(td)
    if len(tl) > tw:
        td = []
        visible = max(1, min(len(n2), tw // 8))
        for i, name in enumerate(n2[:visible]):
            dn = truncate(name, max(3, (tw // visible) - 1))
            if i == p4:
                td.append(f"{g}▸{rs}{c}{dn}{rs}{g}◂{rs}")
            else:
                td.append(f"{gr}┆{rs}{gr}{dn}{rs}")
        if len(n2) > visible:
            td.append(f"{gr}…{rs}")
        tl = ' '.join(td)
    print(f"\n{g}╔═══ Menu{rs}")
    print(f"{g}║{rs} {c}Tabs:{rs} {tl}")
    print(f"{g}╠═══{rs}")

def draw_modules(g, y, c, gr, r, c2, h, w):
    rs = '\033[0m'
    if not c2:
        print(f"{g}║{rs} {r}No modules available{rs}")
    else:
        max_items = min(len(c2), max(1, h - 10))
        for i, m5 in enumerate(c2[:max_items], 1):
            dn = truncate(m5, max(1, w - 8))
            if w < 30:
                print(f"{g}║{rs} {y}{i}{rs}. {c}{dn}{rs}")
            else:
                print(f"{g}║{rs} {y}{i:2}{rs}. {c}{dn}{rs}")
        if len(c2) > max_items:
            print(f"{g}║{rs} {gr}... and {len(c2)-max_items} more{rs}")

def draw_footer(g, r, y, c, b, m, gr, w):
    rs = '\033[0m'
    print(f"{g}╠═══{rs}")
    if w < 30:
        print(f"{g}║{rs} {r}0{rs} {y}s{rs} {c}t{rs} {b}i{rs} {m}c{rs}")
        print(f"{g}║{rs} {gr}Exit Find Tabs Inst Color{rs}")
    elif w < 50:
        print(f"{g}║{rs} {r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t]{rs} Tabs  {b}[i]{rs} Install  {m}[c]{rs} Color")
    else:
        print(f"{g}║{rs} {r}[0]{rs} Exit  {y}[s]{rs} Search  {c}[t]{rs} Tabs  {b}[i]{rs} Install  {m}[c]{rs} Colors")
    print(f"{g}╚═══{rs}")
    print()

__all__ = ['clear_screen', 'get_terminal_size', 'draw_banner', 'draw_header', 'draw_tabs', 'draw_modules', 'draw_footer', 'truncate']
