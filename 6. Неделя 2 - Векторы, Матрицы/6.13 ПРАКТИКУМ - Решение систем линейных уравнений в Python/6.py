import numpy as np

a, b = input().split()

M1 = np.array([[1, 1], [1, -1]], dtype=np.float) # Матрица (левая часть системы)
v1 = np.array([a, b], dtype=np.float) # Вектор (правая часть системы)
r = np.linalg.solve(M1, v1) #Находим решение системы

if r[0] < 0 or r[1] < 0 or r[0] % 1 != 0 or r[1] % 1 != 0:
    print("Такой класс не существует")
else:
    print(int(r[0]), int(r[1]))
