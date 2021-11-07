# QUESTION 1 (14/06/2021)

# --->write a program that accepts a number between 1 and 365 and get the day of 1 from the user. And then print which day that number is.

Names = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print("Project Done By HARSH N PATEL \nclass - 12A")

# Trying/practising error Handling
Num_1 = int(input("Enter day number: "))

if Num_1 < 1 or Num_1 > 365:
    print("Invalid Input \nPlease enter within range 1-365")
    Num_1 = int(input("Enter day number: "))

    if Num_1 < 1 or Num_1 > 365:
        print("USER IS DUMB \nSHUTTING DOWN...")

    else:
        print("Number accepted \n")
        firstDay = input("First day of year: ")

        if firstDay not in Names:
            print(
                f"please say any Valid day Name. Giving List of Valid Day Names \n{Names}")  # Using Functional String to make work easier
            firstDay = "First day of year: "

            if firstDay not in Names:
                print("USER IS DUMB \nSHUTTING DOWN...")
            else:
                print("Day Name Accepted")
                if Num_1 == 1:
                    print(firstDay)
                else:
                    startDay = Names.index(str.upper(firstDay))
                    currDay = Num_1 % 7 + startDay - 1

                    if currDay >= 7:
                        currDay = currDay - 7

                    print("Day on day number", Num_1, ":", Names[currDay])

        else:
            print("Day Name Accepted \n")

            if Num_1 == 1:
                print(firstDay)
            else:
                startDay = Names.index(str.upper(firstDay))
                currDay = Num_1 % 7 + startDay - 1

                if currDay >= 7:
                    currDay = currDay - 7

                print("Day on day number", Num_1, ":", Names[currDay])
else:
    print("Number accepted \n")

    firstDay = input("First day of year: ")

    if firstDay not in Names:
        print(f"please say any Valid day Name. Giving List of Valid Day Names \n {Names}")
        firstDay = "First day of year: "

        if firstDay not in Names:
            print("USER IS DUMB \nSHUTTING DOWN...")

        else:
            print("Day Name Accepted")
            if Num_1 == 1:
                print(firstDay)
            else:
                startDay = Names.index(str.upper(firstDay))
                currDay = Num_1 % 7 + startDay - 1

                if currDay >= 7:
                    currDay = currDay - 7

                print("Day on day number", Num_1, ":", Names[currDay])

    else:
        print("Day Name Accepted \n")

        if Num_1 == 1:
            print(firstDay)
        else:
            startDay = Names.index(str.upper(firstDay))
            currDay = Num_1 % 7 + startDay - 1

            if currDay >= 7:
                currDay = currDay - 7

            print("Day on day number", Num_1, ":", Names[currDay])

# QUESTION 2 (14/06/2021)

# ---> write a program that inputs an integer in range 0-999 and then prints if the integer entered is a 1/2/3 digit numbers (using elif)

Number = input("Please Enter a Number between 1- 999")

if len(Number) == 1:
    print(Number, "is a Single digit Number")

elif len(Number) == 2:
    print(Number, "is a Double digit Number")

elif len(Number) == 3:
    print(Number, "is a Trible digit Number")

else:
    print("Number is not between 1 - 999")

# QUESTION 3 (14/06/2021)

num = int(input("Enter a number: "))
if num >= 10:
    if num >= 100:
        if num >= 1000:
            print("Number is invalid")
        else:
            print("Three digits")
    else:
        print("Two digits")
else:
    print("One digit")

# Ending Part 1
print("Completed Executing Program. \ndate : 14/06/21 \nDone by : HARSH N PATEL\nClass : XII - A")

# Sorting
# Bubble Sorting Lesson

l1 = [42, 29, 74, 11, 65, 59]
n = len(l1)
print("Original list", l1)
for i in range(n - 1):
    for j in range(n - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
        print("sorted list", l1)

# QUESTION 6 (19/06/21)
# Write a python script to input a number and count the occurrence of that given number in the given list,

L1 = [10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10,
      10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10, 10, 20, 30, 40, 10, 50, 10]
a = int(input("Pls enter number u want to find the recurrence of : "))

print(f"The Number of Times {a} is used is - ", L1.count(a))

# Question 7 (21/06/21)
# Write a Python Program INput any two tuples and swap there Values

a = tuple()
n = int(input("number of values"))
for i in range(n):
    a = input("enter elements")
    a = a + (a,)

b = tuple()
m = int(input("number of values"))
for i in range(m):
    a = input("enter elements")
    b = b + (a,)
print("before swapping", a, b)

a, b = b, a

print("after swapping", a, b)

# QUESTION 8 (22/06/21)
# Input a dictionary from users of different sections and show the Output

# -----------using while
my_dic = {}
n = int(input("Enter the Number of sections we have"))
a = 1
while a <= n:
    x, y = input("Enter the section and subject separated by (--) :").split("--")
    my_dic[x] = y
    a += 1

for i in my_dic:
    print("Section ", i, ' : ', my_dic[i])

# -----------Using for
my_dic2 = {}
n = int(input("Enter number of sections: "))

for x in range(n):
    a, b = input("Enter the section and subject sepereated by (--) :").split("--")
    my_dic2[a] = b

for i in my_dic2:
    print("Section ", i, ' : ', my_dic2[i])

# QUESTION 9 (22/06/21)
# Write a program to store student information like admission number like
# Admission number, roll no,  name , Marks (Admission number should be Key)

n = 1
Students_no = int(input("Number Of student's data u want to add in the database : "))
data = {}

while n <= Students_no:
    admission_no = int(input("Enter ur admission number : "))
    lst = []
    roll_no = int(input("Enter ur roll number : "))
    name = input("Enter Your Full name : ")
    marks = float(input("Enter ur Average marks in all Subjects : "))
    lst.append(roll_no)
    lst.append(name)
    lst.append(marks)
    data[admission_no] = lst

    print("\nData has been accepted !\n")
    n += 1
print(f"-------- \n{data}\n----------\nexecution completed")

# Just Trying to learn to import Files
import functions as fnc

print(fnc.areaCircle(10))
print(fnc.areaRectangle(10, 20))
print(fnc.areaCylinder(10, 7))

# ==== display the size of the file in bytes f= .read > len(f)
# ==== display number of lines  f = .headlines > len(f)
