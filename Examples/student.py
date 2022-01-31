import mysql.connector as s

connection = s.connect(host="localhost", user="root", passwd="1234", database="mydb")


if connection.is_connected():
    print("Connection Done!")

cursor = connection.cursor()

# ! To integrate SQL with Python by importing the MySQL module and extracting data from result set

# ? =============== expected output

# (1001, “Vinusha”, 50,70, 80 , “Namakkal”)
# (1001, “Aswin”, 54,82, 85 , “Erode”)
# (1001, “Bheem”, 90,73, 78 , “Salem”)

# ? ====================================


QUERY1 = """CREATE TABLE result(
    student_id INT PRIMARY KEY,
    student_name VARCHAR(20) NOT NULL,
    Marks1 INT,
    Marks2 INT,
    Marks3 INT,
    DistrictName VARCHAR(15)
    )"""

cursor.execute(QUERY1)
print("\nCreated Table")

QUERY2 = "INSERT INTO result(student_id, student_name, Marks1, Marks2, Marks3, DistrictName) VALUES(%s, %s, %s, %s, %s, %s)"
VALUES1 = [
    ("1001", "Vinusha", "50", "70", "80", "Namakkal"),
    ("1002", "Aswin", "54", "82", "85", "Erode"),
    ("1003", "Bheem", "90", "73", "78", "Salem"),
]

cursor.executemany(QUERY2, VALUES1)  # problem occurance

connection.commit()
print(cursor.rowcount, "Record Inserted!!")


QUERY = "SELECT * FROM result"

cursor.execute(QUERY)

print(cursor.fetchall())
