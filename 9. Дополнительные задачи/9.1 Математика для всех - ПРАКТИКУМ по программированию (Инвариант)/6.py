nums = [j for i in range(4) for j in input().split()]

def check(n):
    c = 0
    for i, j in enumerate(n):
        for j_2 in n[i + 1:]:
            if j > j_2:
                c += 1

    return (-1) ** c

print("Бинго!" if check(nums) == -1 else "Не повезло...")
