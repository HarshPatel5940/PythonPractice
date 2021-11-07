print("Some programs")

# ! Random from a specific list example
"""
from random import choice

lst = ["Tanay", "Rudra", "Harsh", "Vrinda"]
td = ["Truth", "dare"]
continue1 = "y"
while continue1 == "y":
    a = choice(lst)
    b = choice(lst)
    c = choice(td)
    if a != b:
        print(
            f"aksing {a}\nanswering {b} -- will do {c} \n ============================="
        )
        ask = input("Do you wanna continue [y] [n]:")
        if ask == "n":
            continue1 = "n"
    else:
        continue
"""

# method 1 "descending order"

"""
day1, day2, day3 = map(float, input("Enter the temperature").split())
if day1 > day2:
    if day1 > day3:
        if day2 > day3:
            print(day1, day2, day3)
        else:
            print(day1, day3, day2)
    if day3 > day1:
        print(day3, day1, day2)
if day2 > day1:
    if day2 > day3:
        if day1 > day3:
            print(day2, day1, day3)
        else:
            print(day2, day3, day1)
    else:
        print(day3, day2, day1)
"""

# ascending order

"""
first = 0
second = 0
third = 0
Day1, Day2, Day3 = map(float, input("Enter the temperature").split())
if Day1 > Day2:
    if Day1 > Day3:
        first = Day1
        second, third = Day2, Day3
    elif Day2 < Day3:
        first = Day2
        second, third = Day1, Day3
elif Day2 < Day3:
    first = Day2
    second, third = Day1, Day3
else:
    first = Day3
    second, third = Day1, Day2
print(first, second, third)
"""

# Q1 revision
"""
name = str(input("enter your name:"))
vowels = ["A", "a", "E", "e", "i", "I", "o", "O", "U", "u"]
if name[0] in vowels:
    print("your name starts with string")
else:
    print("your name does not starts with string")

N = 1
while N <= 5:
    NC = int(input("enter the number of cameras"))
    PC = int(input("enter the number of cameras"))
    salary = 1500 + (200 * NC) + (PC * NC * 0.02)
    print(salary)
    N = N + 1
"""

# FIBONACCI SERIES

"""
n = int(input("Enter the number of terms "))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, "is", n1)
else:
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print("done")
"""

# prime numbers

"""
start = 0
end = 100
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 
"""

# Write a program to print the bigger of any four numbers given by the user

"""
A, B, C, D = map(int, input("enter four numbers separated by space:...").split())
greatest = 0
if (A > B) and (A > C) and (A > D):
    greatest = A
if (B > A) and (B > C) and (B > D):
    greatest = B
if (C > B) and (C > A) and (C > D):
    greatest = C
if (D > B) and (D > A) and (D > C):
    greatest = D
print("the greatest number of all 4 number is", greatest)
"""
# count the number of words
"""
Line = str(input("enter a sentence"))
i = 0
k = len(Line)
words = 0
Line = Line.lstrip().rstrip()
if Line.isspace() == False:
    while i < k:
        if Line[i] == " ":
            words += 1
        i = i + 1
    print("Words : ", words + 1)
else:
    print("No Words")
"""
# DESIGN
"""
a = int(input("enter the number of lines:..."))
b = 1
while b <= a:
    inner = 1
    while inner <= b:
        print(b, " ", end="")
        inner += 1
    print("\n")
    b += 1
print("end of the design")
"""
# REVERSING THE DIGITS AND GETTING THE SUMS
"""
num = int(input("enter a integer"))
sum = 0
while num > 0:
    digit = num % 10
    print(digit, " ", end="")
    sum += digit
    num = num // 10
print("\n", "the sum of the digits", sum)
"""

# counting how many time elements come

"""
Lst = []
for i in range(5):
    Lst.append(input("enter a item"))
print(Lst)
count = input("enter the value you want count in the list")

print(Lst.count(count))
"""

# practice methods
"""
myAddress = "WZ-1,New Ganga Nagar,New Delhi"
print(myAddress.lower())
print(myAddress.upper())
print(myAddress.count('New'))
print(myAddress.find('New'))
print(myAddress.find('New'))
print(myAddress.split(','))
print(myAddress.split(' '))
print(myAddress.replace('New', 'Old'))
print(myAddress.partition(','))
print(myAddress.index('Agra'))
"""
# list practice 1

"""
list1 = [12, 32, 65, 26, 80, 10]
list1.sort()
print(list1)

list1 = [12, 32, 65, 26, 80, 10]
sorted(list1)
print(list1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = list1[::-2]
list1 = list1[:3] + list1[3:]
print(list1)

list1 = [1, 2, 3, 4, 5]
list1 = list1[len(list1) - 1]
print(list1)

myList = [10, 20, 30, 40]
myList.append([50, 60])
myList.extend([80, 90])
print(myList)

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, len(myList)):
    if i % 2 == 0:
        print(myList[i])

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del myList[3:]
print(myList)

list1 = [6, 7, 8, 9]
list1 = list1 * 2
print(list1)

list1 = [6, 7, 8, 9]
list1 *= 2
print(list1)

list1 = [6, 7, 8, 9]
list1 = list1 * 2
print(list1)
"""
# MENU DRIVEN PROGRAM
"""
Line = ""
k = 0
option = 0
while option != 6:
    Line = input("Enter a string ....")
    option = int(input("1. Count of Characters.... \n2. Count of Alphabet....\n3. Count of digits ...."
                       "\n4. Count of special symbols....\n5. Count of Words....\n6. Exit..."))
    if option == 1:
        ch = input("Enter character to be checked...")
        print(Line.count(ch) + Line.count(" "))

    elif option == 2:
        for letter in Line:
            if letter.isalpha():
                k += 1
        print(Line, "has ", k, " letters")
        k = 0

    elif option == 3:
        for letter in Line:
            if letter.isdigit():
                k += 1
        print(Line, "has ", k, " digits")
        k = 0

    elif option == 4:
        for letter in Line:
            if (letter.isalpha() == False) or (letter.isdigit() == False):
                k += 1
        print(Line, "has ", k, " Special Characters")
        k = 0

    elif option == 5:
        print(Line)
        lst = Line.split()
        print(lst)
        print(len(lst))

    elif option == 6:
        print("Terminating...")

"""
# capitalize letter
"""
string = input("Enter a string:")
string = string.lower()
length = len(string)
a = 0
end = length
string2=''             #empty string
while a < length :
   if a == 0:
       string2 += string[0].upper()
       a += 1
   elif (string[a] =='' and string[a+1] !=''):
       string2 += string[a]
       string2 += string[a+1].upper()
       a += 2
   else :
       string2 += string[a]
       a += 1
print("Original String : ", string)
print("")
print("Capitalized words String : ", string2)
"""

# getting sum of digits in a string
"""
Str = "sum of 123 and 678"
sum = 0
for ch in Str:
    if ch.isdigit():
        num = int(ch)
        sum += num
print(sum)
"""
# adding sum of all digits in a tuple
"""
sum = 0
tup = (12, 123, [1, 2, 3])
for ch in tup:
    if type(ch) == int:
        num = ch
        while num > 0:
            digit = num % 10
            sum += digit
            num = num // 10
    elif type(ch) == list:
        for x in ch:
            num = x
            while num > 0:
                digit = num % 10
                sum += digit
                num = num // 10
    else:
        return
print(sum)
"""
# finding index values of elements in a list
"""
usr = input("Enter the element :").lower()
ex = ""
g = ("ram", 141, 3, 'abc', "happy", "omg")
for e in g:
    ex = str(e)
    if usr in ex:
        print(usr, "index value is ", g.index(e))
        break
    elif g.index(e) > (len(g)+ 1):
        print("Not Found")
print("Done")
"""

# random subjects doing
"""
import random

subject = ['english', 'tamil', 'hindi', 'physics','maths', 'chemistry']
chose = random.choice(subject)
print('i am studying ', chose)
"""
# 3 didgit random number with sum of digits
"""
import random
num_1 = random.randrange(100, 999, 1) 
sum = 0
print('the number is: ', num_1)

while num_1 > 0:
    digit = num_1 % 10
    sum += digit
    num_1 = num_1 // 10

print('the sum of the digits is', sum)
"""
# write a program which fills list with randumbs number(.randint)
"""
import random
list_1 = []
count = 3
while count > 0:
    speci = random.randint(0, 20)
    list_1.append(speci)
    count = count - 1

print(list_1)
"""
# length, witdth and hiegt of parrelogram and calculate it's area and permiter
"""
len1 = width = height = 0
len1, width, height = map(int, input('enter lenght width and height of the parralellorgram sperated by space').split())

area_1 = (len1 * height)
perim = 2 * (len1 + width)
print('the area of parallelogram is: ', area_1, '\n', 'the perimeter of parallelogram is: ', perim)
print('Done')
"""
# 3 randomly select students out of 100 present a momento to the guest
"""
import random
list_3 = []
count = 3
while count > 0:
    speci = random.randint(0, 100)
    list_3.append(speci)
    count = count - 1
print('students with role numbers ', list_3[0], ', ', list_3[1], ' and ', list_3[2], 'are requested to present their momneto to the guest')
print('Done')
"""

# Nested disctionary with salary and all
"""

employee = {"harsh" : {'age': 16, 'salary' : 10000}, 'diya' : {'age': 15, 'salary': 8000}}

for Key in employee:
    print(" ------------------------- \n ")

    print("name : ", Key)
    print("Age  : ", employee[Key]["age"])
    print ("Salary  : ", employee[Key]["salary"])
    
print(" \n ------------------------- \n ")

"""

# DESIGNS

print("done by HARSH N Patel ,  class (XI-A)")

# design 1
"""
print("-------  design 1  ----------")
str1 = "**********"
n1 = 1 
while n1 < 5 : 
    print(str1)
    n1 += 1
"""

# design 2
"""
print("-------  design 2  ----------")
str2 = "*"
n2 = 1
while n2 <= 5: 
    pat1 = str2 * n2 
    print(pat1)
    n2 += 1

"""
# design 3
"""
print("-------  design 3  ----------")
str3 = "*"
n3_1 = 1
n3_2 = 4
x1 = " "
while n3_1 <= 5:
    frame1 = (x1 * n3_2) + (n3_1 *str3)
    print(frame1)
    n3_1 += 1
    n3_2 -= 1
"""

# design 4
"""
print("-------  design 4  ----------")
str4 = "*"
n4_1 = 1
n4_2 = 4
x2 = " "
while n4_1 <= 9 : 
    frame2 = (x2 * n4_2) + (n4_1*str4) + (x2 * n4_2)
    print(frame2)
    n4_1 += 2
    n4_2 -= 1
"""

# design 4
"""
print("-------  design 4  ----------")
n=5 
k = n - 1 
for i in range(0, n): 
        for j in range(0, k): 
            print(end=" ") 
        k = k - 1 

        for j in range(0, i+1): 
            print("* ", end="") 
        print("\r") 
"""
# design 5
"""
print("-------  design 5  ----------")
n=6 
for i in range(1,n): 
    for j in range(n-1,i,-1): 
        print(" ",end='') 
    for k in range(1,2*i): 
        print(i,end='') 
    print() 
"""

# design 6
"""
print("-------  design 6  ----------")
n=6 
for i in range(1,n): 
    for j in range(n-1,i,-1): 
        print(" ",end='') 
    for k in range(i,0,-1): 
        print(k,end='') 
    for l in range(2,i+1): 
        print(l,end='') 
    print("\n")
"""
print("\n ------ All patterns have been printed ------")


print("this file has been completely executed")
