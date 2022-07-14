df = pd.read_csv('dataset_345422_14.txt', sep=',', parse_dates=["Date"])

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df["Date"] = df["Date"].map(lambda x: x.date().weekday())
mean_data = [df[df["Date"] == i].mean().sum() for i in range(7)]

print(days[mean_data.index(max(mean_data))])
