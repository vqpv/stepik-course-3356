t = input()

if t == "int":
    num_1, num_2 = int(input()), int(input())
    if num_1 == 0 and num_2 == 0:
        print("Empty Ints")
    else:
        print(num_1 + num_2)
elif t == "str":
    str_1 = input()
    if str_1:
        print(str_1)
    else:
        print("Empty String")
elif t == "list":
    lst_1 = input().split()
    if lst_1:
        print(lst_1[-1])
    else:
        print("Empty List")
else:
    print("Unknown type")
