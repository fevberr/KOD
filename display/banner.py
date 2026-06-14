import shutil
import os

def get_banner_width():
    try:
        terminal_width = shutil.get_terminal_size().columns
        return min(terminal_width, 80)
    except:
        return 80

def show_banner():
    width = get_banner_width()
    
    if width >= 80:
        banner = r"""
     ⢀⣤⡀⣀⣀⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣾⣿⣿⣿⣿⣷⣿⣷⣷⣶⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠈⠻⢿⠉⠉⠉⠙⠛⢻⣽⣿⣿⣿⣿⣶⡦⣀⣤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠲⠼⢿⠿⠾⠿⡿⠿⣿⣿⣶⣵⣧⣆⣠⣀⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠻⢟⣿⣿⣟⣟⣭⣿⣶⣐⣦⣤
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠉⠉⠁⠀
    ⣶⣿⣿⣿⣶⣤⣾⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠙⠀⠀⢠⡻⢾⣻⣿⣿⣠⣀⢀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⣿⣿⣭⣷⣶⠤
    ────────────────────────────────────
"""
    elif width >= 60:
        banner = r"""
     ⢀⣤⡀⣀⣀⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀
    ⣾⣿⣿⣿⣿⣷⣿⣷⣷⣶⣿⣿⣷⣄⠀⠀
    ⠈⠻⢿⠉⠉⠉⠙⠛⢻⣽⣿⣿⣿⣿⣶⡦
    ⠀⠀⠀⠀⠀⠀⠲⠼⢿⠿⠾⠿⡿⠿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠻
    ────────────────────────
"""
    else:
        banner = r"""
     ⢀⣤⡀⣀⣀⡀
    ⣾⣿⣿⣿⣿⣷⣿⣷⣷⣶
    ⠈⠻⢿⠉⠉⠉⠙⠛⢻⣽
    ⠀⠀⠀⠀⠀⠀⠲⠼⢿⠿
    ────────────────
"""
    
    print(banner)
    
    if width < 40:
        print("23 KOD")
        print("────────────────")
