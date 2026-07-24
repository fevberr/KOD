OPTIONS = {
    'a': {'default': 'Hello World!', 'description': 'Text to print'},
    'b': {'default': '1', 'description': 'Number of times to print'},
    'c': {'default': 'normal', 'description': 'normal, uppercase, lowercase, title'}
}

def a1(options=None):
    if options:
        a = options.get('a', 'Hello World!')
        try:
            b = int(options.get('b', '1'))
        except:
            b = 1
        c = options.get('c', 'normal')
    else:
        a = 'Hello World!'
        b = 1
        c = 'normal'
    
    d = []
    d.append(f"[*] Printing '{a}' {b} time(s)...")
    d.append("")
    
    if c == 'uppercase':
        a = a.upper()
    elif c == 'lowercase':
        a = a.lower()
    elif c == 'title':
        a = a.title()
    
    for i in range(b):
        d.append(f"[{i+1}] {a}")
    
    d.append("")
    d.append("[*] Complete")
    return "\n".join(d)

def run(options=None):
    return a1(options)
