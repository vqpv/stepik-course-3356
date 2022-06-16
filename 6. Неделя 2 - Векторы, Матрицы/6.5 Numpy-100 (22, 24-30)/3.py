import numpy as np

try:
    Z = np.dot(A, B)
except ValueError:
    Z = 'Упс! Что-то пошло не так...'
