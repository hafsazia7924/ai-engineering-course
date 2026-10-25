import pandas as pd

data = {
    "name": ["Ali", "Sara", "Ali", "Hina"],
    "city": ["Lahore", "Multan", "Lahore", "Lahore"],
    "math": [78, 91, 78, 88],
}
df = pd.DataFrame(data)
print(df)
print(df.duplicated())

#duplicates remover
df_unique = df.drop_duplicates()
print(df_unique)
print(df)