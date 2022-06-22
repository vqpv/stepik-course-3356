import numpy as np

start = int(input())
stop = int(input())
n = int(input())

Z = np.around(np.linspace(start, stop, num=n+1, endpoint=False), decimals=3)[1:]
