import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 6],
    "marks": [45, 55, 52, 68, 72, 80],
    "phone": [5, 4, 4, 3, 3, 2],
    "shoe_size": [7, 6, 8, 8, 7, 6]
})

# Table of all pairs
print(df.corr().round(2))           # give table of r values(-, + tells direction, distance from 0: strength)
# One pair, and one column against all others
print(df["hours"].corr(df["marks"].round(2)))
# One column against all others
print(df.corr()["marks"].round(2).sort_values(ascending=False))
# Heat map
corr_table = df.corr()
sns.heatmap(corr_table, annot=True, fmt=" .2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation heatmap")
plt.savefig("heatmap.png")
plt.show()
#An outlier can change r
df_out = df.copy()
df_out.loc[5, "marks"] = 20
print(df_out["hours"].corr(df_out["marks"].round(2)))

# Quiz
#Practical
data_shop = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "temp": [24, 28, 31, 35, 38],
    "cold_drinks":[30, 45, 60, 85, 100],
    "umberallas": [8, 5, 2, 1, 0],
    "shop_rent": [500, 500, 500, 500, 500]
}
df_shop = pd.DataFrame(data_shop)
corr_shop = df_shop.corr(numeric_only=True)
#Task 1
print(corr_shop.round(2))
# Task 2
print(corr_shop["cold_drinks"].round(2).sort_values(ascending=False))
# Task 3
sns.heatmap(corr_shop, annot=True, fmt=" .2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Heatmap for shop")
plt.savefig("heatmap_shop.png")
plt.show()