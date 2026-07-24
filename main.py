from menu import m1
import os
import sys

def r1():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        from display.banner import b1
        from display.panels import p1
        b1()
        i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
        p1("23 KOD", i1, "READY")
    except:
        print("+--- 23 KOD")
        print("| Starting...")
        print("------------------------------")
    m1()

if __name__ == "__main__":
    r1()
