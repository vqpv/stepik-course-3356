n, m = map(int, input().split())

nums = []

for row in range(n):
    if row % 2 == 0:
        nums += list(map(int, input().split()))
    else:
        nums += list(map(int, input().split()))[::-1]

nums_e = list(range(1, n * m))

def check(lst_n):
    c = 0
    for i, j in enumerate(lst_n):
        for j_2 in lst_n[i + 1:]:
            if j > j_2:
                c += 1

    return (-1) ** c

print("Бинго!" if check(nums) == check(nums_e) else "Не повезло...")
