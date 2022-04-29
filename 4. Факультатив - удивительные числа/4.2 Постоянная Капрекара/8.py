nums = set()

def numerics(n):
    return [int(i) for i in str(n)]

def kaprekar_step(L):
    s = "".join(map(str, sorted(L)))
    return abs(int(s) - int(s[::-1]))

def kaprekar_check(n):
    lst = numerics(n)
    if len(lst) not in (3, 4, 6):
        return False
    elif lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]:
        return False
    elif n in (100, 1000, 100000):
        return False
    return True

def kaprekar_loop(n):
    if kaprekar_check(n):
        if n not in nums:
            print(n)
            if len(str(n)) == 6:
                nums.add(n)
            while n not in (495, 6174, 549945, 631764):
                return kaprekar_loop(kaprekar_step(numerics(n)))
        else:
            print(f"Следующее число - {n}, кажется процесс зациклился...")
    else:
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
