import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'hala_madrid@123',
    database = 'test_db'
)

cursor = mydb.cursor()

# cursor.execute("CREATE TABLE customers (name VARCHAR(20), address VARCHAR(100))")

###############>>> adding pk after an existing table
# cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

## altering column name 
cursor.execute("ALTER TABLE customers RENAME COLUMN id TO customer_id")
cursor.close()