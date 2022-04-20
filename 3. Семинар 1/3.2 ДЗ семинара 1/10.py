def is_prime(n):
    return bool(not [i for i in range(2, int(n ** 0.5) + 1) if n % i == 0])
