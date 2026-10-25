#Task 01
import pandas as pd
df = pd.read_csv("mini1_students.csv")
print(df.head(3))
print(df.shape)
df.info()
#Task 02
missing_values = df.isna().sum()
print(missing_values)
#Task 03
df_clean = df.fillna({"math" : 0, "science" : 0, "age" : 20})
print(df_clean)
#Task 04
print(df_clean.loc[:, ["name","math"]])
#Task 05
print(df_clean.iloc[3 , 2])
#Task 06
mask=(df_clean["math"] > 80) & (df_clean["city"] == "Lahore")
print(df_clean.loc[mask, ["name" , "math"]])  #mask here to print only true rows
#Task 07
avg_marks=df_clean["math"].mean()
print(round(avg_marks,1))