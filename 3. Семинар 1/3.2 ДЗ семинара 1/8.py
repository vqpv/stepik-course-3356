def front_x(words):
    l_1 = sorted([i for i in words if i.startswith('x')])
    l_2 = sorted([i for i in words if not i.startswith('x')])
    return l_1 + l_2
