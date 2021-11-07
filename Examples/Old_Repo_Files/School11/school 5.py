# QUESTION 1

# Python program to find the largest among three numbers
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
if (num1 >= num2) and (num1 >= num3):
    largestnum = num1
elif (num2 >= num1) and (num2 >= num3):
    largestnum = num2
else:
    largestnum = num3
print("The largest number among", num1, ",", num2, "and", num3, "is: ", largestnum)

# QUESTION 2
letter = input("Enter a letter: ")
if letter == 'A' or letter == "a" or letter == 'E' or letter == 'e' or letter == 'I' or letter == 'i' or letter == 'O' or letter == 'o' or letter == 'U' or letter == 'u':
    print(letter, "is a Vowel")
else:
    print(letter, "is a Consonant")
Uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", " Z"]
if letter in Uppercase:
    print(letter, "letter is a uppercase letter")
else:
    print(letter, "letter is a lowercase letter")

# QUESTION 3
Size = 419430400
S = 960
if (Size // S) < 61:
    print("the file is not too big")
else:
    print("the file is too big")

# QUESTION 4
A = float(input("enter the number:"))
if A % 3 == 0:
    print("the number is divisible by 3")
if A % 5 == 0:
    print("the number is divisible by 5")
if A % 7 == 0:
    print("the number is divisible by 7")
if A % 9 == 0:
    print("the number is divisible by 9")
if A % 13 == 0:
    print("the number is divisible by 13")
else:
    print(A, "is not divisible by 3,5,7,9 and 13")

# QUESTIONS 5
N = input("enter a number from  15 to 20 :")
if N == "15":
    print("fifteen")
elif N == '16':
    print("sixteen")
elif N == "17":
    print("seventeen")
elif N == "18":
    print("eighteen")
elif N == "19":
    print("nineteen")
elif N == "20":
    print("twenty")
else:
    print("your number is out of range")
