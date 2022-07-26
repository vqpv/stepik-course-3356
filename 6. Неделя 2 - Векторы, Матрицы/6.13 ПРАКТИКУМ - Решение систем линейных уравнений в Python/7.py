import numpy as np

n = int(input())

a = []
b = []

for i in range(n):
    s = input().split()
    m = []
    b.append(s[1])
    for j in range(n):
        m.append(float(s[0]) ** j)
    a.append(m)

M1 = np.array(a, dtype=np.float) # Матрица (левая часть системы)
v1 = np.array(b, dtype=np.float) # Вектор (правая часть системы)

r = np.linalg.solve(M1, v1) #Находим решение системы

print(*r)
