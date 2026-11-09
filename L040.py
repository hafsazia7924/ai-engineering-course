import sqlite3

conn = sqlite3.connect(":memory:")  #:memory: create a temporary datbase in RAM 
cur = conn.cursor()

cur.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY, name TEXT, city TEXT)")
cur.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount INTEGER)")
cur.execute("INSERT INTO customers VALUES (1, 'Ali', 'Lahore'), (2, 'Sara', 'Karachi'), (3, 'Usman', 'Islamabad'), (4, 'Hina', 'Lahore')")
cur.execute("INSERT INTO orders VALUES (101, 1, 2500), (102, 2, 1800), (103, 1, 900), (104, 3, 4000), (105, 2, 1200)")
conn.commit()

cur.execute("SELECT * FROM orders")
print(cur.fetchall())

#Inner Join
cur.execute("""SELECT orders.id, customers.name, orders.amount FROM ORDERS INNER JOIN customers
ON orders.customer_id = customers.id ORDER BY ORDERS.ID""")  #Triple quotes let one string run over multiple lines
print(cur.fetchall())

#left Join
cur.execute("SELECT customers.name, orders.amount FROM customers LEFT JOIN orders ON customers.id = orders.customer_id ORDER BY customers.id, orders.id")
print(cur.fetchall())

#find rows with no match
cur.execute("SELECT customers.name FROM customers LEFT JOIN orders ON customers.id = orders.customer_id WHERE orders.id IS NULL")
print(cur.fetchall())

#Join by GROUP BY
cur.execute("""SELECT customers.name, SUM(orders.amount) AS total FROM customers LEFT JOIN orders 
ON customers.id = orders.customer_id GROUP BY customers.id, customers.name ORDER BY total DESC""")
print(cur.fetchall())

# Practical
# Task 1
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT, course TEXT)")
cur.execute("INSERT INTO students VALUES(1, 'Zain', 'BSCS'), (2, 'Mina', 'BSCS'), (3,'Bilal', 'BSIT'), (4,'Noor', 'BSIT')")
cur.execute("CREATE TABLE results(id INTEGER PRIMARY KEY, student_id INTEGER, subject TEXT, marks INTEGER)")
cur.execute("INSERT INTO results VALUES (1, 1, 'Math', 80), (2, 1, 'English', 70), (3,2, 'Math', 90), (4, 2, 'English', 50), (5, 3, 'Math', 55)")
conn.commit()
# Task 2
cur.execute("SELECT students.name, results.subject, results.marks FROM  students INNER JOIN results ON students.id = results.student_id ORDER BY results.marks DESC")
print(cur.fetchall())
# Task 3
cur.execute("SELECT students.name FROM students LEFT JOIN results ON students.id = results.student_id WHERE results.id  IS NULL")
print(cur.fetchall())
# Task 4
cur.execute("SELECT students.name, AVG(results.marks) AS average_marks FROM students LEFT JOIN results ON students.id = results.student_id GROUP BY students.id, students.name ORDER BY average_marks DESC")
print(cur.fetchall())

conn.close()