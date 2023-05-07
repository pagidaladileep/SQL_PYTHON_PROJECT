import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="dileepkumar@123", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
z = "INSERT INTO sale(SALE_ID, STORE_NAME, PRODUCT_NAME, COLOR, NUMBER_ITEMS, SALE_AMOUNT, PROFIT_MARGIN, SALE_DATE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
a = [
    (1, 'MyCare', 'Wooden Chair', 'Brown', 10, 5000, 1000, '2023-04-20'),
    (2, 'ORay', 'Teddy Bear', 'Pink', 5, 500, 100, '2023-04-15'),
    (3, 'MyKids', 'Toy Car', 'Red', 30, 1500, 300, '2023-05-01')
]
cur.executemany(z, a)
mydb.commit()