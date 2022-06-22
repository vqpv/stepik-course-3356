import numpy as np

start = int(input())
stop = int(input())
n = int(input())

Z = np.around(np.geomspace(start, stop, num=n), decimals=3)
