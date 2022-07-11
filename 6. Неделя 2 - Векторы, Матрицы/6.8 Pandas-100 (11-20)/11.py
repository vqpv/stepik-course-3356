df[column] = df[column].map({'yes': True, 'no': False, 1: True, 0: False}, na_action=None)

print(df)
