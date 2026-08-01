import os
import random
from datetime import datetime

def countdown():
    os.system('cls' if os.name == 'nt' else 'clear')
    
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
    
    lights = ['*', '*', '*', '*', '*', '*']
    
    print("=" * 50)
    print("         CHRISTMAS COUNTDOWN TREE          ")
    print("=" * 50)
    print()
    
    print(f"  >>> DAYS UNTIL CHRISTMAS: {days:03d} days")
    print(f"  >>> {hours:02d}:{minutes:02d}:{seconds:02d}")
    print()
    print("  " + "-" * 46)
    print()
    
    for i, line in enumerate(tree):
        if i < len(tree) - 2:
            if i % 2 == 0:
                light = random.choice(lights)
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
    print("=" * 50)
    print("     ^^^ Santa is coming! ^^^")
    print("=" * 50)
    print()
    input("Press Enter to update countdown...")

while True:
    countdown()
