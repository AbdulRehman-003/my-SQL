import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234",
                       database = "db1")

db_cursor = mydb.cursor()
s = "INSERT INTO book (bookid,title,price) VALUES (%s,%s,%s)"

books = [(2,'php',450),(4,'java',130),(4,'html',200)]

db_cursor.executemany(s,books)
mydb.commit()