import numpy as np

i = input().split()

if i[-1].isdigit():
    Z = np.zeros(tuple(map(int, i)), dtype=np.float64)
else:
    Z = np.zeros(tuple(map(int, i[:-1])), dtype=i[-1])
