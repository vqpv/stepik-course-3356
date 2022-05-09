def bruteforce(text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for j in range(1, len(alphabet)):
        c = ""
        for i in text.upper():
            if i in alphabet:
                c += alphabet[(alphabet.index(i) - j) % len(alphabet)]
        print(c)
