def convert(ls):
    return [int(i) for i in ls]

def maxId(ls):
    lst = convert(ls)
    return lst.index(max(lst))
