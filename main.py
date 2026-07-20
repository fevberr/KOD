from menu import m1
from display.banner import b1
from display.panels import p1
from config import host, port, device, system, ping
import os
import sys

def r1():
    os.system('cls' if os.name == 'nt' else 'clear')
    b1()
    i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
    p1("23 KOD", i1, "READY")
    m1()

if __name__ == "__main__":
    try:
        from boot import a5
        a5()
    except:
        r1()
