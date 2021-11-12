# Assignment date: 11-11-2021
# Objective: To demonstrate the use of stacks with small list of options given below
# (i) selecting only those correctly entered entries where the first letters of the first name and last name are titled.
# (ii) selecting only the incorrectly entered names
# (iii) returning a list with corrected names.


def Menu():
    x = """
1. Push
2. Pop
3. Correct Entries
4. Wrong Entries
5. Changed Entries (Entries which are corrected) 
6. Exit
Enter your choice: """
    return x


def Push(stack, name):
    stack.append(name)
    print(f"{stack1[-1]} Has Been Added")


def Pop(stack):
    if len(stack) > 0:
        print(f"{stack[-1]} Has Been Removed")
        stack.pop()
    else:
        print("stack1 is empty. (UnderFlow)")


def CorrectEntries(stack):
    Correct = []
    if len(stack) > 0:
        for i in stack:
            if i == i.title():
                Correct.append(i)
        print(Correct, "# The Original Stack Has Been Updated")
    else:
        print("stack1 is Empty")


def WrongEntries(stack):
    Wrong = []
    if len(stack) > 0:
        for i in stack:
            if i != i.title():
                Wrong.append(i)
        print(Wrong)
    else:
        print("stack1 is Empty")


def ChangedEntries(stack):
    new_stack = []
    corrected = []
    if len(stack) > 0:
        for i in stack:
            if i == i.title():
                new_stack.append(i)
            else:
                corrected.append(i.title())
                new_stack.append(i.title())

        print(corrected)
        return new_stack
    else:
        print("stack1 is Empty")


def main():
    stack = []
    while True:
        choice = input(Menu())
        if choice == "1":
            name = input("Enter First and Last name: ")
            Push(stack, name)
        elif choice == "2":
            Pop(stack)
        elif choice == "3":
            CorrectEntries(stack)
        elif choice == "4":
            WrongEntries(stack)
        elif choice == "5":
            new_stack = ChangedEntries(stack)
            stack = list(new_stack)
        elif choice == "6":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
