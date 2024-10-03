import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234",
                       database = "db1")

db_cursor = mydb.cursor()
s = "select * from book"
db_cursor.execute(s)
result = db_cursor.fetchall()

for rec in result:
    print(rec)