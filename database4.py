import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234",
                       database = "db1")

db_cursor = mydb.cursor()
s = "INSERT INTO book (bookid,title,price) VALUES(%s,%s,%s)"
b1 = (1,'python',350)
db_cursor.execute(s,b1)
mydb.commit()