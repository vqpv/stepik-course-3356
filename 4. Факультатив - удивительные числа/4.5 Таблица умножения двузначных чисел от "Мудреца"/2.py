def multiplication_check(x, y):
    return (x * y) == simple_multiplication(x, y)

def simple_multiplication(x, y):
    return (100 - ((100 - x) + (100 - y))) * 100 + (100 - x) * (100 - y)
