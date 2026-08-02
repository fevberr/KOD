import platform
import socket
import subprocess
import os
import glob

def a1():
    m = []
    if os.path.exists("modules"):
        for f in glob.glob("modules/*.py"):
            m.append(os.path.basename(f))
        for f in glob.glob("modules/*/*.py"):
            m.append(os.path.basename(f))
    return sorted(set(m))

TABS = {
    "Recon Tab": ["DNS lookup.py", "Port Scanner.py", "Reverse DNS.py", "Shodan lookup.py", "OSINT search.py", "Subdomain enumeration.py", "Whois Lookup.py"],
    
    
    "Web Enum Tab": ["Directory Brute Force.py", "Parameter Fuzzer.py"],
    
    
    "Exploit Tab": ["Hash Identifier.py", "Reverse Shell Generator.py"],
    
    
    "Aesthetic": ["Matrix Rain.py", "bad apple.py", "Glitch Effect.py", "test.py", "FPort Scanner.py", "FNetwork Sniffer.py"],
    
    
    "Utility Tab": ["JWT Decoder.py"]
}

def a2():
    return f"{platform.system()} {platform.release()}"

def a3():
    try:
        if platform.system() == "Linux":
            if os.path.exists("/system/build.prop"):
                r = subprocess.run(["getprop", "ro.product.model"], capture_output=True, text=True)
                if r.stdout.strip():
                    return r.stdout.strip()
            r = subprocess.run(["hostname"], capture_output=True, text=True)
            return r.stdout.strip()
        elif platform.system() == "Windows":
            return platform.node()
        elif platform.system() == "Darwin":
            r = subprocess.run(["scutil", "--get", "ComputerName"], capture_output=True, text=True)
            return r.stdout.strip() if r.stdout else platform.node()
    except:
        pass
    return platform.node()

def a4():
    try:
        h = socket.gethostname()
        i = socket.gethostbyname(h)
        return f"http://{i}:{a5()}/"
    except:
        return "http://localhost:8080/"

def a5():
    return 8080

def a6():
    try:
        if platform.system() == "Windows":
            r = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
        else:
            r = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
        for l in r.stdout.split('\n'):
            if "time=" in l:
                t = l.split('time=')[1].split()[0].replace('ms', '')
                return int(float(t))
    except:
        pass
    return 108

def a7():
    return TABS

def a8(t):
    return TABS.get(t, [])

host = a4()
port = a5()
device = a3()
system = a2()
ping = a6()
