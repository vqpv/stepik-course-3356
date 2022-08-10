import pandas as pd

nums = list(map(int, input().split()))

series = pd.Series(nums)
mean = round(series.mean(), 1)
median = round(series.median(), 1)
mods = list(series.mode())

print('Среднее:', mean)
print('Медиана:', median)
print('Мода:' if len(mods) == 1 else 'Моды:', *mods)

if median > mean:
    print('Ме>Ср')
elif mean == median:
    print('Ме=Ср')
else:
    print('Ме<Ср')
for m in mods:
    if m > mean:
        print('Мо>Ср')
    elif m == mean:
        print('Мо=Ср')
    else:
        print('Мо<Ср')
    if m > median:
        print('Мо>Ме')
    elif m == median:
        print('Мо=Ме')
    else:
        print('Мо<Ме')
