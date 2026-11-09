import sqlite3

# Task 1: Build the database
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, category TEXT, price INTEGER)")
cur.execute("""INSERT INTO books (id, title, category, price)
              VALUES 
                 (1, 'Python Basics', 'Programming', 1200), 
                 (2, 'Data Science 101', 'Data', 1500),
                 (3, 'SQL Made Easy', 'Data', 900),
                 (4, 'AI for Everyone', 'AI', 1800),
                 (5, 'Clean Code', 'Programming', 1400),
                 (6, 'Deep Learning', 'AI', 2200) 
            """)
cur.execute("CREATE TABLE sales(id INTEGER PRIMARY KEY, book_id INTEGER, quantity INTEGER)")
cur.execute("""INSERT INTO sales (id, book_id, quantity)
            VALUES
                (1, 1, 2),
                (2, 2, 1),
                (3, 1, 4),
                (4, 4, 2),
                (5, 3, 4),
                (6, 2, 1),
                (7, 4, 1),
                (8, 5, 1)
            """)
cur.execute("SELECT COUNT(*) FROM books")
print(cur.fetchall())
cur.execute("SELECT COUNT(*) FROM sales")
print(cur.fetchall())

# Task 2: Expensive books
cur.execute("SELECT title, price FROM books WHERE price > 1300 ORDER BY price DESC")
print(cur.fetchall())

# Task 3: Price summary
cur.execute("SELECT COUNT(*), AVG(price), MAX(price) FROM books")
print(cur.fetchall())

# Task 4: Average price per category
cur.execute("SELECT category, AVG(price) FROM books GROUP BY category ORDER BY AVG(price) DESC")
print(cur.fetchall())

# Task 5: Copies sold per book
cur.execute("""SELECT books.title, SUM(sales.quantity) AS total_sold 
               FROM books INNER JOIN sales ON books.id = sales.book_id
               GROUP BY books.id, books.title
               ORDER BY total_sold DESC
            """)
print(cur.fetchall())

# Task 6: Books never sold
cur.execute("""SELECT books.title FROM books LEFT JOIN sales
               ON books.id = sales.book_id
               WHERE sales.id IS NULL
            """)
print(cur.fetchall())

# Task 7: Copies sold per category
cur.execute("""SELECT books.category, SUM(sales.quantity)
               FROM books INNER JOIN sales
               ON books.id = sales.book_id
               GROUP BY books.category
               ORDER BY SUM(sales.quantity) DESC
            """)
print(cur.fetchall())

conn.close()

# Task 8:Findings
# Best seller:Python Basics sold 6 copies, the most of any book, so keep it always in stock.
# Weakest category: AI sold only 3 copies, less than half of Programming (7), so it needs attention.
# Action: Deep Learning (price 2200, the highest) has zero sales, so try some discount and check if the highest price stop buyers.