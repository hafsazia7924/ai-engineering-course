import pandas as pd
data={
    "name": ["Ali", "Sara", "Usman", "Hina"],
    "marks": [78, 91, 65, 84],
    "city": ["Lahore", "Karachi", "Quetta", "Lahore"],
}
df=pd.DataFrame(data)
print(df.iloc[0])
print(df.iloc[1,1])
print(df.iloc[0:2])
print(df.iloc[:, 1])  #one column

df_named=df.set_index("name")
print(df_named.loc["Sara"])
print(df_named.loc["Usman","marks"])
print(df_named.loc["Ali":"Usman"])
print(df_named.loc[df_named["marks"]>80,"city"])
print(df_named.loc[:,["marks","city"]])

#practical
import pandas as pd

data = {
    "title": ["Python Basics", "Data Science", "Deep Learning", "SQL Guide", "Statistics"],
    "price": [1200, 2500, 3000, 900, 1800],
    "pages": [300, 450, 520, 210, 380],
}
df = pd.DataFrame(data)
print(df.iloc[2])
print(df.iloc[3, 1])
print(df.iloc[0:3])
df_titled=df.set_index("title")
print(df_titled.loc["Statistics","price"])
print(df_titled.loc["Data Science":"SQL Guide"])
print(df.loc[df["price"]>1500,["title","pages"]])