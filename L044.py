import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE laptops (name TEXT, brand TEXT, price INTEGER, ram INTEGER)")
cur.execute("""
INSERT INTO laptops VALUES
('Inspiron', 'Dell', 85000, 8),
('XPS', 'Dell', 110000, 16),
('Pavilion', 'HP', 70000, 8),
('Envy', 'HP', 95000, 16),
('IdeaPad', 'Lenovo', 60000, 8),
('ThinkPad', 'Lenovo', 105000, 16),
('VivoBook', 'Asus', 75000, 8),
('ROG', 'Asus', 150000, 16)
""")
conn.commit()

#manual two-step way (without a subquery)
cur.execute("SELECT AVG(price) FROM laptops")
print(cur.fetchall())
cur.execute("SELECT name, price FROM laptops WHERE price > 93750")
print(cur.fetchall())

#The subquery way (one command)
cur.execute("""
SELECT name, price
FROM laptops
WHERE price > (SELECT AVG(price) FROM laptops)
""")
print(cur.fetchall())

#Examle 1: the most expensive laptop
cur.execute("""
SELECT name, price
FROM laptops
WHERE price = (SELECT MAX(price) FROM laptops)
""")
print(cur.fetchall())

#Example 2: cheaper than the average Dell
cur.execute("""
SELECT name, price
FROM laptops
WHERE price < (SELECT AVG(price) FROM laptops WHERE brand = 'Dell')
""")
print(cur.fetchall())

#Subquery with IN (the inner query returns a list)
cur.execute("""
SELECT name, brand
FROM laptops
WHERE brand IN (SELECT brand FROM laptops WHERE price > 100000)
""")
print(cur.fetchall())

#NOT IN (the opposite)
cur.execute("""
SELECT name, brand
FROM laptops
WHERE brand NOT IN (SELECT brand FROM laptops WHERE price > 100000)
""")
print(cur.fetchall())

#Practical 
cur.execute("CREATE TABLE students (name TEXT, city TEXT, marks INTEGER)")
cur.execute("""
INSERT INTO students VALUES
('Ali', 'Multan', 72),
('Sara', 'Lahore', 88),
('Bilal', 'Multan', 65),
('Hina', 'Karachi', 91),
('Zain', 'Lahore', 54),
('Maryam', 'Karachi', 80)
""")
conn.commit()

# Task 1
cur.execute("""
              SELECT name, marks FROM students 
              WHERE marks > (SELECT AVG(marks) FROM students)
            """)
print(cur.fetchall())

# Task 2
cur.execute("""
             SELECT name, marks FROM students
             WHERE marks IN (SELECT MIN(marks) FROM students)
            """)
print(cur.fetchall())

# Task 3
cur.execute("""
            SELECT name, city FROM students
            WHERE city IN (SELECT city FROM students WHERE marks > 85)
           """)
print(cur.fetchall())

# Task 4 
cur.execute("""
            SELECT name, city FROM students
            WHERE city NOT IN (SELECT city FROM students WHERE marks > 85)
           """)
print(cur.fetchall())

conn.close()