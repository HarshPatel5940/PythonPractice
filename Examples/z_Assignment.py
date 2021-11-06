# Trial Running of Single programs
file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\poem.txt"

# Write a method/function DisplayWords() in Python to read lines from a text file POEM.TXT
# and display those words which are less than 4 characters.


def DisplayWords():
    file1 = open(file_path, "r")
    f = file1.read()
    words = f.split(" ")

    for w in words:
        if len(w) < 4:
            print(w)
    file1.close()

# Reading a file line by line from beginning is a common task. What if you want to read a file backward?
# This happens when you need to read log files. Write a program to read and display content of file from end to beginning.


def ReverseDisplay():
    file1 = open(file_path, "r")
    lines = file1.readlines()
    lines2 = lines[::-1]
    for line in lines2:
        print(line)

    file1.close()

# Write a function in Python to count and display the number of lines starting with alphabet ‘A’ present in a text file “LINES.TXT”
# An aeroplane is in the sky. Alphabets & numbers are allowed in password. The function should display the output as 3.


def StartingWithA():
    file1 = open(file_path, "r")
    lines = file1.readlines()

    for line in lines:
        if line[0].lower() == 'a':
            print(line)
    file1.close()

# Write a function Remove_Lowercase() that accepts two file names,
# and copies all lines that do not start with lowercase letter from the first file into the second file.


def Remove_Lowercase():
    file1 = input("input file name 1 :")
    file2 = input("input file name 2 :")
    file_1 = open(file1, 'r')
    lines = file_1.readlines()

    for line in lines:
        if line[0] != line[0].lower:
            file_2 = open(file2, "w")
            file_2.write(line)
            file_2.close()

    file_1.close()

# Write a user-defined function in Python that displays the number of lines starting with ‘H’ in the file Para.txt


def StartingWithH():
    file1 = open(file_path, "r")
    lines = file1.readlines()
    count = 0
    for line in lines:
        if line[0].lower() == 'h':
            count += 1
    file1.close()
    print("the number of lines starting with h is", count)


if __name__ == "__main__":    
    DisplayWords()
    print("=========================================")
    ReverseDisplay()
    print("=========================================")
    StartingWithA()
    print("=========================================")
    StartingWithH()
    print("=========================================")
    Remove_Lowercase()
