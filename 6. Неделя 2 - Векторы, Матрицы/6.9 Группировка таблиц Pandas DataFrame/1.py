df = pd.read_csv('dataset_345422_8.txt', sep=';')
df = df[(df['IP_PROP30'] == "pink") & (df['IP_PROP32'] == "XL")]

print((df['CR_PRICE_1_USD'] * df['CP_QUANTITY']).sum())
