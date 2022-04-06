string = input().split()

for word in string:
    if not word.startswith('*'):
        print(word)
