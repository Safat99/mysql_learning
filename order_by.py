## sorting the query result

import mysql.connector as sql

mydb = sql.connect(
    user='root',
    host= 'localhost',
    password='hala_madrid@123',
    database='test_db'
)

cursor = mydb.cursor()

############## order_by normally ascending order e kore ##############
query = "SELECT * FROM customers ORDER BY name"
cursor.execute(query)
result = cursor.fetchall()

for i in result:
    print(i)

############## order by for desencding order ############
print('\norder by name desc-------------------')
query2 = "SELECT * FROM customers ORDER BY name DESC"
cursor.execute(query2)
result2 = cursor.fetchall()

for i in result2:
    print(i)
