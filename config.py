import platform
import socket
import subprocess
import os

def get_system():
    return f"{platform.system()} {platform.release()}"

def get_device():
    try:
        if platform.system() == "Linux":
            if os.path.exists("/system/build.prop"):
                result = subprocess.run(["getprop", "ro.product.model"], capture_output=True, text=True)
                if result.stdout.strip():
                    return result.stdout.strip()
            result = subprocess.run(["hostname"], capture_output=True, text=True)
            return result.stdout.strip()
        elif platform.system() == "Windows":
            return platform.node()
        elif platform.system() == "Darwin":
            result = subprocess.run(["scutil", "--get", "ComputerName"], capture_output=True, text=True)
            return result.stdout.strip() if result.stdout else platform.node()
    except:
        pass
    return platform.node()

def get_host():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return f"http://{local_ip}:{get_port()}/"
    except:
        return "http://localhost:8080/"

def get_port():
    return 8080

def get_ping():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
        else:
            result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)
        
        for line in result.stdout.split('\n'):
            if "time=" in line:
                time_str = line.split('time=')[1].split()[0].replace('ms', '')
                return int(float(time_str))
    except:
        pass
    return 108

host = get_host()
port = get_port()
device = get_device()
system = get_system()
ping = get_ping()

def get_config():
    return {
        "host": host,
        "port": port,
        "device": device,
        "system": system,
        "ping": ping
    }
