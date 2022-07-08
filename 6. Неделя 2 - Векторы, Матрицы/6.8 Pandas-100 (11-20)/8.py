df.loc[new_index] = new_data
df = df.drop([del_index])

print(df)
