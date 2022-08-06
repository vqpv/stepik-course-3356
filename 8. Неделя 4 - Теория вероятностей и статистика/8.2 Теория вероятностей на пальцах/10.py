l_1 = input().split()
l_2 = input().split()
l_3 = input().split()
l_4 = int(input())

c = 100000
P_1, P_2 = 0, 0

for _ in range(c):
    trains = []
    for i, _ in enumerate(l_2):
        trains.extend([l_1[i]] * int(l_2[i]))
    random.shuffle(trains)
    if trains[l_4 - 1] in l_3:
        P_1 += 1
    else:
        P_2 += 1

print(round((P_1 * 100) / c, 1), end='%')
