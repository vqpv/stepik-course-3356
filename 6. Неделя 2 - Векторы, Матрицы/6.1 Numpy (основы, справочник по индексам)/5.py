M2 = np.copy(M1)
M2[-2, :] = np.sin(M2[-2, :] * np.pi / 6)
M2[:, -2] = np.exp(M2[:, -2])
M2[-2, -2] = np.exp(np.sin(M1[-2, -2] * np.pi / 6))
