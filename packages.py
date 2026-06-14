PACKAGES = {
    "python-whois": "installed",
    "dnspython": "installed", 
    "requests": "installed",
    "beautifulsoup4": "installed",
    "socket-engine": "loaded",
    "packet-simulator": "loaded",
    "async-worker": "initialized",
    "kod-core": "ready"
}

def p1():
    print("+--- packages")
    for pkg, status in PACKAGES.items():
        print(f"|\n|- {pkg:<20} - {status}")
    print("|- kod-core           - ready\n")
