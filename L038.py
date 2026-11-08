import sqlite3

conn = sqlite3.connect("school.db")     #created a databse
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS students")      #created a table
cur.execute("CREATE TABLE students (id INTEGER, name TEXT, city TEXT, marks INTEGER)")
cur.execute("INSERT INTO students VALUES (1, 'Ali', 'Lahore', 85)")
cur.execute("INSERT INTO students VALUES(3, 'Usman', 'Lahore', 78)")
cur.execute("INSERT INTO students VALUES(4, 'Hina', 'Multan', 91)")
conn.commit()             #save the changes
cur.execute("SELECT name, marks FROM students WHERE marks > 70")
rows = cur.fetchall()             #to save in a variable
print(rows)

cur.execute("SELECT * FROM students")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT name, marks FROM students ORDER BY marks DESC")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 2")
rows = cur.fetchall()
print(rows)

cur.execute("SELECT name FROM students WHERE city = 'Lahore'")
rows = cur.fetchall()
print(rows)


# Practical
cur.execute("DROP TABLE IF EXISTS products")
cur.execute("CREATE TABLE products(id INTEGER, name TEXT, price INTEGER, stock INTEGER)") #creates a new table
cur.execute("INSERT INTO products VALUES(1, 'Pen', 50, 120)")
cur.execute("INSERT INTO products VALUES(2, 'Notebook', 180, 0)")
cur.execute("INSERT INTO products VALUES(3, 'Bag', 1500, 15)")
cur.execute("INSERT INTO products VALUES(4, 'Calculator', 650, 8)")
cur.execute("INSERT INTO products VALUES(5, 'Marker', 90, 0)")
conn.commit()
cur.execute("SELECT name, price FROM products WHERE price < 500 ORDER BY price ASC")
rows = cur.fetchall()
print(rows)
cur.execute("SELECT name, price FROM products ORDER BY price DESC LIMIT 2")
rows = cur.fetchall()
print(rows)
cur.execute("SELECT name FROM products WHERE stock = 0 ORDER BY price ASC")
rows = cur.fetchall()
print(rows)

conn.close()  #used once at the end