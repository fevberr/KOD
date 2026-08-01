import os
import random
import time
import sys

def 1():
    os.system('cls' if os.name == 'nt' else 'clear')
    rs = '\033[0m'
    g = '\033[92m'
    r = '\033[91m'
    y = '\033[93m'
    c = '\033[96m'
    w = '\033[97m'
    m = '\033[95m'
    b = '\033[94m'
    o = '\033[38;5;208m'

    tree = [
        "                                    .!,            .!,",
        "                                   ~ 6 ~          ~ 6 ~",
        "                              .    ' i `  .-^-.   ' i `",
        "                            _.|,_   | |  / .-. \\   | |",
        "                             '|`   .|_|.| (-` ) | .|_|.",
        "                             / \\ ___)_(_|__`-'__|__)_(______",
        "                            /`,o\)_______________________o_(",
        "                           /_* ~_\\[___]___[___]___[___[_[\\`-.",
        "                           / o .'\\[_]___[___]___[___]_[___)`-)",
        "                          /_,~' *_\\_]                 [_[(  (",
        "                          /`. *  *\\_]                 [___\\ _\\",
        "                         /   `~. o \\]      ;( ( ;     [_[_]`-'",
        "                        /_ *    `~,_\\    (( )( ;(;    [___]",
        "                        /   o  *  ~'\\   /\\ /\\ /\\ /\\   [_[_]",
        "                       / *    .~~'  o\\  ||_||_||_||   [___]",
        "                      /_,.~~'`    *  _\\_||_||_||_||___[_[_]",
        "                      /`~..  o        \\:::::::::::::::::::::\\",
        "                     / *   `'~..   *   \\:::::::::::::::::::::\\",
        "                    /_     o    ``~~.,,_\\=========\\_/========='",
        "                    /  *      *     ..~'\\         _|_ .-_--.",
        "                   /*    o   _..~~`'*   o\\           ( (_)  )",
        "                   `-.__.~'`'   *   ___.-'            `----'",
        "                         \":-------:\"",
        "                      hjw  \\_____/"
    ]

    ornaments = ['*', '+', '·', 'o', 'O', '@', '#', '$', '%', '&', '?', '!', '~', '^', '<', '>', '=', ':', ';', '`', "'", '"', '|', '/', '\\', '(', ')', '[', ']', '{', '}']
    colors = [r, y, g, c, m, b, o, '\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[95m', '\033[94m']
    
    print(f"{r}╔═══════════════════════════════════════════════════════════════╗{rs}")
    print(f"{r}║{rs} {b}* {c}+ {g}o {y}O {m}@ {o}# {r}$ {b}% {c}& {g}? {y}! {m}~ {o}^ {r}< {c}> {g}= {y}: {m}; {o}` {r}' {b}\" {c}| {g}/ {m}\\ {r}( {y}) {o}[ {b}] {c}{ {g}} {rs}{r}║{rs}")
    print(f"{r}╚═══════════════════════════════════════════════════════════════╝{rs}")
    
    sparkles = ['*', '·', '°', '+', '~', '^']
    top_line = "        "
    for s in sparkles:
        color = random.choice(colors)
        top_line += f"{color}{s}{rs}  "
    print(f"  {top_line}")
    print()
    
    for i, line in enumerate(tree):
        if i < len(tree) - 3:
            line_list = list(line)
            num_deco = random.randint(2, 5)
            for _ in range(num_deco):
                pos = random.randint(10, len(line)-5)
                if pos < len(line_list) and line_list[pos] == ' ':
                    deco = random.choice(ornaments)
                    color = random.choice(colors)
                    line_list[pos] = f"{color}{deco}{rs}"
            print(f"  {''.join(line_list)}")
        else:
            print(f"  {line}")
    
    print(f"\n  {c}*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *{rs}")
    print(f"  {w}°  °  °  °  °  °  °  °  °  °  °  °  °  °  °  °  °  °  °  °{rs}")
    print(f"  {c}·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·{rs}")
    
    print(f"\n  {r}* {y}M {g}E {c}R {m}R {b}Y {o}* {r}C {y}H {g}R {m}I {b}S {o}T {r}M {y}A {g}S {c}! {b}* {o}H {r}A {y}P {g}P {c}Y {m}* {b}N {o}E {r}W {y}* {g}Y {c}E {m}A {b}R {o}! *{rs}")
    print(f"\n  {c}° {w}* {c}° {w}* {c}° {w}* {c}° {w}* {c}° {w}* {c}° {w}* {c}° {w}* {c}°{rs}")
    
    presents = [
        f"{r}┌─┐ {y}┌─┐ {g}┌─┐ {b}┌─┐ {m}┌─┐",
        f"{r}│$│ {y}│$│ {g}│$│ {b}│$│ {m}│$│",
        f"{r}└─┘ {y}└─┘ {g}└─┘ {b}└─┘ {m}└─┘"
    ]
    for present in presents:
        print(f"  {present}")
    
    garland = ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
    garland_colored = ''
    for g_char in garland:
        garland_colored += f"{random.choice(colors)}{g_char}{rs} "
    print(f"\n  {garland_colored}")
    
    print(f"\n  {c}* Decorations Used: {len(ornaments) * 5} *{rs}")
    print(f"  {g}@ Tree Height: {len(tree)} rows @{rs}")
    print(f"  {y}+ Snowflakes: {random.randint(50, 100)} +{rs}")
    print(f"  {m}~ Sparkles: {random.randint(30, 80)} ~{rs}")
    
    input(f"\n  {g}* Press Enter for more joy! *{rs}")
    
    greeting = "* MERRY CHRISTMAS & HAPPY NEW YEAR *"
    colors_cycle = [r, y, g, c, m, b, o]
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{r}╔{'═' * 45}╗{rs}")
        print(f"{r}║{rs}", end='')
        for i, char in enumerate(greeting):
            color = colors_cycle[i % len(colors_cycle)]
            print(f"{color}{char}{rs}", end='', flush=True)
            time.sleep(0.02)
        print(f"{r}║{rs}")
        print(f"{r}╚{'═' * 45}╝{rs}")
        
        print(f"\n  {c}*  {y}+  {g}°  {m}~  {b}@  {o}#  {r}$  {c}%  {y}&  {g}?  {m}!  {b}|  {o}/  {r}\\  *{rs}")
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.1)
    
    print(f"\n  {r}* {y}* {g}* {c}* {m}* {b}* {o}* {r}M {y}E {g}R {c}R {m}Y {b}* {o}C {r}H {y}R {g}I {c}S {m}T {b}M {o}A {r}S {y}! {g}* {c}* {m}* {b}* {o}* {r}* {y}* {g}*{rs}")
    print(f"\n  {c}~ {w}° {c}* {w}+ {c}~ {w}° {c}* {w}+ {c}~ {w}° {c}* {w}+ {c}~ {w}° {c}* {w}+ {c}~ {w}° {c}* {w}+{rs}")
    print(f"\n  {r}H {y}A {g}P {c}P {m}Y {b}* {o}N {r}E {y}W {g}* {c}Y {m}E {b}A {o}R {r}!{rs}")
    print(f"\n  {b}@  {c}~  {g}*  {y}+  {m}°  {o}#  {r}$  {b}%  {c}&  {g}?  {y}!  {m}|  {o}/  {r}\\  @{rs}")

__all__ = ['1']
