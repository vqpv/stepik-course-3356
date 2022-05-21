def print_mimic(mimic_dict, word):
    lst = [word]
    for _ in range(199):
        if word in mimic_dict:
            word = random.choice(mimic_dict[word])
        else:
            word = random.choice(mimic_dict[""])
        lst.append(word)
    return " ".join(lst)
