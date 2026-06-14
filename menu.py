from utils.loader import l1
from loader import f1
import os
import sys

I1 = 5

def g1():
    m1 = []
    if os.path.exists("modules"):
        for f in os.listdir("modules"):
            if f.endswith((".py", ".lua")) and f != "__init__.py":
                m1.append(f)
    return sorted(m1)

def s2(m1, q1):
    if not q1:
        return m1
    return [x for x in m1 if q1.lower() in x.lower()]

def d2(m1, p4, t1):
    s3 = p4 * I1
    e1 = s3 + I1
    p5 = m1[s3:e1]
    
    print("\n* menu\n|")
    if not p5:
        print("|   No modules found")
    else:
        for i, mod in enumerate(p5, 1):
            print(f"| > {s3 + i}  | {mod}")
    
    print(f"|\n|- 0  Exit")
    print(f"|- s  Search")
    print(f"|- n  Next page | p  Previous page ({p4 + 1}/{t1})")
    print("------------------------")
    return p5

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        from display.banner import b1
        from display.panels import p1
        from config import h1, p2, d1, s1, p3
        b1()
        i1 = f"host:      {h1}\nPort:        {p2}\nPing:     {p3}\ndevice:   {d1}\nsystem:    {s1}"
        p1("23 KOD", i1, "READY")
        
        a1 = g1()
        f2 = s2(a1, q1)
        t1 = max(1, (len(f2) + I1 - 1) // I1)
        
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        
        if q1:
            print(f"\n[Search: {q1}] ({len(f2)} results)")
        
        p5 = d2(f2, p4, t1)
        
        c1 = input("Select option > ").strip().lower()
        
        if c1 == "0":
            print("Exiting...")
            break
        
        if c1 == "n":
            if p4 < t1 - 1:
                p4 += 1
            continue
        
        if c1 == "p":
            if p4 > 0:
                p4 -= 1
            continue
        
        if c1 == "s":
            q1 = input("Enter search term: ").strip()
            p4 = 0
            continue
        
        if not c1.isdigit():
            print("Invalid option")
            input("\nPress Enter to continue...")
            continue
        
        i2 = int(c1) - 1
        g2 = p4 * I1 + i2
        
        if 0 <= g2 < len(f2):
            n1 = f2[g2]
            f1(n1)
            l1(f"modules/{n1}")
            print(f"\nModule {n1} finished.")
            input("Press Enter to continue...")
        else:
            print("Invalid option")
            input("\nPress Enter to continue...")
