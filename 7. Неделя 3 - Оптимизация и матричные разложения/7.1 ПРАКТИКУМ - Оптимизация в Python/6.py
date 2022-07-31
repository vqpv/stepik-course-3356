from scipy.optimize import golden

def f(x):
    return (x + a) ** 2 - b

def g(x):
    return abs(f(x))

min_f = f(golden(f, brack=(-10, -4)))
min_g = g(golden(g, brack=(-10, -4)))

print(min_f, min_g)
