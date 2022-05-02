def super_L(n):
    x, y = 2, 1
    for _ in range(n):
        x, y = y, x + y
    return x
