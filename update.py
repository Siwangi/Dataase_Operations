import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Shivi@12345')


if conn.is_connected():
    print("Connected")

cursor = conn.cursor()

try:
    cursor.execute("UPDATE server SET name = 'Niks' where name = 'Nikhil'")
    conn.commit()
    print("Server updated")
except:
    conn.rollback()



cursor.close()
conn.close()

