def multiplication_check_list(start=10, stop=99):
    n = 0
    m = 0
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            if multiplication_check(i, j):
                n += 1
            else:
                m += 1
    print(f'Правильных результатов: {n}')
    print(f'Неправильных результатов: {m}')

def multiplication_check(x, y):
    return (x * y) == simple_multiplication(x, y)

def simple_multiplication(x, y):
    return (100 - ((100 - x) + (100 - y))) * 100 + (100 - x) * (100 - y)
