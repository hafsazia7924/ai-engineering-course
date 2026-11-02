# Count pilot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "name": ["Ali", "Sara", "Usman", "Hina", "Omar", "Ayesha", "Bilal", "Zara"],
    "city": ["Lahore", "Multan", "Lahore", "Multan", "Lahore", "Karachi", "Multan", "Lahore"],
    "marks": [82, 65, 74, 58, 90, 71, 49, 85]
}
df = pd.DataFrame(data)
# Countplot: students in each city
sns.countplot(data=df, x="city")
plt.title("Students per city")
plt.savefig("city_count.png")
plt.show()
# Same numbers without a chart
print(df["city"].value_counts())

# Boxplot: one box for all marks
sns.boxplot(data=df, x="marks")
plt.title("Marks of all students")
plt.savefig("marks_box.png")
plt.show()

# Boxplot: one box per city
sns.boxplot(data=df, x="city", y="marks")
plt.title("Marks by city")
plt.savefig("city_box.png")
plt.show()

# A new table with one strange value
df_out = pd.DataFrame({"marks": [60, 62, 63, 65, 66, 68, 70, 12]})
sns.boxplot(data=df_out, x="marks")
plt.title("Marks with an outlier")
plt.savefig("outlier_box.png")
plt.show()


# L034 Practical: Orders table
# Task 1
orders_data = {
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "city": ["Lahore", "Multan", "Lahore", "Karachi", "Multan", "Lahore", "Karachi", "Multan", "Lahore", "Karachi"],
    "amount": [450, 520, 480, 510, 495, 530, 470, 5000, 500, 505]
}
df_orders = pd.DataFrame(orders_data)
# Task 2
print(df_orders.shape)
#Task 3
print(df_orders["city"].value_counts())
# Task 4
sns.countplot(data=df_orders, x="city")
plt.title("Orders per city")
plt.savefig("orders_count.png")
plt.show()
# Task 5
sns.boxplot(data=df_orders, x="amount")
plt.title("Order amounts")
plt.savefig("order_box.png")
plt.show()
#Task 6
print(df_orders.loc[df_orders["amount"] > 1000, ["order_id", "city"]])