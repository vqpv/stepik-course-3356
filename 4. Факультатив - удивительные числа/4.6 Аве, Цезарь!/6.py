def disc_generator(alphabet):
    lst = list(alphabet)
    random.shuffle(lst)
    return ''.join(lst)

def jefferson_encryption(text, discs, step, reverse=False):
    cipher = ""
    s = 0
    for i in text.upper():
        if i in discs[0]:
            disc_num = s % len(discs)
            index = discs[disc_num].index(i)
            disc = discs[disc_num]
            disc_len = len(discs[0])
            if reverse:
                cipher += disc[(index - step) % disc_len]
            else:
                cipher += disc[(index + step) % disc_len]
            s += 1       
    return cipher

discs = [disc_generator(clear_alphabet) for i in range(n)]
