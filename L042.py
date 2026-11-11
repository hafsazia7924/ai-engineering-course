import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE phones (id INTEGER PRIMARY KEY, brand TEXT, price INTEGER, ram INTEGER)")
phones_data = [
    (1, "Samsung", 45000, 8),
    (2, "Apple", 250000, 6),
    (3, "Xiaomi", 38000, 6),
    (4, "Samsung", 32000, 4),
    (5, "Oppo", 41000, 8),
    (6, "Xiaomi", 29000, 4),
    (7, "Apple", 180000, 4),
    (8, "Infinix", 27000, 6),
]
cur.executemany("INSERT INTO phones VALUES (?, ?, ?, ?)", phones_data)
conn.commit()

# AND
cur.execute("SELECT brand, price FROM phones WHERE brand = 'Samsung' AND price < 40000")
print(cur.fetchall())

# OR
cur.execute("SELECT brand, price FROM phones WHERE brand = 'Apple' OR brand = 'Oppo'")
print(cur.fetchall())

# The biggest trap: brackets
cur.execute("SELECT brand, price, ram FROM phones WHERE brand = 'Samsung' OR brand = 'Xiaomi' AND ram = 4")
print(cur.fetchall())

cur.execute("SELECT brand, price, ram FROM phones WHERE (brand = 'Samsung' OR brand = 'Xiaomi') AND ram = 4")
print(cur.fetchall())

# IN
cur.execute("SELECT brand, price FROM phones WHERE brand IN ('Apple', 'Oppo', 'Infinix')")
print(cur.fetchall())

# BETWEEN
cur.execute("SELECT brand, price FROM phones WHERE price BETWEEN 30000 AND 40000")
print(cur.fetchall())

# Search by patteren
cur.execute("SELECT brand, price FROM phones WHERE brand LIKE 'X%'")
print(cur.fetchall())

cur.execute("SELECT brand, price FROM phones WHERE brand LIKE '%i%'")
print(cur.fetchall())

#remove repeated rows
cur.execute("SELECT DISTINCT brand FROM phones")
print(cur.fetchall())

cur.execute("SELECT DISTINCT ram FROM phones")
print(cur.fetchall())

# Practical
cur.execute("CREATE TABLE laptops (id INTEGER PRIMARY KEY, brand TEXT, price INTEGER, ram INTEGER)")
laptops_data = [
    (1, "Dell", 95000, 8),
    (2, "HP", 120000, 16),
    (3, "Lenovo", 85000, 8),
    (4, "Dell", 150000, 16),
    (5, "Asus", 110000, 16),
    (6, "HP", 78000, 8),
    (7, "Lenovo", 135000, 16),
    (8, "Acer", 70000, 4),
]
cur.executemany("INSERT INTO laptops VALUES (?, ?, ?, ?)", laptops_data)
conn.commit()

# Task 1
cur.execute("SELECT brand, price, ram FROM laptops WHERE (brand = 'Dell' OR brand = 'HP') AND ram = 16")
print(cur.fetchall())

# Task 2
cur.execute("SELECT brand, price FROM laptops WHERE brand IN ('Lenovo', 'Acer', 'Asus') AND price BETWEEN 7000 AND 11000")
print(cur.fetchall())

# Task 3
cur.execute("SELECT brand, price FROM laptops WHERE brand LIKE 'H%'")
print(cur.fetchall())

#Task 4
cur.execute("SELECT DISTINCT brand FROM laptops")
print(cur.fetchall())