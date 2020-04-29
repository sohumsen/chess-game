#Example of how i would store past games using SQL

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="user", passwd="passwd", database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
