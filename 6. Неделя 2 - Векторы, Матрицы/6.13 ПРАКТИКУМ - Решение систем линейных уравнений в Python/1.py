import numpy as np

a11, a12, b1 = input().split()
a21, a22, b2 = input().split()

M1 = np.array([[a11, a12], [a21, a22]], dtype=np.float) # Матрица (левая часть системы)
v1 = np.array([b1, b2], dtype=np.float) # Вектор (правая часть системы)
r = np.linalg.solve(M1, v1) #Находим решение системы

print(r[0], r[1])
