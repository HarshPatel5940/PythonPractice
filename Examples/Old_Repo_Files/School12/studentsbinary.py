import pickle

file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\student.dat"


def find_all():
    f1 = open(file_path, "rb")
    counter = 0
    print('======================================================\n')
    try:
        while True:
            data1 = pickle.load(f1)
            counter += 1
            if data1["marks"] >= 0:
                print(data1["roll_no"], '-', data1["name"], "-", data1["marks"])
    except EOFError:
        print(f"Number of students are **{counter}**")
        f1.close()


def find_by_roll_number(number1):
    f1 = open(file_path, "rb")
    print('======================================================\n')
    try:
        while True:
            data1 = pickle.load(f1)
            if data1["roll_no"] == number1:
                print(data1["roll_no"], '-', data1["name"], "-", data1["marks"])
    except EOFError:
        f1.close()


def find_by_name(name):
    f1 = open(file_path, "rb")
    print('======================================================\n')
    try:
        while True:
            data1 = pickle.load(f1)
            if data1["name"] == name:
                print(data1["roll_no"], '-', data1["name"], "-", data1["marks"])
    except EOFError:
        f1.close()


def find_by_marks(marks):
    f1 = open(file_path, "rb")
    print('======================================================\n')
    try:
        while True:
            data1 = pickle.load(f1)
            if data1["marks"] >= marks:
                print(data1["roll_no"], '-', data1["name"], "-", data1["marks"])
    except EOFError:
        f1.close()


def file_write(no):
    file = open(file_path, 'ab')
    n1 = 1
    while n1 <= no:
        print(f'Student {n1} \n')
        name1 = input("enter your name : ")
        try:
            roll_no = int(input("enter your roll_no : "))
            marks = int(input("enter your marks : "))
            l1 = {"roll_no": roll_no, "name": name1, "marks": marks}
            try:
                pickle.dump(l1, file)
            except EOFError:
                file.close()
            n1 += 1
        except ValueError:
            print("There was ValueError pls enter again")


while True:
    print("\n ===> NEW LOOP <==\n")
    Ask_action = input("==> [r] = read\n=> [w]= write\nWhat do you want to do? [r] or [a] : ")

    if Ask_action.lower() == "w":
        try:
            temp_no = int(input("Number of student data you want to enter : "))
            file_write(temp_no)
        except ValueError:
            print("There was ValueError pls enter again")

    elif Ask_action.lower() == "r":
        read_action = input("find by roll [r] \nfind by name [n] \nfind by marks [m] \nshow all[s] \n What do you want to do? : ")
        if read_action.lower() == "r":
            try:
                x = int(input("For Which salary u want find : "))
                find_by_roll_number(x)
            except ValueError:
                print("x = There was a ValueError")
        elif read_action.lower() == "n":
            try:
                x = int(input("For Which salary u want find : "))
                find_by_name(x)
            except ValueError:
                print("x = There was a ValueError")
        elif read_action.lower() == "m":
            try:
                x = int(input("For Which salary u want find : "))
                find_by_marks(x)
            except ValueError:
                print("x = There was a ValueError")
        elif read_action.lower() == "s":
            find_all()
        else:
            print("invalid option")
    else:
        print("Invalid Option")

    Ask_2 = input("Would you like to continue? [y] [n] : ")

    if Ask_2.lower() == "n":
        break
    elif Ask_2.lower() == "y":
        pass
    else:
        pass
