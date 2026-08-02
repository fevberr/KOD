from config import a7 as get_tabs

def search_modules(query, modules):
    results = []
    query_lower = query.lower()
    
    for module in modules:
        module_lower = module.lower()
        tab = None
        
        for tn, mods in get_tabs().items():
            if module in mods:
                tab = tn
                break
        
        if query_lower in module_lower:
            results.append((f"{tab}: {module}" if tab else module, module, tab))
    
    return results

__all__ = ['search_modules']
