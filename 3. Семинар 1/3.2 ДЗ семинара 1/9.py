import math

def fib(n):
    f = math.sqrt(5)
    return round(((((1 + f) / 2) ** n) - (((1 - f) / 2) ** n)) / f)
