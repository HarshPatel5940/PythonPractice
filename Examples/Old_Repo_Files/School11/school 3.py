# QUESTION 1
A = int(input("enter the Radius"))
print("the area of the circle is:", (A ** 2) * 22 / 7)

# QUESTION 2
L = float(input("enter the length of rectangle:"))
B = float(input("enter the width of rectangle:"))
P = (2 * (L + B))
print("the perimeter of the rectangle is:", P)

# QUESTION 3
A = float(input("enter the speed in KM/HR:"))
B = float(A * (6213 / 10000))
print("your speed in miles/hr is:", B)

# QUESTION 4
A = int(input("input the time in hours:"))
B = int(input("input the time in minutes:"))
C = ((A * 60) + B)
print("total time in minutes is: ", C)

# question 13
A = int(input("ENTER THE TOTAL TIME IN MINUTES:"))
B = A // 60
C = A % 60
print("The time in Hr/min format is:", B, ":", C)
