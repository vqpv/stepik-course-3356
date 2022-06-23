import numpy as np

seed = int(input())
n = int(input())

np.random.seed(seed)
Z = np.sort(np.random.random(n))
