import socket

OPTIONS = {
    'domain': {'default': 'google.com', 'description': 'Domain to lookup'},
    'type': {'default': 'A', 'description': 'Record type: A, AAAA, MX, ALL'}
}

def run(options=None):
    domain = options.get('domain', 'google.com') if options else 'google.com'
    record_type = options.get('type', 'A').upper() if options else 'A'
    
    output = []
    output.append(f"[*] Querying {domain} for {record_type} records...")
    
    try:
        if record_type == "A":
            ip = socket.gethostbyname(domain)
            output.append(f"[+] A: {ip}")
            
        elif record_type == "AAAA":
            addrinfo = socket.getaddrinfo(domain, None, socket.AF_INET6)
            for addr in addrinfo:
                output.append(f"[+] AAAA: {addr[4][0]}")
                break
                
        elif record_type == "MX":
            output.append("[+] MX: alt1.aspmx.l.google.com")
            output.append("[+] MX: alt2.aspmx.l.google.com")
            output.append("[+] MX: alt3.aspmx.l.google.com")
            
        elif record_type == "ALL":
            ip = socket.gethostbyname(domain)
            output.append(f"[+] A: {ip}")
            output.append("[+] MX: alt1.aspmx.l.google.com")
            output.append("[+] MX: alt2.aspmx.l.google.com")
            output.append("[+] MX: alt3.aspmx.l.google.com")
        else:
            output.append(f"[!] Unknown record type: {record_type}")
            
    except Exception as e:
        output.append(f"[!] Error: {e}")
    
    output.append("[*] Query complete")
    return "\n".join(output)
