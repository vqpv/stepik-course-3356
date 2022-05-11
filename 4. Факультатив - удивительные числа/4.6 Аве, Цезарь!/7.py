def kidds_encryption(text, reverse=False):
    d = {'e': '8', 't': ';', 'h': '4', 'o': '‡', 's': ')', 'n': '*', 'a': '5', 'i': '6', 'r': '(', 'f': '1', 'd': '†', 'l': '0', 'm': '9', 'b': '2', 'y': ':', 'g': '3', 'u': '?', 'v': '¶', 'c': '-', 'p': '.'}
    inv_d = {value: key for key, value in d.items()}
    c = ""
    for i in text.lower():
        if reverse:
            if i in inv_d:
                c += inv_d.get(i)
        else:
            if i in d:
                c += d.get(i)
    return c
