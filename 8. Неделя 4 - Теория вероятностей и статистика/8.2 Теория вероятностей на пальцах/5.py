import numpy

n, m, k = int(input()), int(input()), int(input())

c = 1000000
P = 0

for _ in range(c):
    t = sum(numpy.random.randint(1, m + 1, size=n))
    P += int(t >= k)

print(round((P * 100) / c, 1), end='%')
