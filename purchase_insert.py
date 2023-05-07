import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="dileepkumar@123", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
insert='INSERT INTO purchase (PURCHASE_ID, STORE_MODE, PRODUCT_NAME, COLOR, NUMBER_ITEMS, PURCHASE_AMOUNT, PURCHASE_DATE) VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[(1, 'Online Store', 'Toy Car', 'Blue', 50, 1000, '2023-04-05'),
       (2, 'Offline Store', 'Wooden Chair', 'Brown', 20, 3000, '2023-04-10'),
       (3, 'Online Store', 'Teddy Bear', 'Pink', 100, 2000, '2023-05-02')]
cur.executemany(insert,values);
mydb.commit();
print("Inserted Successfully");
