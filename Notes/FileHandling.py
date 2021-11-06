# File Handling

Note = \
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

print(Note)
