import pickle

file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\emp.dat"


def file_write(emp_no):
    file_2 = open(file_path, 'ab')
    n1 = 1
    while n1 <= emp_no:
        name1 = input("enter your name : ")
        try:
            salary = int(input("enter your Salary : "))
            l1 = {"Name": name1, "salary": salary}
            try:
                pickle.dump(l1, file_2)
            except EOFError:
                file_2.close()
            n1 += 1
        except ValueError:
            print("There was ValueError pls enter again")


def file_find_same(sal):
    f1 = open(file_path, "rb")
    try:
        while True:
            data1 = pickle.load(f1)
            if data1["salary"] == sal:
                print("==> ", data1["Name"])
    except EOFError:
        f1.close()


def file_show():
    f1 = open(file_path, "rb")
    counter = 0
    try:
        while True:
            data1 = pickle.load(f1)
            counter += 1
            if data1["salary"] >= 0:

                print("==> ", data1["Name"], "-", data1["salary"])
    except EOFError:
        print(f"Number of people in DB are {counter}!!")
        f1.close()


while True:
    print("==================================== New Block ====================================\n")
    Ask_action = input("==> [r] = read\n=> [a]= write/append \nWhat do you want to do? [r] or [a] : ")

    if Ask_action.lower() == "a":
        try:
            temp_no = int(input("Number of employees data you want to enter : "))
            file_write(temp_no)
        except ValueError:
            print("There was ValueError pls enter again")

    elif Ask_action.lower() == "r":
        read_action = input("find by salary [fs] \nfind all [fa] \n What do you want to do? : ")
        if read_action.lower() == "fs":
            try:
                temp_sal = int(input("For Which salary u want find : "))
                file_find_same(temp_sal)
            except ValueError:
                print("There was a ValueError PLs enter a Valid Salary")
        elif read_action.lower() == "fa":
            file_show()
    else:
        print("Invalid Option")
        pass
    Ask_2 = input("Would you like to continue? [y] [n] : ")

    if Ask_2.lower() == "n":
        break
    elif Ask_2.lower() == "y":
        pass
    else:
        pass
