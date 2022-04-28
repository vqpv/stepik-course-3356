def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_check(n):
    lst = numerics(n)
    if len(lst) not in (3, 4, 6):
        return False
    elif lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]:
        return False
    elif n in (100, 1000, 100000):
        return False
    return True
