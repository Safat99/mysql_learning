import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE customers (name VARCHAR(20), address VARCHAR(100))")
cursor.close()