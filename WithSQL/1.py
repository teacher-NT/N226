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

# cursor.execute("SELECT * FROM students;")
# jadval = cursor.fetchall()
# for i in jadval:
#     print(i)


# qator = cursor.fetchone()
# print(qator)

# qatorlar = cursor.fetchmany(3)
# for i in qatorlar:
#     print(i)


ism = input("Ism: ")
fam = input("Familya: ")
sana = input("Sana: ")
manzil = input("Manzil: ")

query1 = f"""
    INSERT INTO students (first_name, last_name, birth_date, manzil)
    VALUES
    ('{ism}', '{fam}', '{sana}', '{manzil}');
"""

cursor.execute(query1)
mydb.commit()

print(cursor.rowcount, "ta qator qo'shildi")
