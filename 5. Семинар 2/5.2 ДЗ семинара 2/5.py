def copy_2(lst):
    new_list = []
    for i in lst:
        if isinstance(i, list):
            new_list.append(copy_2(i))
        else:
            new_list.append(i)
    return new_list

L2 = copy_2(L1)
