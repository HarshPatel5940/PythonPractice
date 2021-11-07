# Practice Question | 14/7/2021
i = 1
stu1 = int(input("Number of Students of data u want to enter"))
file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\data.txt"


f = open(file_path, "a")
while i <= stu1:
    roll = int(input("Enter the roll number : "))
    name = input("Enter the name of the student : ")
    english = float(input("Enter English Marks : "))
    maths = float(input("Enter your maths marks : "))
    science = float(input("enter Your science marks : "))
    tamil = float(input("enter Your tamil marks : "))
    hindi = float(input("enter Your hindi marks : "))

    r = f"{roll},{name},{english},{maths},{science},{tamil},{hindi} \n "
    f.append(r)
    i += 1
f.close()

f = open(file_path, "r")
for line in f.readline():
    print(f)
f.close()
