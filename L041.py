import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, stock INTEGER)")
# Add three rows with one commaND
product_rows = [
    (1, "Pen", 20, 100),
    (2, "Notebook", 150, 40),
    (3, "Bag", 1200, 5),
]
cur.executemany("INSERT INTO products VALUES(?, ?, ?, ?)", product_rows)
conn.commit()

cur.execute("SELECT * FROM products")
print(cur.fetchall())

# Change the price of the Pen
cur.execute("UPDATE products SET price = 25 WHERE name = 'Pen'")
conn.commit()

cur.execute("SELECT * FROM products WHERE name = 'Pen'")
print(cur.fetchall())

# Ten notebooks were sold, so stock goes down by 10
cur.execute("UPDATE products SET stock = stock - 10 WHERE id = 2")
conn.commit()

cur.execute("SELECT * FROM products WHERE id = 2")
print(cur.fetchall())

# Look first: which rows will be deleted?
cur.execute("SELECT * FROM products WHERE stock < 10")
print(cur.fetchall())

# Now delete the same rows
cur.execute("DELETE FROM products WHERE stock < 10")
conn.commit()

cur.execute("SELECT * FROM products")
print(cur.fetchall())

# Mistake on purpose: no WHERE
cur.execute("UPDATE products SET price = 0")

cur.execute("SELECT name, price FROM products")
print(cur.fetchall())

# Undo it before commit
conn.rollback()

cur.execute("SELECT name, price FROM products")
print(cur.fetchall())

# Practical
# Task 1
book_rows = [
    (1, "Python Basics", 500, 12),
    (2, "SQL Guide", 700, 3),
    (3, "Data Science", 900, 0),
    (4, "AI Handbook", 1100, 8) 
]
cur.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, price INTEGER, copies INTEGER)")
cur.executemany("INSERT INTO books VALUES(?, ?, ?, ?)", book_rows)
conn.commit()
cur.execute("SELECT * FROM books")
print(cur.fetchall())

# Task 2
cur.execute("UPDATE books SET price = 750 WHERE title = 'SQL Guide'")
conn.commit()

cur.execute("SELECT * FROM books WHERE TITLE = 'SQL Guide'")
print(cur.fetchall())

# Task 3
cur.execute("UPDATE books SET copies = copies-5 WHERE title = 'AI Handbook'")
conn.commit()

cur.execute("SELECT * FROM books WHERE title = 'AI Handbook'")
print(cur.fetchall())

# Task 4
cur.execute("SELECT * FROM books WHERE copies = 0")
print(cur.fetchall())

cur.execute("DELETE FROM books WHERE COPIES = 0")
conn.commit()

cur.execute("SELECT title, copies FROM books")
print(cur.fetchall())

# Task 5
cur.execute("UPDATE books SET price = 1")

cur.execute("SELECT title, price FROM books")
print(cur.fetchall())

conn.rollback()

cur.execute("SELECT title, price FROM books")
print(cur.fetchall())

# Task 6(comments about Task 5)
# The mistake changed the price of all 3 rows to 1 and SQL showed no error
# Rollback matters because it restored the 3 correct prices before the wrong data was saved