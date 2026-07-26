from menu import m1
import os
import sys

def a1():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        from display.banner import b1
        from display.panels import p1
        b1()
        from config import host, port, device, system, ping
        i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
        p1("23 KOD", i1, "READY")
    except:
        print("+--- 23 KOD")
        print("| Starting...")
        print("------------------------------")
    m1()

if __name__ == "__main__":
    try:
        from boot import a11
        a11()
    except:
        a1()
