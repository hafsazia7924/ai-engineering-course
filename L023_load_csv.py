import pandas as pd

df=pd.read_csv("students.csv")
print(df)
print(df.head(3))
print(df.tail(2))
print(df.shape)
df.info()    #print(df.info)will b wrong
print(df.describe().round(2))    #round2 : round every num to 2 decimals

#practical
import pandas as pd
df=pd.read_csv("products.csv")
print(df.head(2))
print(df.shape)
df.info()
print(df.describe().round(2))
# Marks column is float64
