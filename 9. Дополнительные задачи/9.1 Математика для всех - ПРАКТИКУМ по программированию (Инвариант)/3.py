import numpy as np


n, m = map(int, input().split())

b = np.array([[0., 1.] , [1., 0.]])

Z = np.tile(b, (n // 2 + 1, m // 2 + 1))[:n, :m]
Z[0][0] = 3
Z[-1][-1] = 3

if (Z == 0).sum() == (Z == 1).sum():
    print("Замостить можно")
else:
    print("Замостить нельзя")
