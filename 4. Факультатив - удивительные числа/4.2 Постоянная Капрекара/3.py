def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    s = "".join(map(str, sorted(L)))
    return abs(int(s) - int(s[::-1]))

def kaprekar_loop(n):
    print(n)
    while n != 6174:
        return kaprekar_loop(kaprekar_step(numerics(n)))
