import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Shivi@12345')


if conn.is_connected():
    print("Connected")

cursor = conn.cursor()

try:
    cursor.execute("insert into server values (4, 'Rasika', 50000)")
    conn.commit()
    print("Server added")
except:
    conn.rollback()



cursor.close()
conn.close()