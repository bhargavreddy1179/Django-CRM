import mysql.connector

dataBase = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   passwd = 'NEON1179neon#'
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Bhargava")

print("ALL Done")