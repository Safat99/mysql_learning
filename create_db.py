import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123'
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE test_db")
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)

cursor.close()
