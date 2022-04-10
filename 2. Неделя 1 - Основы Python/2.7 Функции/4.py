def Kfactorial(n, k=1):
    if n <= 1:
        return 1
    elif n <= k:
        return n
    return n * Kfactorial(n - k, k)
