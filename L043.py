import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE laptops (id INTEGER PRIMARY KEY, brand TEXT, price INTEGER)")
cur.execute("""
INSERT INTO laptops (id, brand, price) VALUES
    (1, 'Dell', 85000),
    (2, 'Dell', 120000),
    (3, 'Dell', 65000),
    (4, 'HP', 70000),
    (5, 'HP', 95000),
    (6, 'HP', 60000),
    (7, 'HP', 80000),
    (8, 'Lenovo', 90000),
    (9, 'Lenovo', 105000),
    (10, 'Apple', 250000)
""")
conn.commit()

#groups without any filter
query = "SELECT brand, COUNT(*) FROM laptops GROUP BY brand ORDER BY brand"
cur.execute(query)
rows = cur.fetchall()
print(rows)  # every brand with its count

#HAVING
query = """
SELECT brand, COUNT(*)
FROM laptops
GROUP BY brand
HAVING COUNT(*) >= 2
ORDER BY brand
"""
cur.execute(query)
rows = cur.fetchall()
print(rows)  # only brands with 2 or more laptops

#WHERE and HAVING together
query = """
SELECT brand, COUNT(*)
FROM laptops
WHERE price < 100000
GROUP BY brand
HAVING COUNT(*) >= 2
ORDER BY brand
"""
cur.execute(query)
rows = cur.fetchall()
print(rows)  # cheap laptops only, then brands with 2 or more

#HAVING, filtering groups (Part 2 of 2)
query = """
SELECT brand, AVG(price)
FROM laptops
GROUP BY brand
HAVING AVG(price) > 80000
ORDER BY brand
"""
cur.execute(query)
rows = cur.fetchall()
print(rows)  # brands whose average price is above 80000
