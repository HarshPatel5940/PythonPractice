from math import *

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# VARIABLES

character_name = "tanay"
character_age = "66"

print("there was a man named " + character_name + ",")
print("he was " + character_age + "years old")
print("he really liked the name " + character_name + " ,")
print("but not the age " + character_age + ".")

# STRINGS

phrase = "tanay "
print(phrase + " is cool")
print(phrase.upper())
print(phrase.upper().isupper())

print(len(phrase))
print(phrase[1])
print(phrase.index("a"))
print(phrase.replace("tanay", "george"))

# BASIC CALCULATER

a = -10
print(3 + 4.5550)
print(10 % 3)
print(str(a) + "my unlucky number")
print(abs(a))
print(pow(5, 2))
print(max(100, 1000))
print(min(1000, 10000))
print(round(6.7))
print(floor(5.564))
print(ceil(2.5))
print(sqrt(55))

# VARIABLES

name = input("Enter your name: ")
age = input("Enter your age: ")
print("HELLO " + name + " You are " + age + "years old")

num1 = input("Enter your number:")
num2 = input("Enter your 2nd  number:")
c = float(num1) + float(num2)

print(c)
'''
# FUNCTIONS

A = input("Enter your master password:")
B = "nathuram5940"
C = input("Entermaster password2:")
D = "5940patel"
E = input("Enter mater passward3:")
F = "htr patel"
G = input("Enter master passward4:")
H = "nikul patel59"
if (A == B) and (C == D)and (E == F) and (G == H):
    print("your secret code is RUDRI IS A GOOD BOY")
else:
    print("incorrect password\Pagal; chor")
'''
# LIST FUNCTIONS

A = [2, 3, 4]
B = ("tanay", "rudra")
A.extend(B)
A.append("jack")
A.insert(1, "jack")
A.remove("jack")
A.clear()

# TUPPLES

print(A)

coordinates = [(4, 100), (88, 1000)]
print(coordinates[0])


# FUNCTION

def sayhi():
    print("Bye Corona")


sayhi()


# RETURN FUNCTION

def say_hi(name, age):
    print("Bye " + name + " you are " + age + "old")


say_hi("Corona", "1 year")


def cube(num):
    return num * num * num * num


A = cube(4)
print(A)

# IF FUNCTIONS

is_male = True
if is_male:
    print("you are a male")
else:
    print("you are not a male")


# IF COMPARISONS

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2


print(max_num(3, 88, 9))

# COMPLEX CAL CALCULATER
print("the type of operaters available in the calculator +,-,*,**,/,//,%")

operater = input("Enter operater:")
A = float(input("Enter first number:"))
B = float(input("Enter second number:"))

if operater == "+":
    print("the addition of two numbers is", A + B)
elif operater == "-":
    print("the subtraction of two numbers is", A - B)
elif operater == "*":
    print("the multiplication of two numbers is", A * B)
elif operater == "**":
    print("the power of two numbers is", A ** B)
elif operater == "/":
    print("the division of two numbers is", A / B)
elif operater == "%":
    print("the remainder of two numbers is", A % B)
elif operater == "//":
    print("the integral quotient of two numbers is", A // B)
else:
    print("Invalid operator")

# DICTIONARIES


A = {

    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(A["Nov"])
print(A.get("TANAY", "Not a valid key"))

# WHILE LOOP


A = 10

while A <= 100:
    print(A)
    A = A + 2 - 1
print("Done with loop")

# GUESSING GAME

A = "elephant"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != A and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter Guess:")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")
