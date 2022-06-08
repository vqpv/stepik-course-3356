import numpy as np

np.random.seed(42)

Z = np.random.random_sample((list(map(int, input().split()))))
X = np.mean(Z, axis=0)

print(np.amin(X))
print(np.amax(X))
