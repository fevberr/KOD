from menu import m1
from display.banner import b1
from display.panels import p1
from config import h1, p2, d1, s1, p3
import os

def r1():
    os.system('cls' if os.name == 'nt' else 'clear')
    b1()
    
    i1 = f"host:      {h1}\nPort:        {p2}\nPing:     {p3}\ndevice:   {d1}\nsystem:    {s1}"
    p1("23 KOD", i1, "READY")
    
    m1()

if __name__ == "__main__":
    r1()
