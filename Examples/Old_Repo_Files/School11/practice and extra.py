"""
Q1 write a program to calculate the total expense, quantity , price per unit are input by the user & a discount is given
"""
A = int(input("enter the quantity"))
B = int(input("price per item"))
C = A * B
if C > 5000:
    print(C - (C / 10))
else:
    print(C)

# question 2
S = int(input("enter the selling price:"))
C = int(input("enter the cost of the item:"))
if S > C:
    print("owner is in profit")
    print("the owner is in profit of ", (S - C))

else:
    print("owner is in loss")
    print("the owner is in loss of ", (C - S))

# question 3
A = int(input("enter your age"))
B = int(input("enter your age"))
C = int(input("enter your age"))
if (A > B) and (A > C):
    print(A, "is the eldest")
elif (B > A) and (B > C):
    print(B, "is the eldest ")
else:
    print(C, "is the eldest")

# question 4
# COMPLEX CAL CALCULATOR
N = 1
print("the type of operators available in the calculator +,-,*,**,/,//,%")
while N <= 5:
    operator = input("Enter operator:")
    A = float(input("Enter first number:"))
    B = float(input("Enter second number:"))
    if operator == "+":
        print("the addition of two numbers is", A + B)
    elif operator == "-":
        print("the subtraction of two numbers is", A - B)
    elif operator == "*":
        print("the multiplication of two numbers is", A * B)
    elif operator == "**":
        print("the power of two numbers is", A ** B)
    elif operator == "/":
        print("the division of two numbers is", A / B)
    elif operator == "%":
        print("the remainder of two numbers is", A % B)
    elif operator == "//":
        print("the integral quotient of two numbers is", A // B)
    else:
        print("Invalid operator")
        continue
    N += 1

# question 5
S1 = float(input('enter side 1'))
S2 = float(input('enter side 2'))
S3 = float(input('enter side 3'))
A1 = float(input('enter angle 1'))
A2 = float(input('enter angle 2'))
A3 = float(input('enter angle 3'))
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

# QUESTION 6
t1 = 0
t2 = 0
bill = float(input("enter the number of call"))
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
a = float(input('enter your salary'))
if a < 1500:
    Hra = a * 0.1
    Da = a * 0.9
    print('your hra=', Hra, 'your da=', Da)
elif a >= 1500:
    Hra = 500
    Da = a * 0.98
    print('your hra=', Hra, 'your da=', Da)

# QUESTION 8
x2 = int(input("enter the term x^2"))
x1 = int(input("enter the term X"))
x0 = int(input("enter the term without x"))
root1 = x1 + ((x1 ^ 2)-(4 * x2 * x0))
root2 = x1 - ((x1 ^ 2)-(4 * x2 * x0))
print("the two roots of your equation are", root1, root2)

coordinates = [(4, 100), (88, 1000)]
print(coordinates[0])


# QUESTION 9
info = (input("enter your subject (sci or commerce)"))
if info == "science":
    info2 = (input("enter your subjects(comp or bio)"))
    personal1, personal2, personal3 = map(str, input("enter your name mobile no. and 10th percentage separated by SPACE").split())
    print("your group is", info, "your subjects are", info2)
    print("your name is", personal1)
    print("your mobile is", personal2)
    print("and your 10th percentage is", personal3)
elif info == "commerce":
    info2 = (input("enter your subjects (pure maths or maths with comp)"))
    personal1, personal2, personal3 = map(str, input("enter your name mobile no. and 10th percentage separated by SPACE").split())
    print("your group is", info, "your subjects are", info2)
    print("your name is", personal1)
    print("your mobile is", personal2)
    print("and your 10th percentage is", personal3)


