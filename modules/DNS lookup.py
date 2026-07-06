def run():
    output = []
    
    target = input("Enter domain/IP (default: google.com): ").strip()
    if not target:
        target = "google.com"
    
    output.append(f"[*] DNS Lookup: {target}")
    output.append("=" * 40)
    
    try:
        import socket
        import dns.resolver
        
        output.append("[*] A Records:")
        try:
            answers = dns.resolver.resolve(target, 'A')
            for rdata in answers:
                output.append(f"[+] {rdata.address}")
        except:
            output.append("[-] None")
        
        output.append("\n[*] AAAA Records:")
        try:
            answers = dns.resolver.resolve(target, 'AAAA')
            for rdata in answers:
                output.append(f"[+] {rdata.address}")
        except:
            output.append("[-] None")
        
        output.append("\n[*] MX Records:")
        try:
            answers = dns.resolver.resolve(target, 'MX')
            for rdata in answers:
                output.append(f"[+] {rdata.preference} {rdata.exchange}")
        except:
            output.append("[-] None")
        
        output.append("\n[*] NS Records:")
        try:
            answers = dns.resolver.resolve(target, 'NS')
            for rdata in answers:
                output.append(f"[+] {rdata.target}")
        except:
            output.append("[-] None")
        
        output.append("\n[*] TXT Records:")
        try:
            answers = dns.resolver.resolve(target, 'TXT')
            for rdata in answers:
                output.append(f"[+] {rdata.strings}")
        except:
            output.append("[-] None")
        
        try:
            socket.inet_aton(target)
            output.append("\n[*] Reverse Lookup:")
            try:
                rev = dns.reversename.from_address(target)
                ans = dns.resolver.resolve(rev, "PTR")
                for rdata in ans:
                    output.append(f"[+] {rdata.target}")
            except:
                output.append("[-] None")
        except:
            pass
            
    except ImportError:
        output.append("[-] Install dnspython: pip install dnspython")
    except Exception as e:
        output.append(f"[-] Error: {str(e)}")
    
    output.append("\n" + "=" * 40)
    return "\n".join(output)
