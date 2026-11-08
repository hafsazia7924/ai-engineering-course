import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("CREATE TABLE orders(id INTEGER, product TEXT, city TEXT, amount INTEGER)")
cur.execute("INSERT INTO orders VALUES (1, 'Book', 'Lahore', 500)")
cur.execute("INSERT INTO orders VALUES (2, 'Pen', 'Karachi', 100)")
cur.execute("INSERT INTO orders VALUES (3, 'Book', 'Karachi', 700)")
cur.execute("INSERT INTO orders VALUES (4, 'Bag', 'Lahore', 1500)")
cur.execute("INSERT INTO orders VALUES (5, 'Pen', 'Lahore', 150)")
cur.execute("INSERT INTO orders VALUES (6, 'Book', 'Lahore', 900)")
cur.execute("INSERT INTO orders VALUES (7, 'Bag', 'Karachi', 1200)")
cur.execute("INSERT INTO orders VALUES (8, 'Pen', 'Karachi', 50)")
conn.commit()

cur.execute("SELECT COUNT(*), SUM (amount), AVG(amount), MIN(amount), MAX(amount) FROM orders")
summary = cur.fetchone()    #aggregate functions return one row so fetch one
print(summary)

cur.execute("SELECT COUNT(*), SUM(amount), AVG(amount) FROM orders WHERE product = 'Book'")
book_summary = cur.fetchone()
print(book_summary)

#sumary per group(one row per group)
#a normal column next to an aggregate, you need GROUP BY(otherwise it's a silent error)
cur.execute("SELECT product, COUNT(*), SUM(amount) FROM orders GROUP BY product")
product_totals = cur.fetchall()
print(product_totals)

cur.execute("SELECT city, SUM(amount) FROM orders GROUP BY city ORDER BY SUM(amount) DESC")
city_totals = cur.fetchall()
print(city_totals)

#null value
cur.execute("INSERT INTO orders VALUES(9, 'Pen', 'Lahore', NULL)")
conn.commit()

cur.execute("SELECT COUNT(*), COUNT(amount), SUM(amount), AVG(amount) FROM orders")
null_check = cur.fetchone()
print(null_check)


# Practical
cur.execute("DROP TABLE IF EXISTS marks")
cur.execute("CREATE TABLE marks (id INTEGER, student TEXT, subject TEXT, score INTEGER)")
cur.execute("INSERT INTO marks VALUES (1, 'Ali', 'Math', 80)")
cur.execute("INSERT INTO marks VALUES (2, 'Sara', 'Math', 90)")
cur.execute("INSERT INTO marks VALUES (3, 'Ali', 'Physics', 70)")
cur.execute("INSERT INTO marks VALUES (4, 'Sara', 'Physics', 60)")
cur.execute("INSERT INTO marks VALUES (5, 'Usman', 'Math', 50)")
cur.execute("INSERT INTO marks VALUES (6, 'Usman', 'Physics', 40)")
cur.execute("INSERT INTO marks VALUES (7, 'Ali', 'Chemistry', 90)")
cur.execute("INSERT INTO marks VALUES (8, 'Sara', 'Chemistry', 80)")
conn.commit()

cur.execute("SELECT COUNT(*), AVG(score) FROM marks")
avg_score = cur.fetchone()
print(avg_score)

cur.execute("SELECT MAX(score), MIN(score) FROM marks WHERE SUBJECT = 'Math'")
math_score = cur.fetchone()
print(math_score)

cur.execute("SELECT student, SUM(score) FROM marks GROUP BY student ORDER BY SUM(score) DESC")
students_score = cur.fetchall()
print(students_score)

cur.execute("SELECT subject, MAX(score) FROM marks GROUP BY subject ORDER BY subject ASC")
subject_marks = cur.fetchall()
print(subject_marks)

cur.execute("INSERT INTO marks VALUES(9, 'Usman', 'Chemistry', NULL)")
conn.commit()
cur.execute("SELECT COUNT(*), COUNT(score), AVG(score) FROM marks")
null_score = cur.fetchone()
print(null_score)

conn.close()