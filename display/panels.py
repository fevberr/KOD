from utils.colors import green, red, cyan, yellow, white, gray, blue, magenta, bold, dim, reload_colors

def p1(t1, c1, s1=""):
    reload_colors()
    print(f"\n{cyan('+---')} {white(t1)}")
    l1 = c1.split('\n')
    for l2 in l1:
        if 'host:' in l2 or 'Port:' in l2:
            print(f"{cyan('|')} {white(l2)}")
        elif 'Ping:' in l2:
            print(f"{cyan('|')} {yellow(l2)}")
        elif 'device:' in l2 or 'system:' in l2:
            print(f"{cyan('|')} {magenta(l2)}")
        else:
            print(f"{cyan('|')} {gray(l2)}")
    if s1:
        print(f"{cyan('|-')} {green('Status:')} {white(s1)}")
    print(cyan('-' * 30))
