import numpy as np

n = int(input())

a = [0] * n
b = [0] * n

for i in range(n):
    s = input().split()
    b[i] = s[-1]
    for j in range(n):
        a[i] = s[:-1]

M1 = np.array(a, dtype=np.float) # Матрица (левая часть системы)
v1 = np.array(b, dtype=np.float) # Вектор (правая часть системы)

d = np.linalg.det(M1)

if d == 0:
    print("Матрица системы вырожденная")
else:
    r = np.linalg.solve(M1, v1) #Находим решение системы
    print(*r)
