def multiplication_check_list(start=10, stop=99, length_check = True):
    t = 0
    w = 0
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            if (i * j) == wisdom_multiplication(i, j, length_check):
                t += 1
            else:
                w += 1
    print(f"Правильных результатов: {t}")
    print(f"Неправильных результатов: {w}")
    
def wisdom_multiplication(x, y, length_check = True):
    a = 100 - x
    b = 100 - y
    r_1 = str(100 - (a + b))
    r_2 = str(a * b)
    if (len(r_2) < 2) and length_check:
        r_2 = '0{0}'.format(r_2)
    return int(r_1 + r_2)
