import pandas as pd

#Task 01
data = {
    "customer": ["Ayesha", "Bilal", "Ayesha", "Zara", "Bilal", "Omar"],
    "item": ["Shoes", "Bag", "Shoes", "Watch", "Cap", "Bag"],
    "amount": [2500, 1800, 2500, 3200, 2100, 1500],
}
df_orders = pd.DataFrame(data)
print(df_orders)
#Task 2
df_mask = df_orders.duplicated()
print(df_mask)
#Task 3
df_unique = df_orders.drop_duplicates()
print(df_unique)
#Task 4
df_latest = df_orders.drop_duplicates(subset=["customer"], keep="last")
print(df_latest)
#Task 5
mask = df_unique["amount"] > 2000
print(df_unique.loc[mask, ["customer", "amount"]])
#Task 6
average_amount = df_unique["amount"].mean()
print(round(average_amount, 1))