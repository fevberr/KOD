import platform
import socket
import subprocess
import os

TABS = {
    "Recon Tab": ["Port Scanner.py"],
    "example": ["a.py", "b.py", "c.py"],
    "coming": [],
}

def s1():
    return f"{platform.system()} {platform.release()}"

def d1():
    try:
        if platform.system() == "Linux":
            if os.path.exists("/system/build.prop"):
                r1 = subprocess.run(["getprop", "ro.product.model"], capture_output=True, text=True)
                if r1.stdout.strip():
                    return r1.stdout.strip()
            r1 = subprocess.run(["hostname"], capture_output=True, text=True)
            return r1.stdout.strip()
        elif platform.system() == "Windows":
            return platform.node()
        elif platform.system() == "Darwin":
            r1 = subprocess.run(["scutil", "--get", "ComputerName"], capture_output=True, text=True)
            return r1.stdout.strip() if r1.stdout else platform.node()
    except:
        pass
    return platform.node()

def h1():
    try:
        h2 = socket.gethostname()
        l1 = socket.gethostbyname(h2)
        return f"http://{l1}:{p2()}/"
    except:
        return "http://localhost:8080/"

def p2():
    return 8080

def p3():
    try:
        if platform.system() == "Windows":
            r1 = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
        else:
            r1 = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
        
        for l2 in r1.stdout.split('\n'):
            if "time=" in l2:
                t1 = l2.split('time=')[1].split()[0].replace('ms', '')
                return int(float(t1))
    except:
        pass
    return 108

def g1():
    return TABS

def g2(t1):
    return TABS.get(t1, [])

def a1(t1, m1):
    TABS[t1] = m1

def r1(t1):
    if t1 in TABS:
        del TABS[t1]

host = h1()
port = p2()
device = d1()
system = s1()
ping = p3()

def c1():
    return {
        "host": host,
        "port": port,
        "device": device,
        "system": system,
        "ping": ping,
        "tabs": TABS
    }
