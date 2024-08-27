import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)

my_cursor = mydb.cursor();

# my_cursor.execute("CREATE DATABASE users_python_prac")

my_cursor.execute("SHOW DATABASES")
my_cursor.execute("insert into users_python values")
for db in my_cursor:
    print(db)