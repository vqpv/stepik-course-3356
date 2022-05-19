def list_pull(lst):
    new_list = []
    for i in lst:
        if isinstance(i, list):
            new_list.extend(list_pull(i))
        else:
            new_list.append(i)
    return new_list
