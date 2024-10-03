import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234",
                       database = "db1")

db_cursor = mydb.cursor()
s = "UPDATE book SET price=price+10 WHERE price>200"
db_cursor.execute(s)
mydb.commit()