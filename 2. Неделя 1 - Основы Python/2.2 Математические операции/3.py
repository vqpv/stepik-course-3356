a, b, c = int(input()), int(input()), int(input())

P = a + b + c
p = P / 2

print(P)
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
