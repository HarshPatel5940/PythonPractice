
# QUESTION 1
GradeA, GradeB, GradeC = 0, 0, 0
N = 1
while N <= 5:
    Stu = int(input("enter your grade"))
    if Stu == "A":
        GradeA += 1
    elif Stu == "B":
        GradeB += 1
    elif Stu == "C":
        GradeC += 1
    else:
        print("invalid grade")
        continue
print("Done")


# Question 2
print("the type of operators available in the calculator +,-,*,**,/,//,%")
K = 1
while K <= 5:
    operator = input("Enter operator:")
    A = float(input("Enter first number:"))
    B = float(input("Enter second number:"))
    if operator == "+":
        print("the addition of two numbers is", A + B)
    elif operator == "-":
        print("the subtraction of two numbers is", A - B)
    elif (operator == "*"):
        print("the multiplication of two numbers is", A * B)
    elif operator == "/":
        print("the division of two numbers is", A / B)
    elif operator == "%":
        print("the remainder of two numbers is", A % B)
    else:
        print("Invalid operator")
    K += 1
print("Done")

# QUESTION 4
Str1 = input("enter a string")
n = 0
while n < len(Str1):
    print(Str1[n])
    n += 2
print("done")

