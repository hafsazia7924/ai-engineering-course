import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar", "Zara", "Bilal", "Noor"],
    "marks": [49, 62, 65, 70, 75, 81, 88, 90],
    "study_hours": [1, 2, 2, 3, 4, 4, 5, 6],
}
df = pd.DataFrame(data)
# fig is page and ax is chart below box
fig, ax = plt.subplots(1, 2, figsize=(10, 4))  #plt.subplots(row, col, figsize(w, h)) in inches
ax[0].hist(df["marks"], bins=4)     #chart 1
ax[0].set_title("Marks spread")

ax[1].scatter(df["study_hours"], df["marks"])  #chart 2
ax[1].set_title("Hours vs Marks")

plt.savefig("L036_first.png")
plt.show()

# Part 2: 2 x 2 grid with a new column
df["absences"] = [9, 6, 6, 4, 3, 2, 1, 0]

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].hist(df["marks"], bins=4)    #chart 1
ax[0, 0].set_title("Marks Spread")

ax[0,1].scatter(df["study_hours"], df["marks"])   #chart 2
ax[0,1].set_title("Hours vs Marks")

ax[1,0].bar(df["name"], df["marks"])      #chart 3
ax[1,0].set_title("Marks per student")

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax[1, 1])  #chart 4
ax[1,1].set_title("Correlation")

fig.tight_layout()      #no overlap in tiles and labels
plt.savefig("L036_grid.png")
plt.show()

# Practical

shop_data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "sales": [12000, 15000, 14000, 18000, 21000, 25000],
    "customers": [40, 52, 47, 60, 70, 85],
    "rain_mm": [30, 5, 20, 2, 0, 0],
}
df_shop = pd.DataFrame(shop_data)
fig, ax = plt.subplots(2, 2)
# Task 1
# Shows bar graph for sales per day in top left box 
ax[0, 0].bar(df_shop["day"], df_shop["sales"])
ax[0, 0].set_title("Sales per day")
# Task 2
# Shows scatter plot between customers and sales in top right block
ax[0, 1].scatter(df_shop["customers"], df_shop["sales"])
ax[0, 1].set_title("Customer vs sales")
ax[0, 1].set_xlabel("Customers")
ax[0, 1].set_ylabel("sales")
# Task 3
# Shows histogram for sales spread in 3 bars in bottom left box
ax[1, 0].hist(df_shop["sales"], bins=3)
ax[1, 0].set_title("Sales Spread")
# Task 4
# Shows correlation in customer, sales and rain in bottom right box
sns.heatmap(df_shop.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", ax=ax[1, 1])
ax[1, 1].set_title("Correlation")
# Task 5
# It avoids the overlap in titles and labels, then print after saving the chart page fig
fig.tight_layout()
plt.savefig("L036_shop.png")
plt.show()