import pandas as pd

data = {
    "name": ["Ali", "Sara", "Usman"],
    "marks": ["85", "92", "78"],
}
df = pd.DataFrame(data)
df.info()
#fix
df["marks"] = df["marks"].astype(int)
df.info()
print(df["marks"].mean())

#if the data is not convertable
data2 = {
    "name": ["Ali", "Sara", "Usman"],
    "marks": ["85", "abc", "78"],
}
df2 = pd.DataFrame(data2)
df2["marks"] = pd.to_numeric(df2["marks"], errors="coerce")
print(df2)
df2.info()
print(df2.isna().sum())

#practical

#Task 1
data3 = {
    "product": ["Pen", "Book", "Bag", "Cap"],
    "price": ["250", "400", "n/a", "150"],
    "qty": ["2", "5", "1", "4"],
}
df3=pd.DataFrame(data3)
#Task 2
df3.info()
#Task 3
df3["qty"] = df3["qty"].astype(int)
#Task 4
df3["price"] = pd.to_numeric(df3["price"], errors="coerce")
#Task 5
df3.info()
#Task 6
print(df3.isna().sum())
#Task 7
average_num = df3["price"].mean()
print(round(average_num, 1))