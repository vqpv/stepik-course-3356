from math import factorial

n, m = int(input()), int(input())

C = factorial(n) / (factorial(m) * factorial(n - m))
P = C * ((1 / 2) ** m) * ((1 - (1 / 2)) ** (n - m))

print(P * 100, end='%')
