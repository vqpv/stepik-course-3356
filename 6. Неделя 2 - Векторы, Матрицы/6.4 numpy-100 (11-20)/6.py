import numpy as np

Z = np.ones((list(map(int, input().split()))))
Z[1:-1, 1:-1] = 0
