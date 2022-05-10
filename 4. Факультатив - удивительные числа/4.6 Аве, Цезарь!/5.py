def disc_generator(alphabet):
    lst = list(alphabet)
    random.shuffle(lst)
    return ''.join(lst)
