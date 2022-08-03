l, m = int(input()), int(input())

c = 100000
P = 0

for _ in range(c):
    t_1 = random.random() * l
    t_2 = l - t_1
    P += int(t_1 >= m or t_2 >= m)

print(round((P * 100) / c, 1), end='%')
