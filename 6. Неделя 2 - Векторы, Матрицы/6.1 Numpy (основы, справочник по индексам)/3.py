import numpy as np

v_1 = np.array(list(map(float, input().split(', '))))
v_2 = np.array(list(map(float, input().split(', '))))

V = v_1[v_1 % v_2[-2] == 0] / v_2[-2]
