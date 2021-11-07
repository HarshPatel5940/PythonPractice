# QUESTION 1
k = 1
while k < 5:
    A = int(input("enter the quantity:..."))
    B = int(input("price per item:..."))
    C = A * B
    if C > 5000:
        print(C - (C / 10))
    else:
        print(C)
    k += 1
# QUESTION 2
S = int(input("enter the selling price:..."))
C = int(input("enter the cost of the item:..."))
if S > C:
    print("owner is in profit")
    print("the owner is in profit of ", (S - C))

else:
    print("owner is in loss")
    print("the owner is in loss of ", (C - S))

# QUESTION 3
A = int(input("enter your age:..."))
B = int(input("enter your age:..."))
C = int(input("enter your age:..."))
if (A < B) and (A < C):
    print(A, "is the YOUNGEST")
elif (B < A) and (B < C):
    print(B, "is the YOUNGEST ")
else:
    print(C, "is the YOUNGEST")

# QUESTION 4
S1 = float(input('enter side 1:...'))
S2 = float(input('enter side 2:...'))
S3 = float(input('enter side 3:...'))
A1 = float(input('enter angle 1:...'))
A2 = float(input('enter angle 2:...'))
A3 = float(input('enter angle 3:...'))
if A1 + A2 + A3 == 180:
    R1 = 'true'
else:
    R1 = 'false'
if (S1 + S2) > S3:
    R2 = 'true'
else:
    R2 = 'false'
if (S1 + S3) > S2:
    R3 = 'true'
else:
    R3 = 'false'
if (S3 + S2) > S1:
    R4 = 'true'
else:
    R4 = 'false'
if (R1 == 'true') and (R2 == 'true') and (R3 == 'true') and (R4 == 'true'):
    print("It can form a triangle")
else:
    print('It cannot form a triangle')

# QUESTION 5
a = float(input('enter your salary:...'))
if a < 1500:
    Hra = a * 0.1
    Da = a * 0.9
    print('your hra=', Hra, 'your da=', Da)
elif a >= 1500:
    Hra = 500
    Da = a * 0.98
    print('your hra=', Hra, 'your da=', Da)

# QUESTION 6
t1 = 0
t2 = 0
t3 = 0
bill = float(input("enter the number of call:..."))
if bill < 101:
    print("your total amount is 200 ")
elif (bill > 100) and (bill < 151):
    a1 = (bill - 100) * 0.6
    t1 = 200 + a1
    print("your total amount is", t1)
elif (bill > 150) and (bill < 151):
    a2 = (bill - 150) * 0.50
    t2 = (t1 + a2)
    print("your total amount is", t2)
elif bill > 200:
    a3 = (bill - 200) * 0.4
    t3 = (t2 + a3)
    print("the total amount is", t3)

# QUESTION 7
print("The quadratic equation is if the form ax^2+bx+c, where a is not equal to zero")
a = int(input("Enter the value of 'a' "))
if a == 0:
    print("The value of 'a' cannot be equal to 0")
else:
    b = int(input("Enter the value of 'b' "))
    c = int(input("Enter the value of 'c' "))
    d = (b ** 2) - (4 * a * c)
    if d >= 0:
        r1 = (-b + (d ** (1 / 2))) / (2 * a)
        r2 = (-b - (d ** (1 / 2))) / (2 * a)
        print("The roots of this equation are", r1, r2)
    else:
        print("This equation doesn't have any real roots")


# QUESTION 8
N = 1
while N <= 5:
    M = int(input("enter your marks :.."))
    if M >= 60:
        print("first division")
    elif (M < 60) and (M > 49):
        print("second division")
    elif (M > 39) and (M < 49):
        print("third division")
    elif M < 40:
        print("fail")
    N += 1
print("done")

#                                                                 PART 2
# QUESTION 1
N = 1
while N <= 10:
    print(N)
    N += 1
print("Done")

# QUESTION 2
Counter = 1
Sum1 = 0
num = 0
while Counter <= 10:
    num += 1
    Sum1 = Sum1 + num
    print(Sum1)
    Counter += 1
print("Done")

# QUESTION 3     ""factorial""
num2 = int(input("enter a number:..."))
A = 1
i = 1
while i <= num2:
    A = A * i
    i = i + 1
print("factorial of ", num2, " is ", A)

# QUESTION 4
B = int(input("enter your base number:..."))
P = int(input("enter the power which base is to be raised:..."))
Ans = B ^ P
print(Ans)

# QUESTION 5. Write a program to reveres any given integer number.
num = int(input("enter a integer"))
sum = 0
while num > 0:
    digit = num % 10
    print(digit, "", end="")
    num = num // 10


# QUESTION 6
num = int(input("enter a integer:..."))
sum = 0
digit = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("\n", "the sum of digits is", sum)

# QUESTION 7
ct = int(input("enter the no. of times you want to enter the number"))
P = 0
N = 0
Z = 0
counter = 1
while counter <= ct:
    in2 = int(input("enter the number"))
    if in2 > 0:
        P += 1
    elif in2 < 0:
        N += 1
    else:
        Z += 1
    counter += 1
print("the number of positive values is", P)
print("the number of negative values is", N)
print("the number of Zeros is", Z)
print("DONE")

# QUESTION 8
choice = 'yes'
max1 = min1 = 0
while choice == "y":
    num = int(input("enter a number:..."))
    if num < min1:
        min1 = num
    if num > max1:
        max1 = num
    choice = input("enter  yes or no")
    if choice != "yes":
        print("maximum num:", max1, "minimum number:", min1)
        break
print("DONE")

# QUESTION 9
num = 100
while num < 501:
    d1 = num // 100
    d2 = (num % 100)//10
    d3 = num % 10
    sum = (d1 * d1 * d1) + (d2 * d2 * d2) + (d3 * d3 * d3)
    if sum == num:
        print(num)

# QUESTION 10
n = float(input("enter a number:"))
pattern = 1 / n
i = 1
sum1 = 0
while i <= n:
    pattern = pattern + 1
    i = i+1
    sum1 += pattern
print("the sum of the following pattern is", sum1)
print("done")

# QUESTION 11
"""
n = int(input('enter the integer'))
k = 1
m = -1
s = 0
sum = 0
while k <= n:
    sum = (1/k)(m * s) + sum
    k = k + 1
    s = s + 1
print('sum=', sum)
"""

