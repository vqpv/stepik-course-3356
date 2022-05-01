def fi(L0, L1, n):
    x, y = Decimal(L0), Decimal(L1)
    for _ in range(n - 1):
        x, y = y, x + y
    return y / x
