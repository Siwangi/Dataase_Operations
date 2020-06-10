import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Shivi@12345')


if conn.is_connected():
    print("Connected")

cursor = conn.cursor()

cursor.execute('insert into server values (3, 'Avish', 30000)')



cursor.close()
conn.close()