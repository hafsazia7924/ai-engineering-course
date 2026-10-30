import pandas as pd

df = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ali", "Sara", "Usman", "Hina"],
    "marks": [78, 91, 65, 84]
})

df_city = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "city": ["Multan", "Lahore", "Karachi", "Quetta"]
})
df_all = pd.merge(df, df_city, on="student_id")   #merge only common columns(inner merge)
print(df_all)
df_left = pd.merge(df, df_city, on="student_id", how="left") #merge with all left table values,NaN filling
print(df_left)
df_right = pd.merge(df, df_city, on="student_id", how="right")#merge with all right table columns
print(df_right)
df_outer = pd.merge(df, df_city, on="student_id", how="outer") #merge with every column of both tables
print(df_outer)

#renaming for different table name concept
df_city = df_city.rename(columns={"student_id" : "id"})
print(df_city)
#fix when both keys have diferent name
df_diff = pd.merge(df, df_city, left_on="student_id", right_on="id")
print(df_diff)


#Practical
import pandas as pd

df_orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "cust_id": [1, 2, 2, 4, 5],
    "amount": [2500, 1800, 3200, 900, 4100]
})

df_cust = pd.DataFrame({
    "id": [1, 2, 3, 5],
    "name": ["Ayesha", "Bilal", "Chand", "Danish"],
    "city": ["Multan", "Lahore", "Karachi", "Multan"]
})

#Task 1
df_inner = pd.merge(df_orders, df_cust, left_on="cust_id", right_on="id")
print(len(df_inner))
#Task 02
df_report = pd.merge(df_orders, df_cust, left_on="cust_id", right_on="id", how="left")
print(df_report)
#Task 03
print(df_report.isna().sum())
#Task 04
mask = df_report["name"].isna()
print(df_report.loc[mask])
#Task 5
print(df_report.groupby("city")["amount"].sum().reset_index().sort_values("amount", ascending=False))
#Task 6
df_report["amount_k"] = df_report["amount"] / 1000
print(df_report[["order_id","amount_k"]])