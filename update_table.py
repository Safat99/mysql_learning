import mysql.connector as sql

mydb = sql.connect(
    user = 'root',
    host = 'localhost',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()

# query = "update customers SET address = 'buet hall' WHERE address LIKE '%Dhaka%'"

query2 = "update customers set address = %s where address = %s"
val = ("BUET AH HALL","buet hall")

# cursor.execute(query)
cursor.execute(query2,val)

mydb.commit()

print(cursor.rowcount,"record(s) changed!")