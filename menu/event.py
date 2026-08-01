import os
import random
from datetime import datetime

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
    
    lights = ['Q', 'W', 'E', 'R', 'T', 'Y']
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
    
    print()
    input(f"{g}Press Enter to continue{rs}")

def countdown():
    os.system('cls' if os.name == 'nt' else 'clear')
    rs = '\033[0m'
    g = '\033[92m'
    r = '\033[91m'
    y = '\033[93m'
    c = '\033[96m'
    w = '\033[97m'
    
    now = datetime.now()
    current_year = now.year
    
    if now.month == 12 and now.day > 25:
        target_year = current_year + 1
    elif now.month > 12:
        target_year = current_year + 1
    else:
        target_year = current_year
    
    christmas = datetime(target_year, 12, 25, 0, 0, 0)
    difference = christmas - now
    
    days = difference.days
    hours = difference.seconds // 3600
    minutes = (difference.seconds % 3600) // 60
    seconds = difference.seconds % 60
    
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
        f"   {target_year - 1} - {target_year}   "
    ]
    
    lights = ['A', 'Q', 'W', 'J', 'S', 'N']
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[94m', '\033[95m', '\033[38;5;208m']
    
    print(f"  {g}Days until Christmas: {days:03d} days{rs}")
    print(f"  {y}Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}{rs}")
    print()
    print(f"  {c}{'─' * 46}{rs}")
    print()
    
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
    
    print()
    print()
    input(f"{g}Press Enter to continue{rs}")

__all__ = ['xmas', 'countdown']
