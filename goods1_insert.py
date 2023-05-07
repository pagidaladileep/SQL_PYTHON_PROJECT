import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="dileepkumar@123", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
insert = 'INSERT INTO goods (GOODS_ID, PRODUCT_NAME, COLOR, NUMBER_ITEMS, MANUFACTURE_DATE) values(%s,%s,%s,%s,%s)'
data = [(1, 'Toy Car', 'Blue', 100, '2023-04-01'),
         (2, 'Toy Car', 'Red', 50, '2023-04-03'),
           (3, 'Wooden Chair', 'Brown',200, '2023-03-01'),
             (4, 'Wooden Chair', 'White', 150, '2023-03-15'),
               (5, 'Teddy Bear', 'Pink', 300, '2023-05-01')]
cur.executemany(insert, data)
mydb.commit()
