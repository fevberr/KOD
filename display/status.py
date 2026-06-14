_STATUS = "NOT READY IN TEMP"

def s1(status):
    global _STATUS
    _STATUS = status
    
def s2():
    return _STATUS
