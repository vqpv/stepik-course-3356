from math import *

def derivative(f, x0=0):
    dx = 0.0001
    return round((f(x0 + dx) - f(x0)) / dx, 3)
