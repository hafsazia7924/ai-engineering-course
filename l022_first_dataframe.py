import pandas as pd
data={
    "Name" : ["ali","Sara","Bilai"],
    "Math": [80, 90, 75],
    "City": ["Multan", "Lahore", "Karachi"],
}
df=pd.DataFrame(data)
print(df)
print(df["Math"])
print(df["Math"].mean())
high_math = df[df["Math"] > 78]
print(high_math)

#practical
import pandas as pd
fruit_shop={
    "Item": ["Apple", "Banana", "Mango", "Orange"],
"Price": [200, 120, 300, 150],
"Qty": [5, 12, 3, 8],
}
fs=pd.DataFrame(fruit_shop)
print(fs)
print(fs["Price"])
print(fs["Price"].mean())
greater_price=fs[fs["Price"]>140]
print(greater_price)
