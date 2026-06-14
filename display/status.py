_s1 = "NOT READY"

def s1(s2):
    global _s1
    _s1 = s2
    
def s2():
    return _s1
