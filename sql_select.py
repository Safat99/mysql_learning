import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

# cursor = mydb.cursor()
cursor = mydb.cursor(buffered=True) # fetchone er pore cursor execute e problem solve er jonne

# ########################### selecting all from the tables ##########
print("FETCHING ALL\n")
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()
#fetchall() method fetches all rows from the last executed statement

for i in result:
    print(i)

# ################## selecting some attributes ########################3
print("\nnow only selecting some columns\n")
cursor.execute("SELECT name, address FROM customers")
result2 = cursor.fetchall()

for i in result2:
    print(i)


############ fetching one row ################
print("\nfetching one row by cursor.fecthone()")
cursor.execute('SELECT * FROM customers')
result3 = cursor.fetchone()

print(result3)


