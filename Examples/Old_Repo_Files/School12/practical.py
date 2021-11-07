print("some practice questions based from practical board exams")

#======================= Miscllaneous
# Bubble Sorting Lesson

l1 = [42, 29, 74, 11, 65, 59]
n = len(l1)
print("Original list", l1)
for i in range(n - 1):
    for j in range(n - i - 1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
        print("sorted list", l1)

#======================= exp : 1
# Program to calculate factorial of entered number
num = int(input("Enter any number :"))
fact = 1
n = num # storing num in n for printing
while num>1: # loop to iterate from n to 2
    fact = fact * num
    num-=1
print("Factorial of ", n , " is :",fact)


#======================= exp : 2
# Program to input any number from user Check it is Prime number of not
import math
num = int(input("Enter any number :"))
isPrime=True
for i in range(2,int(math.sqrt(num))+1):
    if num % i == 0:
        isPrime=False

if isPrime:
    print(f"{num} Number is Prime")
else:
    print(f"{num} Number is not Prime")


#======================= exp : 3  
#Program to find sum of elements of list recursively
def findSum(lst,num):
    if num==0:
        return 0
    else:
        return lst[num-1]+findSum(lst,num-1)

mylist = [] #
num = int(input("Enter how many number :"))
for i in range(num):
    n = int(input("Enter Element "+str(i+1)+":"))
    mylist.append(n)
sum = findSum(mylist,len(mylist))
print("Sum of List items ",mylist, " is :",sum)


#======================= exp : 4
#Program to find 'n'th term of fibonacci series Fibonacci series : 0,1,1,2,3,5,8,13,21,34,55,89,...
# nth term will be counted from 1 not 0
def nthfiboterm(n):
    if n<=1:
        return n
    else:
        return (nthfiboterm(n-1)+nthfiboterm(n-2))

num = int(input("Enter the 'n' term to find in fibonacci :"))
term = nthfiboterm(num)
print(num,"th term of fibonacci series is :",term)


#======================= exp : 5
#Program to find the occurence of any word in a string
def countWord(str1,word):
    s = str1.split()
    count=0
    for w in s:
        if w==word:
            count+=1
    return count
str1 = input("Enter any sentence :")
word = input("Enter word to search in sentence :")
count = countWord(str1,word)
if count==0:
    print("## Sorry! ",word," not present ")
else:
    print("## ",word," occurs ",count," times ")

#======================= exp : 6
#Program to roll a dice using carriage return
from random import randint
from time import sleep

play = 'y'
print("Press Ctrl+C to stop the dice")

while True:
    try:
        while True:
            n = randint(1, 6)
            print(f"\rrolling ==> {n}",end="")
            sleep(0.2)
    except KeyboardInterrupt:
        print(f"\n\nYour Number is {n}")
        ans = input("Do you wanna stop [y] [n] : ")
        if ans == "y":
            break
        else:
            print("Starting new game")
            