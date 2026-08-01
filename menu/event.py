import os
import random

def xmas():
    os.system('cls' if os.name == 'nt' else 'clear')
    rs = '\033[0m'
    g = '\033[92m'
    r = '\033[91m'
    y = '\033[93m'
    c = '\033[96m'
    w = '\033[97m'
    m = '\033[95m'

    tree = [
        "        *        ",
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        " *************** ",
        "       |||       ",
        "       |||       ",
        "    MERRY XMAS   ",
        "   2024 - 2025   "
    ]

    lights = ['❆', '❆', '❆', '❆', '❆', '❆']
    colors = [r, y, g, c, m, '\033[38;5;208m']
    
    for i, line in enumerate(tree):
        if i < len(tree) - 2:
            if i % 2 == 0:
                light = random.choice(lights)
                color = random.choice(colors)
                pos = random.randint(2, len(line)-3)
                line_list = list(line)
                if pos < len(line_list) and line_list[pos] == ' ':
                    line_list[pos] = light
                print(f"  {''.join(line_list)}")
            else:
                print(f"  {line}")
        else:
            print(f"  {line}")
    
    input(f"{g}Press Enter to continue{rs}")

__all__ = ['xmas']
