# L037: EDA routine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar", "Ayesha", "Bilal", "Zara", "Ali", "Faisal"],
    "city": ["Lahore", "Multan", "Lahore", "Karachi", "Multan", "Lahore", "Karachi", "Multan", "Lahore", "Karachi"],
    "age": [20, 21, 19, 22, 20, 21, 23, 20, 20, 22],
    "marks": [78, 85, 62, None, 55, 91, 70, 88, 78, 66],
    "hours": [10, 12, 6, 9, 5, 14, 8, 60, 10, 7],
}
df = pd.DataFrame(data)
# Step 1: size and first look
print(df.shape)
print(df.head())            #shows 1st five rows
df.info()  
# Step 2: missing values per column
print(df.isna().sum())
# Step 3: Copied rows
print(df.duplicated().sum())
# Step 4: Numbers Summary
print(df[["marks", "hours"]].describe().round(2))
# Step 5: Categories
print(df["city"].value_counts())
#step 6 and 7: Shape of data, outliers, relationships
fig, ax = plt.subplots(1, 3, figsize=(15, 4)) 

ax[0].hist(df["hours"], bins=5)
ax[0].set_title("Hours, histogram")

sns.boxplot(data=df, y="hours", ax=ax[1])
ax[1].set_title("Hours: Boxplot")

sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", ax=ax[2])
ax[2].set_title("Correlation")

fig.tight_layout()
plt.savefig("EDA_hours.png")
plt.show()

# Step 8: findings
# Finding 1: marks has 1 missing value, and row 8 is a copy of row 0.
# Finding 2: hours has an outlier (60), probably a typing mistake. It pulls the mean up.
# Finding 3: the outlier hides the real marks-hours relationship (0.55 instead of about 0.99)



# Code test
# Task 1
data_test = {
    "product": ["Pen", "Book", "Bag", "Cap", "Book", "Pen", "Bag", "Cap"],
    "price": [20, 150, 900, 120, 150, 20, 900, 5000],
    "sold": [50, 30, 8, 25, 30, 45, None, 10],
}
df_test = pd.DataFrame(data_test)
# Task 2
print(df_test.shape)
print(df_test.head())
df_test.info()
print(df_test.isna().sum())
# Task 3
print(df_test.duplicated().sum())
print(df_test[df_test.duplicated()])
# Task 4
print(df_test[["price", "sold"]].describe().round(2))
# Task 5
print(df_test["product"].value_counts())
# Task 6
totals = df_test.groupby("product")["sold"].sum().reset_index()
print(totals)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].bar(totals["product"], totals["sold"])
ax[0].set_title("Products sold")

sns.boxplot(data=df_test, y="price", ax=ax[1])
ax[1].set_title("Price: boxplot")

fig.tight_layout()
plt.savefig("L037_test.png")
plt.show()

# Finding 1: sold has one NaN value,Book row on 5th row is copy of 2nd row
# Finding 2: price has an outlier 5000 , it may be a typing mistake.
# Finding 3: Outlier is affecting the mean value

