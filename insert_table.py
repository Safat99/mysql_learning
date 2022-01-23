import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()

query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(query,val)

mydb.commit()

print(cursor.rowcount, "record inserted!")

#executemany() >>> list of tuples
query2 = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val2 =[
    ('Zia', 'Dortmund 2nd street'),
    ('Zayed', '23rd street Mohakhali DOHS'),
    ('Zunayed', 'xyz steet Dhaka 1000')
]

cursor.executemany(query2, val2)
mydb.commit()
print(cursor.rowcount, "was inserted!!")
