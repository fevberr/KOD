def p1(t1, c1, s1=""):
    print(f"\n+--- {t1}")
    l1 = c1.split('\n')
    for l2 in l1:
        print(f"| {l2}")
    if s1:
        print(f"|- Status: {s1}")
    print("------------------------------")
