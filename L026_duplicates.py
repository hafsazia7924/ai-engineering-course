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

#subset
data_form = {
    "name": ["Ali", "Sara", "Ali", "Hina"],
    "city": ["Lahore", "Multan", "Karachi", "Lahore"],
    "math": [78, 91, 80, 88],
}
df_form = pd.DataFrame(data_form)
print(df_form)
print(df_form.duplicated())
print(df_form.duplicated(subset = ["name"]))
df_form_unique = df_form.drop_duplicates(subset = ["name"])
print(df_form_unique)
#keep
df_last = df_form.drop_duplicates(subset = ["name"],keep = "last") #keep last and remove any above
print(df_last)

#Task 1
import pandas as pd

data_q = {
    "name": ["Zain", "Mina", "Zain", "Bilal", "Mina"],
    "city": ["Multan", "Lahore", "Multan", "Karachi", "Lahore"],
    "score": [60, 75, 60, 82, 90],
}
df_q = pd.DataFrame(data_q)
print(df_q.duplicated())
print(df_q.duplicated(subset=["name"]))
df_clean = df_q.drop_duplicates(subset=["name"], keep="last")
print(df_clean)
df_unique = df_q.drop_duplicates(subset=["name"])
print(df_unique)
mask = df_q["score"] > 70
print(df_q.loc[mask, ["name", "score"]])