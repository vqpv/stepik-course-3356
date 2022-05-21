def mimic_dict(string):
    keys = string.split()
    d = {"": [keys[0]]}
    for i in range(len(keys) - 1):
        if keys[i] in d:
            d.get(keys[i]).append(keys[i + 1])
        else:
            d[keys[i]] = [keys[i + 1]]
    return d
