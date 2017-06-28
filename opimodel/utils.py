def mangle_name(name):
    """Convert the name found in a color or font configuration file into
       a Python variable:
           - convert to upper-case
           - replace non-letters with underscores
           - avoid consecutive underscores

    Args:
        name to convert
    Returns:
        converted name
    """
    last = ''
    deduped = []
    for char in name:
        if not char.isalpha() and not char.isdigit():
            if last == '_':
                continue
            else:
                char = '_'
        last = char
        deduped.append(char)

    name = ''.join(deduped).upper()
    return name
