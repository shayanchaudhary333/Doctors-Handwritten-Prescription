import pymysql

# Create a connection to the database
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Shayan@123',
    database='login_page'
)

# Check if connection is successful
if connection:
    cursor = connection.cursor()
    print("Successfully connected to the database")
