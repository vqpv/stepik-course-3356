def wisdom_multiplication(x, y, length_check = True):
    a = 100 - x
    b = 100 - y
    r_1 = str(100 - (a + b))
    r_2 = str(a * b)
    if (len(r_2) < 2) and length_check:
        r_2 = '0{0}'.format(r_2)
    return r_1 + r_2
