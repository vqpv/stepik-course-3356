tickets = [i for i in range(int(input()))]
c = 100000
p = 0

for _ in range(c):
    random.shuffle(tickets)
    for i, j in enumerate(tickets):
        if i == j:
            p += 1
            break

print(round((p * 100) / c, 1), end='%')
