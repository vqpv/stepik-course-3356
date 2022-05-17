from math import sin, pi 

def f(x):
    return round(((sin((pi * x) / 2)) / x), 3)

print(f(99999))
