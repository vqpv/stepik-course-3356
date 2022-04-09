def dfactorial(num):
    if num <= 1:
        return 1
    return num * dfactorial(num - 2)
