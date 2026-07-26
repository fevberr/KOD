def run(options=None):
    if options:
        domain = options.get('domain', 'google.com')
        server = options.get('server', 'whois.verisign-grs.com')
        port = options.get('port', 43)
        timeout = options.get('timeout', 30)
        verbose = options.get('verbose', True)
        follow_referral = options.get('follow_referral', True)
        max_redirects = options.get('max_redirects', 5)
        cache_results = options.get('cache_results', False)
        cache_ttl = options.get('cache_ttl', 3600)
        output_format = options.get('output_format', 'detailed')
        filter_regex = options.get('filter_regex', '')
        show_raw = options.get('show_raw', False)
        extract_contacts = options.get('extract_contacts', True)
        dns_lookup = options.get('dns_lookup', True)
        whois_history = options.get('whois_history', False)
        rate_limit = options.get('rate_limit', 1.0)
        user_agent = options.get('user_agent', 'KOD-Whois-Client/2.0')
        proxy = options.get('proxy', '')
        parallel_queries = options.get('parallel_queries', False)
        save_to_file = options.get('save_to_file', '')
        tld_specific = options.get('tld_specific', True)
        parse_detailed = options.get('parse_detailed', True)
        validate_domain = options.get('validate_domain', True)
        retry_attempts = options.get('retry_attempts', 3)
        retry_delay = options.get('retry_delay', 2)
        output_csv = options.get('output_csv', False)
        csv_file = options.get('csv_file', 'whois_results.csv')
        ip_lookup = options.get('ip_lookup', False)
        asn_lookup = options.get('asn_lookup', False)
        geolocation = options.get('geolocation', False)
        ssl_cert = options.get('ssl_cert', False)
        http_headers = options.get('http_headers', False)
        subdomain_scan = options.get('subdomain_scan', False)
        ports_scan = options.get('ports_scan', False)
        network_range = options.get('network_range', False)
        reverse_dns = options.get('reverse_dns', False)
        domain_age = options.get('domain_age', True)
        encoding = options.get('encoding', 'utf-8')
        buffer_size = options.get('buffer_size', 16384)
        max_response_size = options.get('max_response_size', 5000000)
    else:
        domain = 'google.com'
        server = 'whois.verisign-grs.com'
        port = 43
        timeout = 30
        verbose = True
        follow_referral = True
        max_redirects = 5
        cache_results = False
        cache_ttl = 3600
        output_format = 'detailed'
        filter_regex = ''
        show_raw = False
        extract_contacts = True
        dns_lookup = True
        whois_history = False
        rate_limit = 1.0
        user_agent = 'KOD-Whois-Client/2.0'
        proxy = ''
        parallel_queries = False
        save_to_file = ''
        tld_specific = True
        parse_detailed = True
        validate_domain = True
        retry_attempts = 3
        retry_delay = 2
        output_csv = False
        csv_file = 'whois_results.csv'
        ip_lookup = False
        asn_lookup = False
        geolocation = False
        ssl_cert = False
        http_headers = False
        subdomain_scan = False
        ports_scan = False
        network_range = False
        reverse_dns = False
        domain_age = True
        encoding = 'utf-8'
        buffer_size = 16384
        max_response_size = 5000000
    
    output = []
    cache_store = {}
    referral_chain = []
    parsed_data = {}
    results_summary = {}
    
    output.append("│ ●  Starting WHOIS Lookup")
    output.append("│ ●  Target: " + domain)
    output.append("│ ●  Server: " + server + ":" + str(port))
    output.append("│ ●  Timeout: " + str(timeout) + "s, Retries: " + str(retry_attempts))
    
    def _1():
        try:
            import re, sys, os, json, time, socket, ssl, hashlib, base64, ipaddress
            import threading, queue, csv, io, gzip, zlib, binascii, struct
            import random, string, urllib.request, urllib.parse, urllib.error
            import http.client, email.parser, email.policy, xml.etree.ElementTree
            import configparser, logging
            from collections import defaultdict, Counter, OrderedDict
            from datetime import datetime, timedelta
            from concurrent.futures import ThreadPoolExecutor, as_completed
            from functools import lru_cache
            return {
                're': re, 'sys': sys, 'os': os, 'json': json, 'time': time,
                'socket': socket, 'ssl': ssl, 'hashlib': hashlib, 'base64': base64,
                'ipaddress': ipaddress, 'threading': threading, 'queue': queue,
                'csv': csv, 'io': io, 'gzip': gzip, 'zlib': zlib,
                'binascii': binascii, 'struct': struct, 'random': random,
                'string': string, 'urllib': urllib, 'http': http,
                'email': email, 'xml': xml, 'configparser': configparser,
                'logging': logging, 'defaultdict': defaultdict, 'Counter': Counter,
                'OrderedDict': OrderedDict, 'datetime': datetime, 'timedelta': timedelta,
                'ThreadPoolExecutor': ThreadPoolExecutor, 'as_completed': as_completed,
                'lru_cache': lru_cache
            }
        except Exception as e:
            output.append("│ [!] Import error: " + str(e))
            return None
    
    libs = _1()
    if not libs:
        output.append("│ [!] Failed to load libraries")
        output.append("│ ●  Complete")
        return "\n".join(output)
    
    def _2(domain_str):
        try:
            pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
            return bool(libs['re'].match(pattern, domain_str))
        except:
            return False
    
    def _3(domain_str):
        try:
            tld_map = {
                '.com': 'whois.verisign-grs.com', '.net': 'whois.verisign-grs.com',
                '.org': 'whois.pir.org', '.info': 'whois.afilias.net',
                '.biz': 'whois.neulevel.biz', '.edu': 'whois.educause.edu',
                '.gov': 'whois.nic.gov', '.mil': 'whois.nic.mil',
                '.int': 'whois.iana.org', '.eu': 'whois.eu',
                '.uk': 'whois.nic.uk', '.de': 'whois.denic.de',
                '.fr': 'whois.nic.fr', '.jp': 'whois.jprs.jp',
                '.cn': 'whois.cnnic.cn', '.ru': 'whois.ripn.net',
                '.it': 'whois.nic.it', '.nl': 'whois.domain-registry.nl',
                '.se': 'whois.iis.se', '.no': 'whois.norid.no',
                '.dk': 'whois.dk-hostmaster.dk', '.fi': 'whois.fi',
                '.be': 'whois.dns.be', '.at': 'whois.nic.at',
                '.ch': 'whois.nic.ch', '.es': 'whois.nic.es',
                '.pt': 'whois.dns.pt', '.pl': 'whois.dns.pl',
                '.cz': 'whois.nic.cz', '.sk': 'whois.sk-nic.sk',
                '.hu': 'whois.nic.hu', '.gr': 'whois.gr',
                '.il': 'whois.isoc.org.il', '.in': 'whois.inregistry.net',
                '.io': 'whois.nic.io', '.to': 'whois.tonic.to',
                '.tv': 'whois.nic.tv', '.cc': 'whois.nic.cc',
                '.ws': 'whois.website.ws', '.name': 'whois.nic.name',
                '.pro': 'whois.registry.pro', '.mobi': 'whois.mtld.mobi',
                '.tel': 'whois.nic.tel', '.asia': 'whois.nic.asia',
                '.cat': 'whois.cat', '.jobs': 'whois.nic.jobs',
                '.travel': 'whois.nic.travel', '.xxx': 'whois.nic.xxx',
                '.aero': 'whois.aero', '.coop': 'whois.nic.coop',
                '.museum': 'whois.nic.museum', '.app': 'whois.nic.google',
                '.dev': 'whois.nic.google', '.page': 'whois.nic.google'
            }
            for tld, whois_server in tld_map.items():
                if domain_str.lower().endswith(tld):
                    return whois_server
            return None
        except:
            return None
    
    def _4(domain_str, server_str, port_int):
        try:
            for attempt in range(retry_attempts):
                try:
                    sock = libs['socket'].socket(libs['socket'].AF_INET, libs['socket'].SOCK_STREAM)
                    sock.settimeout(timeout)
                    
                    if proxy:
                        parsed = libs['urllib'].parse.urlparse(proxy)
                        if parsed.netloc:
                            proxy_host = parsed.hostname
                            proxy_port = parsed.port or 8080
                            sock.connect((proxy_host, proxy_port))
                            connect_str = "CONNECT " + server_str + ":" + str(port_int) + " HTTP/1.1\r\nHost: " + server_str + "\r\nUser-Agent: " + user_agent + "\r\n\r\n"
                            sock.send(connect_str.encode())
                            response = sock.recv(1024)
                            if b"200" not in response:
                                sock.close()
                                if attempt < retry_attempts - 1:
                                    libs['time'].sleep(retry_delay)
                                    continue
                                return None, "Proxy connection failed"
                        else:
                            sock.connect((server_str, port_int))
                    else:
                        sock.connect((server_str, port_int))
                    
                    if port_int == 443:
                        context = libs['ssl'].create_default_context()
                        context.check_hostname = False
                        context.verify_mode = libs['ssl'].CERT_NONE
                        sock = context.wrap_socket(sock, server_hostname=server_str)
                    
                    query = domain_str + "\r\n"
                    sock.send(query.encode(encoding))
                    
                    response = b""
                    total_size = 0
                    while True:
                        chunk = sock.recv(buffer_size)
                        if not chunk:
                            break
                        response += chunk
                        total_size += len(chunk)
                        if total_size > max_response_size:
                            response += b"\n[...TRUNCATED...]"
                            break
                    
                    sock.close()
                    
                    try:
                        decoded = response.decode(encoding, errors='ignore')
                    except:
                        decoded = response.decode('latin-1', errors='ignore')
                    
                    if not decoded.strip():
                        if attempt < retry_attempts - 1:
                            libs['time'].sleep(retry_delay)
                            continue
                        return None, "Empty response"
                    
                    return decoded, None
                    
                except libs['socket'].timeout:
                    if attempt < retry_attempts - 1:
                        libs['time'].sleep(retry_delay)
                        continue
                    return None, "Timeout after " + str(timeout) + "s"
                except libs['socket'].gaierror:
                    return None, "Invalid server: " + server_str
                except ConnectionRefusedError:
                    return None, "Connection refused"
                except Exception as e:
                    if attempt < retry_attempts - 1:
                        libs['time'].sleep(retry_delay)
                        continue
                    return None, "Error: " + str(e)
            
            return None, "All retry attempts failed"
        except Exception as e:
            return None, "Fatal error: " + str(e)
    
    def _5(raw_data):
        try:
            lines = raw_data.split('\n')
            result = []
            for line in lines:
                line = line.strip()
                if line:
                    result.append(line)
                    if len(result) > 50000:
                        result.append("[...TRUNCATED...]")
                        break
            return result
        except:
            return []
    
    def _6(data_lines):
        try:
            patterns = [
                r'Referral[:\s]+([^\s]+)',
                r'Whois Server[:\s]+([^\s]+)',
                r'Registrar WHOIS Server[:\s]+([^\s]+)',
                r'whois[:\s]+([^\s]+)',
                r'Referral URL[:\s]+([^\s]+)'
            ]
            for line in data_lines:
                for pattern in patterns:
                    match = libs['re'].search(pattern, line, libs['re'].IGNORECASE)
                    if match:
                        candidate = match.group(1).strip()
                        if candidate and '://' not in candidate:
                            if candidate.startswith('whois.') or '.' in candidate:
                                if ' ' not in candidate and '\t' not in candidate:
                                    return candidate
            return None
        except:
            return None
    
    def _7(data_lines):
        try:
            parsed = {
                'domain_name': [], 'registrar': [], 'creation_date': [],
                'expiry_date': [], 'updated_date': [], 'name_servers': [],
                'registrant': [], 'admin': [], 'tech': [], 'billing': [],
                'status': [], 'dnssec': [], 'registrant_email': [],
                'admin_email': [], 'tech_email': [], 'registrant_phone': [],
                'admin_phone': [], 'tech_phone': [], 'registrant_organization': [],
                'admin_organization': [], 'tech_organization': [],
                'registrant_country': [], 'admin_country': [], 'tech_country': [],
                'registrant_address': [], 'admin_address': [], 'tech_address': [],
                'raw_fields': {}, 'whois_server': [], 'registry_domain_id': [],
                'registrar_iana': [], 'registrar_url': [], 'registrar_abuse_email': [],
                'registrar_abuse_phone': []
            }
            
            date_formats = [
                '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d',
                '%d-%b-%Y', '%b %d %Y', '%d/%m/%Y', '%m/%d/%Y',
                '%Y.%m.%d', '%d.%m.%Y', '%Y%m%d'
            ]
            
            for line in data_lines:
                if ':' in line:
                    parts = line.split(':', 1)
                    key = parts[0].strip().lower() if parts else ''
                    value = parts[1].strip() if len(parts) > 1 else ''
                    
                    if not key or not value:
                        continue
                    
                    if 'domain name' in key or 'domain:' in key:
                        parsed['domain_name'].append(value)
                    elif 'registrar' in key and 'whois' not in key and 'server' not in key:
                        parsed['registrar'].append(value)
                    elif 'creation date' in key or 'created' in key:
                        parsed['creation_date'].append(value)
                    elif 'expiry date' in key or 'expiration' in key:
                        parsed['expiry_date'].append(value)
                    elif 'updated date' in key or 'last modified' in key:
                        parsed['updated_date'].append(value)
                    elif 'name server' in key or 'nameserver' in key:
                        if value not in parsed['name_servers']:
                            parsed['name_servers'].append(value)
                    elif 'registrant' in key and 'email' not in key and 'phone' not in key:
                        parsed['registrant'].append(value)
                    elif 'admin' in key and 'email' not in key and 'phone' not in key:
                        parsed['admin'].append(value)
                    elif 'tech' in key and 'email' not in key and 'phone' not in key:
                        parsed['tech'].append(value)
                    elif 'status' in key:
                        parsed['status'].append(value)
                    elif 'dnssec' in key:
                        parsed['dnssec'].append(value)
                    elif 'registrant email' in key or 'registrant e-mail' in key:
                        parsed['registrant_email'].append(value)
                    elif 'admin email' in key or 'admin e-mail' in key:
                        parsed['admin_email'].append(value)
                    elif 'tech email' in key or 'tech e-mail' in key:
                        parsed['tech_email'].append(value)
                    elif 'registrant phone' in key or 'registrant telephone' in key:
                        parsed['registrant_phone'].append(value)
                    elif 'admin phone' in key or 'admin telephone' in key:
                        parsed['admin_phone'].append(value)
                    elif 'tech phone' in key or 'tech telephone' in key:
                        parsed['tech_phone'].append(value)
                    elif 'registrant organization' in key:
                        parsed['registrant_organization'].append(value)
                    elif 'admin organization' in key:
                        parsed['admin_organization'].append(value)
                    elif 'tech organization' in key:
                        parsed['tech_organization'].append(value)
                    elif 'registrant country' in key:
                        parsed['registrant_country'].append(value)
                    elif 'admin country' in key:
                        parsed['admin_country'].append(value)
                    elif 'tech country' in key:
                        parsed['tech_country'].append(value)
                    elif 'registry domain id' in key:
                        parsed['registry_domain_id'].append(value)
                    elif 'iana id' in key:
                        parsed['registrar_iana'].append(value)
                    elif 'abuse email' in key:
                        parsed['registrar_abuse_email'].append(value)
                    elif 'abuse phone' in key:
                        parsed['registrar_abuse_phone'].append(value)
                    
                    parsed['raw_fields'][key] = value
            
            return parsed
        except:
            return {'raw_fields': {}}
    
    def _8(data_lines, pattern):
        try:
            if not pattern:
                return data_lines
            regex = libs['re'].compile(pattern, libs['re'].IGNORECASE)
            return [line for line in data_lines if regex.search(line)]
        except:
            return data_lines
    
    def _9():
        try:
            dns_data = {}
            try:
                import dns.resolver
                import dns.reversename
                
                dns_data['a_records'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'A')
                    dns_data['a_records'] = [str(rdata) for rdata in answers]
                except:
                    pass
                
                dns_data['aaaa_records'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'AAAA')
                    dns_data['aaaa_records'] = [str(rdata) for rdata in answers]
                except:
                    pass
                
                dns_data['mx_records'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'MX')
                    dns_data['mx_records'] = [str(rdata.exchange) + " (priority: " + str(rdata.preference) + ")" for rdata in answers]
                except:
                    pass
                
                dns_data['ns_records'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'NS')
                    dns_data['ns_records'] = [str(rdata) for rdata in answers]
                except:
                    pass
                
                dns_data['txt_records'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'TXT')
                    dns_data['txt_records'] = [''.join(rdata.strings) for rdata in answers]
                except:
                    pass
                
                dns_data['cname'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'CNAME')
                    dns_data['cname'] = [str(rdata) for rdata in answers]
                except:
                    pass
                
                dns_data['soa'] = []
                try:
                    answers = dns.resolver.resolve(domain, 'SOA')
                    dns_data['soa'] = [str(rdata) for rdata in answers]
                except:
                    pass
                
                dns_data['ptr_records'] = []
                if dns_data['a_records']:
                    try:
                        for ip in dns_data['a_records'][:3]:
                            rev = dns.reversename.from_address(ip)
                            ptr = dns.resolver.resolve(rev, 'PTR')
                            dns_data['ptr_records'].extend([str(rdata) for rdata in ptr])
                    except:
                        pass
                
            except ImportError:
                try:
                    import socket
                    try:
                        ips = socket.gethostbyname_ex(domain)[2]
                        dns_data['a_records'] = ips
                    except:
                        pass
                except:
                    pass
            
            return dns_data
        except:
            return {}
    
    def _10(whois_data):
        try:
            contacts = {
                'emails': [], 'phones': [], 'urls': [],
                'names': [], 'ip_addresses': [], 'domains': []
            }
            
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            phone_pattern = r'\+?[\d\s\-()]{10,20}'
            url_pattern = r'https?://[^\s/$.?#].[^\s]*'
            ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
            
            for line in whois_data:
                contacts['emails'].extend(libs['re'].findall(email_pattern, line))
                contacts['phones'].extend(libs['re'].findall(phone_pattern, line))
                contacts['urls'].extend(libs['re'].findall(url_pattern, line, libs['re'].IGNORECASE))
                contacts['ip_addresses'].extend(libs['re'].findall(ip_pattern, line))
                
                if 'name' in line.lower() and ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) > 1:
                        val = parts[1].strip()
                        if len(val) > 2 and len(val) < 100 and not val.isdigit():
                            contacts['names'].append(val)
            
            for key in contacts:
                contacts[key] = list(set(contacts[key]))
            
            return contacts
        except:
            return {'emails': [], 'phones': [], 'urls': [], 'names': [], 'ip_addresses': [], 'domains': []}
    
    def _11(ip_addr):
        try:
            geo_data = {}
            try:
                import requests
                response = requests.get('http://ip-api.com/json/' + ip_addr, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    geo_data = {
                        'country': data.get('country', ''),
                        'region': data.get('regionName', ''),
                        'city': data.get('city', ''),
                        'isp': data.get('isp', ''),
                        'org': data.get('org', ''),
                        'timezone': data.get('timezone', '')
                    }
            except:
                pass
            return geo_data
        except:
            return {}
    
    def _12(ip_addr):
        try:
            asn_data = {}
            try:
                import requests
                response = requests.get('http://ip-api.com/json/' + ip_addr, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    as_data = data.get('as', '')
                    asn_data = {
                        'asn': as_data.split(' ')[0] if as_data else '',
                        'org': data.get('org', ''),
                        'isp': data.get('isp', '')
                    }
            except:
                pass
            return asn_data
        except:
            return {}
    
    def _13(domain_str):
        try:
            cert_data = {}
            try:
                context = libs['ssl'].create_default_context()
                with libs['socket'].create_connection((domain_str, 443), timeout=10) as sock:
                    with context.wrap_socket(sock, server_hostname=domain_str) as ssock:
                        cert = ssock.getpeercert()
                        cert_data = {
                            'subject': dict(x[0] for x in cert.get('subject', [])),
                            'issuer': dict(x[0] for x in cert.get('issuer', [])),
                            'not_before': cert.get('notBefore', ''),
                            'not_after': cert.get('notAfter', ''),
                            'serial_number': cert.get('serialNumber', '')
                        }
            except:
                pass
            return cert_data
        except:
            return {}
    
    def _14(domain_str):
        try:
            headers = {}
            try:
                req = libs['urllib'].request.Request('http://' + domain_str, headers={'User-Agent': user_agent})
                response = libs['urllib'].request.urlopen(req, timeout=10)
                headers = dict(response.headers)
                headers['status_code'] = response.getcode()
            except:
                try:
                    req = libs['urllib'].request.Request('https://' + domain_str, headers={'User-Agent': user_agent})
                    response = libs['urllib'].request.urlopen(req, timeout=10)
                    headers = dict(response.headers)
                    headers['status_code'] = response.getcode()
                except:
                    pass
            return headers
        except:
            return {}
    
    def _15(domain_str):
        try:
            subdomains = ['www', 'mail', 'ftp', 'test', 'dev', 'staging', 'api', 'app', 'blog', 'shop', 'admin', 'secure', 'portal', 'dns', 'ns1', 'ns2', 'mx', 'smtp', 'pop', 'imap', 'webmail', 'cpanel', 'whm', 'mysql', 'db', 'server', 'vpn', 'proxy', 'cdn', 'static', 'media', 'assets', 'images', 'css', 'js', 'files', 'download', 'upload', 'support', 'help', 'docs', 'wiki', 'forum', 'news', 'video', 'music', 'stream', 'cloud', 'host', 'remote', 'office', 'internal', 'external', 'demo', 'sandbox', 'qa', 'prod', 'production', 'stage', 'beta', 'alpha']
            found = []
            for sub in subdomains:
                try:
                    test_domain = sub + '.' + domain_str
                    libs['socket'].gethostbyname(test_domain)
                    found.append(test_domain)
                except:
                    continue
            return found
        except:
            return []
    
    def _16(domain_str):
        try:
            common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017]
            open_ports = []
            for port in common_ports:
                try:
                    sock = libs['socket'].socket(libs['socket'].AF_INET, libs['socket'].SOCK_STREAM)
                    sock.settimeout(2)
                    result = sock.connect_ex((domain_str, port))
                    if result == 0:
                        open_ports.append(port)
                    sock.close()
                except:
                    continue
            return open_ports
        except:
            return []
    
    def _17(ip_str):
        try:
            net_data = {}
            try:
                ip_obj = libs['ipaddress'].ip_address(ip_str)
                if ip_obj.version == 4:
                    net = libs['ipaddress'].ip_network(ip_str + '/24', strict=False)
                    net_data['network'] = str(net)
                    net_data['netmask'] = str(net.netmask)
                    net_data['broadcast'] = str(net.broadcast_address)
                else:
                    net = libs['ipaddress'].ip_network(ip_str + '/64', strict=False)
                    net_data['network'] = str(net)
                    net_data['netmask'] = str(net.netmask)
            except:
                pass
            return net_data
        except:
            return {}
    
    def _18(domain_str):
        try:
            age_data = {}
            try:
                import whois
                w = whois.whois(domain_str)
                if w.creation_date:
                    creation = w.creation_date
                    if isinstance(creation, list):
                        creation = creation[0]
                    if isinstance(creation, libs['datetime']):
                        age = libs['datetime'].now() - creation
                        age_data['created'] = creation.strftime('%Y-%m-%d %H:%M:%S')
                        age_data['days_old'] = age.days
                        age_data['years_old'] = round(age.days / 365.25, 2)
                
                if w.expiration_date:
                    expiry = w.expiration_date
                    if isinstance(expiry, list):
                        expiry = expiry[0]
                    if isinstance(expiry, libs['datetime']):
                        age_data['expires'] = expiry.strftime('%Y-%m-%d %H:%M:%S')
                        days_left = (expiry - libs['datetime'].now()).days
                        age_data['days_left'] = days_left
                        if days_left < 30 and days_left > 0:
                            age_data['expiry_warning'] = 'Expires in ' + str(days_left) + ' days!'
                        elif days_left <= 0:
                            age_data['expiry_warning'] = 'DOMAIN EXPIRED!'
            except:
                pass
            return age_data
        except:
            return {}
    
    if validate_domain and not _2(domain):
        output.append("│ [!] Invalid domain format: " + domain)
        output.append("│ ●  Complete")
        return "\n".join(output)
    
    tld_server = None
    if tld_specific:
        tld_server = _3(domain)
        if tld_server:
            output.append("│ ●  TLD-specific server: " + tld_server)
            server = tld_server
    
    output.append("│ ●  Connecting to: " + server + ":" + str(port))
    output.append("│ ●  Retry attempts: " + str(retry_attempts))
    
    raw_response, error = _4(domain, server, port)
    
    if error:
        output.append("│ [!] Query failed: " + error)
        if tld_server and server != tld_server:
            output.append("│ ●  Attempting fallback")
            raw_response, error = _4(domain, server, port)
            if error:
                output.append("│ [!] Fallback failed: " + error)
                output.append("│ ●  Complete")
                return "\n".join(output)
        else:
            output.append("│ ●  Complete")
            return "\n".join(output)
    
    output.append("│ ●  Query successful")
    output.append("│ ●  Response size: " + str(len(raw_response)) + " bytes")
    
    data_lines = _5(raw_response)
    output.append("│ ●  Parsed " + str(len(data_lines)) + " lines")
    
    if filter_regex:
        data_lines = _8(data_lines, filter_regex)
        output.append("│ ●  Filtered: " + str(len(data_lines)) + " lines")
    
    if show_raw:
        output.append("│")
        output.append("│ ●  Raw Response:")
        output.append("│ ──────────────────────────────")
        for line in data_lines[:200]:
            output.append("│ " + line)
        if len(data_lines) > 200:
            output.append("│ ... (" + str(len(data_lines) - 200) + " more)")
        output.append("│ ──────────────────────────────")
        output.append("│")
    
    parsed_info = {}
    if parse_detailed:
        parsed_info = _7(data_lines)
        output.append("│ ●  Detailed parsing completed")
        output.append("│ ●  Fields found: " + str(len(parsed_info.get('raw_fields', {}))))
        output.append("│")
        
        if parsed_info.get('domain_name'):
            output.append("│ Domain: " + ", ".join(parsed_info['domain_name'][:3]))
            results_summary['domain'] = parsed_info['domain_name'][0] if parsed_info['domain_name'] else domain
        else:
            results_summary['domain'] = domain
        
        if parsed_info.get('registrar'):
            output.append("│ Registrar: " + ", ".join(parsed_info['registrar'][:3]))
            results_summary['registrar'] = parsed_info['registrar'][0] if parsed_info['registrar'] else ''
        
        if parsed_info.get('creation_date'):
            output.append("│ Created: " + ", ".join(parsed_info['creation_date'][:3]))
            results_summary['created'] = parsed_info['creation_date'][0] if parsed_info['creation_date'] else ''
        
        if parsed_info.get('expiry_date'):
            output.append("│ Expires: " + ", ".join(parsed_info['expiry_date'][:3]))
            results_summary['expires'] = parsed_info['expiry_date'][0] if parsed_info['expiry_date'] else ''
        
        if parsed_info.get('updated_date'):
            output.append("│ Updated: " + ", ".join(parsed_info['updated_date'][:3]))
        
        if parsed_info.get('name_servers'):
            output.append("│ Name Servers:")
            for ns in parsed_info['name_servers'][:10]:
                output.append("│   " + ns)
            results_summary['nameservers'] = len(parsed_info['name_servers'])
        
        if parsed_info.get('status'):
            output.append("│ Status:")
            for status in parsed_info['status'][:10]:
                output.append("│   " + status)
        
        if parsed_info.get('dnssec'):
            output.append("│ DNSSEC: " + ", ".join(parsed_info['dnssec']))
        
        if parsed_info.get('registrant'):
            output.append("│ Registrant: " + ", ".join(parsed_info['registrant'][:3]))
        if parsed_info.get('registrant_organization'):
            output.append("│ Registrant Org: " + ", ".join(parsed_info['registrant_organization'][:3]))
        if parsed_info.get('registrant_country'):
            output.append("│ Registrant Country: " + ", ".join(parsed_info['registrant_country']))
        
        if parsed_info.get('registry_domain_id'):
            output.append("│ Registry ID: " + ", ".join(parsed_info['registry_domain_id']))
        if parsed_info.get('registrar_iana'):
            output.append("│ IANA ID: " + ", ".join(parsed_info['registrar_iana']))
        if parsed_info.get('registrar_abuse_email'):
            output.append("│ Abuse Email: " + ", ".join(parsed_info['registrar_abuse_email']))
        
        output.append("│")
    
    contacts = {}
    if extract_contacts:
        contacts = _10(data_lines)
        output.append("│ ●  Contact Information:")
        if contacts.get('emails'):
            output.append("│   Emails (" + str(len(contacts['emails'])) + "):")
            for email in contacts['emails'][:10]:
                output.append("│     " + email)
        if contacts.get('phones'):
            output.append("│   Phones (" + str(len(contacts['phones'])) + "):")
            for phone in contacts['phones'][:10]:
                output.append("│     " + phone)
        if contacts.get('urls'):
            output.append("│   URLs:")
            for url in contacts['urls'][:5]:
                output.append("│     " + url[:100])
        output.append("│")
    
    referral_server = None
    if follow_referral and len(referral_chain) < max_redirects:
        referral_server = _6(data_lines)
        if referral_server and referral_server != server:
            output.append("│ ●  Referral: " + referral_server)
            referral_chain.append(referral_server)
            
            refer_data, refer_error = _4(domain, referral_server, port)
            if not refer_error and refer_data:
                output.append("│ ●  Referral data retrieved")
                refer_lines = _5(refer_data)
                if filter_regex:
                    refer_lines = _8(refer_lines, filter_regex)
                output.append("│ ●  Referral lines: " + str(len(refer_lines)))
                
                if parse_detailed:
                    refer_parsed = _7(refer_lines)
                    if refer_parsed.get('domain_name'):
                        output.append("│   Referral Domain: " + ", ".join(refer_parsed['domain_name'][:3]))
                    if refer_parsed.get('registrar'):
                        output.append("│   Referral Registrar: " + ", ".join(refer_parsed['registrar'][:3]))
                
                for line in refer_lines[:20]:
                    output.append("│ " + line)
                if len(refer_lines) > 20:
                    output.append("│ ... (" + str(len(refer_lines) - 20) + " more)")
            else:
                output.append("│ [!] Referral failed: " + (refer_error or "Unknown"))
    
    dns_data = {}
    if dns_lookup:
        output.append("│ ●  DNS lookup for " + domain)
        try:
            dns_data = _9()
            output.append("│ ●  DNS completed")
            if dns_data.get('a_records'):
                output.append("│   A Records: " + ", ".join(dns_data['a_records'][:5]))
                results_summary['ip_addresses'] = dns_data['a_records'][:3]
                
                if ip_lookup or asn_lookup or geolocation or network_range:
                    for ip in dns_data['a_records'][:3]:
                        output.append("│")
                        output.append("│   IP: " + ip)
                        
                        if geolocation:
                            geo = _11(ip)
                            if geo:
                                output.append("│     Geolocation:")
                                if geo.get('country'): output.append("│       Country: " + geo['country'])
                                if geo.get('region'): output.append("│       Region: " + geo['region'])
                                if geo.get('city'): output.append("│       City: " + geo['city'])
                                if geo.get('isp'): output.append("│       ISP: " + geo['isp'])
                                if geo.get('org'): output.append("│       Org: " + geo['org'])
                        
                        if asn_lookup:
                            asn = _12(ip)
                            if asn:
                                output.append("│     ASN:")
                                if asn.get('asn'): output.append("│       ASN: " + asn['asn'])
                                if asn.get('org'): output.append("│       Org: " + asn['org'])
                                if asn.get('isp'): output.append("│       ISP: " + asn['isp'])
                        
                        if network_range:
                            net = _17(ip)
                            if net:
                                output.append("│     Network:")
                                if net.get('network'): output.append("│       Network: " + net['network'])
                                if net.get('netmask'): output.append("│       Netmask: " + net['netmask'])
                                if net.get('broadcast'): output.append("│       Broadcast: " + net['broadcast'])
                        
                        if reverse_dns:
                            try:
                                import socket
                                rev_host = socket.gethostbyaddr(ip)[0]
                                output.append("│     Reverse DNS: " + rev_host)
                            except:
                                output.append("│     Reverse DNS: Failed")
            
            if dns_data.get('aaaa_records'):
                output.append("│   AAAA Records: " + ", ".join(dns_data['aaaa_records'][:5]))
            if dns_data.get('mx_records'):
                output.append("│   MX Records:")
                for mx in dns_data['mx_records'][:5]:
                    output.append("│     " + mx)
                results_summary['mx_count'] = len(dns_data['mx_records'])
            if dns_data.get('ns_records'):
                output.append("│   NS Records: " + ", ".join(dns_data['ns_records'][:5]))
                results_summary['ns_count'] = len(dns_data['ns_records'])
            if dns_data.get('txt_records'):
                output.append("│   TXT Records:")
                for txt in dns_data['txt_records'][:3]:
                    output.append("│     " + txt[:100] + ("..." if len(txt) > 100 else ""))
            if dns_data.get('cname'):
                output.append("│   CNAME: " + ", ".join(dns_data['cname']))
            if dns_data.get('soa'):
                output.append("│   SOA: " + ", ".join(dns_data['soa'][:3]))
            output.append("│")
        except Exception as e:
            output.append("│ [!] DNS failed: " + str(e))
            output.append("│")
    
    if domain_age:
        output.append("│ ●  Domain age calculation")
        try:
            age_data = _18(domain)
            if age_data:
                output.append("│   Domain Age:")
                if age_data.get('created'):
                    output.append("│     Created: " + age_data['created'])
                if age_data.get('days_old'):
                    output.append("│     Age: " + str(age_data['days_old']) + " days (" + str(age_data.get('years_old', 0)) + " years)")
                if age_data.get('expires'):
                    output.append("│     Expires: " + age_data['expires'])
                if age_data.get('days_left') is not None:
                    output.append("│     Days until expiry: " + str(age_data['days_left']))
                if age_data.get('expiry_warning'):
                    output.append("│ [!] " + age_data['expiry_warning'])
                output.append("│")
        except Exception as e:
            output.append("│ [!] Age calculation failed: " + str(e))
            output.append("│")
    
    if ssl_cert:
        output.append("│ ●  SSL certificate check")
        try:
            cert_data = _13(domain)
            if cert_data:
                output.append("│   SSL Certificate:")
                if cert_data.get('subject'):
                    output.append("│     Subject: " + str(cert_data['subject']))
                if cert_data.get('issuer'):
                    output.append("│     Issuer: " + str(cert_data['issuer']))
                if cert_data.get('not_before'):
                    output.append("│     Valid From: " + cert_data['not_before'])
                if cert_data.get('not_after'):
                    output.append("│     Valid Until: " + cert_data['not_after'])
                output.append("│")
            else:
                output.append("│ [!] No SSL certificate found")
                output.append("│")
        except Exception as e:
            output.append("│ [!] SSL check failed: " + str(e))
            output.append("│")
    
    if http_headers:
        output.append("│ ●  HTTP headers")
        try:
            headers = _14(domain)
            if headers:
                output.append("│   HTTP Headers:")
                if headers.get('status_code'):
                    output.append("│     Status: " + str(headers['status_code']))
                if headers.get('Server'):
                    output.append("│     Server: " + headers['Server'])
                if headers.get('Content-Type'):
                    output.append("│     Content-Type: " + headers['Content-Type'])
                if headers.get('X-Powered-By'):
                    output.append("│     X-Powered-By: " + headers['X-Powered-By'])
                output.append("│     Total: " + str(len(headers)) + " headers")
                output.append("│")
            else:
                output.append("│ [!] Failed to fetch headers")
                output.append("│")
        except Exception as e:
            output.append("│ [!] HTTP check failed: " + str(e))
            output.append("│")
    
    subdomains = []
    if subdomain_scan:
        output.append("│ ●  Subdomain scan")
        try:
            subdomains = _15(domain)
            if subdomains:
                output.append("│   Found " + str(len(subdomains)) + " subdomains:")
                for sub in subdomains[:20]:
                    output.append("│     " + sub)
                if len(subdomains) > 20:
                    output.append("│     ... and " + str(len(subdomains) - 20) + " more")
                output.append("│")
            else:
                output.append("│ [!] No subdomains found")
                output.append("│")
        except Exception as e:
            output.append("│ [!] Subdomain scan failed: " + str(e))
            output.append("│")
    
    open_ports = []
    if ports_scan:
        output.append("│ ●  Port scan")
        try:
            open_ports = _16(domain)
            if open_ports:
                service_map = {
                    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
                    80: 'HTTP', 110: 'POP3', 135: 'MSRPC', 139: 'NetBIOS',
                    143: 'IMAP', 443: 'HTTPS', 445: 'SMB', 993: 'IMAPS',
                    995: 'POP3S', 1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP',
                    5432: 'PostgreSQL', 5900: 'VNC', 6379: 'Redis',
                    8080: 'HTTP-Alt', 8443: 'HTTPS-Alt', 27017: 'MongoDB'
                }
                output.append("│   Open ports: " + ", ".join(map(str, open_ports)))
                output.append("│   Services:")
                for port in open_ports:
                    service = service_map.get(port, 'Unknown')
                    output.append("│     Port " + str(port) + ": " + service)
                output.append("│")
            else:
                output.append("│ [!] No open ports found")
                output.append("│")
        except Exception as e:
            output.append("│ [!] Port scan failed: " + str(e))
            output.append("│")
    
    if output_format == 'summary':
        output.append("│")
        output.append("│ ●  SUMMARY")
        output.append("│ ──────────────────────────────")
        output.append("│   Domain: " + results_summary.get('domain', domain))
        if parsed_info.get('registrar'):
            output.append("│   Registrar: " + ", ".join(parsed_info['registrar'][:2]))
        if parsed_info.get('creation_date'):
            output.append("│   Created: " + ", ".join(parsed_info['creation_date'][:2]))
        if parsed_info.get('expiry_date'):
            output.append("│   Expires: " + ", ".join(parsed_info['expiry_date'][:2]))
        if parsed_info.get('name_servers'):
            output.append("│   Name Servers: " + ", ".join(parsed_info['name_servers'][:3]))
        if contacts.get('emails'):
            output.append("│   Emails: " + ", ".join(contacts['emails'][:3]))
        if dns_data.get('a_records'):
            output.append("│   IPs: " + ", ".join(dns_data['a_records'][:2]))
        output.append("│ ──────────────────────────────")
        output.append("│")
    
    if verbose:
        output.append("│")
        output.append("│ ●  Statistics:")
        output.append("│   Total lines: " + str(len(data_lines)))
        output.append("│   Referrals: " + str(len(referral_chain)))
        output.append("│   Parsed fields: " + str(len(parsed_info.get('raw_fields', {}))))
        output.append("│   Contacts - Emails: " + str(len(contacts.get('emails', []))))
        output.append("│   Contacts - Phones: " + str(len(contacts.get('phones', []))))
        if dns_lookup:
            output.append("│   DNS - A: " + str(len(dns_data.get('a_records', []))))
            output.append("│   DNS - MX: " + str(len(dns_data.get('mx_records', []))))
            output.append("│   DNS - NS: " + str(len(dns_data.get('ns_records', []))))
        output.append("│")
    
    if output_csv:
        try:
            import csv
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Domain', 'Registrar', 'Created', 'Expires', 'Name Servers', 'IPs'])
                writer.writerow([
                    results_summary.get('domain', domain),
                    ', '.join(parsed_info.get('registrar', [])[:2]),
                    ', '.join(parsed_info.get('creation_date', [])[:2]),
                    ', '.join(parsed_info.get('expiry_date', [])[:2]),
                    ', '.join(parsed_info.get('name_servers', [])[:3]),
                    ', '.join(dns_data.get('a_records', [])[:2]) if dns_lookup else ''
                ])
            output.append("│ ●  CSV saved: " + csv_file)
            output.append("│")
        except Exception as e:
            output.append("│ [!] CSV save failed: " + str(e))
            output.append("│")
    
    full_output = "\n".join(output)
    
    if save_to_file:
        try:
            with open(save_to_file, 'w', encoding='utf-8') as f:
                f.write(full_output)
            output.append("│ ●  Results saved: " + save_to_file)
            output.append("│")
        except Exception as e:
            output.append("│ [!] File save failed: " + str(e))
            output.append("│")
    
    output.append("│ ●  Whois lookup completed")
    output.append("│ ●  Complete")
    
    return "\n".join(output)
