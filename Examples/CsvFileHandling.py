import csv

# NOTE FOR PROPER CSV EXAMPLE CHECKOUT https://github.com/HarshPatel5940/DataHandlingProject 

file_path = "data/student.csv"


def find_all():
    file1 = open(file_path, 'r')
    reader = csv.reader(file1)
    for row in reader:
        print(row)


def write_one():
    file1 = open(file_path, 'a', newline='')
    writer = csv.writer(file1)
    try:
        try:
            roll_no = int(input("enter students roll no : "))
            name = input("enter your name : ")
            marks = input("enter your marks : ")
            row = [roll_no, name, marks]
            writer.writerow(row)
            print("done")
        except ValueError:
            print("there was a value error")
    except EOFError:
        file1.close()


def write_many(count):
    file1 = open(file_path, 'a', newline='')
    writer = csv.writer(file1)
    n1 = 1
    try:
        while n1 <= count:
            print(f"student {n1}\n")
            roll_no = int(input("enter students roll no : "))
            name = input("enter your name : ")
            marks = input("enter your marks : ")
            row = [roll_no, name, marks]
            writer.writerow(row)
            print("done")
            n1 += 1
    except ValueError:
        print("There was a Value error")


while True:
    print("\n ===> NEW LOOP <==\n")
    Ask_action = input("==> [r] = read\n=> [w]= write\nWhat do you want to do? [r] or [a] : ")
    if Ask_action == 'r':
        find_all()
    elif Ask_action == 'w':
        ask1 = input(" do you want to enter one student [one] data or many? [many] ")
        if ask1 == 'many':
            try:
                num = int(input("input enter number of students u wanna enter : "))
                write_many(num)
            except ValueError:
                print("Value error try again")
        elif ask1 == 'one':
            write_one()
        else:
            print("invalid option")
    else:
        print("invalid option")

    Ask_2 = input("Would you like to continue? [y] [n] : ")
    if Ask_2.lower() == "n":
        break
    elif Ask_2.lower() == "y":
        pass
    else:
        pass

