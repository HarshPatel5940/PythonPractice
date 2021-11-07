# random subjects doing
import random

subject = ['english', 'tamil', 'hindi', 'physics','maths', 'chemistry']
chose = random.choice(subject)
print('i am studying ', chose)
 
# 3 didgit random number with sum of digits
import random
num_1 = random.randrange(100, 999, 1) 
sum = 0
print('the number is: ', num_1)

while num_1 > 0:
    digit = num_1 % 10
    sum += digit
    num_1 = num_1 // 10

print('the sum of the digits is', sum)
 
# write a program which fills list with randumbs number(.randint)
import random
list_1 = []
count = 3
while count > 0:
    speci = random.randint(0, 20)
    list_1.append(speci)
    count = count - 1

print(list_1)
 
# length, witdth and hiegt of parrelogram and calculate it's area and permiter
 
len1 = width = height = 0
len1, width, height = map(int, input('enter lenght width and height of the parralellorgram sperated by space').split())

area_1 = (len1 * height)
perim = 2 * (len1 + width)
print('the area of parallelogram is: ', area_1, '\n', 'the perimeter of parallelogram is: ', perim)
print('Done')
 
# 3 randomly select students out of 100 present a momento to the guest
import random
list_3 = []
count = 3
while count > 0:
    speci = random.randint(0, 100)
    list_3.append(speci)
    count = count - 1
print('students with role numbers ', list_3[0], ', ', list_3[1], ' and ', list_3[2], 'are requested to present their momneto to the guest')
print('Done')