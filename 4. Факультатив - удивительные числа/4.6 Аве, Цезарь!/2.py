def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    c = ""
    for i in text.upper():
        if i in alphabet:
            c += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return c
