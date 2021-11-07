# data

admin_id = 59406171
admin_pass = 'Sms2021'
re_test = 'y'
register ={}
marks_1 ={}


#registration
while re_test =='y':
    score = 0
    #teacher verification
    check = input('are you a teacher or student: ')
    if check == 'teacher':
        verify1 = int(input('enter your id: '))
        verify2 = input('enter your pass: ')
        if verify1 == admin_id and verify2 == admin_pass:
            print('you have been verified and you have admin perms!')
        else:
            print('worng id or password')

    #student verification
    elif check == 'student':
        entry1 = input('enter your name: ')
        entry2 = input('enter your admission no: ')
        register[entry1] = entry2
        print('your name has been registered :)')
        
        confirm = input('enter "confirm" to start the test: ')
        #quiz
        if confirm == 'confirm':
            category = input('enter the category you want to write [science , maths , computer science] : ')
            
            #Science Quiz
            if category == 'science':
                print("----------------SCIENCE QUIZ----------------")
                q1 = input("Which is called as the building blocks of life?\na)blood b)mitochondria c)cell d)protoplasm\nYOUR ANSWER(a,b,c,d)--------")
                if q1 == 'c':
                    print("Correct Answer ------ You've been Awarded 5 Points !")
                    score += 5
                    print('your current score is:', score)
                else:
                    print("Ouch! Better Luck Next Time")
                q2 = input("What happens to pressure when we go down inside water?\na)Increases b)Decrease c)Remains Same d)none if the above\nYOUR ANSWER(a,b,c,d)--------")
                if q2 == 'a':
                    print("Correct Answer ------ You've been Awarded 5 Points !")
                    score += 5
                    print('your current score is:', score)
                else:
                    print("Ouch! Better Luck Next Time")
            
            #Maths Quiz
            elif category == 'maths':
                print("----------------MATHS QUIZ----------------")
                q1 = input("What is the sum of 4500 and 5000?\na)10000 b)9000 c)8500 d)9500\nYOUR ANSWER(a,b,c,d)--------")
                if q1 == 'd':
                    print("Correct Answer ------ You've been Awarded 5 Points !")
                    score += 5
                    print('your current score is:', score)
                else:
                    print("Ouch! Better Luck Next Time")
                q2 = input("What is the value of 30^3?\na)27000 b)9000 c)33 d)10\nYOUR ANSWER(a,b,c,d)--------")
                if q2 == 'a':
                    print("Correct Answer ------ You've been Awarded 5 Points !")
                    score += 5
                    print('your current score is:', score)
                else:
                    print("Ouch! Better Luck Next Time")

            #Computer Science Quiz
            elif category == 'computer science' or category == 'computerscience':
                print("----------------COMPUTER SCIENCE QUIZ----------------")
                q1 = input("How many bytes form one kilobyte?\na)1024 b)1014 c)1020 d)1008\nYOUR ANSWER(a,b,c,d)--------")
                if q1 == 'a':
                    print("Correct Answer ------ You've been Awarded 5 Points !")
                    score += 5
                    print('your current score is:', score)
                else:
                    print("Ouch! Better Luck Next Time")
                q2 = input("When was Python Created\na)1970s b)1980s c)1960s d)1990s \n YOUR ANSWER(a,b,c,d)--------")
                if q2 == 'b':
                    print("Correct Answer ------ You've been Awarded 5 Points !")
                    score += 5
                    print('your current score is:', score)
                else:
                    print("Ouch! Better Luck Next Time")

            marks_1[entry1] = score
            print("You've scored",score,"Points In",category,"Quiz")
    re_test = input('if you want to write test again type y or else type n: ')

if check == 'teacher':
    print(register)
    print(marks_1)
else:
    print('----------------------------TEST DONE----------------------------')


    