n = int(input())

res = sum([i for i in range(n + 1) if (i % 5 == 0) and (i % 3 != 0)])

print(res)
