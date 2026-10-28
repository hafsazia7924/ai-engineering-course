import pandas as pd

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar"],
    "math": [72, 90, 65, 85, 85],
    "english": [80, 70, 88, 92, 60],
}
df = pd.DataFrame(data)
print(df)
#Sort by english, smallest first
sorted_df = df.sort_values("english")
print(sorted_df)

#sort from large to small
top_df = df.sort_values("english", ascending=False)
print(top_df)

#sort by math 1st,then sort by english
rank_df = df.sort_values(["math", "english"], ascending=False)
print(rank_df)
#Rename two columns
renamed_df = df.rename(columns={"math": "math_marks", "english": "english_marks"})
print(renamed_df)
print(list(renamed_df.columns))
#Silent error
test_df = df.rename(columns={"Math_marks": "m"})     #no change because m is M
print(list(test_df.columns))

#new column: total of both subjects
df["total"] = df["math"]+df["english"]
print(df)
#new column :average of both subjects
df["average"] = df["total"]/2
print(df)
#trap 
df["wrong"] = df["math"]+df["english"]/2       #python does/ first then +
df["right"] = (df["math"] + df["english"]) / 2
print(df)
#new column : True is average is > 70
df["passed"] = df["average"] > 76
print(df[["name", "average", "passed"]])

#Sort by average biggest first
top_df=df.sort_values("average", ascending=False)
print(top_df[["name", "average"]])

#Adding a plain list as column
df["city"] = ["Lahore", "Multan", "Lahore", "Karachi", "Multan"]
print(df)