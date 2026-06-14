from menu import menu
from display.banner import show_banner
from display.panels import draw_panel
from config import host, port, device, system, ping
import os

def run():
    os.system('clear' if os.name == 'posix' else 'cls')
    show_banner()
    
    info = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
    draw_panel("23 KOD", info, "READY")
    
    menu()

if __name__ == "__main__":
    run()
