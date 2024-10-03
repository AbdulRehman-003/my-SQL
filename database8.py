import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234",
                       database = "db1")

db_cursor =mydb.cursor()
s = "DELETE from book WHERE title ='php'"
db_cursor.execute(s)
mydb.commit()