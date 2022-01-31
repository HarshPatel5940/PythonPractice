# pip install mysql-connector

import mysql.connector as s


connection = s.connect(host="localhost", user="root", passwd="1234", database="mydb")


if connection.is_connected():
    print("Connection Done!")

cursor = connection.cursor()

#  ? QUERY = "INSERT INTO customer(name,address,phone) VALUES(%s, %s, %s)"

# ? val = [
# ?     ("Harsh", "Kellys", "01234"),
# ?     ("Tanay", "ainavaram", "23456"),
# ?     ("Rudra", "purshvakam", "789234"),
# ? ]

# ? cursor.executemany(QUERY, val)

# ? connection.commit()
# ? print(cursor.rowcount, "Record Inserted!!")

QUERY = "SELECT * FROM customer"

cursor.execute(QUERY)

print(cursor.fetchall())
