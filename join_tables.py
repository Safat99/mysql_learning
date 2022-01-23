##frst make two tables whom can be connected by some relations
import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()

print('----orders table created------')


query = "CREATE TABLE orders (order_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, date VARCHAR(30))"
cursor.execute(query)

print("-------insertation of orders table ------")

query = "INSERT INTO orders (customer_id, date) VALUES (%s, %s)"
val = [
    (1, 'may 1st'),
    (1,'june last'),
    (3, 'sept 4th'),
    (2, 'nov 10')
]

cursor.executemany(query, val)
mydb.commit()
print(cursor.rowcount, "was insterted")

query = "SELECT * FROM orders\
    INNER JOIN customers\
    ON orders.customer_id = customers.customer_id\
    "

cursor.execute(query)

result = cursor.fetchall()

for i in result:
    print(i)
