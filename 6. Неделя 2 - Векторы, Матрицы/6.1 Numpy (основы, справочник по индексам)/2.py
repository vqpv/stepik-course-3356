import numpy as np

s_1 = list(map(int, input().split(', ')))
s_2 = list(map(int, input().split(', ')))

V1 = np.array(s_1)
V2 = np.array(s_2)
V3 = V1 + V2
V4 = V1[::2] * V2[::-2]
