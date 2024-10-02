import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234")

print(mydb,"conect")