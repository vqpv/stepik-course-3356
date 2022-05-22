import numpy as np

nums = list(map(float, input().split(', ')))

V1 = np.array(nums)
V2 = np.array([V1[-2]])
V3 = V1[::-1]
V4 = V1[::3]
V5 = np.array(range(len(V1)))
