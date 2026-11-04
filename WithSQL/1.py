import os
os.system("cls")

from mysql import connector

mydb = connector.connect(
    host="localhost",
    user='root',
    password='1234',
    database='dars_db'
)

cursor = mydb.cursor()


# cursor.execute("SHOW DATABASES;")
# for i in cursor:
#     print(i)

cursor.execute("SELECT * FROM students;")
jadval = cursor.fetchall()
for i in jadval:
    print(i)

