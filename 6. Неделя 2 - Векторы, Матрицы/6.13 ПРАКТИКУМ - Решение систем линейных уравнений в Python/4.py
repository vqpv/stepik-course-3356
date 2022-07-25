import numpy as np

a11, a12, a13, a14, b1 = input().split()
a21, a22, a23, a24, b2 = input().split()
a31, a32, a33, a34, b3 = input().split()
a41, a42, a43, a44, b4 = input().split()

M1 = np.array([[a11, a12, a13, a14], [a21, a22, a23, a24], [a31, a32, a33, a34], [a41, a42, a43, a44]], dtype=np.float) # Матрица (левая часть системы)
v1 = np.array([b1, b2, b3, b4], dtype=np.float) # Вектор (правая часть системы)

d = np.linalg.det(M1)

if d == 0:
    print("Матрица системы вырожденная")
else:
    r = np.linalg.solve(M1, v1) #Находим решение системы
    print(r[0], r[1], r[2], r[3])
