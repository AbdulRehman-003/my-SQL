import mysql.connector as myconn

mydb = myconn.connect (host = "localhost",
                       user = "root",
                       password = "Abdulrehman!*1234")

db_cursor = mydb.cursor()
db_cursor.execute("create database db1")