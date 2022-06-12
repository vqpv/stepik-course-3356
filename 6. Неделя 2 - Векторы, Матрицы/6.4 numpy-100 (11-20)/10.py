import numpy as np

n, m = map(int, input().split())

b = np.array([[0., 1.] , [1., 0.]])

Z = np.tile(b, (n // 2 + 1, m // 2 + 1))[:n, :m]
