n, m = int(input()), int(input())

c = 1000000
P_1, P_2 = 0, 0

for _ in range(c):
    trains = ['1'] * n + ['2'] * m
    p = random.choice(trains)
    if p == '1':
        P_1 += 1
    else:
        P_2 += 1

print(round((P_1 * 100) / c, 1), end='%')
