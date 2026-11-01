import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [40, 55, 60, 72, 85]

plt.plot(days, marks)
plt.title("Marks per day")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data = {
    "name": ["Ali", "Sara", "Usman", "Hina"],
    "city": ["Multan", "Lahore", "Multan", "Lahore"],
    "marks": [70, 85, 60, 90]
}
df = pd.DataFrame(data)

# One bar per student
plt.bar(df["name"], df["marks"])  #create bar graph
plt.title("Marks o Student")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.savefig("marks_bar.png")    #to save as png file
plt.show()

#chart 2-average marks per city
avg_df = df.groupby("city")["marks"].mean().reset_index()
plt.bar(avg_df["city"], avg_df["marks"])
plt.title("Average marks per city")
plt.xlabel("City")
plt.ylabel("Marks")
plt.show()

# Practical
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Bilal", "Zara"],
    "city": ["Multan", "Lahore", "Multan", "Lahore", "Multan", "Lahore"],
    "marks": [70, 85, 55, 90, 62, 48]
}

class_df = pd.DataFrame(data)
mask = class_df["marks"] > 60
passed_df = class_df.loc[mask,["name", "marks"]]
print(passed_df)
plt.bar(passed_df["name"], passed_df["marks"])
plt.title("Students above 60")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.savefig("passed_bar.png")
plt.show()