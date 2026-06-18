from utils.loader import l1
from loader import f1
import os
import sys
import time
from config import g1, g2, host, port, device, system, ping

I1 = 5

def m2():
    m1 = []
    t1 = g1()
    for t2, m3 in t1.items():
        for m4 in m3:
            if m4 not in m1:
                m1.append(m4)
    return sorted(m1)

def n1():
    t1 = g1()
    return list(t1.keys())

def o1(p4):
    t1 = g1()
    n2 = list(t1.keys())
    if p4 < len(n2):
        return t1[n2[p4]]
    return []

def s2(m1, q1):
    if not q1:
        return m1
    return [x for x in m1 if q1.lower() in x.lower()]

def m1():
    p4 = 0
    q1 = ""
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        from display.banner import b1
        from display.panels import p1
        b1()
        i1 = f"host:      {host}\nPort:        {port}\nPing:     {ping}\ndevice:   {device}\nsystem:    {system}"
        p1("23 KOD", i1, "READY")
        
        n2 = n1()
        t1 = max(1, len(n2))
        
        if p4 >= t1:
            p4 = t1 - 1
        if p4 < 0:
            p4 = 0
        
        c2 = o1(p4)
        
        tab_display = []
        for i, name in enumerate(n2):
            if i == p4:
                tab_display.append(f"[{name}]")
            else:
                tab_display.append(f" {name} ")
        
        tab_line = ' '.join(tab_display)
        print(f"\n* menu | {tab_line}")
        print("|")
        if not c2:
            print("|   (coming soon...)")
        else:
            for i, m5 in enumerate(c2, 1):
                print(f"| > {i}  | {m5}")
        
        print(f"|\n|- 0  Exit")
        print(f"|- s  Search")
        print(f"|- t1, t2, t3... to switch tabs")
        print("------------------------")
        
        sys.stdout.flush()
        try:
            c1 = input("Select option > ").strip().lower()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        
        if c1 == "0":
            print("Exiting...")
            break
        
        if c1 == "s":
            q1 = input("Enter search term: ").strip()
            p4 = 0
            continue
        
        if c1.startswith('t') and len(c1) > 1:
            try:
                t2 = int(c1[1:])
                if 1 <= t2 <= t1:
                    p4 = t2 - 1
                    print(f"\nSwitched to tab: {n2[p4]}")
                    time.sleep(0.5)
                    continue
                else:
                    print(f"Tab {t2} doesn't exist (1-{t1})")
                    time.sleep(1)
                    continue
            except:
                print("Invalid tab number")
                time.sleep(1)
                continue
        
        if not c1.isdigit():
            print("Invalid option")
            time.sleep(1)
            continue
        
        i2 = int(c1) - 1
        c2 = o1(p4)
        
        if c2 and 0 <= i2 < len(c2):
            m5 = c2[i2]
            m6 = f"modules/{m5}"
            if os.path.exists(m6):
                f1(m5)
                l1(m6)
            else:
                print(f"\nModule {m5} not found!")
                print(f"Path: {m6}")
                input("Press Enter to continue...")
        else:
            if c2:
                print("Invalid option")
            else:
                print("This tab has no modules yet")
            time.sleep(1)
