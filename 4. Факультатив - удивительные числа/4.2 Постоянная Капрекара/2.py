def kaprekar_step(L):
    s = "".join(map(str, sorted(L)))
    return abs(int(s) - int(s[::-1]))
