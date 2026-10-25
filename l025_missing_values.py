import numpy as np
import pandas as pd
data={
    "name" : ["Ali","Sara","Usman","Hina"],
    "marks" : [78, np.nan ,65,90],
    "city" : ["Lahore","Multan",None,"Lahore"]
}
df= pd.DataFrame(data)
print(df)
print(df.isna())     #checks missing values
print(df.isna().sum())  #count missing values

df_dropped=df.dropna()
print(df_dropped)

mean_marks=df["marks"].mean()
print(mean_marks)

df_filled=df.copy()
df_filled["marks"]=df_filled["marks"].fillna(mean_marks)
df_filled["city"]=df_filled["city"].fillna("Unknown")
print(df_filled)

print(df)

missing_marks=df["marks"].isna()
print(missing_marks)
print(df[missing_marks])

df_marks_ok=df.dropna(subset=["marks"])  #checks only specific column
print(df_marks_ok)

missing_percent=df.isna().mean()*100   #percentage of missing values
print(missing_percent)
print(missing_percent.round(1))  #roundoff to 1 decimal


