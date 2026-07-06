from config import host, port, device, system, ping
from display.banner import b1
from display.panels import p1
import os
import time

def show_module(module_name, status="READY"):
    os.system('cls' if os.name == 'nt' else 'clear')
    b1()
    i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}ms\ndevice:   {device}\nsystem:    {system}"
    p1(f"23 KOD :: [{module_name}]", i1, status)
    print("\n[+] Menu:")
    print("    (1) Run")
    print("    (2) run2")
    print("    (0) Exit")
    print("\n------------------------------")
    return input("Select > ").strip()
