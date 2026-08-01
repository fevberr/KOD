from config import a7 as get_tabs

def search_items(query, items):
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    for item in items:
        item_lower = item.lower()
        score = 0
        if query_lower == item_lower:
            score = 1000
        elif item_lower.startswith(query_lower):
            score = 500
        elif f" {query_lower} " in f" {item_lower} ":
            score = 300
        elif query_lower in item_lower:
            score = 200
        else:
            word_matches = 0
            for word in query_words:
                if word in item_lower:
                    word_matches += 1
            if word_matches > 0:
                score = 100 * (word_matches / len(query_words))
        if score == 0 and len(query_lower) > 2:
            matches = 0
            qi = 0
            for char in item_lower:
                if qi < len(query_lower) and char == query_lower[qi]:
                    matches += 1
                    qi += 1
            if matches > 0:
                score = 50 * (matches / len(query_lower))
        if score > 0:
            results.append((item, score))
    results.sort(key=lambda x: x[1], reverse=True)
    return [r[0] for r in results]

def search_modules(query, modules):
    results = []
    query_lower = query.lower()
    query_words = query_lower.split()
    for module in modules:
        module_lower = module.lower()
        tab = None
        for tn, mods in get_tabs().items():
            if module in mods:
                tab = tn
                break
        display_name = f"{tab}: {module}" if tab else module
        display_lower = display_name.lower()
        score = 0
        if query_lower == module_lower or query_lower == display_lower:
            score = 1000
        elif module_lower.startswith(query_lower) or display_lower.startswith(query_lower):
            score = 500
        elif f" {query_lower} " in f" {module_lower} " or f" {query_lower} " in f" {display_lower} ":
            score = 300
        elif query_lower in module_lower or query_lower in display_lower:
            score = 200
        else:
            word_matches = 0
            for word in query_words:
                if word in module_lower or word in display_lower:
                    word_matches += 1
            if word_matches > 0:
                score = 100 * (word_matches / len(query_words))
        if score == 0 and len(query_lower) > 2:
            matches = 0
            qi = 0
            for char in module_lower:
                if qi < len(query_lower) and char == query_lower[qi]:
                    matches += 1
                    qi += 1
            if matches > 0:
                score = 50 * (matches / len(query_lower))
        if score > 0:
            results.append((display_name, score, module, tab))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

__all__ = ['search_items', 'search_modules']
