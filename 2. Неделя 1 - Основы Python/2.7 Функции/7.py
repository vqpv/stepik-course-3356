def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sf(n):
    if n <= 1:
        return 1
    return factorial(n) * sf(n - 1)
