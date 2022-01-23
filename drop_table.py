import mysql.connector as sql

mydb = sql.connect(
    user='root',
    host= 'localhost',
    password='hala_madrid@123',
    database='test_db'
)

cursor = mydb.cursor()

query = 'DROP TABLES customers'
#query = 'DROP TABLES IF EXISTS customers"
### >> if exists statement

cursor.execute(query)
