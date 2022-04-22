def both_ends(s):
    if len(s) < 2:
        return ""
    return s[:2] + s[-2:]

print(both_ends(input()))
