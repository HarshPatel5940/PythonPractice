#Assigment of Variables
Name = []
ID = []
Dep = []
Desg = []
index = 0


#Details from The empolyees
while True :

    #Name
    name = input("Enter Employee's Full Name : ")
    Name.append(name)

    #ID
    id = int(input("Enter Employee's ID : "))
    ID.append(id)

    #Department
    dep = input("Enter Employee's Department : ")
    Dep.append(dep)

    #Designation
    desg = input("Enter Employee's Designation : ")
    Desg.append(desg)

    print("\nX---------------------------X\n")

    contin = input("Press 'e' to END Filling Details\n------------OR------------\nPress 'a' to ADD another Employee's Detail\n ")
    if contin == "e":
        break
    else:
        continue

#To Get the details
print(ID)
while True:
    print(" ")
    get_id = int(input("Enter the ID of the Employee to see his/her Details : "))
    if get_id in ID :
        index = ID.index(get_id)
        print("\nDetails of the Employee With ID :",get_id,'\n\n',"NAME :",Name[index],'\n',"ID :",get_id,'\n',"DEPARTMENT :",Dep[index],'\n',"DESIGNATION :",Desg[index],'\n\nX--------------------X\n')
        contin = input("Press 'y' to get the detail of another Employee\n\nOR\n\nPress 'e' to End ")
        if contin == 'e':
            break
        else:
            continue
    else:
        print("-------Access Denied!!!-------\nEnter The Correct ID again")
        continue
# SALARY 


