import numpy as np

np.random.seed(42)

Z = np.random.random_sample((list(map(int, input().split()))))

print(np.amin(Z))
print(np.amax(Z))
