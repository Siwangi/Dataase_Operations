import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Shivi@12345')


if conn.is_connected():
    print("Connected")

cursor = conn.cursor()

cursor.execute('select * from server')

rows = cursor.fetchall()

print("Number of rows in table:", cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()