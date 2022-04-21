n = int(input())

def donuts(n):
    if n <= 9:
        count = n
    else:
        count = "много"
    return f"Всего пончиков: {count}"

print(donuts(n))
