import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()

query = "DELETE FROM customers WHERE address = 'Highway 21'"
cursor.execute(query)
######### if we omit the WHERE clause, all records will be removed

mydb.commit()

print(cursor.rowcount, "record(s) deleted")


#### to prevent sql injection we have to use placeholder %s on the query
### it is considered a good practice to escape the values of any query 
