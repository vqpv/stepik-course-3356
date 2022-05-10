def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    key = str(key)
    c = ""
    s = 0
    for i in text.upper():
        if i in alphabet:
            if reverse:
                c += alphabet[(alphabet.index(i) - int(key[s % len(key)])) % len(alphabet)]
            else:
                c += alphabet[(alphabet.index(i) + int(key[s % len(key)])) % len(alphabet)]
            s += 1
    return c
