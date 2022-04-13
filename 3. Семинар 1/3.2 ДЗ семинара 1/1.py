import math

def f(x):
    return 2 * math.atan(x)

lim = round(f(99999), 3)

print(lim)
