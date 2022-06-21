import numpy as np

n, m = map(int, input().split())
k = int(input())

Z = np.zeros((m, n))
Z += np.arange(k, k + n)
Z = np.transpose(Z)
