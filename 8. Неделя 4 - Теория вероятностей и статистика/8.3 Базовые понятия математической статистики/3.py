import pandas as pd


c = 100000
nums = [gen() for i in range(c)]
series = pd.Series(nums)
mean = round(series.mean(), 2)
sd = round(series.std(), 2)

print("Mean:", mean)
print("Sd:", sd)
