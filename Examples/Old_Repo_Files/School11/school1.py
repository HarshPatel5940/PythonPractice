# question 1
A = 3
B = 3
C = (-5)
X = 8.8
Y = 3.5
Z = (-5.2)
print(A % C)
print(A * B / C)
print((A * C) % C)
print(X / Y)
print(X / (X + Y))
print(int(X) % int(Y))

# question 2
A = float(input("the number you want to round off:"))
print(round(A))

# question 3
A = float(input("length in CM:"))
B = float(input("length in CM:"))
C = (A / (12 * 5 / 2))
D = (B * 5 / 2)
print(C, D)

# question 4
A = int(input("enter the radius:"))
print(4 / 3 * 3.14 * A * A * A)

# question 5
F = float(input("enter the Teamprature in Celsius:"))
C = (F * 9 / 5) + 32
print(C)

# question 6

L = float(input("enter the lenght of rectangle:"))
B = float(input("enter the width of rectangle:"))
P = 2 * (L + B)
print(P)

# question 7
A = float(input("enter the first number"))
B = float(input("enter the second number:"))
C = float(input("enter the third number:"))
M = float((A + B + C) / 2)
print(M)
'''
A=str(input("enter the pattern:"))
print(A[0])
print((A[0]+A[1])*2)
print((A[0]+A[1]+A[2])*2)
'''

A = int(input("enter a integer"))
B = int(input("enter a integer"))
c = A + B - A % B
print(c)

AGE = int(input("enter you age"))
if 15 <= AGE < 46:
    print("you are eligible ti ride roller coaster")
else:
    print("you are eligible ti ride roller coaster")

A = int(input("enter the number"))
if (A % 5 == 0) and (A % 7 == 0):
    print("its divisible by 7 and 5")
else:
    print("ts  not divisible by 7 and 5")

# vowels problem in school
name = input("enter your name :")
vowels = ["a", "e", "i", "o", "u"]
if name[0] in vowels:
    print("name starts with vowels")
else:
    print("name does not starts with vowels")
