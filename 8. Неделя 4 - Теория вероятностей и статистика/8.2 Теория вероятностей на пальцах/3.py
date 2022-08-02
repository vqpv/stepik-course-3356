n, m = int(input()), int(input())

c = 100000
P = 0

for _ in range(c):
    t = sum(random.randint(0, 1) for _ in range(n))
    P += int(t <= m)

print(round((P * 100) / c, 1), end='%')
