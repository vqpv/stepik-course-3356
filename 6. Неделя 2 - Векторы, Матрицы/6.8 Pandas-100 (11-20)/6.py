s = df.sum(numeric_only=True).to_dict()
lst = list(s.items())

for i in lst:
    print(f'{i[0]}:{i[1]}')
