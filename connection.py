import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="dileepkumar@123")
cur = mydb.cursor()
cur.execute("CREATE DATABASE INVENTORY_MANAGEMENT")