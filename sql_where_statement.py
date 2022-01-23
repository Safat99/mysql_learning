import mysql.connector as sql

mydb = sql.connect(
    host='localhost',user='root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()


################ by using where in the query we can filter the queries ########
print("\nfiltering with specific address>>")
query = "SELECT * FROM customers WHERE address ='Dortmund 2nd street'"
cursor.execute(query)
result = cursor.fetchall()

for i in result:
    print(i)

####################### wildcard characters #############33
print("selecting records where the address contains the word 'Dhaka'")
query2 = "SELECT * FROM customers WHERE address LIKE '%Dhaka%'"
cursor.execute(query2)
result2 = cursor.fetchall()

for i in result2:
    print(i)


########### preventing SQL Injection ############
## sql injection is a web hack technique... to prevent it >> 
# when query values are provided by the users we have to escape the values
# mysql.connector has the escape query values
print("\n sql injection--outputs----------")
query3 = "SELECT * FROM customers WHERE address = %s"
adr = ('Highway 21',)

cursor.execute(query3, adr)
result3 = cursor.fetchall()

for i in result3:
    print(i)