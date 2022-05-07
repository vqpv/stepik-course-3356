def caesar(text, key):
    c = ""
    for i in text.upper():
        if ord(i) in range(65, 91):
            c += chr((ord(i) + key - 65) % 26 + 65)
    return c
