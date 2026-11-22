import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

data = {
    "brand": ["Dell", "HP", "Lenovo", "Apple", "Asus", "Dell"],
    "price": [85000, 92000, 78000, 250000, 99000, 120000],
}
df = pd.DataFrame(data)
# SQL and pandas together
df.to_sql("laptops", conn, index=False)  #store data frame in table laptops

df_cheap = pd.read_sql_query("SELECT * FROM laptops WHERE price < 100000", conn)
print(df_cheap)

df_avg = pd.read_sql_query("SELECT brand, AVG(price) AS avg_price FROM laptops GROUP BY brand ORDER BY brand", conn)
print(df_avg)
print(df_avg.shape)
conn.close()

# Practical
import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

# Task 1
data = {
    "name": ["Ali", "Sara", "Hina", "Omar", "Zain", "Maha"],
    "city": ["Lahore", "Karachi","Lahore", "Karachi", "Lahore", "Quetta"],
    "marks": [72, 85, 64, 91, 58, 77]
}
df = pd.DataFrame(data)

df.to_sql("students", conn, index=False)

# Task 2
df_pass = pd.read_sql_query("SELECT * FROM students WHERE marks >= 70", conn)
print(df_pass)

# Task 3
df_avg = pd.read_sql_query("SELECT city, AVG(marks) AS avg_marks FROM students GROUP BY city ORDER BY city", conn)
print(df_avg)
print(df_avg.shape)

conn.close()