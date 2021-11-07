from timeit import default_timer as timer

start = timer()


print("ALL THE NOTES YOU NEED TO LEARN PYTHON")

# File Handling

"""
file Opening Modes : r  w  a  r+ w+  a+  ab  wb  ab+  wb+  

General Methods:
    open()                        used to open the file
    with open <file >as <variable>:    used to automatically close the file when out
    .close()                      used to close the file
    .read()                       used to read whole file
    .readline()                   used to read and return a single line
    .readlines()                  used to read and get multiple lines in a list
    .writeline()                  used to write a single line
    .writelines()                 used to write multiple lines with new line character (\n)
    .flush()                      to ensure the data is saved

Binary: (import pickle)
    .dump()                       used to convert txt to dat 
    .load()                       used to convert dat to txt

csv: (import csv)
    f=open("<file name>","r")      #open first before reader
    .reader(f)                     used to read whole CSV file
    .writer(f)                     used as writer
    .writerow(row)                 used to write a single row or column name
    .writerows(list_row)           used to write multiple rows using nested list

Modes:
    -> r        read txt files
    -> rb       read binary files (.bat)
    -> r+       read and writes a files
    -> w        creates or writes files
    -> w+       writing and reading the file
    -> w+       writing and reading binary files
    -> a        appends the data in end of the file
    -> a+       creates or appends the data in the file
    -> ab+      creates or appends the data in the binary file

"""
# Functions, error handling & Importing
"""
Importing:
    import <module>                     used to import whole module
    from <module> import <function>     used to import specific functions from the module
    <module/function> as <var>          used to give aliases name to the module or functions

Functions:
    fnc_name = keep any function name you want

        def <fnc_name>(parameters):      used to define any function with parameters
        <fnc_name>(arguments)            used to Call Your Function with arguements

        return a                         used to return a single line value
        return a,b                       used to return multiple values i tuple

    from <filename> import <function>    Used to import functions from a specific file 
    from file import <function> as <var> used to give aliases name to the module or functions
    from file import fnc1, fnc2 , fnc3   used to import multiple functions

Error Handling:
    We can reduce Most of the errors by error handling one of the common error handlers are try/except

    try:
        ur code block                   # try executing code
    except <error>:
        do the necessary things          # if "try" code causes error instead of raising it do this code

    Note : if you don't specify <error> in except then it will consider all errors for it
"""

print("=============  Learnt by project  ===============")  # Things Learnt From Project
"""
    => For God Sake don't hesitate to use multi line strings

    => Colored Text ( from termcolor import colored, cprint )

    => invoking terminal for color text to work in terminal ()
        from os import system
        system("")

    => carriage return (\r) with end=""
        carriage return is good in certain scenarios but makes problem in terminal (output mode completely fine)
        when the replacing string is shorter than exsisting string

    => os.system("cls") invoke terminal commands which can help to clear screen after a fnc completed
"""

# LIST
"""
Methods:
    .append                        to add item in the list at the end of the list
    .extend                        to add multiple values
    .insert(1, "chocolate")        to add a value at a specific position
    .pop(INX)                      to remove value using index value
    .remove("anything")            to remove a value using value itself
    .clear()                       to clear list
    .sort()                        to sort the list
    .reverse()                     to reverse the list order
    .copy()                        to copy original list to new list
    .del()                         to delete whole list
 list(my_list)                     is also used to copy original list
"""

# TUPLES
"""
Methods:
    tuple(list)     to convert list to tuple
    .count()        to count the value
    .index()        to give the index of the value

--> Note :  We can concatenate tuples other operations are not allowed

    tuple is an immutable object...it takes less space than list and also less time to run.
    tuple helps us when handling large data bases by python
"""
my_tuple = tuple([9, "Damodaran street", "kellys", "chennai", 6, 0, 0, 0, 1, 0])
print(my_tuple[1:3])
print(my_tuple[0:6:2])
print(my_tuple[::2])
print(my_tuple.count("kellys"))
print(my_tuple.index(0))

# Dictionary
"""
Methods:
    dict(my_dict)                          Function to create dictionaries, also Used for copying
    my_dict["email"] = "ABc@xYZ.com"       to add new values to dictionary and also to overwrite existing values
    del my_dict["name"]                    to delete existing values
    my_dict.pop("age")                     to delete existing values too
    dic1.update(dic2)                      to Concatenate 2 dictionaries
    .keys()                                to get all the keys in dictionary
    .values()                              to get all the Values in dictionary
    .items()                               to get all the Items in dictionary
    .copy()                                to copy dictionaries
    .update                                to add dictionaries dictionaries
    
"""
my_dict = {"name": "harsh", "age": 16, "area": "kellys", "city": "chennai", "country": "India"}
print(my_dict)
print(my_dict["area"])
"""
    -------------------------------------------------|  looping values in dictionaries
    for values in my_dict.values():                  |  values are stored
        print(values)                                |  
    for keys in my_dict.keys():                      |  looping values in dictionaries
        print(keys)                                  |  keys are the object in which values are stored
    for key, values in my_dict.items():              |  
        print(key, ":", values)                      |  key and values are used with .items to loop
    -------------------------------------------------|  
    ____________________________________________________________________________________________________________
    try:                              |
        if statement                  |  to check whether the value is stored in dictionary or not
    except:                           | 
        else statement                |
    __________________________________|_________________________________________________________________________
"""
my_dict = {"name": "harsh", "age": 16, "area": "kellys", "city": "chennai", "country": "India"}
my_dict_2 = {"gender": "male", "lastname": "patel"}

# MERGING DICTIONARIES
my_dict.update(my_dict_2)
print(my_dict)
print(my_dict_2)

my_dict_3 = {3: 9, 4: 16, 5: 25}
print(my_dict_3[3])  # To Call out a value u cannot use index values u should use the key

# SETS
"""
    {}                                to make sets no repeating of characters is allowed here.
    set(["hello"])                    is also used to make null sets
    .add()                            to add something
    .discard()                        to remove something
    .clear()                          to clear the set characters
    set1.union(set2)                  to combine two sets
    set1.intersection(set2)           to get the common between two sets
    set1.difference(set2)             to get difference between the sets 
    set1.issuperset(set2)             to check it is a super set or not 
    set1.issubset(set2)               to check it is a sub set or not
"""
my_set = {"hello", "how", "are", "you"}
my_set2 = set("hello")
print(my_set, my_set2)

my_set3 = {1, 2, 3, 4, 6, 7}
for i in my_set3:
    print(i)

# ! ===================================== STRINGS
"""
    .split("")                         to split the string 
    ' '.join("")                       to join elements of a string (concatenate)
    %s/d/f                             s represents string format/d represents integer format/frepresents float format
    .format()                          format method used with strings
    f"...{}..."                        f-strings method # Very efficiant method
"""
# STRING FORMAT METHOD WITH EXAMPLES

# ------ old formatting style ("  %s/d/f" %s/f/d) ----------

var = "Tom"
my_string1 = "the variable is %s" % var  # %s represents string
print(my_string1)

var = 3.76168
my_string2 = "the variable is %d" % var  # %d represents integer
print(my_string2)

my_string3 = "the variable is %f" % var  # %f represents Float Values
print(my_string3)

my_string4 = "the variable is %.2f" % var  # %.nf represents n Float Values to be considered
print(my_string4)

# new (not efficiant) Formatting Style [.format() method)]
var = 3.124567
var2 = 6.1193

my_string5 = "the variable is {}".format(var)
print(my_string5)

my_string6 = "the variable is {:.3f} and {}".format(var, var2)
print(my_string6)

# - new formating style (f-strings method)

var = 3.124567
var2 = 6.1193
my_string7 = f"the variable is {var:.2f} and {var2}"
print(my_string7)

# /////////////////////////////////// Collections \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ------------------- Counter ------------
from collections import Counter

a = 'aaaaaabbbbbbbbbbbbbbbbcccccccccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))  # here 1 represents no. of most common elements
print(list(my_counter.elements()))

# ------------- Namedtuple ------
from collections import namedtuple

point1 = namedtuple("point", "x,y")
pt = point1(34, -135)
print(pt)
print(pt.x, pt.y)

# ----------- deque ----------
from collections import deque

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.pop()
d.popleft()
d.clear()
d.extend([1, 6, 4, 3, 2, 9, 8, 7, 6, 5])
d.extendleft([23, 45, 65, 61])
n1 = 5
d.rotate(n1)  # This will rotate n elements right sied
# while rotating n can also be = -n for rotating left side
print(d)

# itertools did not learn

stop = timer()
print(stop - start)  # to check time
