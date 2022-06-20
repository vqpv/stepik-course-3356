import numpy as np

n, m = map(int, input().split())
k = int(input())

Z = np.zeros((n, m))
Z += np.arange(k, k + m)
