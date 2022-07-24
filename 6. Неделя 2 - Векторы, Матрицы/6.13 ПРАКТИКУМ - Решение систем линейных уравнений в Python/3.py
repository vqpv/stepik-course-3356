import numpy as np

a11, a12, a13, b1 = input().split()
a21, a22, a23, b2 = input().split()
a31, a32, a33, b3 = input().split()

M1 = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]], dtype=np.float) # Матрица (левая часть системы)
v1 = np.array([b1, b2, b3], dtype=np.float) # Вектор (правая часть системы)

d = np.linalg.det(M1)

if d == 0:
    print("Матрица системы вырожденная")
else:
    r = np.linalg.solve(M1, v1) #Находим решение системы
    print(r[0], r[1], r[2])
