def parse_option_input(inp, ol, co, mo):
    parts = inp.strip().split()
    if not parts:
        return False, None, None
    if not parts[0].isdigit():
        if '=' in inp or ':' in inp:
            sep = '=' if '=' in inp else ':'
            kv = inp.split(sep)
            if len(kv) == 2:
                key = kv[0].strip()
                val = kv[1].strip()
                for i, k in enumerate(ol, 1):
                    if k.lower() == key.lower():
                        return True, i, val
        return False, None, None
    num = int(parts[0])
    if num < 1 or num > len(ol):
        return False, None, None
    if len(parts) == 1:
        return True, num, None
    val = ' '.join(parts[1:])
    return True, num, val

__all__ = ['parse_option_input']
