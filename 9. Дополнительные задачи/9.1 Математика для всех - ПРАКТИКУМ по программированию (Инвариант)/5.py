n = list(map(int, input().split()))

c = 0

for i, j in enumerate(n):
    for j_2 in n[i + 1:]:
        if j > j_2:
            c += 1

print((-1) ** c)
