def luka(L0, L1, n):
    x, y = L0, L1
    for _ in range(n):
        x, y = y, x + y
    return x
