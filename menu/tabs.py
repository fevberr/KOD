from config import a7 as get_tabs

def get_tab_list():
    t = get_tabs()
    return list(t.keys())

def get_tab_count():
    return len(get_tab_list())

def get_current_tab_modules(p4):
    t = get_tabs()
    n = list(t.keys())
    if p4 < len(n):
        return t[n[p4]]
    return []

def switch_tab(p4, direction):
    t = get_tab_list()
    if direction == "next":
        return (p4 + 1) % len(t)
    elif direction == "prev":
        return (p4 - 1) % len(t)
    elif direction == "first":
        return 0
    elif direction == "last":
        return len(t) - 1
    return p4

__all__ = ['get_tab_list', 'get_tab_count', 'get_current_tab_modules', 'switch_tab']
