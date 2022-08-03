l, n, m = int(input()), int(input()), int(input())

c = 1000000
P = 0

for _ in range(c):
    crd = sorted([random.uniform(0,l) for _ in range(n - 1)], reverse=True)
    crd.insert(0, l)
    crd.insert(len(crd), 0)
    for i in range(len(crd) - 1):
        if crd[i] - crd[i + 1] >= m:
            P += 1
            break

print(round((P * 100) / c, 1), end='%')
