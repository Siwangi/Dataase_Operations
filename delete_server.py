import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Shivi@12345')


if conn.is_connected():
    print("Connected")

cursor = conn.cursor()

try:
    cursor.execute("delete from server where name = 'Rasika'")
    conn.commit()
    print("Server deleted")
except:
    conn.rollback()



cursor.close()
conn.close()