import pandas as pd

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar", "Zara", "Bilal"],
    "city": ["Lahore", "Multan", "Lahore", "Multan", "Karachi", "Karachi", "Lahore"],
    "marks": [80, 90, 70, 60, 85, 79, 90],
}
df = pd.DataFrame(data)

#average marks of each city
print(df.groupby("city")["marks"].mean())
#total marks of each city
print(df.groupby("city")["marks"].sum())
#number of students in each city
print(df.groupby("city")["name"].count())
#average marks of each table as a normal table
print(df.groupby("city")["marks"].mean().reset_index())
#total marks of each city, highest first
city_total=df.groupby("city")["marks"].sum().reset_index()
print(city_total.sort_values("marks", ascending=False))
#mean, max and count of each city
print(df.groupby("city")["marks"].agg(["mean", "max", "sum"])) 


#practical
#Task 1
print(df.groupby("city")["marks"].min())
#Task 2
print(df.groupby("city")["marks"].sum().reset_index())
#Task 3
print(df.groupby("city")["marks"].mean())
#Task 4
city_total = df.groupby("city")["marks"].sum().reset_index()
print(city_total.sort_values("marks", ascending=True))
#Task 5
print(df.groupby("city")["marks"].agg(["mean", "max", "count"]))
#Task 6
avg_marks=df.groupby("city")["marks"].mean().reset_index()
print(round(avg_marks,1))