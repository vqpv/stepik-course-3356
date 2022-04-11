def translate(n, f=2):
    s = ""
    while n:
        s = str(n % f) + s
        n //= f
    return s
