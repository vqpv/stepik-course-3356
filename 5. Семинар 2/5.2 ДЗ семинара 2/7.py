def front_back(a, b):
    s_a = (len(a) + 1) // 2
    s_b = (len(b) + 1) // 2
    return a[:s_a] + b[:s_b] + a[s_a:] + b[s_b:]
