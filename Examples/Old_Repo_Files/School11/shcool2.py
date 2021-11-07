A = 10
B = 10
C = A == B
print(C)
c = (A < B)
print(C)
C = A <= B
print(C)
X = True
print(not X)
print(ord("A"))  # ord says here the askey number of"A"

# SEQUENCES
num_1 = [11, 12, 13, 14, 15]  # List
num_2 = (11, 12, 13, 14, 15)  # TUPPLES

A, *B, C = 1, 2, 'lol bro', "you learned it"
print(A, B, C)

X = 36 / 4 * (3 + 2) * 4 + 2
print(X)
A, B = B, A
print(A, B)

A = int(input("enter the principle"))
B = int(input("enter the rate"))
C = int(input("enter the time"))
print(A * B * C)

A = int(input("enter the Teamprature"))
C = (A * 5 / 9) + 32
print(C)

A = int(input("enter the firstnumber"))
B = int(input("enter the second number"))
print(A + B)
print(A - B)
print(A * B)
print(A / B)

A = int(input("enter the Radius"))
print((A ** 2) * 22 / 7)

Amt = int(input("enter the amount"))
R500 = Amt / 500
amt: int = Amt % 500
print(R500)

R100 = Amt / 100
amt = Amt % 100
print(R100)

R50 = Amt / 50
amt = Amt % 50
print(R50)

R20 = Amt / 20
amt = Amt % 20
print(R20)

R10 = Amt / 10
amt = Amt % 10
print(R10)

print(Amt / 1)
print(R500)

date = int(input("enter the Date in which you are born:"))
months = int(input("enter the month in which you are born:"))
year = int(input("enter the year in which you are born:"))
if date <= 31:
    if months <= 12:
        print(date, '/', months, "/", year)

A = int(input("length in inches:"))
B = int(input("length in foot:"))
C = (A * 5 / 2)
D = (B * 30)
print(C, D)

# question 1
A = input("enter the first number:")
B = input("enter the second number:")
A, B = B, A
print(A, B)

# question 2
P = int(input("enter the principle:"))
R = int(input("enter the rate:"))
TIME = int(input("enter the time:"))
S = P * R * TIME
print(S)

# question 3
F = float(input("enter the Teamprature in farenheat:"))
C = (F * 5 / 9) - 32
print(C)

# question 4
A = int(input("enter the first number:"))
B = int(input("enter the second number:"))
print("the sum of numbers is:", A + B)
print("the subraction of numbers is:", A - B)
print("the product of numbers is:", A * B)
print("the quotient of numbers is:", A / B)

# question 5
A = float(input("enter the Radius:"))
print((A * A) * 22 / 7)

# question 6
Amt = int(input("enter the amount"))
R500 = Amt // 500
Amt = Amt % 500
print("No of 500 rupee notes is:", R500)

R100 = Amt // 100
Amt = Amt % 100
print("No of 100 rupee notes is:", R100)

R50 = Amt // 50
Amt = Amt % 50
print("No of 50 rupee notes is:", R50)

R20 = Amt // 20
Amt = Amt % 20
print("No of 20 rupee notes is:", R20)

R10 = Amt // 10
Amt = Amt % 10
print("No of 10 rupee notes is:", R10)

R1 = Amt
print("No of 1 rupee notes is:", Amt)

# QUESTION 11
A = float(input("enter the speed in KM/HR:"))
B = float(A * (6213 / 10000))
print("your speed in miles/hr is:", B)

# question 12
A = int(input("input the time in hours:"))
B = int(input("input the time in minutes:"))
C = ((A * 60) + B)
print("total time in minutes is: ", C)

# question 13
A = int(input("ENTER THE TOTAL TIME IN MINUTES:"))
B = A // 60
C = A % 60
print("The time in Hr/min format is:", B, ":", C)
