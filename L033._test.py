import pandas as pd 
import matplotlib.pyplot as plt 

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar", "Ayesha", "Bilal", "Zara"],
    "city": ["Lahore", "Multan", "Lahore", "Multan", "Karachi", "Karachi", "Lahore", "Multan"],
    "hours": [2, 5, 3, 6, 1, 4, 7, 8],
    "marks": [45, 70, 55, 82, None, 66, 90, 95]
}
df = pd.DataFrame(data)
# Task 1
print(df.shape)
# Task 2
df["marks"] = df["marks"].fillna(0)
print(df["marks"])
# Task 3
print(df.loc[df["marks"] > 60, ["name", "marks"]])
# Task 4
avg_marks = df.groupby("city")["marks"].mean().reset_index()
print(avg_marks.sort_values("marks", ascending=False))
# Task 5
plt.hist(df["marks"], bins=4)
plt.title("Marks Histogram")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.savefig("marks_hist_test.png")
plt.show()
# Task 6
plt.scatter(df["hours"], df["marks"])
plt.title("Hours vs Marks")
plt.xlabel("hours")
plt.ylabel("marks")
plt.savefig("hours_marks_test.png")
plt.show()
# relationship is postive
# labours,work done