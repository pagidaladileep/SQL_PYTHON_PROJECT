import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="dileepkumar@123", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
t = 'CREATE TABLE MANUFACTURE(MANUFACTURE_ID INT NOT NULL,MANUFACTURE_COMPANY VARCHAR(20),DEFECTIVE BIT NOT NULL,NUMBER_ITEMS INT NOT NULL,MANUFACTURE_DATE DATE PRIMARY KEY NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(10) NOT NULL)'
cur.execute(t)