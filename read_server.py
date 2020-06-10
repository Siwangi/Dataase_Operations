import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Shivi@12345')


if conn.is_connected():
    print("Connected")

cursor = conn.cursor()

cursor.execute('select * from server')

row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()