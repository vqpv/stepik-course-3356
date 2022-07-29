from math import sqrt, ceil

def S(x):
    s_5 = (sqrt(25 + 10 * sqrt(5)) / 4) * (x ** 2)
    s_6 = ((3 * sqrt(3)) / 2) * (x ** 2)
    return s_5 * 12 + s_6 * 20

def S_ceil(x):
    return ceil(S(x))
