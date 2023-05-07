import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="dileepkumar@123", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
z = 'INSERT INTO manufacture (MANUFACTURE_ID,MANUFACTURE_COMPANY, PRODUCT_NAME, COLOR, NUMBER_ITEMS, MANUFACTURE_DATE, DEFECTIVE) VALUES(%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'SS EXPORT', 'Toy Car', 'Blue', 100, '2023-04-01', 0), (2, 'SG EXPORT', 'Toy Car', 'Red', 50, '2023-04-03', 1), (3, 'SS EXPORT', 'Wooden Chair','Brown', 200, '2023-03-01', 1), (4, 'SRS EXPORT', 'Wooden Chair', 'White', 150, '2023-03-15', 0), (5, 'XYZ EXPORT', 'Teddy Bear', 'Pink', 300, '2023-05-01', 1)]
cur.executemany(z, a)
mydb.commit()