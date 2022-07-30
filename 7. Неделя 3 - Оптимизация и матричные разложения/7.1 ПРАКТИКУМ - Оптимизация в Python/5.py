from scipy.optimize import golden

def f(x):
    return (x + a) ** 2 - b

def g(x):
    return abs(f(x))

min_f = golden(f)
min_g = golden(g)

print(min_f, min_g)
