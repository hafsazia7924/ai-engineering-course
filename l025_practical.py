#task 1
import pandas as pd
import numpy as np

data = {
    "name": ["Ahmed", "Zara", "Bilal", "Noor", "Fatima"],
    "age": [20, np.nan, 22, 21, np.nan],
    "city": ["Multan", "Lahore", None, "Multan", "Karachi"]
}
df = pd.DataFrame(data)
missing_values=df.isna().sum()
print(missing_values)
missing_part=df.isna().mean()*100
print(missing_part.round(1))
missing_age=df["age"].isna()
print(df[missing_age])
df_age_ok=df.dropna(subset="age")
print(df_age_ok)
mean=df["age"].mean()
df_filled=df.fillna({"age":mean,"city":"Unknown"})
print(df_filled)

print(df)