import mysql.connector;
my_db=mysql.connector.connect(host='localhost',user='root',password='dileepkumar@123',database='INVENTORY_MANAGEMENT');
cur=my_db.cursor();
#Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.
delete='DELETE FROM MANUFACTURE WHERE DEFECTIVE=1';
cur.execute(delete);
print("Deleted Successfully");