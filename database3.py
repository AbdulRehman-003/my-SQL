import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234",
                       database = "db1")

db_cursor = mydb.cursor()
s ="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
db_cursor.execute(s)